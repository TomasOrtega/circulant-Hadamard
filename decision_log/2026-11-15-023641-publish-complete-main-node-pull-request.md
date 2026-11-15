# Publish the complete main-node pull request

- Recorded at: 2026-11-15T02:36:41-08:00.
- Observed work interval: 2026-11-15T02:26:28-08:00–2026-11-15T02:36:41-08:00
  (613 seconds through PR creation and browser verification).
- Participants: Steven Creech (authorized publication); Codex/GPT-6
  (commit, push, API publication, and verification); Codex/GPT-6 subagent
  (browser review, 02:33:01–02:36:12 on the same date/offset, 191 seconds).
  The browser interval overlaps the primary interval.

## Context and decision

Complete the [combined PR preparation](2026-11-15-023010-prepare-combined-main-node-pull-request.md)
and [validated integration](2026-11-15-023359-integrate-main-with-complete-proof-map-work.md).
Push `steven/main-node-scripts-and-proof-map` and open
[PR #10](https://github.com/TomasOrtega/circulant-Hadamard/pull/10) against main.
The PR is open and non-draft. It includes the remaining main-node scripts,
refined graphs and exposition, shared layout, interactive diagrams, local
Node 1 edits, and decision records.

The local snapshot commit is `4a7ab30`. Integration commit
`b1e3c23d55325cc825f63275938faabd2e460858` includes main at
`e8c8449c2b69b6dcad5cd9209c66d7f86c13a2b9`. Both commits carry the required
`Assisted-by: Codex:GPT-6` trailer. GitHub confirmed no merge conflicts
and an initial PR scope of 86 changed files before this publication record.

## Evidence and outcome

- The integrated branch passes **145 website tests, 8,359 assertions**,
  builds **48 pages**, and passes full repository lint. Source-preservation
  checks are detailed in the integration record.
- Browser smoke checks passed at **1440 px** and **390 px** for the main
  Node 4 section, its own page, and Nodes 6/7's interactive diagrams.
  No page overflow, MathJax errors, or JavaScript exceptions were observed.
- The Node 4 video decodes as **238.8 seconds, 1920×1080**; captions return
  HTTP 200 and valid WEBVTT. All five clip ranges match main. Rotation controls
  respond, and normalized point pairs agree within floating-point tolerance.
- The first normalization QA compared SVG transform strings exactly; small
  floating-point differences triggered that check. A coordinate tolerance of
  $10^{-7}$ pixels passed, with maximum observed difference
  $1.42\times10^{-14}$ pixels. No product change was needed.
- Desktop main-page, mobile Node 4, and mobile normalization screenshots were
  inspected. Evidence: `/private/tmp/circulant-integrated-browser-qa.json`
  and `/private/tmp/circulant-integrated-*.png`.
- The dedicated browser and temporary profile were closed. The existing
  localhost:8000 preview remains running with the integrated build.
- At the first CI inspection, lint had passed for both triggers and one
  website job had passed; the other website job and TeX jobs were still
  running. This is not a claim that all CI completed or that later reruns
  have passed.
- Add this record in a documentation-only follow-up commit, push it, and
  verify that the PR head matches the local branch. No merge into main or
  hosted deployment is included in the user's request.

## Report relevance

Records the actual user-authorized publication and independent preview checks
for the accumulated main-node work, including preservation of the collaborator's
recordings. The prior disk-space restriction was resolved by the user before
the successful full validation and Git publication.
