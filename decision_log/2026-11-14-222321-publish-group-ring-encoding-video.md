# Publish the group ring encoding video

- Recorded at: 2026-11-14T22:23:21-08:00
- Observed work interval: 2026-11-14T22:17:53-08:00/2026-11-14T22:23:21-08:00 (328 seconds; synthesis, rendering, integration, and validation; initial authoring preceded this measured interval).
- Participants: Tomas Ortega (requested production and publication); OpenAI Codex, GPT-6 (scene, narration adaptation, integration, checks); Google Chirp 3 HD Achird (one full-script synthesis); faster-whisper Base English (local alignment).

## Context and decision

Continue the [scripted-video request](2026-11-14-220805-produce-scripted-node-videos.md).
Publish [group-ring-encoding.mp4](../website/media/group-ring-encoding.mp4), its exact-source
[captions](../website/media/group-ring-encoding.vtt), the reproducible
[scene](../videos/group_ring_encoding.py), and the [full SSML take](../videos/scripts/group-ring-encoding.ssml).
Attach the measured duration to its website node, preserving draft/foundation
status and the original [editorial script](../website/scripts/node1/group-ring-encoding.md).
Commit and push this video's changes separately as requested.

## Rationale

Use the original row (-1,1,1,1), multiplication as a cyclic shift, generic
coefficient reversal, the four correlations, and both directions of the
dictionary. Include the supplied h=2 counterexample to make the sign hypothesis
explicit. The 3,019-byte spoken adaptation fits one synthesis request; visual
iterations reuse that cached take. Independent finite arithmetic checks agree
for all 126 sign rows of lengths 1–6 and arbitrary row pairs, and verify the
order-four example, 2I counterexample, and all-ones counterexample. These checks
support the numerical illustrations, not a proof of the conjecture.

Add five measured parent previews: Group Ring 16.51–45.89 seconds; Cyclic Shifts
45.89–69.27; Star 69.27–99.31; Correlation 99.31–135.35; Dictionary 135.35 to
the video's measured end. Child videos remain separate recordings. Colors use
the corrected shared helper described in the
[color correction](2026-11-14-222235-correct-video-emphasis-colors.md).

## Evidence and outcome

The export is H.264, 1920 by 1080 at 30 fps, 200.566667 seconds.
Its AAC track lasts 200.560998 seconds and covers the complete
200.560227-second narration. Fast-start metadata supports web
playback. Representative frames from each section were inspected. The
[production metadata](../videos/production/group-ring-encoding.json) records source, narration,
and video hashes and cues measured against this take. The local transcript
supports wording and timing (match ratio 0.9579); it is not
independent human listening acceptance. No human approval of this new take is
claimed. The selected voice and defaults match the approved project baseline.

All 20 narration tests, 15 video tests, 66 website tests, and the production
website build pass. Export checks require complete audio and 1080p at 30 fps;
caption text is checked against the spoken source. Generated WAVs, transcripts,
preview frames, and caches remain ignored. Repository lint and whitespace checks
are run before committing, with the conventional commit and AI trailer.

## Report relevance

Records AI-assisted production of supplied mathematical exposition, its actual
media timings, and technical and visual checks. This adds no new theorem or
independent verification of the overall proof.
