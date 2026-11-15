# Inherit contents transitions

- Recorded at: 2026-11-15T11:22:11-08:00
- Observed implementation/check interval: 2026-11-15T11:18:47-08:00/2026-11-15T11:22:11-08:00 (204 seconds).
- Participants: Tomas Ortega (request); OpenAI Codex, GPT-6 (implementation
  and browser verification).

## Context and decision

The user requests 3Blue1Brown's nicer side-contents animations. Adapt the pinned
[TableOfContents.tsx](https://github.com/3b1b/3Blue1Brown.com/blob/4bcd89ef6e61e35001f58a58753226939eda3d89/app/components/TableOfContents.tsx)
slide and Tailwind transition timing: 150 milliseconds with the default
cubic-bezier(0.4, 0, 0.2, 1) easing. Fade the separate toggle, and move the
reserved desktop reading space with the panel. Honor reduced motion and clear
transitions in print. Retain the
[persistent sidebar behavior](2026-11-15-111048-keep-contents-open-beside-text.md).

## Rationale

Use existing Tailwind utilities and replace the controls' display-based hidden
state with native inert state. Closed controls remain unavailable to keyboard,
pointer and assistive navigation while their exit transition renders.
Keep the separate toggle and desktop reading lane required by the earlier
layout rather than porting the upstream React component. Add no timer,
framework, dependency or custom stylesheet rule; keep vendored CSS unchanged.

## Evidence and outcome

- The initial visibility-transition approach lost keyboard focus at the first
  animation frame. A browser assertion reproduced it. Opacity plus translation
  and inert state fixes both opening focus and Escape focus restoration.
- All 185 website tests pass (10,009 assertions); all 48 active pages build.
  Repository lint and whitespace checks pass. The minified page controller
  remains 2.68 KB, slightly smaller than the previous 2.69 KB build.
- 176 browser assertions pass in Chromium and Firefox at widths 1280, 390 and
  640 pixels, including a 640×320 short window, with normal and reduced motion.
  Checks sample opening/closing midway, matched panel/lane movement, toggle
  fades, focus entry/restoration, inaccessible closed controls, persistent
  heading navigation, outside dismissal, print and JavaScript-off behavior.
  An intermediate animation screenshot was inspected. Safari and physical
  phones were not tested. Temporary Playwright harnesses add no project dependency.

## Report relevance

Records a user-directed presentation refinement and checked accessibility
behavior. Mathematical content and video production are unchanged.

Publication check recorded at 2026-11-15T11:24:43-08:00: the
[CI run](https://github.com/TomasOrtega/circulant-Hadamard/actions/runs/43752052361)
passes its website, lint and deployment jobs. All 176 browser assertions also
pass on the public site; its stylesheet and page controller match the tested
build byte for byte. One initial harness assertion missed a toggle transition
after forcing the preceding animation to finish. Waiting two animation frames
before the next interaction resolves that sampling failure; project code
is unchanged by this harness correction.
