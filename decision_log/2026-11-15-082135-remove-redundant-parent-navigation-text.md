# Remove redundant parent-navigation text

- Recorded at: 2026-11-15T08:21:35-08:00
- Observed work interval: 2026-11-15T08:19:37-08:00/2026-11-15T08:21:35-08:00 (118 seconds).
- Participants: Tomas Ortega (copy change and explicit commit/push request);
  OpenAI Codex, GPT-6 (implementation and validation).

## Context and decision

The user requested removing “Return to the bigger picture.” because the button
below already communicates the destination. Remove the paragraph from the
shared [node page renderer](../website/node.jsx), retaining its ParentButton.
This follows the [recent navigation polish](2026-11-15-080003-finalize-active-page-status-and-neutral-route-buttons.md).
The user explicitly requested committing and pushing this follow-up.

## Rationale

The existing button names the higher-level view and provides the return link.
Removing the repeated instruction simplifies every non-root page with a
single shared-template edit.

## Evidence and outcome

All 184 website tests pass (9,352 assertions), and the website build emits 50
active pages. Inspection of all generated active pages confirms the sentence
is absent and every non-root page retains parent navigation. This is a copy
removal; no new test was added. Repository lint follows before commit.

## Report relevance

Records a user-requested editorial simplification. No mathematical content,
video, or proof-status metadata changes.

Final validation recorded at 2026-11-15T08:21:49-08:00: `uv run --locked prek -a --quiet` and staged whitespace checks passed.
