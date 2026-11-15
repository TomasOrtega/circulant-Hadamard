# Draft Node 7 from a common rotation to a vanishing sum

- Recorded at: 2026-11-14T20:47:11-08:00
- Observed work interval: 2026-11-14T20:38:06-08:00/2026-11-14T20:47:11-08:00 (545 seconds through this record).
- Participants: Steven Creech (supplied five-scene outline); OpenAI Codex,
  GPT-6 (integration, delegated mathematical review and script/storyboard/leaf
  drafting, and validation).
- Delegated observed intervals: mathematical review,
  2026-11-14T20:40:19-08:00/2026-11-14T20:40:52-08:00 (33 seconds);
  leaf drafting, 2026-11-14T20:42:36-08:00/2026-11-14T20:44:32-08:00
  (116 seconds); script/storyboard,
  2026-11-14T20:40:49-08:00/2026-11-14T20:44:22-08:00 (213 seconds).
  Earlier delegated read times were not recoverable after compaction and
  are unknown. These intervals overlap and are not additive person-hours.

## Context and decision

Steven supplied “Node 7 — From Products to Sums: One Rotation, One
Vanishing Sum,” asking for a script. Preserve the five-scene progression:
recall the common rotation, construct E from difference vectors, divide by
c to cancel the rotation, state the general alternating sum, and defer its
all-ones evaluation to Node 8. Save the edited
[script](../website/scripts/node7/products-to-sums.md) and the
[supplied outline](../website/scripts/node7/reference/supplied-outline.md)
in node7. The preserved outline differs from the attachment only by a
normalized final newline. The production script is an edited draft.

Continue the established website workflow from the
[Node 6 decision](2026-11-14-202804-draft-node-six-common-rotation.md):
add a three-panel [storyboard](../website/scripts/node7/storyboards/rotation-cancellation.svg),
its editable generator, and four general proof steps inside
[Node 7](../website/nodes/products-to-sums.md). The overview motivates the
result with u=3; the smaller nodes provide the general argument.
The new graph has edges 7.1→7.3, 7.2→7.3, and 7.3→7.4:
split exact products, expand products with exact quotients, cancel before
reducing, and identify E while adding the sums. Keep the site's blue/white
palette, solid arrows, and
[compiled LaTeX labels](2026-11-14-195930-typeset-proof-graph-mathematics.md).
Put explanations in the child sections and the main lemma in the parent
body shown on the main page. Update the website and script indexes.

## Rationale

The two-evaluation case gives an exact zero difference. A fixed complex
linear combination follows the same rotation as c,d,g; dividing E by the
nonzero c value cancels that multiplier. With several distinct prime
divisors, Node 6 supplies alternating product identities rather than a
single common rotation across all evaluations. Preserve that distinction:
the general conclusion here is the congruence modulo 1+i.

The inner proof uses the same characteristic-zero domain as Node 6,
A=Z[i,{ζp},1/u]. Coefficientwise divisibility first constructs
(d−c)/2 and (g−c)/(1+i); evaluation and the inverse of cS put the
normalized quotients in A. They need not be algebraic integers, because
u is inverted. Write the factors as 1+t xS, with t=2 or t=1+i.
Expand the equal even and odd products as finite exact polynomials;
subtract their constants and cancel t in A before reduction. The
remaining terms have a factor t and therefore vanish modulo 1+i.
Adding the two resulting sums identifies E/c term by term. No analytic
approximation, abstract linearization homomorphism, or new black box is
needed. The reduction ring need not be a field or a domain.

The all-ones residue E≡J is explicitly left for Node 8. The earlier
coefficient divisibilities have already been used, so the script says
only that the all-ones conclusion has not yet been used in this calculation.

**Mathematical clarifications to the supplied geometry:** λ is a rotation
multiplier, and arg(λ) is its angle. Multiplication by 1/(1+i) rotates
clockwise 45° and scales by 1/√2. The arrows represent evaluated complex
numbers, not formal polynomials. E need not lie on the radius-three
circle and may be zero; normalization divides by c, never by E.
The storyboard continues the schematic c(1)=3, d(1)=−3, g(1)=3i,
λ=ω, giving E(1)=−3+3i and both normalized E values equal to −1+i.
Its caption identifies it as an illustration, not a Hadamard construction.

## Evidence and outcome

- Independent review checked the general derivation against the locally
  available primary paper, Section 4, Lemma 4.1 and equations (4.10)–(4.11).
  The direct finite expansion works in the global ring used by the site;
  it does not require every element of 1+tA to be a unit. These are written
  deductions from earlier nodes, not a Lean verification.
- The new topology test failed before the parent had children. Final
  website checks pass: 59 tests, 6,651 assertions, and 44 compiled pages.
  The new tests cover the dependency edges and links, script/storyboard
  math rendering, and the schematic linear combination and cancellation.
- Numerical checks confirm the specific coordinates, common rotation,
  E's modulus 3√2, and normalized value −1+i. These check the illustration,
  not a general existence or nonexistence theorem. SVG/XML parsing,
  accessible title/description, 24 compiled math labels, and source-copy
  fidelity also pass.
- Required all-files lint completed with the known notices for the two
  previously archived unstaged paths. Explicit lint over all 209 existing
  project files passed, as did git diff --check. No archived route was
  restored.
- Browser inspection confirmed the three-panel storyboard, four-step
  graph, and compiled mathematics on the desktop page. At 500px width,
  text and equations fit and the graph retains its existing horizontal
  scrolling behavior. Temporary screenshots are not project assets.
- The parent and all four leaf preview URLs returned HTTP 200. Opened
  the updated local Node 7 page. Videos and cuts remain unset; this task
  produced narration and a static storyboard, not a recorded video.
  No commit, push, PR update, or hosted deployment was performed.
  Prior local work, including Steven's Node 1 edits, is preserved.

## Report relevance

This records user-led narration and visual development with AI assistance
for the passage from exact multiplicative identities to an additive
congruence. It separates the exact motivating example, the general
algebraic deduction, and bounded illustration checks, and documents the
website integration and validation.
