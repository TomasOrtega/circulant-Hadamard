# Remove the redundant homepage summary paragraph

- Recorded at: 2026-11-15T11:07:35-08:00
- Observed work interval: 2026-11-15T11:06:21-08:00/2026-11-15T11:07:35-08:00 (74 seconds).
- Participants: Tomas Ortega (issue request); OpenAI Codex, GPT-6
  (implementation and checks).

## Context and decision

[Issue #25](https://github.com/TomasOrtega/circulant-Hadamard/issues/25)
requests removing the visible homepage sentence beginning “A high-level
overview of the proof.” Render summary paragraphs only on non-root views.
Keep the homepage's description metadata and other node summaries.
This revises the visible framing from the
[front-page exposition decision](2026-11-14-171213-simplify-front-page-exposition.md).

## Rationale

The proof map already communicates the available deeper explanations.
One condition removes the repeated instruction without changing mathematical
content, metadata, or layout elsewhere.

## Evidence and outcome

All 184 website tests pass (9,865 assertions), and all 48 active pages build.
A Chromium check confirms the sentence is absent from visible body text,
remains in description metadata, and all eight main deeper links remain.
Repository lint and whitespace checks pass. No new test, dependency, or
client code is added for this copy removal.

## Report relevance

Records a user-directed editorial simplification with no mathematical change.
