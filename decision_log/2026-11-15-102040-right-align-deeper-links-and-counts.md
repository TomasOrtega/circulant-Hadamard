# Right-align deeper links with their child counts

- Recorded at: 2026-11-15T10:20:40-08:00
- Observed work interval: 2026-11-15T10:16:58-08:00/2026-11-15T10:20:40-08:00 (222 seconds).
- Participants: Tomas Ortega (alignment and count-placement request); OpenAI
  Codex, GPT-6 (implementation and checks).

## Context and decision

The user requested right-aligned “Dig in deeper” buttons with the number of
child nodes to the right of each button. Keep the neutral controls below
their headings and group each link with its existing count/status label in
a right-aligned row. Update the website guidance accordingly.
This revises the alignment in the
[previous placement decision](2026-11-15-101330-place-neutral-deeper-links-below-titles.md).

## Rationale

Move the existing label into the header row instead of duplicating its content
or adding styling helpers. An initial wrapping flex row put the child count
below the button at 320 pixels. Remove wrapping from the row so text can
reflow within the controls while the count remains on the right.

## Evidence and outcome

- All 188 website tests pass (9,894 assertions); all 50 active pages build.
  Repository lint and whitespace checks pass.
- The initial Firefox check failed on the 320-pixel homepage when the count
  wrapped below its button. After the row adjustment, Firefox 153 and Chromium
  checks pass for every child header on the homepage and Group-Ring Encoding
  at 320, 390, 768, and 1280 pixels. Rows sit directly below headings, align
  right, stay within the viewport, and keep child counts to the right and
  vertically centered beside their links.
- Desktop and phone screenshots were inspected, including text reflow at
  320 pixels. Existing status labels, destinations, and mathematical content
  are preserved. No custom CSS, client script, or dependency was added.

## Report relevance

Records a user-directed navigation layout refinement and its browser checks.
It adds no mathematical result or verification claim.
