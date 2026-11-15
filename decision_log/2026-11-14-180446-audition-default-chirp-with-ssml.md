# Audition default Chirp Achird with an SSML pause

- Recorded at: 2026-11-14T18:04:46-08:00
- Observed work interval: 2026-11-14T17:59:16-08:00/2026-11-14T18:04:46-08:00 (330 seconds).
- Participants: Tomas Ortega (explicit SSML trial request); Codex (GPT-6, implementation, synthesis, and technical checks); Google Cloud Chirp 3 HD Achird (SSML synthesis); faster-whisper Base English (supporting transcript positions).

## Context and decision

The user requested trying SSML after the [pause-control explanation](2026-11-14-175133-chirp-pauses-with-one-take.md).
Implement explicit SSML input and audition the audio before changing animation
timing, following the [baseline-first strategy](2026-11-14-173913-recommend-approved-chirp-baseline.md).
Keep the original Chirp Achird voice, speaking rate 1.0, mono LINEAR16 at
44,100 Hz, and one full-script synthesis request.

The [SSML script](../narration/achird-demo.ssml) preserves the existing spoken
words and inserts one `<break time="800ms"/>` before "The sum is zero."
Use no pitch, emotion, or Gemini prompts in this audition. Retain the existing
video for comparison pending the user's assessment of this standalone take.

## Rationale

SSML must enter the SDK through `SynthesisInput.ssml`, rather than the text
field. Add `Narrator(ssml=True)`, CLI `--ssml`, and the scene-level
`narration_ssml` option. Distinguish SSML from plain text in cache keys and
include the actual XML, so pause changes invalidate a take while existing
plain-text Chirp recordings keep their cache identities.

Validate well-formed XML, a `<speak>` root, spoken content, the complete byte
limit including markup, and a single selected voice before requesting audio.
Reject SSML with Gemini settings. Agent guidance now names the approved
`en-US-Chirp3-HD-Achird` default explicitly, and the README documents the trial
command. No per-sentence synthesis or automatic stitching was introduced.

## Evidence and outcome

Four new SSML tests first failed because the constructor lacked SSML support.
After implementation, all 19 speech tests and 11 video tests passed. Coverage
includes actual SDK SSML fields with a mocked transport, one Chirp request,
normal pace, cache separation and reuse, pause invalidation, XML and voice
validation, request-size accounting, and existing one-take enforcement.

The live Google request succeeded with Chirp SSML. The
[audition WAV](../narration/build/achird-demo-ssml.wav) contains mono 16-bit PCM
at 44,100 Hz and lasts 25.440227 seconds. An offline dry run reports zero missing
requests. The measured quiet interval before the zero result is approximately
1.205 seconds, from 8.861746 to 10.066893 seconds using FFmpeg silencedetect at
-40 dB. This is the total quiet gap around the sentence boundary, not proof
that the SSML tag alone produced exactly 800 ms.

Local ASR reconstructed the intended main text, but also repeated a tiny "row"
end token. Its output is supporting evidence only; audible clarity and timbre
remain for the user's listening assessment. Audio was not sent to another
service for transcription. No new video was rendered or quality approval
claimed in this trial.

Ruff, formatting, `uv run --locked prek -a --quiet`, whitespace checks, and
local documentation links passed. No dependency, credential, website, or Git
commit change was made.

## Report relevance

This is a successful live SSML capability trial with measured media and pause
evidence, distinct from human voice-quality assessment. It implements the
user-requested experiment using the previously preferred voice family. It adds
no mathematical result.
