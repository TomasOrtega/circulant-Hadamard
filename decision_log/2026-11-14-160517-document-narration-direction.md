# Document narration delivery and teaching pauses

- Recorded at: 2026-11-14T16:05:17-08:00
- Observed work interval: 2026-11-14T16:04:40-08:00/2026-11-14T16:05:17-08:00 (37 seconds).
- Participants: Tomas Ortega (instruction update request); Codex (GPT-6, documentation and checks).

## Context and decision

The user requested adding the accepted
[expressive narration proposal](2026-11-14-160253-expressive-narration-and-pauses.md)
to the appropriate agent instructions. Extend [videos/AGENTS.md](../videos/AGENTS.md)
with guidance for teaching pauses, delivery cues, and the planned narrator controls.

## Rationale

Keep narration conventions beside the existing scene instructions. Explain that
thinking pauses follow completed narration blocks, and distinguish the planned
`delivery` and `pause_after` keywords from the current API. Record optional Gemini
synthesis, an Achird audition before changing the default, and the required cache
and timing coverage. Link the proposal for API details and source limitations.

## Evidence and outcome

Reviewed the instructions against the earlier proposal. All local links in
videos/AGENTS.md resolve, and whitespace checks passed. Only documentation
changed; runtime tests and rendering were unnecessary. The narration controls
remain proposed and no audio was generated.

## Report relevance

This records the user's adoption of AI-assisted production guidance after
submission. It changes authoring instructions without adding a mathematical
claim or publishing media.
