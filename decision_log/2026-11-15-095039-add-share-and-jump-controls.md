# Adapt the upstream share and jump controls

- Recorded at: 2026-11-15T09:50:39-08:00
- Observed work interval: 2026-11-15T09:49:12-08:00/2026-11-15T09:50:39-08:00 (87 seconds through browser validation).
- Participants: Tomas Ortega (issue request); OpenAI Codex, GPT-6
  (implementation and checks).

## Context and decision

[Issue #14](https://github.com/TomasOrtega/circulant-Hadamard/issues/14)
requests 3Blue1Brown's bottom-right share and jump-to-top overlay. Inspect
`ViewCorner.tsx`, `Jump.tsx`, `Share.tsx`, and `util/url.ts` at the website's
already pinned upstream revision. Adapt those controls to the static node
renderer, with inline SVG icons and one small script, and document provenance.

This extends the [upstream-style decision](2026-11-13-232834-website-style.md).
The user's feature request extends the earlier restriction on client scripts;
update that instruction to include these page controls.

## Rationale

Reuse the fixed corner layout, contrast treatment, focus/hover labels, and
500-pixel jump threshold. Native sharing falls back to clipboard copy; an
unavailable clipboard presents a native copy prompt. Cancellation stays quiet.
Respect reduced motion when returning to the top. Hide inert controls when
JavaScript is unavailable and omit them from print. No client React, icon
package, analytics, or new repository dependency is needed.

## Evidence and outcome

- All 188 website tests pass (9,894 assertions), and all 50 pages build.
  The new minified controller is 0.73 KB.
- Browser checks in Firefox 153 and Chromium exercise keyboard jump, threshold
  visibility, reduced-motion return, fixed placement at a 390-pixel width,
  print hiding, and hidden controls with JavaScript disabled.
- Browser API stubs verify native-share delegation with the current page URL,
  unsupported/failed sharing with clipboard fallback, quiet cancellation,
  and a copy prompt when clipboard access fails. The operating-system share
  sheet itself was not invoked. A phone-width screenshot was inspected.
- Repository lint and whitespace checks pass. Existing proof navigation,
  mathematical content, and video assets are unchanged.

## Report relevance

Records adaptation of the referenced site's navigation affordances, with
browser checks of fallback behavior. It adds no mathematical claim.
