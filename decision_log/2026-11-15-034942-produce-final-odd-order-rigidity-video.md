# Produce the final Odd-Order Rigidity video

- Recorded at: 2026-11-15T03:49:42-08:00.
- Observed production, review, and repair interval:
  2026-11-15T02:58:26-08:00/2026-11-15T03:49:42-08:00 (3,076 seconds through final frame acceptance and preview metadata).
- Participants: Tomas Ortega (continuing video-production request); Steven
  Creech (six-slide source); OpenAI Codex, GPT-6 (narration adaptation,
  animated scene, independent root-agent rendering/review, and checks).
- The interval includes waiting and the overlapping compiler-diagnosis work
  linked below; these intervals are not additive person-hours.

## Context and decision

Publish the [Node 6 source](../website/scripts/node6/odd-order-rigidity.md) as
one finished [animated video](../videos/odd_order_rigidity.py), following the
[normalized-E revision](2026-11-15-021017-derive-normalized-e-in-node-six-and-clarify-polynomial-notation.md)
and [latest six-slide script](2026-11-15-022452-refine-scripts-for-nodes-six-through-eight.md).
Preserve the editorial source. Adapt its mathematics into one 3,776-byte,
624-word SSML request using default Chirp3-HD-Achird. Reuse that recording
offline for visual iterations; no further synthesis was requested.

The scene rotates the distinct schematic values $3,-3,3i$ counterclockwise
through $120^\circ$, while $\Delta(c)$ measures the reverse direction. A
separate unit circle contains phase comparisons. Divisibilities become ratio
congruences only after checking units. The geometric-sum proof cancels its
nonzero factor before reduction, then pairs ones in characteristic two.

Keep $d/c=-1$ and $g/c=i$ distinct. Animate the common factor in the linear
combination defining $E$, show $E(1)=-3+3i$ outside the circle, and cancel the
rotation in $E/c$. The schematic's actual $E(1)$ has residue zero; the separate
panel's residues one and zero are requirements of the hypothetical Hadamard
construction. The general-case closing explicitly concerns alternating
products, without asserting a common rotation across all inputs.

## Experiments and corrections

Two unpublished exports exposed wrong formulas. The
[shared compiler scratch race](2026-11-15-032334-isolate-concurrent-manim-tex-compilation.md)
required process isolation. A later
[joined TeX command and stale-DVI fallback](2026-11-15-034434-reject-stale-tex-output-after-compiler-errors.md)
required a source separator correction, per-formula scratch files, strict
compiler errors, and the v3 cache namespace. Three real-compiler regressions
now pass. The final native crop at 259 seconds correctly shows both comparison
ratios equal to one, replacing the duplicated product formula.

**Factual correction:** a full-frame preview appeared to lose title letters.
The actual native crop retains the complete title. Snapshots across 108 plays
showed zero CPU title mutations, and file measurements retained a 62-pixel
header span. No GPU bug was established, so camera/batching settings stayed
unchanged. The measurement harness remains ignored, not a claimed regression.

## Evidence and outcome

- Final MP4: **9,681,793 bytes**, **261.966667 seconds**, H.264 at 1920×1080,
  30 fps; AAC audio lasts 261.940998 seconds and covers the 261.940227-second
  narration. Manifest hashes cover the editorial source, SSML, scene, layout,
  and final video.
- Eleven measured section cues and 37 detail cues pass the timing preflight
  with no lateness above 0.25 seconds. Inspected completed phases and native
  crops at 27, 215, and 259 seconds; the diagrams, formulas, and separate
  arithmetic panel remain legible. No draft footer is present.
- All **7,859 frames** keep the lower 20% blank, with maximum limited-range
  luma 16. The 61 caption cues retain all exact spoken-source text; lines use
  at most 42 characters and two lines. ASR alignment score is 0.9037;
  recognition supports timing and does not certify human listening acceptance.
- Added five measured parent-video cuts for the Node 6 children. The source,
  media, metadata, and cuts are frozen for root's full repository checks and
  individual commit/push. Ruff, formatting, and scoped whitespace checks pass.

## Report relevance

Records final video production, mathematical scope controls, actual export
inspection, and both successful and revised implementation approaches. The
schematic calculations were checked numerically; this task adds no formal
verification or new proof of the conjecture.

## Final integration validation

Observed at 2026-11-15T03:57:10-08:00: all 20 narration and 30 video tests pass, without resource warnings; all 147 website tests pass (8,570 assertions), and the build emits 50 pages. All six new or revised scenes pass strict-compiler preflight without late animation cues. Ruff and whitespace checks pass. Current editorial, narration, scene, layout, and video hashes match all 14 final production records. Root publishes each video in its own commit.
