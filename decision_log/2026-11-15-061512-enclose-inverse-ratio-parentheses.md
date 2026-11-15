# Enclose the inverse ratio parentheses

- Recorded at: 2026-11-15T06:15:12-08:00.
- Observed export-review and correction interval:
  2026-11-15T06:12:27-08:00/2026-11-15T06:15:12-08:00 (165 seconds,
  including regression execution and waiting).
- Participants: OpenAI Codex, GPT-6 (author export review and root validation).

## Context and decision

The first actual Integrality export exposed a second extent of the
[ratio-enclosure issue](2026-11-15-060718-enclose-complete-local-ratios.md):
the corrected right highlight enclosed its fraction bar, but crossed the
outer inverse parentheses. Include both enclosing parentheses and the
negative-one exponent in the same actual bounding group. Keep the product
dot outside the highlight. Reuse the frozen narration, cue times, and all
other scene content.

## Rationale

The highlighted object is an invertible ratio, including its displayed
inverse power. Bounding the complete expression avoids crossing notation
whose role is mathematically significant.

## Evidence and outcome

- Extracted and inspected 17 native frames from the exported MP4 at
  28, 35, 40, 59, 65, 79, 96, 106, 112, 130, 133, 140, 149, 154, 166.5,
  174, and 179 seconds. Frame 59 shows the intersecting parentheses.
  The remaining proof states have no observed mathematical or layout blocker.
- Extended the existing actual-scene regression before changing the source,
  using the actual inverse notation and highlight bounds. Root confirmed two
  failures in 0.877 seconds: horizontal gaps −0.2858814073 and −0.8787439537.
  Log: `videos/build/integral-delta-enclosure-red.log`.
- Apply only the expanded right bounding group. Python compilation, Ruff,
  and formatting pass. Root will rerun the regression and strict preflight,
  render again, and inspect the corrected state before final acceptance.
- The first export's 42 caption cues exactly match the SSML; at most two
  lines and 42 characters, minimum 2 seconds, no overlap, and bounded times.
  Root's first-export scan checked all 5,429 frames: lower 20% maximum luma
  16. The revised export still needs its own final scan and hashes.

## Report relevance

Records a visual defect found by actual-export review, the reproduced
failure, and a minimal correction that retains the accepted narration.
