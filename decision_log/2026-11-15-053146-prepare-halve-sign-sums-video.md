# Prepare the Parity of Sign Columns video

- Recorded at: 2026-11-15T05:31:46-08:00
- Observed work interval: 2026-11-15T05:24:27-08:00/2026-11-15T05:31:46-08:00 (439 seconds through source reading, narration, authoring, arithmetic and caption checks; overlaps root synthesis/alignment).
- Participants: Steven Creech (three-slide source and refined exposition); Tomas Ortega (finished-video and subtitle-space requirements); OpenAI Codex, GPT-6 (delegated authoring and root synthesis/alignment); Google Chirp 3 HD Achird (one complete default take); faster-whisper Base English (alignment).

## Context and decision

Produce [Video 3.4](../videos/halve_sign_sums.py) from the unchanged
[Parity of Sign Columns script](../website/scripts/node3/halve-sign-sums.md),
following the [refined Node 3 exposition](2026-11-15-031448-develop-node-two-and-three-refined-proofs-and-scripts.md).
Cover all three slides: a common coefficient position, the even real
combinations, and the two even components of the Gaussian combination.

## Rationale

Hold P^b fixed while copying its four coefficients out of H_0(P),...,H_3(P).
Move these same coefficients into the two signed real sums. Reduce both
expressions to four ones in a modulo-two panel, pair them, then return to
the original integer expressions before dividing by two. Keep the exact
divisions distinct from modular reduction.

For the Gaussian coefficient, move a_0,a_2 together into the real difference
and a_1,a_3 into the imaginary difference. Halve those even differences
separately before combining them in Z[i]. The numerical column
(−1,1,1,−1) gives 0,0,−1+i. Label it as one coefficient check, not a
Hadamard row or a norm solution. Finish by applying the argument independently
at every power of P and stating that only the common signs are used.
No norm identity is invoked. Register copied targets before animation and
use the common final framing with an empty lower caption band and no draft
label.

## Evidence and outcome

The complete [SSML](../videos/scripts/halve-sign-sums.ssml) has 1,896 UTF-8
bytes and three paragraphs. Root synthesized one default Achird take lasting
127.440227 seconds and aligned its exact-source words. The three paragraph
cues and 20 internal animation cues are measured from those words. The
alignment match ratio is 0.8952. Ruff lint and formatting and Python
compilation pass. The editorial source hash remains unchanged.

An exhaustive check of all 16 four-sign columns confirms that both real
sums and both real/imaginary differences are even. Their halves are integers,
and the Gaussian half has integer real and imaginary components. The
specified example gives the stated three half-coefficients exactly. This
checks the coefficient algebra without assuming a Hadamard construction or
using its norm identity; the source's general passage to polynomials is
coefficientwise.

All 28 caption cues match the semantic SSML source, with at most two lines
of 42 characters, no overlaps, a minimum display time of two seconds, and
bounds within the take. Automated alignment does not establish audible
clarity of every word, and no independent human listening acceptance is
claimed. Root-controlled strict timing preflight, final render, native-frame
review, subtitle-band audit, website attachment, and publication remain
pending. The subsequent [final export record](2026-11-15-054938-finalize-halve-sign-sums-video.md)
records their observed outcome.

## Report relevance

Records AI-assisted production of the exact parity step that makes later
normalization integral, with a complete small coefficient check and explicit
separation from the norm proof and hypothetical Hadamard matrices.
