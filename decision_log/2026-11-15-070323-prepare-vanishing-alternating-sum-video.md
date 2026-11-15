# Prepare the vanishing alternating sum video

- Recorded at: 2026-11-15T07:03:23-08:00.
- Observed authoring interval:
  2026-11-15T06:59:24-08:00/2026-11-15T07:03:23-08:00 (239 seconds).
- Participants: Tomas Ortega (continuing video request); Steven Creech
  (editorial script); OpenAI Codex, GPT-6 (narration, animation, CPU checks,
  root-agent synthesis and measured alignment). Concurrent intervals are
  not additive person-hours.

## Context and decision

Produce the complete [Node 7.4 script](../website/scripts/node7/vanishing-alternating-sum.md),
following the [child-exposition decision](2026-11-15-025408-complete-node-seven-eight-child-exposition-and-scripts.md).
Preserve the editorial script and mathematical-status metadata. The
[scene](../videos/vanishing_alternating_sum.py) uses one complete 2,696-byte
default Achird narration, six paragraphs and 27 measured internal phrases.
The accepted take lasts 194.520227 seconds. Visual iterations reuse it.

## Rationale

Display the two congruences from Node 7.3 in the same quotient and with
matching subset indices. Four explicitly illustrative columns for
$I=\{p,q\}$ show their common indexing, with signs $+,-,-,+$.
Replace both entries of each column by its normalized evaluation of $E$,
then restore the full sum over arbitrary subsets. This separates an
illustrative four-column arrangement from the general conclusion.

Use the polynomial definition with its argument $P$. State that division
by two and $1+i$ is exact coefficientwise before reduction, while division
by each evaluated $c_S$ uses a unit in $A$. The identity combining the two
column entries is exact in $A$; adding their alternating-sum congruences
gives $\mathcal S\equiv0\pmod{1+i}$. Keep the original signs even though
plus and minus agree after reduction.

Treat $u=3$ separately. Its common rotation cancels in the normalized ratio;
no division by $E(1)$ occurs, so $E(1)=0$ is allowed. This gives exact
zero for the two-term difference. The many-prime conclusion remains a
congruence without a common-rotation assertion. The final state identifies
the coefficient congruence and the residue-one computation as Node 8's
next input. These choices retain the
[earlier normalization correction](2026-11-15-014331-place-the-example-contradiction-in-node-seven.md).

## Evidence and outcome

- CPU construction compiles all 54 formula objects and checks 49 shown
  objects against the frame bounds. Ruff, formatting and Python
  compilation pass. TransformFromCopy targets are registered before
  animation. Faded column entries and dividers leave their cleanup groups.
- Exact rational Gaussian arithmetic checks 1,944 column identities:
  nonzero $c=a+bi$ with $a,b\in[-2,2]$, and independently chosen real and
  imaginary coordinates in $[-1,1]$ for the integral quotients
  $(d-c)/2$ and $(g-c)/(1+i)$. Subset-sign parity counts pass for one
  through eight distinct indices. These bounded checks support the
  arithmetic and illustration; the general proof is the exact polynomial
  identity followed by addition in a common quotient.
- Root's single take is aligned with ASR match ratio 0.9867. The ignored
  alignment helper initially counted top-level SSML break tags as empty
  paragraphs; root filtered those entries and reused the cached take and
  transcript. Neither the SSML nor committed caption code changed.
- Measured section and internal phrase fields are preserved in the
  manifest. Two paragraph-opening phrase cues are metadata only, so the
  scene does not wait redundantly after its section transition.
- The scene is frozen for actual-scene timing preflight, rendering, native
  export review, captions and the all-frame subtitle-band check. These
  pending outcomes are not claimed by the CPU checks. ASR is supporting
  evidence and does not establish human listening acceptance.

## Report relevance

Records production choices for the sourced additive step, with an explicit
separation between exact integral operations, reduction and the special
two-input cancellation. This adds no research theorem or formal verification.
