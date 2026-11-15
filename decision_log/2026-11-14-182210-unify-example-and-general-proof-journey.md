# Unify the example and general proof journey

- Recorded at: 2026-11-14T18:22:10-08:00
- Observed work interval: 2026-11-14T18:16:47-08:00/2026-11-14T18:22:10-08:00 (323 seconds through this record).
- Participants: Steven Creech (narrative and video-structure clarification);
  OpenAI Codex, GPT-6 (implementation, documentation, content review, and checks).
- Documentation interval: 2026-11-14T18:17:18-08:00/2026-11-14T18:17:48-08:00
  (30 seconds). Read-only content review:
  2026-11-14T18:17:24-08:00/2026-11-14T18:17:47-08:00 (23 seconds).
  These overlap the primary interval and are not additive person-hours.

## Context and decision

Steven clarified that the two example/general tabs suggested separate videos.
His intended structure is one proof journey: larger overviews use n=36 as a
guiding example, and deeper nodes develop the general statements and proofs.
This supersedes the separate reading routes in the
[original proof-map implementation](2026-11-14-151609-eight-node-proof-map.md).

Remove the reading-route navigation and the two supplemental pages from the
active hierarchy. Each node continues to own one full overview video, with
child excerpts cut from that parent's video. Keep the recursive graph and
[subsection exposition](2026-11-14-172603-put-node-exposition-in-child-sections.md).
Retain supporting order-four and order-16 examples where useful.

## Rationale

Removing only the buttons would leave standalone route pages and their video
placeholders. Archive both outlines under
[reading-routes](../website/archive/reading-routes/README.md) and remove the
unused supplemental-node filtering as well as the route component.

Explain the example-to-general progression on the main page. Use the caption
“The proof at a glance” and rename “First route” headings in six later nodes
to “Guiding example.” Replace the theorem's retired route link with the final
contradiction and proof map. Keep existing node URLs and parent navigation
for all retained proof nodes.

Preserve both archived outlines' mathematics and retarget their source links.
The general outline contained useful arithmetic-setting detail that was absent
from the active node: carry it into
[From Products to Sums](../website/nodes/products-to-sums.md), including the
ambient ring, invertible denominators, and divisions before reduction.

Update authoring and script guidance to describe one overview per node and
deeper general explanations. Production narration itself is not rewritten.

## Evidence and outcome

- The navigation regression check failed before implementation because the
  route selector was still present. It now checks exactly one overview slot
  per page and absence of the selector. The proof-map test also excludes the
  two retired routes from the active hierarchy.
- All 42 tests passed (5,233 assertions), including all internal links, parent
  anchors, math rendering, and configured-video behavior. The build emits
  21 pages; its existing cleanup removes the two obsolete route directories.
- All 64 local Markdown links resolve across 25 changed/new Markdown files.
  Parsed math expressions in both archives exactly match their prior committed
  versions; source links and obsolete continuation wording were adjusted.
- Required repository lint exited successfully but reported missing old paths
  for the unstaged archive moves. Explicit lint of all 162 existing tracked
  and untracked files passed, as did whitespace checks.
- Desktop and 500-pixel browser inspection confirmed the heading flows into
  one overview, with no route choices, and deeper parent navigation remains.
  The served main page contains the new narrative and caption. A final scan
  of all 21 built pages found one overview each and no retired route links.
  Opened the updated main page.
- Existing local Node 2 work is preserved. No video sources or timings were
  invented, and no commit, push, PR update, or hosted deployment was made.

## Report relevance

This records a user correction to the teaching structure, replacing parallel
reading routes with increasing depth in one hierarchy. It preserves the
mathematical drafts and clarifies the intended video production model.
