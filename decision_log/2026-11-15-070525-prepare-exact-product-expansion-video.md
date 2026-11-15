# Prepare the exact product-expansion video

- Recorded at: 2026-11-15T07:05:25-08:00.
- Observed authoring span: 2026-11-15T07:00:27-08:00/2026-11-15T07:05:25-08:00
  (298 seconds, overlapping other video coordination and rendering waits).
- Participants: Tomas Ortega (continuing request); Steven Creech (editorial
  script); OpenAI Codex, GPT-6 (narration, animation and algebra checks).

## Context and decision

Produce a final video for [Node 7.2](../website/nodes/expand-integral-products.md)
following its complete [editorial script](../website/scripts/node7/expand-integral-products.md).
Continue the requested final-video production after the individually pushed
Node 6 videos. Freeze one complete default Achird narration in six paragraphs;
reuse it for every subsequent visual correction.

## Rationale

Make the order of operations visible: exact coefficientwise division,
evaluation, multiplication by the unit inverse of c. Introduce a and b as
the existing polynomial quotients; no inverse of 2 or 1+i is required.
Show the two families as 1+t x with their own x values. Use a four-cell
multiplication table for two factors, then group all eight three-factor
terms by the number of selected x values. Keep the quadratic and cubic
terms in an explicit t²Q; this is an exact expansion. Finally expand the
even and odd sides separately, keeping their sums and remainders distinct.
Only the one-factor case u=3 has no remainder on either side.

## Evidence and outcome

The accepted single recording is 203.180227 seconds. Unique exact-source
phrases provide measured internal cue times. The general-paragraph section
setup already introduces the identity, so its opening phrase does not add
a redundant detail wait. Actual full-scene TeX/timing preflight passes at
203.18 seconds with no late events; Ruff and formatting pass.

All 15,624 integer examples pass the exact expansion: zero through five
factors, each x from -2 through 2, and t in {-2,0,1,2}. The computation
supports the illustration, while the finite-choice argument supplies the
general identity. It is not a formal proof or Hadamard construction.
Native rendering, independent review, caption/band/hash verification and
repository acceptance remain before the separate commit and push.

## Report relevance

Documents production of an explanatory finite-product calculation already
present in the source, including the retained exact remainder and the
distinction between scalar divisibility and unit inverses.
