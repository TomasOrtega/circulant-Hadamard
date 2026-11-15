# Finalize the Parity of Sign Columns video

- Recorded at: 2026-11-15T05:49:38-08:00
- Observed work interval: 2026-11-15T05:48:01-08:00/2026-11-15T05:49:38-08:00 (final combined-export review, file verification, and metadata completion; earlier preparation and corrections have separate measured records).
- Participants: Tomas Ortega (finished-video and subtitle-space requirements); Steven Creech (editorial source); OpenAI Codex, GPT-6 (root rendering, test execution and subtitle audit; delegated scene authoring, regression fixes and final visual verification).

## Context and decision

Complete the [production preparation](2026-11-15-053146-prepare-halve-sign-sums-video.md),
[highlight-spacing revision](2026-11-15-053722-clear-sign-column-highlights.md),
and [pair-frame/scope correction](2026-11-15-054353-remove-completed-sign-pair-frames.md).
Accept the combined offline [Video 3.4 export](../website/media/halve-sign-sums.mp4)
with the original complete Achird take and exact-source captions.

## Rationale

The final opening selection boxes clear both neighboring terms. Pair-selection
rectangles fade as the residue sums become single zeros, leaving no obsolete
border across the results. The closing coefficient range is the exact bounded
set of powers, including the single-position u=1 case. The video still uses
only common signs to justify integer and Gaussian-integer half-coefficients;
it neither invokes a norm identity nor constructs a Hadamard row.

## Evidence and outcome

Reviewed fresh final-export frames at 31, 56, 68, 90.2, 109, and
126 seconds. The four selected coefficients stay attached to the same P^b
position. The modulo-two zeros, two real integer halves, separate Gaussian
half-differences, complete Gaussian coefficient, numerical column, and final
polynomial integrality statements are readable. The column (−1,1,1,−1)
gives 0,0,−1+i with its coefficient-only explanation visible. No clipping,
overlapping glyphs, surviving pair-frame ghosts, or draft label remains.

Both actual-scene regressions pass in root's final green check: two tests
in 0.737 seconds. Their preceding observed failures and focused fixes are
preserved in the linked records. Strict timing preflight reports 127.44
seconds and no late cues. Root's terminal subtitle-band audit checked all
3,824 frames in the lower 20 percent, with maximum encoded luma 16, black.

The H.264 export is 1920 by 1080 at 30 fps, lasting 127.466667 seconds;
its AAC stream lasts 127.440998 seconds and covers the 127.440227-second
take. All 28 VTT cues still match the semantic SSML source, with at most
two 42-character lines, no overlaps, and a minimum display time of two
seconds. Editorial, narration, and final-video hashes match. Current scene
and shared-layout hashes are now recorded in the
[final production manifest](../videos/production/halve-sign-sums.json).
The exhaustive 16-column parity check from preparation applies unchanged.

Root owns combined batch checks, website attachment, and the separate
publication commit. This record does not claim their unobserved global
results or independent human listening acceptance. The earlier superseded
exports are not the artifacts accepted by this record.

## Report relevance

Records final observed media quality and measurable subtitle clearance,
including two defects caught in actual frames and corrected with regressions.
The mathematical coefficient argument and its single narration remain intact.

## Final integration validation

Observed at 2026-11-15T05:50:53-08:00: all 20 narration tests pass in 0.216 seconds and all 36 video tests pass in 24.997 seconds, including both actual-scene parity layout/cleanup regressions. All 183 website tests pass (9,148 assertions) and the build emits 50 pages with native video/caption links. Accepted exports match their editorial, SSML, scene, layout, and media hashes; strict timing preflights have no late events. Ruff, formatting, and whitespace checks pass. Root publishes each video in its own conventional commit and push.
