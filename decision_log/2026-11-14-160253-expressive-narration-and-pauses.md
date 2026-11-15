# Plan expressive narration and deterministic teaching pauses

- Recorded at: 2026-11-14T16:02:53-08:00
- Observed work interval: 2026-11-14T16:00:49-08:00/2026-11-14T16:03:12-08:00 (143 seconds; main repository inspection, source checks, and recommendation review).
- Observed research interval: 2026-11-14T16:01:05-08:00/2026-11-14T16:02:53-08:00 (108 seconds; overlaps the main architecture discussion and is not additive person-hours).
- Participants: Tomas Ortega (architecture request); Codex (GPT-6, main agent and background documentation researcher); Google documentation (sources only; no synthesis).

## Context and decision

The user asked how to improve narration delivery and add pauses to the
[ManimGL narration setup](2026-11-14-154431-programmatic-achird-narration.md).
This is a proposed architecture, not an implementation or a voice change.
Retain the approved Chirp 3 HD Achird default until another model is auditioned.

In [NarratedScene](../videos/narrated_scene.py), audio starts on entry and
continues during every animation or `self.wait()` inside the block. A wait
between completed narration blocks already creates a teaching pause. Propose
`narrate(text, delivery="curious", pause_after=2)` as a convenience: finish both
audio and animations using the existing duration logic, then wait two seconds.
For a standalone WAV needing exact silence, insert a measured number of zero
PCM frames locally. These choices make the requested additional silence
independent of model interpretation; generated clips can retain natural
leading or trailing silence.

## Rationale

Use a Cloud Gemini TTS option through the existing SDK when emotion is needed.
Keep delivery instructions separate from spoken mathematics. A proposed request
uses the following shape, with the existing client and caching surrounding it:

```python
response = client.synthesize_speech(
    input=texttospeech.SynthesisInput(text=spoken_text, prompt=delivery_prompt),
    voice=texttospeech.VoiceSelectionParams(
        language_code="en-US", name="Achird", model_name="gemini-2.5-flash-tts"
    ),
    audio_config=texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
    ),
    retry=None,
    timeout=120,
)
```

For example, `delivery_prompt` could ask for warm, curious US English
mathematics narration, measured phrasing, and gentle emphasis on new ideas.
Google's [Cloud Gemini guide](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts)
documents the separate prompt, short voice name, and explicit model selection.
Its models include Achird and the 2.5 Flash and Pro options. The shared name
does not establish identical delivery across model families; re-audition it.
No new Agent Platform dependency is needed for this option.

Include provider/model, input kind, prompt, voice, language, rate, sample rate,
and cache format version in audio cache keys. Keep `pause_after` in the scene
timeline so changing it reuses speech. Use model-specific chunk limits: Cloud
Gemini allows 4,000 UTF-8 bytes each for text and prompt, up to 8,000 combined;
the current 4,500-byte text splitter is unsuitable for that model. The same
guide requires `aiplatform.endpoints.predict`; existing access was not checked.

## Evidence and outcome

- Current [speech.py](../narration/speech.py) uses `en-US-Chirp3-HD-Achird`,
  `SynthesisInput(text=...)`, LINEAR16 at 44,100 Hz, and rate 1.0. It supplies
  neither a Gemini model nor a prompt. The installed SDK is 2.38.0.
- The [Chirp family guide](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd#chirp_3_hd_ssml_support),
  updated November 10, 2026, lists Preview synchronous SSML support including
  `<break>` and `<prosody>`. Unlisted tags are ignored; `<mark>` is absent.
  Its Preview `[pause short]`, `[pause long]`, and `[pause]` controls require
  `input.markup`, not `input.text`, and have contextual, potentially ignored
  durations. The [generic voice page](https://docs.cloud.google.com/text-to-speech/docs/list-voices-and-types)
  still says Chirp lacks SSML and speaking-rate support. Prefer the specific
  family guide provisionally; this discrepancy was not settled by a live call.
- Generic [SSML documentation](https://docs.cloud.google.com/text-to-speech/docs/ssml#break)
  defines `<break time="250ms"/>` and `<break time="2s"/>`. These are an optional
  Chirp experiment, not evidence of measured timing accuracy. Do not assume
  generic SSML or emotion tags work on every Google voice family.
- The [Cloud Gemini markup guide](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts#markup_tag_guide)
  marks stage tags Preview and warns that emotional adjectives such as
  `[curious]` can themselves be spoken. Prefer the prompt for overall emotion;
  audition any localized tags. Its documented Gemini input is text plus prompt;
  no source checked promises Gemini SSML timepoints or exact pause durations.
- [SSML timepoints](https://docs.cloud.google.com/text-to-speech/docs/ssml#ssml_timepoints)
  report offsets at `<mark>` tags. The [v1beta1 synthesis API](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/text/synthesize)
  requests `enableTimePointing=["SSML_MARK"]` and returns `timepoints`. This is
  not a documented timing solution for the approved Chirp voice, whose tag list
  omits `<mark>`, or for the proposed Gemini path.
- Local construction and serialization succeeded for SDK request objects with
  `input.prompt`, short name `Achird`, a Gemini model, and LINEAR16 at 44,100 Hz.
  Schema inspection confirmed that the current v1 request/response lack
  timepoint fields, whereas v1beta1 has them. These checks validate local
  schema only: no client was created, credentials inspected, or paid API called.

If implemented, add regression coverage for scene pause ordering, unchanged
speech-cache reuse after pause edits, prompt/model cache invalidation, and
Gemini byte limits. Generate a short audition only after opting into the model,
then review it and reuse its cache for offline scene previews. No narration,
scene, dependency, or credential configuration changed during this research.

## Report relevance

This is post-submission, AI-assisted production architecture research. Evidence
consists of repository inspection, first-party documentation, and local SDK
schema checks, not generated-audio quality or synchronization measurements.
It adds no mathematical result and publishes no video.
