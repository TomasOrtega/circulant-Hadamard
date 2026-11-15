# Publish the cyclic shifts video

- Recorded at: 2026-11-14T22:31:54-08:00
- Observed work interval: 2026-11-14T22:28:44-08:00/2026-11-14T22:31:54-08:00 (190 seconds; production and validation).
- Participants: Tomas Ortega (requested production and publication); OpenAI Codex, GPT-6 (scene, narration adaptation, integration, checks); Google Chirp 3 HD Achird (one full-script synthesis); faster-whisper Base English (local alignment).

## Context and decision

Continue the [scripted-video request](2026-11-14-220805-produce-scripted-node-videos.md).
Publish [cyclic-shifts.mp4](../website/media/cyclic-shifts.mp4), its exact-source
[captions](../website/media/cyclic-shifts.vtt), the reproducible
[scene](../videos/cyclic_shifts.py), and the [full SSML take](../videos/scripts/cyclic-shifts.ssml).
Attach the measured duration to its website node, preserving draft/foundation
status and the original [editorial script](../website/scripts/node1/cyclic-shifts.md).
Commit and push this video's changes separately as requested.

## Rationale

Animate a four-position coefficient strip while giving the arbitrary-n formula.
Preserve the original sign matrix. Show its row polynomials and explicitly
separate one-based row j (X to the j−1 times h) from zero-based row r and
column j (coefficient h at j−r modulo n). The displayed n=4 indexing example
r=2, j=1 gives h3=1 and matches the fixed matrix. The existing parent preview
remains a cut of Node 1, while this standalone video gives the general rule.

## Evidence and outcome

The export is H.264, 1920 by 1080 at 30 fps, 102.800000 seconds.
Its AAC track lasts 102.780998 seconds and covers the complete
102.780227-second narration. Fast-start metadata supports web
playback. Representative frames from each section were inspected. The
[production metadata](../videos/production/cyclic-shifts.json) records source, narration,
and video hashes and cues measured against this take. The local transcript
supports wording and timing (match ratio 0.9331); it is not
independent human listening acceptance. No human approval of this new take is
claimed. The selected voice and defaults match the approved project baseline.

All 20 narration tests, 16 video tests, 66 website tests, and the production
website build pass. Export checks require complete audio and 1080p at 30 fps;
caption text is checked against the spoken source. Generated WAVs, transcripts,
preview frames, and caches remain ignored. Repository lint and whitespace checks
are run before committing, with the conventional commit and AI trailer.

## Report relevance

Records AI-assisted production of supplied mathematical exposition, its actual
media timings, and technical and visual checks. This adds no new theorem or
independent verification of the overall proof.
