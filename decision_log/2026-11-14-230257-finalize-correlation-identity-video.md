# Finalize the correlation identity video

- Recorded at: 2026-11-14T23:02:57-08:00
- Observed work interval: 2026-11-14T22:38:54-08:00/2026-11-14T23:02:57-08:00 (revision/verification across brief goal interruptions; intervals overlap other videos).
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

Expand pairwise products into a four-by-four grid and color terms by exponent.
Copy the four selected cells into their collected coefficient sum, then identify
the general coefficient with a cyclic dot product. Verify the example gives
coefficients (4,0,0,0), while the formula also applies to integer coefficients.
The earlier finite check of126 sign rows (lengths1–6) and arbitrary row pairs
supports these numerical illustrations.

A first full take incorrectly said that only sign coefficients could give
constant correlation n. The supplied h=2 example at n=4 disproves that wording.
Correct the narration to the sufficient statement, “For sign coefficients, the
constant correlation is n,” and regenerate the whole SSML take. The earlier
recording/script remain only in ignored diagnostic storage; the published
122.880227-second take contains the correction. No fragments were synthesized
or stitched. This is a factual correction during production, before publishing
this node's video.

## Evidence and outcome

The [final video](../website/media/correlation-identity.mp4) is 1080p at 30 fps, lasting
122.900000 seconds and covering its 122.880227-second
take. Inspected representative rendered frames. Every one of its
3687 frames was checked in the lower band; maximum
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
