# Explain CRT and the circle in Node 3's main-page section

- Recorded at: 2026-11-14T22:25:01-08:00
- Observed work interval: 2026-11-14T22:22:54-08:00/2026-11-14T22:25:01-08:00 (127 seconds).
- Participants: Steven Creech (requested exposition); OpenAI Codex, GPT-6 (editing, delegated review, build and browser validation).
- Delegated review: 2026-11-14T22:23:11-08:00/2026-11-14T22:23:17-08:00 (6 seconds, overlapping the primary interval).

## Context and decision

Following the [Node 3 circle-script revision](2026-11-14-222005-combine-node-three-normalization-and-preview-phases.md),
Steven requested a fuller CRT explanation before the lemma in the main proof
map's Three Evaluations section, then the u=3 intuition and circle takeaway.
Update only the body of [the Node 3 content file](../website/nodes/three-evaluations.md),
which supplies this parent-page section under the existing recursive layout.

Before the boxed lemma, explain coprimeness of four and u squared, the cyclic
group decomposition, and the bijection between a coefficient position and
its two residues. Introduce Z and P, the substitution X to ZP, and the two-variable
group ring. Explain why fourth roots are natural substitutions for Z.
Retain the boxed lemma verbatim and the star convention immediately below it.

Afterward, describe the hypothetical order-36 example, the four groups of nine
sign coefficients, and the three evaluations. Explain that division by two
in each factor removes four from the product, while coefficient parity preserves
integrality. Finish by deriving the radius-three output circle and introducing
the later phase comparison at one and omega.

## Rationale

The setup makes the change of coordinates understandable before using h(Z,P)
in a formal statement. The example explains both why normalization is useful
and why its coefficients remain in the required rings. Clarify the user's
"no matter the value of P" as every value satisfying P to the ninth power
equals one; the group-ring identity does not imply the same modulus at
arbitrary complex inputs. This follows the
[initial Node 3 construction](2026-11-14-183958-draft-node-three-evaluations-and-keep-u.md)
and the recent script, without changing the mathematics.

## Evidence and outcome

- Independent review confirmed the CRT indexing, star convention, normalization,
  and the necessary restriction to ninth roots of unity for the circle conclusion.
- Verified the existing boxed lemma, metadata, and all five internal graph nodes
  are unchanged. No production scripts were edited.
- All 65 tests passed (6,928 assertions); the build emitted 48 node pages.
- Broad lint passed with mutating whitespace and Python hooks skipped to protect
  concurrent work, with the known two removed-route notices. Full applicable
  hooks passed on the edited page source.
- Checked the built main-page section order and inspected desktop (1440px) and
  narrow (500px) screenshots. Prose, boxed lemma, formulas, and links fit correctly.
  Screenshots used the exact compiled section and original head in a temporary
  preview page; the temporary page was removed afterward.
- Opened the refreshed local proof-map anchor. No commit, push, PR update,
  published deployment, or new mathematical proof was produced.

## Report relevance

Records user-led improvement of the public-facing mathematical explanation,
with AI-assisted wording, consistency review, and rendered-page checks.
The radius conclusion is an exposition of the existing norm identity under
its valid evaluation condition, not a computational or research result.
