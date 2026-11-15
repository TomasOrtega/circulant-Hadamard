# Introduce the theorem between the overview video and graph

- Recorded at: 2026-11-14T16:23:45-08:00
- Observed work interval: 2026-11-14T16:22:06-08:00/2026-11-14T16:23:45-08:00 (99 seconds).
- Participants: Steven Creech (request); Codex (GPT-6, text, layout, and checks).

## Context and decision

The user said their colleague is making the overview video and requested
paper-style text between it and the graph: state the main theorem, explain
that the dependency graph follows, and invite readers to click nodes.

Render [overview.md](../website/nodes/overview.md)'s Markdown body between the
video and graph on the main overview. State the theorem once, followed by
brief context and the graph instructions. Remove the previous duplicate
hardcoded statement above the video. Other node views retain their existing
text placement. Update the website authoring guide and agent instructions to
reflect this user-requested exception to immediate video-to-graph placement.

## Rationale

Keep the introduction in the existing editable Markdown source rather than
adding another content field or embedding mathematical prose in JSX. Use the
site's serif text, white background, and existing spacing utilities for a
paper-like reading block. Preserve the cited source, example-first route,
accepted-black-box framing, and the
[simplified graph styling](2026-11-14-153401-simplify-proof-graph-style.md).
The production video script remains separate and unchanged.

## Evidence and outcome

All 34 website tests passed (955 assertions), and the production build emitted
12 pages. A generated-HTML check confirmed the ordering video, theorem,
navigation explanation, graph, with exactly one main-theorem statement.
Source whitespace checks passed. A desktop browser screenshot was inspected,
and the updated localhost preview was opened for the user. Repository lint
and targeted lint for this new record passed. No mathematical statement was newly established or verified;
this relocates and restates the theorem already used in the supplied proof map.

## Report relevance

This is an AI-assisted exposition and page-order refinement requested by the
user. It makes the main theorem and the purpose of the graph available as
written text alongside the forthcoming overview video.

Final checks recorded at 2026-11-14T16:23:55-08:00; follow-up interval
2026-11-14T16:23:45-08:00/2026-11-14T16:23:55-08:00.
