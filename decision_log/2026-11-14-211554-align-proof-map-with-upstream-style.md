# Align proof maps with the upstream website style

- Recorded at: 2026-11-14T21:15:54-08:00
- Observed work interval: 2026-11-14T21:09:01-08:00/2026-11-14T21:15:54-08:00
  (413 seconds through this record).
- Participants: user (styling request); OpenAI Codex, GPT-6 (design,
  implementation, and validation).

## Context and decision

The user said the high-level proof map did not fit the 3Blue1Brown style.
Review the pinned upstream Card, Button, Heading, and Lesson components and
the existing vendored theme. Update [the shared graph renderer](../website/dependency-graph.jsx)
to use ruled captions, larger sans-serif titles, blue node numbers, serif
equations, white nodes, and lighter solid connections. Remove the enclosing
white board and reserve blue outlines for hover, focus, and the current node.
The Node 1 map uses the same presentation.

This refines the [earlier graph styling](2026-11-14-153401-simplify-proof-graph-style.md).
Retain its single accent color, solid arrows, dependency structure, and ordinary
links. Carry forward the user's preceding request to commit and push completed
website changes.

## Rationale

The upstream Card component emphasizes typography and hover treatment rather
than persistent outlines. Reuse its theme and the site's caption rules without
changing the vendored stylesheet or adding dependencies or client JavaScript.
Increase node height from 96 to 112 SVG units to fit the larger labels.

The first visual pass used serif text summaries. Inspection exposed literal
exponent and subscript markers, so convert all 14 map summaries to Markdown
with LaTeX and render them through the existing MathJax pipeline in SVG
`foreignObject` regions. Include their styles and validation in the shared
math stylesheet generation. Document this authoring support in the website README.

## Evidence and outcome

- `make -C website check all` passed: 44 tests, 5,051 assertions, and 17 pages.
  New checks cover rendered math inside every high-level node link, styles for
  map-only math, and rejection of malformed summary equations. Existing checks
  retain all dependency edges, context links, breadcrumbs, and return anchors.
- Safari inspection of the built site confirmed readable equations and titles
  in the high-level and Node 1 maps. Clicking a rendered equation opened its
  node; keyboard traversal reached the current Correlation Identity node and
  showed its blue emphasis. Parent-map expansion also worked.
- A narrower native window retained readable type and the existing contained
  overflow region. No phone-size or additional-browser visual run is claimed.
- Repository lint and `git diff --check` passed. No proof statements, dependency
  metadata, node positions, video sources, or vendored CSS changed.

## Report relevance

This is AI-assisted visual presentation and mathematical typesetting work
requested by the user. It reformats existing equations and adds no mathematical
result or independent verification of the proof.
