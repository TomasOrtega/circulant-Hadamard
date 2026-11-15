# Explain TeX CI purpose

- Recorded at: 2026-11-15T11:09:20-08:00
- Observed work interval: 2026-11-15T11:09:10-08:00/2026-11-15T11:09:20-08:00.
- Participants: Tomas Ortega (user); OpenAI Codex (GPT-6-based agent; exact model identifier unavailable).

## Context and decision

The user asked why TeX CI is needed. Explain its current responsibilities and
the earlier [PDF publication decision](2026-11-15-084535-publish-linked-pdfs-with-ci-freshness-checks.md).
No workflow change was requested or made.

## Rationale

The job checks recorded source/PDF hashes, lints and compiles the report and
slides, produces a self-contained report source, and uploads submission
artifacts. The earlier record attributes the PDF freshness requirement to an
explicit user request. CI automates these checks; submission requirements alone
do not prescribe this workflow.

## Evidence and outcome

Inspected [CI](../.github/workflows/ci.yml), [Makefile](../tex/Makefile), and
[PDF checker](../tex/published_pdfs.py). Website deployment currently depends on
the TeX job as well as lint and website jobs, so a TeX failure blocks deployment.
The hash check is a publication-record check, not an independent comparison of
compiled PDF contents. No build or tests were needed for this explanation.

## Report relevance

Explains build and publication automation; provides no mathematical evidence.
