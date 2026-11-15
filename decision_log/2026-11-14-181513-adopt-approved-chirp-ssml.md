# Adopt the accepted Chirp SSML recording and publish the workflow

- Recorded at: 2026-11-14T18:15:13-08:00
- Observed work interval: 2026-11-14T18:09:26-08:00/2026-11-14T18:15:13-08:00 (347 seconds; preparation through validation).
- Participants: Tomas Ortega (explicit audio acceptance, SSML agent-guidance request, and commit/push authorization); Codex (GPT-6, integration, validation, and publication preparation).

## Context and decision

The user liked the [Chirp SSML audition](2026-11-14-180446-audition-default-chirp-with-ssml.md)
and requested SSML breaks in the agent instructions, followed by committing and
pushing the changes. Adopt that exact recording in the demo and publish the
accumulated narration implementation and decision history on the existing main
branch. This is human acceptance of the audition, distinct from earlier
technical checks and rejected Gemini experiments.

## Rationale

[videos/AGENTS.md](../videos/AGENTS.md) now directs agents to put SSML
`<break time="..."/>` pauses in one complete `<speak>` script, keeping default
Chirp Achird settings, one full-script take, and visual timing based on the
accepted recording. Preserve the short narration guidance and ASR limitation.

Version the [accepted WAV](../narration/achird-demo.wav) alongside its
[SSML script](../narration/achird-demo.ssml). The helper imports it into the
cache, and previews seed that cache automatically. This makes a fresh checkout
reproduce the accepted voice without another synthesis request. Replace the
demo's Gemini override with default Chirp and SSML input, then measure cues from
the accepted take. Keep scripts and their versioned recordings paired.

## Evidence and outcome

The versioned recording is byte-identical to the user's audition: 2,243,872 bytes,
25.440227 seconds, mono 16-bit PCM at 44,100 Hz. SHA-256:
`3ae03b14151b30cecc9179a5fd146f298972e4d5c1d1623c1ac5adc90e91c5cf`.
An empty-cache offline import reproduced those exact bytes, and the helper made
no Google calls during this work.

A regression first showed that import-only dry runs incorrectly reported an
uncached synthesis request. Correct the count to zero and retain the regression.
A second regression failed against the previous Gemini video because speech
played during the expected SSML pause. With the accepted take and retimed scene,
all 20 speech tests and 12 video tests passed. These include the one-take guards,
SSML fields and validation, cache identity, complete exported audio, actual
pause silence, frame checks, and the known order-four matrix identity.

The rebuilt local MP4 is H.264, 1920 by 1080 at 30 fps, lasting 25.466667 seconds;
its 44,100 Hz AAC track lasts 25.440998 seconds. Checked the product/pause and
final layouts. Ruff, formatting, `uv run --locked prek -a --quiet`, whitespace,
and documentation checks passed. Generated renders and caches stay ignored;
the approved WAV is a source asset like the original audition.

A fresh fetch found three remote commits adding website work. Their files did
not overlap these changes, so fast-forward local main from 5ab4412 to 5430e84
before publication. Include only narration/video changes and their new decision
records in the requested feature commit. Use conventional commits with the
`Assisted-by: Codex:GPT-6` trailer. Record the observed commit and push outcome
in a follow-up publication record.

## Report relevance

This records the user's final voice preference, adoption of SSML pauses,
reproducible offline media preparation, and authorized publication. The retained
decision history distinguishes unsuccessful experiments from the accepted
result. No new mathematical result or website video is claimed.
