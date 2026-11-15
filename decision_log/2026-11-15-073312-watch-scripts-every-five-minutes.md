# Watch the script queue every five minutes

- Recorded at: 2026-11-15T07:33:12-08:00.
- Observed revalidation interval:
  2026-11-15T07:32:43-08:00/2026-11-15T07:33:12-08:00 (29 seconds).
- Independent queue observation: 2026-11-15T07:33:24-08:00.
- Participants: Tomas Ortega (updated goal); OpenAI Codex, GPT-6
  (remote, production and independent queue checks).

## Context and decision

The user replaced the earlier 30-minute idle interval with five minutes.
This supersedes the monitoring interval in
[the integration record](2026-11-15-072130-accept-all-scripted-node-videos.md).
Preserve that historical record and use the newly active goal: make final
videos for all scripted nodes, merge open PRs, commit and push each video,
and wait five minutes between checks when no script remains.

## Rationale

Retain the completed videos and check current source hashes against committed
production manifests before deciding whether new production is needed. Save
the actual five-minute deadline in ignored watch state. Keep the goal active
while monitoring rather than treating the currently empty queue as completion.

## Evidence and outcome

The fresh fetch shows main and origin/main synchronized at d16df728, with a
clean working tree and no open PRs. CI for the final video commit succeeds.
All 48 canonical scripts still match committed final manifests. The complete
source/scene/layout/SSML/video hash, caption, codec and narration-coverage audit
passes. An independent current mapping check finds no missing assets, changed
scripts, attachment mismatches or new script IDs at 07:33:24.

No video needs regeneration. This update changes the requested monitoring
interval only; the existing final video quality and subtitle-space acceptance
remain supported by the integration and individual production records.

## Report relevance

Records the user's changed polling instruction and current publication/CI
outcomes without rewriting the prior production chronology.
