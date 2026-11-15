# Simplify report notation and add worked examples and proof figures

- Recorded at: 2026-11-15T10:33:58-08:00.
- Observed work interval: 2026-11-15T10:25:07-08:00/2026-11-15T10:33:58-08:00 (531 seconds through edits, reviews, rendering, and publication of local PDFs).
- Participants: Steven Creech (requested changes); Codex/GPT-6 (report integration, notation and exposition); three Codex/GPT-6 subagents (rotation figure, inner dependency graph, independent mathematical review).

## Context and decision

The user asked to simplify the report by writing 1+i directly instead of
introducing pi, use the guiding example more consistently, add the u=15
case to explain Delta's alternating definition, include rotation figures
like the Node 6/7 website illustrations, and show an inner dependency graph
near the beginning. Revise the [report](../tex/report.tex) and refresh its
[compiled PDF](../tex/report.pdf), continuing the
[initial report work](2026-11-15-101232-write-mathathon-report-and-proof-exposition.md).
This task makes no website edits, commit, PR, or external publication.

## Rationale and implementation

- Replace every shorthand pi denoting 1+i in the report, including exact
  quotients, congruences, quotient ideals, products, and squared factors.
  Retain the ordinary circular constant in root-of-unity exponentials.
  Parentheses in (1+i)c, (1+i)A, and (1+i)^2 preserve their meanings.
- Introduce Delta through u=3 before the general subset definition, including
  why 1 and omega are valid substitutions into P^9=1 and how their quotient
  removes the common magnitude. The genuine norm solution f(P)=3iP gives
  Delta(f)=omega^2 without claiming a Hadamard sign construction.
- Add u=15 with its four allowed inputs 1, zeta_3, zeta_5, and their product
  in the cycle of order 225. A small table identifies the even and odd
  subsets. Display the alternating quotient and its two pairings to show
  why the same expression supports comparison in either prime direction.
- Return to u=15 in the local comparison, using C_225 = C_9 x C_25 and
  225 = 3^2 * 25. Local unit statements justify integrality; alternating
  signs alone do not cancel denominator valuations. State that Delta=1
  for u=15 because its order is both a three-power and a five-power.
- Continue both examples through E(P), the normalized comparison, and the
  final sum. For u=15, show all four signed terms and the surviving residue
  225/(plus or minus 15) = plus or minus 15, congruent to one. Do not extend
  the two-input common-rotation conclusion to arbitrary numbers of primes.
- Add [the inner Delta graph](../tex/assets/diagrams/report-delta-detail.tex),
  reproducing the website's six nodes and eight dependency edges. Place it
  alongside the main map near the beginning, with a paragraph explaining
  how readers can open a claim while preserving its context.
- Add [a three-panel rotation figure](../tex/assets/diagrams/report-common-rotation.tex)
  from the website's exact schematic: c(1)=3, d(1)=-3, g(1)=3i, E(1)=-3+3i;
  rotate by omega; then divide each configuration by its own c-value.
  The shared normalized points are 1, -1, i, -1+i. Distinct markers identify
  the polynomials, with E shown as an outlined triangle outside the circle.
- Use native TikZ for precise scalable mathematical graphics and inline
  flattening. Captions and prose describe the figures for text-only review.
  Explicitly distinguish schematic complex geometry from modular residues:
  these sample points do not satisfy all Hadamard requirements. The separate
  algebra displays equal normalized values with required residues one and
  zero, and explains why an invertible rotation cannot reconcile them.

## Evidence and observed outcome

- An independent read-only comparison with the earlier report and source
  statements found no mathematical correction needed. It checked allowed
  root orders, both u=15 pairings, matching local exponents, Delta=1, the
  four-term sum, the surviving term, the orientation of the normalized
  equality, and every contextual replacement of pi by 1+i.
- Programmatically checked the inner graph against the actual Node 4
  metadata: all six nodes and all eight arrows match. A first vertical
  layout crowded edges and hyphenated labels; the final two-row layout
  removes those problems. Its standalone compilation and ChkTeX pass.
- Independently compiled and visually reviewed the rotation figure. It uses
  the existing website phase coordinates, a positive 120-degree rotation,
  and normalization by the corresponding c-value. No residue values are
  inferred from the schematic points.
- Full report compilation initially produced only one ChkTeX warning about
  a vertical table rule; remove the rule. Reposition the rotation figure
  before its detailed argument, and keep the short inner-graph explanation
  on one page. These changes retain readable figure placement without new
  TeX packages or external image files.
- Final `make -C tex publish check check-pdfs` passes. The PDF has 16 pages,
  no LaTeX warnings, no overfull/underfull boxes, and no ChkTeX warnings.
  Inspected the rendered graphs, u=3/u=15 definitions, and the rotation and
  contradiction pages. The graphs are on page 3, worked Delta examples on
  page 8, and the rotation/contradiction on pages 12--13.
- `uv run --locked prek -a --quiet` passes; the two new diagram files were
  also explicitly linted. The existing temporary TeX environment from the
  prior record was reused. Both checked-in PDFs and their source fingerprint
  record were refreshed under the repository's publication workflow; the
  slides' content remains unchanged.
- No finite illustration check is used as a proof of nonexistence. The
  existing source attribution and cited cyclotomic prerequisites remain.
  The report's submission hash remains pending, as in the earlier draft.

Measured delegated work (all on 2026-11-15, offset -08:00): rotation figure
10:25:46--10:28:19 (153s); inner graph 10:25:50--10:29:29 (219s);
example suggestions 10:26:01--10:26:54 (53s); independent integrated math
review 10:29:43--10:30:06 (23s). These overlap the main interval and are not
additive person-hours.

## Report relevance

Documents the user's example-led editorial refinement and the addition of
precise mathematical illustrations. These are improvements to exposition
of the cited argument, not new theorem claims or formal verification. The
figures explain recursive navigation, common rotation, and normalization;
the written proof separately establishes the arithmetic contradiction.
