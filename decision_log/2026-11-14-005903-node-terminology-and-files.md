# Use nodes and one content file per node

- Recorded at: 2026-11-14T00:59:03-08:00
- Observed work interval: 2026-11-14T00:39:58-08:00/2026-11-14T00:59:03-08:00
- Participants: user (terminology and file organization); Codex (implementation and checks).

## Context and decision

The user requested separate content files and a standard name at every depth:
**node**. Split the former content tree into 12 files in
[website/nodes/](../website/nodes/), starting at
[overview.js](../website/nodes/overview.js).

Use the same vocabulary in the renderer, build, tests, interface, URLs, and
authoring guide. Record definitions in [GLOSSARY.md](../GLOSSARY.md).
This revises the [recursive lesson structure](2026-11-14-002050-recursive-lesson-hierarchy.md).

## Rationale

Each file owns one node's overview, script, and child references. Parent links
own the cut timing and narration used to introduce a child. Reused node files
retain navigation within each parent's context.

Moved source links in historical records now point to the committed snapshot
before this refactor. Those link-maintenance notes preserve the original
decisions and their terminology.

## Evidence and outcome

All 21 tests and a clean frozen-install production build passed, generating
12 node pages. Tests cover per-node files, deep links, parent navigation,
undergraduate stopping points, and the retained footer wording.

A reused-file navigation test failed before the parent-context lookup fix
and passed afterward. The authoring guide and agent instructions were updated.

## Report relevance

This records an organizational and terminology choice implemented by Codex.
The work resumed after an interruption with the user's node-naming request.
