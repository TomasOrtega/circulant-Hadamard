# Produce the opposite-coefficient divisibility video

- Recorded at: 2026-11-15T05:21:34-08:00
- Observed work interval: 2026-11-15T04:57:28-08:00/2026-11-15T05:21:34-08:00
  (1,446 seconds, including synthesis, render, and regression-check waits;
  overlaps other video production).
- Participants: Tomas Ortega (standing final-video request); Steven Creech
  (editorial script); OpenAI Codex, GPT-6 (scene, narration adaptation,
  mathematical checks, regression, and frame review); Google Chirp 3 HD
  Achird (one complete take); local faster-whisper Base English (alignment).

## Context and decision

Produce final Video 2.4 from the unchanged
[five-slide script](../website/scripts/node2/cyclotomic-divisibility.md),
following the [refined-node decision](2026-11-15-031448-develop-node-two-and-three-refined-proofs-and-scripts.md).
Keep the specialized cyclotomic basis and valuation statement explicitly
labeled as the supplied Lemma 2.1 input. The video derives the required
opposite-coefficient consequence from that input; it does not claim to prove
the full general local lemma.

Add the [scene](../videos/cyclotomic_divisibility.py), frozen
[SSML](../videos/scripts/cyclotomic-divisibility.ssml),
[production record](../videos/production/cyclotomic-divisibility.json), and
[layout regression](../videos/test_cyclotomic_divisibility.py).
Root coordinates the final [video](../website/media/cyclotomic-divisibility.mp4),
[captions](../website/media/cyclotomic-divisibility.vtt), website integration,
and separate commit. No parent metadata or shared helper is changed here.

## Rationale

Show opposite cyclic positions with generic integer coefficients, explicitly
labeling the eight-position drawing as an illustration. Retain k≥1, integer
t≥0, odd w, and the cycle relation. Animate substitution into the basis,
valuation transferring divisibility to individual coefficients, the shifted
cyclotomic polynomial and unit relation, valuation of the norm, and equality
of the conjugate valuations. Pair opposite powers using ξ^D=−1, collect their
coefficient difference, and apply the supplied basis fact.

The order-16 illustration assumes signs only in that section. Reject the
nonzero sign differences, then swap two identical symbolic eight-entry halves
to show why the eighth shift repeats the row. The final section carries the
divisibility into the general descent with larger odd coefficients; folding
and averaging remain the next step. No hypothetical Hadamard row is invented.

The 3,267-byte SSML fits one default Achird request. Ten section cues and
40 internal cues follow measured source words, with phrase/index provenance.
All visual corrections reuse this complete take.

## Evidence and outcome

- Bounded integer checks cover all length-two and length-four coefficient
  lists in −3 through 3 having positive square scalar norm: respectively
  12 and 48 admissible lists satisfy opposite-coefficient divisibility.
  Shifted Eisenstein coefficients check for D=1,2,4,8,16,32,64. All 256
  sign rows formed by repeating an eight-entry half have dot product 16
  with their eighth shift. These illustrate the argument, not a proof of
  the general cyclotomic input or formal verification of the conjecture.
- Strict TeX preflight first rejected automatic delimiters; a fixed-size
  delimiter attempt also failed through the pinned Manim string parser.
  Compose the hypothesis from ordinary Tex pieces with sized parentheses,
  and use ordinary parentheses in three conjugate-valuation expressions.
  All 56 static formula strings and the composite hypothesis then compiled
  through the strict CPU TeX path. The full scene preflight passes with no
  late events and duration 228.04 seconds. No renderer or helper was altered.
- Reviewed ten native resting frames and nine intermediate states. This
  found the coefficient highlight touching adjacent math in the conclusion.
  Increase only that expression's inter-object spacing from 0.08 to 0.3.
  The actual-scene regression captures the displayed Tex and rectangle at
  the production `show` boundary, without duplicating coordinates. Restoring
  the old spacing failed both neighbor checks with gap −0.0500000763 in
  1.655 seconds; corrected spacing passed in 1.649 seconds. Logs remain in
  `videos/build/cyclotomic-divisibility-layout-red.log` and
  `videos/build/cyclotomic-divisibility-layout-green.log`. The final native
  coefficient crop independently confirms clear margins on both sides.
- Independently probed the final H.264 export: 1920 by 1080 at 30 fps,
  6,842 frames, 228.066667 seconds, 7,513,094 bytes. AAC lasts 228.040998
  seconds and covers the full 228.040227-second narration. Editorial, SSML,
  video, scene, and shared-layout hashes match the manifest.
- Root's final all-frame scan checks all 6,842 frames: maximum luma 16
  in the lower 20% (black). This automated evidence is separate from the
  sampled visual review. Exact-source captions have 51 cues, at most two
  42-character lines, minimum 1.7 seconds, no overlaps, final end 226.48
  seconds. ASR supports timing and wording review; no independent human
  listening acceptance is asserted.
- Shared validation observed by root at 2026-11-15T05:21:07-08:00 passes:
  20 narration tests, 34 video tests, 183 website tests with 9,112 assertions,
  and the 50-page build. Scoped Ruff and whitespace checks pass.

## Report relevance

Records production of a technical supplied-input argument, its animation
and timing choices, observed compiler and geometry corrections, demonstrated
regression failure and success, and the distinction between arithmetic
illustrations, source-level reasoning, and formal verification.
