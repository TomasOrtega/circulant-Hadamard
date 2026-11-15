# Refine Node 1 from the corrected video script

- Recorded at: 2026-11-14T16:48:17-08:00
- Observed work interval: 2026-11-14T16:37:49-08:00/2026-11-14T16:48:17-08:00 (628 seconds through this record).
- Participants: Steven Creech (request and supplied PDF); OpenAI Codex, GPT-6
  (implementation, prose adaptation, transcription, and checks).

## Context and decision

Steven supplied `hadamard_node_1_corrected.pdf` and requested its refined graph,
natural-language explanations, and video script files. Its authoring time is
unknown. Preserve the supplied document in
[the source folder](../website/scripts/node1/reference/README.md), with a page-to-script
index. The PDF is source material for this request; its production directions
are retained as content, not treated as unrelated agent instructions.

Add exactly five children to [Group-Ring Encoding](../website/nodes/group-ring-encoding.md):
1.1 Group Ring, 1.2 Cyclic Shifts, 1.3 Star Operation, 1.4 Correlation Identity,
and 1.5 Hadamard Dictionary. This supplies the first refinement deferred by the
[eight-node map decision](2026-11-14-151609-eight-node-proof-map.md). Other main
nodes retain their existing scope. The order-36 and general reading routes remain.

Use the five logical arrows in PDF page 6 and retain 1.1-to-1.4 as shared notation.
All connections remain solid with uniform blue-outlined nodes, following Steven's
[graph-style preference](2026-11-14-153401-simplify-proof-graph-style.md), even though
this PDF distinguishes the context link with dashes. Node descriptions explain
that distinction in words.

## Rationale

Keep production narration and animation cues in six editable files under
[scripts](../website/scripts/README.md), following the
[script-storage decision](2026-11-14-154516-store-overview-video-script.md).
Restore PDF equations as LaTeX, omit running headers/footers, and normalize
punctuation and line wrapping. Make the modulo-n exponent convention explicit
in the dictionary script. These are edited transcriptions, not byte-identical
text extractions; the original PDF is preserved byte-for-byte.

Adapt separate reader-facing explanations into the parent and five node files.
Use the fixed row (-1, 1, 1, 1), whose star equals itself; use generic coefficients
to illustrate reversal. Include the coefficient proof for arbitrary integers,
both directions of the sign-matrix equivalence, and the all-ones counterexample.
Keep Fourier evaluations outside this supplied refinement. Mark the three basic
algebra nodes as terminal undergraduate foundations; leave all videos and cuts
unset until recordings and timings exist.

Extend the existing renderer with a custom graph caption, height from node
positions, and an outer route for the long notation connection. Derive notation
labels from the actual source node instead of hardcoding Group-Ring Encoding.
Child pages show the parent-map disclosure and retain ordinary navigation links.
Node 1 opts into prose-before-graph ordering, continuing the
[paper-style introduction](2026-11-14-163149-formal-theorem-and-matrix-definitions.md).
Remove the generic claim that video scripts are forthcoming now that scripts
exist for this part of the site. Preserve the earlier uncommitted overview edits.

## Evidence and outcome

- `make -C website check all` with the pinned Bun binary passed: 39 tests,
  4,985 assertions, and 17 built pages. Checks cover the supplied dependency
  structure, child/parent links, all rendered math, and six narration scripts.
- Independent finite arithmetic checks cover all 126 sign rows of lengths 1–6,
  comparing cyclic polynomial coefficients, shifted-row dot products, and the
  Gram matrix; one nonsign integer row checks the coefficient identity separately.
  The fixed order-four example and all-ones counterexample also pass. These are
  computational checks, not Lean verification or a proof of the main conjecture.
  The general elementary proofs are written in the new explanatory pages.
- Repository lint and explicit checks of new files passed. `git diff --check`
  passed. `cmp` confirmed the archived PDF matches the supplied source.
- Chrome screenshots at 1440px wide show the full refined graph, readable
  equations, and dictionary table. A 500px-wide check of Correlation Identity
  shows its parent link, context label, formulas, and complete example table.
- During preparation, a temporary frontmatter formatter incorrectly split on
  Markdown table separators, truncating two bodies. Inspection caught this;
  both tables and their following prose were restored from the authored text
  before the final build and visual checks. A test initially required every
  script to repeat the fixed tuple; this overconstraint was removed because
  the source's general-only sections do not repeat that example.
- Work remains local on the existing feature branch. This request does not
  create a recording or publish a new deployment.

## Report relevance

This records AI-assisted conversion of Steven's supplied corrected teaching
material into a navigable refinement, readable mathematical exposition, and
editable production scripts. It adds an explanation of the group-ring
Hadamard dictionary, not new research evidence for the overall theorem.
