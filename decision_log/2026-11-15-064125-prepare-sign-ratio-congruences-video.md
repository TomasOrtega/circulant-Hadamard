# Prepare the residue-one ratios video

- Recorded at: 2026-11-15T06:41:25-08:00.
- Observed authoring span:
  2026-11-15T06:35:20-08:00/2026-11-15T06:41:25-08:00 (365 seconds,
  overlapping root synthesis/alignment and other production).
- Participants: Tomas Ortega (continuing final-video request); Steven Creech
  (editorial source); OpenAI Codex, GPT-6 (child narration, scene, and exact
  arithmetic checks; root canonical-number clarification and synthesis/ASR).

## Context and decision

Produce the complete three-slide
[Sign Ratio Congruences script](../website/scripts/node6/sign-ratio-congruences.md).
Use its canonical number **6.3**, confirmed by root after a numbering typo
in the assignment. Follow the
[refined Nodes 5–6 decisions](2026-11-15-031546-develop-node-five-six-child-exposition.md)
and the exact-divisibility input from
[Form the Combination](2026-11-15-063418-finalize-form-sign-combination-video.md).
Preserve the editorial source and website metadata.

Use one complete 2,808-byte, 508-word SSML request with default Achird.
Root produced a 199.740227-second take and paragraph cues at 0, 74.07,
and 132.17 seconds. Freeze the narration; visual iterations reuse that take.

## Rationale and mathematical scope

Start with the common sign coefficients and exact polynomial quotients
already formed before reduction. Transform divisibility into identities
and evaluate both sides at the same subset root. Use the preceding Node 6.2
as the explicit input that A=B[1/u] has unit evaluations and a nonzero
quotient by 1+i. Keep the particular inverse of c_S, its conjugate divided
by u squared, visible before constructing ratios.

Rewrite each ratio minus one as a difference over c_S and substitute the
exact identities. The remaining quotients belong to A. Show
2=−i(1+i) squared, then apply an explicit reduction map pi to the entire
equation: the right factors become zero. Do not display the unreduced
ratios as equal to one, or divide by zero residues.

Prove the inverse rule by reducing t times its inverse, with t an arbitrary
r_S or w_S. Arrange the general comparison products into even/odd subset
fractions, with explicit S-subset-I bounds. Change their labels to pi(R)
and pi(W) when replacing the factors by one. Conclude congruence modulo
1+i. The two-input u=3 example illustrates the same product rule, without
claiming exact comparisons or a general common rotation. Odd-order
rigidity remains a later step.

## Evidence and outcome

- All **16 sign columns** satisfy d−c=2a and g−c=(1+i)b with the stated
  integral quotients, and both differences have zero Gaussian residue.
  No coefficient value c is used as a denominator in these checks: unit
  evaluations are a separate algebraic input. Four Gaussian unit inverses
  and 16 unit products preserve residue one; the displayed factorization of
  2 is exact. These finite illustrations do not formally verify the proof.
- Twenty-seven internal keys have unique exact-source phrase anchors.
  ASR match is 0.9337. One alignment limitation is documented in the manifest:
  the subtraction sentence's words have zero duration at 86.16 seconds,
  tied to the following “Combine” onset. Anchor `subtract_one` to the
  preceding denominator phrase beginning with c at 81.62 seconds, while
  retaining the reliable combine-fractions onset. This uses a measured
  source-word boundary and publishes no estimated spoken-word times.
- All **46** VTT cues reproduce the frozen narration exactly, with at most
  two lines and 42 characters per line, minimum duration 1.88 seconds,
  no overlaps, and bounded times. Alignment supports timing and does not
  establish human listening acceptance.
- Python compilation, Ruff, formatting, and scoped whitespace checks pass.
  Copy targets are registered before animation; faded transients leave body
  ownership. Root's measured-detail integration, strict preflight, final
  render, frame/export review, caption-band scan, hashes, and publication
  remain pending at this checkpoint.

## Report relevance

Records production of an existing proof node, its exact-division and unit
dependencies, explicit distinction between reduction and equality, checked
finite illustrations, and a measured alignment limitation.

Final export evidence and both typesetting follow-ups are linked in
[the final production entry](2026-11-15-065510-finalize-sign-ratio-congruences-video.md).
