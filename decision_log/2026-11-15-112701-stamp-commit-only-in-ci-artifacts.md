# Stamp submission commit only in CI artifacts

- Recorded at: 2026-11-15T11:27:01-08:00
- Observed implementation and local validation interval: 2026-11-15T11:24:57-08:00/2026-11-15T11:27:01-08:00
  (124 seconds).
- Participants: Tomas Ortega (user); OpenAI Codex (GPT-6-based agent; exact model identifier unavailable).

## Context and decision

The user clarified the [canceled hash automation](2026-11-15-111546-cancel-automatic-submission-hash.md):
keep committed TeX as authored, but insert the commit hash into CI artifacts so
the PDF can be submitted directly. Change only the workflow, a new artifact
stamping helper and its tests, and build documentation. Continue the user's
earlier commit-and-push authorization for this CI work.

After the ordinary freshness check and `make check`, CI stamps only
`tex/build/report.tex` with `GITHUB_SHA`, then compiles and uploads it alongside
`report.pdf` and `slides.pdf` in the existing `tex-documents` artifact. Local
build rules, tracked metadata, published PDFs, and their checksum record remain
unchanged. Preserve the pre-existing local report PDF modification.

## Rationale

Artifacts built from a commit can identify that exact commit without a
self-referential checked-in hash. Stamping the flattened source gives matching
submission source/PDF metadata. Reject invalid hashes and missing/duplicate
macro definitions before writing.

An initial draft used a custom environment variable; inspection of the
[action wrapper](https://github.com/xu-cheng/latex-action/blob/v4/action.sh)
showed that its Docker invocation forwards `GITHUB_SHA` but not arbitrary
variables. Revised the hook to use `GITHUB_SHA` directly. The
[container dependencies](https://github.com/xu-cheng/latex-docker/blob/master/deps.sh)
include Python 3. This CI-only design supersedes the canceled local-build design.

## Evidence and outcome

- The new tests failed before the helper existed; all 11 TeX helper tests pass
  after implementation, including CLI invocation and preservation of authored
  metadata and invalid-input outputs.
- An isolated copy of committed TeX passed PDF freshness, TeX lint, and report
  and slides compilation using the workflow arguments. Its generated source
  has no remaining `\input` commands. Extracted PDF title text includes the
  full tested source hash, and the title-page rendering fits without clipping.
- SHA-256 comparisons confirmed that all isolated input files and both tracked
  PDF copies were unchanged. The exact workflow pre-compile command passed
  with `GITHUB_SHA` supplied.
- Ruff, formatting, `uv run --locked prek -a --quiet`, and whitespace checks
  passed. Remote CI and artifact verification follow publication.

## Report relevance

Implements submission provenance in downloadable CI documents; it changes no
mathematics or authored report content. Submit the report source and PDF from
the artifact for the repository commit being judged.

## Remote verification

Verified at 2026-11-15T11:29:47-08:00. Overall observed work interval:
2026-11-15T11:24:57-08:00/2026-11-15T11:29:47-08:00
(290 seconds, including CI wait).

Published implementation commit `5ac60bdc9190246a09d5a061b6bcde70b76e193d`.
[CI run 43752491670](https://github.com/TomasOrtega/circulant-Hadamard/actions/runs/43752491670)
passed all jobs; TeX completed in 1 minute 46 seconds. Downloaded
`tex-documents` artifact `14177285215` and verified that the generated source
definition and PDF title both contain the exact full commit hash above.
The self-contained source contains no remaining `\input` commands, and
`slides.pdf` is present. Visually inspected the actual downloaded PDF title
page: the full hash fits without clipping. The pre-existing local report PDF
modification and unrelated estimate records remain untouched.
