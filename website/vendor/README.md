# 3Blue1Brown styles

`3b1b.css` is an unchanged copy of
[`app/styles.css`](https://github.com/3b1b/3Blue1Brown.com/blob/4bcd89ef6e61e35001f58a58753226939eda3d89/app/styles.css)
from `3b1b/3Blue1Brown.com`, revision
`4bcd89ef6e61e35001f58a58753226939eda3d89`, retrieved on 2026-11-13.
Its source is Tailwind CSS. The repository contains no SCSS files at this
revision.

Keep the copied stylesheet unchanged and update this provenance when replacing
it. Add project-specific styles to the entry stylesheet or the page's Tailwind
classes.

The node layout also follows the same revision's
[`Lesson.tsx`](https://github.com/3b1b/3Blue1Brown.com/blob/4bcd89ef6e61e35001f58a58753226939eda3d89/app/pages/lessons/Lesson.tsx)
and [`Button.tsx`](https://github.com/3b1b/3Blue1Brown.com/blob/4bcd89ef6e61e35001f58a58753226939eda3d89/app/components/Button.tsx)
class conventions: a tinted lesson header, alternating article sections, narrow
reading columns, and shared button colors and sizes. The React components are
adapted for this project's static recursive nodes.

The fixed page controls adapt the same revision's `ViewCorner.tsx`, `Jump.tsx`,
`Share.tsx`, `Feedback.tsx`, and `util/url.ts`: jump to top after scrolling,
native sharing with a copy-link fallback, and feedback linking to GitHub issues.
The static implementation uses inline SVG icons
and no client React runtime.

The contents panel and masthead appearance switch follow `TableOfContents.tsx`,
`DarkMode.tsx`, and `Nav.tsx` at the same revision. The static panel keeps section
navigation open, reserves reading space on desktop, and uses a drawer on smaller
screens. Its slide and toggle fade use upstream Tailwind transition timing;
desktop reading space moves with the panel. Reduced motion disables transitions.
The switch uses the existing dark palette.

The upstream repository has no license file at this revision; this copy does
not assign a license to their work. Tailwind's MIT license and the Fontsource
fonts' SIL Open Font Licenses are included in the built website.
Build-time math rendering uses MathJax; its Apache license is included as
`mathjax-LICENSE.txt` alongside the generated SVG and shared math styles.
