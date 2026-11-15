# Recommend grouping production scripts by expanded node

- Recorded at: 2026-11-14T17:27:21-08:00
- Observed work interval: 2026-11-14T17:26:37-08:00/2026-11-14T17:27:21-08:00 (44 seconds through this record).
- Participants: Steven Creech (organization question); OpenAI Codex, GPT-6
  (repository inspection, recommendation, and independent organization review).
- Review interval: 2026-11-14T17:26:52-08:00/2026-11-14T17:27:02-08:00
  (10 seconds, overlapping the primary interval).

## Context and decision

Steven asked whether the production scripts should remain in one folder or
be grouped into folders by node. Recommend a hierarchy aligned with the
[recursive exposition model](2026-11-14-172603-put-node-exposition-in-child-sections.md).
This is a proposal; no script files are moved in response to the advice request.

Keep `website/scripts/overview.md` for Video 0. Give each expanded main node
a directory named by its stable node ID, such as `group-ring-encoding/`, with
`overview.md` for that node's own video and named Markdown files for its child
videos. Keep that node's source PDF and production references inside its own
`reference/` directory. Node 2 can similarly use
`restriction-on-the-order/overview.md` as its draft and graph outline grow.

A terminal script can stay a single named file. When it gains subnodes, promote
it to a directory with its own `overview.md`. Keep node numbers in headings
rather than depending on numbered paths. Retain a top-level README index.

## Rationale

The current flat directory was reasonable when scripts were first
[stored beside the website](2026-11-14-154516-store-overview-video-script.md).
The current eight narration files already include six for Node 1. Grouping
an overview with the scripts it expands into makes the hierarchy easier to
browse without creating a directory around every terminal file. It also
keeps reference materials close to the corresponding production work.

## Evidence and outcome

Inspected the current script inventory and authoring documentation. The
website build consumes node content rather than production scripts, so this
organization can change independently of page URLs. A future move must update
README/source links and the script paths read by `website/group-ring.test.jsx`.
No production files, application code, or tests were changed for this advice;
no new build or browser check is needed. Existing uncommitted work is preserved.

## Report relevance

This records an AI-assisted organizational recommendation as the user develops
recursive video scripts. It is a proposed authoring convention, not an
implemented migration or a mathematical contribution.
