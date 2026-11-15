# Explain Chirp pauses while preserving one generated take

- Recorded at: 2026-11-14T17:51:33-08:00
- Observed work interval: 2026-11-14T17:50:11-08:00/2026-11-14T17:51:33-08:00 (82 seconds).
- Participants: Tomas Ortega (pause-control question); Codex (GPT-6, current documentation and local SDK checks); Google documentation (sources only).

## Context and decision

Following the [Chirp baseline recommendation](2026-11-14-173913-recommend-approved-chirp-baseline.md),
the user asked how pauses and related delivery controls would work. Keep one
full-script synthesis call. Recommend punctuation for natural phrasing and
local silence insertion at sentence boundaries for precisely timed teaching
pauses, preserving the speech samples from the same take. Align visual cues
to the resulting WAV. A Manim wait by itself does not pause an existing recording.

## Rationale

Editing a quiet gap in one recording retains its voice performance and allows
pause-duration edits without resynthesizing individual sentences. This differs
from joining independent synthesized takes; the one-take rule concerns generation.
Keep the selected Chirp voice and normal rate fixed. Use wording and visuals
for emphasis before experimenting with pitch or other delivery changes.

The current [Chirp family guide](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd#chirp_3_hd_ssml_support)
also documents Preview SSML support for synchronous synthesis, including
`<break>`, `<prosody>`, and pronunciation elements. The [SSML reference](https://docs.cloud.google.com/text-to-speech/docs/ssml#break)
defines requested break durations such as `<break time="800ms"/>`. SSML belongs
in `input.ssml`, not the current plain-text input path. This is an optional
single-request generation method requiring an implementation change and a live
audition; no timing or voice-quality equivalence was established here.

## Evidence and outcome

Rechecked the specific Chirp guide, updated November 10, 2026. It also documents
Preview `[pause short]`, `[pause long]`, and `[pause]` controls through
`input.markup`, with context-dependent durations and possibly ignored tags.
Those are unsuitable for promising exact teaching-pause lengths.

The installed SDK locally constructed `SynthesisInput(ssml=...)` with an
800 ms break, leaving its text field empty. No client, credentials, live API
call, narration, or media was involved. The existing wrapper still supports
plain text only. Documentation establishes available controls, not successful
synthesis or measured pause accuracy in this project.

## Report relevance

This clarifies a production approach preserving the user-preferred voice and
separates documented Preview capabilities from deterministic local timing edits.
It introduces no mathematical result or implemented narration feature.
