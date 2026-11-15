# Produce the alternating phase product video

- Recorded at: 2026-11-15T06:13:36-08:00.
- Observed production and review interval:
  2026-11-15T05:54:40-08:00/2026-11-15T06:13:36-08:00 (1,136 seconds).
- Participants: Tomas Ortega (continuing production request); Steven Creech
  (editorial script); OpenAI Codex, GPT-6 (narration, animation, rendering,
  mathematical checks and independent export review). Concurrent intervals
  overlap and are not additive person-hours.

## Context and decision

Produce a final video from the [Node 4.2 script](../website/scripts/node4/alternating-phase-product.md),
following the [refined exposition decision](2026-11-15-031809-develop-all-refined-node-exposition-and-scripts.md).
Preserve that editorial source and its mathematical status. The
[scene](../videos/alternating_phase_product.py) uses one complete 2,923-byte
default Achird SSML synthesis, seven measured sections and 18 internal cues.
All visual development reuses the accepted recording.

## Rationale

Start with the valid norm example $f(P)=3iP$ in $\mathbb Z[i][C_9]$:
$ff^*=9$ and $\Delta(f)=\omega^{-1}$. Show the quotient removing the common
length three and retaining the relative angle. Use exact $\sqrt3$ geometry.
Then introduce allowed subset inputs, the two-prime numerator/denominator
roles, and the toggle involution. Label that drawing as an illustration;
the general equal counts are $2^{r-1}$ for $r\ge1$.

Keep nonzero complex division separate from later local residue arguments.
An embedding acts on coefficients, including $i$, as well as on the chosen
roots. Explain why it commutes with conjugation on the cyclotomic field,
then apply the transformed norm identity and the same subset pairing.
Integrality remains an explicit next step before Kronecker is applicable.

## Evidence and outcome

- Strict actual-scene TeX/timing preflight passes at 196.840227 seconds
  with no late events. Source formatting and lint checks pass.
- Exact finite bookkeeping checks toggle pairing for one through eight
  distinct primes (36 directions). The example has cyclic norm
  $(9,0,\ldots,0)$; floating-point checks confirm its quotient and all four
  embeddings of $\mathbb Q(i,\omega)$. These illustrate the supplied
  general argument, rather than formally proving the theorem.
- Root and an independent agent reviewed seven native exported phases,
  including a native crop confirming the complete conjugate equation.
  Independent review at 06:08:54–06:09:36 PST found no blockers.
- Final MP4: **6,435,225 bytes**, **196.866667 seconds**, H.264 1920×1080 at
  30 fps; AAC lasts 196.840998 seconds. All **5,906 frames** preserve a
  blank lower 20%, maximum limited-range luma **16**. No draft footer.
- All 46 captions exactly preserve the spoken source, at most two lines
  of 42 characters, minimum duration 1.92 seconds and no overlaps.
  ASR match ratio 0.9421 supports timing; it does not establish a human
  listening review. Editorial, scene, layout, SSML and video hashes match.
  Final repository checks and the individual commit/push follow.

## Report relevance

Records explanatory production of the alternating-product construction
and its archimedean magnitude argument. This presents supplied mathematics;
it adds no new research proof or formal verification of the conjecture.

## Final repository validation

Recorded at 2026-11-15T06:20:32-08:00. Root independent source and native-export review
accepts the final candidate. Repository checks pass: 20 narration tests,
38 video tests, 183 website tests with 9,184 assertions, and a 50-page
website build. The 26 prior final videos retain matching source, scene,
layout, SSML and media hashes and valid exact captions. Each new video
is committed and pushed separately after its own staged lint check.
