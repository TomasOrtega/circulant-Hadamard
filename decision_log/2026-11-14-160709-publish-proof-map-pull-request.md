# Publish the proof-map and video-script pull request

- Recorded at: 2026-11-14T16:07:09-08:00
- Observed work interval: 2026-11-14T16:06:05-08:00/2026-11-14T16:07:09-08:00 (64 seconds).
- Participants: Steven Creech (publication authorization); Codex (GPT-6, commit, push, and GitHub API actions).

## Context and decision

Complete the publication requested by the user and prepared in the
[preceding decision](2026-11-14-160605-prepare-proof-map-pull-request.md).
Push `steven/proof-map-and-video-scripts` and create a pull request targeting
`TomasOrtega/circulant-Hadamard:main`.

## Rationale

Use the feature branch for review while retaining current upstream narration
work in its base. The user authorized the push and pull request, not a merge.
Include this observed publication outcome as a follow-up documentation commit
on the same branch.

## Evidence and outcome

Commit `d0d0427` contains the implementation, production script, and decision
records, with the required assistance trailer. Git reported a successful new
branch push and configured upstream tracking. GitHub returned an open,
non-draft [pull request #1](https://github.com/TomasOrtega/circulant-Hadamard/pull/1) from the intended feature
branch to `main`, with head `d0d04270a636085fe8dc6f5bf49b9c3de414789f` at creation. Its description
starts with the required AI-text notice and records the browser/source checks.
The worktree was clean immediately after publication.

All 34 website tests and repository lint passed before the implementation
commit, as recorded in the preceding decision. Remote CI completion has not
yet been established at this recording time. No merge was performed.

## Report relevance

The user's proof-map presentation and overview script are now available for
review through the linked PR. The record distinguishes verified publication
from a future review, merge, or remote CI result.
