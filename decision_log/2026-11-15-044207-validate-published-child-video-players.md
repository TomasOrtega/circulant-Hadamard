# Validate published child video players

- Recorded at: 2026-11-15T04:42:07-08:00
- Observed validation-artifact interval: 2026-11-15T04:14:24-08:00/2026-11-15T04:42:07-08:00 (through this record; earlier planning time is unknown).
- Participants: Tomas Ortega (all-scripted-nodes production request); OpenAI Codex, GPT-6 (implementation and checks).

## Context and decision

Publishing the first refined videos exposed seven parent-graph tests that assumed every child video must remain null. The original Node 2 test failed when Evaluate at One acquired its real recording. Keep the graph and mathematical assertions, remove only the placeholder-state assumptions, and add one integration test that follows the built native player and caption URLs for every published local overview.

## Rationale

Video availability changes as the requested production queue is completed. The enduring requirement is that a published overview renders its correct native source, English captions, valid duration, and existing built files. Unproduced nodes retain their ordinary empty state; this requires no product UI or hierarchy change.

## Evidence and outcome

The old order-restriction assertion failed on the actual new video metadata (one failure, no passes in the focused test). After the update, all 183 website tests pass (9,076 assertions). The current 50-page build includes all 18 published overview players. The new integration check resolves their MP4 and caption URLs, checks the declared source association and positive duration, and reads each WebVTT header. The complete local video/narration checks also pass: 32 video and 20 narration tests. Two actual-scene layout regressions independently failed on the original collision positions and pass after their minimal corrections.

## Report relevance

Records the transition from temporary empty slots to verified native playback for the refined-node series. It changes validation expectations while preserving navigation, graph structure, and mathematical content.
