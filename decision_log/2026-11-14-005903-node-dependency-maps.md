# Navigate with node dependency maps

- Recorded at: 2026-11-14T00:59:03-08:00
- Observed work interval: 2026-11-14T00:33:38-08:00/2026-11-14T00:59:03-08:00
- Participants: user (graph requirement); Codex (model, renderer, and checks).

## Context and decision

Place a clickable dependency graph immediately below each node's overview.
Declare prerequisites separately from narrative order using child-node IDs.
Arrows point from a prerequisite to the node that uses it.

Use [dependencies.js](../website/dependencies.js) for validation and topological
layers and [dependency-graph.jsx](../website/dependency-graph.jsx) for SVG links.
At terminal nodes, show the parent's map with the current node highlighted so
readers can navigate to siblings.

## Rationale

Dependencies can branch or converge independently of the video's order.
Static SVG links keep graph navigation available without a client router.
The maps reuse the existing theme, fonts, and colors. Wide maps scroll on
small screens, and their links are keyboard focusable.

## Evidence and outcome

Tests cover a branching dependency graph, missing references, cycles, graph
placement, and graph links at every depth. A terminal-view regression test
failed before adding the sibling-map fallback and passed afterward.

All 21 tests and the clean production build passed. Each of the 12 generated
pages contains a graph. Browser visual QA remained unavailable in this session.

## Report relevance

The initial maps are labeled drafts and describe the planned exposition.
They do not establish new logical dependencies in a completed mathematical
proof. Codex implemented and checked the model and navigation.
