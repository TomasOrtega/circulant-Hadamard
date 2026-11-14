import hashlib
import io
import json
import math
import os
import re
import tempfile
import wave
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CACHE = ROOT / "narration" / ".cache"
MAX_REQUEST_BYTES = 4500


@dataclass(frozen=True)
class Voice:
    name: str = "en-US-Chirp3-HD-Achird"
    language_code: str = "en-US"
    sample_rate: int = 44100
    speaking_rate: float = 1.0

    def __post_init__(self):
        if not math.isfinite(self.speaking_rate) or not 0.25 <= self.speaking_rate <= 2:
            raise ValueError("Speaking rate must be between 0.25 and 2.0.")
        if self.sample_rate <= 0:
            raise ValueError("Sample rate must be positive.")


@dataclass(frozen=True)
class AudioClip:
    path: Path
    duration: float


def split_text(text, limit=MAX_REQUEST_BYTES):
    remaining = text.strip()
    if not remaining:
        raise ValueError("Narration text is empty.")
    chunks = []
    while len(remaining.encode("utf-8")) > limit:
        prefix = remaining.encode("utf-8")[:limit].decode("utf-8", errors="ignore")
        boundaries = (
            list(re.finditer(r"\n\s*\n", prefix))
            or list(re.finditer(r"(?<=[.!?])\s+", prefix))
            or list(re.finditer(r"\s+", prefix))
        )
        if not boundaries:
            raise ValueError(f"A narration word exceeds the {limit}-byte limit.")
        end = boundaries[-1].start()
        chunks.append(remaining[:end].strip())
        remaining = remaining[end:].lstrip()
    chunks.append(remaining)
    return chunks


@contextmanager
def atomic_output(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, filename = tempfile.mkstemp(suffix=path.suffix, dir=path.parent)
    os.close(descriptor)
    temporary = Path(filename)
    try:
        yield temporary
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def read_pcm(data, sample_rate):
    try:
        with wave.open(io.BytesIO(data), "rb") as audio:
            if (audio.getnchannels(), audio.getsampwidth(), audio.getframerate()) != (
                1,
                2,
                sample_rate,
            ):
                raise ValueError(
                    "Expected mono 16-bit PCM at the configured sample rate."
                )
            frames = audio.readframes(audio.getnframes())
            if not frames or len(frames) != 2 * audio.getnframes():
                raise ValueError("Narration WAV is empty or incomplete.")
            return frames
    except (wave.Error, EOFError) as error:
        raise ValueError("Narration response is not a valid PCM WAV.") from error


class Narrator:
    def __init__(
        self, *, cache_dir=DEFAULT_CACHE, voice=Voice(), project=None, offline=False
    ):
        self.cache_dir = Path(cache_dir)
        self.voice = voice
        self.project = project or os.environ.get("GOOGLE_CLOUD_PROJECT")
        self.offline = offline
        self._client = None

    def cache_path(self, text):
        settings = {"version": 1, "text": text.strip(), "voice": asdict(self.voice)}
        digest = hashlib.sha256(
            json.dumps(settings, sort_keys=True).encode()
        ).hexdigest()
        return self.cache_dir / f"{digest}.wav"

    def import_audio(self, text, source):
        split_text(text)
        return self._store_audio(text, Path(source).read_bytes())

    def _store_audio(self, text, data):
        frames = read_pcm(data, self.voice.sample_rate)
        target = self.cache_path(text)
        with atomic_output(target) as temporary:
            temporary.write_bytes(data)
        return AudioClip(target, len(frames) / (2 * self.voice.sample_rate))

    def audio(self, text):
        chunks = split_text(text)
        target = self.cache_path(text)
        if target.is_file():
            frames = read_pcm(target.read_bytes(), self.voice.sample_rate)
            return AudioClip(target, len(frames) / (2 * self.voice.sample_rate))
        if self.offline:
            raise RuntimeError(
                "This narration is not cached. Generate it once with Google "
                "credentials, then use offline previews."
            )
        if len(chunks) == 1:
            data = self._synthesize(chunks[0])
            return self._store_audio(text, data)
        parts = [self.audio(chunk) for chunk in chunks]
        with (
            atomic_output(target) as temporary,
            wave.open(str(temporary), "wb") as output,
        ):
            output.setnchannels(1)
            output.setsampwidth(2)
            output.setframerate(self.voice.sample_rate)
            for part in parts:
                frames = read_pcm(part.path.read_bytes(), self.voice.sample_rate)
                output.writeframesraw(frames)
        return AudioClip(target, sum(part.duration for part in parts))

    def _synthesize(self, text):
        try:
            from google.api_core.exceptions import GoogleAPICallError
            from google.auth.exceptions import DefaultCredentialsError
            from google.cloud import texttospeech
        except ImportError as error:
            raise RuntimeError(
                "Install speech dependencies: uv sync --group narration"
            ) from error
        try:
            if self._client is None:
                options = {"quota_project_id": self.project} if self.project else None
                self._client = texttospeech.TextToSpeechClient(client_options=options)
            response = self._client.synthesize_speech(
                input=texttospeech.SynthesisInput(text=text),
                voice=texttospeech.VoiceSelectionParams(
                    name=self.voice.name, language_code=self.voice.language_code
                ),
                audio_config=texttospeech.AudioConfig(
                    audio_encoding=texttospeech.AudioEncoding.LINEAR16,
                    sample_rate_hertz=self.voice.sample_rate,
                    speaking_rate=self.voice.speaking_rate,
                ),
                retry=None,
                timeout=120,
            )
            return response.audio_content
        except DefaultCredentialsError as error:
            raise RuntimeError(
                "Google sign-in is missing. Run gcloud auth application-default login, "
                "then gcloud auth application-default set-quota-project "
                "YOUR_PROJECT_ID."
            ) from error
        except GoogleAPICallError as error:
            raise RuntimeError(f"Google speech synthesis failed: {error}") from error
