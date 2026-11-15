# Restore natural pace and neutral narration

- Recorded at: 2026-11-14T17:00:47-08:00
- Observed work interval: 2026-11-14T16:55:57-08:00/2026-11-14T17:00:47-08:00 (290 seconds).
- Participants: Tomas Ortega (pace, tone, and shorter-guidance request); Codex (GPT-6, revisions, offline render, and checks).

## Context and decision

The user found the [82-second expressive demo](2026-11-14-165219-update-demo-narration-style.md)
far too slow and excited, preferring the original. Supersede that delivery choice:
restore the approved [Chirp recording](../narration/achird-math-sample.wav), its
[script](../narration/achird-math-sample.txt), and the original scene timing.
The main [demo MP4](../videos/build/rendered/AchirdDemo.mp4) is again about
26 seconds. Preserve the rejected version as
`videos/build/rendered/AchirdDemo-expressive-slow.mp4`.

Reduce narration instructions in [videos/AGENTS.md](../videos/AGENTS.md) to
three short bullets: natural pace and neutral delivery, concise scripts and
pauses, and slight emphasis used sparingly at the main insight. Keep API details
in the README. The writing-for-agents skill informed this pruning.

Optional Gemini controls now default to `neutral`, with an `insight` preset
for slight emphasis. Replace the earlier curious/deliberate/delighted prompts
with natural conversational pacing, approximately 175 words per minute.
These optional prompts were tested locally but have not been freshly synthesized
or assessed for audio quality. The final demo uses the original Chirp audio.

## Rationale

The user preferred the original delivery. Reusing its approved recording restores
both tempo and tone without another voice experiment. A first revision shortened
the seven-block Gemini script, but automatic approval review rejected synthesis:
the prior authorization covered the earlier text and prompts, and the reviewer
required fresh approval for the changed payload. No revised text was transmitted.
Continue with the existing recording locally; no additional permission was needed
for that alternative. Update the demo preparation command to import that WAV,
and make previews seed it automatically before rendering offline.

## Evidence and outcome

Added a media-length regression before the change: the 82.300-second export
failed its 35-second ceiling. After restoring the source and rendering offline,
all 16 speech tests and 10 video tests passed. They cover request construction,
cache invalidation and reuse, pause ordering, the approved recording's cache
identity, complete media duration, title visibility, full products, and the
known order-four matrix identity.

The new render is H.264, 1920 by 1080 at 30 fps, lasting 26.166667 seconds,
with 44,100 Hz AAC lasting 26.160998 seconds. It covers the full approved
recording. Reviewed extracted product and final frames. Ruff, formatting,
`uv run --locked prek -a --quiet`, whitespace checks, and local documentation
links passed. No new speech was synthesized, credentials changed, website video
published, or Git commit made.

## Report relevance

This records user feedback reversing an AI-assisted production choice after
submission. The previous expressive experiment remains documented. Validation
concerns media delivery and the known illustrative matrix, not a new proof of
the conjecture.
