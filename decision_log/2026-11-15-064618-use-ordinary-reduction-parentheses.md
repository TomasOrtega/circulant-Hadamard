# Use ordinary reduction parentheses

- Recorded at: 2026-11-15T06:46:18-08:00.
- Observed correction interval:
  2026-11-15T06:46:13-08:00/2026-11-15T06:46:18-08:00 (5 seconds).
  Root's preceding failing-preflight start is unknown to the author.
- Participants: OpenAI Codex, GPT-6 (root actual-construction preflight and
  parser diagnosis; child local correction).

## Context and decision

After the [joined-command correction](2026-11-15-064346-separate-joined-tex-control-word.md),
the next complete construction reaches the reduced ratio rows but fails
with a missing-delimiter error. The dynamic quotient wraps its fraction
with `\pi\!\left(...\right)`. Root identifies the pinned Manim string
parser's sized-delimiter handling as the same limitation encountered in
earlier production.

Replace only this wrapper with ordinary `\pi(...)` parentheses. The ring
map, fraction, mathematics, narration, and timing are unchanged. Do not
change upstream parsing or the shared cache. This is the scene's only
left/right delimiter pair.

## Rationale

Ordinary parentheses express the same application of the reduction map
without exercising the failing wrapper path. An audit of literal TeX
control words cannot establish compatibility with the actual Manim parser
and its rewritten strings; full scene construction is required.

## Evidence and outcome

- Existing actual-scene RED evidence is
  `videos/build/sign-ratio-congruences-timing-green.log` despite its intended
  success-oriented filename. The traceback identifies `ratio_row`'s quotient
  formula during construction of the reduced r row and reports
  `Missing delimiter (. inserted)`.
- Apply the one local wrapper change. Ruff, formatting, Python compilation,
  and scoped whitespace checks pass. Root will repeat the complete
  construction/preflight before rendering. No new mirrored string test,
  narration request, or upstream/cache modification is added.

## Report relevance

Records a second concrete preflight failure, the limits of a static source
audit, and a minimal production-compatible notation change.
