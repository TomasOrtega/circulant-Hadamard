# Publish the final Hadamard Dictionary video

- Recorded at: 2026-11-14T23:02:07-08:00
- Observed work interval: 2026-11-14T22:36:39-08:00/2026-11-14T23:02:07-08:00 (chronology includes parent authoring, delegated production, and authorization waits; intervals overlap other production work).
- Participants: Tomas Ortega (requested final videos and explicitly approved Google narration); OpenAI Codex, GPT-6 (primary integration and delegated scene authoring/review); Google Chirp 3 HD Achird (one full-script take); faster-whisper Base English (local alignment).

## Context and decision

Complete [the supplied dictionary script](../website/scripts/node1/hadamard-dictionary.md)
as a final teaching video with [ManimGL source](../videos/hadamard_dictionary.py),
one [complete SSML recording](../videos/scripts/hadamard-dictionary.ssml),
[MP4](../website/media/hadamard-dictionary.mp4), and
[WebVTT captions](../website/media/hadamard-dictionary.vtt).
The user's updated goal requires finished videos, 3Blue1Brown-style mathematical
animation, and room for subtitles. Remove the earlier shared draft footer and
use the primary agent's subtitle-safe camera framing. Preserve the sign
hypothesis and both implications of the lemma; do not change the editorial draft.

## Rationale

Connect each nonconstant polynomial coefficient to a highlighted shifted row,
then fade its zero contribution while retaining the constant norm. Demonstrate
the converse with simultaneous common shifts of rows 1 and 3 into rows 0 and 2;
keep the relative offset visible and reindex the general dot-product formula.
Branch the sign hypothesis into its norm and matrix-entry roles. Show the
concrete 2I counterexample and the all-ones matrix with its non-diagonal Gram
entries. Measured intra-section beats keep these transformations aligned to
spoken claims instead of exposing the entire calculation at once.

## Evidence and outcome

The 2,752-byte approved SSML produced one 195.400227-second take. Initial
synthesis was rejected by automatic approval review because Google payload
transmission had not been recognized as authorized. The primary agent obtained
the user's explicit response “Approve Google narration” for these exact files
and destination; its exact clock time was not separately captured by the
delegated agent. The delegated executor still could not resolve Google DNS;
the primary executor generated the approved recording. A delegated offline GPU
audit also found no exposed Metal adapter, so the primary executor rendered it.
Neither rejected nor failed child request produced an additional recording.

The final H.264 MP4 is 1920 by 1080 at 30 fps and lasts 195.433333 seconds.
Its 195.400998-second AAC track covers the whole recording. The primary agent's
full-frame check covers all 5,863 frames: maximum luma in the bottom 20 percent
is 16, the encoded black level. Reviewed ten representative rendered frames,
including both sides of the common shift, coefficient cancellation, reindexing,
the sign roles, both counterexamples, and the closing equivalence. No draft
label, clipping, or lingering animation target was observed.

Independent arithmetic checks cover all 126 sign rows of lengths 1–6 and every
pair of their circulant rows. They confirm the displayed coefficient/Gram
identity and dictionary equivalence, the explicit simultaneous shift, and both
order-four counterexamples. These finite checks support the illustrations;
the general proof remains the supplied elementary argument. Ruff formatting
and lint pass. Source, SSML, and exported-media hashes match the
[production metadata](../videos/production/hadamard-dictionary.json).
Captions reproduce the spoken source exactly, with at most two 42-character
lines per cue. ASR match ratio is 0.9426; this supports timing and wording but
is not independent human listening acceptance. Voice settings match the
approved continuous Achird workflow. Root will run integration checks and
commit/push this video's files separately.

Primary integration at 2026-11-14T23:08:28-08:00: all20 narration tests,23 video tests,
and87 website tests pass; the website build emits22 pages. Repository lint
and whitespace checks run before the separate commit and push.

## Report relevance

Records final mathematical exposition, its actual recording and rendering
outcomes, bounded arithmetic verification, visual review, the authorization
boundary, and the difference between synthesis consent and listening approval.
It adds no new theorem or independent verification of the larger conjecture.
