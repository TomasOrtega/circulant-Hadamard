# Ignore empty SSML pause paragraphs

- Recorded at: 2026-11-15T07:11:51-08:00.
- Observed diagnosis and correction span:
  2026-11-15T07:10:32-08:00/2026-11-15T07:11:51-08:00 (79 seconds,
  overlapping other scene checks).
- Participants: OpenAI Codex, GPT-6.

## Context and decision

The full video check for the new
[vanishing-sum video](2026-11-15-070647-finalize-vanishing-alternating-sum-video.md)
counted eleven direct XML children instead of its six spoken paragraphs.
Five valid top-level SSML breaks created five empty text entries. An earlier
alignment attempt failed on the same mismatch; the ignored alignment and
audit helpers filtered empty entries to reuse the cached transcript.

Fix `spoken_paragraphs` to omit empty extracted text, preserving all spoken
words and internal pause word boundaries. Have the published-video integration
check count spoken paragraphs rather than raw XML elements. Keep the frozen
SSML, recording, timestamps and caption file unchanged.

## Rationale

A pause contributes timing but contains no caption text or paragraph cue.
Filtering empty extracted entries supports valid pauses between paragraphs
without rearranging a frozen synthesis request or generating another take.

## Evidence and outcome

Before the fix, the focused regression returned five entries, three empty,
instead of the two expected spoken paragraphs. It failed as expected; the
existing published-video integration check independently reproduced the
eleven-versus-six mismatch. After the fix all eight caption tests pass,
including internal pause boundaries, exact words, wrapping and timing.
Logs are retained in ignored `videos/build/vanishing-caption-break-{red,green}.log`.
The complete video suite is being rerun for final acceptance.

## Report relevance

Documents a parser correction discovered while producing an existing proof
video. It changes caption extraction semantics for silent elements and does
not change narration, mathematics or the editorial script.

Final acceptance at 2026-11-15T07:13:23-08:00: all 20 narration and
41 video tests pass; the published-video integration check now accepts the
six spoken paragraphs and unchanged exact captions.
