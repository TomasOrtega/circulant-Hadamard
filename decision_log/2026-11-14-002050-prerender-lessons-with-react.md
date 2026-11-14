# Pre-render recursive lesson views with React

- Recorded at: 2026-11-14T00:20:50-08:00
- Observed work interval: 2026-11-14T00:03:39-08:00/2026-11-14T00:20:50-08:00
- Participants: user (authorization to use React and request to commit and push); Codex (architecture and implementation).

## Context and decision

The recursive lesson structure now needs a shared layout across many pages.
Use React 19.2.7 and React DOM to generate static HTML through
[build-lessons.jsx](../website/build-lessons.jsx), replacing the single-page
approach in the [earlier tooling decision](2026-11-13-234909-bun-and-static-html.md).

Keep Bun and the existing copied Tailwind stylesheet. Reuse the upstream
lesson, section, typography, and button conventions in
[lesson.jsx](../website/lesson.jsx), with attribution in the
[vendor notes](../website/vendor/README.md).

Each lesson has an explicit HTML URL. Navigation uses ordinary links, including
direct parent links and breadcrumbs. Pages have no client-side JavaScript,
router, or hydration requirement. Videos use native controls or YouTube embeds
when configured.

## Rationale

React makes the repeated lesson layout a reusable component. Pre-rendering
matches the upstream lesson site's delivery and keeps deep links, refreshes,
browser history, and keyboard navigation native to the browser.

Using relative URLs supports deployment under a repository subpath without
server rewrite rules. The [authoring guide](../website/README.md) explains the
tree, media fields, and undergraduate cutoff.

## Evidence and outcome

- Eight Bun tests passed with 311 assertions across navigation, build output,
  authoring constraints, mathematical example checks, and configured media.
- A clean frozen install passed the tests and generated all 12 pages.
- The production build and lint checks passed.
- The copied upstream stylesheet remained unchanged.
- CI now runs the lesson tests before its production build.

The browser host was unavailable, so visual browser QA could not be performed.
The user authorized a commit and push after verification.

## Report relevance

This records a change in implementation driven by the new lesson requirements,
with the earlier static-page decision preserved. Codex implemented and checked
the layout, content model, and generator. This interval overlaps the
[lesson hierarchy work](2026-11-14-002050-recursive-lesson-hierarchy.md) and is not additive person-hours.
