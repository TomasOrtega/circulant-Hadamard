# Define the phase product before stating the Delta theorem

- Recorded at: 2026-11-15T00:19:44-08:00
- Observed work interval: 2026-11-15T00:16:41-08:00/2026-11-15T00:19:44-08:00
  (183 seconds through this record).
- Participants: Steven Creech (requested exposition sequence); OpenAI Codex,
  GPT-6 (writing, delegated review, build and visual checks).
- Delegated read-only review: 2026-11-15T00:17:10-08:00/2026-11-15T00:18:21-08:00
  (71 seconds, including waiting for the edit; overlaps the primary interval).

## Context and decision

Steven requested revising “4. The Δ-Theorem” on the proof map: introduce the
general definition, explain even subsets in the numerator and odd subsets
in the denominator, specialize to the simple quotient for u=3, and give an
intuitive proof sketch centered on Kronecker's theorem.

Edit only the Markdown body of
[delta-theorem.md](../website/nodes/delta-theorem.md), which supplies this
homepage section. Keep the graph, child explanations, videos, and production
script intact. This follows the
[script revision](2026-11-15-000416-center-node-four-script-on-kronecker.md)
and refines the
[original Node 4 exposition](2026-11-14-195152-draft-node-four-phase-storyboard.md).

## Rationale

Display the definition as an explicit ratio of products so the parity rule
is visible. State u>1 odd and nonzero evaluated factors before defining it.
Explain that the empty subset supplies f(1). Then use the two subsets for
u=3 to obtain f(1)/f(ω), followed by the boxed theorem and phase interpretation.

For the proof idea, equal counts of even and odd subsets cancel the evaluation
magnitudes. All conjugates also have absolute value one. Retain the separate
arithmetic comparison that gives integrality, the necessary hypothesis for
Kronecker, and the further congruence argument that gives odd order. Connect
the norm identity to the Hadamard construction through c(P), d(P), and g(P).
The general Gaussian polynomial itself is not assumed to have sign coefficients.

## Evidence and outcome

- Independent read-only review found the definition, quotient direction,
  theorem, and separation of arithmetic inputs consistent with the detailed
  nodes. No new mathematical result or formal verification is claimed.
- Required website checks pass: 129 tests with 7,902 assertions. The build
  emits 48 node pages and the existing compatibility redirects.
- Desktop (1440px) and mobile (390px) browser checks show the new fraction
  within the full text width, with no MathJax errors or page overflow.
  Screenshots were visually inspected; temporary evidence is in
  `/private/tmp/circulant-delta-exposition-qa.json` and matching PNG files.
- Repository lint passes with mutating hooks skipped to preserve unrelated
  unfinished script formatting. No tests were added for this prose revision.
- The existing local preview serves the rebuilt text. No Git commit, remote
  push, PR, hosted deployment, or production-script change is included.

## Report relevance

Documents user-led mathematical exposition and AI-assisted consistency and
rendering checks. The revision brings the phase product's definition and
example ahead of the theorem while keeping its arithmetic hypotheses explicit.

Final checks observed at 2026-11-15T00:19:58-08:00 (197 seconds since task start): all applicable lint hooks passed on the changed text and this record. Opened the updated section in the local preview and removed the closed headless browser’s temporary profile.
