# Publish the website navigation fixes

- Recorded at: 2026-11-14T21:05:14-08:00
- Observed work interval: 2026-11-14T21:04:33-08:00/2026-11-14T21:05:14-08:00
  (41 seconds through this record).
- Participants: user (commit and push authorization); OpenAI Codex, GPT-6
  (publication and checks).

## Context and decision

Publish the [reading-route highlight fix](2026-11-14-210008-fix-reading-route-highlight.md)
and [source-dropdown removal](2026-11-14-210433-remove-copyable-source-dropdown.md)
to `origin/main`, as the user requested. Include their tests, authoring-guide
update, and decision records in the implementation commit.

## Rationale

The current branch was `main` and matched the fetched remote before the commit.
Publish the validated changes directly on that branch, then preserve the
observed publication result in this follow-up documentation commit.

## Evidence and outcome

- Created [d41ffe2](https://github.com/TomasOrtega/circulant-Hadamard/commit/d41ffe200fc8c89a33b1e80de5699ba3c6339b1d),
  `fix(website): correct route selection and remove source dropdowns`, with
  `Assisted-by: Codex:GPT-6`. Commit hooks passed.
- `git push origin main` succeeded, advancing the remote from `0a249ce` to
  `d41ffe2`. Local and remote-tracking tips matched, and the worktree was clean
  before adding this publication record.
- The implementation passed all 42 website tests, the production build, and
  repository lint. All 17 generated pages omit the source dropdown.

## Report relevance

This records publication of the user-requested interface changes and their
AI assistance. It adds no mathematical result or verification claim.
