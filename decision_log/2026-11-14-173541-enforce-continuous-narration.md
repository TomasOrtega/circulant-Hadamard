# Enforce one continuous narration take per scene

- Recorded at: 2026-11-14T17:35:41-08:00
- Observed work interval: 2026-11-14T17:26:35-08:00/2026-11-14T17:35:41-08:00 (546 seconds).
- Participants: Tomas Ortega (enforcement, simplification, and agent-instruction requests); Codex (GPT-6, implementation and checks); Google Cloud Gemini 2.5 Pro TTS (single Achird take); faster-whisper Base English (supporting cue alignment).

## Context and decision

The user accepted the [continuous-take recommendation](2026-11-14-172228-assess-chunk-voice-drift-and-articulation.md)
and requested enforcing it, simplifying the implementation, and updating the
corresponding agent instructions. Implement the rule in
[NarratedScene](../videos/narrated_scene.py) and
[speech.py](../narration/speech.py), and replace the chunk-based guidance in
[videos/AGENTS.md](../videos/AGENTS.md). The writing-for-agents skill informed
keeping the narration instructions short and avoiding duplicate QA wording.

A scene now rejects second and nested `narrate()` calls before synthesizing
another recording. The speech layer rejects a script exceeding one request
instead of silently splitting it. Retain the existing UTF-8 byte ceilings:
4,500 for Chirp and 4,000 for Gemini. Authors shorten the script or use separate
scenes when necessary. Remove automatic chunk joining, per-block delivery
presets, and `pause_after`; Gemini uses one shared neutral style prompt.

## Rationale

Sentence-sized synthesis introduced independently generated performances and
weakened voice continuity. Generate the entire [66-word script](../narration/achird-demo.txt)
in one take, then align visual cues to that finished recording. The new
`wait_until_narration(seconds)` helper schedules visuals against the original
audio start without stopping or restarting speech. Late cues do not rewind time.

Simplify the [demo preparation module](../narration/demo.py) to reuse the full-script
CLI. Model, voice, and prompt still identify the cache; original Chirp cache
keys and the shared Chirp default are preserved. The complete script and neutral
prompt are identical to those already explicitly approved for Google synthesis;
no new payload approval was requested.

## Evidence and outcome

Regression tests were added first and failed against both existing loopholes:
second/nested narration calls were accepted, and oversized text produced multiple
takes. After the changes, all 15 speech tests and 11 video tests passed. Coverage
includes both guards, Unicode byte boundaries, one full-script request, cache
reuse and invalidation, failed-take recovery, cue ordering, full exported speech,
title visibility, and the known order-four matrix identity.

Google generated one continuous Pro Achird WAV lasting about 17.89 seconds.
Local word alignment supplied visual cue offsets at 2.20, 4.10, 6.70, 9.35,
11.90, and 14.95 seconds. ASR is supporting timing evidence, not proof of audible
word clarity or voice quality. It reconstructed "are" around 8.18-8.36 seconds
and also produced uncertain tiny end tokens; these inferred alignments are not
accepted as a substitute for listening. The agent instructions explicitly
preserve that verification limitation.

The rebuilt [MP4](../videos/build/rendered/AchirdDemo.mp4) is H.264,
1920 by 1080 at 30 fps, lasting 17.900000 seconds. Its 44,100 Hz AAC track lasts
17.891995 seconds and covers the complete cached take. Rendering used offline
speech mode. The [WAV](../narration/build/achird-demo-neutral.wav) is the new
single take, and the previous video is preserved as
`videos/build/rendered/AchirdDemo-chunked.mp4`.

Inspected product and final frames. Offline preparation reports zero missing
requests. Ruff, formatting, `uv run --locked prek -a --quiet`, whitespace checks,
and local documentation links passed. Removed API references are absent from
current narration/video source and docs. No dependency change, website
publication, or Git commit was made.

## Report relevance

This implements user feedback about voice continuity and records the reversal
of sentence-by-sentence synthesis. It simplifies production tooling and keeps
human listening distinct from automated technical checks. It adds no
mathematical result or claim of human audio-quality approval.
