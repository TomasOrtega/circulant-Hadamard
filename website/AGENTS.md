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
links. Limit client JavaScript to playback bounds for native video cuts.

Use the vocabulary in [GLOSSARY.md](../GLOSSARY.md): nodes at every depth.
Keep one content file per node in [nodes/](nodes/), starting at
[overview.js](nodes/overview.js). Every view has its own full overview video,
a dependency graph immediately below it, script-based text, and child previews.
Each preview is a timed cut of the parent's video, using the corresponding
parent-script excerpt; a child's own video is its separate, deeper overview.
Validate dependency references and cycles, cut bounds, and script content.
Every non-root view must have a visible link back to its direct parent.
Stop expanding at standard undergraduate prerequisites: `foundation: true`
nodes must have no children. Keep unfinished proof material visibly marked as
draft, and leave unavailable videos as empty slots.

Run `make -C website check` and `make -C website` after changes. Preview `website/dist/`: the source
`styles.css` requires compilation. The build installs locked dependencies when
needed and emits node pages, CSS, the cut player, local fonts, and licenses.
See [README.md](README.md) for node and video authoring.
