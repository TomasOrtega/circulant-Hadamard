import hashlib
import io
import json
import math
import os
import tempfile
import wave
import xml.etree.ElementTree as ET
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CACHE = ROOT / "narration" / ".cache"
MAX_REQUEST_BYTES = 4500
GEMINI_REQUEST_BYTES = 4000
GEMINI_MODELS = ("gemini-2.5-flash-tts", "gemini-2.5-pro-tts")
GEMINI_PROMPT = (
    "Read this mathematics explanation in clear US English at a natural, brisk "
    "conversational pace, about 175 words per minute. Use ordinary sentence rhythm "
    "and short natural pauses. Speak only the supplied text. "
    "Use an even, matter-of-fact tone throughout."
)


@dataclass(frozen=True)
class Voice:
    name: str = "en-US-Chirp3-HD-Achird"
    language_code: str = "en-US"
    sample_rate: int = 44100
    speaking_rate: float = 1.0
    model_name: str = ""

    def __post_init__(self):
        if not math.isfinite(self.speaking_rate) or not 0.25 <= self.speaking_rate <= 2:
            raise ValueError("Speaking rate must be between 0.25 and 2.0.")
        if self.sample_rate <= 0:
            raise ValueError("Sample rate must be positive.")
        if self.model_name:
            if self.model_name not in GEMINI_MODELS:
                raise ValueError(f"Unsupported expressive model: {self.model_name}")
            if self.name != "Achird":
                raise ValueError("Gemini narration uses the short voice name Achird.")
            if self.speaking_rate != 1:
                raise ValueError("Gemini pacing is set by the shared narration prompt.")


@dataclass(frozen=True)
class AudioClip:
    path: Path
    duration: float


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
        self,
        *,
        cache_dir=DEFAULT_CACHE,
        voice=Voice(),
        project=None,
        offline=False,
        ssml=False,
    ):
        if ssml and voice.model_name:
            raise ValueError("SSML input requires a Chirp voice.")
        self.cache_dir = Path(cache_dir)
        self.voice = voice
        self.project = project or os.environ.get("GOOGLE_CLOUD_PROJECT")
        self.offline = offline
        self.ssml = ssml
        self._client = None

    def validate_text(self, text):
        text = text.strip()
        if not text:
            raise ValueError("Narration text is empty.")
        limit = GEMINI_REQUEST_BYTES if self.voice.model_name else MAX_REQUEST_BYTES
        if len(text.encode("utf-8")) > limit:
            raise ValueError(
                f"Narration must fit in one {limit}-byte request. "
                "Shorten the script or make separate videos."
            )
        if self.ssml:
            try:
                root = ET.fromstring(text)
            except ET.ParseError as error:
                raise ValueError("Narration SSML must be well-formed XML.") from error
            if root.tag.rsplit("}", 1)[-1] != "speak":
                raise ValueError("Narration SSML requires a <speak> root.")
            if not "".join(root.itertext()).strip():
                raise ValueError("Narration SSML contains no spoken text.")
            if any(
                element.tag.rsplit("}", 1)[-1] == "voice" for element in root.iter()
            ):
                raise ValueError(
                    "Narration SSML must keep the selected voice throughout."
                )
        if (
            self.voice.model_name
            and len(GEMINI_PROMPT.encode("utf-8")) > GEMINI_REQUEST_BYTES
        ):
            raise ValueError("Gemini delivery prompt exceeds the 4000-byte limit.")
        return text

    def cache_path(self, text):
        text = self.validate_text(text)
        voice = asdict(self.voice)
        if not self.voice.model_name:
            # Preserve the approved Chirp recording's existing cache identity.
            voice.pop("model_name")
        settings = {"version": 1, "text": text, "voice": voice}
        if self.voice.model_name or self.ssml:
            settings.update(
                version=2,
                provider="google-cloud-tts",
                input_kind="ssml" if self.ssml else "text",
            )
        if self.voice.model_name:
            settings["prompt"] = GEMINI_PROMPT
        digest = hashlib.sha256(
            json.dumps(settings, sort_keys=True).encode()
        ).hexdigest()
        return self.cache_dir / f"{digest}.wav"

    def import_audio(self, text, source):
        self.validate_text(text)
        return self._store_audio(text, Path(source).read_bytes())

    def _store_audio(self, text, data):
        frames = read_pcm(data, self.voice.sample_rate)
        target = self.cache_path(text)
        with atomic_output(target) as temporary:
            temporary.write_bytes(data)
        return AudioClip(target, len(frames) / (2 * self.voice.sample_rate))

    def audio(self, text):
        text = self.validate_text(text)
        target = self.cache_path(text)
        if target.is_file():
            frames = read_pcm(target.read_bytes(), self.voice.sample_rate)
            return AudioClip(target, len(frames) / (2 * self.voice.sample_rate))
        if self.offline:
            raise RuntimeError(
                "This narration is not cached. Generate it once with Google "
                "credentials, then use offline previews."
            )
        return self._store_audio(text, self._synthesize(text))

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
            voice = {"name": self.voice.name, "language_code": self.voice.language_code}
            audio_config = {
                "audio_encoding": texttospeech.AudioEncoding.LINEAR16,
                "sample_rate_hertz": self.voice.sample_rate,
            }
            if self.voice.model_name:
                voice["model_name"] = self.voice.model_name
            else:
                audio_config["speaking_rate"] = self.voice.speaking_rate
            synthesis_input = {"ssml" if self.ssml else "text": text}
            if self.voice.model_name:
                synthesis_input["prompt"] = GEMINI_PROMPT
            response = self._client.synthesize_speech(
                input=texttospeech.SynthesisInput(**synthesis_input),
                voice=texttospeech.VoiceSelectionParams(**voice),
                audio_config=texttospeech.AudioConfig(**audio_config),
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
