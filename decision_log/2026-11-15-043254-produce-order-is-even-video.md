# Produce the even-order video

- Recorded at: 2026-11-15T04:32:54-08:00
- Observed work interval: 2026-11-15T04:04:10-08:00/2026-11-15T04:32:54-08:00
  (1,724 seconds, including synthesis, render, and regression-check waits).
- Participants: Tomas Ortega (standing final-video request); Steven Creech
  (editorial script); OpenAI Codex, GPT-6 (scene, narration adaptation,
  mathematical checks, regression, and export review); Google Chirp 3 HD
  Achird (one complete narration take); local faster-whisper (alignment).

## Context and decision

Produce final Video 2.2 from the unchanged
[three-slide editorial script](../website/scripts/node2/order-is-even.md),
developed in the [refined-node work](2026-11-15-031448-develop-node-two-and-three-refined-proofs-and-scripts.md).
Add the [scene](../videos/order_is_even.py), frozen
[SSML](../videos/scripts/order-is-even.ssml), final
[MP4](../website/media/order-is-even.mp4), exact-source
[captions](../website/media/order-is-even.vtt), and measured
[production metadata](../videos/production/order-is-even.json).
Update only the leaf node's video fields; preserve its foundation and
mathematical draft metadata. Parent cuts are coordinated separately.

## Rationale

Use the known order-four rows, not an invented higher-order candidate.
Copy each vertical coordinate pair into its product, separate positive and
negative contributions, pair them, and collapse each pair to zero. Generalize
with the counts a and b: orthogonality gives a−b=0, the number of positions
gives a+b=n, and a=b yields n=2a. For the circulant case, combine this with
the preceding node's square restriction. An odd m would have odd square;
therefore m is even, and m=2u gives n=4u². The final display explicitly
leaves oddness of the same positive integer u as the next goal.

The complete 1,945-byte SSML uses one default Achird synthesis request.
Seven section cues and 34 internal cues follow measured source-word times,
with phrase/index provenance retained. Visual changes reuse that take.

## Evidence and outcome

- Checked the actual four coordinate products and their zero sum. Bounded
  arithmetic checks cover positive/negative counts for n=2 through 17,
  the odd-square expansion for r=−50 through 50, and (2u)²=4u² for u=1
  through 100. These illustrate the elementary general arguments; no new
  research result or formal verification is claimed.
- Inspected 12 actual initial-export states across the seven sections.
  This found the multiplication sign overlapping the second-row label at
  36.46 seconds. Move only that sign left by one scene unit. The focused
  [regression](../videos/test_order_is_even.py) constructs the production
  scene and captures the actual displayed Tex objects rather than copying
  their layout coordinates into a separate model.
- The child environment could not create a graphics adapter, so its first
  attempted regression run stopped before the assertion. Root then restored
  the old placement temporarily: the test failed with bounding-box gap
  −0.129529. Restoring the corrected placement passed; both measured test
  runs took 0.624 seconds. Evidence is retained in
  `videos/build/order-is-even-layout-red-root.log` and
  `videos/build/order-is-even-layout-green-root.log`. The final native-size
  36.46-second frame visibly separates the sign and label. The regression
  and source fix are included together.
- Independently probed the corrected H.264 export: 1920 by 1080 at 30 fps,
  3,860 frames, 128.666667 seconds. AAC lasts 128.660998 seconds and covers
  the full 128.660227-second take. Its extracted AAC is byte-identical to
  the first export, with SHA-256
  `37db5f8a6db7938017f074a9e385be71143f1fafbd0811a1dabfbe6c0bd77708`.
- Editorial, SSML, video, scene, and shared-layout hashes are recorded and
  match current files. Root's final all-frame scan records maximum luma 16
  in the lower 20% across all 3,860 frames; sampled visual review is separate
  evidence. The measured timing preflight reports no late events.
- Captions exactly preserve normalized SSML text: 31 cues, at most two
  42-character lines, minimum 1.62 seconds, no overlaps, final end 127.34
  seconds. ASR supports timing and wording review, not independent human
  listening acceptance. Scoped Ruff and whitespace checks pass; root runs
  the final shared suite and commits this video separately.

## Report relevance

Records production of the supplied parity proof, a visual defect discovered
in exported frames, a demonstrated regression failure and fix, and evidence
that the corrected export retains the single complete narration take.

## Final integration validation

Observed at 2026-11-15T04:42:07-08:00: all 20 narration and 32 video tests pass, including both actual-scene layout regressions and the three compiler regressions. All 183 website tests pass (9,076 assertions); the 50-page build and native player/caption links are current. Ruff, formatting, and whitespace checks pass. All 18 final editorial, narration, scene, layout, and media hashes match their production records. Root publishes each video separately; no further narration request was needed for visual corrections.
