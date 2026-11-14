# Audition Google Achird for mathematical narration

- Recorded at: 2026-11-14T15:18:23-08:00
- Observed work interval: 2026-11-14T15:15:55-08:00/2026-11-14T15:18:23-08:00 (148 seconds).
- Participants: Tomas Ortega (voice selection); Codex (GPT-6, script preparation, browser generation, and file checks); Google Cloud Chirp 3 HD (Achird speech synthesis).

## Context and decision

The user selected Achird after the
[stock-voice recommendation](2026-11-14-151301-assess-narration-voice-quality.md).
Generate a short mathematical narration sample using English (United States),
Chirp 3 HD, and Achird. Retain the console's default pace and LINEAR16 output
at 44,100 Hz for an initial audition.

The [403-character, 71-word transcript](../narration/achird-math-sample.txt)
introduces sign entries, orthogonal rows, cyclic shifts, and the spoken
equation H times H transpose equals n times the identity. It presents
background definitions, without claiming a proof of the conjecture.

## Rationale

An actual excerpt tests mathematical names and pacing more directly than
Google's generic voice preview. The selected stock voice needs no personal
recording or cloning approval.
[Google documents Achird and Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd);
its [current pricing](https://cloud.google.com/text-to-speech/pricing)
includes one million Chirp 3 HD characters monthly at no charge.

## Evidence and outcome

The signed-in Cloud console visibly confirmed Chirp 3 HD, Achird, and US
English, then returned a 26.2-second player. Export completed as speech.wav.
Copied it without changes to the
[local audition WAV](../narration/achird-math-sample.wav).

The exported file contains 1,153,666 complete mono PCM frames at 44,100 Hz,
16 bits per sample: 26.160 seconds and 2,307,376 bytes. Signal checks found
nonzero audio and six full-scale samples out of 1,153,666. File bytes match
the export. These checks establish a valid audio artifact, not pronunciation
or listening quality; the user's audition remains pending.

No payment, billing upgrade, or credential creation was needed. This is a
voice audition, not approval to use Achird for every video. No video was
produced or published.

## Report relevance

This is post-submission, AI-assisted media preparation. Preserve the transcript,
voice settings, and generated sample as evidence. Do not present waveform
checks as human evaluation of narration quality.
