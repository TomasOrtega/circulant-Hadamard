# Prepare the incompatible residues video

- Recorded at: 2026-11-15T07:10:35-08:00.
- Observed authoring interval:
  2026-11-15T07:06:47-08:00/2026-11-15T07:10:35-08:00 (228 seconds).
- Participants: Tomas Ortega (continuing video request); Steven Creech
  (editorial script); OpenAI Codex, GPT-6 (narration, animation, CPU checks,
  root-agent synthesis and alignment). Concurrent independent review of
  Node 7.2 overlaps this interval and is not additive person-time.

## Context and decision

Produce the complete [Node 8.4 script](../website/scripts/node8/incompatible-residues.md),
following the [Node 8 exposition decision](2026-11-14-205411-draft-node-eight-and-merge-theorem.md)
and [child-script completion](2026-11-15-025408-complete-node-seven-eight-child-exposition-and-scripts.md).
Preserve the editorial source and mathematical-status metadata. The
[scene](../videos/incompatible_residues.py) uses one complete 1,981-byte
default Achird synthesis, five paragraphs and 19 internal phrase cues.
Root's accepted take lasts 129.390227 seconds; all visual iterations reuse it.

## Rationale

State the assumed circulant Hadamard matrix of order $4u^2$ with odd
$u>1$, its distinct-prime subset roots, and the full normalized alternating
sum. Draw the product-to-sum and all-ones proof branches as conclusions
about this same element arising from the same matrix and inputs.

Place both reductions in the full quotient $A/(1+i)A$, without reusing
the comparison symbol $R$ as a ring name. Recall its nonzeroness from
Node 6, and carry $c_Sc_S^{-1}=1$ through reduction to retain defined
normalized terms. No field or domain property of the quotient is assumed.

The two residues force $0=1$, contrary to nonzeroness. Explicitly distinguish
this from the characteristic-two identity $1+1=0$. Exclude precisely all
odd $u>1$, with $u=3$ an instance rather than the entire argument. Leave
$u=1$ separate and retain the earlier delta-theorem hypothesis $u>1$.
The next node, rather than this step, combines the order restriction and
checks both remaining matrix orders.

## Evidence and outcome

- Read the full canonical script and node, plus the preceding surviving-term
  script and following theorem script, to verify the scope of the handoff.
- CPU construction compiles all 22 formula objects and checks 35 shown
  objects against the frame bounds. Ruff, formatting and Python
  compilation pass. Copy targets are registered before animation and
  faded objects leave the cleanup registry.
- The argument is an application of the earlier proof inputs and elementary
  ring identities. No bounded numerical experiment is presented as proof.
  There was no concrete authoring defect requiring a regression test.
- Root's single-take ASR match ratio is 0.9043. Paragraph timing is measured;
  internal phrase alignment, strict actual-scene preflight, rendering,
  native export review, captions and all-frame subtitle-band checks remain
  pending at this author handoff. ASR supports timing and does not establish
  human listening acceptance.

## Report relevance

Records production of the sourced contradiction, with its shared-ring
requirements and exact exclusion range kept explicit. This adds no new
research theorem or formal verification of the proof chain.
