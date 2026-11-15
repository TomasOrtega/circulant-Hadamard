# Prepare the combined main-node scripts and proof-map pull request

- Recorded at: 2026-11-15T02:30:10-08:00.
- Observed work interval: 2026-11-15T02:26:28-08:00–2026-11-15T02:30:10-08:00
  (222 seconds through scope review and the successful fetch).
- Participants: Steven Creech (request and disk-space recovery); Codex/GPT-6
  (integration and review); Codex/GPT-6 subagents (scope and validation audit).

## Context and decision

Steven requested a PR with everything accumulated now that the main-node
scripts have been revised. This broadens the earlier Node 1–4 scoped PRs:
include all pending project sources and decision records, including his local
Node 1 script edits, Node 2's refinement, Nodes 5–8, the shared proof-map
layout, and the interactive phase diagrams. Preserve the supplied source
notes and native SVG storyboards with their generators.

Create `steven/main-node-scripts-and-proof-map` from the existing working
checkout. First commit the accumulated work with its history records, then
merge current main, validate the integrated result, and publish a PR against
main. Keeping the initial local state in a commit protects the user edits
during integration. No merge into main is requested.

## Rationale

The [latest script revision](2026-11-15-022452-refine-scripts-for-nodes-six-through-eight.md)
completes the requested narrative sequence. The main-page example now leads
into the general argument through the deeper nodes; Nodes 6–8 distinguish
shared rotation, the example contradiction, and the general final sum.

GitHub confirms main is `e8c8449c2b69b6dcad5cd9209c66d7f86c13a2b9` and
there are no open PRs. The earlier Node 4 PR has merged. Main also adds
Tomas's Node 4 recording and captions, duration 238.8 seconds, and five
child clip ranges. These must survive integration with the local exposition.

## Evidence and observed limits

- Scope review found 99 pending files, all project sources or decision
  records; no dependency caches, generated website builds, or credential
  files appeared in the candidate list. Existing recordings remain tracked
  source assets and will be compared with main after integration.
- Git initially could not write `FETCH_HEAD` because the disk was full.
  A bounded audit found no substantial disposable assistant artifacts.
  Steven freed space; at 02:30:10 the volume reported 9.3 GiB available and
  `git fetch origin` succeeded.
- The disk audit ran 02:27:13–02:28:05 (52 seconds, same date and offset).
  Full test files copy complete video assets into temporary build trees.
  Separate test processes were considered to reduce peak disk use, but
  the freed space now permits the ordinary full test command.
- GitHub CLI and connector tools are unavailable here. Use Git for branch
  operations and GitHub's authenticated API for PR publication, keeping
  credentials in memory. Python's default certificate lookup failed; the
  system CA file verified the connection successfully.
- The review noted that Node 1's general dictionary already introduces a
  circulant sign matrix. Preserve Steven's shortened wording in that context;
  remove incidental trailing whitespace through the required lint hooks.
- Integration, full validation, commit hashes, and publication outcomes will
  be recorded in a subsequent entry; this preparation makes no success claim
  for those steps yet.

## Report relevance

Records the user's expansion from individual node PRs to the complete pending
website work, the preservation of collaborator video production, and the
environmental issue resolved before publication.
