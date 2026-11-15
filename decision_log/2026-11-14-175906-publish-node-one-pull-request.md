# Publish the Node 1 pull request

- Recorded at: 2026-11-14T17:59:06-08:00
- Observed work interval: 2026-11-14T17:57:35-08:00/2026-11-14T17:59:06-08:00 (91 seconds through this record).
- Participants: Steven Creech (publication authorization and Node 1 scope);
  OpenAI Codex, GPT-6 (commit, push, GitHub API actions, and preservation checks).

## Context and decision

Complete the publication prepared in the
[preceding record](2026-11-14-175735-prepare-node-one-pull-request.md).
Commit the reviewed Node 1 work, push `steven/node-1-proof-graph`, and create
an ordinary pull request targeting `TomasOrtega/circulant-Hadamard:main`.
Include this observed publication record in a follow-up documentation commit.

## Rationale

The previous PR was already merged, so the fresh branch starts at fetched
main `5ab4412`. Honor Steven's explicit choice to keep Node 2 local.
Historical records remain available without including its draft script or
page expansion in the PR.

## Evidence and outcome

- Implementation commit `88755e0470042e4db4c3bdad918404d82527f72d` contains
  the scoped work and decisions, with the required assistance trailer.
- Git successfully pushed the branch and configured upstream tracking.
  GitHub returned open, non-draft [PR #2](https://github.com/TomasOrtega/circulant-Hadamard/pull/2),
  titled “feat(website): refine Node 1 proof graph and scripts”, with that
  implementation commit as its head at creation and `main` as its base.
- The PR description begins with the required AI-text notice and describes
  the final behavior, documentation-link checks, earlier visual checks, and
  scope. No merge was performed.
- The exact scoped snapshot passed 41 tests (5,023 assertions), built 17 pages,
  and passed the checks recorded in the preceding entry. Remote CI completion
  has not been established at this recording time.
- A post-commit hash check confirmed all prepublication local source files
  still match. The remaining working changes are the Node 2 page, its script,
  and its entries in the website and script READMEs. They were not pushed.

## Report relevance

Node 1's refined graph, explanations, editable scripts, and supporting website
changes are now available for review. This records observed publication and
preservation of ongoing local work without claiming review, merge, or CI success.
