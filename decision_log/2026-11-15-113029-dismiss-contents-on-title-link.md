# Dismiss contents on title navigation

- Recorded at: 2026-11-15T11:30:29-08:00
- Observed implementation/check interval: 2026-11-15T11:27:32-08:00/2026-11-15T11:30:29-08:00 (177 seconds).
- Participants: Tomas Ortega (request); OpenAI Codex, GPT-6 (implementation
  and browser checks).

## Context and decision

The user requests that clicking the top contents item dismiss the panel,
like 3Blue1Brown. Reuse the existing close action for the first heading link.
Hide the toggle while the title remains in view; other section links retain
open contents. Preserve native anchor navigation and the
[existing transitions](2026-11-15-112211-inherit-contents-transitions.md).
This adds the requested exception to the
[persistent sidebar decision](2026-11-15-111048-keep-contents-open-beside-text.md).

## Rationale

The pinned upstream
[TableOfContents.tsx](https://github.com/3b1b/3Blue1Brown.com/blob/4bcd89ef6e61e35001f58a58753226939eda3d89/app/components/TableOfContents.tsx)
hides the panel near the opening section. Adapt that behavior to our separate
toggle and reserved desktop space with two controller-line changes, without
new state, timers or dependencies. Update the documented title-link exception.

## Evidence and outcome

Eight browser cases fail to close the title link before the change and pass
after it: Chromium/Firefox, desktop/phone, pointer/animated and keyboard/reduced
motion. All 48 focused assertions pass, including section links staying open,
the existing heading scroll margin, dismissal, hidden toggle and reopening.
The prior 176 animation/accessibility assertions also pass in both browsers.
All 185 website tests (10,009 assertions), the 48-page build, repository lint
and whitespace checks pass. Safari and physical phones were not tested.
Browser harnesses are temporary; no project dependency is added.

## Report relevance

Records a user-directed navigation refinement and failed-first browser checks.
Mathematical content and media are unchanged.

Publication check at 2026-11-15T11:33:25-08:00: all 48 focused browser assertions
also pass on the live site; its controller matches the tested build byte for
byte. The [CI run](https://github.com/TomasOrtega/circulant-Hadamard/actions/runs/43752811176)
passes its website, lint and deployment jobs.
