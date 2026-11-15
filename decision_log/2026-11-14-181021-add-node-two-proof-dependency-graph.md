# Add the Node 2 proof dependency graph

- Recorded at: 2026-11-14T18:10:21-08:00
- Observed work interval: 2026-11-14T18:03:10-08:00/2026-11-14T18:10:21-08:00 (431 seconds through this record).
- Participants: Steven Creech (graph-first request and example-led direction);
  OpenAI Codex, GPT-6 (implementation, delegated mathematical review and leaf
  outlines, validation, and preview).
- Mathematical review: 2026-11-14T18:03:50-08:00/2026-11-14T18:04:25-08:00
  (35 seconds). Leaf outlines: 2026-11-14T18:04:50-08:00/2026-11-14T18:06:25-08:00
  (95 seconds). These overlap the primary interval and are not additive hours.

## Context and decision

Steven requested Node 2's proof dependency graph first, followed later by
editing the main overview script before developing detailed scripts. He
expects more example-led exposition here. Implement the six-node outline
already developed in the
[Node 2 planning decision](2026-11-14-170130-polynomial-notation-and-node-two-outline.md).

The [Node 2 page](../website/nodes/restriction-on-the-order.md) now links:

1. Evaluate at 1: the order is a square.
2. Pair positive and negative dot-product terms: the order is even.
3. Project to a power-of-two cycle with odd coefficients.
4. Compare opposite coefficients using cyclotomic divisibility.
5. Fold the cycle, preserving odd coefficients.
6. Use odd squares modulo eight to conclude the power of two is exactly four.

The edges are 2.1→2.3, 2.2→2.3, 2.3→2.5, 2.4→2.5, and 2.5→2.6.
Keep 2.4 independent and iteration inside 2.5 rather than adding a graph loop.
Use the existing blue outlines and solid gray arrows.

## Rationale

Follow the [Node 1 subsection layout](2026-11-14-172603-put-node-exposition-in-child-sections.md):
video, graph, then each step's explanation. The main-page card states the
order-restriction lemma. Add six concise child pages with statements and
examples; defer the technical proofs and all deeper production scripts.
Keep the two elementary nodes terminal foundations. Retain Proposition 2.2
as an accepted input at the main level and explicitly label Lemma 2.1 at 2.4.

The independent divisibility statement applies to arbitrary integer coefficients.
The folding step additionally needs odd coefficients and t≥2. After s−1 folds,
the cycle has 2^(s+1) odd coefficients and scalar norm 4u²; for s≥2 their squares
give zero rather than four modulo eight. The conclusion is s=1, because u
was already defined to be odd.

Use order four for row sum and parity, hypothetical order 36 for grouping nine
signs into each of four positions, and order 16 for equal opposite signs and a
repeated row. The order-16 argument depends on the divisibility lemma and does
not alone exclude all multiples of 16. Recommend the 4→16→36 narrative for the
next overview edit without rewriting the current narration.

Update only the introductory status and graph-planning portion of the
[existing script](../website/scripts/node2/restriction-on-the-order.md), leaving
its narration intact. Update the website and script indexes to reflect the
implemented outline. No new video sources or timings are invented.

## Evidence and outcome

- Independently reviewed the DAG and its assumptions against the local primary
  paper, Section 2, pages 4–7, and the official
  [source page](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
  This organizes an existing argument, not a new theorem or formal verification.
- A focused graph test failed before the parent was expanded. With the new
  graph, all 42 tests pass (5,378 assertions), including generated navigation
  and math rendering. The build emits 23 pages.
- Repository lint, explicit lint of new files, and whitespace checks pass.
  The overview narration is retained; its graph notes now match the website.
- Desktop inspection confirms all six labels and five arrows are legible.
  Shortened long box summaries. Narrow-screen inspection prompted moving
  the divisibility statement's parameter conditions into prose; the equation
  then fits. The child page retains its parent link and map disclosure.
- The first screenshot URLs omitted the site's /nodes/ prefix and hit missing
  pages. Inspection of generated paths corrected the URLs; subsequent captures
  and HTTP verification succeeded. Opened the Node 2 local page.
- Work remains local, consistent with the [PR scope selection](2026-11-14-175735-prepare-node-one-pull-request.md).
  No commit, push, PR update, or hosted deployment was made.

## Report relevance

This records the transition from a private Node 2 plan to a navigable local
proof outline. It separates the elementary examples from the technical input
needed for the general restriction and preserves the user's intended sequence:
graph first, overview narration next, detailed scripts later.
