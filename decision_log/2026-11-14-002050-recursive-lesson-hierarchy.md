# Organize the proof as recursive lessons

- Recorded at: 2026-11-14T00:20:50-08:00
- Observed work interval: 2026-11-14T00:03:39-08:00/2026-11-14T00:20:50-08:00
- Participants: user (structure, draft-content approval, and navigation requirements); Codex (implementation and checks).

## Context and decision

The user requested a 3Blue1Brown-style lesson with an overview video, written
explanations, chapter clips, and a right-hand “Dig in deeper” link for each
chapter. Deeper views repeat that structure. Every non-root view also has a
visible button back to its direct parent.

Use a recursive content tree in [lessons.js](https://github.com/TomasOrtega/circulant-Hadamard/blob/eff0cad336c140ddd677560ca64e25d2da4cf723/website/lessons.js). Stop at
standard undergraduate prerequisites: foundation nodes are leaves, enforced
by the build. Breadcrumbs allow larger jumps, and parent buttons return to the
corresponding chapter in the higher-level view.

The user explicitly approved draft chapters and empty video slots. Seed 12
views covering the question, cyclic structure, and draft argument sections.
Keep the proof material marked as unfinished.

## Rationale

A single tree keeps the chapter previews, deep links, numbering, and parent
relationships consistent. The depth follows the mathematics rather than an
arbitrary number of pages. Undergraduate foundations do not expand further.

The report currently supplies background rather than a completed proof.
Draft proof slots preserve the intended structure without inventing results.
Empty video slots have labels and no inactive playback controls.

## Evidence and outcome

Eight tests passed, including every generated page's chapter and parent links,
breadcrumbs and return anchors, undergraduate stopping points, media slots,
configured video players, and CSS paths at depth. All 12 pages built successfully
from a clean frozen install.

The order-four example was checked by computing every cyclic correlation;
this is evidence for that example only. Browser preview was unavailable.

## Report relevance

This records the presentation structure and AI-assisted drafting and
implementation. The draft proof sections establish no mathematical result.
The background comes from the existing report, with the small example checked
directly.

Link maintenance (2026-11-14): moved source links now point to the snapshot
before the node refactor; the original decision is unchanged.
