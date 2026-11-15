# Prepare Form the Combination

- Recorded at: 2026-11-15T06:30:45-08:00.
- Observed production span:
  2026-11-15T06:19:30-08:00/2026-11-15T06:30:45-08:00 (675 seconds,
  including root synthesis/alignment and an interruption). The interruption's
  exact boundaries were not measured. This span overlaps other production
  and is not a measure of active person-hours.
- Participants: Tomas Ortega (continuing final-video request); Steven Creech
  (editorial source); OpenAI Codex, GPT-6 (child narration, scene, exact
  arithmetic checks; root pre-synthesis wording review and synthesis/ASR).

## Context and decision

Produce a final video from the complete three-slide
[Form the Combination script](../website/scripts/node5/form-sign-combination.md),
following the [refined Nodes 5–6 source decisions](2026-11-15-031546-develop-node-five-six-child-exposition.md).
Do not change the editorial script, website fields, or the shared scene helper.

The frozen narration is one complete 2,553-byte, 450-word SSML request with
default Chirp3-HD-Achird. Before the first and only synthesis, root caught an
auditory grouping ambiguity and requested “i times the difference of H one
and H three” instead of the ungrouped “i times H one minus H three.” Apply
that wording clarification before the take; no post-synthesis SSML edits.
The resulting take lasts 170.860227 seconds.

## Rationale and mathematical scope

Use any positive integer u, matching the editorial script: the coefficient
calculation does not require oddness or norm identities. The leaf's broader
proof context still says odd u; no website text is changed. Display the exact
bounded sum for every sign polynomial, including u=1, and copy matching
polynomials into c, d, and g. Highlight the common H-zero cancellation.

Expand d−c and cancel H-zero and H-two terms before taking its exact half.
For (g−c)/(1+i), explicitly multiply by (1−i)/2, expand the numerator over
four, and collect its real and imaginary halves. Demonstrate coefficientwise
integrality with the possible sums −2, 0, 2 and halves −1, 0, 1. These are
exact characteristic-zero calculations; the divisions do not treat 2 or
1+i as units of a reduced ring.

Add the two integral quotients only after justifying them. Move the two
negative H-three halves into −H-three, combine the remaining real half-sum,
and collect i−1. Keep i−1=i(1+i) as a handoff to the later reduction, which
is not performed here. Retain both exact divisibilities for Node 6. Copy
targets are registered before animation and faded transients leave body
ownership. No nine-coefficient example or Hadamard sign row is invented.

## Evidence and outcome

- Exact rational/Gaussian arithmetic checks cover all **16 sign columns**:
  the normalized evaluations, both quotients, the numerator-over-four
  expansion, the collected E formula, and both divisibilities agree.
  Additionally, **625 Gaussian values**, with integer real and imaginary
  parts from −12 through 12, satisfy the displayed reciprocal calculation
  and reconstruct the original value after multiplication by 1+i. These
  finite checks illustrate the general algebra rather than formally verify it.
  Results are in ignored `videos/build/form-sign-combination-math-checks.json`.
- Three measured paragraph cues are 0, 41.67, and 110.21 seconds; ASR match
  is 0.882. Twenty-two internal keys have unique exact-source phrases in the
  production manifest, ready for root's measured-cue integration.
- All **39** VTT cues exactly reproduce the frozen narration: at most two
  lines and 42 characters per line, minimum duration 1.54 seconds, no
  overlaps, and bounded times. Automated alignment does not establish human
  listening acceptance.
- Python compilation, Ruff, and formatting checks pass. Root reviewed and
  accepted the full algebra/common-sign scope of the scene. Strict timing
  preflight, actual rendering, frame and audio/export inspection, final
  caption-band scan, hashes, website attachment, and publication remain.

## Report relevance

Records AI-assisted production of existing sign-polynomial algebra, a
pre-synthesis clarity correction, exact finite illustration checks, and the
current boundary between prepared scene source and unreviewed final media.

Final export acceptance and the prose-label correction are recorded in
[the final production entry](2026-11-15-063418-finalize-form-sign-combination-video.md).
