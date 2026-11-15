# Decouple website deployment from TeX CI

- Recorded at: 2026-11-15T11:09:58-08:00
- Observed work interval: 2026-11-15T11:09:46-08:00/2026-11-15T11:09:58-08:00
  (12 seconds).
- Participants: Tomas Ortega (user); OpenAI Codex (GPT-6-based agent; exact model identifier unavailable).

## Context and decision

The user accepted the recommendation in the
[TeX CI explanation](2026-11-15-110920-explain-tex-ci-purpose.md).
Change [CI](../.github/workflows/ci.yml) so website deployment depends on
`lint` and `website`, removing `tex` from its prerequisites. Retain the TeX job,
including PDF freshness checks, compilation, and submission artifacts.

## Rationale

A report or slides failure should not delay website deployment after its
required checks pass. TeX failures still appear in the overall CI result.
This revises the deployment gate while preserving the earlier
[PDF publication checks](2026-11-15-084535-publish-linked-pdfs-with-ci-freshness-checks.md).

## Evidence and outcome

The workflow diff changes only the deployment dependency list.
`uv run --locked prek -a --quiet` and `git diff --check` passed.
No remote workflow execution was performed; deployment still runs only for
pushes to `main`. No report, website source, or TeX build inputs changed.

## Report relevance

Records user-directed CI maintenance during the event. It changes publication
scheduling and provides no mathematical evidence.

## Publication follow-up

At 2026-11-15T11:10:28-08:00, the user explicitly requested committing and pushing.
Include the workflow change and the three decision records from this
conversation; leave the two pre-existing video estimate records untracked.
Publish on the current `main` branch to `origin`.

At 2026-11-15T11:10:39-08:00, the first push was rejected because remote `main` had
advanced to `7353d7f` (report/slides PR #26). Fetched and rebased the local
CI commit onto it without conflicts. The incoming changes affect the report,
slides, assets, and their records; the deployment change remains one line.
The earlier placeholder observation describes the state before this merge.
