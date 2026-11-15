# Apply expressive narration guidance to the demo

- Recorded at: 2026-11-14T16:52:19-08:00
- Observed work interval: 2026-11-14T16:44:01-08:00/2026-11-14T16:52:19-08:00 (498 seconds).
- Participants: Tomas Ortega (narration update request and explicit Google synthesis approval); Codex (GPT-6, script, implementation, rendering, and checks); Google Cloud Gemini 2.5 Flash TTS (Achird audio).

## Context and decision

The user requested updating the demo narration with the new
[delivery guidance](2026-11-14-160517-document-narration-direction.md).
Implement the [expressive narration proposal](2026-11-14-160253-expressive-narration-and-pauses.md)
and apply it to [AchirdDemo](../videos/achird_demo.py).

Use seven short [script blocks](../narration/demo.py), separating curious
questions, deliberate mathematical explanations, and restrained delight at
reveals. Each block finishes speech and animations before its explicit teaching
pause. Hold the zero result until after the question's two-second pause.
The script preserves the known order-four example and its cyclic correlations.

Opt this demo into Gemini Achird through the existing Google SDK. Preserve
Chirp Achird as the shared default, its original approved WAV and script, and
its existing cache identity. New Gemini recordings are generated examples for
review; synthesis approval does not establish a new shared voice preference.

## Rationale

The original single recording could not express separate delivery cues or
place exact silence between deductions. The implemented
`narrate(text, delivery="curious", pause_after=2)` keeps silence on the scene
timeline, so changing pauses reuses speech. Optional Gemini requests supply
short voice name `Achird`, an explicit model, and a separate style prompt.
Model and resolved prompt enter expressive cache keys; Chirp retains version-one
keys for offline reuse of its approved recording.

Checked the current [Google Gemini TTS guide](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts).
It documents Gemini 2.5 Flash and Pro, Achird, separate prompt fields, 4,000-byte
UTF-8 limits for each text and prompt field, and the model permission requirement.
Use those limits for Gemini while retaining the existing 4,500-byte Chirp
splitter. Unsupported delivery/model settings fail before creating a client.

Update the video README, Make targets, and agent guidance to describe the
implemented controls. `seed` generates missing demo clips; `preview` uses only
cached speech. The writing-for-agents skill informed the instruction update.

## Evidence and outcome

New feature tests first failed against the earlier API because `model_name`
was unsupported. After implementation, all 16 speech tests and 10 video tests
passed with `make -C videos check`. Coverage includes actual SDK request fields
with a mocked transport, Unicode chunk limits, prompt/model cache invalidation,
pause ordering for shorter and longer animations, unchanged speech reuse after
pause edits, the original Chirp cache key, and exported media.

Automatic approval review initially rejected Google synthesis because it
required explicit approval for the script and destination. The user approved
sending the seven math narration blocks to Google Cloud using the configured
credentials, including normal synthesis charges. Only then did live synthesis
proceed. The question and reveal were generated first, followed by the other
five blocks. A subsequent offline preparation reused all seven cached WAVs.
Credentials were neither displayed nor changed.

The first staged reveal incorrectly indexed `Tex` glyphs instead of selecting
its isolated text parts. A rendered regression check failed with only 86 bright
pixels in the formula region. Switching to `get_part_by_tex` displayed the
complete products and then the zero result; the corrected frame contains 2,629
bright pixels there. The final check uses a resolution-independent proportion.
This issue was introduced and corrected during this task.

Both renders used cached audio with network synthesis disabled. The final
[local MP4](../videos/build/rendered/AchirdDemo.mp4) is H.264, 1920 by 1080,
30 fps, with 44,100 Hz AAC. Its video lasts 82.300 seconds and audio lasts
80.492 seconds; the remaining 1.8 seconds are the final silent teaching pause.
The duration check distinguishes complete speech from final video silence.
An FFmpeg PCM check confirms silence within the question's thinking pause.

Inspected extracted question, reveal, identity, and final frames. Pixel checks
confirm title visibility and full products before the answer. The exact matrix
dot-product check still gives `H H^T = 4 I`. Preserved the previous render at
`videos/build/rendered/AchirdDemo-chirp.mp4` and assembled a short WAV audition
with the question, two-second pause, and reveal at
`narration/build/achird-style-audition.wav`. Generated media and speech caches
remain ignored. Audio timbre has not received a new human quality approval.

`uv run --locked prek -a --quiet`, explicit Ruff checks including the new demo
module, formatting checks, and whitespace checks passed after routine formatting.
No website video was published and no commit was requested.

## Report relevance

This is post-submission, AI-assisted media production work implementing the
user's narration guidance. Its evidence includes live speech generation,
offline rendering, timeline tests, frame inspection, and one corrected visual
regression. The known order-four example is illustrative computation, not a
new proof of the conjecture or a completed proof video.
