# Use one dropdown for every graph view

- Recorded at: 2026-11-14T21:59:25-08:00
- Observed work interval: 2026-11-14T21:57:27-08:00/2026-11-14T21:59:25-08:00
  (118 seconds through this record).
- Participants: user (consistency and simplification request); OpenAI Codex,
  GPT-6 (regression tests, implementation, documentation, and checks).

## Context and decision

The user reported graph views that were not dropdowns and requested a unified,
simpler implementation. Make [DependencyGraph](../website/dependency-graph.jsx)
return one native, initially collapsed disclosure labeled “Show the proof map”
for every graph. Remove the conditional parent-map wrapper, temporary graph
variable, and redundant navigation classes. Keep graph ownership and both
layout algorithms intact. Update the [authoring guide](../website/README.md).

This extends the parent-map disclosure discussed in the
[reading-order decision](2026-11-14-170447-video-graph-text-reading-order.md)
to all graphs following the
[general-route hierarchy change](2026-11-14-215449-nest-proof-pages-under-general-route.md).

## Rationale

A single return path makes collapse behavior independent of graph layout and
whether a page shows its own map or its parent's. Native disclosures preserve
ordinary links and keyboard controls without adding client JavaScript.
Direct static-page regressions reproduced the issue, so broader speculative
debugging was unnecessary. Used the diagnosing-bugs skill.

## Evidence and outcome

- Added regressions before implementation. The generated-page check failed on
  both expanded proof maps because they had no disclosure; other proof views
  had the old parent-specific label. Automatic-layout fixtures also failed for
  both their own and parent views because neither had a disclosure.
- After implementation, an existing refinement assertion still expected the
  old label. Updated that assertion to the shared label.
- `make -C website check` passed: 66 tests and 5,191 assertions, including all
  17 generated pages and automatic-layout fixtures. `make -C website` rebuilt
  17 pages and compiled the stylesheet.
- `uv run --locked prek -a --quiet` and `git diff --check` passed.
- An HTTP comparison confirmed the existing preview on
  [port 4174](http://127.0.0.1:4174/) serves all 17 current built pages exactly.
  Browser visual inspection was unavailable because the computer-use browser
  access host was unavailable; no interactive or visual QA is claimed.
- No commit, push, or hosted deployment was requested or performed.

## Report relevance

This records a user-directed presentation correction and AI-assisted code
simplification, checked through static rendering, regressions, and a local
HTTP preview. No mathematical content or proof dependencies were changed.
