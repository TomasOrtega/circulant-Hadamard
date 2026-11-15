# Use video, graph, then text throughout the website

- Recorded at: 2026-11-14T17:04:47-08:00
- Observed work interval: 2026-11-14T17:02:38-08:00/2026-11-14T17:04:47-08:00 (129 seconds through this record).
- Participants: Steven Creech (request); OpenAI Codex, GPT-6 (implementation,
  validation, and a parallel documentation agent).
- Documentation interval: 2026-11-14T17:02:55-08:00/2026-11-14T17:03:12-08:00
  (17 seconds, overlapping the primary interval).

## Context and decision

Steven explicitly requested video, graph, then text, replacing the earlier
video, text, graph ordering. This supersedes the placement decision in
[the overview introduction](2026-11-14-162345-introduce-theorem-before-proof-graph.md)
and its extension to [Node 1](2026-11-14-164817-refine-node-one-from-corrected-script.md).
Preserve those historical records and record this reversal separately.

Move the dependency graph directly after the overview video in the shared
[page renderer](../website/node.jsx). Keep the existing white explanation cards
and theorem styling after the graph on pages with their own proof maps. Other
views retain their explanations below the parent-map disclosure. Remove the
obsolete `introductionBeforeGraph` option and its Node 1 metadata. Update the
authoring instructions and change the overview and Node 1 prose to refer to
the graph above.

## Rationale

Use a single reading order across views while preserving their mathematical
content, video slots, graph connections, and existing appearance. The user's
latest preference replaces the earlier introduction-before-graph exception.
The source video narration can still refer to the graph below the video;
that remains accurate and does not require editing the original overview script.

## Evidence and outcome

Updated existing layout checks to require video before graph before explanation
on every generated page. The changed check failed on the previous overview
layout before implementation, then passed with the renderer change. All 39
tests passed (5,019 assertions), and the build emitted 17 pages. Required lint,
explicit lint of the untracked graph test, and `git diff --check` passed.

A desktop browser screenshot confirmed the main overview's video, complete
proof graph, then definitions/theorem card. Opened the refreshed local website.
No mathematical claim was changed or newly verified by this layout work.
Earlier uncommitted work remains in place; no commit, push, or deployment was made.

## Report relevance

This records a user-directed presentation change and its AI-assisted
implementation. It changes the order in which the exposition is presented,
not the proof or its dependency structure.
