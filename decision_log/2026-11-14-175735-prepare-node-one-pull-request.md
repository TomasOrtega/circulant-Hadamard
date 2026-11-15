# Prepare the Node 1 pull request

- Recorded at: 2026-11-14T17:57:35-08:00
- Observed work interval: 2026-11-14T17:52:51-08:00/2026-11-14T17:57:35-08:00 (284 seconds through this record).
- Participants: Steven Creech (sync/PR request and scope selection);
  OpenAI Codex, GPT-6 (integration, validation, and delegated review).
- Review interval: 2026-11-14T17:53:18-08:00/2026-11-14T17:53:50-08:00
  (32 seconds, overlapping the primary interval).

## Context and decision

Steven requested synchronization with main and a pull request for all Node 1
work. GitHub confirmed that [PR #1](https://github.com/TomasOrtega/circulant-Hadamard/pull/1)
was already merged. Fetch origin, fast-forward from `d681fc2` to current
`origin/main` at `5ab4412`, and create `steven/node-1-proof-graph` for a new PR.
The fast-forward preserved the working edits without conflicts and incorporated
upstream README and narration-guidance work.

Steven explicitly chose to keep this PR focused on Node 1 and leave Node 2
local. Stage the five refined nodes, six scripts and PDF reference, dictionary
statements, renderer/navigation changes, shared front-page exposition and
polynomial notation, tests, authoring guidance, and their decision records.
The substantive work is documented in the
[Node 1 refinement](2026-11-14-164817-refine-node-one-from-corrected-script.md),
[subsection layout](2026-11-14-172603-put-node-exposition-in-child-sections.md),
[script organization](2026-11-14-173621-move-scripts-into-numbered-node-folders.md),
and [sign-hypothesis clarification](2026-11-14-175124-clarify-sign-hypothesis-in-dictionary-converse.md).

## Rationale

Leave the expanded Node 2 page and its production draft unstaged. Stage scoped
versions of the website and script READMEs without links to the unpublished
draft; keep their full local versions intact. Node 2's committed page is
byte-identical to main. Preserve the mixed historical records because they
also document Node 1 decisions; their descriptions of local Node 2 work do
not publish it. Change two unavailable draft links to plain source paths,
preserving the earlier narrative and timestamps.

Export the exact index to a temporary directory and validate that snapshot,
so the PR is checked without depending on unpublished Node 2 content. Reuse
the unchanged locked website dependencies. Record file hashes to ensure the
staging procedure preserves every local source file.

## Evidence and outcome

- Independent read-only review found no blocking issues in the scoped Node 1
  mathematics, renderer, loader, graph, navigation, or tests.
- The exact staged snapshot passed all 41 tests (5,023 assertions) and built
  all 17 pages. Repository lint and staged whitespace checks passed.
- All 89 local Markdown links resolve across 30 staged Markdown files. The
  link checker needed frontmatter parsing and generated-page URL resolution
  to avoid treating graph formulas and output links as missing source files.
- Hash checks confirmed all local source files were unchanged by staging.
  The staged snapshot has no Node 2 script and retains main's Node 2 page.
- Existing records document desktop and 500-pixel browser inspections and
  finite arithmetic checks. This publication task adds no mathematical result.
- GitHub CLI is unavailable. Read PR state through the GitHub API with the
  existing credential helper; no credentials are printed or persisted. The
  default Python certificate store failed, so use the system trusted bundle
  with TLS verification enabled, as in the previous publication workflow.

Commit with the required assistance trailer, push the new branch, and create
the PR next. A subsequent record will capture observed publication results;
no PR creation or remote CI outcome is claimed here.

## Report relevance

This records user-authorized publication preparation, upstream synchronization,
and deliberate separation of Node 1 from the ongoing Node 2 draft. The scoped
snapshot and preserved local files make the reviewed changes reproducible.
