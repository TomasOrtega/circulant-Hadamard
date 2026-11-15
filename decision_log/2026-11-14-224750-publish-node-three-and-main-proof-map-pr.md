# Publish the Node 3 and main proof-map pull request

- Recorded at: 2026-11-14T22:47:50-08:00
- Observed work interval: 2026-11-14T22:37:35-08:00/2026-11-14T22:47:50-08:00 (615 seconds through this publication record).
- Participants: Steven Creech (authorized sync, push, and PR); OpenAI Codex, GPT-6 (publication and verification).

## Context and decision

Complete the [reviewed preparation](2026-11-14-224622-prepare-node-three-and-main-proof-map-pr.md).
Commit the Node 3 and main proof-map scope as
`7fa705c3c4eef180ee5b015e6682e6475c1dabbf`, with the required
`Assisted-by: Codex:GPT-6` trailer. Push `steven/node-3-and-proof-map`
and open [PR #8](https://github.com/TomasOrtega/circulant-Hadamard/pull/8)
against main. The branch is based on current main
`3f3c26ca74fcfc3bbb4b2e822e80b31e5cc12dd8`.

## Rationale

The PR contains the approved Node 3 script and refinement plus the shared
main-map integration, while preserving published media and URL compatibility.
The isolated checkout keeps the other in-progress drafts local. No merge
into main or hosted deployment is performed.

## Evidence and outcome

GitHub confirms PR #8 is open, non-draft, targets main, and has no merge
conflicts. The implementation changes 48 files including required history.
The branch passed 81 local tests (5,531 assertions), a 20-page build plus
redirects, and full lint. Desktop/narrow browser checks and upstream media
preservation checks are recorded in the preparation entry.

All 236 pre-existing source files in the original checkout retain their
initial hashes. The PR checkout was clean after the implementation commit.
The temporary QA server was stopped; the original local preview remains.
Add this publication record in a documentation-only follow-up commit on the
same branch, then verify its remote head. GitHub checks may restart for that
new commit; no completed-CI claim is made for the final head here.

## Report relevance

Records the successful user-authorized publication, exact main-based commit,
reviewable scope, and verified preservation of concurrent local work.
