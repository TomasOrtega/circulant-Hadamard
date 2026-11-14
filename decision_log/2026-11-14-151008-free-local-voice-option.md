# Recommend a free local voice-cloning option

- Recorded at: 2026-11-14T15:10:08-08:00
- Observed work interval: 2026-11-14T15:09:34-08:00/2026-11-14T15:10:08-08:00 (34 seconds of source checks).
- Original request and billing-cancellation times: unknown, before the measured source-check interval.
- Participants: Tomas Ortega (free-option request); Codex (GPT-6, browser cancellation and source checks).

## Context and decision

The user withdrew the paid route in the
[Google setup assessment](2026-11-14-151008-google-voice-setup-assessment.md)
and asked for a free third option. Cancel the pending Google billing dialog
and recommend local Qwen3-TTS through MLX Audio for evaluation. The user has
not yet selected or installed the local option.

## Rationale

The [Qwen Base model](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base)
supports voice cloning and carries an Apache 2.0 license. The
[MLX Audio instructions](https://github.com/Blaizzy/mlx-audio/blob/main/mlx_audio/tts/models/qwen3_tts/README.md)
describe cloning with reference audio and its exact transcript. The available
[MLX conversion](https://huggingface.co/mlx-community/Qwen3-TTS-12Hz-0.6B-Base-bf16)
offers a local path for Apple silicon, without a metered synthesis service.
Chatterbox was also considered; Qwen's documented MLX path fits this Mac.

## Evidence and outcome

`uname -m` returned `arm64`; uv, FFmpeg, and afconvert are available. Sandbox
restrictions prevented the hardware-memory query, so capacity and generation
speed remain unverified. No packages or model weights were installed, and no
voice likeness or audio quality was tested. A clean recording and its
transcript are still needed for a personal-voice test.

Firefox visibly returned to the AI Studio speech landing page after canceling
billing and closing the paid replication dialog. No billing upgrade or payment
was submitted, and no voice recording was uploaded. Downloads, local resource
use, and listening checks remain work for a subsequent setup step.

## Report relevance

This records a user-directed change in media tooling, not a completed narration
experiment. Findings come from publisher and implementation documentation;
local inference has not been verified. The interval follows the earlier
assessment and is not a measure of total person-hours.
