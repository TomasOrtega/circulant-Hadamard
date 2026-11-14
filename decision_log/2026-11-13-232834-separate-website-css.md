# Separate website CSS from HTML

- Recorded at: 2026-11-13T23:28:34-08:00
- Observed work interval: 2026-11-13T23:24:20-08:00/2026-11-13T23:28:34-08:00
- Participants: user (request); Codex (implementation and checks).

## Context and decision

The user requested a separate CSS file. Move the inline stylesheet to
[website/styles.css](../website/styles.css), link it from
[index.html](../website/index.html), and update the
[Makefile](../website/Makefile) to copy both files to `website/dist/`.
This retains the design in the [earlier decision](2026-11-13-232834-website-style.md).

## Rationale

Keeping markup and styling separate makes each easier to edit. Reuse the
existing static build with a copy rule for each asset; no additional build
tool is needed.

## Evidence and outcome

- `make -C website clean all` passed and produced both assets.
- Compared the extracted CSS and page body against the previous source:
  both were unchanged.
- Compared built files against their sources: both matched exactly.
- A dry run with `make -C website -n -W styles.css` confirmed that a CSS-only
  change rebuilds the stylesheet.
- `prek -a --quiet` and `git diff --check` passed. An explicit `prek --files`
  run also passed for all changed and new files.

Browser preview remains unavailable. Validation covers the source and build.

## Report relevance

This is website maintenance during the event. Codex performed the extraction
and checks. It contributes no mathematical claim.
