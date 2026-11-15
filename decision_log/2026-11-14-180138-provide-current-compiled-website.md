# Provide the current compiled website

- Recorded at: 2026-11-14T18:01:38-08:00
- Observed work interval: 2026-11-14T18:00:17-08:00/2026-11-14T18:01:38-08:00 (81 seconds).
- Participants: Steven Creech (compiled-preview request); OpenAI Codex, GPT-6
  (build, packaging, preview verification, and delegated archive review).
- Archive review: 2026-11-14T18:01:08-08:00/2026-11-14T18:01:08-08:00
  (under one second, overlapping the primary interval).

## Context and decision

Provide the current local website after the
[Node 1 PR publication](2026-11-14-175906-publish-node-one-pull-request.md).
Build the working checkout, including its local Node 2 exposition, rather than
only the scoped PR snapshot. Open the existing local preview and provide a ZIP
of the complete compiled output.

## Rationale

The user requested the current compiled version. The local build includes the
latest reader-facing content while keeping the unpublished Node 2 work local.
A ZIP supplies a portable copy of the static pages and their required assets.
Production narration in scripts remains separate from the website build.

## Evidence and outcome

- The pinned Bun build completed successfully. The output contains 17 HTML
  pages and 29 files including stylesheets, player, fonts, and licenses.
- Packaged the output under a single directory in `/private/tmp/circulant-hadamard-website-2026-11-14-180038.zip`. CRC checks
  passed; independent inspection confirmed all 322 local href/src references
  resolve inside the archive and required assets are present.
- The existing server at http://127.0.0.1:8000/ returned all 17 HTML pages and
  the three CSS/JavaScript assets byte-for-byte equal to the build output.
  Opened that address in the user's browser.
- No source content changed. The preceding task already validated all 41 tests;
  this task checks the requested build and artifact rather than repeating them.
  No commit, push, PR update, or hosted deployment was performed.

## Report relevance

This records delivery and verification of the current local preview and its
compiled archive, distinguishing the working copy from the Node 1 PR snapshot.
