# Produce the final Three Evaluations video

- Recorded at: 2026-11-14T23:10:12-08:00
- Observed work interval: 2026-11-14T22:53:48-08:00/2026-11-14T23:10:12-08:00 (984 seconds; scene authoring, primary-agent synthesis/rendering, and delegated verification overlap).
- Participants: Tomas Ortega (production and quality requirements); OpenAI Codex, GPT-6 (primary and delegated authoring, timing, integration, checks); Google Chirp 3 HD Achird (one full-script take); faster-whisper Base English (local supporting alignment).

## Context and decision

Produce the new [Three Evaluations script](../website/scripts/node3/three-evaluations.md)
merged in [PR #8](https://github.com/TomasOrtega/circulant-Hadamard/pull/8).
Continue the [scripted-video production request](2026-11-14-220805-produce-scripted-node-videos.md)
with the user's updated requirement for finished videos, mathematical animation,
and lower subtitle clearance. Keep the editorial source byte-for-byte intact.
The [scene](../videos/three_evaluations.py), [full spoken adaptation](../videos/scripts/three-evaluations.ssml),
[production metadata](../videos/production/three-evaluations.json), [MP4](../website/media/three-evaluations.mp4),
and [exact-source captions](../website/media/three-evaluations.vtt) form one final production.

## Rationale

Use symbolic coefficients for the hypothetical order-36 matrix; no concrete
sign row is invented. Animate each cyclic position j into grid cell
(j mod 4, j mod 9), and group its four rows into H0 through H3. The grid
explicitly differs from rows of the matrix. Evaluate at 1, -1, and i, then
transform the two denominators into 4 and simplify 36/4 to 9. Explain
integer/Gaussian-integer coefficients by even four-sign sums and two-sign
differences, with complex star conjugating coefficients and inverting P.

At permitted ninth-root inputs, transform the norm into modulus three and
show output vectors. State the general odd-u analogue, then illustrate the
later common-rotation result with schematic points and a 120-degree rotation.
The preview explicitly uses additional sign information; common phase change
does not follow from the norm alone. The starting positions are schematic,
not values from an actual order-36 Hadamard matrix. Labels stay attached to
the moving outputs. This preserves the mathematical assumptions without a
creative-draft footer.

The 3,013-byte SSML fits one request and was synthesized once by the primary
agent. Nine paragraph cues and twenty internal mathematical cues were measured
against that take. The five parent previews use the actual CRT, collection,
evaluation, integrality, and normalization intervals; normalization precedes
integrality in the recording, following the supplied six-slide script.

## Evidence and outcome

- Verified the inverse CRT index (9a + 28b) mod 36 for every grid cell and
  checked all 36 positions form a bijection. Checked evenness of the four
  required numerators for all 16 sign columns. These finite checks verify the
  displayed combinatorics and coefficient argument, not existence of a matrix.
- The primary-agent H.264 export is 1920 by 1080, 30 fps, lasting
  214.966667 seconds; 44,100 Hz AAC lasts 214.960998 seconds and covers
  the full 214.960227-second narration. The primary's full
  scan checked all 6449 frames and measured maximum
  limited-range luma 16 in the lower 20 percent
  (black). No footer occupies that subtitle band.
- Inspected representative frames for all sections, plus resting calculations
  at 35, 56, 80, 104, 139, 160, 177, 206, and 212 seconds. The CRT grid,
  normalized identities, integral coefficient formulas, schematic circles,
  attached labels, and final qualification remain readable without overlaps.
- The local alignment ratio is 0.8831; number/letter
  recognition differences limit its evidential value. Captions retain exact
  source wording, case, and punctuation with the shared readable-caption
  segmenter. Automated recognition is supporting timing evidence, not a claim
  of independent human listening acceptance.
- Ruff and scene imports pass. The primary reported 20 narration, 23 video,
  and 87 website tests passing and a successful 22-page build before these
  five measured cuts were attached. After attaching them, all 87 website tests
  passed and the 22-page production build completed successfully. No commit or push is made by
  this delegated author; the primary publishes each video separately.

## Report relevance

Records AI-assisted production of the newly supplied teaching material,
actual work chronology, numerical checks, final media timing, subtitle
clearance, and the distinction between mathematical proof and schematic
animation. No new research result or actual order-36 matrix is asserted.
