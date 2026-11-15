# Include the four-polynomial grouping in the Node 3 lemma

- Recorded at: 2026-11-14T22:27:45-08:00
- Observed work interval: 2026-11-14T22:26:31-08:00/2026-11-14T22:27:45-08:00 (74 seconds).
- Participants: Steven Creech (requested grouping in the formal statement); OpenAI Codex, GPT-6 (editing, delegated review, and validation).
- Delegated review: 2026-11-14T22:26:42-08:00/2026-11-14T22:26:49-08:00 (7 seconds, overlapping the primary interval).

## Context and decision

Extend the boxed lemma in [Node 3's main-page text](../website/nodes/three-evaluations.md),
following the [CRT exposition](2026-11-14-222501-explain-crt-and-circle-in-node-three-main-card.md).
After its hypothesis, display h(Z,P) as H0(P) + H1(P)Z + H2(P)Z squared
+ H3(P)Z cubed. Explain that each H_a collects the coefficients with
Z-exponent a and has u squared coefficients, all plus or minus one.
The definitions of c, d, g and the lemma's conclusion stay unchanged.

## Rationale

The decomposition makes explicit the four pieces used in the surrounding
explanation and subsequent substitutions. Split the displayed expression into
two aligned lines so it fits the existing statement box on narrow screens.
This is a presentation refinement of the existing construction.

## Evidence and outcome

Independent review found no notation or hypothesis concern. All 65 tests passed
(6,928 assertions), and the build emitted 48 pages. Broad lint passed with
mutating hooks skipped to preserve concurrent work; known missing-route notices
remain. A 500px browser screenshot of the exact compiled section confirms
that the grouping and explanation fit inside the lemma. Removed the temporary
preview file. Production scripts and the graph are unchanged; no commit, push,
PR update, or publication occurred.

## Report relevance

Records a user-requested clarification of the formal statement, with AI editing
and rendering validation. No new mathematical claim is introduced.
