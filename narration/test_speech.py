import io
import struct
import tempfile
import unittest
import wave
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

from narration.__main__ import main
from narration.speech import Narrator, Voice


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

    def test_unicode_limit_counts_bytes_and_rejects_before_synthesis(self):
        for voice, limit in (
            (Voice(), 4500),
            (Voice(name="Achird", model_name="gemini-2.5-pro-tts"), 4000),
        ):
            narrator = Narrator(cache_dir=self.root, voice=voice)
            with (
                self.subTest(limit=limit),
                patch.object(narrator, "_synthesize", return_value=wav_bytes()) as call,
            ):
                narrator.audio("é" * (limit // 2))
                self.assertEqual(call.call_count, 1)
                with self.assertRaisesRegex(ValueError, "one.*request"):
                    narrator.audio("é" * (limit // 2 + 1))
                self.assertEqual(call.call_count, 1)

    def test_empty_script_fails_before_synthesis(self):
        with patch.object(self.narrator, "_synthesize") as call:
            with self.assertRaises(ValueError):
                self.narrator.audio(" \n ")
        call.assert_not_called()

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

    def test_ssml_uses_the_ssml_field_in_one_chirp_request(self):
        script = (
            '<speak>Multiply matching entries, then add.<break time="800ms"/>'
            "The sum is zero. Distinct rows are orthogonal.</speak>"
        )
        narrator = Narrator(cache_dir=self.root, ssml=True)
        with patch("google.cloud.texttospeech.TextToSpeechClient") as factory:
            client = factory.return_value
            client.synthesize_speech.return_value.audio_content = wav_bytes()
            narrator.audio(script)
        client.synthesize_speech.assert_called_once()
        request = client.synthesize_speech.call_args.kwargs
        self.assertEqual(request["input"].ssml, script)
        self.assertEqual(request["input"].text, "")
        self.assertEqual(request["input"].prompt, "")
        self.assertEqual(request["voice"].name, "en-US-Chirp3-HD-Achird")
        self.assertEqual(request["audio_config"].speaking_rate, 1)

    def test_ssml_cache_tracks_input_kind_and_pause_duration(self):
        script = '<speak>A sentence.<break time="800ms"/>Another sentence.</speak>'
        narrator = Narrator(cache_dir=self.root, ssml=True)
        self.assertNotEqual(
            narrator.cache_path(script), self.narrator.cache_path(script)
        )
        self.assertNotEqual(
            narrator.cache_path(script),
            narrator.cache_path(script.replace("800ms", "400ms")),
        )
        with patch.object(narrator, "_synthesize", return_value=wav_bytes()) as call:
            original = narrator.audio(script)
            cached = Narrator(cache_dir=self.root, ssml=True, offline=True).audio(
                script
            )
        call.assert_called_once()
        self.assertEqual(original, cached)

    def test_invalid_ssml_fails_before_google(self):
        narrator = Narrator(cache_dir=self.root, ssml=True)
        with patch("google.cloud.texttospeech.TextToSpeechClient") as factory:
            for script in (
                "<speak>Unclosed.",
                "<p>A wrong root.</p>",
                '<speak><break time="800ms"/></speak>',
                '<speak><voice name="another-voice">A different voice.</voice></speak>',
            ):
                with self.subTest(script=script), self.assertRaises(ValueError):
                    narrator.audio(script)
            with self.assertRaises(ValueError):
                Narrator(
                    voice=Voice(name="Achird", model_name="gemini-2.5-pro-tts"),
                    ssml=True,
                )
        factory.assert_not_called()

    def test_ssml_markup_counts_toward_the_request_limit(self):
        narrator = Narrator(cache_dir=self.root, ssml=True)
        script = "<speak>" + "a" * 4500 + "</speak>"
        with patch.object(narrator, "_synthesize") as call:
            with self.assertRaisesRegex(ValueError, "one 4500-byte request"):
                narrator.audio(script)
        call.assert_not_called()

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

    def test_oversized_script_is_rejected_instead_of_stitching_takes(self):
        for voice in (Voice(), Voice(name="Achird", model_name="gemini-2.5-pro-tts")):
            narrator = Narrator(cache_dir=self.root, voice=voice)
            with (
                self.subTest(model=voice.model_name),
                patch.object(narrator, "_synthesize", return_value=wav_bytes()) as call,
            ):
                with self.assertRaisesRegex(ValueError, "one.*request"):
                    narrator.audio("A sentence. " * 500)
                call.assert_not_called()

    def test_voice_settings_change_the_cache_key(self):
        slower = Narrator(cache_dir=self.root / "cache", voice=Voice(speaking_rate=0.9))
        self.assertNotEqual(
            self.narrator.cache_path("Same script"), slower.cache_path("Same script")
        )

    def test_gemini_sends_delivery_separately_from_spoken_text(self):
        narrator = Narrator(
            cache_dir=self.root,
            voice=Voice(name="Achird", model_name="gemini-2.5-flash-tts"),
        )
        with patch("google.cloud.texttospeech.TextToSpeechClient") as factory:
            client = factory.return_value
            client.synthesize_speech.return_value.audio_content = wav_bytes()
            narrator.audio("What happens to these two rows?")
        request = client.synthesize_speech.call_args.kwargs
        self.assertEqual(request["input"].text, "What happens to these two rows?")
        self.assertIn("matter-of-fact", request["input"].prompt)
        self.assertEqual(request["voice"].name, "Achird")
        self.assertEqual(request["voice"].model_name, "gemini-2.5-flash-tts")

    def test_gemini_cache_tracks_model_and_the_shared_prompt(self):
        narrator = Narrator(
            cache_dir=self.root,
            voice=Voice(name="Achird", model_name="gemini-2.5-flash-tts"),
        )
        pro = Narrator(
            cache_dir=self.root,
            voice=Voice(name="Achird", model_name="gemini-2.5-pro-tts"),
        )
        original = narrator.cache_path("The full script.")
        self.assertNotEqual(original, pro.cache_path("The full script."))
        with patch("narration.speech.GEMINI_PROMPT", "A different shared style."):
            self.assertNotEqual(original, narrator.cache_path("The full script."))

    def test_oversized_prompt_fails_before_google(self):
        narrator = Narrator(voice=Voice(name="Achird", model_name="gemini-2.5-pro-tts"))
        with (
            patch("google.cloud.texttospeech.TextToSpeechClient") as factory,
            patch("narration.speech.GEMINI_PROMPT", "é" * 2001),
        ):
            with self.assertRaises(ValueError):
                narrator.audio("The full script.")
        factory.assert_not_called()

    def test_existing_chirp_recording_keeps_its_cache_key(self):
        text = (Path(__file__).with_name("achird-math-sample.txt")).read_text()
        self.assertEqual(
            self.narrator.cache_path(text).name,
            "bcd5f76980e159be0b34728ec4358022a8b4bf19baccd01685e808c0c9096593.wav",
        )

    def test_full_script_is_one_request_and_a_failed_take_is_not_cached(self):
        text = "The first sentence. The second sentence. The main insight."
        with patch.object(
            self.narrator, "_synthesize", side_effect=RuntimeError("failed")
        ):
            with self.assertRaises(RuntimeError):
                self.narrator.audio(text)
        self.assertFalse(self.narrator.cache_path(text).exists())
        with patch.object(
            self.narrator, "_synthesize", return_value=wav_bytes()
        ) as call:
            self.narrator.audio(text)
        call.assert_called_once_with(text)

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

    def test_import_dry_run_reports_no_synthesis_request(self):
        script = self.root / "script.ssml"
        script.write_text("<speak>The approved recording.</speak>")
        recording = self.root / "approved.wav"
        recording.write_bytes(wav_bytes())
        with (
            redirect_stdout(io.StringIO()) as output,
            patch("google.cloud.texttospeech.TextToSpeechClient") as factory,
        ):
            self.assertEqual(
                main(
                    [
                        str(script),
                        "--ssml",
                        "--import-audio",
                        str(recording),
                        "--dry-run",
                        "--cache-dir",
                        str(self.root / "cache"),
                    ]
                ),
                0,
            )
        factory.assert_not_called()
        self.assertIn("0 uncached request(s)", output.getvalue())
        self.assertFalse((self.root / "cache").exists())

    def test_gemini_cli_rejects_oversized_script_without_google(self):
        script = self.root / "script.txt"
        script.write_text("é " * 1400)
        with (
            patch("google.cloud.texttospeech.TextToSpeechClient") as factory,
            redirect_stderr(io.StringIO()) as error,
        ):
            self.assertEqual(
                main(
                    [
                        str(script),
                        "--model",
                        "gemini-2.5-pro-tts",
                        "--dry-run",
                        "--cache-dir",
                        str(self.root / "cache"),
                    ]
                ),
                1,
            )
        factory.assert_not_called()
        self.assertIn("one 4000-byte request", error.getvalue())


if __name__ == "__main__":
    unittest.main()
