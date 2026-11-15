# Keep contents navigation open beside the text

- Recorded at: 2026-11-15T11:10:48-08:00
- Observed primary interval: 2026-11-15T11:00:35-08:00/2026-11-15T11:10:48-08:00 (613 seconds through implementation, integration and checks).
- Independent reference/browser review: 2026-11-15T11:00:34-08:00/2026-11-15T11:08:23-08:00 (469 seconds; final automated run ended at 2026-11-15T11:07:52.988-08:00). This overlaps the primary interval and is not additive person-hours.
- Participants: Tomas Ortega (issue and parallel-work authorization); OpenAI
  Codex, GPT-6 (implementation and independent browser review).

## Context and decision

[Issue #24](https://github.com/TomasOrtega/circulant-Hadamard/issues/24)
reports contents overlapping article text and closing after heading navigation,
and requests moving the appearance switch to the top right. Replace the
native popover with a fixed, nonmodal contents panel and ordinary heading links.
Keep its open state across those links. Reserve its width at the existing
70-rem desktop breakpoint; use a dismissible drawer on narrower screens.
Move the single appearance switch from the footer to the masthead's top right.
This supersedes those layout choices in the
[original controls decision](2026-11-15-104739-add-contents-panel-and-dark-mode.md).

Work in an isolated branch, then rebase onto `41b0b69` to retain the separately
completed placeholder removal (#23), homepage-copy correction (#25), report
merge and CI deployment change.
Keep video/script sources, fingerprints, authors, excerpt widths and theme
initialization/persistence unchanged. Add no dependency or client framework.

## Rationale

The reproduced causes were the overlay-only layout, explicit link-click
dismissal, and footer placement. A persistent panel needs explicit open,
close, Escape and focus handling once native popover dismissal is removed.
Desktop body padding reserves the same width as the panel; print clears it.
A narrow drawer keeps the full article width and dismisses on outside clicks.
Open state lasts for the current page without another storage preference.
Copied heading labels retain compiled math but shed descendant IDs.

The pinned upstream TableOfContents uses ordinary links without close-on-link;
Nav contains its masthead DarkMode switch. Independent measurements of the
[live lesson](https://www.3blue1brown.com/lessons/fourier-transforms/) show
the reference can itself overlap text at 1280 pixels, so reserving desktop
space follows this user's explicit non-overlap requirement. Its current live
Chromium contents remained transparent after scrolling; source inspection,
rather than successful live pointer navigation, establishes reference link
persistence. Update provenance and live authoring guidance accordingly.

## Evidence and outcome

- Before implementation, a Chromium/Firefox browser regression reproduces
  article overlap (panel right 336 pixels, article left 115), middle-to-bottom
  navigation closing the panel, and the misplaced switch. The permanent
  masthead-switch regression also fails against pristine `d1542ba`.
- The original browser regression passes after the fix. Broader primary QA
  passes 384 assertions across seven desktop, tablet, phone and short-window
  sizes in both browsers, including keyboard focus, Escape, forward/backward
  heading links, outside dismissal, print, storage denial and JavaScript-off.
  All 48 active pages and 161 contents links per browser have valid targets,
  nonempty labels, unique IDs and no JavaScript errors. Ten additional
  assertions verify a compiled mathematical heading and an existing label ID.
- Narrow-screen pointer checks caught corner-control labels intercepting the
  drawer's links. Placing the drawer above those controls fixes the failure;
  the same pointer checks now pass. Desktop/mobile screenshots were inspected.
- Independent Chromium 151/Firefox 153 review passes another 275 assertions,
  including resizing, theme persistence and an actual Chromium PDF. The PDF
  and masthead screenshots were visually checked; print clears the reserved
  width and restores the chosen appearance afterward.
- Combined checks after integration pass: 185 website tests, 10,009 assertions,
  48 built pages, `uv run --locked prek -a --quiet`, and `git diff --check`.
  The complete minified page controller is 2.69 KB. Safari and physical phones
  were not tested. Browser regressions use temporary Playwright harnesses;
  the committed masthead regression runs with the existing Bun suite.

## Report relevance

Records a user-directed navigation correction, its failed-first reproductions,
responsive and independent browser checks, and integration with parallel work.
The mathematical exposition and published media are unchanged.

Final integration validation recorded at 2026-11-15T11:11:45-08:00: after rebasing onto `41b0b69`, all 185 website tests (10,009 assertions), the 48-page build, repository lint and whitespace checks pass again. The branch retains #23 and #25; only this controls change and its record are committed next.
