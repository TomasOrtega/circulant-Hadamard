# Move scripts into numbered node folders

- Recorded at: 2026-11-14T17:36:21-08:00
- Observed work interval: 2026-11-14T17:33:49-08:00/2026-11-14T17:36:21-08:00 (152 seconds through this record).
- Participants: Steven Creech (requested structure); OpenAI Codex, GPT-6
  (file migration, reference updates, validation, and delegated documentation).
- Documentation interval: 2026-11-14T17:34:18-08:00/2026-11-14T17:34:54-08:00
  (36 seconds, overlapping the primary interval).

## Context and decision

Steven asked whether the scripts had been moved and specified a top-level
`overview.md` with `node1/` containing `group-ring-encoding.md` and its subnode
scripts. Explain that the prior discussion was only a proposal, then perform
the requested migration. This supersedes the directory naming and per-node
`overview.md` suggestion in the
[earlier recommendation](2026-11-14-172721-recommend-script-folders-by-node.md).

Keep Video 0 at [scripts/overview.md](../website/scripts/overview.md).
Move the six Node 1 scripts, retaining their descriptive filenames, into
[scripts/node1/](../website/scripts/node1/). Move its source PDF and source
README together into `node1/reference/`. Move the existing Node 2 draft into
`website/scripts/node2/restriction-on-the-order.md`.
Do not create empty folders for videos that do not yet have scripts.

## Rationale

The user's numbered parent folders correspond directly to the graph, while
filenames continue to identify each script. Keeping the main Node 1 narration
named `group-ring-encoding.md` follows the explicit request rather than the
previous proposal to rename it `overview.md`.

Update the top-level script index, website authoring guide, website instructions,
and script-reading test path. Retarget two Markdown links in earlier decision
records to the moved Node 1 source folder and Node 2 draft; preserve those
records' original descriptions and timestamps. Relative links inside the
source README still work because its scripts and reference directory moved
together. Narration wording and mathematical notation are unchanged.

## Evidence and outcome

- Moved nine files: seven narration drafts, the source README, and the source
  PDF. SHA-256 checks before and after each move matched for all nine files.
  The top-level overview hash also remained unchanged, and the old moved-file
  paths no longer exist.
- All 53 local Markdown links across twelve current script/authoring files
  resolve. Used the Markdown parser with math support after a simple text
  pattern mistook coefficient notation for a link.
- All 41 existing tests passed (5,023 assertions), including rendering the six
  Node 1 scripts from their new locations. `make -C website check all` completed
  successfully. The production script move does not alter website page URLs
  or reader-facing content, so another browser preview was unnecessary.
- Required repository lint, explicit lint for moved untracked files, and
  `git diff --check` passed. The script index now displays the actual directory
  tree and links to the new locations.
- Prior uncommitted work is preserved. No commit, push, or deployment was made.

## Report relevance

This implements the user's production-file organization preference as video
scripts expand alongside the proof graph. It changes storage and navigation,
not the mathematical exposition or narration content.
