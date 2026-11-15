# Produce the local character comparison video

- Recorded at: 2026-11-15T06:20:49-08:00
- Observed work interval: 2026-11-15T05:55:02-08:00/2026-11-15T06:20:49-08:00
  (1,547 seconds, including synthesis/render waits;
  overlaps other videos).
- Participants: Tomas Ortega (standing final-video request); Steven Creech
  (editorial script); OpenAI Codex, GPT-6 (narration adaptation, scene,
  timing, independent semantic review, and exported-frame review); Google
  Chirp 3 HD Achird (one complete take); local faster-whisper Base English
  (alignment).

## Context and decision

Produce final Video 4.3 from the unchanged
[six-slide script](../website/scripts/node4/local-character-comparison.md),
following the [refined exposition decision](2026-11-15-031809-develop-all-refined-node-exposition-and-scripts.md).
Add the [scene](../videos/local_character_comparison.py), frozen
[SSML](../videos/scripts/local-character-comparison.ssml), measured
[production metadata](../videos/production/local-character-comparison.json),
and [actual-scene typography regression](../videos/test_local_character_comparison.py).
Root owns synthesis, GPU rendering, the [MP4](../website/media/local-character-comparison.mp4),
[captions](../website/media/local-character-comparison.vtt), website integration,
shared checks, and separate commit/push. No editorial source, parent metadata,
shared helper, or mathematical draft status changes in this delegated work.

## Rationale

Label the unramified coefficient ring and cyclotomic basis/divisibility
facts as supplied Lemma 2.1 input. Separate nonzero values from possibly zero
residues before attempting division. In the exponent-one case, distribute
one p-factor between the two value boxes, select a unit denominator, then
obtain the other ratio by inversion.

Allow fractional extended valuations in the higher-exponent step. Use their
sum to select a factor with valuation at least one; polynomial division
isolates a remainder whose coefficients inherit p-divisibility by the supplied
input. Project the p cyclotomic terms to p ones. Divide exactly one projected
factor by p in the free A-module before any residue reduction.

Keep both ratio cards fixed while the cycle and scalar exponents decrease
together. Either factor may be divided at later stages; stop at exponent one.
In the norm application, identify e as the exponent of p in u squared and
b = u squared divided by p to the e as a unit. Attach the residue-one unit
conclusion to the neighboring-character ratio and its inverse at every prime
above p, without claiming that the individual character values are units.
No higher-order Hadamard coefficient example is invented.

The 3,885-byte SSML fits one default Achird request. Ten paragraph cues and
38 internal cues use measured exact-source words with phrase/index provenance.
Copied targets enter the body before their animations, and faded transients
are removed. The inherited framing reserves the bottom 20% without a footer.

## Evidence and outcome

- All 55 static and seven dynamic formula strings compile through the strict
  CPU TeX path. Scoped Ruff and formatting checks pass. Root's complete
  corrected-scene preflight lasts 279.14 seconds and has zero late events.
- A bounded integer check confirms the p cyclotomic terms project to p ones
  for p = 2, 3, 5, 7, 11 and e = 2 through 5 (20 cases). This illustrates
  the displayed polynomial projection; it does not prove the supplied local
  cyclotomic input or constitute formal verification. The general comparison
  follows the accepted source proof.
- A separate read-only Codex review of the script, exposition, frozen SSML,
  and scene found no material mathematical continuity issue. Its actual
  interval was 2026-11-15T06:13:12-08:00/2026-11-15T06:13:57-08:00
  (45 seconds); it performed no rendering or audio inspection.
- Independently inspected native first-export frames at 24, 56, 75, 79, 92,
  112, 135, 146, 152, 162, 170, 184, 194, 202, 215, 220, 245, 254, 269,
  and 278 seconds. The sole defect was a Unicode prose fraktur glyph at
  24 seconds that rendered a tall stray stroke. Ordinary prose now reads
  “Localize at the chosen prime”; narration still explains the denominators.
  All mathematical formulas, timing, and other sections remain unchanged.
- Added the regression before that fix. It captures the actual production
  Text at the localization show seam and compares its line height with
  the median glyph height, without duplicating source text or coordinates.
  Root observed RED in 0.517 seconds: height 1.477754793 exceeded the
  0.354689367 limit. The one-label fix gives GREEN in 0.495 seconds.
  Logs: videos/build/local-character-comparison-glyph-red.log and
  videos/build/local-character-comparison-glyph-green.log. Fresh corrected
  native frames at 24, 184, and 278 seconds confirm the clean label,
  exact-division proof, and ratio-only conclusion.
- Independently probed the corrected H.264 export: 1920 by 1080 at 30 fps,
  8,375 frames, 279.166667 seconds, 9,497,799 bytes. AAC lasts 279.140998
  seconds and covers the complete 279.140227-second take. Its extracted
  stream is byte-identical to the first export, SHA256
  4db92ee7313b9c806f295a44a5bec9a97c31494293a6c43452138c5bdca81fe8.
  Editorial, SSML, video, scene, and layout hashes match the final manifest.
- Root's corrected all-frame scan checks all 8,375 frames: maximum luma
  16 in the bottom 20% (black). This is separate from sampled visual review.
  The 63 exact-source captions use at most two 42-character lines, have
  durations of at least 1.84 seconds, do not overlap, and end at 277.74 seconds.
  ASR supports wording and timing checks; no independent human listening
  acceptance is asserted.
- Root reports the final shared checks pass: 20 narration tests, 38 video
  tests, and 183 website tests with 9,184 assertions; the build emits 50 pages.

## Report relevance

Records a complete animated local-comparison descent with supplied inputs
and ratio conclusions preserved, measured narration/captions, a concrete
rendered-font defect caught and regression-tested before correction, native
export review, cached-audio reuse, and full-frame subtitle-space evidence.
