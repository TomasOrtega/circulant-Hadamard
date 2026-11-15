# Develop the refined proofs and scripts for Nodes 2 and 3

- Recorded at: 2026-11-15T03:14:48-08:00.
- Observed work interval: 2026-11-15T02:46:50-08:00–2026-11-15T03:14:48-08:00
  (1678 seconds, through drafting and focused checks).
- Participants: Steven Creech (request for every refined node's exposition and
  production script); Codex/GPT-6 (delegated Nodes 2–3 authoring and validation).

## Context and decision

Complete the six refined nodes of the order restriction and the five refined
nodes of the three evaluations. This develops the earlier
[Node 2 outline](2026-11-14-181021-add-node-two-proof-dependency-graph.md) and
[Node 3 decomposition](2026-11-14-183958-draft-node-three-evaluations-and-keep-u.md).
Add one production script per child in `website/scripts/node2/` and
`website/scripts/node3/`, keeping descriptive filenames. Each has three to five
slides with spoken exposition, displayed equations, and a concrete animation
cue on every slide. Existing main overview scripts are unchanged.

Each leaf now has a boxed result and a concise argument. Parent child excerpts
summarize those arguments rather than promising future expansion. Preserve the
parent overview bodies, graph structure, published media, and cut timings.
Remove the parent-wide Proposition 2.2 black-box metadata now that the descent
is developed; retain the explicitly identified Lemma 2.1 input at Node 2.4.

## Mathematical choices

In [opposite-coefficient divisibility](../website/nodes/cyclotomic-divisibility.md),
state the standard p=2, L=1 specialization of the paper's Lemma 2.1. Explain
its primitive-root basis and normalized valuation, with the Eisenstein and
ramification facts that support the coefficient statement. This is an explicitly
stated cyclotomic input, not a claim to prove the full general local lemma.
Then give the entire deduction: conjugation preserves valuation, the norm
forces valuation t, and the primitive-root basis consists of the opposite
coefficient differences, making each divisible by 2^t.

The [folding proof](../website/nodes/fold-and-divide.md) shows directly that
averaging congruent odd coefficients preserves oddness. Projection commutes
with star, and coefficientwise division of the norm by four is valid in the
free integer group ring. The induction tracks (k,t)=(2s-j,s-j), applies only
while t is at least two, and ends after s-1 steps at length 2^(s+1), norm 4w².
The final odd-square argument gives the contradiction modulo eight. Keep the
original parameter u throughout, introducing only u=2^(s-1)w with w odd.

Node 3 proves the CRT map by injectivity and equal finite cardinalities,
uses the group-ring basis for the four sign polynomials, checks that evaluation
commutes with star, proves coefficient parity independently, and then normalizes
the three norms. Gaussian star conjugates coefficients and inverts the variable.
The circle consequence applies only at u²-th roots of unity. Isolated sign
columns illustrate parity without asserting a hypothetical Hadamard construction.

## Evidence and outcome

- Read the local primary-paper extraction, Section 2 (Lemma 2.1 and
  Proposition 2.2), and the existing Section 4 exposition before writing.
  The new arguments organize those mathematical deductions; they are not new
  research results or Lean verification of the conjecture.
- Four focused existing tests pass, with 120 assertions: Node 2/3 graph and
  navigation, overview math rendering, CRT checks for u=1,3,5, and all sixteen
  sign-column parity/norm calculations. Those finite checks are illustrative,
  not substitutes for the general proofs.
- Rendered all 35 affected bodies, child excerpts, and new scripts with the
  shared Markdown/MathJax renderer, with no reported math errors.
- Verified 11 new scripts, each with three to five slides and exactly one
  animation cue per slide. No recording source or duration was invented.
- Both parent main-page bodies are byte-for-byte unchanged from the starting
  snapshot. Parsed metadata comparison preserves IDs, titles, numbering,
  dependencies, video records, cut timings, and existing status flags, apart
  from the deliberate removal of the parent-wide black-box label.
- The coordinating agent owns combined repository lint, full tests/build,
  global documentation, final header-format normalization, and the separate PR.
  This delegated scope did not edit shared implementation files or perform Git
  staging, commits, or publication.

## Report relevance

Records the transition from refined outlines to complete authored exposition
and per-node animation scripts. AI assistance wrote and checked the content,
with the standard cyclotomic input distinguished from the deductions proved
here and the published recordings preserved.
