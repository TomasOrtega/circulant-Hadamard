# Preserve reading guides after the complete proof-map merge

- Recorded at: 2026-11-15T02:57:20-08:00.
- Observed review interval: 2026-11-15T02:51:05-08:00/2026-11-15T02:54:51-08:00 (226 seconds).
- Observed restoration and validation interval: 2026-11-15T02:55:38-08:00/2026-11-15T02:57:20-08:00 (102 seconds through this record).
- Participants: Tomas Ortega (existing navigation requirement); Steven Creech
  (expanded proof map); OpenAI Codex, GPT-6 (review, restoration, and checks).

## Context and decision

PR #10 merged the complete proof map at `04fef7c`. Its navigation changes
removed the two reading-guide buttons and redirected both readable guides.
Preserve Tomas's [explicit restoration request](2026-11-14-230907-restore-reading-route-entrypoints.md),
implemented in `0a44d61`, while retaining the new full-width sections and phase
controls. This reverses only the guide-removal portion of Steven's
[single-journey decision](2026-11-15-001404-restore-single-proof-map-and-widen-node-sections.md).
The historical records remain unchanged.

Restore homepage-only ordinary buttons and build the existing supplementary
guides at their published URLs. Keep both outside the eight-node hierarchy.
Restore guide sources as Makefile dependencies and correct the contradictory
authoring guidance. No proof, media, caption, cut, or phase-model source changes.

## Rationale

Supplementary guides can provide the requested entry points while linking
into one shared proof hierarchy. Their existing prose and renderer suffice;
no duplicate subtree or client navigation is needed. The writing-for-agents
skill informed the concise positive instruction in `website/AGENTS.md`.

## Evidence and outcome

- Restored positive tests first: five failures confirmed missing buttons,
  guide text, and supplementary build entries. Evidence:
  `videos/build/reading-routes-pr10-regression.log` (ignored).
- After restoration, all 147 website tests pass (8,516 assertions), including
  guide links/return anchors, legacy redirects, video cuts, and phase controls.
  The production build emits 50 pages; scoped whitespace checks pass.
- The detached PR review also passed its original 145 tests and 48-page build.
  This child's browser host was unavailable and local server binding was
  sandbox-denied, so no fresh screenshot inspection is claimed.
- Root handles final repository lint, commit, and push separately.

## Report relevance

Records a navigation-preservation repair during integration, with observed
failing-first evidence. The expanded mathematics and interactive illustration
remain unchanged; this task adds no mathematical proof or formal verification.
