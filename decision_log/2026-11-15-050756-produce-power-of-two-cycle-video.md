# Produce the power-of-two projection video

- Recorded at: 2026-11-15T05:07:56-08:00
- Observed work interval: 2026-11-15T04:56:47-08:00/2026-11-15T05:07:56-08:00 (overlaps the other three Node 2 productions; not additive person-hours).
- Participants: Tomas Ortega (standing request); Steven Creech (editorial source); OpenAI Codex, GPT-6 (scene, integration, and independent review); Google Chirp 3 HD Achird (one take); local faster-whisper Base English (supporting alignment).
- Independent review: 2026-11-15T05:06:27-08:00/2026-11-15T05:06:38-08:00.

## Context and decision

Continue the [refined-script production](2026-11-15-040551-merge-refined-scripts-and-start-child-videos.md) with [Video 2.3](../website/scripts/node2/power-of-two-cycle.md). Preserve the source Markdown and publish its own finished ManimGL overview, exact captions, production record, and separate commit/push. Keep the original parameter u: u = 2^(s−1) w, with w odd and s at least one.

## Rationale

Animate the order factorization, then send 36 symbolic coefficients from their original order into four residue buckets. Each bucket contains nine positions; no hypothetical Hadamard signs are invented. Show the general coefficient sum and its parity before carrying multiplication, inverse, star, and the unchanged scalar norm through the quotient map. A labeled schematic prepares antipodal pairs for the later descent; s = 1 and odd u remain its future goal here.

## Evidence and outcome

- One 2,322-byte default Achird SSML take lasts 156.480227 seconds. Six paragraph cues and 18 exact-source internal cues pass strict-compiler preflight with no late events. Local transcription supports wording/timing (alignment ratio 0.897); it does not establish human listening acceptance.
- Actual MP4 frames revealed touching summation limits. A focused actual-scene geometry regression first failed with a −0.170926-unit gap, then passed after separating and resizing the sums. The corrected render reuses the same SSML and recording.
- Final H.264/AAC media is 1920 by 1080 at 30 fps, 156.5 seconds, 5,182,136 bytes. Audio lasts 156.480998 seconds. Every one of 4,695 decoded frames retains a black bottom 20 percent (maximum limited-range luma 16).
- All 36 captions exactly preserve semantic source text, with at most two 42-character lines, ordered nonoverlapping bounded times, and minimum display 1.88 seconds. Editorial, narration, scene, layout, and media hashes match.
- Primary and independent review checked the coefficient motion, bucket indices, corrected sums, ring map, scalar norm, and conditional descent handoff in fresh native frames. Apparent missing glyphs in a large preview were absent from native title crops; no renderer settings changed.
- Bounded checks verify the four nine-position buckets partition 0 through 35, all 512 nine-sign sums are odd, and 11,760 basis-product pairs respect projection; reversal was also checked for s = 1 through 3 and w = 1, 3, 5. These illustrate the general elementary proof, not the full Hadamard theorem.
- Full repository checks follow before publication. No open pull requests were observed during this batch's checks.

## Report relevance

Records a complete child-node video, measured chronology and export quality, symbolic example scope, independent review, and a failing-first visual correction. The inherited proof status remains in node metadata while the video itself is final.

## Final integration validation

Observed at 2026-11-15T05:17:07-08:00: all 20 narration and 33 video tests pass. All 183 website tests pass (9,112 assertions), and the build emits 50 pages with the new native players and captions. Editorial, narration, scene, layout, and media hashes match the accepted exports. Each scene passes strict timing/TeX preflight without late events. All-frame subtitle audits remain black. Root publishes each video in its own conventional commit and push.
