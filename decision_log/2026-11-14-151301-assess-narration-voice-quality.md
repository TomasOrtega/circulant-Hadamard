# Assess narration quality and recommend stock-voice auditions

- Recorded at: 2026-11-14T15:13:01-08:00
- Observed work interval: 2026-11-14T15:12:14-08:00/2026-11-14T15:13:01-08:00 (47 seconds).
- Participants: Tomas Ortega (quality and stock-voice questions); Codex (GPT-6, source checks and recommendation).

## Context and decision

Following the [free local option](2026-11-14-151008-free-local-voice-option.md),
the user asked how good Qwen3-TTS is and whether a default Google voice would
be better. Recommend auditioning Google Cloud Chirp 3 HD stock voices first
if reproducing the user's own voice is optional. This is an advisory refinement;
the user has not selected a final voice or authorized a billing upgrade.

## Rationale

The [Qwen technical report](https://arxiv.org/html/2601.15621v1)
reports strong speech accuracy, but that does not establish personal voice
likeness. An [independent evaluation](https://arxiv.org/abs/2610.23678)
finds strengths in intelligibility and weaknesses in prosody, with reference
transcription affecting cloning results. A separate
[long-form study](https://arxiv.org/abs/2609.16989)
documents reliability problems with lengthy prompts. Short, reviewed segments
would be prudent for a local narration experiment.

Stock voices avoid reference-recording preparation and local model installation.
[Google's pricing](https://cloud.google.com/text-to-speech/pricing)
currently includes one million Chirp 3 HD characters per month at no charge;
usage beyond that costs $30 per million. Cloud billing must be enabled.
These terms differ from paid AI Studio voice replication. Google also
[documents pronunciation and pacing controls](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd),
which are relevant to mathematical narration.

## Evidence and outcome

No audio was generated or listened to, and no personal cloning quality or Mac
inference speed was measured. No source establishes a direct quality ranking
between the proposed local MLX setup and Google for this user's scripts.
The recommendation concerns setup effort and auditioning cost, not a measured
superiority claim. The earlier browser check established that Cloud TTS is
already enabled. No account settings, packages, or website content changed.

## Report relevance

This is post-submission media-planning research. Distinguish published
evaluations from future listening tests with the team's actual narration.
