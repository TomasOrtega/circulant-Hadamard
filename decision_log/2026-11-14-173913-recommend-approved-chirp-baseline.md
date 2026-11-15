# Recommend returning to the approved Chirp baseline

- Recorded at: 2026-11-14T17:39:13-08:00
- Observed work interval: 2026-11-14T17:37:58-08:00/2026-11-14T17:39:13-08:00 (75 seconds).
- Participants: Tomas Ortega (listening feedback and strategy request); Codex (GPT-6, configuration review and recommendation).

## Context and decision

The user judged the [continuous Gemini take](2026-11-14-173541-enforce-continuous-narration.md)
worse than the original default Achird voice. Treat that listening judgment as
the production quality criterion. Recommend returning to the approved
[Chirp 3 HD Achird reference](2026-11-14-151823-audition-google-achird.md),
keeping its voice/model and normal rate fixed, while retaining one continuous
recording per scene. This is a strategy recommendation; no new recording or
code change was made in this turn.

## Rationale

The original sample uses `en-US-Chirp3-HD-Achird` at speaking rate 1.0.
The current [demo override](../narration/demo.py) instead selects short name
`Achird` with `gemini-2.5-pro-tts` and a style prompt. Switching synthesis
families to obtain expressive controls did not preserve the sound the user
preferred. Continuous synthesis addresses joins; it does not restore that
original voice performance.

Keep the successful baseline as the reference. Generate the full scene script
with default Chirp delivery, assess the standalone audio against that reference,
then cache the accepted take and align animations. Evaluate any future voice
or delivery change separately before adopting it. Automated tests and ASR are
supporting technical evidence, not a substitute for listening preference or
clear articulation.

## Evidence and outcome

Reviewed `Voice` defaults, the demo's explicit Gemini override, and prior voice
and production decisions. Measured script word counts and WAV durations for
the approved reference and the current demo. The requested speaking pace in a
Gemini prompt is an instruction, not evidence of achieved rate; the two takes
have different measured delivery rates as well as different model settings.
No credentials, dependencies, source configuration, or media were changed.
The current demo remains the Gemini take until the recommended change is made.

## Report relevance

This records another user quality assessment and a proposed return to a known
preferred production baseline. It separates voice identity/model choice,
continuity, actual pace, and subjective listening quality. It adds no
mathematical result or claim of a controlled voice-quality benchmark.
