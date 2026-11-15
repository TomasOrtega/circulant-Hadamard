# Prepare the Node 2 script pull request

- Recorded at: 2026-11-14T21:31:26-08:00
- Observed work interval: 2026-11-14T21:28:10-08:00/2026-11-14T21:31:26-08:00 (196 seconds through this record).
- Participants: Steven Creech (sync and script-only PR request); OpenAI Codex, GPT-6 (scoped preparation, delegated review, and validation).
- Delegated read-only review: 2026-11-14T21:29:34-08:00/2026-11-14T21:30:34-08:00 (60 seconds; overlapping).

## Context and decision

Steven approved the Node 2 overview and requested synchronization with main
and a pull request for this script. Fetch origin/main, now at
`73765b29757f66ed5ab6f08c079e281c9d829fed`, and create
`steven/node-2-script` from it in an isolated worktree at
`/private/tmp/circulant-node2-script-pr`. The earlier Node 1 PR is merged.
The original working checkout stays on its current branch with its local
proof-map and script drafts intact; this new PR branch incorporates current
main, including the colleague's newer navigation and styling changes.

Publish the exact approved [Node 2 script](../website/scripts/node2/restriction-on-the-order.md),
a scoped [script index](../website/scripts/README.md), the five recent Node 2
editing/review/recovery records, and this publication preparation record.
The script is introduced to main here; the earlier PR deliberately left it
local. This follows the [approved refinements](2026-11-14-212726-apply-node-two-narration-refinements.md).
The user's other scripts, new graph nodes, renderer edits, and website
exposition changes are outside this PR.

## Rationale

The original checkout has substantial unrelated, uncommitted work, while
main has overlapping website changes. A clean branch based on current main
allows a focused PR without stashing, overwriting, or merging those local
drafts. The script includes six slides and animation directions, proves
square and parity, defers oddness to deeper material, and sets up a
contradiction for odd u>1 with u=3 as the guiding example.

Retain the historical records' wording and times. In the PR copies of the
revision record, turn two links to still-local graph/notation records into
plain source filenames, so the scoped branch has no dangling links. Those
historical records describe a larger local website; their 65-test result
is distinct from the 46-test current-main snapshot checked here.
The main script index gains only the Node 2 description, folder, and link.

## Evidence and outcome

- Independent review found no blocking scope, mathematics, narration, or
  animation-cue issues. All 32 local Markdown links across the initial
  seven-file PR scope resolve.
- The exact main-based branch passes all 46 website tests (5,129 assertions)
  and builds 17 pages. Full repository lint passes. The source and lockfile
  match the existing website dependencies, which were temporarily reused
  for validation; the untracked dependency symlink is removed before commit.
- Direct rendering confirms all six slides, their cues, and every equation
  compile with main's MathJax renderer. The script byte-matches the approved
  working copy. No new mathematical result or video recording is claimed.
- A hash comparison of all 226 pre-existing tracked/untracked source files
  confirms the original working checkout was untouched during preparation.
- GitHub CLI and a connected GitHub tool are unavailable. Use the GitHub
  API with the existing credential helper, keeping credentials in memory
  and TLS verification enabled through the system certificate bundle.
  The API confirms no existing open PR for this branch.
- Commit, push, and PR creation follow this record; they have not yet
  occurred. A subsequent record will capture their observed results.

## Report relevance

Records user-authorized publication of a reviewed production script, its
separation from ongoing local research exposition, and validation against
the collaborator's current main branch without disturbing either body of work.
