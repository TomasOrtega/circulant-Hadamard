# Restrict reading routes and simplify page headings

- Recorded at: 2026-11-14T21:47:05-08:00
- Observed work interval: 2026-11-14T21:44:22-08:00/2026-11-14T21:47:05-08:00
  (163 seconds through this record).
- Participants: user (fix request and commit/push authorization); OpenAI Codex,
  GPT-6 (implementation and validation).

## Context and decision

The user asked to fix the open GitHub issue. The only open issue was
[#6](https://github.com/TomasOrtega/circulant-Hadamard/issues/6), with no comments:
show the two reading-route buttons only on the proof map page, and show only
node titles in page headings. The user subsequently requested commit and push.

Restrict [ReadingRoutes](../website/node.jsx) to the root view, keeping its
example-first emphasis and link anchors. Remove node numbers, black-box labels,
and foundation labels from page heading groups. Update the website authoring
guidance to match the user's request, which supersedes its earlier heading rule.
Keep the metadata and contextual information in child sections and maps.

This revises the earlier decisions to
[retain heading labels](2026-11-14-212404-simplify-node-headings.md) and
[display unselected reading routes on shared nodes](2026-11-14-212404-reading-routes-on-shared-nodes.md).
Prepare the fix on a dedicated branch and submit an issue-linked pull request.

## Rationale

The shared static renderer emitted both controls and heading metadata on every
page. Hiding the controls through CSS would retain redundant navigation in the
markup. Restrict rendering instead, and remove obsolete current-route logic
because route pages no longer display these buttons.

The generated HTML reproduces both symptoms directly. The small deterministic
rendering tests supply the feedback loop, so broader hypothesis generation and
debug instrumentation were unnecessary. Use the diagnosing-bugs skill, the
writing-for-agents skill for the authoring-rule change, and the PR skill for the
short issue-linked description, following the user's format requirements.

## Evidence and outcome

- Added regression coverage before the implementation. The focused Bun command
  with the pattern `page headings contain only|reading routes appear only`
  failed on Group-Ring Encoding: its heading included `Node 1`, and its page
  contained the reading-route navigation. Both tests pass with the fix.
- An initial draft assertion matched a hover-class substring; corrected the
  test to check the reported visibility before implementing the fix.
- `make -C website check` passed all 46 tests and 5,113 assertions;
  `make -C website` emitted all 17 pages. Internal links, return anchors,
  breadcrumbs, and dependency navigation remain covered by the suite.
- `uv run --locked prek -a --quiet` and `git diff --check` passed.
- Served the production output locally and checked all 17 pages over HTTP:
  each returned 200 and matched the current build, all heading groups contained
  only their titles, and only the root contained the two route buttons.
- Browser visual inspection could not run because the computer-use browser
  access host was unavailable. No visual verification is claimed.
- Commit, push, and pull-request publication outcomes will be recorded separately.

## Report relevance

This is an AI-assisted repair to the website's navigation and headings,
requested through GitHub. It changes presentation and authoring guidance;
no mathematical statement, proof, or production narration changed.
