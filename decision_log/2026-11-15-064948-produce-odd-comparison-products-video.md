# Produce the odd comparison-products video

- Recorded at: 2026-11-15T06:49:48-08:00
- Observed work interval: 2026-11-15T06:37:21-08:00/2026-11-15T06:49:48-08:00
  (747 seconds, including synthesis/render waits;
  overlaps other videos).
- Participants: Tomas Ortega (standing final-video request); Steven Creech
  (editorial script); OpenAI Codex, GPT-6 (narration adaptation, scene,
  arithmetic, timing, and exported-frame review); Google Chirp 3 HD Achird
  (one complete take); local faster-whisper Base English (alignment).

## Context and decision

Produce final Video 6.1 from the unchanged
[four-slide script](../website/scripts/node6/odd-comparison-products.md),
following the [refined Node 5–6 exposition decision](2026-11-15-031546-develop-node-five-six-child-exposition.md).
Add the [scene](../videos/odd_comparison_products.py), one frozen
[SSML](../videos/scripts/odd-comparison-products.ssml), and measured
[production metadata](../videos/production/odd-comparison-products.json).
Root owns synthesis, GPU preflight/rendering, the
[MP4](../website/media/odd-comparison-products.mp4),
[captions](../website/media/odd-comparison-products.vtt), website integration,
final shared checks, and separate commit/push. Preserve editorial content,
mathematical draft metadata, parents, and shared helpers.

## Rationale

Recall odd u greater than one, the three normalized norm identities, and
nonzero evaluations at all subset inputs. Regroup the Delta construction
into even-subset numerator factors and odd-subset denominator factors.
Label the odd-order Delta theorem as known input from Node 4. Use Delta(c)
as the reference for R and W, which are complex quotients of whole Delta
values rather than comparisons of individual polynomial coefficients.

Animate the general proof with positive odd exponents m and n: raise
alpha/beta to mn, regroup into the known powers, then replace numerator
and denominator by one. Its order divides odd mn; apply this to both
comparisons and explicitly include order one. This develops the supplied
comparison argument rather than reproving the Delta theorem.

For u = 3, preserve the orientation of each ratio of ratios: the relative
ratio at one is above the ratio at omega. Recall the three-candidate
restriction from Node 4; oddness alone is not presented as proof of that
restriction. Show closure of cubic roots under division and retain all
three candidates on a separate complex unit circle. State that these are
complex phases, with residue arithmetic still to come. Interpret R = 1
and W = 1 conditionally, without identifying the two relative ratios or
asserting that the three evaluated points coincide. The final scene leaves
the sign condition and rigidity as separate pending steps; it does not
prematurely conclude a common rotation or R = W = 1.

The 2,693-byte SSML fits one default Achird request. Seven paragraph cues
and 29 internal cues use unique exact-source phrases measured against the
single take, anticipating each phrase by 0.2 seconds. Copy targets enter
the body before their animations, and faded transients leave the registry.
Inherited framing reserves the bottom 20% without a footer.

## Evidence and outcome

- Exact Fraction phase arithmetic checks all 1,296 pairs of roots for
  m,n in {1,3,5,7,9,11}, with every exponent from zero through m−1 or n−1.
  Every quotient order divides mn and is odd, including order one. All
  nine quotients of cubic roots remain among the three candidates. These
  bounded illustrations support the displayed general power calculation;
  they are not formal verification or hypothetical Hadamard data.
- All 34 static and nine dynamic formula strings compile through the strict
  CPU TeX path. Numerator/bar and bar/denominator clearances exceed 0.33
  units; the lower omega label is horizontally separated from the result
  line by over 0.9 units. Scoped Ruff, formatting, and whitespace checks
  pass. Root's full strict scene preflight lasts 182.58 seconds and reports
  zero late events.
- Independently extracted and inspected native actual-export frames at
  16, 36, 42, 51, 70, 79, 83, 90, 94, 103, 132, 150, 154, 167, and
  181 seconds. These cover all seven sections, the alternating factors,
  exponent raising/regrouping/order argument, both oriented ratios,
  candidate-circle labels, and conditional ending. Tight native crops
  confirm the complete input and circle/set labels when broad previews
  drop glyphs. Mathematical expressions and geometry are clear. No
  post-render source fix or additional synthesis was needed.
- Independently probed the final H.264 export: 1920 by 1080 at 30 fps,
  5,478 frames, 182.6 seconds, 6,096,675 bytes. AAC lasts 182.580998
  seconds and covers the complete 182.580227-second take. Editorial, SSML,
  video, scene, and shared-layout hashes match the final manifest.
- Root's final all-frame scan checks all 5,478 frames: maximum luma 16
  in the lower 20% (black). This is separate from sampled visual review.
  The 43 exact-source captions have at most two 42-character lines,
  minimum duration 1.22 seconds, no overlap, and final end 181.26 seconds.
  ASR supports wording and timing checks; no independent human listening
  acceptance is asserted. Root performs the shared integration checks
  before the separate publication commit.

## Report relevance

Records a complete animated odd-exponent proof and comparison construction,
with theorem inputs and later sign conditions kept distinct, exact bounded
arithmetic, measured narration/captions, native export review, and full-frame
subtitle-space evidence. It preserves the distinction between complex
phases, arithmetic residues, and hypothetical norm-solution data.

## Independent export and repository acceptance

At 2026-11-15T07:00:38-08:00 root Codex accepted the final native MP4
frames after independently checking the scene against the editorial argument.
The final audit verifies source, scene, layout, SSML and video hashes, exact
captions, default Achird voice, audio coverage and 1080p30 H264/AAC. The full
checks passed: 20 narration tests and 39 video tests; website 183 tests with
9,265 assertions and 50 built node pages. All-frame bottom-20% scans pass
(maximum luma 16). Caption and ASR checks support timing; they are not a
human listening certification. The requested per-video commit/push follows.
