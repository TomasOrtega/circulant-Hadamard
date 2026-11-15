# Place neutral deeper links directly below their titles

- Recorded at: 2026-11-15T10:13:30-08:00
- Observed work interval: 2026-11-15T10:12:03-08:00/2026-11-15T10:13:30-08:00 (87 seconds through browser validation).
- Participants: Tomas Ortega (layout question and approval); OpenAI Codex,
  GPT-6 (recommendation, implementation, and checks).

## Context and decision

After asking whether below-title links fit the 3Blue1Brown style, the user
approved that recommendation: place each “Dig in deeper” link directly below
its title, left-aligned with the text, with a small gap and neutral styling.
This supersedes the [side-by-side layout](2026-11-15-094840-wrap-deeper-links-beside-headings.md).
The upstream guide leaves this placement open; this is the user's accepted
design choice rather than an upstream requirement.

## Rationale

A simple column header gives all screen sizes the same reading order and
keeps long headings at full width. Reuse the existing neutral navigation
style for optional deeper links. Remove the now-unused filled-button variant
and heading sizing classes. Update the website guidance to match the choice.
No custom CSS, client script, or dependency is needed.

## Evidence and outcome

- All 188 website tests pass (9,894 assertions), and all 50 active pages build.
- Firefox 153 and Chromium checks cover every child header on the homepage
  and Group-Ring Encoding at 320, 390, 768, and 1280 pixels. Each link sits
  below its heading with a gap under 24 pixels, aligns with the header's left
  edge, fits within the viewport, and has a transparent default background.
  Desktop and phone screenshots were inspected.
- Repository lint and whitespace checks pass. The shared renderer loses ten
  net lines; mathematical content, link destinations, and videos are unchanged.

## Report relevance

Records a user-approved revision to presentation and a smaller renderer.
It adds no mathematical claim or proof verification.
