# Animate section anchor scrolling

- Recorded at: 2026-11-15T11:37:55-08:00
- Observed implementation/check interval: 2026-11-15T11:36:48-08:00/2026-11-15T11:37:55-08:00 (67 seconds).
- Participants: Tomas Ortega (request); OpenAI Codex, GPT-6 (implementation
  and browser checks).

## Context and decision

The user requests the animation that scrolls to a clicked TOC section.
Add `motion-safe:scroll-smooth` to the document root. Native same-page anchors
scroll smoothly, retaining their URLs and normal link behavior. Reduced-motion
preferences retain instant scrolling. Preserve the
[title-link dismissal](2026-11-15-113029-dismiss-contents-on-title-link.md).

## Rationale

The pinned upstream [scroll utility](https://github.com/3b1b/3Blue1Brown.com/blob/4bcd89ef6e61e35001f58a58753226939eda3d89/app/util/dom.ts)
uses browser-native smooth scrolling. One Tailwind utility supplies that behavior
for ordinary anchors here, without an event handler, new state or dependency.
The preference is evaluated by CSS, including later changes to reduced motion.

## Evidence and outcome

Before implementation, 16 motion/trajectory assertions fail. Afterward, all
72 browser assertions pass in Chromium and Firefox at desktop and phone widths,
with normal and reduced motion. Frame samples confirm actual intermediate
scroll positions with normal motion and instant navigation with reduced motion.
Checks cover pointer/keyboard navigation, target alignment and hashes, sections
keeping the TOC open, and title navigation closing it. All 185 website tests
(10,009 assertions), the 48-page build, lint and whitespace checks pass.
Browser harnesses are temporary. Safari and physical phones were not tested.

## Report relevance

Records a user-directed navigation animation with failed-first behavior checks.
Mathematical content and media are unchanged.
