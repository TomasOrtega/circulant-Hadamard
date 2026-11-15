# Store video production scripts beside website content

- Recorded at: 2026-11-14T15:45:16-08:00
- Observed work interval: 2026-11-14T15:43:45-08:00/2026-11-14T15:45:16-08:00 (91 seconds).
- Participants: Steven Creech (request and supplied script); Codex (GPT-6, organization, documentation, and checks).

## Context and decision

The user asked for a suitable place for video scripts and supplied Video 0,
Introduction and Proof Roadmap, as an attached text document. Save it in
[website/scripts/overview.md](../website/scripts/overview.md), preserving all
wording, equations, and animation directions. The only byte-level change is
adding the missing terminal newline. Add an authoring guide in that directory
and link it from [website/README.md](../website/README.md).

## Rationale

Use one production script per node, matching the node ID in its filename.
These are editable Markdown drafts without YAML. Keeping animation cues and
spoken narration together supports recording work without replacing the
reader-facing mathematical explanations on the current website.

This refines the workflow in the
[Markdown authoring decision](2026-11-14-013449-markdown-node-authoring.md):
node bodies remain reader-facing explanations; production drafts live beside
them. When ready, adapt narration into those bodies and the parent-owned
[video cut excerpts](2026-11-14-005903-overview-video-cuts-and-scripts.md).
Do not automatically publish the draft, invent media sources or timings, or
create scripts for unsupplied videos. No loader or rendering change is needed.

## Evidence and outcome

A byte comparison confirmed that the saved overview matches the attachment
apart from the final newline. Documentation links resolve. All 34 existing
website tests passed (955 assertions), and the build was already up to date.
The website's rendered content and media metadata are unchanged. This task
stored the user's draft; it did not fact-check, rewrite, or endorse its historical
or mathematical assertions. The script's references to future internal graphs
remain part of the supplied production draft, not newly implemented features.

Targeted lint passed for the script, both authoring guides, and this record;
whitespace checks passed. The all-files lint invocation still reports the
previously moved draft paths as missing. Earlier uncommitted website changes
and decision records are preserved.

## Report relevance

This records the arrival and storage of a user-authored video script and the
AI-assisted choice of an editing workflow. The prose and production cues are
attributed to the user, not claimed as AI-written or as new mathematical work.

Final checks recorded at 2026-11-14T15:45:33-08:00; follow-up work interval
2026-11-14T15:45:16-08:00/2026-11-14T15:45:33-08:00.
