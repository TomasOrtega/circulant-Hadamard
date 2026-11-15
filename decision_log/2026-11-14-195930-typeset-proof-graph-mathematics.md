# Typeset the proof-graph labels with the shared LaTeX renderer

- Recorded at: 2026-11-14T19:59:30-08:00
- Observed work interval: 2026-11-14T19:54:34-08:00/2026-11-14T19:59:30-08:00 (296 seconds through this record).
- Participants: Steven Creech (reported untypeset graph math); OpenAI Codex,
  GPT-6 (implementation, delegated metadata conversion and design review,
  and validation).
- Delegated intervals: metadata conversion,
  2026-11-14T19:55:10-08:00/2026-11-14T19:56:10-08:00 (60 seconds);
  renderer review,
  2026-11-14T19:55:20-08:00/2026-11-14T19:55:53-08:00 (33 seconds).
  These overlap the primary interval and are not additive person-hours.

## Context and decision

Steven reported that the mathematical text in the graphs did not look like
the site's normal compiled LaTeX. Inspection confirmed that the SVG graph
rendered raw text while the surrounding prose used MathJax. Unicode
superscripts, subscripts, stars, and fraction approximations bypassed the
[existing math pipeline](2026-11-14-013449-markdown-node-authoring.md).

Correct [dependency-graph.jsx](../website/dependency-graph.jsx) to use that
same build-time Markdown/MathJax renderer for its labels. Place the generated
HTML and SVG math inside an SVG foreignObject; retain each outer SVG link,
plain accessible name, node position, and dependency arrow. Keep visual
labels out of pointer hit-testing and redundant accessibility output.
Use the existing font, color, and spacing utilities rather than modifying
the vendored stylesheet or adding a client math runtime.

Convert mathematical map summaries to inline LaTeX in 29 node frontmatters.
Add optional mapTitle for five titles containing mathematical notation;
leave title and shortTitle plain for navigation and accessible names.
Graph summaries and titles use genuine stars, fractions, subscripts,
superscripts, and symbols. The mathematical statements and node bodies
remain unchanged.

Collect graph-label styles in [mathStyles](../website/markdown.js), including
when there is no math in page bodies. Document inline label authoring and
single-quoted YAML in the website README and AGENTS instructions.

## Rationale

Reuse the current renderer so the equations have the same appearance and
error handling as the prose. A foreignObject supports mixed ordinary text
and compiled inline math while preserving the existing SVG graph geometry.
Browser text layout replaces character-count wrapping, which would split
LaTeX commands. Tight paragraph line height and disabled text trimming keep
fractions and exponents inside the node boxes.

Render the node number separately: prefixing Markdown with “1. ” would
parse as an ordered list. Keep graph-only math titles separate from plain
navigation titles so breadcrumbs and accessible labels never expose TeX.
Restrict authored labels to short inline prose/math; links, images, and
block Markdown do not belong inside an already-clickable node box.

## Evidence and outcome

- Added three regression checks first. All failed before the fix: graph
  math produced no compiled SVG, graph-only equations contributed no CSS,
  and malformed graph TeX was not validated. All pass with the fix.
- All 53 website tests pass (6,158 assertions), covering both graph layouts,
  ordinary links, plain accessible names, separate numbering, graph-only
  math CSS, malformed TeX, and existing navigation and content behavior.
  The build still emits 35 pages.
- All 39 graph metadata fields parse and render. Delegated review measured
  the longest math fragments below 45ex, fitting the existing summary area.
- Browser inspection of the main graph and Node 1 confirmed compiled stars,
  sums, fractions, subscripts, and superscripts without clipped equations.
  A 500px Node 2 preview confirmed labels render within the existing
  horizontally scrollable graph. Screenshots are temporary local artifacts.
- Required lint completed with the previously known notices for unstaged
  archived paths. Explicit lint of all 188 existing files passed, as did
  whitespace checks. The refreshed local main page was opened for Steven.
- No mathematical claim, dependency structure, video, commit, push, PR, or
  hosted deployment was changed by this task. Earlier local work is retained.

## Report relevance

This is a user-reported presentation bug fix with AI-assisted rendering
implementation, metadata conversion, and browser checks. It extends the
existing static math pipeline to proof maps without adding mathematical
results or changing the argument.
