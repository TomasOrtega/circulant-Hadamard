# Prepare the final theorem video

- Recorded at: 2026-11-15T07:12:56-08:00.
- Observed work interval: 2026-11-15T07:10:43-08:00–2026-11-15T07:12:56-08:00
  (133 seconds; overlaps other final-video production).
- Participants: user (continuous final-video request); Codex/GPT-6 (authoring);
  coordinating Codex/GPT-6 agent (narration and rendering).

## Context and decision

Produce the four slides of the [canonical theorem script](../website/scripts/node8/theorem.md)
and [matching exposition](../website/nodes/theorem.md) as the final
[Theorem scene](../videos/theorem.py). Preserve the editorial Markdown,
source draft proof status, and reliance on the stated earlier inputs. Follow
the [Node 7–8 exposition decision](2026-11-15-025408-complete-node-seven-eight-child-exposition-and-scripts.md)
and the earlier [overview production](2026-11-15-033824-produce-final-contradiction-video.md).

The coordinating agent accepted the frozen [SSML](../videos/scripts/theorem.ssml)
before synthesis: one complete default Achird take, 1,946 UTF-8 bytes and
306 spoken words. Its paragraph keys are `conclusion`, `restriction`, `one`,
and `four`. Add 21 unique exact-source detail phrases for later measured
alignment; placeholders are not estimated publication timings.

## Rationale

Keep both directions visible as separate tasks at the start. For necessity,
pass `n>1` through the earlier odd square-order restriction and general
contradiction, leaving `u=1` and `n=4`. Give `n=1` a separate path because it
lies outside the restriction's hypothesis.

For existence, show the actual one-entry matrix fixed by cyclic shifting
and its Gram identity. Construct the order-four matrix by copying each
coefficient into its cyclic right-shifted position. Compare two real rows,
mark their two agreements and two disagreements, and transform the actual
dot product to zero. Then fill the Gram diagonal with fours and the other
entries with zeros. Register every copy target in the owned body first.

Return to the theorem only after both examples. Explain that `n=4` has
`u=1`, outside the Delta theorem's hypothesis `u>1`; the exception is
consistent with the preceding contradiction. The final narration explicitly
uses the earlier stated inputs rather than claiming independent verification.

## Evidence and outcome

- Python compilation and scoped Ruff checks pass. CPU LaTeX compilation
  passes for all 16 literal formula expressions; actual Manim construction
  and layout inspection remain the coordinating agent's next checks.
- All 21 phrase anchors occur uniquely in the frozen narration.
- Exact integer calculations verify every one of the 16 entries of the
  order-four Gram matrix. Each of the six distinct row pairs has exactly two
  agreements and two disagreements. All three consecutive right shifts and
  the order-one identity pass. These are complete checks of these finite
  examples, not a formal verification of the exclusion theorem.
- The scene reserves the lower caption band through the existing shared
  layout. Speech, measured timing, native-frame review, captions, and the
  final all-frame band scan are still pending.

## Report relevance

Records the measured AI-assisted authoring interval and the explicit
necessity/existence distinction at the end of the supplied proof chain.
No new research theorem, external mathematical review, or human listening
acceptance is asserted.
