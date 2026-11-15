# Wrap deeper links beside headings and remove reverse dependency copy

- Recorded at: 2026-11-15T09:48:40-08:00
- Observed work interval: 2026-11-15T09:47:13-08:00/2026-11-15T09:48:40-08:00 (87 seconds through validation).
- Participants: Tomas Ortega (issue and minimal-change request); OpenAI Codex,
  GPT-6 (implementation and checks).

## Context and decision

[Issue #13](https://github.com/TomasOrtega/circulant-Hadamard/issues/13)
requests deeper buttons on the side when space permits, simpler styling, and
removal of “Used by”. Put each heading and deeper link in one wrapping flex
header. Remove the single-use Heading helper and reverse dependency/notation
rows and their computations. Keep prerequisite links and the full-width
exposition. Update the website guidance to match the user's current request.

This revises the below-heading placement retained in the
[child-section exposition decision](2026-11-14-172603-put-node-exposition-in-child-sections.md).
The newly merged thumbnail work was preserved when rebasing the previous
issue's documentation commit before its successful push.

## Rationale

The existing markup explicitly separated the heading from the controls.
A wrapping flex row handles available space without custom CSS, breakpoints,
or client code. Reverse relationships are already navigable in the proof map;
removing their repeated prose reduces both markup and calculation.

## Evidence and outcome

- Before the fix, the updated rendered-page header regression and new
  “Used by” absence check both failed. All 188 website tests now pass
  (9,894 assertions); all 50 active pages build.
- Firefox 153 and Chromium checks on the homepage and Group-Ring Encoding
  cover every child header at 320, 390, 768, and 1280 pixels. Buttons stay
  within the viewport, sit beside headings at 1280 pixels, and wrap below at
  320 and 390 pixels. Inspected desktop and phone screenshots match.
- Repository lint and whitespace checks pass. Production changes remove
  twelve net lines from the shared renderer. No proof content or video
  assets changed.

## Report relevance

Records an interface simplification and responsive layout correction.
It adds no mathematical result or proof verification.
