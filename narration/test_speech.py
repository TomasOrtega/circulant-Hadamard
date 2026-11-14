import io
import struct
import tempfile
import unittest
import wave
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from narration.__main__ import main
from narration.speech import Narrator, Voice, read_pcm, split_text


def wav_bytes(value=1000, frames=100, sample_rate=44100):
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(sample_rate)
        output.writeframes(struct.pack("<h", value) * frames)
    return buffer.getvalue()


class SpeechTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.narrator = Narrator(cache_dir=self.root / "cache")

    def test_unicode_chunks_fit_the_byte_limit_and_preserve_words(self):
        text = ("Équation λ égale zéro. " * 1000).strip()
        chunks = split_text(text)
        self.assertTrue(all(len(chunk.encode("utf-8")) <= 4500 for chunk in chunks))
        self.assertEqual(" ".join(chunks).split(), text.split())
        self.assertGreater(len(chunks), 1)

    def test_unbreakable_word_and_empty_script_fail_before_synthesis(self):
        with self.assertRaises(ValueError):
            split_text("é" * 3000)
        with self.assertRaises(ValueError):
            split_text(" \n ")

    def test_google_request_uses_the_approved_voice_and_audio_settings(self):
        with patch("google.cloud.texttospeech.TextToSpeechClient") as factory:
            client = factory.return_value
            client.synthesize_speech.return_value.audio_content = wav_bytes()
            clip = self.narrator.audio("A circulant Hadamard matrix.")
        request = client.synthesize_speech.call_args.kwargs
        self.assertEqual(request["voice"].name, "en-US-Chirp3-HD-Achird")
        self.assertEqual(request["voice"].language_code, "en-US")
        self.assertEqual(request["audio_config"].sample_rate_hertz, 44100)
        self.assertEqual(request["audio_config"].speaking_rate, 1)
        self.assertGreater(clip.duration, 0)

    def test_cache_reuses_audio_without_google_credentials(self):
        with patch.object(
            self.narrator, "_synthesize", return_value=wav_bytes()
        ) as call:
            first = self.narrator.audio("One row, all shifts.")
            second = Narrator(cache_dir=self.root / "cache", offline=True).audio(
                "One row, all shifts."
            )
        call.assert_called_once()
        self.assertEqual(first, second)

    def test_voice_settings_change_the_cache_key(self):
        slower = Narrator(cache_dir=self.root / "cache", voice=Voice(speaking_rate=0.9))
        self.assertNotEqual(
            self.narrator.cache_path("Same script"), slower.cache_path("Same script")
        )

    def test_long_script_joins_pcm_without_embedded_wav_headers(self):
        text = "First " * 600 + ". " + "Second " * 600 + "."
        first = wav_bytes(1000, frames=100)
        second = wav_bytes(2000, frames=200)
        with patch.object(
            self.narrator, "_synthesize", side_effect=[first, second]
        ) as call:
            clip = self.narrator.audio(text)
        self.assertEqual(call.call_count, 2)
        self.assertAlmostEqual(clip.duration, 300 / 44100)
        self.assertEqual(
            read_pcm(clip.path.read_bytes(), 44100),
            read_pcm(first, 44100) + read_pcm(second, 44100),
        )

    def test_failed_request_preserves_completed_chunks_for_retry(self):
        text = "First " * 600 + ". " + "Second " * 600 + "."
        with patch.object(
            self.narrator,
            "_synthesize",
            side_effect=[wav_bytes(), RuntimeError("offline")],
        ):
            with self.assertRaises(RuntimeError):
                self.narrator.audio(text)
        self.assertFalse(self.narrator.cache_path(text).exists())
        with patch.object(
            self.narrator, "_synthesize", return_value=wav_bytes()
        ) as call:
            self.narrator.audio(text)
        call.assert_called_once()

    def test_invalid_audio_is_not_cached(self):
        with patch.object(self.narrator, "_synthesize", return_value=b"not a WAV"):
            with self.assertRaises(ValueError):
                self.narrator.audio("A short script.")
        self.assertFalse(self.narrator.cache_path("A short script.").exists())

    def test_imported_audio_supports_offline_previews(self):
        source = self.root / "approved.wav"
        source.write_bytes(wav_bytes())
        original = self.narrator.import_audio("Approved words.", source)
        offline = Narrator(cache_dir=self.root / "cache", offline=True)
        self.assertEqual(offline.audio("Approved words."), original)
        with self.assertRaises(RuntimeError):
            offline.audio("Changed words.")

    def test_dry_run_makes_no_requests_or_cache_files(self):
        script = self.root / "script.txt"
        script.write_text("A short script.")
        arguments = [
            "narration",
            str(script),
            "--dry-run",
            "--cache-dir",
            str(self.root / "cache"),
        ]
        with (
            patch("sys.argv", arguments),
            patch.object(Narrator, "_synthesize") as call,
        ):
            output = io.StringIO()
            with redirect_stdout(output):
                self.assertEqual(main(), 0)
        call.assert_not_called()
        self.assertIn("1 uncached request(s)", output.getvalue())
        self.assertFalse((self.root / "cache").exists())


if __name__ == "__main__":
    unittest.main()
