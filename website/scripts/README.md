# Video scripts

Write and revise video production drafts here, including spoken narration,
equations, animation directions, and recording notes. These are working
production drafts.

[overview.md](overview.md) contains Steven's supplied **Video 0 — Introduction
and Proof Roadmap** script, preserving its wording and animation cues.

The six Node 1 scripts are transcribed from the supplied corrected PDF, with
math restored as LaTeX. See [source and production conventions](node1/reference/README.md)
for the original PDF, page mapping, and the fixed order-four example.
Their polynomial notation now explicitly uses $h(X)h^*(X)$ at Steven's request.

[Video 2](node2/restriction-on-the-order.md) uses six slides, each pairing
narration with animation directions. It states the goal, evaluates the
polynomial identity abstractly at $X=1$, and proves the parity restriction.
The oddness of $u$ is an accepted input in this overview, with its proof
in the deeper graph. The script ends by assuming $u>1$ for the contradiction
and choosing $u=3$ as the guiding example. Detailed subnode scripts are still to come.

[Video 3](node3/three-evaluations.md) develops Steven's order-36 outline:
Chinese remainder coordinates, four sign polynomials, evaluations at $1,-1,i$,
and division by two to obtain norm-nine polynomials. Its six slides pair
narration with animation directions, explaining both the factor of four
removed from the product and the coefficient parity that permits division.
The final slide puts evaluations on the radius-three circle and previews
Node 6's common phase change from $1$ to $\omega$.

[Video 4](node4/delta-theorem.md) introduces the Δ-theorem using Gaussian
coefficients and the example $f(P)=3iP$. Its
[phase-circle storyboard](node4/storyboards/phase-circles.svg) distinguishes
evaluation values from their relative rotation. The script then states the
general alternating product and explains the role of Kronecker's theorem. The inner graph separates integrality,
Kronecker's criterion, and the local congruences that force odd order.

[Video 5](node5/signs-become-all-ones.md) uses five slides to motivate $E(P)$
and expand it directly in the sign polynomials $H_a(P)$. The nine-position
example shows why every coefficient becomes $1$ modulo $1+i$, and closes
with $E(1)\equiv1$ for odd $u$. Write out the all-ones polynomial before
naming it $J(P)$.
Its three-node refinement develops the coefficient calculation for general $u$.

[Video 6](node6/odd-order-rigidity.md) uses six slides to show why three
points share one rotation in the nine-position example. It joins odd order
with the sign congruences, proves rigidity, and previews the consequence for
$E(P)/c(P)$. Its final slide contrasts the shared rotation with the all-ones
residue requirements: an invertible multiplier cannot send a nonzero residue
to zero. The [storyboard](node6/storyboards/common-rotation.svg) keeps the
three points distinct, with compiled LaTeX labels. The general refinement
justifies the denominators and develops alternating-product identities.
The [supplied notes](node6/reference/supplied-outline.md) retain their original wording.

[Video 7](node7/products-to-sums.md) uses three slides: recall Node 6's
normalized equality, derive the algebraic contradiction for $u=3$, and
introduce the alternating-sum congruence for general odd $u$.
The [earlier storyboard](node7/storyboards/rotation-cancellation.svg)
illustrates the rotation and cancellation now covered in Node 6.
The four-step inner graph develops the general product expansions and
cancellations. The [supplied notes](node7/reference/supplied-outline.md) are retained.

[Video 8](node8/final-contradiction.md) finishes the general argument in two
slides: the nonempty-subset terms vanish, the surviving term is
$u^2/c(1)=\pm u\equiv1$, and this contradicts Node 7's vanishing sum. The
[storyboard](node8/storyboards/odd-ones.svg) separates exact geometric
cancellation from pairing ones after reduction. The theorem concludes
Node 8, and its five-step inner graph includes both remaining examples.
The [supplied outline](node8/reference/supplied-outline.md) is retained
with its pasted mathematics normalized to LaTeX.

## Narrative structure

Write one overview script for each node. The main overviews use $n=36$ as the
guiding example and explain the idea of each lemma. Opening a node develops
the general argument through its smaller steps. Use the known order-four
matrix or the order-16 obstruction when they make a particular step clearer.

This is one sequence of videos through the proof hierarchy. A preview in the
parent page is a cut from the parent's overview; the child's own video gives
the next level of detail.

## Naming and editing

Group each main node's script and its subnode scripts in a numbered folder,
such as `node1/` or `node2/`. Keep the descriptive filenames matching
[../nodes/](../nodes/); `overview.md` stays at the top level for Video 0.

```text
scripts/
├── overview.md
├── node1/
│   ├── group-ring-encoding.md
│   ├── cyclic-group-ring.md
│   ├── cyclic-shifts.md
│   ├── star-operation.md
│   ├── correlation-identity.md
│   ├── hadamard-dictionary.md
│   └── reference/
├── node2/
│   └── restriction-on-the-order.md
├── node3/
│   └── three-evaluations.md
├── node4/
│   ├── delta-theorem.md
│   └── storyboards/
│       └── phase-circles.svg
├── node5/
│   └── signs-become-all-ones.md
├── node6/
│   ├── odd-order-rigidity.md
│   ├── reference/
│   │   └── supplied-outline.md
│   └── storyboards/
│       ├── common-rotation.svg
│       └── render-common-rotation.mjs
├── node7/
│   ├── products-to-sums.md
│   ├── reference/
│   │   └── supplied-outline.md
│   └── storyboards/
│       ├── rotation-cancellation.svg
│       └── render-rotation-cancellation.mjs
└── node8/
    ├── final-contradiction.md
    ├── reference/
    │   └── supplied-outline.md
    └── storyboards/
        ├── odd-ones.svg
        └── render-odd-ones.mjs
```

| Video | Script file | Website node |
| --- | --- | --- |
| 0 — Introduction and Proof Roadmap | [overview.md](overview.md) | [overview](../nodes/overview.md) |
| 1 — Group-Ring Encoding | [node1/group-ring-encoding.md](node1/group-ring-encoding.md) | [Group-Ring Encoding](../nodes/group-ring-encoding.md) |
| 1.1 — Group Ring | [node1/cyclic-group-ring.md](node1/cyclic-group-ring.md) | [Group Ring](../nodes/cyclic-group-ring.md) |
| 1.2 — Cyclic Shifts | [node1/cyclic-shifts.md](node1/cyclic-shifts.md) | [Cyclic Shifts](../nodes/cyclic-shifts.md) |
| 1.3 — Star Operation | [node1/star-operation.md](node1/star-operation.md) | [Star Operation](../nodes/star-operation.md) |
| 1.4 — Correlation Identity | [node1/correlation-identity.md](node1/correlation-identity.md) | [Correlation Identity](../nodes/correlation-identity.md) |
| 1.5 — Hadamard Dictionary | [node1/hadamard-dictionary.md](node1/hadamard-dictionary.md) | [Hadamard Dictionary](../nodes/hadamard-dictionary.md) |
| 2 — Restriction on the Order | [node2/restriction-on-the-order.md](node2/restriction-on-the-order.md) (slide narration and animation directions) | [Restriction on the Order](../nodes/restriction-on-the-order.md) |
| 3 — The Three Evaluations | [node3/three-evaluations.md](node3/three-evaluations.md) (slide narration and animation directions) | [The Three Evaluations](../nodes/three-evaluations.md) |
| 4 — The Δ-Theorem | [node4/delta-theorem.md](node4/delta-theorem.md) (narration and animation directions) | [The Δ-Theorem](../nodes/delta-theorem.md) |
| 5 — Signs Become All Ones | [node5/signs-become-all-ones.md](node5/signs-become-all-ones.md) (draft and proof outline) | [Signs Become All Ones](../nodes/signs-become-all-ones.md) |
| 6 — Odd-Order Rigidity | [node6/odd-order-rigidity.md](node6/odd-order-rigidity.md) (slide narration and animation directions) | [Odd-Order Rigidity](../nodes/odd-order-rigidity.md) |
| 7 — From Products to Sums | [node7/products-to-sums.md](node7/products-to-sums.md) (slide narration and animation directions) | [From Products to Sums](../nodes/products-to-sums.md) |
| 8 — The Final Contradiction | [node8/final-contradiction.md](node8/final-contradiction.md) (slide narration and animation directions) | [The Final Contradiction](../nodes/final-contradiction.md) |

Create a numbered folder when a main node gets its first script, and keep its
supporting sources in that folder's `reference/` directory. Put the video
number and title in the document heading; filenames remain stable if the
recording order changes. No YAML frontmatter is needed here. Keep narration in
ordinary paragraphs and production cues in italic brackets, as in the overview.

Edit the saved script directly as it develops. Keep the existing LaTeX notation
and explicit distinctions between equalities and congruences.

## Connecting a script to the website

The website build reads `nodes/`; it does not automatically publish `scripts/`.
These files are production drafts. For a node with children, adapt its narration
into the children's `script: |` sections beneath the graph. Its own Markdown
body states the result shown in its parent's card. A terminal node keeps its
full explanation in its body. Use `$...$` and `$$...$$` for the website's math
renderer.

For an excerpt introducing a main proof step, put the reader-facing passage in
that child's `script: |` field in [../nodes/overview.md](../nodes/overview.md).
A child node's own video has its own full script in this directory. Animation
directions stay with the production draft.

Once a recording exists, add its `video` source to the node and the real cut
times to the parent-child entries. Leave sources and timings unset until then.
See the [website authoring guide](../README.md) for the field formats.
