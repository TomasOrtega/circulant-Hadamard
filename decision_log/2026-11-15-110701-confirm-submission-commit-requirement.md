# Confirm submission commit requirement

- Recorded at: 2026-11-15T11:07:01-08:00
- Observed work interval: 2026-11-15T11:06:47-08:00/2026-11-15T11:07:01-08:00.
- Participants: Tomas Ortega (user); OpenAI Codex (GPT-6-based agent; exact model identifier unavailable).

## Context and decision

The user asked whether the report must identify the submission commit.
Yes: [submission guidelines §4](../rules/participants/submission-guidelines.md)
require every repository link and its full commit hash in the report title block.
[Participant rules §4](../rules/participants/participant-rules.md) also require
the full hash when submitting a repository link on the platform.

## Rationale

The hash identifies the repository version to be judged. This is an explicit
requirement in the locally copied rules, rather than an optional citation.

## Evidence and outcome

Read both rule files and the report metadata. The title block already uses
`\SubmissionCommit`, but [metadata.tex](../tex/metadata.tex) still defines it as
`Full submission commit hash`. No report content was changed. Attempted to
verify the current participant page online; the web tool could not access it,
so this answer relies on the rules copied on November 13, 2026.

## Report relevance

Replace the placeholder with the full hash identifying the version to be judged
when preparing the submission. This check provides no mathematical evidence.
