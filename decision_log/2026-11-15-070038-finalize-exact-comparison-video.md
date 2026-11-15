# Finalize the exact-comparison video

- Recorded at: 2026-11-15T07:00:38-08:00.
- Observed production span: 2026-11-15T06:30:04-08:00/2026-11-15T07:00:38-08:00
  (1,834 seconds, overlapping other video coordination and render waits).
- Participants: Tomas Ortega (continuing request); Steven Creech (editorial
  script); OpenAI Codex, GPT-6 (authoring, production and independent review).

## Context and decision

Complete [the preparation](2026-11-15-064351-prepare-exact-comparison-video.md)
as a final video for [Node 6.5](../website/nodes/exact-comparison-identities.md),
with one frozen complete default Achird recording and the inherited narration
block. Keep the source's mathematical draft status and reserve the lower 20%
for subtitles. Attach the final MP4 and exact-source captions to the node.

## Rationale

Keep general alternating product equalities separate from the common rotation
available for u=3. The forward multiplier is c(omega)/c(1)=Delta(c) inverse.
Apply it to the exact integral combination E, then normalize by the unit c;
E(1)=0 is allowed. Label the numerical illustration as schematic, and never
assign it all-ones residues or infer general pointwise rotation.

An initial timing preflight found a redundant paragraph-start detail wait
arriving two seconds late after its section setup. Remove that wait and its
metadata; the setup already introduces division by c. Preserve the recording
and measured timestamps for all other cues.

Add c/d/g labels to both circle diagrams to identify each arrow explicitly.
The first labeled export put g(1) on the circle outline. Before correcting
it, add an actual-scene geometry regression that captures both constructed
diagrams and checks the label rectangles against the circle outline. It
failed twice with the previous placement. Moving both g(1) labels above
their arrow tips passes the same regression without copied coordinates.

## Evidence and outcome

- The failed and passing regression logs are retained under ignored
  `videos/build/exact-comparison-identities-label-{red,green}.log`.
  The single regression passed in 1.360 seconds after the placement change.
- Full actual-scene TeX/timing preflight passes at 209.12 seconds with no
  late events. No renderer, upstream dependency or cache changes were needed.
- Final export is 7,314,913 bytes, H264 1920x1080 at 30 fps, 209.133333 seconds;
  its AAC stream covers the 209.120227-second accepted take.
- All 6,274 frames pass the bottom-20% scan (maximum luma 16). All 51 captions
  match the narration text, last at least 1.78 seconds, fit two 42-character
  lines, do not overlap and remain within the video.
- Root reviewed native final states, including both newly corrected diagrams.
  A second Codex reviewer accepted the mathematical scope and final geometry
  at 2026-11-15T06:59:15-08:00. The illustration gives E(1)=-3+3i and E/c=-1+i;
  exact rational Gaussian checks and three zero-E cases support the example,
  not a Hadamard construction or a formal proof.
- All five source/scene/layout/SSML/video hashes match the production manifest.
  Repository checks pass: 20 narration tests, 39 video tests, and 183 website
  tests with 9,265 assertions; all 50 node pages build.
- ASR and exact-source captions support alignment; they do not establish a
  human listening certification. The per-video commit and push follow.

## Report relevance

Documents a final explanatory video, its observed authoring correction and
failed-first geometry regression. It illustrates existing mathematics and
does not add a research result or change the proof status of the source.
