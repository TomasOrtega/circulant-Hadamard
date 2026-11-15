# Regenerate the demo with brief neutral narration

- Recorded at: 2026-11-14T17:12:22-08:00
- Observed work interval: 2026-11-14T17:02:28-08:00/2026-11-14T17:12:22-08:00 (594 seconds).
- Participants: Tomas Ortega (fresh narration/video request and explicit Google synthesis approval); Codex (GPT-6, script, generation, verification, and rendering); Google Cloud Gemini TTS (Flash trials and final Pro Achird); faster-whisper (local transcript checks).

## Context and decision

After the [pace and tone correction](2026-11-14-170047-restore-neutral-narration-pace.md),
the user explicitly requested newly generated narration and video with the new
guidelines. Replace the reused Chirp recording in the demo with seven fresh
[script blocks](../narration/demo.py), totaling 66 words. Six blocks use neutral
delivery; only the final cyclic-correlation insight uses slight emphasis.
Added silence is limited to 0.4 seconds before the zero result and 0.2 seconds
at the end. Preserve the original approved Chirp sample and shared voice default.

Use Gemini 2.5 Pro Achird for this demo after rejecting Flash outputs containing
unscripted speech. Keep the short narration guidance; add one sentence to the
existing video QA instructions requiring spoken-word checks against the script.

## Rationale

The user requested a fresh performance rather than another restoration. Separate
short blocks synchronize definitions, products, the zero result, cyclic shifts,
the identity, and the final insight. Bound animation times against each clip's
duration to maintain a concise timeline. Select isolated TeX parts for the
products and result, retaining the earlier formula-display correction.

Automatic approval review initially rejected synthesis because it required
approval for the revised payload and Google destination. Presented the complete
script and delivery directions; the user explicitly approved sending them to
Google Cloud Text-to-Speech with existing credentials and normal TTS billing.
The subsequent Pro requests used the same approved text and prompts at that
same destination. Credentials were neither displayed nor changed.

## Evidence and outcome

Flash generated 29.85-, 27.17-, and 45.25-second clips for three short lines.
Local transcripts showed the intended sentence followed by unrelated generated
mathematical exposition. Reject those recordings and move them out of the
reusable cache into `narration/build/rejected-flash/`. Cancel the pending Flash
preparation request. These additions are rejected model output, not project
mathematical claims. Correct Flash samples were also excluded from the final
video to keep the voice model consistent.

A Pro sample spoke only the requested entry sentence in 1.93 seconds. Generate
all seven Pro blocks, then review local transcripts. Tiny English ASR confused
some mathematical vocabulary; a second Base English model with a short
mathematical vocabulary prompt recognized the intended terms. The resulting
transcripts contain the approved sentences, with number formatting, punctuation,
and a then/than homophone difference. This is an automated content check, not
human approval of timbre or a guarantee of perfect pronunciation.

ASR ran locally with public downloaded weights; audio was not uploaded to an
additional service. Its initial PyAV decoding failed, so FFmpeg supplied raw
samples instead. These temporary tools and weights remain in ignored caches;
project dependencies were unchanged. Transcripts are retained under
`videos/build/neutral-narration-transcripts.json` and
`videos/build/neutral-narration-base-transcripts.json`.

Rendered offline from the verified Pro cache. The final
[MP4](../videos/build/rendered/AchirdDemo.mp4) is H.264, 1920 by 1080 at 30 fps,
lasting 20.333333 seconds, with 44,100 Hz AAC lasting 20.104989 seconds.
The standalone [WAV](../narration/build/achird-demo-neutral.wav) lasts
20.078254 seconds, including both explicit pauses. Video timing includes frame
rounding. The original Chirp render remains available locally.

All 16 speech tests and 11 video tests passed. Export checks cover complete
speech, the 35-second ceiling, title visibility, full products before the result,
and actual silence in the short pause. Existing exact dot-product checks still
verify the known order-four matrix. Inspected product and final frames.
Offline narration preparation reused all seven clips. Ruff, formatting,
`uv run --locked prek -a --quiet`, and whitespace checks passed.

## Report relevance

This is post-submission, AI-assisted media production following user feedback.
It records both fresh synthesis and a content-quality failure discovered during
verification. The model switch and local transcript review prevent unscripted
mathematics from entering the demo. It adds no mathematical result, published
website video, or Git commit.
