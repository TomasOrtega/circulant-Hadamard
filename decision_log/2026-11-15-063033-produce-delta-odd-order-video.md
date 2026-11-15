# Produce the odd-order video

- Recorded at: 2026-11-15T06:30:33-08:00.
- Observed production and review span:
  2026-11-15T06:16:57-08:00/2026-11-15T06:30:33-08:00 (816 seconds).
  This span includes coordination of other videos and an interruption;
  overlapping intervals are not additive person-hours.
- Participants: Tomas Ortega (continuing final-video request); Steven Creech
  (editorial source); OpenAI Codex, GPT-6 (narration, animation, rendering,
  mathematical checks and export review).

## Context and decision

Produce a final video from the [Node 4.6 script](../website/scripts/node4/delta-odd-order.md)
and its [refined exposition](2026-11-15-031809-develop-all-refined-node-exposition-and-scripts.md).
The [scene](../videos/delta_odd_order.py) uses one complete 2,619-byte,
462-word default Achird take, seven measured sections and 23 internal cues.
Preserve the editorial source and its mathematical status.

## Rationale

Split a root's order as $p^a m$ with $p\nmid m$. Raising the root to
$p^a$ leaves order $m$ and residue one. For $m>1$, derive the exact
vanishing geometric sum in the domain before reducing it. Its $m$ terms
then become ones, contradicting $p\nmid m$. The complex five-arrow polygon
is labelled as an illustration; the local residue calculation is separate.
Allow order one explicitly.

Apply the conclusion at every prime dividing odd $u>1$. Include the
nonzero finite-free cyclotomic ring argument ensuring that primes above
$p$ exist. Two distinct prime restrictions force order one; the one-prime
case permits nontrivial phase. For $u=3$, field degrees exclude ninth and
higher $3$-power roots, leaving $1,\omega,\omega^2$. The valid norm example
$f(P)=3iP$ gives $\omega^2$. Carry the three odd-order phases into Node 6
without assuming them equal.

## Evidence and outcome

- Strict actual-scene TeX/timing preflight passes at 179.400227 seconds
  with no late events; Ruff formatting and checks pass.
- Finite arithmetic checks cover 3,072 order splits for integers 1–512
  and primes $2,3,5,7,11,13$. Illustrative polygon closure error is below
  $2\times10^{-16}$. Degree checks for exponents 2–8 support the displayed
  exclusion. These computations illustrate the supplied general proof;
  they are not formal verification.
- Root reviewed ten native completed/intermediate frames, including the
  exact domain cancellation, residue contradiction, prime restrictions,
  field degrees and nonzero phase example. No layout or mathematical
  blocker was observed. Independent review follows separately.
- Final MP4: **5,898,056 bytes**, **179.433333 seconds**, H.264 1920×1080
  at 30 fps; AAC lasts 179.400998 seconds. All **5,383 frames** preserve a
  blank lower 20%, maximum limited-range luma **16**. No draft footer.
- Forty exact captions have at most two lines of 42 characters, minimum
  duration 2.12 seconds, no overlaps and bounded times. Alignment ratio
  0.9128 supports cue timing, without certifying a human listening review.
  Editorial, scene, layout, SSML and media hashes match. Final repository
  checks and the individual commit/push remain.

## Report relevance

Records explanatory production of the local root-order argument and its
application to the existing Delta theorem. No new research theorem or
formal proof of the conjecture is claimed.

## Final repository validation

Recorded at 2026-11-15T06:35:41-08:00. Root independent source and native-export review
accepts the final candidate. Repository checks pass: 20 narration tests,
38 video tests, 183 website tests with 9,220 assertions, and a 50-page
website build. Each video has its own staged lint check, commit and push.
An independent agent also accepts the source and ten native proof states
with no blockers, reviewed 2026-11-15T06:29:30-08:00/2026-11-15T06:30:34-08:00
(64 seconds, overlapping its other production work).
