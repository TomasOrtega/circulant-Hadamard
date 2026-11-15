# Website styling

Adapted from [3Blue1Brown's agent guide](https://github.com/3b1b/3Blue1Brown.com/blob/main/AGENTS.md),
reviewed on 2026-11-14.

Use Tailwind 4 utilities in the HTML and the upstream theme and base styles in
[vendor/3b1b.css](vendor/3b1b.css). Keep the copied file unchanged; its revision
and provenance are in [vendor/README.md](vendor/README.md).

- Start with existing elements and selectors. Add a variant only for a distinct
  need; keep the implementation small.
- Prefer Tailwind classes. Add custom CSS to [styles.css](styles.css) only when
  utilities cannot express the requirement. Reserve style attributes for values
  computed at runtime.
- Reuse the upstream theme for colors, fonts, spacing, and widths. Use Tailwind's
  `--spacing()` function in `calc()` expressions and its color-alpha utilities.
- Keep the black masthead, white page, blue accent, serif copy, and sans-serif
  headings and navigation consistent.
- Resolve precedence through conditional classes or cascade layers; avoid the
  important modifier.
- Name CSS classes and assets in kebab-case; keep page assets with their page.
- Choose features established across Chrome, Firefox, and Safari for at least a
  year.
- Explain unusual tradeoffs briefly; record substantive exceptions in the
  [decision log](../decision_log/README.md).

Use Bun for dependency installation and scripts, with the pinned version in
[package.json](package.json) and the committed `bun.lock`. Keep application code
compatible with Node.js 24+ as a fallback. Use React to pre-render node views
into static pages. Keep graph, breadcrumb, and parent navigation as ordinary
links. Limit client JavaScript to page controls, playback bounds for native video cuts, and
small, self-contained mathematical illustrations requested for a node.
Use the top-left contents panel for page headings and the footer switch for
persistent dark mode. Hide these controls in print.
Keep a useful static diagram and explanation when JavaScript is unavailable;
use native keyboard-accessible controls and keep arithmetic congruences
distinct from complex-plane geometry.

Use the vocabulary in [GLOSSARY.md](../GLOSSARY.md): nodes at every depth.
Keep one Markdown file per node in [nodes/](nodes/), starting at
[overview.md](nodes/overview.md). Put metadata in YAML frontmatter and prose and
LaTeX in the body. Child IDs replace code imports; cut scripts use YAML literal
blocks (`script: |`) and support Markdown and math. The homepage owns the
eight main proof nodes in one hierarchy. Main overviews use order 36 as a
guiding example, while deeper nodes develop the general argument. Show Steven
Creech and Tomas Ortega below the homepage title. Redirect the former
Proof by Example and General Proof guide URLs to the homepage.
Keep the order-four and order-16 examples where
they clarify a lemma. Every view
has its own full overview video and written explanations. Retain redirects
when published node paths change.
Show a dependency graph when the view or its parent has proof children.
After the video and graph, an expanded proof node puts its exposition in
the individual child sections, each with a link to go deeper.
Place each neutral “Dig in deeper” button in a right-aligned row directly below
its child heading, with a small gap and its child-node count to the right.
Keep the exposition at full section width.
Its Markdown body states the goal proved by that node and appears in its parent's section,
rather than as a separate block on its own page. A parent's explicit child
`script` overrides that goal statement; a terminal child's fallback is its
short summary. Put each step's explanation in the parent's child `script: |`.
The main overview retains its definitions, example, and theorem after its
graph. Terminal proof views retain their full Markdown body after the
parent-map disclosure. Each preview is a timed cut of the parent's video
alongside the reader-facing explanation of that step; a child's own video is its separate,
deeper overview. Keep production narration in `scripts/`: `overview.md` at the
top level, and each main node's script and subnode scripts in `node1/`, `node2/`,
and so on, retaining descriptive filenames. Keep supporting sources in that
node folder's `reference/` directory.
Validate dependency references and cycles, cut bounds, and script content.
Render inline `$...$` and display `$$...$$` math at build time with MathJax SVG.
Refer directly to the group ring $\mathbb Z[X]/(X^n-1)$ or $\mathbb Z[C_n]$;
avoid introducing an additional symbol for it. Use “this group ring” in prose
once the context is clear.
Write $c(P),d(P),g(P),E(P),J(P)$ when referring to formal polynomials,
and use the actual argument for evaluations, such as $c(1)$ or $E(\omega)$.
Keep established functional notation such as $\Delta(c)$ and explicitly
defined scalar abbreviations distinct from polynomial notation.
Keep generated math styles in the shared `math.css`; content needs no client
math renderer. Preserve node paths and parent context when editing the loader.
Every non-root view must have a visible link back to its direct parent.
Stop expanding at standard undergraduate prerequisites: `foundation: true`
nodes must have no children. Record unfinished proof status with `draft: true`
in metadata; page headings show only node titles. Leave unavailable videos
as empty slots.

Run `make -C website check` and `make -C website` after changes. Preview `website/dist/`: the source
`styles.css` requires compilation. The build installs locked dependencies when
needed and emits node pages, CSS, the cut player, local fonts, and licenses.
See [README.md](README.md) for node and video authoring.

Put formal theorem, lemma, and proposition statements in Markdown blockquotes
with bold labels. The shared renderer gives them a blue border, subtle background,
and padding; keep proofs outside the box. Graph `mapTitle` and `mapSummary`
support inline math with the shared renderer. Retain plain navigation titles,
and avoid links, images, and block Markdown inside graph labels.
