# Commit and publish the approved Chirp SSML workflow

- Recorded at: 2026-11-14T18:17:04-08:00
- Observed work interval: 2026-11-14T18:15:13-08:00/2026-11-14T18:17:04-08:00 (111 seconds; staging and publication after preparation).
- Participants: Tomas Ortega (explicit commit/push request and audio acceptance); Codex (GPT-6, final checks, Git commit, and push).

## Context and decision

Publish the [accepted SSML workflow](2026-11-14-181513-adopt-approved-chirp-ssml.md)
and its accumulated decision history on the existing main branch, as requested
by the user. Include the concise agent instructions, one-take enforcement,
SSML input and cache handling, accepted WAV and script, offline demo preparation,
timed scene, documentation, and regression tests.

## Rationale

The user explicitly authorized publication and accepted the audio. Preserve its
exact recording for reproducible previews. A fetch and non-overlapping
fast-forward incorporated the remote website commits before staging. Generated
videos and caches remained excluded. Use the required conventional commit and
`Assisted-by: Codex:GPT-6` trailer.

## Evidence and outcome

All 32 local speech/video checks passed. Ruff, formatting, full prek checks,
commit hooks, local documentation links, and staged whitespace checks passed.
Empty-cache offline import reproduced the approved WAV exactly.

Created commit
[3e8f021](https://github.com/TomasOrtega/circulant-Hadamard/commit/3e8f02129dd8b53e59ba61a0e504284d31506ebc),
`feat(video): adopt single-take Chirp narration with SSML pauses`.
Git confirmed that origin/main advanced from 5430e84 to 3e8f021. Immediately
after that push, local and remote-tracking main matched and the working tree
was clean. This follow-up record captures the observed publication outcome.

## Report relevance

This records authorized publication of the user-accepted media workflow and
its development history. Local technical validation and the user's audio
acceptance are separate evidence. It introduces no mathematical result or
website-hosted video.
