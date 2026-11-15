# Omit media placeholders and track unfinished previews

- Recorded at: 2026-11-15T11:00:57-08:00
- Observed implementation and validation interval: 2026-11-15T10:54:40-08:00/2026-11-15T11:00:57-08:00 (377 seconds).
- Independent media inventory: 2026-11-15T10:54:44-08:00/2026-11-15T10:56:48-08:00 (124 seconds). Intervals overlap and are not additive person-hours.
- Participants: Tomas Ortega (issue and minimal-change request); OpenAI Codex,
  GPT-6 (implementation and independent inventory agent).

## Context and decision

[Issue #23](https://github.com/TomasOrtega/circulant-Hadamard/issues/23)
requests that missing videos and scripts be tracked in a to-do folder instead
of shown as placeholders. Omit absent media and delete the stale terminal
“video script pending” label. Keep written explanations and real players.
Put the outstanding parent-preview work in
[scripts/to-do/](../website/scripts/to-do/README.md), and update authoring guidance.

All 48 active nodes already have accepted full videos and production scripts,
as established by the [video acceptance record](2026-11-15-072130-accept-all-scripted-node-videos.md)
and checked again here. Retain their canonical source paths and production
records. The ten missing slots concern parent previews: six in Node 2, one in
Node 4, and three in Node 7. Some require additional parent coverage, as the
queue explains with links to the original production decisions.

## Rationale

Returning no media for an unset source removes placeholders without CSS or
client code. Move the existing width limits onto the media figure so an absent
video leaves no empty wrapper. Keep the
[reference excerpt width](2026-11-15-103056-match-reference-excerpt-video-width.md),
[contents and appearance controls](2026-11-15-104739-add-contents-panel-and-dark-mode.md),
and [dependency-panel removal](2026-11-15-104426-remove-uses-panel.md).

Use one to-do table for the ten parent-child gaps rather than moving completed
scripts or inventing preview timings. Tests compare that table with the actual
unset cuts. A future node without an accepted video/script pair needs its own
`<node-id>.md` to-do and an unset video source.

## Evidence and outcome

- Before the fix, regressions failed for an unset overview, unset cut,
  placeholder counts, pending-script text, and the absent to-do queue. All
  184 website tests now pass (9,865 assertions).
- The independent inventory checks 48 canonical script/video pairings,
  all 192 source/scene/SSML/MP4 hashes, captions and thumbnails, durations,
  and the 37 published cuts against production manifests. All match; the ten
  remaining edges have no recorded cuts to copy.
- The website build succeeds. All 98 generated HTML files omit missing-work
  copy; the 48 active pages retain 85 real players, their graphs and controls.
  Node content, media, production files, and page-control scripts are unchanged.
- Chromium and Firefox previews cover four affected/representative pages at
  320, 390, and 1280 pixels (24 layouts). Players fit, retain 16:9 proportions,
  and keep their reference widths. Contents links, dark-mode switching, and
  literal-white corner controls work. Desktop and phone screenshots were inspected.
- Factual correction: the first temporary browser assertion assumed a 16-pixel
  root font. Inspection confirms 16.8 pixels on desktop, giving the unchanged
  840-pixel overview and 735-pixel excerpt caps. The corrected assertion passes.
- Repository lint and whitespace checks pass. Existing video acceptance was
  reused; this task does not re-render videos or finish the queued previews.

## Report relevance

Records a user-directed presentation simplification and a checked queue of
remaining preview work. It adds no mathematical result or proof verification.
