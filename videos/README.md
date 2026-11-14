# ManimGL videos with Achird narration

Scenes inherit from [NarratedScene](narrated_scene.py), which generates Google
Cloud Achird audio, caches it, and adds it to the ManimGL timeline. Each
narration block waits for its audio to finish before the next block starts.
The shared voice is `en-US-Chirp3-HD-Achird`, at the auditioned default pace
and 44,100 Hz. Its settings live in [speech.py](../narration/speech.py).

## Install and preview

Use the project's pinned Python through uv. On macOS, FFmpeg, Pango, pkgconf,
and a TeX installation with `latex` and `dvisvgm` are needed:

```sh
brew install ffmpeg pango pkgconf
uv sync --locked --group narration --group video
make -C videos preview
```

The preview imports the [approved Achird recording](../narration/achird-math-sample.wav)
into the cache and renders [AchirdDemo](achird_demo.py) offline. It makes no
Google API calls. The output is `videos/build/rendered/AchirdDemo.mp4`.

The project uses **3Blue1Brown's ManimGL**, pinned to an upstream commit in
`pyproject.toml` and `uv.lock`. PyAV is an explicit dependency because that
revision imports it without declaring it. The unchanged upstream
[animation guide and license](reference/README.md) are included locally.
Project conventions are in [AGENTS.md](AGENTS.md).

## Authenticate once for new narration

Cloud Text-to-Speech is already enabled in the selected Google project.
Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk)
if it is unavailable, then authenticate from the repository root:

```sh
gcloud auth application-default login
gcloud auth application-default set-quota-project YOUR_PROJECT_ID
```

Google stores these application credentials in your user configuration, outside
the repository. The SDK uses them automatically; an API key or service-account
JSON file is unnecessary for this local workflow. You can set
`GOOGLE_CLOUD_PROJECT` to choose a different quota project.

## Write a narrated scene

```python
from manimlib import Tex, Write

from videos.narrated_scene import NarratedScene


class Orthogonality(NarratedScene):
    def construct(self):
        equation = Tex(r"H H^{\mathsf{T}} = n I_n")
        with self.narrate(
            "H times H transpose equals n times the identity matrix."
        ) as audio:
            self.play(Write(equation), run_time=min(3, audio.duration))
```

Write spoken mathematics in the narration, and LaTeX in `Tex` objects. Use
separate narration blocks to synchronize different parts of an explanation.
Audio starts at the block's entry; any remaining narration plays before the
block exits. Animations that last longer keep their full duration.

Render a new scene from the repository root:

```sh
make -C videos render SOURCE=videos/orthogonality.py SCENE=Orthogonality
```

`render` writes 1080p at 30 fps; `render-4k` writes 4K at 30 fps. The Make
commands invoke `python -m manimlib`, ManimGL's module entry point, so project
imports resolve consistently. [custom_config.yml](../custom_config.yml)
controls the black background, fonts, output directory, and ManimGL caches.

Unchanged text and voice settings reuse cached WAVs. Set `NARRATION_OFFLINE=1`
when iterating on visuals to require cached audio. Google receives text only
when the cache lacks the requested narration. Longer text is split at paragraph,
sentence, or word boundaries below Google's per-request byte limit; completed
chunks survive a failed request. [Google's usage pricing](https://cloud.google.com/text-to-speech/pricing)
applies to new synthesis requests.

You can also generate audio independently:

```sh
uv run --locked --group narration python -m narration narration/achird-math-sample.txt --dry-run
uv run --locked --group narration python -m narration narration/achird-math-sample.txt --output narration/build/sample.wav
make -C videos check
```

Keep render output under `videos/build/`. Once a full node video is approved,
copy it to `website/media/<node-id>.mp4` and set that node's `video.src` and
actual `duration` in `website/nodes/<node-id>.md`. Parent previews use timed
cuts of the parent's video; measure those bounds from the finished render.
The audition scene is an example, and the website's unfinished video slots
remain available for the team's completed material.
