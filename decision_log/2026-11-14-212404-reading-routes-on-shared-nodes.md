# Leave reading routes unselected on shared proof nodes

- Recorded at: 2026-11-14T21:24:04-08:00
- Observed work interval: 2026-11-14T21:19:10-08:00/2026-11-14T21:24:04-08:00
  (294 seconds through this record, overlapping the styling and heading work).
- Participants: Tomas Ortega (issue author and goal to close all open issues);
  OpenAI Codex, GPT-6 (diagnosis, implementation, and checks).

## Context and decision

The user's active goal was to close all open issues. GitHub listed two:
[#3, Button shade](https://github.com/TomasOrtega/circulant-Hadamard/issues/3),
and [#4, Too many titles](https://github.com/TomasOrtega/circulant-Hadamard/issues/4).
Read both complete issue bodies and confirmed Tomas authored them, with no
additional comments.

Issue 3 describes opening a shared node from the general proof and seeing the
example button shaded. The [earlier fix](2026-11-14-210008-fix-reading-route-highlight.md)
corrected the route pages themselves but retained that fallback elsewhere.
Limit the example's fallback emphasis to the homepage. Shared proof nodes
leave both routes unselected; each route page highlights itself.

## Rationale

A shared proof node's URL identifies its statement, without identifying the
reading route used to reach it. A default example highlight implies a selection
that did not occur. Keep navigation static and reserve current-route feedback
for the route's own page, while retaining the homepage's recommended entry.

## Evidence and outcome

- Added the shared-node regression before implementation. It failed on
  Group-Ring Encoding because the example still had the filled-button style.
- The final regression checks all 14 shared node pages, alongside the existing
  checks for both route pages. All 46 website tests passed; the build emitted
  17 pages, and lint and whitespace checks passed.
- Safari navigation from the General Odd-u Proof to From Products to Sums
  confirmed that both route buttons remain unselected.
- The issue will be closed after the implementation is pushed; publication
  and closure outcomes will be recorded separately.

## Report relevance

This extends an earlier interface correction to the actual shared-node path
reported in GitHub. It changes navigation feedback, not mathematical content.
