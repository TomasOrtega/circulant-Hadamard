# Prepare the Node 4 pull request

- Recorded at: 2026-11-15T00:29:21-08:00
- Observed work interval: 2026-11-15T00:20:29-08:00/2026-11-15T00:29:21-08:00
  (532 seconds through this record).
- Participants: Steven Creech (authorized the Node 4 PR); OpenAI Codex,
  GPT-6 (scope isolation, integration, delegated audits, validation).
- Delegated initial scope review: 2026-11-15T00:21:24-08:00/2026-11-15T00:22:21-08:00
  (57 seconds). Documentation: 2026-11-15T00:25:58-08:00/2026-11-15T00:26:25-08:00
  (27 seconds). Final scope audit: 2026-11-15T00:26:06-08:00/2026-11-15T00:26:53-08:00
  (47 seconds). These intervals overlap the primary interval.

## Context and decision

Steven requested a pull request for the work on Node 4. Following the
[isolated Node 3 workflow](2026-11-14-224622-prepare-node-three-and-main-proof-map-pr.md),
fetch main and create `steven/node-4-delta-theorem` in
`/private/tmp/circulant-node4-delta-pr`, based on
`0a44d6141ec21710888844375b1e8a7de19833ba`. A second fetch before publication
confirmed the same main head. Preserve the original working checkout.

Include the reviewed Node 4 parent exposition, six-node refinement, four-section
production script, phase-circle storyboard, associated tests, and four Node 4
history records. Include only their supporting index, test-expectation, and
cross-reference changes. Other node drafts and shared navigation/layout fixes
remain local. The branch retains main's reading guides, renderer, and videos.

## Rationale

Main's explicit Node 4 overview excerpt overrides the updated body. Remove
only that override so the approved definition-first exposition appears on the
homepage, preserving the 131.85–145.45 video cut and the notation-context edge.
Update the refinement count and whole-node black-box expectation. Escape the
expected title in the title-only test for the apostrophe in Kronecker's title.
The technical character-comparison lemma and Kronecker remain stated inputs;
this PR does not claim a new proof or formal verification.

Keep historical records' prior outcomes. In the scoped copy of the original
Node 4 record, change its link to the unpublished Node 5 record into an unlinked
historical filename. The current PR scope is defined here, not by earlier
full-workspace test counts.

## Evidence and outcome

- The exact branch passes 96 tests with 6,260 assertions and builds 28 node
  pages including main's reading guides, plus compatibility redirects.
- Full lint passes without notices after restoring the sparse checkout's
  tracked text sources. Initial lint exited successfully but reported absent
  video-source paths. Scoped whitespace checks pass.
- Independent audit confirms all 10 approved Node 4 source files match the
  working copies exactly; 59 parsed relative source/history links resolve.
  All 18 media assets match main's Git blobs, and all 9 published video
  records and 18 cut timings are unchanged. Seventeen other existing node
  files are unchanged; the theorem has only a relevant cross-reference edit.
- Desktop and mobile browser checks of the exact PR build show the new math
  without rendering errors or page overflow; screenshots were inspected.
  Temporary evidence is under `/private/tmp/circulant-node4-pr-*`.
- All 340 pre-existing source files in the original checkout match the initial
  SHA256 manifest. The local preview remains on port 8000; the PR build uses
  a separate temporary port.
- Sparse checkout initialization initially left an empty index; initializing
  the index and restoring main populated it. A low-disk-space write left one
  temporary media copy empty. The original media was verified intact. Reuse
  existing media through hard links, remove only inactive assistant browser
  profiles and a prior generated PR build, and verify all media against main.
  Recovery snapshots and user files remain untouched.
- Commit, push, and PR creation follow this preparation; their observed
  outcomes will be recorded separately. No merge or hosted deployment is
  included.

## Report relevance

Records publication preparation for user-led mathematical exposition, with
AI-assisted scope isolation, source preservation, rendering checks, and
explicit separation of accepted arithmetic inputs from new exposition.
