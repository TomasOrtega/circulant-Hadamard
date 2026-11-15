# Move component tests into dedicated subfolders

- Recorded at: 2026-11-15T09:53:14-08:00
- Observed relocation and validation interval: 2026-11-15T09:52:13-08:00/2026-11-15T09:53:14-08:00 (61 seconds); preceding inventory start unknown.
- Participants: Tomas Ortega (issue and minimal-change request); OpenAI
  Codex, GPT-6 (relocation and checks).

## Context and decision

[Issue #16](https://github.com/TomasOrtega/circulant-Hadamard/issues/16)
requests test subfolders. Move all 35 test files from the website, narration,
video, and TeX component roots into their respective `tests/` directories.
Adjust relative imports, fixture/repository paths, and Python discovery in CI
and the video Makefile. Keep existing assertions and the existing runners.

This includes the publication tests introduced in the
[PDF publication decision](2026-11-15-084535-publish-linked-pdfs-with-ci-freshness-checks.md).

## Rationale

Component-local test folders separate tests from production files without a
new framework or shared test layer. Empty Python package markers and explicit
discovery roots keep module names unambiguous. Bun already finds nested tests.
Add the folder convention to the root agent guidance to prevent recurrence.

## Evidence and outcome

- Comparing the previous Git tree with the new directories confirms that all
  35 test filenames moved and none remain in the four component roots.
- All 188 website, 20 narration, 41 video, and 7 PDF-publication tests pass.
  The Python narration/video counts match the discovery counts captured
  before relocation. The existing website build and PDF freshness check pass.
- Initial lint reformatted the moved narration fixture path; the subsequent
  repository lint and staged whitespace checks pass.
- Production behavior, mathematical content, and published assets are unchanged.

## Report relevance

Records a test-layout refactor and successful rediscovery of existing checks.
It adds no mathematical result or new verification claim.
