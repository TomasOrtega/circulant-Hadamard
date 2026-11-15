# Draft Node 5 and refine the all-ones congruence

- Recorded at: 2026-11-14T19:37:48-08:00
- Observed work interval: 2026-11-14T19:30:26-08:00/2026-11-14T19:37:48-08:00 (442 seconds through this record).
- Participants: Steven Creech (scope, example-led narration, and notation
  question); OpenAI Codex, GPT-6 (integration, delegated mathematics review
  and drafting, and validation).
- Delegated intervals: mathematics review,
  2026-11-14T19:32:01-08:00/2026-11-14T19:32:42-08:00 (41 seconds observed;
  any earlier review start is unknown because the initial clock output was
  truncated); script and leaf drafting,
  2026-11-14T19:33:56-08:00/2026-11-14T19:36:11-08:00 (135 seconds).
  These overlap the primary interval and are not additive person-hours.

## Context and decision

Steven requested Node 5 next: define E(P), explain its congruence to the
all-ones polynomial using nine positions, and develop general u inside the
node. He asked whether to introduce J(P) or write the sum explicitly.

Save the overview draft at
[scripts/node5/signs-become-all-ones.md](../website/scripts/node5/signs-become-all-ones.md).
Write 1+P+...+P⁸ first, then introduce J(P) as a short name for that sum.
Keep P consistent with Node 3 instead of returning to X. Include narration,
optional board algebra, animation cues, and a three-node graph outline.
This follows the
[example-to-general progression](2026-11-14-182210-unify-example-and-general-proof-journey.md)
and the [Node 3 draft](2026-11-14-183958-draft-node-three-evaluations-and-keep-u.md).
The text is an AI-assisted draft from Steven's request, not a supplied
verbatim script. Video sources and cut timings remain unset.

Refine [Signs Become All Ones](../website/nodes/signs-become-all-ones.md)
with three general-exposition leaves:

1. Form the Combination: integral quotients and the exact sign formula.
2. Gaussian Parity: reduction modulo 1+i, a terminal undergraduate foundation.
3. All Coefficients Become 1: combine both inputs to prove the congruence.

Edges are 5.1→5.3 and 5.2→5.3. Reuse the existing blue-accent boxes and solid
gray arrows. Put the step explanations beneath the graph, and use the
parent node's body for the lemma and its big idea on the main page.
Update both authoring indexes. All changes remain local.

## Rationale

The branched graph keeps the arithmetic rule independent of the sign
calculation; a longer linear graph would subdivide this short lemma without
adding a needed proof dependency. Expanded notation comes before J(P), while
retaining that shorthand for the later proof nodes.

The common sign array, rather than just the three norm identities, gives
(d−c)/2=−(H1+H3)/2 and
(g−c)/(1+i)=−(H2+H3)/2+i(H1+H2)/2. Every half-sum is integral
coefficientwise. Consequently E=−H3+(i−1)(H1+H2)/2. The factor i−1 is a
multiple of 1+i, and both signs have residue 1.

Form the integral quotients before reducing. The proof is in
Z[i][P]/(P^(u²)−1), followed by coefficient reduction modulo 1+i.
It does not require norm identities, oddness, or the Δ-theorem. Keep the
project's positive odd u as context, while explaining this weaker input.
Retain both divisibilities for Node 6. Move the previous Node 5 discussion
of root evaluations and localized coefficient rings out of this exposition;
the later nodes already develop those steps.

Use the single coefficient column (−1,1,1,−1) to give c_r=d_r=0,
g_r=−1+i, and e_r=i≡1. Explicitly distinguish a coefficient illustration
from a whole order-36 Hadamard construction, and congruence from equality.

## Evidence and outcome

- Independent review checked the exact identities against Section 4,
  equations (4.1) and (4.5)–(4.9), of the local primary paper and its
  [official source page](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
  The general proof is the coefficientwise algebra in the new leaf pages.
- Extended the existing exhaustive check of all sixteen sign columns to
  verify each separate quotient's integrality and formula. This finite check
  supports the exposition; it is not a new research result or Lean proof.
- The new graph check failed before expansion. The first full run then
  exposed a test using Node 5 as a terminal-page fixture; changed that fixture
  to the still-terminal Δ-theorem page, preserving its navigation assertion.
- All 47 tests pass, with 5,777 assertions. Script math renders successfully;
  graph links, parent navigation, and video ordering pass the existing checks.
  The compiled site contains 29 pages.
- Required lint completed with the known missing-old-path notices from the
  earlier unstaged route archive moves. Explicit lint of all 176 existing
  tracked/untracked files passed; whitespace checks passed.
- Desktop inspection confirmed the three boxes and two solid arrows. A
  500px browser preview confirmed the integral formulas fit; the longer
  second quotient is split across two lines in the subsection, leaf, and
  script. Preview images are temporary artifacts outside the repository.
- All four Node 5 URLs returned HTTP 200, and the updated local Node 5 page
  was opened for Steven. The direct HTTP check required sandbox escalation
  for localhost access; it succeeded after escalation.
- No commit, push, PR update, or hosted deployment was performed. Existing
  Node 1, Node 2, Node 3, and navigation work remains intact.

## Report relevance

This records user-led development of the short sign-congruence explanation,
with AI assistance for narration, proof organization, coefficient checks,
and website integration. It distinguishes the algebraic argument from its
bounded computational checks and the unrecorded video production work.
