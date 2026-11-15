# Video scripts

Write and revise video production drafts here, including spoken narration,
equations, animation directions, and recording notes. These are working
production drafts.

[overview.md](overview.md) contains Steven's supplied **Video 0 — Introduction
and Proof Roadmap** script, preserving its wording and animation cues.

## Naming and editing

Use the same filename as the corresponding file in [../nodes/](../nodes/):

| Video | Script file | Website node |
| --- | --- | --- |
| 0 — Introduction and Proof Roadmap | [overview.md](overview.md) | [overview](../nodes/overview.md) |
| 1 — Group-Ring Encoding | `group-ring-encoding.md` (next draft) | [Group-Ring Encoding](../nodes/group-ring-encoding.md) |
| 2 — Restriction on the Order | `restriction-on-the-order.md` (future draft) | [Restriction on the Order](../nodes/restriction-on-the-order.md) |

Continue with the matching node IDs for the remaining videos. Put the video
number and title in the document heading; filenames remain stable if the
recording order changes. No YAML frontmatter is needed here. Keep narration in
ordinary paragraphs and production cues in italic brackets, as in the overview.

Edit the saved script directly as it develops. Keep the existing LaTeX notation
and explicit distinctions between equalities and congruences.

## Connecting a script to the website

The website build reads `nodes/`; it does not automatically publish `scripts/`.
These files are production drafts, while each node's Markdown body is its
reader-facing explanation. When the script is ready, adapt its narration into
that body and use `$...$` and `$$...$$` for the website's math renderer.

For an excerpt from the overview, put the corresponding reader-facing passage
in that child's `script: |` field in [../nodes/overview.md](../nodes/overview.md).
A child node's own video has its own full script in this directory. Animation
directions stay with the production draft.

Once a recording exists, add its `video` source to the node and the real cut
times to the parent-child entries. Leave sources and timings unset until then.
See the [website authoring guide](../README.md) for the field formats.
