# Produce the Four Sign Polynomials video

- Recorded at: 2026-11-15T05:41:28-08:00
- Observed work interval: 2026-11-15T05:23:59-08:00/2026-11-15T05:41:28-08:00 (overlaps the other Node 3 productions; not additive person-hours).
- Participants: Tomas Ortega (standing video request); Steven Creech (editorial source); OpenAI Codex, GPT-6 (primary production and independent review); Google Chirp 3 HD Achird (one complete take); local faster-whisper Base English (supporting alignment).
- Independent review: 2026-11-15T05:33:07-08:00/2026-11-15T05:36:20-08:00 (193 seconds, including rerender waiting and overlapping parity-video work).

## Context and decision

Continue the [refined-script production](2026-11-15-040551-merge-refined-scripts-and-start-child-videos.md) with [Video 3.2](../website/scripts/node3/four-sign-polynomials.md). Preserve its Markdown and the parent overview/cuts. Publish a separate final ManimGL scene, recording, captions, and node player, with its own commit/push.

## Rationale

Move eight representative coefficient/Z/P terms into four groups without separating their coefficient and P power. Label this illustration u greater than one and keep omitted P powers explicit. Collapse the groups into named H-polynomials while retaining their common Z factors, then copy them into the full decomposition.

Explain uniqueness through the integer group-ring basis and re-expand H_2 using its exact finite sum. The initial endpoint/ellipsis expansion would duplicate terms at u = 1; replace it with the finite sum before publication so this general step also covers that boundary. The same recording and measured cues remain valid.

Use 36 symbolic coefficient positions for the u = 3 illustration, selecting the four signs at P^4. No hypothetical Hadamard values are assigned. End with separate evaluation/norm and parity/integrality arrows: the two checks have distinct logical roles before normalization.

## Evidence and outcome

- One 2,226-byte default Achird SSML take lasts 150.880227 seconds. Six paragraph cues and fourteen exact-source internal cues pass strict timing/TeX preflight with no late events. Local transcription supports alignment (ratio 0.9859), without establishing human listening acceptance.
- Final H.264/AAC MP4 is 1920 by 1080 at 30 fps, 150.9 seconds, 5,419,781 bytes; AAC lasts 150.880998 seconds. All 4,527 decoded frames retain a black lower 20 percent, maximum limited-range luma 16.
- All 37 captions exactly preserve semantic source text, fit at most two 42-character lines, and have ordered nonoverlapping bounded times; minimum display 1.68 seconds. Editorial, SSML, scene, layout, and video hashes match.
- Primary and independent native-frame review checks attached factors, all four groups, decomposition, exact bounded re-expansion, hypothetical 36-position grid, selected column, and independent handoff. No clipping, overlapping labels, visible ghosts, or draft footer remains. Native crops resolve unreliable large-preview glyph omissions without changing renderer settings.
- Bounded bookkeeping checks cover 660 distinct basis positions across u = 1, 3, 5, 7, 9. Regrouping preserves every synthetic sign coefficient and the four selected order-36 indices. Synthetic signs appear only in the ignored check, never as a claimed Hadamard construction. This illustrates the general basis argument; it is not formal verification of the full theorem.
- Ruff, formatting, and scoped whitespace checks pass. Combined repository checks follow before the separate publication commit. No open pull requests were observed during this batch.

## Report relevance

Records a finished foundational grouping video, actual production/review intervals, preservation of coefficients and proof scope, the u = 1 display refinement, and measured media/caption quality.

## Final integration validation

Observed at 2026-11-15T05:50:53-08:00: all 20 narration tests pass in 0.216 seconds and all 36 video tests pass in 24.997 seconds, including both actual-scene parity layout/cleanup regressions. All 183 website tests pass (9,148 assertions) and the build emits 50 pages with native video/caption links. Accepted exports match their editorial, SSML, scene, layout, and media hashes; strict timing preflights have no late events. Ruff, formatting, and whitespace checks pass. Root publishes each video in its own conventional commit and push.
