# Recursive proof nodes

Build and check with `make -C website check all` from the repository root.
Serve `website/dist/` with a static HTTP server to preview the site. React
pre-renders every node; graph links, breadcrumbs, and parent buttons work
without a client router. Native video cuts use a small playback controller.

## One file per node

Edit the files in [nodes/](nodes/), starting at [overview.js](nodes/overview.js).
Each file exports one node and imports its child nodes. Use **node** at every
level; name each file `<id>.js`. The shared vocabulary is in
[GLOSSARY.md](../GLOSSARY.md).

A node defines its `id`, `title`, `shortTitle`, `summary`, `video`, `script`, and
`children`. Each child entry links a node to a cut from this parent's video:

```js
import detail from "./detail.js";

export default {
  id: "overview",
  title: "The proof at a glance",
  shortTitle: "Overview",
  summary: "The route through the argument.",
  video: { src: "media/overview.mp4", duration: 1200 },
  script: ["The written introduction follows the opening narration."],
  children: [
    {
      node: detail,
      dependsOn: [],
      segment: { start: 90, end: 210 },
      script: ["A written explanation following this cut's narration."],
    },
  ],
};
```

`script` is the draft narration outline and its readable written explanation.
It need not be a word-for-word transcript. The parent file owns the script
excerpt for each cut; the child's own file owns the deeper explanation.
Display order follows the overview's narrative. Node IDs must be stable slugs.
Reusing a node file under multiple parents keeps each view's own breadcrumbs,
back button, and graph links.

Mark undergraduate prerequisites with `foundation: true` and no children. The
build rejects deeper expansion of a foundation. Keep unfinished proof nodes
marked `draft: true`. The supplied script outlines are drafts, and the proof
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
of that same source, rather than independent uploads. Opening a child shows its
own long, more detailed overview, with cuts for its children in turn.

Configure a node's `video` once:

- YouTube: `{ youtubeId: "YOUR_VIDEO_ID", duration: 1200 }`.
- Hosted file: `{ src: "https://example.com/overview.mp4", duration: 1200 }`.
- Local file: `{ src: "media/overview.mp4", captions: "media/overview.vtt", duration: 1200 }`.

Put local media under `website/media/`; it is copied into the build. Relative
paths work at every depth. `duration`, `segment.start`, and `segment.end` are
seconds from the start of the parent's full video. YouTube IDs have 11
characters and its cut times use whole seconds. File videos allow fractional
seconds. A cut must have `0 <= start < end`, within the duration when supplied.

Leave `video` or `segment` as `null` until the source or timing is known. An
unset cut stays an empty slot even if its parent's full video is available.
The current draft deliberately contains no invented timings.

YouTube cuts use its start/end parameters. Native file cuts use media fragments
and a small controller that stops at the end, bounds seeking, and restarts the
cut on replay. Full overviews keep ordinary controls. Videos never autoplay.

The shared renderer is [node.jsx](node.jsx), with the pinned
[3Blue1Brown styling](vendor/README.md). The dependency graph is in
[dependency-graph.jsx](dependency-graph.jsx).
