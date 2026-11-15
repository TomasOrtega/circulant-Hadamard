# Produce the final Delta-theorem video

- Recorded at: 2026-11-15T01:18:30-08:00
- Observed work interval: 2026-11-15T00:47:07-08:00/2026-11-15T01:18:30-08:00 (1883 seconds; primary and delegated work overlaps and is not additive person-hours).
- Participants: Tomas Ortega (ongoing production and quality request); Steven Creech (source script revisions); OpenAI Codex, GPT-6 (primary and delegated authoring, mathematical checks, review, rendering, integration); Google Chirp 3 HD Achird (one complete synthesis); faster-whisper Base English (local supporting alignment).

## Context and decision

Continue the [scripted-video request](2026-11-14-220805-produce-scripted-node-videos.md)
after its recurring check found [PR #9](https://github.com/TomasOrtega/circulant-Hadamard/pull/9).
The primary agent [merged the CI-green source](2026-11-15-005212-merge-node-four-for-video-production.md)
before production. Preserve the [editorial script](../website/scripts/node4/delta-theorem.md)
byte-for-byte and follow its corrected quotient direction and Kronecker-led
proof sketch, including the [source storyboard](../website/scripts/node4/storyboards/phase-circles.svg).
The [scene](../videos/delta_theorem.py), [single full SSML take](../videos/scripts/delta-theorem.ssml),
[production metadata](../videos/production/delta-theorem.json), [MP4](../website/media/delta-theorem.mp4),
and [captions](../website/media/delta-theorem.vtt) form the finished production.

## Rationale

Keep root-of-unity inputs on a separate plane from radius-three output values.
Use the genuine Gaussian group-ring example f(P)=3iP, with f*=−3iP inverse,
whose nine outputs rotate by 90 degrees and scale by three. The equal spacing
is specific to that polynomial, which is explicitly not a Hadamard sign row.
Define omega as exp(2 pi i/3). The quotient f(1)/f(omega) rotates clockwise
120 degrees from denominator to numerator and equals omega squared. Its
endpoint appears on a separate unit circle; neither original output point
is relabeled as the quotient.

For general odd u>1, use distinct prime divisors and subsets. Explain even
subsets above the fraction line, odd subsets below it, and the empty factor
f(1). Animate the two-prime terms into numerator and denominator products,
without suggesting vector addition. Equal counts cancel evaluation magnitudes
for every conjugate. Show algebraic integrality as a separate arithmetic
input; together these allow Kronecker's theorem. Reveal odd order only after
the separately labeled congruence step. Then show the full u=3 restriction
to 1, omega, omega squared and carry the three Delta(c), Delta(d), Delta(g)
inputs to Node 6. Its conclusion remains for the later node.

The overview names the arithmetic comparison but does not explain the local
character-component/unit/residue lemma. Leave that child's excerpt unset.
Attach only the five measured previews actually covered by this recording:
Circle Evaluations 15.81–57.83 seconds; Alternating Phase Product 103.13–168.05;
Integral Delta 188.50–193.76; Kronecker Step 168.05–197.79; Odd Order
197.79–216.39. These excerpts introduce the relevant overview ideas; they are
not substitutes for the detailed proofs.

## Evidence and outcome

- One 3,768-byte SSML request generated the complete 238.780227-second
  default Achird take. Eleven paragraph cues and 22 internal mathematical
  beats were measured against it. Offline visual revisions reused that take;
  there was no additional synthesis. Timing preflight recorded no late events
  above its 0.25-second tolerance and a 238.780-second scene timeline.
- The final H.264 export is 1920 by 1080 at 30 fps, 238.800000 seconds,
  and 8,269,620 bytes. Its 44,100 Hz AAC track lasts 238.780998 seconds and
  covers the whole recording. The primary decoded every one of its
  7164 frames; the lower 20 percent has maximum
  limited-range luma 16, which is black. No
  footer or other mathematical content occupies the subtitle band.
- Inspected the section contact sheet and resting calculations, including
  fresh final-export frames at 85, 96, and 195 seconds. The primary independently
  reviewed representative frames across all sections. The quotient direction,
  separate unit circle, parity fraction, two Kronecker inputs, and separate
  odd-order conclusion remain legible.
- Pre-publication frame review found cardinal value labels colliding with axes
  and circle arcs, and the conclusion arrow crossing the arithmetic caption.
  Five geometry cases failed before their respective corrections. Labels now
  anchor outside the circle, the initial reference label is removed before
  rotation, and the arithmetic caption uses two clear lines to the right.
  All three focused geometry tests now pass. The corrected full export was
  rerendered offline and inspected again.
- Floating-point checks with tolerance 1e-12 verified all nine concrete output
  magnitudes, the displayed norm product, and the quotient's clockwise angle
  and value. Enumerated balanced subset counts for 1–7 distinct-prime
  directions. These are illustration checks, not an independent proof of the
  general arithmetic theorem or formal verification.
- The local alignment ratio is 0.9325. Recognition
  supports wording and timing but does not establish human listening
  acceptance. Captions retain exact spoken-source case and punctuation in
  54 nonoverlapping cues, each at most two 42-character lines; the observed
  minimum display is 2.3 seconds. The selected voice and defaults match the
  approved project baseline.
- The primary reports all 20 narration and 26 video tests passing, plus all
  96 website tests and the 28-page build after the measured previews. Ruff
  and the focused geometry suite pass locally. The prior nine productions'
  source/SSML/scene/layout/video hashes and all 18 prior media Git objects
  were checked unchanged. Current source, scene, layout, narration, and video
  hashes match this production's metadata.
- The delegated author makes no commit or push. The primary stages this video
  separately, runs repository lint/whitespace checks, and publishes it with
  the required conventional commit and AI trailer.

## Report relevance

Records user-supplied mathematical exposition becoming a final teaching video,
actual work chronology, bounded computations, measured media and subtitle
clearance, and independently reviewed visual corrections. It separates the
accepted arithmetic inputs and illustrative computations from a new proof,
an actual Hadamard sign construction, or human acceptance of this take.
