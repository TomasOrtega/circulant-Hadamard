# Author proof nodes in Markdown with LaTeX

- Recorded at: 2026-11-14T01:34:49-08:00
- Observed work interval: 2026-11-14T01:10:03-08:00/2026-11-14T01:34:49-08:00 (24 minutes 46 seconds).
- Participants: user (format acceptance and integration request); Codex (GPT-6, implementation and checks).

## Context and decision

The user accepted the recommendation to replace JavaScript node content with
Markdown and YAML frontmatter, then integrate and push the changes. Migrate all
12 files in [website/nodes/](../website/nodes/), starting at
[overview.md](../website/nodes/overview.md). This supersedes the JavaScript
format in the [earlier node-file decision](2026-11-14-005903-node-terminology-and-files.md)
while retaining its node vocabulary and one-file-per-node organization.

Put the full script and explanation in the Markdown body. Put metadata, video
sources, dependency IDs, and cut bounds in YAML. Parent cut scripts are Markdown
literal blocks; child references use IDs rather than code imports. Support
inline `$...$` and display `$$...$$` LaTeX in both full explanations and cuts.

Use [remark-math and rehype-mathjax](https://github.com/remarkjs/remark-math)
to render static SVG at build time. Extract MathJax's generated style blocks
into shared `math.css` and include its license. Keep glyphs self-contained
without generated glyph IDs or a browser math runtime.

## Rationale

Markdown removes code syntax and escaped backslashes from routine math editing.
YAML keeps the existing graph and video-cut structure readable without mixing
content with React. MDX's executable component syntax is unnecessary for the
current prose, equations, and metadata.

The [loader](../website/load-nodes.js) resolves shared node IDs before the
existing hierarchy, dependency, undergraduate-depth, and cut validation runs.
The [renderer](../website/markdown.js) supports ordinary Markdown and GFM tables.
Malformed YAML, unknown node references, and invalid TeX stop the build with
authoring errors. Preserve current URLs, parent contexts, video placeholders,
and the footer. Leave the vendored 3Blue1Brown stylesheet unchanged.

Update the [authoring guide](../website/README.md) and
[website agent instructions](../website/AGENTS.md). Maintain the older decision's
source link through its pre-migration Git snapshot rather than changing its
historical explanation. The checkout is already on `main`; a fresh fetch
confirmed it matched `origin/main` before integration.

## Evidence and outcome

All 29 website tests passed (585 assertions). A separate temporary source copy
passed a frozen dependency install, tests, and production build: 12 Markdown
node files produced 12 static pages. The lockfile stayed unchanged during that
install. Incremental Make targets were up to date.

Checks cover inline and display math, Markdown formatting, malformed content,
shared references, dependency graphs, deep links, direct-parent navigation,
video sources and cuts, terminal undergraduate nodes, and retained footer
wording. The order-four example's actual Markdown matrix was checked by direct
row-inner-product arithmetic. No mathematical proof claim was added.

The generated pages use static SVG and separate math CSS. Their local links
resolve, the MathJax license is included, and the upstream CSS is byte-identical.
No real video sources or cut timings were supplied; their slots remain empty.
Browser preview was unavailable in this session, so visual inspection remains
a limitation. Unrelated research records appearing concurrently were excluded
from this website change.

## Report relevance

This records a content-authoring and rendering improvement implemented with
Codex during the measured interval. The contribution is website infrastructure
and editable mathematical exposition, not a new proof result. Automated checks
verified the migrated structure and math rendering; the team's proof and video
content still need to be supplied.
