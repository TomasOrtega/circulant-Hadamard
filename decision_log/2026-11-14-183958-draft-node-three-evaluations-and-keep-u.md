# Draft Node 3 and keep u fixed through the order restriction

- Recorded at: 2026-11-14T18:39:58-08:00
- Observed work interval: 2026-11-14T18:28:28-08:00/2026-11-14T18:39:58-08:00 (690 seconds through this record).
- Participants: Steven Creech (notation request and Node 3 narration outline);
  OpenAI Codex, GPT-6 (integration, delegated mathematics review, Node 2 edits,
  Node 3 script/leaf drafting, and validation).
- Delegated intervals: mathematics review,
  2026-11-14T18:29:04-08:00/2026-11-14T18:29:45-08:00 (41 seconds);
  Node 2 notation, 2026-11-14T18:29:27-08:00/2026-11-14T18:31:03-08:00
  (96 seconds); Node 3 drafting,
  2026-11-14T18:31:00-08:00/2026-11-14T18:35:31-08:00 (271 seconds).
  These overlap the primary interval and are not additive person-hours.

## Context and decision

Steven requested n=4u² in Node 2.2 so that the later task is to prove that
same u is odd. He also supplied a Node 3 overview outline: specialize to the
hypothetical order-36 case, use the Chinese remainder theorem, collect powers
of Z, evaluate at 1, −1, i, and divide by two to obtain norm-nine polynomials.
Create a draft script and a matching internal dependency graph.

Update the [Node 2 page](../website/nodes/restriction-on-the-order.md), its
relevant leaves, and [production script](../website/scripts/node2/restriction-on-the-order.md).
Use u from the elementary square/parity step onward. This supersedes the
v/u distinction in the
[earlier outline](2026-11-14-170130-polynomial-notation-and-node-two-outline.md).
During descent, introduce only the temporary odd part w through
u=2^(s−1)w. Then n=2^(2s)w², and proving s=1 proves the original u=w is odd.
The order-16 illustration now has u=2,w=1. The valuation function v(·) in
the technical notes is unrelated and remains unchanged.

Save the new narration at
[scripts/node3/three-evaluations.md](../website/scripts/node3/three-evaluations.md).
It is an edited draft based on Steven's outline, with complete formulas and
animation cues, not a verbatim transcript or timed recording. Follow the
[single proof journey](2026-11-14-182210-unify-example-and-general-proof-journey.md):
the overview uses n=36, while the five smaller nodes state the general facts.

## Rationale

The [Node 3 graph](../website/nodes/three-evaluations.md) has five nodes:

1. Chinese remainder coordinates.
2. Four sign polynomials.
3. Evaluate at 1, −1, and i.
4. Parity of sign columns.
5. Normalize the norm identities.

Its edges are 3.1→3.2, 3.2→3.3, 3.2→3.4, 3.3→3.5, and 3.4→3.5.
Choose the branched graph over a purely linear outline because preservation
of the norm and coefficient parity establish independent facts. Both are
needed for normalized integral solutions. Keep the CRT and coefficient
grouping nodes as terminal undergraduate foundations.

Make the CRT map explicit: X maps to ZP, and coefficient position j maps to
(j mod 4,j mod u²). This reindexes signs rather than splitting the original
row into consecutive blocks. Each H_a(P) has u² sign coefficients.

Fill in c=(H0+H1+H2+H3)/2, d=(H0−H1+H2−H3)/2, and
g=(H0−H2)/2+i(H1−H3)/2. Four-sign sums and two-sign differences are even,
giving integer c,d and Gaussian-integer g. Star conjugates Gaussian
coefficients as well as inverting P. Dividing each polynomial by two divides
its product with its star by four: 36 becomes 9, and 4u² becomes u².
The −i evaluation is coefficientwise conjugate to the i evaluation.

Keep evaluation in P at 1 and a cube root as a brief handoff, not an additional
proof node. Add the normalized-evaluation lemma and its big idea to Node 3's
parent-card body; place the step explanations beneath its graph. Update the
script and website indexes. All video sources and cut timings remain unset.

## Evidence and outcome

- Independent review checked the formulas, CRT indexing, star compatibility,
  and graph assumptions against the local primary paper, Section 4, page 11,
  equations (4.1)–(4.2), and its
  [official source page](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
  The Node 2 factorization change was also reviewed.
- The new topology check failed before Node 3 was expanded. All 45 final
  tests pass (5,580 assertions), including script math rendering, graph links,
  and one-video-per-node navigation. The build emits 26 pages.
- Finite arithmetic checks verify CRT reindexing for u=1,3,5 and all sixteen
  four-sign columns, including integral half-coefficients and the relation
  between cyclic correlations, the three evaluations, and division of the
  norm by four. These are bounded computations, not a proof for all orders.
- Required lint completed; unstaged archive moves again produced missing-old-
  path notices. Explicit lint of all 170 existing tracked/untracked files
  passed, along with final changed-file lint and whitespace checks.
- Desktop inspection confirmed the five-node graph and arrows. Narrow-screen
  inspection found the three definitions too wide on one line; stacked them
  in the parent card, subsection, and leaf. The revised leaf fits at 500px.
  Shortened graph summaries while keeping explicit polynomial notation.
- Corrected an animation weight typo and clarified that the numerators of
  g's coefficients are even, rather than suggesting their halves are even.
- The local Node 3 page serves all five graph nodes and was opened for Steven.
  Existing work and the published PR are untouched by Git actions; no commit,
  push, PR update, or hosted deployment was performed.

## Report relevance

This records user-led narration development and mathematical organization for
the three evaluations, plus a notation change that keeps the order restriction's
goal visible. AI assistance supplied the draft prose, dependency structure,
coefficient checks, and rendering validation; no new research result or formal
verification is claimed.
