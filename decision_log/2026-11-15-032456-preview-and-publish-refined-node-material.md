# Preview and publish the refined-node material

- Recorded at: 2026-11-15T03:24:56-08:00.
- Observed work interval: 2026-11-15T03:21:33-08:00–2026-11-15T03:24:56-08:00
  (203 seconds through browser review, readability fixes, and final validation).
- Participants: Steven Creech (authorization); Codex/GPT-6 (final adjustments
  and publication); Codex/GPT-6 subagent (browser review, 03:19:52–03:22:37,
  165 seconds, and targeted recheck 03:23:30–03:24:16, 46 seconds, all on
  2026-11-15 at offset -08:00). These intervals overlap other work.

## Context and decision

Complete the [validated refined-node package](2026-11-15-032133-validate-refined-node-pr-against-main.md)
and publish it as a separate PR against main. The content commit is
`41808a9`; integration commit `5ee6e20de33d19e257f3f4e202cd75b2894f78b0`
includes main at `ae1e554`. The preceding PR #10 has merged.

The browser sweep checked all **34 refined pages and seven parents** at
1440 px and 390 px, for **82 page checks**. There were no page overflows,
MathJax errors, JavaScript exceptions, or missing/styling-free leaf statement
boxes. Node 4's six parent excerpts also contain their result boxes.

## Readability adjustment and evidence

The sweep found lengthy explanatory prose inside two valuation displays,
in Nodes 2.4 and 4.3. Scrolling was contained, but the long lines made the
argument harder to read. Move the coefficient-divisibility explanation into
ordinary prose and retain only the necessary valuation formula as a display.
No hypothesis or mathematical conclusion changes.

- Targeted recheck: both pages at both widths fit their columns without
  horizontal scrolling in the revised criteria (735 px desktop, 323 px
  mobile). Both mobile proof screenshots were inspected.
- Final suite after these edits: **182 tests pass, 8,936 assertions**.
  Build emits **50 pages**. Full lint and focused final-file checks pass.
- Browser evidence: `/private/tmp/circulant-refined-browser-qa.json`,
  `/private/tmp/circulant-refined-readability-qa.json`, and screenshots matching
  `/private/tmp/circulant-refined-*.png`.
- Final test/build logs: `/private/tmp/circulant-refined-nodes-final-check.log`
  and `/private/tmp/circulant-refined-nodes-final-build.log`.
- Both dedicated browsers and their temporary profiles were closed. The
  existing localhost:8000 preview server remains running with the final build.
- Commit the two presentation adjustments with this record, then push and
  open the PR. The actual publication result will be appended with its
  observed timestamp. No merge into main or rendered-video production is
  requested in this task.

## Publication outcome

- Follow-up recorded at: 2026-11-15T03:26:35-08:00. Total observed task interval from
  2026-11-15T02:45:23-08:00 through this follow-up: 2472 seconds.
- Pushed `steven/refined-node-scripts-and-exposition` and opened
  [PR #11](https://github.com/TomasOrtega/circulant-Hadamard/pull/11),
  non-draft, against main. GitHub confirms no merge conflicts.
- Verified initial PR head `c97ff7fc4cc15ec4364ed898eec1a7d2164699ec`
  and base `ae1e55484c0f21d582b28756e2271fee749f096f`. The PR changes
  86 files and contains this refined-node stage rather than the prior PR's
  already-merged work. Commit trailers identify Codex/GPT-6 assistance.
- Add this observed outcome in a documentation-only follow-up commit and
  verify the final pushed head. Automated CI may still be running; the local
  test, build, lint, mathematical-review, and browser results above are complete.

## Report relevance

Records comprehensive visual checking of the second-level proof content,
the resulting mobile readability improvement, and the distinction between
completed production scripts and videos that remain to be generated.
