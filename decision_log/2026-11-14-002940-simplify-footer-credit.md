# Use a single project credit in the footer

- Recorded at: 2026-11-14T00:29:40-08:00
- Observed work interval: 2026-11-14T00:29:14-08:00/2026-11-14T00:29:40-08:00
- Participants: user (wording); Codex (implementation and checks).

## Context and decision

Use “A project for the Caltech × SAIR Mathathon, by Steven Creech and Tomas
Ortega” in the shared [lesson footer](https://github.com/TomasOrtega/circulant-Hadamard/blob/eff0cad336c140ddd677560ca64e25d2da4cf723/website/lesson.jsx), replacing the
separate project sentence and author affiliations.

## Rationale

The user requested this shorter credit on every lesson page.

## Evidence and outcome

All eight existing tests and the production build passed. Parsed the footer
from all 12 generated pages and confirmed the requested text. Lint checks and
`git diff --check` passed.

## Report relevance

This is a presentation copy edit implemented and checked by Codex.

Link maintenance (2026-11-14): moved source links now point to the snapshot
before the node refactor; the original decision is unchanged.
