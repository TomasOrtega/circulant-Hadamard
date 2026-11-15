# Publish informative video thumbnails

- Recorded at: 2026-11-15T09:43:40-08:00.
- Original implementation interval: 2026-11-15T09:11:13-08:00/2026-11-15T09:18:17-08:00
  (424 seconds; known from the observed local creation record).
- Observed publication preparation: 2026-11-15T09:38:20-08:00/2026-11-15T09:43:40-08:00
  (320 seconds through clean-checkout validation).
- Independent staged review: 2026-11-15T09:42:08-08:00/2026-11-15T09:43:03-08:00
  (55 seconds, overlapping preparation).
- Participants: Steven Creech (thumbnail and PR requests); Codex/GPT-6
  (frame selection, implementation, independent review, and publication).

## Context and decision

Address [issue #15](https://github.com/TomasOrtega/circulant-Hadamard/issues/15):
the videos have uninformative previews until playback. Provide a reviewed
thumbnail for each of the 48 published videos and a frame specific to each
of the 37 configured excerpts. Prepare a PR to main on
`steven/video-thumbnails` with `Fixes #15`, so merging resolves the issue.

## Rationale

Extract completed, representative frames from the actual Manim animations,
retaining their black backgrounds, blue/yellow emphasis, and typeset mathematics.
Prefer clear diagrams or concise statements over opening fades or intermediate
calculations. Save 1280-by-720 JPEGs, totaling 3.33 MiB for all 85 assets.

Native players resolve `video.poster` at every node depth. An optional
`segment.poster` overrides the parent poster for a timed excerpt; preserve
the parent fallback. Ten children have no configured cut and remain unchanged.
The build watches and copies both thumbnail directories. No client JavaScript
is added.

The [selection manifest](../videos/thumbnail-selections.json) records frame
times, reasons, source hashes, and excerpt bounds. The documented
[extraction script](../videos/thumbnails.py) regenerates the assets and rejects
changed source videos or choices outside the recorded excerpt bounds.

Fetch main before publication; it remains at `68501c1`. Stage only thumbnails,
their metadata, build/render integration, documentation, and relevant tests.
Separate unrelated local navigation edits in shared files. The user's local
corner-control experiment was reverted and is absent from this PR.

## Evidence and outcome

- Visually reviewed candidate frames for all 48 videos, including extra checks
  to avoid fading diagrams. Every excerpt selection falls within its published
  source cut. Every JPEG decodes at 1280 by 720.
- Original browser review covered the homepage, Node 5, and Gaussian Parity
  at 1440px and 390px: 28 successful poster loads, no overflow or JavaScript
  errors. Evidence remains in `/private/tmp/circulant-thumbnail-browser-qa.json`.
- Independent staged review verifies all 48 video hashes, frame durations,
  37 excerpt parents and bounds, and 85 JPEG dimensions. Parsing the 48 staged
  node documents confirms only poster metadata changed. No MP4, caption,
  narration, or production-script changes are included.
- The exact staged patch applied to a clean checkout of main passes both
  required Make targets: 187 tests, 9,798 assertions, and 50 built pages.
  Its 85 posters match the reviewed local assets byte for byte. Main's existing
  navigation remains intact. Locked website dependencies are reused from the
  working checkout. Repository/scoped lint and staged whitespace checks pass.
- This entry records preparation; commit, push, and PR creation follow.

## Report relevance

Records AI-assisted creation and publication of faithful video previews and
the evidence for a narrowly scoped issue fix. No mathematical claim or video
content changes.
