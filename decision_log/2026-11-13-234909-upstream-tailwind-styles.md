# Use Tailwind and copy the upstream stylesheet

- Recorded at: 2026-11-13T23:49:09-08:00
- Observed work interval: 2026-11-13T23:36:58-08:00/2026-11-13T23:49:09-08:00
- Participants: user (direction); Codex (implementation and validation).

## Context and decision

The user clarified that the website should follow the upstream Tailwind
instructions and copy its styles. This replaces the plain-CSS adaptation in
the [previous styling decision](2026-11-13-233612-website-styling-guidelines.md).

Copy upstream `app/styles.css` unchanged to
[website/vendor/3b1b.css](../website/vendor/3b1b.css), pinned to revision
`4bcd89ef6e61e35001f58a58753226939eda3d89`. The inspected repository contains
Tailwind CSS and no SCSS files at this revision.

Use Tailwind 4.3.3 utilities in the HTML, with a separate CSS entry point and
compiled stylesheet. Bundle Fontsource 5.3.0 variable fonts locally.
Update the [website instructions](../website/AGENTS.md) and build accordingly.

## Rationale

Using the actual source keeps the theme, typography, responsive section layout,
and interaction styles aligned with 3Blue1Brown. An unchanged vendor copy with
[provenance](../website/vendor/README.md) makes future updates traceable.

The upstream checkout contains no license file; the provenance records that
fact without assigning a license. The build includes Tailwind's MIT license
and each font's SIL Open Font License.

## Evidence and outcome

- Compared the vendor file byte for byte with the pinned checkout: identical.
- Clean production build and a frozen Bun install in a fresh temporary checkout
  passed and produced identical CSS.
- Confirmed that Tailwind directives were compiled and the responsive and
  interaction utilities were emitted.
- Checked all font URLs against bundled WOFF2 files and their accompanying
  licenses. Attribution is included in the build.
- Compared body text and project links with the earlier page: preserved.
- The Node compiler fallback emitted identical CSS.
- `prek -a --quiet`, explicit lint checks on new files, and
  `git diff --check` passed.

Browser preview remains unavailable; verification covers source, assets, and
the production build.

## Report relevance

This records website presentation and AI-assisted implementation during the
event. No mathematical result is claimed. The source revision, checks, and
verification limits are explicit.
