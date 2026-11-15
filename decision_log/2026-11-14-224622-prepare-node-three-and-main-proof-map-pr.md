# Prepare Node 3 and the main proof-map pull request

- Recorded at: 2026-11-14T22:46:22-08:00
- Observed work interval: 2026-11-14T22:37:35-08:00/2026-11-14T22:46:22-08:00 (527 seconds).
- Participants: Steven Creech (authorized main sync and PR); OpenAI Codex, GPT-6 (integration, delegated scope/UI/redirect review, and validation).
- Delegated scope audit: 2026-11-14T22:38:21-08:00/2026-11-14T22:39:11-08:00 (50 seconds).
- Delegated UI integration: 2026-11-14T22:39:27-08:00/2026-11-14T22:41:41-08:00 (134 seconds).
- Delegated redirect implementation: 2026-11-14T22:39:51-08:00/2026-11-14T22:41:23-08:00 (92 seconds).
- Delegated final scope review: 2026-11-14T22:42:15-08:00/2026-11-14T22:43:29-08:00 (74 seconds). Intervals overlap and are not additive person-hours.

## Context and decision

Steven requested a PR for Node 3 and the main proof-map changes, synchronized
with main. Following the [Node 3 edits](2026-11-14-223418-expand-node-three-evaluations-in-sign-polynomials.md)
and the [earlier isolated PR workflow](2026-11-14-213126-prepare-node-two-script-pull-request.md),
fetch origin and create `steven/node-3-and-proof-map` in
`/private/tmp/circulant-node3-proof-map-pr`, based on current main
`3f3c26ca74fcfc3bbb4b2e822e80b31e5cc12dd8`. Preserve the original dirty checkout and its other drafts.

Include the exact approved six-slide script, Node 3's five-node refinement,
main-page CRT/normalization/circle exposition, and expanded boxed lemma. Bring
the eight main proof nodes onto the homepage; include their current high-level
statements, Node 2's revised exposition, statement-box styling, and compiled
graph labels. Retain current main's published videos, captions, five Node 1
cuts, graph disclosures, rounded muted arrows, 112px nodes, and lean headings.
The root-local renderer is older, so do not copy it wholesale.

Keep Node 2 and Nodes 4–8 detailed graphs and scripts local. Node 8 keeps its
already published proof as the excerpt introducing a single unnumbered theorem
child; later refinement can insert the remaining steps and number that child.
The theorem avoids references to absent Node 8.4 or a completed Node 4 refinement.
Node 2 and Node 4 remain accepted inputs. Main cards for terminal nodes use
explicit parent excerpts, because their default excerpt is only a short summary.
References to unavailable smaller graphs in these scoped excerpts are adjusted.

## Rationale

An isolated main-based branch protects concurrent edits and avoids overwriting
Tomas's new media and interface work. Publishing the shared map entails moving
existing URLs: preserve retired reading-route entrypoints and general-proof-
prefixed proof URLs with static redirects and ordinary fallback links. The
redirect targets derive from actual entries and never replace live pages.
Archive the old outlines outside the active node directory.

Carry relevant historical decision records without changing their original
outcomes; these records describe the larger local website at their recorded
times. Convert one link to an unpublished historical record into a plain
filename in the PR copy. The current PR scope and validation are recorded here.
Keep graph titles/navigation accessible as plain text while typesetting visual
labels. Browser review found the long Node 3 norm summary clipped at 14px;
use 12px summary text to fit the complete identity without dropping P arguments.

## Evidence and outcome

- Graph-label regressions failed two checks before implementation and pass after.
  Redirect regressions had three expected missing-route failures before the fix;
  all six redirect checks now pass. Full integration initially exposed a removed
  general-route fixture and a changed diagnostic label; update the fixture to the
  homepage and preserve the existing map-summary diagnostic.
- The exact PR branch passes all 81 tests (5,531 assertions) and builds 20 active
  node pages plus compatibility redirects. Full repository lint passes; before
  staging, retired-file notices reflect the intentional archive moves.
- Independent review verified five published video metadata records and five cut
  timings unchanged, no media or Node 1/2 script differences from main, and an
  exact match between the approved Node 3 script and its PR copy.
- All 236 pre-existing source files in the original working checkout match their
  initial hashes. A read-only relative-link review passed. Two documentation
  inconsistencies (a table break and retired routing instructions) were fixed.
- Inspected the main map and 500px Node 3 statement on the exact PR build. Verified
  the final formula-size correction visually. Temporary QA pages and the reused
  dependency symlink were removed before staging.
- No new mathematical result is claimed. Commit, push, and PR creation follow
  this record; a subsequent entry records the observed publication outcome.

## Report relevance

Records user-authorized integration of reviewed exposition with current
collaborator work, preservation of published resources and URLs, and AI-assisted
scope separation, regression checks, and visual verification.
