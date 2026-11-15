# Publish the Node 2 script pull request

- Recorded at: 2026-11-14T21:32:44-08:00
- Observed work interval: 2026-11-14T21:28:10-08:00/2026-11-14T21:32:44-08:00 (274 seconds through this publication record).
- Participants: Steven Creech (authorized sync, push, and PR); OpenAI Codex, GPT-6 (publication and verification).

## Context and decision

Complete the [Node 2 preparation](2026-11-14-213126-prepare-node-two-script-pull-request.md).
Commit the reviewed script, scoped index, and decision history as
`6e1a80bfb51ad5301ff62dd6dda2e40c5035b57b`, with the required
`Assisted-by: Codex:GPT-6` trailer. Push `steven/node-2-script` and open
[PR #5](https://github.com/TomasOrtega/circulant-Hadamard/pull/5) against `main`.
The branch begins at current main `73765b29757f66ed5ab6f08c079e281c9d829fed`.

## Rationale

The PR is ready for review and includes only the approved Node 2 production
script, its script-index entry, and required records. The main checkout
retains the other local scripts and proof-map work without changes; the
PR was prepared in a separate worktree to avoid overlapping upstream edits.
No merge into main or hosted deployment is authorized or performed here.

## Evidence and outcome

- GitHub confirms PR #5 is open, non-draft, targets main, and is mergeable
  without conflicts. Its initial eight-file diff matches the intended scope.
- At 2026-11-14T21:32:20-08:00, GitHub's lint and website checks passed
  for the implementation commit; the two TeX jobs were still in progress.
  These are observed statuses, not a claim that all CI has finished.
- The exact PR branch passed 46 local website tests, built 17 pages, and
  passed full lint; the approved script and its math rendering were checked
  separately. All 226 previously existing source files in the original
  checkout were unchanged by PR preparation.
- Add this publication record in a follow-up documentation commit on the
  same branch. That commit changes no script or implementation; final
  remote status is checked again after pushing it.

## Report relevance

Records the successful user-authorized publication, exact implementation
commit, focused PR scope, current-main basis, and the observed validation
status without implying that the larger local proof website was published.
