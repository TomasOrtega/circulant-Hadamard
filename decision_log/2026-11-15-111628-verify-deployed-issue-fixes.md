# Verify deployed issue fixes

- Recorded at: 2026-11-15T11:16:28-08:00
- Observed integration/publication audit: 2026-11-15T11:11:14-08:00/2026-11-15T11:16:28-08:00 (314 seconds, including CI waiting).
- Participants: Tomas Ortega (requests); OpenAI Codex, GPT-6 (integration,
  browser checks and publication audit).

## Context and decision

Finish issues #19–25 with their separate implementation commits and pushes.
Integrate the [persistent contents fix](2026-11-15-111048-keep-contents-open-beside-text.md)
as `d18758a`, preserving the concurrent report merge and CI change.
Its implementation agent reports a complete interval of
2026-11-15T11:00:35-08:00/2026-11-15T11:11:53-08:00 (678 seconds).
The original record separately measures implementation/checks before commit.
No thumbnail or mathematical source changes were made for these issue fixes.

## Rationale

Validate the integrated build and actual published pages after the parallel
branches merge. Preserve unrelated working files and remove only the completed
issue worktrees and preview servers.

## Evidence and outcome

- Root reran the website checks: 185 tests and 10,009 assertions pass. All
  48 active pages build; repository lint and whitespace checks pass.
- The final [CI run](https://github.com/TomasOrtega/circulant-Hadamard/actions/runs/43751141010)
  passes all four jobs: website, lint, TeX and deployment.
- All 98 public HTML documents and three checked assets match the local build.
  Ninety-five HTML files and all three assets match byte for byte. Three pages
  differ only in SVG geometry rounded to nine decimal places across macOS/Linux.
- An additional 70 assertions pass on the public site in Chromium and Firefox
  at 1280 and 390 pixels. Checks cover authors, retired-guide redirects, excerpt
  width, absent placeholder copy, the eight right-aligned deeper-link rows with
  counts on their right, feedback destination, persistent contents navigation,
  desktop clearance and the top-right appearance switch with saved preference.
  The same focused checks passed locally before publication.
- Factual correction: the first temporary smoke harness assumed a `video.src`
  attribute and a trailing-slash homepage URL. Actual players use child `source`
  elements; retired guides resolve to `index.html`. Correcting those assumptions
  gives the reported passes without changing project code.
- GitHub shows no open issues at the final audit. Independent responsive,
  mathematical-heading and print checks are recorded with the contents fix.
  Safari and physical phones were not tested.

## Report relevance

Records user-directed website corrections, per-issue publication and checked
integration of parallel AI work. It adds no mathematical claim or video render.
