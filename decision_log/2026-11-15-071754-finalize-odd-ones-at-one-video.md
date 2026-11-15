# Finalize the value-at-one video

- Recorded at: 2026-11-15T07:17:54-08:00.
- Observed production interval: 2026-11-15T07:06:29-08:00–2026-11-15T07:17:54-08:00
  (685 seconds, including coordinating-agent narration/rendering).
- Observed author export review: 2026-11-15T07:16:27-08:00–2026-11-15T07:17:54-08:00
  (87 seconds; overlaps theorem review and is not additive person-hours).
- Participants: user (standing final-video request); Steven Creech (editorial
  source); Codex/GPT-6 (authoring and coordinating production); Google Chirp 3
  HD Achird (one complete take); local ASR (supporting alignment).

## Context and decision

Accept the finished [OddOnesAtOne video](../website/media/odd-ones-at-one.mp4)
after the [preparation decision](2026-11-15-071025-prepare-odd-ones-at-one-video.md).
Keep the canonical script unchanged and its mathematical inputs explicit.
Freeze scene/layout hashes in the [production metadata](../videos/production/odd-ones-at-one.json).
The coordinating agent owns independent review, repository checks, website
attachment, and the separate publication commit.

## Rationale

The native export clearly separates the exact count `J(1)=9` from the residue
panel. Four pairs disappear there, leaving four zeros and one highlighted
one without surviving pair frames. The general odd count then has residue
one. Both reversed and ordinary coefficient sums evaluate to the same real
value at one before the norm square gives the two possibilities `±u`.

The final slide retains the evaluation ring and unit denominator through
the exact quotient. The two signed numerical examples precede reduction;
both signs then give residue one. The empty-subset card includes its input,
positive alternating sign, and normalized contribution. No sign row or
order-36 matrix is presented as an existence example.

## Evidence and outcome

- One unchanged 2,011-byte, 334-word Achird SSML take lasts 135.320227 seconds.
  Three paragraph cues and 23 internal cues are measured from that take;
  the actual construction preflight finishes at 135.32 with no late events.
  Supporting ASR match ratio is 0.858.
- Final H.264 export: 1920×1080, 30 fps, 135.333333 seconds, 4,647,916 bytes.
  Its AAC track lasts 135.320998 seconds and covers the full take.
- The coordinating agent's terminal scan checks all 4,060 frames: the lower
  20 percent remains black, with maximum limited-range luma 16.
- All 30 VTT cues exactly reproduce the frozen spoken source, are ordered,
  nonoverlapping and bounded, and use at most two 42-character lines. The
  minimum display interval is 2.140 seconds.
- Author review inspected 21 actual native time points: 13, 15.2, 18, 31,
  32.5, 40, 50, 58, 61, 68, 72, 75, 83, 94, 100, 101.5, 101.7, 108, 117,
  119.5, and 134 seconds. Intermediate transformations and completed states
  were distinguished; the exact quotient was additionally checked in
  `videos/build/odd-ones-at-one-author-exact-101.7.png`. No blocker was found.
- Source, SSML, scene, shared layout, and video hashes match the final
  manifest. The scoped audit is saved at
  `videos/build/odd-ones-at-one-author-final-audit.json`. Python, Ruff, CPU
  LaTeX, and the bounded exact arithmetic checks are recorded in preparation.

## Report relevance

Records final teaching media, actual chronology, measured timing, native
visual review, and media/caption checks. Automated alignment is supporting
evidence, not human listening acceptance. The finite illustrations and
production review do not independently or formally verify the full proof.

## Root acceptance and repository checks

At 2026-11-15T07:19:02-08:00 root Codex independently accepts representative
completed and intermediate native states, with the author's 21-time-point
review covering each full argument. The final source/scene/layout/SSML/video
hashes, exact captions, audio coverage and all-frame subtitle band pass.
Complete repository checks pass: 20 narration tests, 41 video tests, 183 website
tests with 9,346 assertions and 50 built pages. The separate commit/push follows.
