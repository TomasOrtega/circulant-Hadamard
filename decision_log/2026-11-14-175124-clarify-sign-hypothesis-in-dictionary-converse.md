# Clarify the sign hypothesis in the dictionary converse

- Recorded at: 2026-11-14T17:51:24-08:00
- Observed work interval: 2026-11-14T17:48:54-08:00/2026-11-14T17:51:24-08:00 (150 seconds through this record).
- Original request and initial read time: unknown; the observed interval starts
  at the first recoverable clock reading after conversation compaction.
- Participants: Steven Creech (script edits and requested clarification);
  OpenAI Codex, GPT-6 (editing, validation, and delegated mathematical review).
- Review interval: 2026-11-14T17:49:09-08:00/2026-11-14T17:49:20-08:00
  (11 seconds, overlapping the primary interval).

## Context and decision

Steven requested edits to his current [Node 1 script](../website/scripts/node1/group-ring-encoding.md)
and the website statement, emphasizing the need for coefficients $\pm1$ in
its converse. Preserve the current example-first narration and its edits;
make targeted changes to the dictionary and one inaccurate opening phrase.
Use the [numbered script folders](2026-11-14-173621-move-scripts-into-numbered-node-folders.md)
and maintain the [explicit group-ring notation](2026-11-14-172944-remove-group-ring-abbreviation.md).

State explicitly that all $n$ coefficients, including the constant position,
are signs. The converse constructs the circulant matrix from that list and
its cyclic right shifts; the polynomial identity gives orthogonality, and
the coefficient assumption gives the required matrix entries. Update the
[main-page goal and Node 1 subsection](../website/nodes/group-ring-encoding.md),
[deeper dictionary proof](../website/nodes/hadamard-dictionary.md), and its
[production narration](../website/scripts/node1/hadamard-dictionary.md)
consistently. The statement placement follows the
[existing subsection layout](2026-11-14-172603-put-node-exposition-in-child-sections.md).

## Rationale

The original lemma already assumed sign coefficients, but the reverse
explanation did not repeat the assumption. The norm identity alone is
insufficient for a Hadamard matrix: at $n=4$, $h(X)=2$ has product $4$, yet its
coefficient list $(2,0,0,0)$ gives $2I_4$, not a sign matrix. Add this short
example to the deeper proof and narration. Retain their all-ones example,
which illustrates the separate failure of orthogonality despite sign entries.
Keep the high-level narration focused on the dictionary.

**Factual correction:** replace “Its rows are not independent” with “The
first row determines every row.” Hadamard rows are linearly independent;
being determined by cyclic shifts is a different assertion. Also replace
“nonconstant dot products” with the precise reference to the product's
nonconstant coefficients.

## Evidence and outcome

- Read the current script from disk before editing and independently reviewed
  the converse. The argument is elementary mathematical reasoning, not a new
  research result or formal verification.
- A direct integer computation checked all four product coefficients and all
  sixteen Gram entries for $(2,0,0,0)$: the product is $(4,0,0,0)$ and the Gram
  matrix is $4I_4$, while the sign condition fails.
- All 41 existing website tests passed (5,023 assertions), including script
  math rendering and statement placement. The build emitted 17 pages.
  No new tests were needed for this prose clarification.
- Required repository lint, explicit lint of all four edited Markdown files,
  and `git diff --check` passed. The rebuilt local preview contains the revised
  statements. There were no layout or graph changes.
- Prior uncommitted changes are preserved. No commit, push, recording, or
  hosted deployment was made.

## Report relevance

This documents a user-identified exposition gap and a separate factual wording
correction, with AI-assisted editing and mathematical review. It makes the
hypotheses needed for the reverse construction visible at both reading depths.
