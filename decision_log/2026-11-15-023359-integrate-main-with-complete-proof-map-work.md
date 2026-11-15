# Integrate main with the complete proof-map work

- Recorded at: 2026-11-15T02:33:59-08:00.
- Observed work interval: 2026-11-15T02:30:10-08:00–2026-11-15T02:33:59-08:00
  (229 seconds through integration, tests, build, lint, and preservation audit).
- Participants: Steven Creech (authorization); Codex/GPT-6 (integration and
  checks); Codex/GPT-6 subagents (documentation and preservation review).
- Overlapping review intervals on 2026-11-15, offset -08:00: initial scope
  02:27:03–02:30:24 (201 seconds); documentation 02:31:49–02:32:32
  (43 seconds); final preservation 02:32:28–02:33:02 (34 seconds).
  These are not additive person-hours.

## Context and decision

Implement the [combined-PR preparation](2026-11-15-023010-prepare-combined-main-node-pull-request.md).
Commit the accumulated local state as
`4a7ab30` on `steven/main-node-scripts-and-proof-map`, including all pending
website sources and decision records. Lint removed only incidental trailing
whitespace from Steven's Node 1 script before this snapshot.

Merge main at `e8c8449c2b69b6dcad5cd9209c66d7f86c13a2b9`.
Six files required conflict resolution:

- Keep main's Node 4 recording, captions, duration, and five clip ranges.
  The local Node 4 mathematical exposition is otherwise unchanged.
- Keep all local refinement counts in `proof-map.test.jsx` and Node 8.5's
  theorem cross-reference to the expanded Node 2 and Node 4 proof outlines.
- Keep the shared full-width, single-journey documentation and all Nodes 5–8
  descriptions. Incorporate main's Node 4 details and newly published video.
  Update stale scene counts in the website guide to the saved scripts.
- Restore the original Node 4 decision record's link to Node 5 history, which
  is now included. The scoped Node 4 PR had rendered it as an unpublished
  filename; no historical substantive claim is changed.

## Rationale

The combined PR should publish the developed website as one coherent state
while preserving the collaborator's video production. Keeping a local
snapshot commit before integration makes the source-preservation comparison
explicit. A separate PR against main supports review without merging the work.

## Evidence and outcome

- `make -C website check`: **145 tests pass, 8,359 assertions**, across
  17 files. The normal full command now succeeds after disk space was freed.
- `make -C website`: **48 node pages** built successfully, with compatibility
  redirects. Existing video assets are copied into the preview output.
- `uv run --locked prek -a --quiet` and staged whitespace checks pass.
- Independent audit: all **66** upstream media/video-production files match
  main's Git blobs; all **10** video records and **23** clip ranges match main.
- All **26** production scripts, supplied references, and storyboards match
  snapshot `4a7ab30`. All **52** node/phase files match it except Node 4's
  expected recording metadata and clip additions. Script-index and website
  guide changes are the documented merge resolutions.
- Initial scope review resolved all **176** relative links across **73**
  pending Markdown files and found every referenced child node. Candidate
  files contain no build output, dependency caches, or credential-pattern flags.
- Full-test evidence: `/private/tmp/circulant-all-main-nodes-pr-check.log`.
  Browser review and actual publication outcomes follow in the publication
  record. No new mathematical proof or formal verification is claimed.

## Report relevance

Records the integration choices, user-edit preservation, full validation, and
successful inclusion of collaborator recordings in the complete proof-map
and script sequence.
