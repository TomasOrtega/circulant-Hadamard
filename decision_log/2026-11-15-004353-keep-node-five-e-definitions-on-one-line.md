# Keep both Node 5 E formulas on one line

- Recorded at: 2026-11-15T00:43:53-08:00
- Observed work interval: 2026-11-15T00:42:51-08:00/2026-11-15T00:43:53-08:00
  (62 seconds).
- Participants: Steven Creech (explicit formatting preference); OpenAI Codex,
  GPT-6 (edit, read-only review, and validation).
- Delegated review: 2026-11-15T00:43:18-08:00/2026-11-15T00:43:21-08:00
  (3 seconds, overlapping the primary interval).

## Context and decision

Steven requested that both the lemma's definition of E(P) and the expansion
in the H polynomials appear on one line in the proof-map exposition.
Remove their aligned environments and forced line breaks in the body of
[Signs Become All Ones](../website/nodes/signs-become-all-ones.md).

This supersedes the two relevant line-breaking choices in the
[preceding edit](2026-11-15-003958-simplify-node-five-around-the-sign-polynomials.md).
The user prefers the complete additions on one line; narrow screens retain
the existing math-container overflow behavior. Leave the other displays,
production script, graph, and mathematical content unchanged.

## Rationale

Keep each defining sum together as requested. This is a presentation change,
not a mathematical correction.

## Evidence and outcome

The independent read-only check confirms both formulas are single-line
displays and their algebra is unchanged. All 129 website tests pass with
7,902 assertions; the rebuilt site contains 48 pages. Repository lint passes
with mutating hooks skipped to preserve unrelated user edits. The existing
local preview serves the new build. No commit, push, or PR update was made.

## Report relevance

Records the user's display preference and its implementation, preserving the
history of the earlier responsive-formatting choice.
