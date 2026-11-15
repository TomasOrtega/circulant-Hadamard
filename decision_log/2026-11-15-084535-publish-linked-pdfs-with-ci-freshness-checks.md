# Publish linked PDFs with CI freshness checks

- Recorded at: 2026-11-15T08:45:35-08:00
- Observed preparation, discussion, and implementation interval:
  2026-11-15T08:34:09-08:00/2026-11-15T08:45:35-08:00 (686 seconds).
- Participants: Tomas Ortega (README links, publication choice, CI freshness,
  and TeX-folder requirements); OpenAI Codex, GPT-6 (implementation and checks).

## Context and decision

The user requested links for report.pdf and slides.pdf in the
[README](../README.md), then asked about CI artifacts. After comparing options,
the user explicitly chose checked-in PDF copies, required their placement
inside tex/, and requested that CI ensure they stay current.

Publish [report.pdf](../tex/report.pdf) and [slides.pdf](../tex/slides.pdf)
from the existing TeX build and link them directly from the README. Remove
only these two paths from the build-output ignore rules. Add
`make -C tex publish` to refresh both copies and their source/output checksum
record, and `make -C tex check-pdfs` to validate that record. Run the checker
and its tests in the existing TeX CI job before its ordinary compilation.
Continue the user's established commit-and-push instruction.

This extends the [README presentation decision](2026-11-14-160826-collapse-readme-installation.md).
An initial top-level pdfs/ destination was provisional; the user's subsequent
location instruction superseded it. That folder is absent from the final tree.

## Rationale

The original files were ignored build outputs and had no working repository
links. No GitHub releases existed. CI currently bundles report.tex and both
PDFs into one tex-documents artifact. GitHub's
[artifact documentation](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/download-workflow-artifacts)
states that downloads require sign-in and normally expire after 90 days;
the current artifact's API expiration is 2027-02-13T16:28:53Z. Persistent
[release assets](https://docs.github.com/en/repositories/releasing-projects-on-github/linking-to-releases)
were offered, but the user selected repository copies.

Record hashes for root TeX and bibliography files, shared diagram/image
inputs, the Makefile, the publication helper, and both PDF copies. Input
additions, removals, or edits and modified/missing PDFs fail the check with
the refresh command. Publication reads and validates both build outputs before
writing the copies. The freshness contract checks recorded build inputs and
PDF integrity, without requiring byte-identical compiler output across local
and CI environments. It is not a semantic PDF comparison or a mathematical
verification.

## Evidence and outcome

- The local report build predated the latest abstract edit. The canonical
  `make -C tex` build refreshed it successfully; no TeX prose was edited.
- All seven publication/checker tests pass, covering source and shared-input
  edits, added/removed inputs, altered/missing PDFs, missing/malformed records,
  safe failure on an invalid build, and the CLI's actionable error message.
  The initial test run failed because the helper had not yet been implemented.
- The actual CI command, run against an isolated copy of the real inputs,
  passes for the current state and fails after either a source edit or PDF
  alteration. These failure checks leave the working sources untouched.
- `make -C tex publish`, `make -C tex check-pdfs`, and `make -C tex check`
  pass. Both README links resolve to PDF files inside tex/ whose bytes match
  their current build outputs. No top-level pdfs/ directory remains.
- Initial lint found and reformatted one long Python line; the subsequent
  `uv run --locked prek -a --quiet` and whitespace checks pass. Final lint,
  publication, and remote CI validation follow this record.

## Report relevance

Records user-directed publication of the current report and slides, including
an automated guard against stale checked-in copies. It adds no mathematical
argument and does not certify that these are byte-identical to any earlier
competition upload.

Final local validation recorded at 2026-11-15T08:46:07-08:00: repository lint, staged whitespace checks, and the published-PDF freshness check all passed with both PDFs staged.
