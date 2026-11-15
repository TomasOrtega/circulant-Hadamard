# Separate the geometric preview from the algebraic contradiction

- Recorded at: 2026-11-15T01:43:31-08:00.
- Observed work interval: 2026-11-15T01:35:15-08:00–2026-11-15T01:43:31-08:00
  (496 seconds, through final browser checks, lint, and preview opening).
- Participants: Steven Creech (request); Codex/GPT-6 (implementation and
  validation); Codex/GPT-6 subagents (mathematical audit and exposition).
- Overlapping subagent intervals on 2026-11-15, UTC offset -08:00:
  mathematical audit 01:35:52–01:36:42 (50 seconds); exposition
  01:36:05–01:36:58 (53 seconds). These are not additive person-hours.

## Context and decision

Steven requested a geometric preview of the contradiction in Node 6 and the
actual algebra for the guiding case $u=3$ in Node 7, with the rest of the
proof-map exposition following that sequence. This revises the
[previous Node 6 presentation](2026-11-15-012341-lead-node-six-with-rigidity-and-plot-e.md)
and the earlier [Node 7 handoff](2026-11-14-204711-draft-node-seven-rotation-cancellation.md),
which deferred the all-ones calculation entirely to Node 8.

- [Node 6](../website/nodes/odd-order-rigidity.md) retains odd-order rigidity,
  the shared rotation, and the fact that $E$ follows it. Its picture previews
  the incompatible nonzero/zero residue requirements; the normalized equality
  and detailed algebra now belong to Node 7.
- [Node 7](../website/nodes/products-to-sums.md) cancels the common factor in
  $E/c$, explains the unit denominators, evaluates $J(1)=9$ and
  $J(\omega)=3(1+\omega+\omega^2)=0$, and derives the contradiction for $u=3$.
  Its boxed general lemma and four-step product-expansion refinement remain.
- [Node 8](../website/nodes/final-contradiction.md) now explicitly finishes
  the argument for general odd $u>1$, using the alternating sum, and concludes
  with orders one and four. This preserves the eight-node structure and its
  five-step final refinement.
- Updated the overview's description of this sequence, the main-map summaries,
  the Node 7 child/leaf transitions, and website authoring notes. IDs, titles,
  video/cut metadata, and dependency topology remain. The required $5\to7$
  dependency was already present, so no new edge was necessary.

The [phase explorer](../website/phase-explorer.jsx) now has two stages. The
rotation stage appears in Node 6 and its exact-comparison section. Node 7
and its final sum section provide the normalization control and the algebraic
contradiction panel. The homepage contains both widgets, with independent
controls and one shared browser script. A continuation link leads from the
geometric preview to the Node 7 section. Production narration files were not
part of this request and were preserved.

## Rationale and mathematical correction

**Factual correction to the proposed inference:** invertibility of $c$ does
not imply $E(1)\equiv E(\omega)$. The exact equality is
$E(1)/c(1)=E(\omega)/c(\omega)$. The two raw values differ by the unit
$\lambda$, which need not have residue one. A change in complex angle does
not itself make a residue zero.

For the geometric preview, multiplication by an invertible residue preserves
whether a residue is zero. It cannot carry the required nonzero residue at
one to the required zero residue at $\omega$. Node 7 makes the denominator
calculation explicit in $\mathbb Z[i,\omega,1/3]$: the norm gives
$c(z)^{-1}=\overline{c(z)}/9$, and $c(1)=\pm3\equiv1$. Thus the equal
normalized values would have residues one and zero in a nonzero quotient.
These are deductions from the earlier nodes, not a new proof verification of
the entire conjecture.

The plotted schematic remains $c(1)=3,d(1)=-3,g(1)=3i$, with
$E(1)=-3+3i$. It illustrates the common rotation but does not meet all
Hadamard assumptions. Both stages keep the all-ones requirements separate
from the actual residues of these plotted points. Node 6's panel labels
required nonzero and zero residues; it does not move the plotted points to
one or zero or identify a residue with a direction.

## Evidence and outcome

- Full website suite: **145 tests pass, 8,527 assertions**, across 17 files.
  Stage-specific checks ensure Node 6 has no normalization control, Node 7
  owns the algebraic panel, both homepage widgets render, and the browser
  script loads once per page. Existing finite phase-model tests remain valid.
- Built **48 pages** and compatibility redirects. The browser bundle is
  2.92 KB; no new dependencies were introduced.
- Browser checks covered the homepage at 1440 px and 390 px and the deeper
  Node 6 and Node 7 pages at 390 px. Both widgets initialize, their controls
  act independently, the rotated $E$ point is correct, and normalization aligns
  the $E/c$ points. Each view has the intended controls. No runtime or math
  errors, horizontal page overflow, wide widget formulas, or clipped labels.
- With JavaScript disabled, both homepage diagrams retain all eight plotted
  values and their explanations, with controls disabled. Desktop and mobile
  screenshots were visually inspected. Evidence is in
  `/private/tmp/circulant-node67-flow-qa.json` and screenshots matching
  `/private/tmp/circulant-node67-*-*.png`. Test output is in
  `/private/tmp/circulant-node7-contradiction-tests.log`.
- The first browser-validation command had an extra parenthesis in its own
  coordinate assertion; corrected that temporary command and reran it
  successfully. This was not an application failure.
- Non-mutating whole-repository lint and full hooks on all eleven changed
  implementation/content files passed. Temporary browser profiles were
  removed after closing. The existing server remains available and the
  refreshed preview opened at `http://localhost:8000/#node-products-to-sums`.
- Unrelated local edits and production scripts were preserved. No commit,
  push, or pull request was requested or performed.

## Report relevance

This records a user-directed change to the pedagogical sequence, the precise
correction concerning unit denominators and modular residues, and AI-assisted
implementation and validation of separate geometric and algebraic stages.
