# Publish the introduction video

- Recorded at: 2026-11-14T22:16:17-08:00
- Observed work interval: 2026-11-14T22:04:03-08:00/2026-11-14T22:16:17-08:00 (discovery, production, and validation through this record).
- Participants: Tomas Ortega (requested production and publication); OpenAI Codex, GPT-6 (scene, adaptation, integration, checks); Google Chirp 3 HD Achird (one synthesis request); faster-whisper Base English (local alignment).

## Context and decision

Complete the first video in the [requested queue](2026-11-14-220805-produce-scripted-node-videos.md).
The [introduction scene](../videos/overview.py) explains sign matrices,
orthogonality, cyclic shifts, and the eight-component proof route. Attach its
[finished MP4](../website/media/overview.mp4) and exact-source
[captions](../website/media/overview.vtt) to the homepage. Keep the supplied
editorial script intact and use the concise [spoken adaptation](../videos/scripts/overview.ssml).
The proposed-proof wording, draft footer, and two accepted inputs preserve
its exposition status without making a new claim of independent verification.

## Rationale

A shared scene helper supports consistent layout and exactly one full-script
narration block. The introduction is 3,546 UTF-8 bytes, within the one-request
limit, with SSML pauses at section boundaries. Measured cues and source/media
hashes are in the [production record](../videos/production/overview.json).
No clips are assigned to the two reading routes: neither has a production
script or a matching section in this introduction.

Update the website's existing integration checks to validate actual media
assets and configured players. Their previous assumption that every video
slot was empty is no longer true. No player or navigation implementation
change is needed.

## Evidence and outcome

The final H.264 export is 1920 by 1080, 30 fps, lasting 214.933333 seconds;
its AAC audio lasts 214.920998 seconds and covers the complete 214.920227-second
take. Fast-start metadata supports browser playback. Representative matrix,
shift, proof-graph, and conclusion frames were inspected.

Frame review found twelve temporary transform targets left over later scenes.
A regression failed with those twelve objects, then passed after explicit
cleanup. Each proof-graph step now uses yellow only for the current focus.
All 20 narration and 14 video tests pass, including that regression and
complete exported audio. All 66 website tests and the production build pass.
Captions are checked against the exact spoken source rather than ASR spelling.
The local transcript supports wording and cue alignment (match ratio 0.9313);
no separate human listening acceptance is claimed.

The initial frame-only command opened ManimGL's interactive mode; stop it and
use file-writing mode for unattended rendering. PyAV 19 rejects the ASR
library's decoder keyword, so decode to 16 kHz PCM with FFmpeg and supply the
sample array directly. Neither experiment changes the pinned runtime.
Generated WAVs, transcripts, diagnostic frames, and caches remain ignored.

## Report relevance

Records the first completed teaching video and its technical/visual validation,
with AI production, local recognition, and human approval kept distinct.
The mathematical content comes from the supplied scripts, not new research.
