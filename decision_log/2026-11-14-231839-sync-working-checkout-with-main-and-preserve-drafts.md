# Sync the working checkout with main and preserve unpublished drafts

- Recorded at: 2026-11-14T23:18:39-08:00
- Observed work interval: 2026-11-14T23:08:37-08:00/2026-11-14T23:18:39-08:00 (602 seconds).
- Participants: Steven Creech (requested main sync); OpenAI Codex, GPT-6 (preservation, integration, delegated review, recovery, and validation).
- Delegated audit: 2026-11-14T23:10:06-08:00/2026-11-14T23:10:49-08:00 (43 seconds).
- Delegated docs/test integration: 2026-11-14T23:11:00-08:00/2026-11-14T23:12:40-08:00 (100 seconds).
- Delegated final media review: 2026-11-14T23:14:45-08:00/2026-11-14T23:15:14-08:00 (29 seconds). Intervals overlap.

## Context and decision

Steven requested another synchronization after the
[Node 3 PR](2026-11-14-224750-publish-node-three-and-main-proof-map-pr.md).
GitHub confirms that PR #8 merged. Update the actual working checkout from
`2bd1087949dfdbe93479046a0e7e8a8fe8686b06` to fetched main
`0a44d6141ec21710888844375b1e8a7de19833ba`, retaining its branch name
`steven/node-1-proof-graph` and restoring unpublished work as local changes.
Fast-forward the separate local main reference after checking ancestry.
No remote branch or PR is changed.

Prepare and verify the combined tree in `/private/tmp/circulant-main-sync-review`.
Keep main's shared renderer, current styling, redirect implementation, published
media, and matching node/cut metadata. Restore the local Node 2 and Nodes 4–8
refinements, their scripts/tests, and unpublished records. Preserve both edited
Node 1 production scripts byte for byte. Update documentation and graph tests
for the larger local hierarchy without replacing upstream functionality.

An additional fetch during verification brought in Node 3's video and the
restored reading-route entry buttons/pages. Integrate these new main changes
as well; preserve the eight-node hierarchy and the separate reading pages.
This follows the user's request to synchronize current main rather than
revert upstream navigation decisions.

## Preservation and recovery

Before changes, snapshot all 240 tracked/untracked file states to
`/private/tmp/circulant-before-main-sync-20261114-231011` and retain the original local work in Git stash
`c16acbbcf90a83026c47a2319ce75056424b4a56` (label
`codex-before-main-sync-2026-11-14-230837`). A separate temporary integration
stash is `9508084a9f4b058eed347eb495f7f092a307f42d`.

The first working-checkout fast-forward could not write the Node 3 MP4 while
the disk was nearly full, leaving HEAD/index unchanged and most main files
already written. Remove only assistant-created temporary browser profiles
and generated QA build directories. Verify every current source blob against
the old or target Git tree and detect no unexpected user edits. Exactly one
main file was incomplete: the zero-length Node 3 video. Restore its exact
bytes from the reviewed checkout, verify all target blobs, and complete the
branch/index update with a mixed reset that does not overwrite worktree files.
Then restore the 72 verified draft/history overlay files from the snapshot.
The original work remains recoverable from both the stash and file snapshot.

## Evidence and outcome

- The final combined tree passes 130 tests (7,917 assertions), and builds
  50 pages including the two current reading pages, plus compatibility redirects.
  The actual working checkout was rebuilt after its verified overlay transfer.
- Two integration-test assumptions were updated: terminal navigation now chooses
  an actual leaf, and heading comparisons account for escaped apostrophes.
  Existing dropdown, route, video, and graph-label tests remain intact.
- Independent checks confirm nine video records, eighteen clip timings, and all
  referenced MP4/VTT assets match latest main. Both user-edited Node 1 scripts
  match their pre-sync bytes. No unpublished script content was reformatted.
- Lint ran with mutating formatting hooks skipped to protect unfinished user
  edits. The known pre-existing trailing space in a Node 1 script is retained.
- The original port-8000 preview now serves the rebuilt synchronized website.
  Main and the working branch point to the same fetched commit; drafts remain
  uncommitted. No mathematical result, remote push, or new PR is claimed.

## Report relevance

Records safe integration of current collaborator videos and navigation with
ongoing local proof work, including observed disk-write recovery and explicit
preservation checks. AI assistance concerns integration and validation.
