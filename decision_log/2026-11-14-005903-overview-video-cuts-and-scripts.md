# Use overview cuts and corresponding script excerpts

- Recorded at: 2026-11-14T00:59:03-08:00
- Observed work interval: 2026-11-14T00:33:38-08:00/2026-11-14T00:59:03-08:00
- Participants: user (video model clarification); Codex (implementation and checks).

## Context and decision

The user clarified that each node should own a long overview video, with its
children previewed through cuts of that video. Opening a child shows its own
separate, deeper overview.

Store each cut's start/end seconds and corresponding written script excerpt
on the parent-child link. Render that script as the preview's text; use the
node's own script for its detailed written explanation. Text is a readable
adaptation of the narration rather than a required verbatim transcript.

This replaces the independently configured video/clip fields in the
[earlier renderer](2026-11-14-002050-prerender-lessons-with-react.md).

## Rationale

One source per node avoids duplicating uploads and keeps cuts tied to the
overview they explain. Unknown sources and timings remain empty slots.
The supplied narration outlines remain drafts.

YouTube cuts use its documented
[start/end parameters](https://developers.google.com/youtube/player_parameters).
Native files use media fragments and the small
[cut controller](../website/video-player.js) to bound playback and seeking
and restart a completed cut.

## Evidence and outcome

All 21 tests and the clean build passed. Tests distinguish the parent cut from
the child's own overview, check script placement, reject invalid ranges,
and confirm an untimed preview never plays the entire overview.

Native playback logic was checked with simulated media events for metadata,
seeking, end bounds, replay, and listener cleanup. No actual recordings were
supplied, and decoded-video playback could not be checked in a browser.
The build emits the cut player; navigation itself needs no client script.

## Report relevance

This is an AI-assisted presentation and media-authoring change. Recording
timings were not invented. This interval overlaps the other node work and
spans the interrupted and resumed task; it is not a measure of person-hours.
