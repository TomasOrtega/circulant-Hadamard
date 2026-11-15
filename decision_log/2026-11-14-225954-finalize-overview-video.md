# Finalize the overview video

- Recorded at: 2026-11-14T22:59:54-08:00
- Observed work interval: 2026-11-14T22:38:54-08:00/2026-11-14T22:59:54-08:00 (revision/verification across brief goal interruptions; intervals overlap other videos).
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

The eight-node proof graph retains the dependency arrows and highlights one
component at a time. Cyclic row copies are cleaned up after each transformation.
The newly merged hierarchy allows eight real parent previews, from the
Group-Ring Encoding cue through the final contradiction; attach those measured
cuts to the homepage instead of leaving empty slots.

Merged [Steven's PR #8](https://github.com/TomasOrtega/circulant-Hadamard/pull/8)
at 2026-11-14T22:52:03-08:00 after all lint, website, and TeX checks passed for
head 42be51e054ecbb76cd4dd168e4fd75db3b520372. Merge commit:
0585776be100ea9c8b9ab3c1cb769d114e412657. It adds the Three Evaluations script
and the unified main map. Preserve the ongoing local video work while
fast-forwarding, and add that new scripted node to the production queue.
The user's subsequent report about the opening route buttons is being fixed
separately; this record does not claim that repair complete.

## Evidence and outcome

The [final video](../website/media/overview.mp4) is 1080p at 30 fps, lasting
214.933333 seconds and covering its 214.920227-second
take. Inspected representative rendered frames. Every one of its
6448 frames was checked in the lower band; maximum
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
