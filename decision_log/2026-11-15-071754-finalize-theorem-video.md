# Finalize the theorem video

- Recorded at: 2026-11-15T07:17:54-08:00.
- Observed production interval: 2026-11-15T07:10:43-08:00–2026-11-15T07:17:54-08:00
  (431 seconds, including coordinating-agent narration/rendering).
- Observed author export review: 2026-11-15T07:16:27-08:00–2026-11-15T07:17:54-08:00
  (87 seconds; overlaps value-at-one review and is not additive person-hours).
- Participants: user (standing final-video request); Steven Creech (editorial
  source); Codex/GPT-6 (authoring and coordinating production); Google Chirp 3
  HD Achird (one complete take); local ASR (supporting alignment).

## Context and decision

Accept the finished [Theorem video](../website/media/theorem.mp4) after the
[preparation decision](2026-11-15-071256-prepare-final-theorem-video.md).
Preserve the source Markdown's draft proof status and the stated earlier
inputs. Freeze scene/layout hashes in the
[production metadata](../videos/production/theorem.json). Independent review,
full checks, website attachment, and the separate commit remain coordinated
by the root agent.

## Rationale

The export covers necessity and existence separately. The order restriction
and general contradiction leave `n=4` for `n>1`, while `n=1` follows its own
path. The actual one-entry example is fixed by a cyclic shift. The four-row
example is built through right shifts, two rows are compared coefficient by
coefficient, their dot product becomes zero, and the Gram matrix receives
fours on the diagonal and zeros elsewhere. The final state retains the
`u=1` exception to the Delta theorem and the earlier-input qualifier.

## Timing revision and observed outcome

At 2026-11-15T07:13:43-08:00, the actual construction preflight reported that
`four_row_length` arrived at 90.08 seconds instead of its measured 89.44:
a 0.64-second overrun. This existing full-scene preflight reproduced the
problem before the fix; no mirrored string test was added.

With the root render held, shorten the preceding zero-dot transformation
from 1.0 to 0.6 seconds and its explanatory prose reveal from 0.9 to 0.6.
The source was refrozen at 2026-11-15T07:14:03-08:00. These two local changes
save 0.7 seconds without changing words, measured cues, or mathematical
states. The root's subsequent strict construction preflight finishes at
119.24 seconds with no late events. No extra synthesis was used.

## Evidence and outcome

- The unchanged 1,946-byte, 306-word default Achird take lasts 119.240227
  seconds, with four paragraph cues and 21 internal measured cues.
  Supporting ASR match ratio is 0.8969.
- Final H.264 export: 1920×1080, 30 fps, 119.266667 seconds, 3,818,460 bytes.
  Its AAC track lasts 119.240998 seconds and covers the complete take.
- The coordinating agent's terminal band scan checks all 3,578 frames:
  the lower 20 percent is black, maximum limited-range luma 16.
- All 27 exact-source caption cues are ordered, nonoverlapping and bounded,
  with at most two 42-character lines. Minimum display time is 1.680 seconds.
- Author review inspected 21 actual native time points: 13, 20, 32, 41, 54,
  56, 60, 64, 69, 74.8, 78, 81.7, 83, 85, 89, 90, 94, 98, 100, 110, and
  118 seconds. Completed Gram identity and stable final heading were checked
  in `videos/build/theorem-author-gram-100.png` and
  `videos/build/theorem-author-header-118.png`. No blocker was found.
- Exact finite construction checks cover all 16 Gram entries, six distinct
  row pairs, three consecutive cyclic shifts, and the order-one identity.
  These validate the examples, not the preceding exclusion theorem.
- Source, narration, scene, shared layout, and video hashes match the final
  manifest. The audit is `videos/build/theorem-author-final-audit.json`.
  Scoped Python/Ruff and CPU LaTeX checks pass.

## Report relevance

Records the end of the supplied proof chain as final teaching media,
including the reproduced timing failure and measured correction. Earlier
mathematical inputs remain stated dependencies. No new theorem, external
mathematical verification, formal proof, or human listening acceptance is
claimed by this production work.

## Root acceptance and repository checks

At 2026-11-15T07:19:02-08:00 root Codex independently accepts representative
completed and intermediate native states, with the author's 21-time-point
review covering each full argument. The final source/scene/layout/SSML/video
hashes, exact captions, audio coverage and all-frame subtitle band pass.
Complete repository checks pass: 20 narration tests, 41 video tests, 183 website
tests with 9,346 assertions and 50 built pages. The separate commit/push follows.
