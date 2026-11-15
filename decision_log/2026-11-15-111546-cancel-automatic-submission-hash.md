# Cancel automatic submission hash

- Recorded at: 2026-11-15T11:15:46-08:00
- Observed work interval: 2026-11-15T11:12:27-08:00/2026-11-15T11:15:46-08:00
  (199 seconds, including user interruption).
- Participants: Tomas Ortega (user); OpenAI Codex (GPT-6-based agent; exact model identifier unavailable).

## Context and decision

After the [submission hash discussion](2026-11-15-110701-confirm-submission-commit-requirement.md),
the user requested automatic hash insertion, then explicitly canceled it.
Revert the entire uncommitted implementation and keep manual metadata.

## Rationale

The abandoned approach stamped the flattened report source with Git HEAD or
an explicit full hash before compilation, with CI supplying its checkout SHA.
It avoided a self-referential checked-in PDF hash. The user's cancellation
supersedes this implementation choice.

## Evidence and outcome

Before cancellation, 11 helper tests passed, TeX lint and compilation passed,
the rendered title fitted the hash, and default/override hash refresh and
unchanged-output timestamps were checked. The publication command completed
during the interruption. No implementation commit or push occurred.

Restored workflow, README, Makefile, publication helper, and existing tests;
removed the new stamping helper and tests. Restored both published PDFs and
their checksum record byte-for-byte from the pre-publication backup, preserving
the pre-existing local report PDF modification. Rebuilt the generated report
with its original manual placeholder. The earlier deployment decoupling remains.

## Report relevance

Records an abandoned automation experiment and its user-directed reversal.
It adds no mathematical content or final submission hash.
