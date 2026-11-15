# Finalize the exact product-expansion video

- Recorded at: 2026-11-15T07:13:23-08:00.
- Observed production span: 2026-11-15T07:00:27-08:00/2026-11-15T07:13:23-08:00
  (776 seconds, overlapping other production and render waits).
- Participants: Tomas Ortega (continuing request); Steven Creech (editorial
  script); OpenAI Codex, GPT-6 (production and independent review).

## Context and decision

Complete [the prepared video](2026-11-15-070525-prepare-exact-product-expansion-video.md)
as a final MP4 with exact-source captions for
[Node 7.2](../website/nodes/expand-integral-products.md). Preserve the source
mathematical draft status, one frozen default Achird recording and the empty
lower fifth of every frame.

## Rationale

Native export review found insufficient space between lower fractions and
the three pipeline box outlines. Add a regression using the actual constructed
scene and its label rectangles before changing the layout: five assertions
failed. Enlarge the boxes and separate their formula rows. A fresh export then
showed the external inverse label touching the enlarged middle box; extending
the same actual-scene regression reproduced that collision. Move the inverse
below the boxes. Both internal and external clearance now pass.

A second reviewer also requested the leading plus sign on the grouped t²Q
remainder so it remains visibly part of the stacked three-factor expansion.
Restore that notation without changing narration or mathematical content.

## Evidence and outcome

- The original internal-clearance regression failed five assertions in
  0.694 seconds; the external-clearance extension failed once in 0.766 seconds.
  The final combined actual-scene regression passes in 0.772 seconds. Logs
  remain under ignored `videos/build/expand-integral-products-*`.
- Final full actual-scene preflight passes at 203.18 seconds with no late
  events. All visual exports reuse the single 203.180227-second take.
- Final MP4: 6,688,775 bytes, H264 1920x1080 at 30 fps, 203.2 seconds;
  AAC duration 203.181474 seconds. All 6,096 frames pass the bottom-20% scan
  at maximum luma 16.
- All 46 exact-source captions fit two 42-character lines, last at least
  1.66 seconds, remain in bounds and do not overlap. ASR supports alignment
  and does not supply a human listening certification.
- Root accepted the native final states. Independent mathematical review
  accepted the two/three-factor expansions, family-dependent x/t values,
  exact retained remainder, distinct even/odd expansions and one-factor
  exception. Fresh final geometry and the plus sign were accepted at
  2026-11-15T07:13:10-08:00.
- Source/scene/layout/SSML/video hashes match. Repository checks pass:
  20 narration tests, 41 video tests, 183 website tests with 9,301 assertions,
  and all 50 node pages built. The individual commit and push follow.

## Report relevance

Records the final explanatory asset and observed layout corrections,
including failed-first tests of actual scene geometry. The integer
illustrations from the preparation record support the existing algebraic
argument and do not claim a new theorem or formal verification.
