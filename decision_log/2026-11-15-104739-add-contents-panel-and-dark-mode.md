# Adapt the contents panel and dark-mode switch

- Recorded at: 2026-11-15T10:47:39-08:00
- Observed primary interval: 2026-11-15T10:31:49-08:00/2026-11-15T10:47:39-08:00 (950 seconds).
- Parallel source/browser audit intervals: 2026-11-15T10:41:52-08:00/2026-11-15T10:43:39-08:00 (107 seconds) and 2026-11-15T10:43:57-08:00/2026-11-15T10:44:54-08:00 (57 seconds).
- Parallel interaction verification: 2026-11-15T10:41:58-08:00/2026-11-15T10:46:19-08:00 (261 seconds, including preparation/build wait). Intervals overlap and are not additive person-hours.
- Participants: Tomas Ortega (issue and parallel-work authorization); OpenAI
  Codex, GPT-6 (implementation and two read-only verification agents).

## Context and decision

[Issue #21](https://github.com/TomasOrtega/circulant-Hadamard/issues/21)
requests a 3Blue1Brown-style top-left contents button instead of the inline
subnode list, plus its footer dark-mode button. Inspect the pinned upstream
TableOfContents, DarkMode, Heading, Footer, and root components. Adapt the
contents panel with a native popover and current-page heading links; retain
existing node anchors. Add a footer switch and remembered appearance using
the existing palette, applying saved state before styles load.

This extends the [corner-control adaptation](2026-11-15-095039-add-share-and-jump-controls.md).
The user explicitly authorized parallel work; independent checks run beside
implementation, while another isolated worktree handles issue #22.

## Rationale

Native popovers provide keyboard activation, Escape, and light dismissal
without client React or a dialog dependency. The [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
is baseline across current browsers since January 2025, meeting the project's
one-year compatibility convention at this task's date. Generate ordinary
heading links, preserve mathematical heading labels, guard unavailable storage,
and keep the proof readable without JavaScript. Existing corner controls use
literal white so their blend-mode contrast survives the theme change. Print
temporarily uses the light palette and then restores the chosen appearance.

## Evidence and outcome

- All 181 website tests pass (9,528 assertions); all 48 active pages build.
  Repository lint and whitespace checks pass. The complete minified page
  controller is 2.19 KB; no dependency is added.
- Independent checks found and reproduced an unscrollable short-screen panel,
  masthead overlap, and stale visibility after resizing. Explicit viewport
  height, a sticky close control, masthead-aware visibility, and a resize
  listener fix these cases.
- Chromium and Firefox audits cover all 48 pages and 161 generated contents
  links per browser: every target exists, labels are nonempty, IDs stay unique,
  and no nested anchors or JavaScript errors appear.
- 216 focused browser assertions cover keyboard/dismissal behavior, node and
  terminal-heading links, four desktop/mobile/short viewports, saved and
  cross-tab appearance, denied storage, contrast, and print. A Chromium PDF
  renders light and restores dark mode afterward. Screenshots were inspected.
  Safari, physical phones, and the operating-system share sheet were not tested.

## Report relevance

Records user-directed navigation and appearance controls, including parallel
review and observed corrections. Mathematical exposition and media are unchanged.
