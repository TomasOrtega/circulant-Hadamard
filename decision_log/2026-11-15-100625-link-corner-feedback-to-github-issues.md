# Link corner feedback to the project's GitHub issues

- Recorded at: 2026-11-15T10:06:25-08:00
- Observed work interval: 2026-11-15T10:04:43-08:00/2026-11-15T10:06:25-08:00 (102 seconds through browser validation).
- Participants: Tomas Ortega (feedback-link request); OpenAI Codex, GPT-6
  (implementation and checks).

## Context and decision

The user requested adding the inherited feedback control and linking it to
the project's GitHub issues page. Extend the existing
[corner controls](2026-11-15-095039-add-share-and-jump-controls.md) with a
“Website feedback” link to `https://github.com/TomasOrtega/circulant-Hadamard/issues`.
Retain the existing styling, with an inline chat icon following the pinned
upstream Feedback component's presentation.

## Rationale

Use an ordinary anchor in the existing control renderer. This preserves native
link and keyboard behavior while sharing the buttons' markup and styling.
The requested destination needs no feedback form, client handler, or dependency.

## Evidence and outcome

- All 188 website tests pass (9,894 assertions); all 50 active pages build
  with the accessible feedback link and exact requested destination.
- Firefox 153 and Chromium checks cover keyboard activation and control
  placement at 320, 390, and 1280 pixels. Navigation to the expected GitHub
  URL is verified with an intercepted request; no issue is submitted.
  A phone-width screenshot was inspected.
- Repository lint and whitespace checks pass. The share and jump controls
  retain their native button elements; their client script is unchanged.

## Report relevance

Records a user-directed feedback entry point. It adds no mathematical claim.
