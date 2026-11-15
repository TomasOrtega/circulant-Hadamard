# Finalize the cyclic group ring video

- Recorded at: 2026-11-14T23:01:26-08:00
- Observed work interval: 2026-11-14T22:38:54-08:00/2026-11-14T23:01:26-08:00 (revision/verification across brief goal interruptions; intervals overlap other videos).
- Participants: Tomas Ortega (final-video, 3Blue1Brown-style, and subtitle-space requirements); OpenAI Codex, GPT-6 (primary work and delegated caption/visual review).

## Context and decision

Follow the updated [video-production request](2026-11-14-220805-produce-scripted-node-videos.md).
Replace the earlier draft-labelled export with finished ManimGL teaching media:
black background, light mathematical text, recurring blue objects, yellow
focus, and animations explaining relationships. Remove the draft footer;
mathematical assumptions and accepted inputs remain explicit. The original
editorial script is unchanged.

## Rationale

The shared camera reserves the lower 20% (216 pixels at 1080p) for subtitles
without disturbing each scene's coordinate relationships. Narration remains
one complete Achird take; visual revisions reuse it offline. Exact-source
captions now use duration-aware grouping, at most two 42-character lines,
and readable display intervals rather than 0.1-second tail fragments.

Retain the moving position marker, exponent wraparound, reduction example, and
normal-form proof. Remove the former draft footer and leave a clear caption
band without changing the mathematical explanation or recording.

## Evidence and outcome

The [final video](../website/media/cyclic-group-ring.mp4) is 1080p at 30 fps, lasting
120.033333 seconds and covering its 120.000227-second
take. Inspected representative rendered frames. Every one of its
3601 frames was checked in the lower band; maximum
luma was 16 (black). The production record includes
source, scene, layout, narration, and video hashes. Caption tests preserve the
spoken text and verify line length, timing, and overlaps.

Before the framing change, the subtitle-band regression failed against all six
existing exports. After rebuilding, the full local narration/video checks
passed: 20 narration and 23 video tests. All 81 website tests passed and the
production build emitted 20 pages at this verification point. Separate caption
regressions first failed for a flashing word and a long unwrapped line; all six
caption cases now pass. Lint and whitespace checks run before committing.
No independent human listening acceptance of the new take is asserted.

## Report relevance

Records the user's higher production-quality requirement, AI-assisted visual
and caption revision, and direct exported-frame evidence. This changes the
teaching medium, not the mathematical proof or its accepted inputs.
