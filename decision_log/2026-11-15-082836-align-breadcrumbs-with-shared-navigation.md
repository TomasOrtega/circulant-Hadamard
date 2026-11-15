# Align breadcrumbs with shared navigation

- Recorded at: 2026-11-15T08:28:36-08:00
- Observed implementation and validation interval:
  2026-11-15T08:24:35-08:00/2026-11-15T08:28:36-08:00 (241 seconds).
- Participants: Tomas Ortega (styling request); OpenAI Codex, GPT-6
  (implementation and checks).

## Context and decision

The user reported inconsistent styling and font size in the upper-left
breadcrumb path. Update [Breadcrumbs](../website/node.jsx) to use the same
neutral NodeButton component as the surrounding navigation and its `text-lg`
sans-serif typography. Give the current-page label matching padding and use
the existing dark-gray color for the decorative slash separators.

This follows the [parent-navigation simplification](2026-11-15-082135-remove-redundant-parent-navigation-text.md)
and the [shared-theme styling decision](2026-11-14-211554-align-proof-map-with-upstream-style.md).
Continue the user's instruction to commit and push completed website changes.

## Rationale

The breadcrumbs used `text-sm` and ordinary underlined links, while nearby
navigation used larger, padded neutral links. Reusing the existing component
keeps font, spacing, default appearance, hover, and keyboard-focus feedback
consistent. The current-page label remains noninteractive with
`aria-current="page"`; ancestor links retain their original destinations.

## Evidence and outcome

- Added a rendered-page regression first. It failed on the Group-Ring
  Encoding page's smaller breadcrumb typography before the fix. The same
  check now passes on every non-root page, comparing breadcrumb link styling
  with parent navigation and checking the larger sans-serif typography.
- All 185 website tests pass: 9,489 assertions across 18 files.
  `make -C website` rebuilds all 50 active pages and compiled styles.
- Native Firefox accessibility inspection confirms the Proof map and
  Group-Ring Encoding ancestor links in the rebuilt hierarchy. Screenshot
  inspection timed out twice, including after reconnecting; no successful
  screenshot or narrow-viewport visual validation is claimed.
- Whitespace checks pass. Repository lint follows before commit. No vendored
  CSS, mathematical content, video, or navigation destinations were changed.

## Report relevance

Records a user-directed consistency improvement to the shared website
navigation. It adds no mathematical result or proof verification.

Final repository validation recorded at 2026-11-15T08:28:47-08:00: `uv run --locked prek -a --quiet` and staged whitespace checks passed.
