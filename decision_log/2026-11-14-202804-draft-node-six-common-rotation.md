# Draft Node 6 around odd-order rigidity and a common rotation

- Recorded at: 2026-11-14T20:28:04-08:00
- Observed work interval: 2026-11-14T20:20:28-08:00/2026-11-14T20:28:04-08:00 (456 seconds through this record).
- Participants: Steven Creech (supplied six-scene script instructions);
  OpenAI Codex, GPT-6 (integration, delegated mathematical review and
  script/storyboard/leaf drafting, and validation).
- Delegated intervals: mathematical review,
  2026-11-14T20:21:14-08:00/2026-11-14T20:22:42-08:00 (88 seconds);
  script/storyboard,
  2026-11-14T20:22:31-08:00/2026-11-14T20:26:02-08:00 (211 seconds);
  general leaf exposition,
  2026-11-14T20:23:09-08:00/2026-11-14T20:25:33-08:00 (144 seconds).
  These overlap the primary interval and are not additive person-hours.

## Context and decision

Steven supplied Node 6 notes through the attached “Pasted text.txt,” asking
for an outline and narration using two circles of radius three. The sequence
recalls c, d, g; defines R and W; brings in sign congruences; applies
odd-order rigidity; interprets a common rotation; and hands the result to
Node 7. Preserve the one-prime example/general-product distinction and
avoid treating congruence as geometric proximity.

Save the edited [script](../website/scripts/node6/odd-order-rigidity.md)
in node6, along with the [supplied notes](../website/scripts/node6/reference/supplied-outline.md).
The copied wording is unchanged; the required end-of-file lint hook
normalizes its final newline. The working script is an edited draft,
not a verbatim transcript. Retain all six scenes, add the missing unit
justification, and give the short geometric-sum proof of rigidity.
Do not repeat the Δ-theorem's proof or introduce Node 7's alternating sums.
Video sources, recordings, and cut timings remain unset.

Create an embedded [two-circle storyboard](../website/scripts/node6/storyboards/common-rotation.svg)
and its editable generator. Compile its fifteen mathematical labels through
the shared MathJax renderer, following the
[graph-typesetting correction](2026-11-14-195930-typeset-proof-graph-mathematics.md).
Use c(1)=3, d(1)=−3, g(1)=3i and a common counterclockwise rotation
λ=ω through 120°. Label the picture as a schematic conclusion, not a
Hadamard construction. Keep the three points distinct and note that
Δ(c)=λ⁻¹ has the opposite orientation.

Expand [Node 6](../website/nodes/odd-order-rigidity.md) into five steps:
odd comparison products, invertible evaluations, sign-ratio congruences,
the elementary rigidity lemma, and exact comparison identities. The graph
has edges 6.2→6.3, 6.1→6.4, 6.3→6.4, and 6.4→6.5. Use existing
LaTeX labels, solid arrows, colors, and subsection layout. Put the main
lemma and its idea in the body shown on the main page; update both indexes.
This follows the earlier [Node 4](2026-11-14-195152-draft-node-four-phase-storyboard.md)
and [Node 5](2026-11-14-193748-draft-node-five-all-ones-congruence.md) refinements.

## Rationale

The denominator step warrants its own node: a congruence cannot simply be
divided by an arbitrary nonzero complex value. In
A=Z[i,{ζp},1/u], every evaluated cS, dS, gS has inverse given by its
complex conjugate divided by u². It is therefore a unit before and after
reduction. The quotient A/(1+i)A is nonzero of characteristic two; the
leaf proves properness using a maximal ideal of the cyclotomic ring above
2 that avoids odd u. This global ring matches the current Node 7 exposition;
the cited paper instead localizes at one such maximal ideal.

The exact sign divisibilities give dS/cS and gS/cS residue one. Products
and inverse factors preserve that residue, so R and W have residue one.
The Δ-theorem gives odd order. For a nontrivial odd-order root, cancel
ξ−1 in the original characteristic-zero domain to obtain a vanishing
geometric sum. Reduction would give an odd sum of ones equal to zero,
a contradiction. The quotient need not itself be a domain.

For u=3, the exact product identities become equal ratios and hence a
single rotation of the three evaluation points. In general they compare
alternating products over several evaluations; do not assert a shared
rotation across all of them. The displayed schematic also respects the
real values of c(1),d(1) and the Gaussian norm-nine values of g(1).

**Factual wording correction:** remove the old Node 6 phrase “approximate
congruence becomes exact equality.” Algebraic congruence is not a metric
approximation. The exact equality follows from two algebraic conditions.

## Evidence and outcome

- Independent review checked the denominator argument, residue proof,
  quotient orders, and geometric interpretation against Section 4,
  equations (4.3)–(4.10), and Lemma 3.3(ii) of the
  [primary paper](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
  The general deductions are written proofs from the already accepted
  Δ-theorem; no new black box is added.
- The new topology check failed before the node was expanded. All 56 final
  tests pass, with 6,445 assertions, and the build emits 40 pages. Tests
  cover graph links, script and storyboard math, and the common-rotation
  example. The terminal-page fixture now finds a terminal main node instead
  of naming a node that will cease to be terminal as the site develops.
- Finite checks verify the three schematic coordinates, radius-three norms,
  λ=ω, Δ=λ⁻¹, R=W=1, and preserved relative ratios with distinct points.
  These validate the illustration, not existence of a Hadamard matrix or
  the general theorem. SVG XML and accessible description checks pass.
- Required lint completed with the known notices for the earlier unstaged
  archived paths. Explicit lint initially normalized the copied source's
  final newline; after that, all 199 existing files passed. A byte comparison
  confirms the source differs only by that newline normalization.
- Browser inspection confirmed readable compiled labels in the storyboard,
  the five-node graph and its arrows, and the stacked general/example
  equations at a 500px viewport. Screenshots remain temporary artifacts.
- The parent and all five leaf URLs returned HTTP 200. Opened the updated
  local Node 6 page. No commit, push, PR update, hosted deployment, narration
  synthesis, or video rendering was performed; previous local work is intact.

## Report relevance

This records user-led narration and visual development with AI assistance
for a precise congruence-to-equality argument, dependency structure, and
website integration. It distinguishes the schematic phase illustration,
bounded numerical checks, and the general mathematical proof.
