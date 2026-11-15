# Explicit polynomial notation and the Node 2 video outline

- Recorded at: 2026-11-14T17:01:30-08:00
- Observed work interval: 2026-11-14T16:53:59-08:00/2026-11-14T17:01:30-08:00 (451 seconds through this record).
- Participants: Steven Creech (notation request and initial Node 2 argument);
  OpenAI Codex, GPT-6 (primary implementation, notation delegate, and independent
  mathematics reviewer).
- Delegated intervals: notation 2026-11-14T16:54:31-08:00/2026-11-14T16:55:39-08:00
  (68 seconds); mathematics research 2026-11-14T16:54:14-08:00/2026-11-14T16:55:58-08:00
  (104 seconds); draft review 2026-11-14T16:58:42-08:00/2026-11-14T16:59:08-08:00
  (26 seconds). These overlap the primary interval and are not additive person-hours.

## Context and decision

Steven requested more explicit polynomial notation in the group-ring identity
and supplied the beginning of a Node 2 video: evaluation at one makes the order
a square; row orthogonality makes it even; an even square is four times a square.
He asked for a script or outline and advice about the inner graph and whether
order 16 could illustrate the remaining oddness restriction.

Revise the Node 1 explanations, graph summaries, and editable narration to
write $h(X)h^*(X)=n$ explicitly. Explain that the equality is in
$\mathbb Z[X]/(X^n-1)$ and that $n$ is the constant polynomial. Carry the same
clarity into Node 2 and use $h(Z,P)h^*(Z,P)$ at the later two-variable inputs.
This refines the notation in the [corrected Node 1 material](2026-11-14-164817-refine-node-one-from-corrected-script.md).
The archived PDF and supplied overview script remain unchanged; document the
new notation revision in the source README.

Save a Node 2 narration draft at `website/scripts/node2/restriction-on-the-order.md`
with animation cues, an optional order-16 passage, a six-node graph proposal,
and technical notes for later scripts. Adapt the elementary proof and the
scope of the deeper step into the [website explanation](../website/nodes/restriction-on-the-order.md).
Keep the general divisibility/descent step identified as an accepted input on
that page. The internal graph is a proposal in the script rather than newly
published child pages, since the user is developing its structure.

## Rationale

The user's elementary reasoning is correct. Use $n=4v^2$ at that stage, reserving
$u$ for the odd part in $n=2^{2s}u^2$ and the final statement. Evaluation at one
is justified because it respects $X^n=1$.

The general remaining claim is $16\nmid n$. Excluding only $n=16$ would not
establish it. The optional illustration specializes the paper's divisibility
argument: $4\mid h_j-h_{j+8}$ forces equality of opposite signs, so the eighth
shift repeats the first row and contradicts orthogonality. Explicitly name the
cyclotomic lemma supplying that divisibility; do not derive it from the row
sum or an ordinary complex absolute value alone.

Propose six internal nodes: evaluation at one; parity of an orthogonal dot
product; projection to the power-of-two cycle; independent cyclotomic
coefficient divisibility; repeated folding and division by two; and the final
odd-square contradiction modulo eight. The first two feed projection, and
projection plus divisibility feed folding. The last node concludes $s=1$.
An independent review corrected its initial label, “u is odd,” because $u$ is
already defined as odd in the factorization. Iteration is within the folding
node, not a cycle in the dependency graph.

This develops the previously [deferred order restriction](2026-11-14-151609-eight-node-proof-map.md)
without presenting a new general proof as an elementary consequence of the
order-16 example. Production drafts remain separate from reader-facing pages,
following the [script workflow](2026-11-14-154516-store-overview-video-script.md).

## Evidence and outcome

- Checked Section 2 of the previously downloaded full
  [primary paper](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf):
  page 4 for square/parity, pages 5–6 for Lemma 2.1, and pages 6–7 for
  Proposition 2.2. The research agent also opened the primary GitHub page;
  raw-PDF retrieval failed, so this was not a fresh extraction of the paper.
- Independently reviewed the written outline: projection sums an odd number
  of signs; cyclotomic valuation gives differences divisible by $2^t$;
  pairwise averages stay odd for $t\geq2$; after $s-1$ folds, $2^{s+1}$ odd
  squares would sum to $4u^2$, impossible modulo eight when $s\geq2$.
  Added the valuation justification to the order-16 technical notes after review.
- The research agent exhaustively checked all 65,536 length-16 sign rows;
  none meet all cyclic orthogonality conditions. This checks the example only,
  not the general theorem. No Lean verification is claimed.
- All 39 website tests passed (4,985 assertions); the build emitted 17 pages.
  The full new narration, including its technical notes, separately rendered
  successfully through the site's MathJax pipeline. No extra tests mirroring
  prose edits were added.
- Required repository lint, explicit lint of updated untracked files, and
  `git diff --check` passed. Browser inspection confirmed readable Node 2 math
  and that the longer polynomial labels fit the existing Node 1 graph.
  Opened the updated Node 2 local page for review.
- Earlier uncommitted work is preserved. No recording, cut timing, commit,
  push, or hosted deployment was created.

## Report relevance

This is AI-assisted exposition and production planning based on Steven's
argument and the paper's established order restriction. The order-16 example
is a pedagogical specialization, not a new research result. The proposal makes
the boundary between elementary steps, a technical algebraic input, and the
general descent visible to future script authors.
