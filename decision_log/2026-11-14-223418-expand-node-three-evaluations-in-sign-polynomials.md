# Expand Node 3 evaluations in the four sign polynomials

- Recorded at: 2026-11-14T22:34:18-08:00
- Observed work interval: 2026-11-14T22:33:00-08:00/2026-11-14T22:34:18-08:00 (78 seconds).
- Participants: Steven Creech (requested expanded formulas); OpenAI Codex, GPT-6 (editing, delegated sign check, and validation).
- Delegated review: 2026-11-14T22:33:24-08:00/2026-11-14T22:33:27-08:00 (3 seconds, overlapping the primary interval).

## Context and decision

Extend [Node 3's boxed lemma](../website/nodes/three-evaluations.md) after the
[latest sentence edit](2026-11-14-223141-shorten-node-three-grouping-sentence.md).
Retain the definitions c=h(1,P)/2, d=h(-1,P)/2, g=h(i,P)/2 and add their
expansions in H0(P) through H3(P), matching the existing production script.

## Rationale

The expansions make the substitutions visible directly in the statement.
Use weights (1,1,1,1), (1,-1,1,-1), and (1,i,-1,-i), with division by two.
Show the last expression as separate real and imaginary differences.
Put each expansion on the line below its evaluation definition to fit narrow
screens while retaining explicit polynomial arguments throughout.

## Evidence and outcome

Independent review confirmed all signs. All 65 tests passed (6,928 assertions),
and the build emitted 48 pages. Broad lint passed with mutating hooks skipped
to preserve concurrent edits, with the known removed-route notices.
Inspected the compiled section at 500px width: all three expansions fit inside
the lemma. Removed the temporary preview page. The script, graph, hypotheses,
and conclusions are unchanged; no commit, push, or publication occurred.

## Report relevance

Records user-directed expansion of existing formulas for clearer exposition,
with AI assistance and rendering validation; no new mathematical result.
