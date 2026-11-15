# Restore the example and general reading-route entrypoints

- Recorded at: 2026-11-14T23:09:07-08:00
- Observed work interval: 2026-11-14T22:59:42-08:00/2026-11-14T23:09:07-08:00 (565 seconds).
- Participants: Tomas Ortega (reported the missing start buttons and requested usable proof-by-example navigation); OpenAI Codex, GPT-6 (delegated regression, restoration, source adaptation, and validation).

## Context and decision

The latest merged proof-map change removed the homepage's start buttons and
made both former route URLs redirect to the homepage. Restore visible example
and general start links while preserving the new unified hierarchy of eight
main proof nodes. This follows the new user request and changes the route-entry
behavior chosen in the [unified-journey decision](2026-11-14-182210-unify-example-and-general-proof-journey.md)
and [Node 3 publication preparation](2026-11-14-224622-prepare-node-three-and-main-proof-map-pr.md).
The archived records and files remain unchanged.

## Rationale

Build two supplementary reading guides from [reading-routes/](../website/reading-routes/)
at their existing published URLs. These entries sit outside the main proof's
child/dependency hierarchy. Homepage-only ordinary link buttons open them;
their breadcrumbs and parent returns lead directly back to visible homepage
anchors. Existing redirects for old general-proof-prefixed deeper node URLs
remain intact. No client navigation code or duplicate proof subtree is added.

Reuse the archived order-36 and general odd-u mathematics, replacing source-file
links with current page links. The order-36 guide explicitly states the fixed
linear combination E, copied from the general outline, before using its linearity.
The Δ-theorem remains an accepted input, and the example is not claimed to prove
every order. The general guide presents the alternating-product argument and
links into the same main proof map and its deeper nodes. The original video
metadata, parent cuts, and production scripts are untouched by this restoration.
Add reading-guide Markdown to the existing Makefile content dependency list so
editing a guide triggers the normal static rebuild.

## Evidence and outcome

Before implementation, three new production regressions failed: homepage start
buttons were missing, and both route entrypoints contained meta-refresh redirects
to the root. After the fix, all four reading-route tests pass, including actual
proof text, rendered mathematics, ordinary destination links, and return anchors.
Update two stale no-reading-route expectations to require homepage-only buttons
and keep the proof hierarchy itself free of supplementary route children.
The synthetic-tree redirect test still covers its custom-tree fallback behavior.

All 87 website tests pass; the production build emits 22 pages, including both
reading guides. All generated guide links and return anchors resolve; deep legacy
redirect tests pass. Scoped whitespace checks pass. Browser screenshot preview
was attempted, but this child's preview runtime cannot import Playwright or
Playwright Core (“index.js does not provide an export named default”). The primary browser-preview attempt also failed because the computer-use
host was unavailable. No browser screenshot is claimed. The primary agent
verified served HTML destinations and runs final repository lint before the
scoped commit.

## Report relevance

Records a user-directed navigation repair after a hierarchy simplification,
with failing-first regression evidence. Existing mathematical exposition is
restored and linked; no new proof or video is invented.
