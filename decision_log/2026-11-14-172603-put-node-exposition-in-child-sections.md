# Put expanded-node exposition in its child sections

- Recorded at: 2026-11-14T17:26:03-08:00
- Observed work interval: 2026-11-14T17:21:07-08:00/2026-11-14T17:26:03-08:00 (296 seconds through this record).
- Participants: Steven Creech (layout clarification and dictionary-card request);
  OpenAI Codex, GPT-6 (primary implementation and delegated content/documentation).
- Content interval: 2026-11-14T17:21:54-08:00/2026-11-14T17:22:46-08:00
  (52 seconds). Documentation interval: 2026-11-14T17:22:06-08:00/2026-11-14T17:22:34-08:00
  (28 seconds). These overlap the primary interval and are not additive person-hours.

## Context and decision

Steven clarified the structure while exploring Node 1: after its video and
graph, put the written exposition in the individual subsection cards, with
links to go deeper. On the main page, the Group-Ring Encoding card should
state the dictionary result it establishes. This refines the
[video, graph, text decision](2026-11-14-170447-video-graph-text-reading-order.md)
and the [Node 1 refinement](2026-11-14-164817-refine-node-one-from-corrected-script.md).

For non-root nodes with children, remove the separate body and summary block
from their own pages. Keep their video and graph, dependency navigation, and
child sections. Preserve the main page's recently edited definitions, example,
and theorem, and keep terminal nodes' full explanations on their own pages.

Redistribute Node 1's exposition across its five existing child `script: |`
blocks: group ring and polynomial encoding; cyclic shifts and indexing; star;
correlations and the order-four dot products; and the dictionary equivalence
with its proof sketch and translation table. Preserve the explicit polynomial
notation and fixed first row. Production narration and deeper child proofs
remain separate and unchanged by this request.

## Rationale

Use an expanded node's Markdown body as its concise goal statement. When a
parent has no explicit child `script`, the loader now uses that body for an
expanded child's card. Explicit parent text still takes precedence, and a
terminal child's default remains its short summary. This makes the main-page
Group-Ring Encoding card display the self-contained dictionary lemma from
[Node 1](../website/nodes/group-ring-encoding.md) without duplicating its source.
The lemma states both the polynomial identity and its matrix equivalent.

Apply the existing theorem-rule styling to blockquotes in child cards. Retain
all deeper links, video placeholders, and dependency edges. Update website
instructions, authoring documentation, and script guidance to describe the
parent-card statement and child-section exposition model.

## Evidence and outcome

- Added checks for expanded-node goal fallback, explicit excerpt precedence,
  terminal summary fallback, dictionary placement on the main page, and math
  and deeper links in all five Node 1 sections. The fallback test failed with
  the previous loader before the implementation changed.
- Updated existing page-order checks for subsection text. Removed an old
  dependency test assertion requiring a standalone summary paragraph on every
  page; the graph/video and link checks remain, and content ordering is covered
  separately. All 41 tests passed (5,023 assertions).
- The build emitted 17 pages. Required repository lint, explicit lint of the
  untracked graph test, and `git diff --check` passed.
- Browser inspection confirmed Node 1 goes from its video and graph to the
  subsection navigation and explanations, with no separate introductory body.
  A full main-page capture confirmed the dictionary card and deeper link.
  Two anchor-based captures were blank and logged GPU errors; a fresh-profile
  full-page capture rendered correctly. No source change was needed for that
  capture problem. Opened the reorganized Node 1 local page for Steven.
- This reorganizes existing elementary mathematics; no new research result
  or formal verification is claimed. Earlier uncommitted work is preserved.
  No commit, push, recording, or hosted deployment was made.

## Report relevance

This records a user-directed change to the recursive exposition model:
a parent card states a result, and the corresponding expanded page explains
its constituent steps in separate sections. The AI assistance covers content
organization, rendering behavior, authoring guidance, and verification.
