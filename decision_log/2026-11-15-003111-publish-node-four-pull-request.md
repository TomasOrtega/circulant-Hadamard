# Publish the Node 4 pull request

- Recorded at: 2026-11-15T00:31:11-08:00
- Observed work interval: 2026-11-15T00:20:29-08:00/2026-11-15T00:31:11-08:00
  (642 seconds through this publication record).
- Participants: Steven Creech (authorized PR); OpenAI Codex, GPT-6
  (commit, push, publication, and verification).

## Context and decision

Complete the [reviewed preparation](2026-11-15-002921-prepare-node-four-pull-request.md).
Commit the implementation as `c9a6ad83b9e4f170536295b5b66de7399c3c3b28`
with the required `Assisted-by: Codex:GPT-6` trailer. Push
`steven/node-4-delta-theorem` and open
[PR #9](https://github.com/TomasOrtega/circulant-Hadamard/pull/9) against main.
The branch is based on current main
`0a44d6141ec21710888844375b1e8a7de19833ba`.

## Rationale

The PR publishes Node 4's script, phase-circle storyboard, six-step refinement,
and revised proof-map exposition with the required supporting integration and
history. Keep other node drafts and shared navigation/layout changes local.
The isolated branch preserves current main's video and navigation behavior.
No merge into main or hosted deployment is performed.

## Evidence and outcome

- GitHub confirms PR #9 is open, non-draft, targets main, and has no merge
  conflicts. The implementation changes 21 files including decision records.
- The exact PR branch passes 96 tests (6,260 assertions), builds 28 pages plus
  redirects, and passes full lint. Desktop/mobile inspection and media/source
  preservation results are recorded in the preparation entry.
- All 340 pre-existing source files in the original working checkout still
  match the initial manifest. The isolated checkout was clean after the
  implementation commit; the dependency symlink was removed before staging.
- The temporary PR preview server and headless browser were stopped; the
  existing port-8000 workspace preview remains available. Temporary screenshots
  and audit artifacts remain outside the repository.
- Add this publication record in a documentation-only follow-up commit and
  verify the final remote head. CI may restart for that commit; no completed-CI
  claim is made here.

## Report relevance

Records user-authorized publication of the reviewed Node 4 material, its
main-based source commit, and verified preservation of concurrent local work.
