# Generate and cache Achird narration for Manim scenes

- Recorded at: 2026-11-14T15:44:31-08:00
- Observed work interval: 2026-11-14T15:19:39-08:00/2026-11-14T15:44:31-08:00 (24 minutes 52 seconds).
- Original decision times: unknown within the observed interval.
- Participants: Tomas Ortega (sample acceptance, programmatic setup, Manim requirements, project selection, and Google sign-in); Codex (GPT-6, implementation and verification); Google Cloud Chirp 3 HD (Achird synthesis).

## Context and decision

The user accepted the [Achird audition](2026-11-14-151823-audition-google-achird.md)
and requested programmatic narration for the videos. Add the
[speech module](../narration/speech.py), a text-to-WAV CLI, and a
[narrated scene base](../videos/narrated_scene.py). All scenes using this base
default to `en-US-Chirp3-HD-Achird`, US English, normal pace, and mono 16-bit
PCM at 44,100 Hz.

An initial Manim Community/Cairo integration was chosen for straightforward
local rendering. The user's subsequent clarification supersedes that choice
in the [ManimGL decision](2026-11-14-154431-use-manimgl-and-upstream-guidance.md).

## Rationale

Use Google's official Python SDK and Application Default Credentials, following
the [Cloud TTS quickstart](https://docs.cloud.google.com/text-to-speech/docs/create-audio-text-client-libraries).
The user selected the existing Google project and completed sign-in through
a temporary helper. Credentials remain in the user's Google Cloud configuration;
the quota project was verified without printing credentials. No billing upgrade,
API key creation, or service-account key was needed. The helper was syntax
checked, preserved its skill's library, and was removed after completion.

Hash text and voice settings to cache audio independently of animation edits.
Use atomic writes, validate PCM headers and frame lengths, and merge long
narration as PCM rather than concatenating WAV headers. Split text below
4,500 UTF-8 bytes per request; Google's
[documented limit](https://docs.cloud.google.com/text-to-speech/quotas)
is 5,000 bytes. Successful chunks survive a later request failure. Offline
previews require cached audio, and dry runs report missing requests.

The scene context adds audio at the current timeline position and waits for
any remaining speech. Longer animations retain their duration. The setup guide
explains spoken mathematics, rendering, and later placement of approved node
videos in the website.

## Evidence and outcome

Ten speech tests passed, covering actual SDK request objects with a mocked
transport, cache reuse, settings changes, Unicode limits, PCM merging, failure
recovery, imported recordings, and dry runs. Three scene tests passed, covering
timing and the displayed matrix identity; two exported-video checks also passed.
The narration tests were added to CI. Ruff and `uv run --locked prek -a --quiet`
passed using writable local cache locations.

The live SDK generated a new 71-character line as 4.720 seconds of Achird
audio. Repeating it with API access disabled reused the same cache entry.
The ADC quota project matched the selected project. The approved 403-character
recording also rendered successfully without new synthesis. Google Cloud CLI
593.0.0 was downloaded from Google's official archive into the ignored cache
and verified against its published SHA-256. Root Python 3.13 remained pinned.

## Report relevance

This is post-submission, AI-assisted video production infrastructure. Live API
verification is distinct from mocked tests and from the user's earlier voice
approval. The interval overlaps the ManimGL record and is not additive
person-hours. No new proof claim or completed proof video was published.
