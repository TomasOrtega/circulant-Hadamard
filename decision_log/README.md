# Decision log

Keep a chronological record of the project's decisions, evidence, and AI use
for the [report](../tex/report.tex), especially its event work, limitations, and
acknowledgements. The [agent instructions](../AGENTS.md) require these records.

Create one Markdown file per substantive decision, named
`YYYY-MM-DD-HHMMSS-short-topic.md` using its recording time in
`America/Los_Angeles`. Add a suffix if filenames would collide. Use ISO 8601
timestamps with explicit UTC offsets inside each record, including seconds.
Read the clock when recording times.

Record the observed start and finish of work when available. These intervals
describe chronology; overlapping intervals are not additive person-hours.
For a retrospective entry, distinguish its recording time from the original
decision time with an `Original decision time` field, and mark unavailable times
as unknown.

Use this format:

```markdown
# Short decision title

- Recorded at: YYYY-MM-DDTHH:MM:SS-08:00
- Observed work interval: start/end timestamps, or unknown.
- Participants: people and AI tools involved; include the model when known.

## Context and decision

State the problem, the choice, and whether it came from a user request or agent
judgment. Link relevant files, sources, and earlier decisions.

## Rationale

Explain why this choice fits the project, alternatives actually considered, and
any tradeoffs.

## Evidence and outcome

Record checks and their results, supporting artifacts, limitations, and open
questions. For mathematical claims, distinguish proofs, computations (with
their ranges), cited results, Lean verification, and conjectures.

## Report relevance

Explain the contribution, when the work happened, and any AI assistance and
how it was checked. Separate known prior work from work during the event.
```

Keep entries concise and factual. Record unsuccessful approaches when they
explain a later choice. Add new entries for reversals or follow-up decisions,
linking earlier records so their original rationale remains available.
