# Prepare the Chinese Remainder Coordinates video

- Recorded at: 2026-11-15T04:10:37-08:00
- Observed work interval: 2026-11-15T04:04:16-08:00/2026-11-15T04:10:37-08:00 (381 seconds through narration, scene authoring, and static/arithmetic/caption checks; overlaps root synthesis/alignment work).
- Participants: Steven Creech (three-slide script and refined exposition); Tomas Ortega (finished-video, animation-style, and subtitle-space requirements); OpenAI Codex, GPT-6 (delegated scene authoring and root synthesis/alignment); Google Chirp 3 HD Achird (one continuous default take); faster-whisper Base English (local alignment).

## Context and decision

Produce the [CRT coordinates video](../videos/crt_coordinates.py) from the
unchanged [Video 3.1 script](../website/scripts/node3/crt-coordinates.md),
following the [refined-node exposition](2026-11-15-031448-develop-node-two-and-three-refined-proofs-and-scripts.md).
Cover all three slides: the two residue coordinates, the bijection and its
additivity, and the induced group-ring coordinate change preserving star
and the original norm identity.

## Rationale

Use two residue dials of lengths four and nine, alongside a 36-position
cycle, for the u=3 illustration. Positions 1, 4, and 9 map to (1,1),
(0,4), and (1,0); one further step advances both dials together. Separate
the general coprime injectivity argument from the finite display. Fill a
four-by-nine grid with all original position labels exactly once, then
highlight 4+9=13 and its coordinate addition. This grid groups by residues,
not consecutive blocks of the row.

Keep the polynomial coefficient h_j symbolic and attached while its
monomial changes from X^j to Z^jP^j and its separately reduced exponents.
Do not supply a sign row claimed to be a Hadamard matrix of order 36.
Display multiplication, inversion, and star before carrying the given
norm identity to h(Z,P)h*(Z,P)=4u². Use the shared final-video framing,
explicit colors, and empty lower subtitle band, with no draft label.

## Evidence and outcome

The complete [SSML](../videos/scripts/crt-coordinates.ssml) is 1,976 UTF-8
bytes in three paragraphs. Root synthesized one default Achird take lasting
131.180227 seconds and aligned its exact-source words. Three paragraph
cues and 28 internal detail cues are measured from those words, not estimated.
The editorial SHA-256 still matches the unchanged script. Ruff lint and
formatting and Python compilation pass.

Exact bounded checks cover u in {1,3,5,7,9}: 660 positions, 154,704
addition pairs, 660 inversions, and 660 autocorrelation shifts. Every
coordinate pair occurs once, arbitrary attached coefficients remain
unchanged, and the cyclic and two-coordinate autocorrelations agree.
The displayed j=1,4,9,13 examples are correct. These computations check
the illustrations and map implementation; the general argument is the
coprimality and finite-cardinality proof in the source, not a finite
search or a new Hadamard construction.

All 33 VTT cues match the semantic SSML source, have at most two
42-character lines, no overlaps, a minimum display time of 1.5 seconds,
and bounds within the take. Automated alignment does not establish that
every word is clearly spoken; no independent human listening acceptance
is claimed. The root-controlled timing preflight, final render, visual
review, metadata attachment, and export audit remain pending. A follow-up
record must state their observed outcome before publication.

The subsequent [final export record](2026-11-15-041933-finalize-crt-coordinates-video.md)
records those observed outcomes.

## Report relevance

Records AI-assisted production of a complete refined-node explanation and
its measured single-take timing, explicit preservation of coefficient data,
and bounded numerical evidence. The coordinate change preserves an
assumed norm identity; it does not construct an order-36 Hadamard matrix.
