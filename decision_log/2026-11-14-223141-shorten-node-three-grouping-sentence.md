# Shorten the Node 3 grouping sentence

- Recorded at: 2026-11-14T22:31:41-08:00
- Observed work interval: 2026-11-14T22:31:18-08:00/2026-11-14T22:31:41-08:00 (23 seconds).
- Participants: Steven Creech (requested punctuation and wording); OpenAI Codex, GPT-6 (editing and verification).

## Context and decision

Refine the [recent grouping addition](2026-11-14-222745-include-four-polynomial-grouping-in-node-three-lemma.md)
in [Node 3's boxed lemma](../website/nodes/three-evaluations.md).
End the description of each H_a after its Z-exponent a. Remove the remaining
coefficient-count clause and begin the next sentence with the instruction to
define c(P), d(P), g(P) by the existing formulas.

## Rationale

Follow Steven's requested sentence break and avoid an unnecessary clause.
The sign-coefficient hypothesis remains in the lemma's opening sentence.

## Evidence and outcome

All 65 tests passed (6,928 assertions), and the build emitted 48 pages.
Broad lint passed with mutating hooks skipped to preserve concurrent work;
known removed-route notices remain. No formulas, scripts, or graph changed.
No new tests or browser inspection were needed for this sentence-only edit.

## Report relevance

Records a user-directed editorial correction; no mathematical change.
