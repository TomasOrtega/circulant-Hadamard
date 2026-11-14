# Assess Google voice cloning for video narration

- Recorded at: 2026-11-14T15:10:08-08:00
- Observed work interval: 2026-11-14T15:05:41-08:00/2026-11-14T15:09:34-08:00 (3 minutes 53 seconds).
- Original decision times: unknown within the observed interval; recorded retrospectively.
- Participants: Tomas Ortega (request and route selection); Codex (GPT-6, documentation and account checks); Gemini (earlier advice supplied by the user; model unknown).

## Context and decision

The user requested narration resembling his own voice for the project's
[overview videos](2026-11-14-005903-overview-video-cuts-and-scripts.md), using
Google if practical. Check the supplied Gemini instructions against current
documentation and the signed-in account before recording or generating audio.
The user initially selected AI Studio after learning its billing requirement.

## Rationale

[Chirp Instant Custom Voice](https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice)
requires allowlisting through Google sales. Its documented consent script
omits the extra word "custom" supplied by Gemini; the request field is
`consent_script`, rather than Gemini's `consent_text`.
[AI Studio voice replication](https://ai.google.dev/gemini-api/docs/voice-replication)
provides a browser workflow without that separate allowlist, but requires a
paid-tier API project.

## Evidence and outcome

Firefox showed Cloud Text-to-Speech already enabled and an unused $300 trial
credit. AI Studio offered Voice Replication but required a paid API key.
Its billing dialog warned that proceeding would upgrade the trial billing
account and that trial credit excludes Gemini API. No upgrade, payment,
credential creation, audio upload, or synthesis was performed. Local `gcloud`
was unavailable; plugin discovery found no direct Cloud TTS connector.
The website contains draft scripts and video slots, without a speech-generation
pipeline or supplied voice recordings.

## Report relevance

This was post-submission media preparation and AI-assisted verification of
another AI's setup advice. No mathematical claims or published media changed.
The user's subsequent free-option request is recorded in the
[follow-up decision](2026-11-14-151008-free-local-voice-option.md).
