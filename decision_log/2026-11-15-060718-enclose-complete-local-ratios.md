# Enclose complete local ratios

- Recorded at: 2026-11-15T06:07:18-08:00.
- Observed surrounding work checkpoints:
  2026-11-15T06:02:46-08:00/2026-11-15T06:07:18-08:00 (272 seconds,
  including waiting for the root-run regression). The precise regression
  authoring start was not measured.
- Participants: OpenAI Codex, GPT-6 (child authoring and root validation).

## Context and decision

During source review after the
[Integrality preparation](2026-11-15-060246-prepare-integral-delta-video.md),
the author noticed that the ratio highlights enclosed only the evaluation
labels, whereas their fraction bars were wider. Add the actual corresponding
bar to each highlight's bounding group. This changes two expressions and
reuses all frozen narration and measured timings.

## Rationale

The focus rectangle should enclose the complete ratio, including its fraction
bar. A border crossing the bar would suggest an unintended partition of the
expression. Capturing real production objects gives a regression independent
of copied layout coordinates.

## Evidence and outcome

- Added [an actual-scene regression](../videos/test_integral_delta.py) before
  changing the scene. It captures the first two ratio highlights at the
  public `show` seam and checks at least 0.1-unit containment on both sides
  of each actual fraction bar.
- Root confirmed four failures in 4.467 seconds before the fix. The bar
  extended beyond the original highlights by approximately 1.16 and 1.22
  units on each respective ratio's sides.
- Include the left and right fraction bars in the two existing
  `SurroundingRectangle` bounds. Python compilation, Ruff, formatting, and
  scoped whitespace checks pass. Root's GREEN run, strict preflight, final
  export, and actual-frame acceptance are pending.

## Report relevance

Records a reproduced source-layout defect corrected before the first export,
with a failing-first test of the actual scene and no additional narration.
