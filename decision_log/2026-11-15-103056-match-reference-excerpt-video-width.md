# Match the reference site's inline video width

- Recorded at: 2026-11-15T10:30:56-08:00
- Observed work interval: 2026-11-15T10:26:08-08:00/2026-11-15T10:30:56-08:00 (288 seconds).
- Participants: Tomas Ortega (issue and sequential commit/push request);
  OpenAI Codex, GPT-6 (reference inspection, implementation, and checks).

## Context and decision

[Issue #20](https://github.com/TomasOrtega/circulant-Hadamard/issues/20)
requests wider excerpt videos matching non-main videos in 3Blue1Brown's
interactive lessons. Change the shared excerpt wrapper's maximum width from
125 to 175 spacing units. Keep the responsive full width and centered placement.
This extends the [full-width child-section layout](2026-11-15-001404-restore-single-proof-map-and-widen-node-sections.md).

## Rationale

The live [Fourier Transform lesson](https://www.3blue1brown.com/lessons/fourier-transforms/)
has 735-pixel inline videos at a 1280-pixel viewport. Browser inspection in
Firefox and Chromium confirms this matches its 175-unit reading column at
a 16.8-pixel root font size. The unchanged vendored stylesheet defines that
column width. Reuse the same existing width scale instead of adding CSS or
making excerpts arbitrarily fill the wider project sections.

## Evidence and outcome

- Before the fix, the browser regression fails on the homepage's Group-Ring
  Encoding excerpt: 525 pixels wide instead of the reference's 735.
- After the one-class change, Firefox 153 and Chromium checks cover all 37
  published excerpt players across their parent pages at 320, 390, 768, and
  1280 pixels. Each matches the reference width or the available content width,
  fits the viewport, and retains its 16:9 aspect ratio. Checked overview
  players retain their 840-pixel desktop width. Desktop and phone screenshots
  were inspected. Reference media downloads were blocked for layout measurement;
  no playback comparison with the reference site is claimed.
- All 181 website tests pass (9,622 assertions), and all 48 active pages build.
  Repository lint and whitespace checks pass. Video files, captions, posters,
  timings, and overview styling are unchanged; no dependency or client code
  is added.

## Report relevance

Records a reference-measured presentation correction. It changes the display
size of existing videos and adds no mathematical claim.
