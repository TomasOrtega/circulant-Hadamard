# Remove completed pair frames and state the full coefficient range

- Recorded at: 2026-11-15T05:43:53-08:00
- Observed work interval: 2026-11-15T05:40:18-08:00/2026-11-15T05:43:53-08:00 (fresh-export review, second regression, and focused correction; includes a wait for root's red check).
- Participants: OpenAI Codex, GPT-6 (root and delegated native-frame review, root test execution, delegated regression and correction); Tomas Ortega (finished-video requirements).

## Context and decision

Continue the actual-export review of [Video 3.4](../videos/halve_sign_sums.py)
after the [highlight-spacing correction](2026-11-15-053722-clear-sign-column-highlights.md).
The fresh opening highlights clear their neighboring terms, and the first
regression passes. The residue panel reveals a second issue: its four pair
rectangles remain after the two sums collapse to single zeros, so those
zeros cross an obsolete border.

## Rationale

Add a second actual-scene regression at the agreed semantic
`at("integer_halves")` boundary. Run the real scene to that cue and require
that no pair-selection rectangle remains in its current body. Fade the pair
frames concurrently with the existing 0.75-second row-to-zero transformation,
remove them from the scene body, and omit them from the later hide call so
they cannot revive. No time is added.

Also replace the closing illustrative powers strip by the exact set
{P^b:0≤b<u²}. The original strip explicitly listed P^1, which did not
express the single-position u=1 case cleanly. The bounded set matches the
universal coefficientwise argument, including u=1. The underlying parity
formulas, complete narration, cue times, and other closing content remain
unchanged. Root explicitly approved including this scope clarification in
the same offline rerender.

## Evidence and outcome

Root confirmed the first layout regression green: one test in 0.524 seconds.
Before the second fix, its new regression failed in 0.691 seconds because
the current body retained all four obsolete rectangles at the integer-half
cue. The concurrent fade/removal is now applied. Source and both tests pass
Ruff and Python compilation; root owns the next two-test green check and
rerender. The initial fresh spacing frame is accepted, and the other
sampled coefficient, half-integrality, and numerical-example frames remain
mathematically correct. Final export acceptance, hashes, and the full
subtitle-band result are pending the combined rerender; no superseded
export hashes are presented as current-source evidence.

## Report relevance

Records another defect found only by inspecting the actual rendered
transition, a failing-first scene-graph regression, and a universal-domain
notation correction. These improve visual clarity and mathematical scope
without changing the parity proof or its single accepted recording.
