# Explain the order restriction on the main page

- Recorded at: 2026-11-14T18:12:04-08:00
- Observed work interval: 2026-11-14T18:10:34-08:00/2026-11-14T18:12:04-08:00 (90 seconds).
- Participants: Steven Creech (requested explanatory copy); OpenAI Codex,
  GPT-6 (editing, build checks, and delegated read-only review).
- Review interval: 2026-11-14T18:11:18-08:00/2026-11-14T18:11:21-08:00
  (3 seconds, overlapping the primary interval).

## Context and decision

After adding the Node 2 graph (`2026-11-14-181021-add-node-two-proof-dependency-graph.md`, retained in the local work history),
Steven asked for the main-page section to state the lemma and its big idea:
evaluation at one gives a square, orthogonality gives evenness, and proving
the remaining factor odd requires a deeper argument.

Revise the body of [Restriction on the Order](../website/nodes/restriction-on-the-order.md),
which the existing loader displays in the main page's Node 2 card. Lead with
the lemma for order n>1, explain the two elementary steps, and distinguish
the harder exclusion of orders divisible by 16. Replace the earlier graph
status and example-route description with this mathematical explanation.

## Rationale

The main page should explain what the node establishes before readers explore
its six internal steps. An even square is four times a square; that reasoning
alone does not establish oddness. Keep the additional divisibility argument
clearly separate and leave its details in the inner graph.

## Evidence and outcome

Independent review confirmed the wording and the role of n>1. All 42 existing
tests passed (5,378 assertions), and the build produced 23 pages. Required lint
and whitespace checks passed. Verified the served main-page card contains the
lemma and all three explanatory stages, then opened its section anchor.
No new tests were added for this prose edit. The graph, scripts, and detailed
nodes are unchanged; no commit, push, or deployment was performed.

## Report relevance

This records a user-directed shift from graph-status commentary to the
mathematical idea of the lemma, with AI-assisted editing and validation.
