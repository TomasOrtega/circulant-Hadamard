# Derive the normalized E identity in Node 6 and clarify polynomial notation

- Recorded at: 2026-11-15T02:10:17-08:00.
- Observed work interval: 2026-11-15T01:58:03-08:00–2026-11-15T02:10:17-08:00
  (734 seconds, through implementation, tests, build, and browser review).
- Participants: Steven Creech (request); Codex/GPT-6 (implementation and
  checks); Codex/GPT-6 subagents (Node 6–8 exposition and notation audit).
- Overlapping subagent intervals on 2026-11-15, UTC offset -08:00:
  exposition 01:58:38–01:59:40 (62 seconds); notation audit
  01:58:48–02:00:34 (106 seconds). These are not additive person-hours.

## Context and decision

Steven requested that Node 6 use the definition of $E(P)$ to derive
$E(\omega)/c(\omega)=E(1)/c(1)$, that formal polynomials keep their arguments,
that the general case receive a caution, and that the illustration note
explain why its values cannot come from an order-36 circulant Hadamard matrix.
He also requested a simpler Node 7 diagram without repeated exposition.
This revises the division between the two stages recorded in the
[previous decision](2026-11-15-014331-place-the-example-contradiction-in-node-seven.md).

[Node 6](../website/nodes/odd-order-rigidity.md) now substitutes the defining
combination for $E(P)$. At each $z\in\{1,\omega\}$,

$$
\frac{E(z)}{c(z)}=
\frac12\left(\frac{d(z)}{c(z)}-1\right)
+\frac1{1+i}\left(\frac{g(z)}{c(z)}-1\right).
$$

The preserved ratios on the right give the desired equality. The exposition
states that division by $2$ and $1+i$ is exact before modular reduction.
It then records the equivalent shared-rotation statement. The general-case
paragraph distinguishes the two-evaluation example from alternating products
when $u$ has several distinct prime divisors; the latter require the later
product-to-sum congruence.

[Node 7](../website/nodes/products-to-sums.md) now starts from that established
equality and retains the residue contradiction in its main exposition. Its
normalization diagram contains the circles, controls, a short status, and the
illustration note; removed the repeated algebraic-contradiction disclosure and
long explanation below the circles. Node 8 retains the general conclusion.

## Notation and display choices

Use $c(P),d(P),g(P),E(P),J(P)$ for formal polynomials and explicit arguments
for their values. Updated relevant parent and child exposition, including
Nodes 3, 6, 7, and 8. Retained standard functionals such as $\Delta(c)$,
actual evaluations, and defined scalar abbreviations such as $c_S,E_S$.
Recorded this distinction in [website/AGENTS.md](../website/AGENTS.md).

The [phase explorer](../website/phase-explorer.jsx) again displays the full
formula for $E(P)$ below Node 6's circles, replacing the scalar shorthand
introduced during the earlier mobile-layout work. Its point labels now show
$c(1),d(1),g(1),E(1)$ on the left and the corresponding values at $\omega$
on the right. Normalization switches to proper typeset fractions with the
appropriate denominator. Both label states are compiled with MathJax during
the build, and the browser only switches their visibility and positions.
The normalization checkbox has an explicit accessible name.

The illustration note explicitly says that no **circulant** Hadamard matrix
of order 36 exists. This qualification matters: the note must not claim that
all Hadamard matrices of that order are excluded. The plotted values remain
the same schematic, so their actual residues are still distinct from the
hypothetical all-ones requirements in the preview panel. No new theorem or
verification of the full conjecture is claimed here.

The notation audit touched the three main files for Nodes 6–8 and eight
additional node files: three-evaluations, normalized-evaluation-norms,
odd-comparison-products, evaluation-units, vanishing-alternating-sum,
roots-cancel-ones, odd-ones-at-one, and incompatible-residues. The latter
sum leaf's title now names E(P); its ID is unchanged. The overview and
website authoring notes reflect the updated sequence. Production scripts,
video metadata, URLs, and graph topology were preserved.

## Evidence and outcome

- Full website suite: **145 tests pass, 8,341 assertions**, across 17 files.
  Updated checks cover compiled evaluation/fraction labels, their two states,
  the checkbox's accessible name, and the absence of the repeated proof panel.
  Removed assertions for the obsolete plain-text label anchors; the underlying
  phase, norm, E-combination, and normalization tests remain.
- Built **48 pages** and compatibility redirects. No new dependencies or
  client math renderer were introduced.
- Browser checks at 1440 px and 390 px covered all three rotations and both
  normalization states where available: 18 scenarios total. Each diagram has
  eight visible typeset labels, the intended label state, no clipped math,
  no runtime or math errors, and no horizontal page overflow. Node 7 has no
  duplicate disclosure. Desktop and mobile screenshots were inspected.
- The first mobile check found the full E(P) formula wider than its container.
  Kept every polynomial argument and used a slightly smaller display size on
  narrow screens; the final check confirms it fits on one line. The shortened
  scalar formula was not restored.
- Evidence: `/private/tmp/circulant-explicit-polynomial-qa.json`, screenshots
  matching `/private/tmp/circulant-explicit-polynomial-*-*.png`, and
  `/private/tmp/circulant-explicit-polynomial-tests.log`.
- Non-mutating whole-repository lint and full hooks on all nineteen changed
  implementation/content files passed. The temporary browser was closed and
  its profile removed; the existing preview server remains available.
- Unrelated local edits and production scripts were preserved. No commit,
  push, or pull request was requested or performed.

## Report relevance

This records the requested change in explanatory order, a precise distinction
between formal polynomials and their evaluations, and the removal of repeated
proof text from an interactive illustration. AI assistance revised and checked
both the mathematical exposition and its typeset presentation.
