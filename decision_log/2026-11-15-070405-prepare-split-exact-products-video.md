# Prepare Split the Exact Products

- Recorded at: 2026-11-15T07:04:05-08:00.
- Observed authoring span:
  2026-11-15T06:58:57-08:00/2026-11-15T07:04:05-08:00 (308 seconds,
  overlapping root narration production and other video work).
- Participants: Tomas Ortega (continuing final-video request); Steven Creech
  (editorial source); OpenAI Codex, GPT-6 (child narration, animation, and
  exact finite checks; root one-take synthesis/alignment).

## Context and decision

Produce canonical [Video 7.1](../website/scripts/node7/split-exact-products.md)
from all four source slides, following the
[Nodes 7–8 source decisions](2026-11-15-025408-complete-node-seven-eight-child-exposition-and-scripts.md).
Preserve the editorial script, node text, shared helpers, and other work.
The canonical script hash is
`2c33806f55d384b2b5da03a6902d777871c3d356cac3797ec96c57cd27c31ffd`;
the node-text hash at reading is
`ec26eeb3c30700ab922098ef974059413b556cd8b0ebb6891b050429bcb6d32e`.

Freeze one complete 2,331-byte, 379-word default Achird SSML request with
four paragraphs. Root's single take lasts 153.520227 seconds; measured
paragraph cues are 0, 43.75, 81.67, and 126.97 seconds. Visual iterations
reuse the same narration. Twenty internal source phrases are unique and
ready for root's measured-cue integration.

## Rationale and mathematical scope

Keep the source assumption u>1 odd, so its prime-divisor set is nonempty.
Introduce the empty input and an arbitrary subset input, then keep both
ratio families in A with the explicit norm inverse for c. Move the actual
even and odd products into a fraction. Highlight the denominator as a
product of units, then move a copy of that same product to the other side
while cancelling its inverse. Label the resulting equality as exact in A,
before reduction.

Use symbolic two-card and four-card examples for u=3 and u=15. The four
ratio labels are copied from their correct parity corners into opposite
products. Explain that the two-prime identity constrains products rather
than forcing all four individual ratios to coincide. No numerical
polynomial values or Hadamard row are invented. Repeat the exact separation
for w and retain both finite positive-exponent products for the next node;
do not perform that later expansion or its cancellation/reduction argument.

The input cards are taller where they contain a root-product formula.
Only actual factor objects move; copy targets enter body ownership first,
and faded bars, factors, and highlights are removed. Ordinary prose stays
in Text and mathematical notation in Tex.

## Evidence and outcome

- Formal exponent bookkeeping checks **510 subset incidences** for one
  through eight primes: multiplying the alternating exponent vector by
  its odd-subset product leaves precisely the even-subset product.
- Exhaustive abstract Gaussian-unit illustrations cover **16 assignments**
  for one prime and **256 assignments** for two primes. Alternating product
  one is equivalent to even-product equal to odd-product in every case.
  Four one-prime assignments and 64 two-prime assignments satisfy it;
  60 of the latter have differing individual ratios. These are abstract
  unit-ring illustrations, not values claimed to arise from the original
  sign polynomials. They support the scope caution rather than replace
  the general algebraic proof.
- Python parsing caught an initial malformed f-string during drafting.
  Replace it with a local product-source helper before freezing the scene.
  Audit 38 AST constants containing TeX and all four actual helper outputs:
  no joined spacing control words or left/right wrappers, and balanced
  helper delimiters. This does not replace actual Manim construction.
- All **34** VTT cues exactly reproduce the frozen narration, at most two
  lines and 42 characters per line, minimum duration 1.86 seconds, no
  overlaps, and bounded times. ASR match is 0.9508; no human listening
  acceptance is claimed.
- Ruff, formatting, Python compilation, and scoped whitespace checks pass.
  Root's full construction/timing preflight, final render, actual-frame and
  export inspection, caption-band scan, hashes, website attachment, and
  individual commit/push remain pending at this checkpoint.

## Report relevance

Records final-video preparation for an existing finite-product lemma,
checked parity illustrations, a clear boundary between equal products and
equal individual ratios, and measured narration/caption limits.

Final export acceptance is recorded in
[the final production entry](2026-11-15-070549-finalize-split-exact-products-video.md).
