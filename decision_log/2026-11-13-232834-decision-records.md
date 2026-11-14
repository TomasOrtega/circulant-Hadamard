# Require timestamped project decision records

- Recorded at: 2026-11-13T23:28:34-08:00
- Observed work interval: 2026-11-13T23:24:20-08:00/2026-11-13T23:28:34-08:00
- Participants: user (request); Codex (format and instructions).

## Context and decision

The user requested a `decision_log/` folder and mandatory logging instructions
in a root [AGENTS.md](../AGENTS.md), so the team can reconstruct its work for
the report. Adopt the format in [README.md](README.md), with one timestamped
Markdown record per substantive decision.

Record user directions and agent choices, including revised or unsuccessful
approaches. Include actual recording times, observed work intervals,
participants, rationale, evidence, limitations, and report relevance. Preserve
history through linked follow-up entries.

## Rationale

Plain Markdown is readable, versioned alongside the work, and needs no extra
tooling. Pacific timestamps with explicit offsets match the event's time
convention. Recording known times and labeling retrospective uncertainty
supports an honest chronology.

The fields support the [report](../tex/report.tex) sections on contributions,
event work, limitations, and AI use, and the repository's
[submission guidelines](../rules/participants/submission-guidelines.md).
Overlapping work intervals describe chronology and should not be summed as
person-hours.

## Evidence and outcome

The report template and stored submission guidelines were inspected to choose
the fields. The root agent instructions require reading relevant records
before work and recording decisions and observed outcomes before completion.
The project README links the folder. The earlier website design is
[recorded retrospectively](2026-11-13-232834-website-style.md); the
[CSS extraction](2026-11-13-232834-separate-website-css.md) is recorded with its checks.

Documentation links, record formats, and timestamps were checked successfully.
Lint checks passed for all changed and new files.

This requirement relies on agents following `AGENTS.md`; no automated logging
enforcement was added.

## Report relevance

These records provide source material for the team's account of its process
and AI assistance. Codex drafted the format and instructions from the user's
request and the existing report structure.
