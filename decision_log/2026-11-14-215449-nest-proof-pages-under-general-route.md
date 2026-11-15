# Put proof pages under the general odd-u route

- Recorded at: 2026-11-14T21:54:49-08:00
- Observed work interval: 2026-11-14T21:50:46-08:00/2026-11-14T21:54:49-08:00
  (243 seconds through this record).
- Participants: user (navigation request); OpenAI Codex, GPT-6
  (regression, implementation, documentation, and checks).

## Context and decision

The user requested that every proof page except Proof by Example come from
The General Odd-u Proof. Move the eight main steps and theorem conclusion
from [overview.md](../website/nodes/overview.md) into the children of
[general-proof.md](../website/nodes/general-proof.md). Their five deeper
Group-Ring Encoding nodes follow the same ancestor, giving 14 proof pages
under the general route. The example and general route remain the homepage's
two direct children.

This revises the flat hierarchy in the
[eight-node map decision](2026-11-14-151609-eight-node-proof-map.md) and moves
the parent cards described in the
[exposition decision](2026-11-14-172603-put-node-exposition-in-child-sections.md)
onto the general proof page. Preserve the existing dependency edges, theorem,
and mathematical explanations. Keep the general route's full written proof
between its map and child sections. Omit empty dependency graphs on the
homepage and example page. Rename the homepage's short title to Overview,
and update prose links, authoring instructions, and navigation tests.

## Rationale

Make the content hierarchy own the requested parent relationship so graph
links, breadcrumbs, return anchors, asset paths, and child sections derive
consistent nested URLs. A back-button-only change would leave the general
proof without its actual child map. Pages containing only route choices have
no proof dependencies to draw; their route buttons provide navigation.

## Evidence and outcome

- Added the hierarchy regression before implementation. Running
  `bun test node.test.jsx -t 'all proof nodes belong'` failed because the nine
  main proof pages were direct homepage children; it passed after the move.
  This direct structural reproduction made broader speculative debugging
  unnecessary. Used the diagnosing-bugs and writing-for-agents skills.
- `make -C website check all` passed: 47 tests, 5,121 assertions, and 17
  generated pages. Existing checks validate every internal link and return
  anchor, graph edges, child sections, math, and relative asset references.
- `uv run --locked prek -a --quiet` and `git diff --check` passed.
- The existing server on port 4173 served the separate
  `circulant-Hadamard` checkout, so its initial preview comparison failed.
  Started this workspace's `website/dist` preview on
  [port 4174](http://127.0.0.1:4174/). An HTTP audit confirmed all 17 pages
  match the build, all 284 internal links and anchors resolve, and all 14
  detailed proof pages have paths beneath `nodes/general-proof/`.
- Browser visual inspection was unavailable: the computer-use tool reported
  that its browser access host was unavailable. HTTP and static-page checks
  provide the observed navigation evidence; no visual QA is claimed.
- Detailed page URLs now include `general-proof/`; legacy flat URLs are not
  generated or redirected. No commit, push, or hosted deployment was requested
  or performed.

## Report relevance

This is a user-directed correction to the exposition's navigation hierarchy.
AI assistance covered implementation, regression checks, and authoring notes.
The mathematical content and accepted-proposition status were preserved; no
new mathematical result or independent proof verification is claimed.
