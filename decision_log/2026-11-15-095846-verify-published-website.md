# Verify the published website and close the publishing issue

- Recorded at: 2026-11-15T09:58:46-08:00
- Observed publication and validation interval: 2026-11-15T09:55:26-08:00/2026-11-15T09:58:46-08:00 (200 seconds, including CI wait).
- Participants: Tomas Ortega (issue-handling request); OpenAI Codex, GPT-6
  (publication monitoring, browser checks, and issue closure).

## Context and decision

Complete [the Pages publishing change](2026-11-15-095526-publish-website-with-pages-ci.md)
only after its actual deployment and public URL succeed. Close
[issue #17](https://github.com/TomasOrtega/circulant-Hadamard/issues/17)
after that verification, and commit this outcome record. The record-only
commit skips repeated CI; it changes no deployed files.

## Rationale

A valid workflow alone does not establish that Pages accepts the artifact or
that the custom-domain project path serves the site and its relative assets.
Check the real publication before declaring the issue resolved.

## Evidence and outcome

- Implementing commit `d7a55c7` passed all four jobs in
  [CI run 43743841858](https://github.com/TomasOrtega/circulant-Hadamard/actions/runs/43743841858):
  lint, website, TeX, and deployment. Deployment completed at
  2026-11-15T09:57:49-08:00.
- The [public homepage](https://tomasortega.net/circulant-Hadamard/) now returns
  HTTP 200, compared with the prior 404.
- Firefox 153 and Chromium successfully navigate two levels of child pages
  and return to the parent anchor. Deeper buttons sit beside headings at
  1280 pixels and wrap within a 390-pixel viewport. The mobile screenshot
  was inspected; the removed “Used by” text is absent.
- Public styles.css, math.css, page-controls.js, and overview captions match
  the local build byte for byte. The public video supports HTTP 206 byte
  ranges and returns the requested 1,024 bytes, supporting native seeking.
- All 256 component tests passed during the preceding test-folder work;
  the remote test-folder CI run also succeeded. GitHub confirms #17 is closed.
  The agent's temporary local preview server was stopped.

## Report relevance

Records observed public availability and deployment/browser checks of the
existing mathematical exposition. These checks do not establish its correctness.
