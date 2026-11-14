# Use Bun and retain static HTML

- Recorded at: 2026-11-13T23:49:09-08:00
- Observed work interval: 2026-11-13T23:43:39-08:00/2026-11-13T23:49:09-08:00
- Participants: user (conditional request); Codex (tooling assessment and implementation).

## Context and decision

The user asked whether React and Bun made sense, authorized adopting them when
appropriate, and requested a commit and push after completion.

Adopt Bun 1.4.4 for dependency installation and script execution. Commit
[bun.lock](../website/bun.lock), pin the package manager in
[package.json](../website/package.json), and configure the website CI job with
`oven-sh/setup-bun@v2`.

Keep this single page as static HTML. The website currently needs no client
state or reusable interactive components. The
[website instructions](../website/AGENTS.md) describe when React would become
appropriate and preserve Node.js compatibility.

## Rationale

Bun aligns installation and scripts with upstream. The Tailwind CLI provides
the required static build without adding a UI framework. React would add
dependencies and build structure without changing the current page's behavior.

Replace the intermediate npm lockfile with Bun's lockfile so one package
manager owns dependency resolution. The Makefile automatically installs frozen
dependencies when inputs change and rebuilds CSS when HTML or styles change.

## Evidence and outcome

- Bun 1.4.4 installed the pinned dependencies and generated its lockfile.
- A clean temporary checkout installed with `--frozen-lockfile` and built
  successfully, leaving the lockfile unchanged.
- The Bun build and Node fallback produced byte-identical CSS.
- A subsequent Make check reported the build up to date.
- Lint checks passed for the build, dependency metadata, CI, and documentation.

The user authorized committing and pushing these changes to the existing
repository after verification.

## Report relevance

This records the tooling choice, the reason for retaining static HTML, and
Codex's implementation and checks. Work intervals overlap the
[Tailwind work](2026-11-13-234909-upstream-tailwind-styles.md) and are not additive person-hours.
