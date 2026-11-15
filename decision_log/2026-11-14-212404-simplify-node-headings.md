# Remove generic node-heading labels

- Recorded at: 2026-11-14T21:24:04-08:00
- Observed work interval: 2026-11-14T21:19:10-08:00/2026-11-14T21:24:04-08:00
  (294 seconds through this record, overlapping the route and styling work).
- Participants: Tomas Ortega (issue author and goal to close all open issues);
  OpenAI Codex, GPT-6 (implementation and validation).

## Context and decision

In [issue 4](https://github.com/TomasOrtega/circulant-Hadamard/issues/4), Tomas
requested removal of the generic argument tagline and exposition-draft label.
Remove those heading elements and the generic draft-node fallback. Retain
titles, node numbers, accepted-black-box labels, and foundation labels.

Update [website/AGENTS.md](../website/AGENTS.md) to record draft status in node
metadata and use the meaningful labels in headings. This applies the user's
new direction in place of the earlier instruction requiring a visible draft
badge. Keep existing draft metadata and source-context paragraphs in the
article bodies. Use the writing-for-agents skill for the concise rule update.

## Rationale

The title already identifies the page; the removed labels repeat generic status
without explaining the proof. Black-box and foundation labels convey specific
mathematical scope and remain useful.

## Evidence and outcome

- The heading check failed before implementation. An initially broader assertion
  also matched draft wording in useful source-attribution paragraphs, so narrow
  it to the actual heading group requested in the issue.
- All 17 generated headings retain their titles and omit the generic labels.
  The combined website suite passed: 46 tests and 5,129 assertions; build,
  repository lint, and whitespace checks passed.
- Safari inspection of From Products to Sums confirmed the simplified heading.
  No mathematical prose, draft metadata, or source citations were removed.
- The issue will be closed after the implementation is pushed; publication
  and closure outcomes will be recorded separately.

## Report relevance

This is a user-requested simplification of the website's headings. The AI
assistance concerns rendering, authoring guidance, and validation.
