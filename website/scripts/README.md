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

## Naming and editing

Group each main node's script and its subnode scripts in a numbered folder,
such as `node1/` or `node2/`. Keep the descriptive filenames matching
[../nodes/](../nodes/); `overview.md` stays at the top level for Video 0.

```text
scripts/
├── overview.md
└── node1/
    ├── group-ring-encoding.md
    ├── cyclic-group-ring.md
    ├── cyclic-shifts.md
    ├── star-operation.md
    ├── correlation-identity.md
    ├── hadamard-dictionary.md
    └── reference/
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
| 2 — Restriction on the Order | `node2/restriction-on-the-order.md` (future addition) | [Restriction on the Order](../nodes/restriction-on-the-order.md) |

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

For an excerpt from the overview, put the corresponding reader-facing passage
in that child's `script: |` field in [../nodes/overview.md](../nodes/overview.md).
A child node's own video has its own full script in this directory. Animation
directions stay with the production draft.

Once a recording exists, add its `video` source to the node and the real cut
times to the parent-child entries. Leave sources and timings unset until then.
See the [website authoring guide](../README.md) for the field formats.
