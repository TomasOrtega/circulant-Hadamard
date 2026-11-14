# Recursive proof nodes

Build and check with `make -C website check all` from the repository root.
Serve `website/dist/` with a static HTTP server to preview the site. React
pre-renders every node; graph links, breadcrumbs, and parent buttons work
without a client router. Native video cuts use a small playback controller.

## One Markdown file per node

Edit the `.md` files in [nodes/](nodes/), starting at
[overview.md](nodes/overview.md). Use **node** at every level and name each file
`<id>.md`. The shared vocabulary is in [GLOSSARY.md](../GLOSSARY.md).

Each file begins with YAML frontmatter, followed by its written script and
explanation in Markdown. Node references use IDs rather than JavaScript imports:

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

The body is the node's readable script and explanation, rather than a required
verbatim transcript. The parent file owns each cut's `script` as an indented
Markdown literal block (`|`); the child's own file owns the deeper explanation.
Display order follows the overview's narrative. Reused node IDs preserve each
view's own breadcrumbs, back button, and graph links.

Mark undergraduate prerequisites with `foundation: true` and no children. The
build rejects deeper expansion of a foundation. Keep unfinished proof nodes
marked `draft: true`. The supplied narration outlines are drafts, and the proof
argument and videos still await the team's material.

## Dependency graph

The graph directly below each overview links to the child nodes. An arrow
points from a prerequisite to a node that uses it. Set `dependsOn` to the IDs
of other children in this view; an empty array means no prerequisite here.
Dependencies determine graph placement independently of narrative order.
Unknown references, duplicate IDs, and dependency cycles fail the build.

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
