# Collapse the README installation guide by default

- Recorded at: 2026-11-14T16:08:26-08:00
- Observed work interval: 2026-11-14T16:07:31-08:00/2026-11-14T16:08:26-08:00 (55 seconds, through implementation and initial checks).
- Participants: Tomas Ortega (request and commit/push authorization); Codex (GPT-6, implementation and validation).

## Context and decision

The user requested a closed-by-default installation dropdown in the
[root README](../README.md), followed by a commit and push. Wrap the existing
prerequisites, build commands, and output locations in a `<details>` element
with the summary "Installation and local build" and omit the `open` attribute.

## Rationale

Use the native disclosure element to keep setup instructions accessible while
reducing the README's initial length. Preserve all original instructions and
leave the submitted-artifact information outside the dropdown.

## Evidence and outcome

A standard-library HTML parser confirmed one balanced details/summary pair
without an `open` attribute. Removing the wrapper and its spacing reproduced
the previous README exactly. Markdown code-fence spacing was checked.
`uv run --locked prek -a --quiet` and whitespace checks passed. No runtime code
changed, so application tests and video renders were unnecessary.

A fresh fetch confirmed main matched origin/main before committing. The user
explicitly authorized publication to this existing branch.

## Report relevance

This is a post-submission, AI-assisted documentation presentation change. It
changes neither the build procedure nor the project's mathematical claims.
