# Finalize Form the Combination

- Recorded at: 2026-11-15T06:34:18-08:00.
- Observed production span:
  2026-11-15T06:19:30-08:00/2026-11-15T06:34:18-08:00 (888 seconds,
  including root production, waiting, and the previously noted interruption).
- Observed author export-review interval:
  2026-11-15T06:31:48-08:00/2026-11-15T06:34:18-08:00 (150 seconds,
  including the prose correction and rerender). These intervals overlap.
- Participants: Tomas Ortega (continuing final-video request); Steven Creech
  (editorial source); OpenAI Codex, GPT-6 (child narration, scene, exact
  arithmetic checks, and author review; root synthesis/alignment, preflight,
  rendering, independent review, and full-frame caption-band scan).

## Context and decision

Accept the final [Form the Combination video](../website/media/form-sign-combination.mp4)
after the [preparation and source checks](2026-11-15-063045-prepare-form-sign-combination-video.md).
Keep the editorial script, one complete Achird recording, and measured
timings unchanged. The only post-export scene revision replaces an inaccurate
Unicode coefficient label with ordinary prose.

## Rationale and correction

The first export's prose used `hₐ,ᵦ`: its final character is Greek subscript
beta, not the Latin b in the correctly typeset formula above it. Root and
author observed this at 12 seconds. At 2026-11-15T06:32:20-08:00, replace
only that prose with “The same original signs define c, d, and g.” Root
explicitly classified this as a prose correction, requiring no mirrored
string test. Reuse the complete narration and all cues; no extra synthesis.
Both root and author accepted the corrected actual 12-second frame.

The mathematical sequence remains exact: retain the same signs in all
normalized evaluations, cancel in d−c, multiply the second difference by
(1−i)/2, collect the numerator over four, establish integer half-sums, and
then add the quotients. The two negative H-three halves become −H-three;
the remaining half-sum acquires i−1. Both divisibilities remain explicit,
and reduction is deferred. The coefficient argument applies to every
positive u without norm identities or oddness assumptions.

## Evidence and outcome

- One frozen 2,553-byte, 450-word SSML take lasts **170.860227 seconds**.
  Three measured paragraph cues and **22** unique exact-source internal cues
  drive the scene. ASR match is 0.882. Strict final preflight reports
  **170.86 seconds** and **no late events**.
- All **16** sign columns satisfy the normalized evaluations, exact
  quotients, numerator-over-four expansion, collected E identity, and both
  divisibilities. The reciprocal calculation reconstructs **625** Gaussian
  values with real/imaginary parts −12 through 12. These finite checks
  support the displayed general algebra; they are not formal verification.
- Reviewed the 12 actual resting frames at 12/33/40/54/66/75/90/109/130/142/
  153/169 seconds. Also extracted and inspected intermediate frames at
  45/68.7/71/98.7/100.1/117.3/119 for cancellation, reciprocal multiplication,
  completed integer halves, and H-three copy/highlight cleanup. The corrected
  final 12-second frame is `videos/build/form-sign-combination-corrected-12.png`.
  No mathematical, overlap, cleanup, or caption-space blocker remains.
- Final MP4: **6,509,374 bytes**, **170.866667 seconds**, H.264 1920×1080
  at 30 fps; AAC lasts **170.860998 seconds**. Root's final scan checks
  **all 5,126 frames**, lower 20% maximum limited-range luma **16**.
  No draft footer appears.
- All **39** VTT cues reproduce the frozen narration exactly, with at most
  two lines and 42 characters per line, minimum duration **1.54 seconds**,
  no overlaps, and bounded times. No human listening acceptance is claimed.
- Editorial, SSML, scene, shared-layout, and media hashes match the final
  production manifest. Python compilation, Ruff, formatting, and scoped
  whitespace checks pass. Root owns full repository checks, website
  attachment, and the separate commit/push.

## Report relevance

Records final production of an existing coefficient-algebra proof, exact
finite illustrations, a small actual-export prose correction, measured
narration, and observed media/caption limits. No new theorem or formal
proof claim is introduced.

## Final repository validation

Recorded at 2026-11-15T06:35:41-08:00. Root independent source and native-export review
accepts the final candidate. Repository checks pass: 20 narration tests,
38 video tests, 183 website tests with 9,220 assertions, and a 50-page
website build. Each video has its own staged lint check, commit and push.
