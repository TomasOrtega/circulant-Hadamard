# Simplify the front-page definition and proof overview

- Recorded at: 2026-11-14T17:12:13-08:00
- Observed work interval: 2026-11-14T17:10:23-08:00/2026-11-14T17:12:13-08:00 (110 seconds through this record).
- Participants: Steven Creech (requested wording and scope); OpenAI Codex,
  GPT-6 (editing, validation, and independent editorial review).
- Editorial review interval: 2026-11-14T17:10:52-08:00/2026-11-14T17:11:08-08:00
  (16 seconds, overlapping the primary interval).

## Context and decision

Steven requested a plain-language Hadamard definition, a standalone example
without referring to the overview video, and front-page framing around a
high-level proof with progressively explorable detail rather than order 36.
Edit [overview.md](../website/nodes/overview.md) only, refining the earlier
[formal introduction](2026-11-14-163149-formal-theorem-and-matrix-definitions.md).

Define a Hadamard matrix as an n-by-n matrix H with entries plus or minus one
and distinct orthogonal rows, replacing set-power notation. Introduce the
existing order-four matrix with “Example” and identify it directly as a
circulant Hadamard matrix. Keep its explanation followed by the main theorem.
Replace order-36 framing in the introduction and summary with the high-level
proof overview and instructions for exploring individual nodes more deeply.

## Rationale

Use familiar prose for the definition while retaining H for the norm identity.
Make the example understandable independently of a recording. Keep the source
attribution and identify the order restriction and Delta theorem as inputs at
this level. The existing reading-route buttons remain accurate navigation;
this request edits the exposition rather than those routes. The
[video, graph, text order](2026-11-14-170447-video-graph-text-reading-order.md)
continues unchanged.

## Evidence and outcome

Read back the edited Markdown and obtained an independent editorial review.
All 39 existing tests passed (5,019 assertions), including the displayed
order-four matrix and page-order checks. The build emitted 17 pages. Required
lint and `git diff --check` passed. Opened the refreshed local front page.
No new tests were added for this prose edit, and no mathematical claim was
newly proved. Earlier uncommitted changes are preserved; no commit or push
was requested or made.

## Report relevance

This is user-directed editorial refinement with AI assistance, making the
front-page exposition more direct and independent of the video narration.
It changes presentation, not the mathematical argument.
