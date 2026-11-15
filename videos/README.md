# ManimGL videos with Achird narration

Each scene uses one continuous recording of its complete script. Generate the
take first, then time the animations to it. Keep delivery natural and neutral,
with sparse emphasis on the main insight. Agent guidance is in [AGENTS.md](AGENTS.md).

The shared default is `en-US-Chirp3-HD-Achird` at normal pace and 44,100 Hz.
The demo uses the approved Chirp SSML take, with a break before the zero result.
Settings and caching live in [speech.py](../narration/speech.py).

## Install and preview

Use the project's pinned Python through uv. On macOS, FFmpeg, Pango, pkgconf,
and a TeX installation with `latex` and `dvisvgm` are needed:

```sh
brew install ffmpeg pango pkgconf
uv sync --locked --group narration --group video
make -C videos seed
make -C videos preview
```

`seed` imports the [approved recording](../narration/achird-demo.wav) for
[the full SSML script](../narration/achird-demo.ssml), writing
`narration/build/achird-demo-ssml.wav`. `preview` seeds the cache automatically
and renders offline to `videos/build/rendered/AchirdDemo.mp4`. This demo needs
no Google credentials or new synthesis; its accepted recording is versioned.
Keep the versioned WAV paired with the SSML that produced it.

The project uses **3Blue1Brown's ManimGL**, pinned to an upstream commit in
`pyproject.toml` and `uv.lock`. PyAV is explicit because that revision imports it
without declaring it. The unchanged upstream [animation guide and license](reference/README.md)
are included locally. The [original Chirp recording](../narration/achird-math-sample.wav)
and its [script](../narration/achird-math-sample.txt) remain the voice baseline.

## Website thumbnails

The website posters are selected frames from the published videos. They retain
the original Manim typography, colors, and mathematical illustrations. Reviewed
timestamps, selection reasons, and source-video hashes are recorded in
[thumbnail-selections.json](thumbnail-selections.json). Each existing excerpt
has a separate selection inside its playback bounds.

Regenerate the 1280-by-720 JPEGs using the existing video environment:

```sh
uv run --locked --group video python -m videos.thumbnails
```

To regenerate one video and its excerpts, append its node ID, for example
`signs-become-all-ones`. The script refuses a changed video hash: review a
completed frame in the new render and update its selections first. It writes
the final assets to `website/media/thumbnails/`; node `video.poster` and child
`segment.poster` metadata attach them to the players. Rebuild the website after
regenerating. Source videos, narration, and playback timings are untouched.

## Authenticate once for new narration

Cloud Text-to-Speech is already enabled in the selected Google project. Install
the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk), then:

```sh
gcloud auth application-default login
gcloud auth application-default set-quota-project YOUR_PROJECT_ID
```

Credentials stay in your Google configuration, outside this repository. Set
`GOOGLE_CLOUD_PROJECT` to select another quota project. Gemini also requires
`aiplatform.endpoints.predict`, normally through `roles/aiplatform.user`.

## Write and time a scene

```python
from manimlib import Tex, Write

from videos.narrated_scene import NarratedScene


class Orthogonality(NarratedScene):
    def construct(self):
        script = (
            "The rows are orthogonal. H times H transpose equals n times "
            "the identity matrix."
        )
        with self.narrate(script):
            self.play(Write(Tex(r"H H^{\mathsf{T}} = n I_n")), run_time=1)
            self.wait_until_narration(4.2)
```

Use exactly one `narrate(full_script)` block per scene. A second or nested call
raises an error before synthesis. Audio starts at block entry; the block waits
for remaining speech, and longer animations retain their duration.
`wait_until_narration(seconds)` waits until an offset from that same audio start.
It schedules visuals while the recording continues. Measure cue times from the
finished take, as in [AchirdDemo](achird_demo.py).

To opt into Gemini, set the scene's voice once:

```python
from narration.speech import Voice

narration_voice = Voice(name="Achird", model_name="gemini-2.5-pro-tts")
```

The complete script must fit one synthesis request: 4,500 UTF-8 bytes for Chirp,
4,000 for Gemini. Oversized scripts fail before an API call; shorten the scene
or make separate videos. Speech is never automatically split and stitched.
Gemini uses one style prompt for the whole take, documented by the
[Google TTS guide](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts).
Listen for clear wording and a consistent voice; automatic transcripts are only
supporting evidence.

## Render and check

```sh
make -C videos render SOURCE=videos/orthogonality.py SCENE=Orthogonality
make -C videos check
```

`render` writes 1080p at 30 fps; `render-4k` writes 4K at 30 fps. Commands use
`python -m manimlib` from the repository root so imports resolve consistently.
[custom_config.yml](../custom_config.yml) controls appearance and build directories.

Set `NARRATION_OFFLINE=1` when iterating on visuals. Cached takes are identified
by their complete script, voice, model, and style prompt; animation cue edits
reuse the same recording. Google receives the script and style prompt only when
that take is absent. [Google's usage pricing](https://cloud.google.com/text-to-speech/pricing)
applies to new synthesis.

The speech CLI also accepts full scripts:

```sh
uv run --locked --group narration python -m narration narration/achird-demo.ssml --ssml --dry-run
uv run --locked --group narration python -m narration narration/achird-demo.ssml --ssml --output narration/build/demo.wav
```

## Chirp SSML pauses

[achird-demo.ssml](../narration/achird-demo.ssml) uses the default Chirp Achird
voice and requests an 800 ms break before the zero result, in one continuous take.
To synthesize a new SSML recording when needed:

```sh
uv run --locked --group narration python -m narration narration/achird-demo.ssml --ssml --output narration/build/achird-demo-ssml.wav
```

`--ssml` sends the complete XML through `input.ssml`. SSML and plain text have
separate cache identities; changing a break duration generates a new take.
Malformed XML, empty scripts, and SSML voice changes fail before a request.
SSML is available for Chirp, and is rejected with `--model` Gemini options.
Google documents synchronous Chirp SSML as
[Preview](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd#chirp_3_hd_ssml_support).
Listen to changed narration before retiming the video. A scene using SSML
sets `narration_ssml = True` and passes the complete `<speak>` document to its
single `narrate()` block.

Keep generated video under `videos/build/`. After a full node video is approved,
copy it to `website/media/<node-id>.mp4` and set its `video.src` and actual
`duration` in `website/nodes/<node-id>.md`. Parent previews use measured cuts of
that finished video. The demo does not replace unfinished website video slots.

## Scripted node videos

Published node videos use the scenes listed in `production/<node-id>.json`.
Their complete, spoken mathematics scripts are in `scripts/<node-id>.ssml`;
the original editorial drafts remain in `website/scripts/`. The introduction
uses a concise adaptation so its narration fits one synthesis request.

For example, rebuild the introduction with:

```sh
make -C videos render SOURCE=videos/overview.py SCENE=Overview
```

Each scene uses one continuous Achird take. Production records contain the
source draft's SHA-256, measured cue offsets, and narration duration. Visual
iterations use `NARRATION_OFFLINE=1` to reuse that recording. A fresh checkout
needs Google credentials to synthesize a new take; its timing must be checked
again. The published MP4 preserves the finished recording.

Final 1080p, 30 fps MP4s and matching WebVTT captions live in `website/media/`.
Captions retain the exact spoken source text; local speech recognition helps
align them and the animation cues. [captions.py](captions.py) groups measured
words into at most two 42-character lines, avoiding flashing fragments.
Recognition is supporting evidence, not human listening acceptance.

Finished videos have no draft watermark. The camera reserves the bottom 20%
for subtitles, and export checks inspect this band. Mathematical assumptions
and accepted inputs remain explicit. Child previews use measured sections of
their parent's recording, and remain empty when that parent has no video.
