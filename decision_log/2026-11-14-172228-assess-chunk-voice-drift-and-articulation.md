# Assess voice drift and unclear articulation

- Recorded at: 2026-11-14T17:22:28-08:00
- Observed work interval: 2026-11-14T17:20:30-08:00/2026-11-14T17:22:28-08:00 (118 seconds).
- Participants: Tomas Ortega (listening feedback and explanation request); Codex (GPT-6, source inspection and evidence review); faster-whisper Base English (local word alignment).

## Context and decision

The user reported voice changes between chunks and heard "distinct rows
orthogonal" rather than "distinct rows are orthogonal" in the
[fresh demo](2026-11-14-171222-regenerate-neutral-demo-narration.md).
Investigate the source and clarify the limits of the earlier verification.
This turn diagnoses the problem; it does not change or regenerate the audio.

## Rationale

[demo.py](../narration/demo.py) synthesizes seven short clips independently.
All use Gemini 2.5 Pro Achird; six share a neutral prompt and the final clip
uses an insight prompt. Each request supplies only its own text, not surrounding
spoken context. Independent performances and the changed final prompt are the
likely explanation for perceived delivery/timbre discontinuity. This is an
inference from the implementation and listening feedback, not a measured
speaker-identity analysis. Google's [Gemini TTS guide](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts)
describes prompt control over style, accent, pace, tone, and expression.

The source explicitly says "The sum is zero. Distinct rows are orthogonal."
[NarratedScene](../videos/narrated_scene.py) plays that complete WAV without
cutting or editing individual words. The question is therefore articulation
or fidelity of the generated recording, rather than an omitted source word.

## Evidence and outcome

The earlier Tiny and Base ASR transcripts both reconstructed "are". A fresh
local Base English word alignment without a mathematical vocabulary prompt
again assigned "are" an estimated 1.48-1.78-second interval in that raw clip.
ASR recognition and alignment can infer expected grammar; they cannot settle
whether the word was omitted, reduced, or perceptually merged into "orthogonal".
The user's listening report remains evidence of inadequate audible clarity.

Factual clarification of the earlier delivery claim: successful transcript,
format, duration, and frame checks do not establish consistent voice identity
or clearly articulated verbatim speech. The prior response relied too heavily
on automated transcription. No new synthesis, dependency change, or media edit
was performed here.

Recommend a single continuous take for this short narration, with animation
cues aligned afterward, rather than independently generated sentence clips.
This recommendation is not implemented or claimed to guarantee perfect delivery.

## Report relevance

This records user quality feedback and a limitation of ASR-based verification.
It distinguishes written input, synthesized audio, automated inference, and
human listening. It adds no mathematical result.
