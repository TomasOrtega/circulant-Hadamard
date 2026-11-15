# Preserve caption word boundaries at SSML pauses

- Recorded at: 2026-11-15T03:21:18-08:00
- Retained regression-artifact interval: 2026-11-15T03:07:49-08:00/2026-11-15T03:21:18-08:00. Diagnosis began before this artifact; its exact start is unknown. Broader export validation continues.
- Participants: OpenAI Codex, GPT-6 (primary fix, delegated discovery while producing Node 7); Tomas Ortega (standing final-video quality request).

## Context and decision

Node 7's complete narration includes internal SSML breaks without surrounding literal whitespace. Concatenating XML text nodes produced captions such as `zero.Consequently`. The same extraction had joined `star.The` in the published order-restriction captions. Treat an SSML break as a word boundary, while preserving case, punctuation, inline emphasis, and paragraph boundaries.

Add `spoken_paragraphs` to [captions.py](../videos/captions.py), use it for exact-source caption validation and the local alignment workflow, and regenerate affected captions from the existing full recordings and local transcripts. The SSML and recordings remain byte-for-byte unchanged; no additional synthesis request is made. The old order video's production cues and MP4 also remain unchanged.

## Rationale

A pause separates spoken words even when the source XML omits a literal space. Correct text extraction preserves the actual narration rather than requiring a new recording or changing the accepted SSML take. The shared extractor makes the rule explicit for future scripts.

## Evidence and outcome

The new regression first failed on both internal-break cases, then passed with the fix. All seven caption unit tests pass. Current validation of all 14 caption files confirms exact spoken text, at most two lines of 42 characters, at least one-second display intervals, nonoverlapping cues, and bounds within their recordings. The order-restriction caption grouping now ends `h star.` before the pause and starts `The Hadamard condition` after it.

The change does not add or alter mathematical claims. Full video and website checks will be recorded after the separate render-cache repair; new exports remain unpublished pending that review.

## Report relevance

Records an observed caption-quality defect, failing-first evidence, and a repair using the same complete narration recordings. It distinguishes automated source/timing checks from human listening acceptance.

## Final integration validation

Observed at 2026-11-15T03:57:10-08:00: all 20 narration and 30 video tests pass, without resource warnings; all 147 website tests pass (8,570 assertions), and the build emits 50 pages. All six new or revised scenes pass strict-compiler preflight without late animation cues. Ruff and whitespace checks pass. Current editorial, narration, scene, layout, and video hashes match all 14 final production records. Root publishes each video in its own commit.
