# Retire duplicate proof guides and credit the authors

- Recorded at: 2026-11-15T10:25:16-08:00
- Observed work interval: 2026-11-15T10:21:26-08:00/2026-11-15T10:25:16-08:00 (230 seconds).
- Participants: Tomas Ortega (issue and sequential commit/push request);
  OpenAI Codex, GPT-6 (implementation and checks).

## Context and decision

[Issue #19](https://github.com/TomasOrtega/circulant-Hadamard/issues/19)
requests replacing the two reading-route buttons with the authors' names
and removing those separate guides, while retaining the current main proof.
Credit Steven Creech and Tomas Ortega below the homepage title. Delete the
two guide sources, their extra build path, the button component, and obsolete
guide tests. Keep the existing redirects so both former URLs open the main map.

This supersedes the earlier
[guide-preservation request](2026-11-15-025720-preserve-reading-guides-after-complete-proof-map-merge.md).
Historical decision records and archived outlines remain unchanged.

## Rationale

The user selected the existing hierarchy as the general odd-u proof. Preserve
all of its source content rather than maintaining a separate summary route.
Removing the supplementary build path lets the existing redirect logic handle
the old URLs. The redirect regression now exercises the real proof-map root;
the earlier synthetic tree did not trigger the guide-loading branch.

## Evidence and outcome

- Before implementation, regressions fail for missing introductory authors,
  two unwanted build entries, and the real guide URL lacking a redirect.
- All 181 remaining website tests pass (9,622 assertions across 17 files).
  Five guide-specific tests and two generated guide-page cases are retired;
  the mathematical and proof-navigation checks remain. The build emits 48
  active proof pages and the existing legacy redirects.
- Firefox 153 and Chromium at 320, 390, and 1280 pixels show the author credit
  between the title and overview, without route controls, and retain all
  eight main deeper links. Both retired URLs navigate to the main proof.
  A phone screenshot was inspected.
- Repository lint and whitespace checks pass. The diff confirms every file
  under website/nodes/ is unchanged. The change removes 195 net lines before
  this required decision record and adds no dependency or client script.

## Report relevance

Records a user-directed reduction in duplicate exposition and clearer author
credit. It changes navigation and presentation, not the proof's mathematics.
