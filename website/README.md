# Recursive proof nodes

Build and check with `make -C website check all` from the repository root.
Serve `website/dist/` with a static HTTP server to preview the site. React
pre-renders every node; graph links, breadcrumbs, and parent buttons work
without a client router. Native video cuts use a small playback controller.

Successful pushes to `main` publish the built site to
[GitHub Pages](https://tomasortega.net/circulant-Hadamard/) after all CI checks pass.

## One Markdown file per node

The active outline contains eight high-level proof nodes, with the theorem
concluding Node 8, in one recursive proof journey. The main overviews use $n=36$ as
the guiding example to explain the ideas. Opening a node develops its general
statement and proof through smaller steps. The known order-four matrix and
the order-16 obstruction remain useful supporting examples. The main videos
state results whose detailed arguments appear in the refined nodes.
[Group-Ring Encoding](nodes/group-ring-encoding.md)
expands into five subnodes (1.1–1.5), each with a written proof and a separate
video script. [Restriction on the Order](nodes/restriction-on-the-order.md)
has six detailed nodes (2.1–2.6), each with a written argument and its own
video script. [The Three Evaluations](nodes/three-evaluations.md)
has five detailed nodes (3.1–3.5) alongside its six-slide order-36 overview.
[The Δ-Theorem](nodes/delta-theorem.md) has six steps (4.1–4.6): circle
evaluations, the alternating phase product, local character comparison,
integrality, Kronecker's theorem, and odd order. Its overview script has a
phase-circle storyboard. The detailed nodes prove the local comparison by
descent and give the bounded-polynomial proof of Kronecker's theorem.
Nodes 2.4 and 4.3 state the standard cyclotomic basis and valuation facts
they use, with references to the source paper's Lemma 2.1.
[Signs Become All Ones](nodes/signs-become-all-ones.md) has three smaller
nodes (5.1–5.3): form the integral combination, explain Gaussian parity,
and combine them to obtain the all-ones congruence. Its overview uses nine
coefficients; the inner explanations use general $u$.
[Odd-Order Rigidity](nodes/odd-order-rigidity.md) has five steps (6.1–6.5),
separating odd order, invertible evaluations, sign congruences, rigidity,
and the resulting exact comparisons. Its six-slide overview uses two circles
to show the shared rotation in the nine-position example, derives the
normalized equality, and previews the conflicting residue requirements.
[From Products to Sums](nodes/products-to-sums.md) has four steps (7.1–7.4):
split the exact products, expand using coefficientwise divisibility,
cancel before reduction, and combine into the vanishing alternating sum.
Its three-slide overview recalls the normalized equality from Node 6,
uses the all-ones evaluations to complete the contradiction for $u=3$,
and introduces the general alternating sum. The earlier storyboard remains
a reference for the rotation and cancellation now covered in Node 6.
[The Final Contradiction](nodes/final-contradiction.md) has five steps (8.1–8.5):
evaluate the all-ones polynomial at nontrivial roots and at one, identify
the surviving odd term, contradict Node 7, and conclude the theorem.
The proof-map exposition uses this step to finish the argument for general
odd $u>1$, after the example is settled in Node 7.
Its two-slide script uses the general all-ones evaluations to give one
surviving term and conclude the theorem. The earlier nine-term storyboard
remains a visual reference. The theorem is now inside Node 8; the former
`/nodes/theorem/` URL redirects to its new location.

The homepage presents one proof map: the overviews use order 36 to introduce
the ideas, and following a node develops the general argument. The homepage's
reading-route buttons open the supplementary
[order-36 proof](reading-routes/proof-by-example.md) and
[general odd-u proof](reading-routes/general-proof.md). These readable guides
link into the same eight-node hierarchy and retain their published URLs at
`nodes/proof-by-example/` and `nodes/general-proof/`. The earlier outlines remain
in [the archive](archive/reading-routes/README.md).
Old general-proof-prefixed deeper URLs still
redirect to the corresponding current nodes, including their published videos.

The former background outline is retained in [archive/nodes/](archive/nodes/)
and is not built. Active nodes have new descriptive URLs.

Draft video narration and animation directions in [scripts/](scripts/README.md).
Every one of the 34 refined nodes under Nodes 2–8 has a numbered script
with spoken narration and animation directions for each slide. The
[script index](scripts/README.md#refined-node-scripts) links to all of them.
Keep the introduction in [scripts/overview.md](scripts/overview.md), and group
each main node's script and subnode scripts in a numbered folder: Node 1 uses
[scripts/node1/](scripts/node1/), Node 2 uses [scripts/node2/](scripts/node2/),
Node 3 uses [scripts/node3/](scripts/node3/), Node 4 uses
[scripts/node4/](scripts/node4/), Node 5 uses [scripts/node5/](scripts/node5/),
Node 6 uses [scripts/node6/](scripts/node6/), and Node 7 uses
[scripts/node7/](scripts/node7/). Node 8 uses [scripts/node8/](scripts/node8/).
Retain descriptive filenames such as `group-ring-encoding.md` inside those
folders. These production drafts are not automatically published by the website build.

Adapt the narration into reader-facing explanations under each child's
`script: |` entry in its parent file. A terminal node keeps its full explanation
in its own Markdown body. A node with children uses its body for the goal
statement displayed in its parent's section. Keep video sources and cut timings
unset until supplied.

Edit the `.md` files in [nodes/](nodes/), starting at
[overview.md](nodes/overview.md). Use **node** at every level and name each file
`<id>.md`. The shared vocabulary is in [GLOSSARY.md](../GLOSSARY.md).

Each file begins with YAML frontmatter, followed by its explanation or goal
statement in Markdown. Node references use IDs rather than JavaScript imports:

```markdown
---
id: overview
title: The proof at a glance
shortTitle: Overview
summary: The route through the argument.
video:
  src: media/overview.mp4
  duration: 1200
children:
  - node: question
    dependsOn: []
    segment: { start: 90, end: 210 }
    script: |
      The corresponding cut introduces a sign matrix $H$.

      Its rows should satisfy

      $$
      H H^{\mathsf{T}} = n I_n.
      $$
---

The full written explanation follows the overview's narration.

For a sign matrix $H$, the Hadamard condition is

$$
H H^{\mathsf{T}} = n I_n.
$$
```

`id` defaults to the filename and must match it when supplied. `shortTitle` and
`summary` default to `title`; use plain text for those metadata fields. Omitted
`video` and `children` default to an empty slot and an empty list. A new node
needs a title and a nonempty Markdown body.

The body supports headings, emphasis, lists, links, tables, and LaTeX math.
Write inline math as `$...$` and display math between `$$` lines. Ordinary
LaTeX backslashes need no JavaScript escaping. MathJax generates SVG at build
time, with shared styles in `math.css`. No client-side math script is needed.
Malformed YAML, missing node references, and malformed equations fail the build.

The text is reader-facing exposition, rather than a required verbatim
transcript. The parent file owns each child's section text in an indented
Markdown literal block (`script: |`). For example, Node 1 splits its explanation
among the Group Ring, Cyclic Shifts, Star Operation, Correlation Identity, and
Hadamard Dictionary sections beneath its graph.

The body of a non-root node with children states the main result it establishes.
When its parent omits a child `script`, that body becomes the text in the
parent's corresponding section. Thus the homepage's Group-Ring Encoding
section states the dictionary lemma. An explicit child `script` takes precedence;
for a terminal child, an omitted `script` falls back to its short summary.
Terminal nodes display their complete Markdown explanation on their own pages.
Display order follows the overview's narrative. Reused node IDs preserve each
view's own breadcrumbs, back button, and graph links.

Mark undergraduate prerequisites with `foundation: true` and no children. The
build rejects deeper expansion of a foundation. Keep unfinished proof nodes
marked `draft: true`. The supplied narration outlines remain editable drafts.
Published videos cover the overview, Node 1 and its five children, and Nodes 2–4;
other video slots remain unset until recordings are available.

## Dependency graph

Every view starts with its video. Views with proof children, or with proof
siblings, follow it with a collapsed “Show the proof map” dropdown. All graphs
use the same native disclosure. Expanded proof nodes present the written
exposition across the full child-section width, with a “Dig in deeper”
button beside each heading when space permits and below it on narrow screens.
On the main overview, the Markdown body gives the definitions, example, and
theorem. Use Markdown blockquotes with bold labels and italic statements for
boxed theorems, lemmas, and propositions. The shared renderer supplies the
blue border, subtle background, and padding; keep proofs outside the box. Terminal proof views put their full
explanation after the parent-map disclosure. The graph links to the child nodes. An arrow
points from a prerequisite to a node that uses it. Set `dependsOn` to the IDs
of other children in this view; an empty array means no prerequisite here.
Dependencies determine graph placement independently of narrative order.
Unknown references, duplicate IDs, and dependency cycles fail the build.

Use `contextFrom` for shared-notation links. These are validated but are not
logical prerequisites; in particular the Δ-theorem does not depend on the
Hadamard signs. All connections use the same solid arrow styling; the statement
pages explain their inputs in words. The overview's `graphLayout: proof-map`
uses each node's `mapPosition: [x, y]` and `mapSummary` to match the supplied diagram. Map summaries
support inline Markdown and `$...$` math, rendered at build time like the article.
Use optional `mapTitle` for a mathematical graph title while retaining a plain
`shortTitle` for navigation. Keep links, images, and block Markdown out of labels. Use
`graphTitle` to label a refined map; its height follows the node positions. `number`
keeps the eight node numbers stable. Maps use the website's ruled headings,
white nodes with subtle blue outlines, blue numbers, and serif math summaries.
The current node and hovered or keyboard-focused links receive a blue tint and
stronger outline. Elbow connections use curved bends.

Page headings show only the node title.
Terminal statement pages list their prerequisites and shared notation. No disclosure
contains an invented internal proof.

At a terminal node, the graph shows its siblings and highlights the current
node. Native SVG links support clicking and keyboard navigation. Wide graphs
scroll horizontally on small screens. The initial dependency maps are drafts.

## One long video per node

Every node owns a full overview video. Its children's preview players use cuts
of that same source. Opening a child shows its own long, more detailed overview,
with cuts for its children in turn.

Use `youtubeId: YOUR_VIDEO_ID` for YouTube or `src` for a hosted/local file.
The optional `duration` gives the full length in seconds. A local example:

```yaml
video:
  src: media/overview.mp4
  captions: media/overview.vtt
  poster: media/thumbnails/overview.jpg
  duration: 1200
```

Put local media under `website/media/`; it is copied into the build. Relative
paths work at every depth. `segment.start` and `segment.end` are seconds from
the start of the parent's full video. YouTube IDs have 11 characters and its
cut times use whole seconds. File videos allow fractional seconds. A cut must
have `0 <= start < end`, within the duration when supplied.

For native file videos, `poster` supplies the thumbnail shown before playback.
Keep each video's image in `media/thumbnails/<node-id>.jpg`, selected from a
representative frame of that video to preserve its mathematical typography and
visual style. Each timed excerpt can set `segment.poster` to an image selected
from that part of the parent's video, under
`media/thumbnails/excerpts/<child-id>.jpg`. Without it, the excerpt inherits the
parent's poster. Opening a child shows the child's own full video and thumbnail.
The build copies these images and refreshes them when a thumbnail changes.

Leave `video` or `segment` as `null` until the source or timing is known. An
unset cut stays an empty slot even if its parent's full video is available.
The current draft deliberately contains no invented timings.

YouTube cuts use its start/end parameters. Native file cuts use media fragments
and a small controller that stops at the end, bounds seeking, and restarts the
cut on replay. Full overviews keep ordinary controls. Videos never autoplay.

Bottom-right page controls share the current URL and jump to the top after
scrolling. Sharing uses the native share sheet or falls back to copying the link.

The shared renderer is [node.jsx](node.jsx), with the pinned
[3Blue1Brown styling](vendor/README.md). Parsing and math rendering are in
[load-nodes.js](load-nodes.js) and [markdown.js](markdown.js).

The [phase explorer](phase-explorer.jsx) has two stages. Node 6 derives equality
of the normalized evaluations from the definition of $E(P)$. Its diagram shows
the common rotation of the values of $c(P),d(P),g(P),E(P)$ and previews the
incompatible residue requirements. Node 7 and its final sum section add the
division control, with the algebraic contradiction in the exposition above
the diagram. The two widgets operate independently. Their labels show the
actual evaluation arguments and use build-time MathJax, including the normalized
fractions. Only the values of $c(P),d(P),g(P)$ must lie on the radius-three
circle; the values of $E(P)$ can lie outside it. The diagram is
pre-rendered; a small [controller](phase-explorer.js) enables native controls.
Its [model](phase-model.js) keeps circle geometry separate from the later
arithmetic requirements. The chosen points are schematic, not values from an
order-36 circulant Hadamard matrix. The explanation and initial diagram remain available
without JavaScript; there is no automatic animation or network request.
