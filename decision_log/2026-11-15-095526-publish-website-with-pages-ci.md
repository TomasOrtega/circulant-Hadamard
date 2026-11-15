# Publish the website through the existing CI workflow

- Recorded at: 2026-11-15T09:55:26-08:00
- Observed configuration interval: 2026-11-15T09:53:39-08:00/2026-11-15T09:55:26-08:00 (107 seconds through local validation).
- Participants: Tomas Ortega (issue and commit/push request); OpenAI Codex,
  GPT-6 (configuration and checks).

## Context and decision

[Issue #17](https://github.com/TomasOrtega/circulant-Hadamard/issues/17)
reports that CI does not publish the website. Replace the generic website
artifact with GitHub's Pages artifact and add a deployment job after lint,
TeX, and website checks. Deploy only pushes to `main`, using the existing
`github-pages` environment. Link the public site from the README.

This resolves the missing publishing job observed in the
[earlier local preview](2026-11-14-080340-fork-request-and-local-preview.md).
Also correct one remaining website README sentence about reverse dependency
links removed for [issue #13](2026-11-15-094840-wrap-deeper-links-beside-headings.md).

## Rationale

Follow GitHub's [custom Pages workflow guidance](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
The Pages API confirms workflow publishing is already enabled, the public URL
is `https://tomasortega.net/circulant-Hadamard/`, and the environment permits
only the main branch. No repository setting or credential change is needed.
The official action releases and their metadata confirm v5 for both artifact
upload and deployment. Keep write and identity-token permissions in the
deployment job. Serialize workflows per Git ref without canceling an active
publication, so an older build cannot replace a newer deployment.

## Evidence and outcome

- Before the change, the public URL returned HTTP 404 and CI contained only
  a generic website upload, with no Pages deployment step.
- Actionlint 1.7.12, repository lint, and whitespace checks pass. The existing
  website build is current. All 256 component tests passed in the immediately
  preceding test-relocation task; application code is unchanged here.
- Publication awaits the implementing commit's push. The issue stays open
  until the actual deployment and public site can be checked.

## Report relevance

Records user-directed website publication infrastructure and its local checks.
Hosting publishes the existing exposition; it does not verify its mathematics.
