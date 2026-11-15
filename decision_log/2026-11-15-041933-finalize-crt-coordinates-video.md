# Finalize the Chinese Remainder Coordinates video

- Recorded at: 2026-11-15T04:19:33-08:00
- Observed work interval: 2026-11-15T04:18:34-08:00/2026-11-15T04:19:33-08:00 (final export inspection and metadata completion; follows the separate preparation interval).
- Participants: Tomas Ortega (finished-video and subtitle-space requirements); Steven Creech (editorial source); OpenAI Codex, GPT-6 (root rendering and delegated visual/metadata review).

## Context and decision

Complete the pending export outcome from the
[preparation record](2026-11-15-041037-prepare-crt-coordinates-video.md).
Publish the full [Video 3.1 export](../website/media/crt-coordinates.mp4)
with its exact-source captions and own-node video metadata. Keep the
source Markdown, accepted narration, and frozen animation unchanged.
This foundation node has no children, so no child cuts are introduced.

## Rationale

The final scene covers all three source slides: the residue dials,
coprime injectivity and equal finite counts, additive coordinates, and
preservation of coefficients, multiplication, inversion, star, and the
norm identity. Position labels in the 36-cell grid illustrate the
coordinate bijection; they are not a hypothetical Hadamard sign row.

## Evidence and outcome

Inspected eleven fresh resting frames at 21, 24, 27, 47, 58, 65, 75,
99, 110, 122, and 130 seconds. The examples show the correct residue
pairs for 1, 4, and 9; all grid positions are unique, and the highlighted
4+9=13 cells agree with coordinate addition. The same symbolic h_j stays
attached to the relabelled monomial. Multiplication, inversion, star,
and the transferred norm equation are readable, with no overlapping
labels, visible ghosts, clipping, or draft footer. A native crop also
confirms the complete final norm and defining relations.

The H.264 export is 1920 by 1080 at 30 fps, lasting 131.2 seconds and
covering its 131.180227-second take. Timing preflight reports 131.18
seconds and no late events. Root's full-export subtitle audit checked
all 3,936 frames in the lower 20 percent, with maximum encoded luma
16, black. The 33 exact-source caption cues and bounded CRT checks in
the preparation record remain valid. Recomputed editorial, narration,
and video hashes match; scene and shared-layout hashes are now recorded
in the [manifest](../videos/production/crt-coordinates.json), with final
production status. Own-node media paths and duration match this export.

Root owns combined project checks and the separate publication commit;
this record does not claim unobserved combined results or independent
human listening acceptance. The finite arithmetic checks validate the
illustration, while the general CRT argument remains the source proof.

## Report relevance

Records the observed completion of the refined-node teaching video,
measured subtitle clearance, and the preservation of sign data through
an explicit coordinate change. No order-36 Hadamard construction is
claimed or depicted.

## Final integration validation

Observed at 2026-11-15T04:42:07-08:00: all 20 narration and 32 video tests pass, including both actual-scene layout regressions and the three compiler regressions. All 183 website tests pass (9,076 assertions); the 50-page build and native player/caption links are current. Ruff, formatting, and whitespace checks pass. All 18 final editorial, narration, scene, layout, and media hashes match their production records. Root publishes each video separately; no further narration request was needed for visual corrections.
