# Finalize the residue-one ratios video

- Recorded at: 2026-11-15T06:55:10-08:00.
- Observed production span:
  2026-11-15T06:35:20-08:00/2026-11-15T06:55:10-08:00 (1,190 seconds,
  including root production, preflight revisions, and waiting).
- Observed author export-review interval:
  2026-11-15T06:54:30-08:00/2026-11-15T06:55:10-08:00 (40 seconds).
  These intervals overlap and are not additive person-hours.
- Participants: Tomas Ortega (continuing final-video request); Steven Creech
  (editorial source); OpenAI Codex, GPT-6 (child narration, animation,
  arithmetic checks, and author review; root synthesis/alignment, full
  construction/preflight, rendering, and full-frame caption-band scan).

## Context and decision

Accept the author's final [Sign Ratio Congruences export](../website/media/sign-ratio-congruences.mp4),
following the [preparation](2026-11-15-064125-prepare-sign-ratio-congruences-video.md),
[joined-TeX separator correction](2026-11-15-064346-separate-joined-tex-control-word.md),
and [ordinary-parenthesis correction](2026-11-15-064618-use-ordinary-reduction-parentheses.md).
Use canonical source number 6.3 and preserve the editorial script and the
single complete narration take. Neither preflight correction changes the
mathematics, audio, or cue times.

## Mathematical and visual scope

The scene carries already-integral polynomial identities through evaluation,
keeps c_S invertible in A=B[1/u], and cites the preceding node for the
nonzero reduction ring. It displays c_S's explicit inverse, rewrites ratios
minus one over that denominator, and shows 2=−i(1+i) squared. The entire
equation acquires the reduction map pi before its right factors become zero.
This prevents the reduced equality from being read as an equality in A.

The inverse calculation applies to either ratio. General products retain
their full subset bounds and even/odd roles, then become one-over-one only
after their labels change to pi(R) and pi(W). The conclusion is congruence
modulo 1+i. The u=3 two-input illustration and closing label explicitly
defer exact comparisons to odd-order rigidity. No general common rotation
or equality R=W=1 is asserted here.

## Evidence and outcome

- One frozen **2,808-byte**, **508-word** Achird take lasts
  **199.740227 seconds**. Three paragraph cues and **27** internal phrase
  cues drive the scene. ASR match is 0.9337; the collapsed subtraction-word
  interval and preceding measured denominator anchor remain documented in
  the manifest.
- Both typesetting failures were reproduced by full scene construction
  before their minimal fixes. The final actual-construction/timing
  preflight succeeds at **199.74 seconds** with **no late events**.
  Static Python/AST checks alone had not established compatibility with the
  TeX engine and Manim string parser. No mirrored string tests or new
  narration requests were added.
- Exact coefficient checks cover **all 16 sign columns**, without dividing
  by potentially zero coefficient values c. Four Gaussian unit inverses
  and 16 unit products preserve residue one, and the factorization of 2
  is exact. These finite illustrations support the displayed algebra;
  the general unit-ring argument is not claimed as formal verification.
- Inspected **22 native actual-export frames**: 26/50/58/65/70/73.07/84/87/
  96/105/115/120/121.5/131.17/140/151.4/155/160/163/170/190/198.766667.
  They cover exact quotient types, the common ring and unit inputs,
  evaluation, both ratio transformations, factor highlights, reduction
  labels, inverse proof, parity products, the boxed congruence, and the
  final example/handoff. No remaining mathematical, overlap, cleanup, or
  caption-space blocker was observed. PNGs are in ignored
  `videos/build/sign-ratio-congruences-final-<time>.png`.
- Final MP4: **6,945,812 bytes**, **199.766667 seconds**, H.264 1920×1080
  at 30 fps; AAC lasts **199.740998 seconds**. Root's terminal scan checks
  **all 5,993 frames**, with lower 20% maximum limited-range luma **16**.
  No draft footer appears.
- All **46** VTT cues exactly reproduce the frozen narration, at most two
  lines and 42 characters per line, minimum duration **1.88 seconds**,
  no overlaps, and bounded times. No human listening acceptance is claimed.
- Editorial, SSML, scene, shared-layout, and final-media hashes match the
  production manifest, marked final. Ruff, formatting, Python compilation,
  and scoped whitespace checks pass. Root retains independent review,
  full repository checks, website attachment, and the separate commit/push.

## Report relevance

Records final production of an existing proof node, explicit preservation
of the exact-division/unit prerequisites, measured alignment limits, two
real preflight repairs, and actual media/frame/caption evidence. No new
theorem or formal proof claim is introduced.

## Independent export and repository acceptance

At 2026-11-15T07:00:38-08:00 root Codex accepted the final native MP4
frames after independently checking the scene against the editorial argument.
The final audit verifies source, scene, layout, SSML and video hashes, exact
captions, default Achird voice, audio coverage and 1080p30 H264/AAC. The full
checks passed: 20 narration tests and 39 video tests; website 183 tests with
9,265 assertions and 50 built node pages. All-frame bottom-20% scans pass
(maximum luma 16). Caption and ASR checks support timing; they are not a
human listening certification. The requested per-video commit/push follows.
