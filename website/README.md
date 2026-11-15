# Recursive proof nodes

Build and check with `make -C website check all` from the repository root.
Serve `website/dist/` with a static HTTP server to preview the site. React
pre-renders every node; graph links, breadcrumbs, and parent buttons work
without a client router. Native video cuts use a small playback controller.

## One Markdown file per node

The homepage owns the eight high-level proof nodes in one recursive map.
Main overviews use order 36 as a guiding example; deeper nodes explain the
general argument. Proposition 2.2 remains an accepted input at this level.
[Group-Ring Encoding](nodes/group-ring-encoding.md) and
[The Three Evaluations](nodes/three-evaluations.md) each expand into five
subnodes. [The Δ-Theorem](nodes/delta-theorem.md) has six steps (4.1–4.6):
circle evaluations, the alternating phase product, local character comparison,
integrality, Kronecker's theorem, and odd order. Its detailed outline retains
the technical character-comparison lemma (Lemma 3.1) and Kronecker's theorem
as stated inputs. The theorem concludes Node 8. Other detailed graphs remain in
preparation.

The homepage's reading-route buttons open the supplementary
[order-36 proof](reading-routes/proof-by-example.md) and
[general odd-u proof](reading-routes/general-proof.md). These readable guides
use the same eight-node hierarchy; they do not duplicate its proof nodes.
They retain their published URLs at `nodes/proof-by-example/` and
`nodes/general-proof/`. Old general-proof-prefixed deeper URLs still redirect
to the corresponding current nodes, including their published videos.
The earlier route files remain in [the archive](archive/reading-routes/README.md).

The former background outline is retained in [archive/nodes/](archive/nodes/)
and is not built. Active nodes have new descriptive URLs.

Draft video narration and animation directions in [scripts/](scripts/README.md).
Keep the introduction in [scripts/overview.md](scripts/overview.md), and group
each main node's script and subnode scripts in a numbered folder: Node 1 uses
[scripts/node1/](scripts/node1/). Create the other numbered folders as their
scripts are added.
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
marked `draft: true`. The supplied narration outlines are drafts, and the proof
argument and videos still await the team's material.

## Dependency graph

Every view starts with its video. Views with proof children, or with proof
siblings, follow it with a collapsed “Show the proof map” dropdown. All graphs
use the same native disclosure. Expanded proof nodes present the written
exposition in the child sections, with a deeper link for each step.
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
Terminal statement pages list their incoming and outgoing links. No disclosure
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
  duration: 1200
```

Put local media under `website/media/`; it is copied into the build. Relative
paths work at every depth. `segment.start` and `segment.end` are seconds from
the start of the parent's full video. YouTube IDs have 11 characters and its
cut times use whole seconds. File videos allow fractional seconds. A cut must
have `0 <= start < end`, within the duration when supplied.

Leave `video` or `segment` as `null` until the source or timing is known. An
unset cut stays an empty slot even if its parent's full video is available.
The current draft deliberately contains no invented timings.

YouTube cuts use its start/end parameters. Native file cuts use media fragments
and a small controller that stops at the end, bounds seeking, and restarts the
cut on replay. Full overviews keep ordinary controls. Videos never autoplay.

The shared renderer is [node.jsx](node.jsx), with the pinned
[3Blue1Brown styling](vendor/README.md). Parsing and math rendering are in
[load-nodes.js](load-nodes.js) and [markdown.js](markdown.js).
