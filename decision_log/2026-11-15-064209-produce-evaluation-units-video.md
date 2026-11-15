# Produce the evaluation units video

- Recorded at: 2026-11-15T06:42:09-08:00.
- Observed production, correction and review interval:
  2026-11-15T06:31:20-08:00/2026-11-15T06:42:09-08:00 (649 seconds,
  including rendering waits).
- Participants: Tomas Ortega (continuing video request); Steven Creech
  (editorial script); OpenAI Codex, GPT-6 (narration, animation, root-agent
  synthesis/rendering, independent mathematical and export review).
  Concurrent intervals overlap and are not additive person-hours.

## Context and decision

Produce a final video from the [Node 6.2 script](../website/scripts/node6/evaluation-units.md),
following the [Node 5–6 exposition decision](2026-11-15-031546-develop-node-five-six-child-exposition.md).
Preserve that editorial source and mathematical-status metadata. The
[scene](../videos/evaluation_units.py) uses one complete 2,745-byte default
Achird synthesis, seven measured sections and 31 internal phrase cues.
All visual revisions reuse the accepted recording.

## Rationale

Construct the common ring $A=B[1/u]$ for odd $u>1$. Keep the subset
evaluations together and use the norm identity to give the explicit inverse
$\overline{x_S}/u^2$ in this ring. Explain closure under conjugation through
inverses of the generating roots, and give $\overline{c(\omega)}/9$ for $u=3$.

Prove nonzero reduction separately. Bounded powers of the generating roots
give finite generation over $\mathbb Z$; containment in $\mathbb C$ gives
additive torsion-freeness. The standard structure theorem then gives a
nonzero free abelian group of finite rank, so $B/2B\ne0$. Choose a maximal
ideal above two. In its nonzero residue field, $(1+i)^2=2i=0$ forces
$1+i=0$, while odd $u$ maps to one. Extend this map after adjoining $1/u$
and factor it through $A/(1+i)A$. Its image of one proves that this quotient
is nonzero; the factorization of two gives characteristic two. Do not
assume that the quotient itself is a field.

Carry $x_Sx_S^{-1}=1$ through reduction to prove that the required
denominators remain units. Keep this operation separate from the earlier
exact polynomial divisions by two and $1+i$, whose residues are zero.

## Correction and validation

The first visual candidate introduced the abbreviation $R=A/(1+i)A$.
Root review at 06:38:22 PST identified its collision with the comparison
product $R=\Delta(d)/\Delta(c)$ defined in Node 6.1 and used later.
Remove that abbreviation throughout the visuals, use the full quotient
expression or ordinary prose, and separate the nonzero and characteristic
statements to retain readable spacing. The SSML already says “the quotient,”
so narration and every cue remain unchanged. This notation correction is
checked through fresh actual-export review rather than a mirrored string test.

- Final CPU construction compiles all 42 formula objects and checks 56
  shown objects against the frame bounds. Ruff, formatting and Python
  compilation pass. Copy targets are registered before animation; faded
  transient labels leave the cleanup registry.
- Nineteen exact rational Gaussian examples verify the inverse formula:
  signed real/imaginary norm examples for $u=3,5,7,9$, and three signed
  $3+4i$ norm-25 examples. A concrete $\mathbb F_4$ calculation checks its
  three nonzero inverses and odd denominators from 3 through 31.
  These bounded checks support the examples; the general proof uses the
  displayed norm and ring-map arguments, with standard algebra inputs.
- Strict actual-scene timing preflight passes at 185.660227 seconds with
  no late events. Author review inspected all seven completed proof phases
  and 15 intermediate frames of the first candidate. After correction,
  root and author accepted the revised quotient notation, characteristic
  statement, and unit conclusion; the author also inspected fresh
  intermediate field-map and reduced-inverse states. No remaining blockers.
- Final MP4: **6,170,766 bytes**, **185.666667 seconds**, H.264 1920×1080 at
  30 fps; AAC lasts 185.660998 seconds. Root's final scan checks all
  **5,570 frames**, preserving a blank lower 20% with maximum limited-range
  luma **16**. No draft footer is present.
- All 43 captions exactly reproduce the spoken source, with at most two
  lines of 42 characters, minimum duration 1.62 seconds, no overlaps and
  in-bounds times. ASR match ratio 0.9678 supports timing; it does not
  establish a human listening review. Editorial, scene, layout, SSML and
  video hashes match and are saved in the manifest.
- Root reports the full video check passing and the website's 183 tests,
  9,229 assertions and 50-page build passing. The individual commit/push
  follows these recorded production outcomes.

## Report relevance

Records production of the existing unit-denominator and nonzero-quotient
arguments, including a project-wide notation correction found in review.
This adds no new research proof or formal verification of the conjecture.
