# Simplify the proof graph's visual language

- Recorded at: 2026-11-14T15:34:01-08:00
- Observed work interval: 2026-11-14T15:33:06-08:00/2026-11-14T15:34:01-08:00 (55 seconds).
- Participants: Steven Creech (request); Codex (GPT-6, implementation and checks).

## Context and decision

The user requested a simple graph matching the website, without branch colors
or a dashed connection. This supersedes the visual encoding selected in the
[eight-node proof-map decision](2026-11-14-151609-eight-node-proof-map.md).

Use white node backgrounds, the existing blue accent for outlines and
hover/current-node emphasis, and uniform solid gray arrows. Remove the purple
color extension, unused branch metadata, and the color/dash legend. Update
the overview and authoring guide to describe the simplified presentation.

## Rationale

The extra visual categories distracted from the user's high-level reading
route. Preserve all nodes and connections while reducing the styling to the
site's existing palette. Keep shared-notation information in the data and
statement-page explanations so simplifying the drawing does not turn the
Δ-theorem into a consequence of Hadamard signs. Describe graph connections
neutrally rather than incorrectly calling every edge a logical dependency.

## Evidence and outcome

All 34 website tests passed (955 assertions), including the existing edge and
navigation checks with updated appearance expectations. The production build
emitted all 12 pages. A desktop screenshot confirmed uniform nodes and solid
arrows; the refreshed local website was opened in the user's browser. The
vendored stylesheet, mathematical content, node layout, and video slots were
preserved. Source whitespace checks passed. The all-files lint command
reported the earlier moved paths as missing, as before; explicit-file lint
passed for all 89 existing tracked and new files.

## Report relevance

This is a user-directed presentation refinement, not a mathematical change.
The earlier styling decision remains recorded; the new choice improves
consistency with the website while preserving the proof map's content.

Final checks recorded at 2026-11-14T15:34:19-08:00; follow-up work interval
2026-11-14T15:34:01-08:00/2026-11-14T15:34:19-08:00.
