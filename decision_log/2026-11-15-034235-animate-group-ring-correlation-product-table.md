# Animate the correlation product table

- Recorded at: 2026-11-15T03:42:35-08:00
- Observed work interval: 2026-11-15T03:17:35-08:00/2026-11-15T03:42:35-08:00
  (1,500 seconds, including the render queue and overlapping Node 5 review).
- Participants: Tomas Ortega (standing final-video request); Steven Creech
  (merged editorial animation cue); OpenAI Codex, GPT-6 (scene revision,
  arithmetic, timing, export, and frame review).

## Context and decision

Implement the optional four-by-four product-table cue in the current
[Node 1 editorial source](../website/scripts/node1/group-ring-encoding.md).
Revise only the correlation section of the
[scene](../videos/group_ring_encoding.py), replacing four separate dot-product
equations with a table whose entry in row a, column j is h_j h_(j−a), with
indices modulo four. Row sums become the coefficients of h times h star.
This extends the [previous final video](2026-11-14-230124-finalize-group-ring-encoding-video.md)
without changing the [sign-hypothesis clarification](2026-11-14-175124-clarify-sign-hypothesis-in-dictionary-converse.md).

Reuse the existing complete Achird recording, frozen SSML, measured cues,
duration, and five child-preview ranges. The narration already describes the
four correlations; the new editorial cue requires a visual revision only.
Refresh the current editorial, scene, layout, and export hashes in the
[production metadata](../videos/production/group-ring-encoding.json).

## Rationale

The table makes the four individual coefficient products visible before their
sum is identified with a polynomial coefficient. Focus the constant row at
109.46 seconds and its sum at 112.40. During the X-coefficient narration,
reveal its four entries at measured word times 115.30, 116.38, 117.40, and
118.52, then its zero sum at 119.10. Focus the remaining rows at 120.66 and
122.00. The animation finishes by 123.20, before the unchanged product cue
at 124.41. Keep the constant result bright and dim the three zero results.
The table introduces no double-sum expansion. All other scene sections remain
unchanged.

## Evidence and outcome

- Direct integer arithmetic checked all 16 entries for the fixed example
  h=(-1,1,1,1), with a and j ranging from zero through three. The rows are
  (1,1,1,1), (−1,−1,1,1), (−1,1,−1,1), and (−1,1,1,−1), with sums
  4,0,0,0. This checks the illustration, not a new general theorem.
- Independently inspected actual exported frames at 10, 108, 113, 116,
  119.8, 123.3, 154, 160, 167, and 188 seconds. The table, row focus, sums,
  later dictionary, completed arbitrary-row converse, and h=2 sign
  counterexample are legible and correctly separated. The 160-second frame
  samples the existing formula transformation; 167 shows its completed result.
- Independently probed the revised H.264 video: 1920 by 1080 at 30 fps,
  6,017 frames, 200.566667 seconds. The AAC stream lasts 200.560998 seconds,
  covering the complete 200.560227-second WAV. Extracted AAC is byte-identical
  to the prior committed export (SHA-256
  `5999c9af4bf69d2e4afebae7a688c043e363fb6081c44d7b386e81ca18ddc94c`).
  SSML is also byte-identical to HEAD; no synthesis request was made.
- Current editorial, narration, and video hashes match the manifest. Root's
  full-frame subtitle-band scan records maximum luma 16 in the lower 20%
  across all 6,017 frames. This automated evidence is separate from the
  independent sampled-frame review.
- Caption text matches normalized SSML exactly: 47 cues, at most two lines,
  at most 42 characters per line, minimum 1.46 seconds, no overlaps, final
  end 199.40 seconds. All five parent-preview ranges remain unchanged.
  Scoped Ruff and whitespace checks pass; root runs the final shared suite
  before committing this video separately. No new human listening acceptance
  is asserted for the reused take.

## Report relevance

Records a merged editorial cue becoming a mathematical animation, with
bounded arithmetic checks, direct exported-frame review, and byte-level
evidence that the existing approved narration was reused.

## Final integration validation

Observed at 2026-11-15T03:57:10-08:00: all 20 narration and 30 video tests pass, without resource warnings; all 147 website tests pass (8,570 assertions), and the build emits 50 pages. All six new or revised scenes pass strict-compiler preflight without late animation cues. Ruff and whitespace checks pass. Current editorial, narration, scene, layout, and video hashes match all 14 final production records. Root publishes each video in its own commit.
