# Adopt 3Blue1Brown's website styling guidelines

- Recorded at: 2026-11-13T23:36:12-08:00
- Observed work interval: 2026-11-13T23:30:11-08:00/2026-11-13T23:36:12-08:00
- Participants: user (request); Codex (adaptation, implementation, and checks).

## Context and decision

The user requested the styling guidance from
[3Blue1Brown's AGENTS.md](https://github.com/3b1b/3Blue1Brown.com/blob/main/AGENTS.md).
Adapt the relevant rules in [website/AGENTS.md](../website/AGENTS.md) and link
them from the [root instructions](../AGENTS.md).

Apply the guide through shared design tokens in
[styles.css](../website/styles.css): consistent colors, a four-pixel spacing
scale, typography, content width, and navigation states. Match the reference's
350 font weight, heading size, paragraph leading, and compact masthead.
This refines the [earlier visual direction](2026-11-13-232834-website-style.md).

## Rationale

Shared tokens make later changes consistent. Retain the existing static HTML
and [separate CSS](2026-11-13-232834-separate-website-css.md), adapting the
upstream Tailwind-specific advice to this project's implementation. A framework
migration would add maintenance for this small page.

The scoped guide keeps website rules next to the files they govern and
attributes the upstream source. Its adaptation is explicit.

## Evidence and outcome

- Read the upstream guide and compared the reference's previously retrieved
  stylesheet for concrete design values.
- `make -C website` passed; built HTML and CSS matched their source files.
- Confirmed that page content and project links were preserved, with styling
  still in a separate file.
- Verified that Google Fonts serves both families at weight 350 for a modern
  browser. The initial generic-user-agent check returned legacy 300/400
  fallbacks; repeating the check with a modern browser user agent resolved it.
- `prek -a --quiet`, explicit lint checks on the changed and new website
  files and agent guides, and `git diff --check` passed. Local guide links
  resolved successfully.

Browser preview remains unavailable in this session, so the visual result has
not been checked in a browser.

## Report relevance

This is presentation and documentation work during the event. Codex adapted
the guide and implemented and checked the changes. It contributes no
mathematical claim; the checks and browser-verification limit are explicit.
