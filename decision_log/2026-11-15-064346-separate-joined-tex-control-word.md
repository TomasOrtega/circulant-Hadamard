# Separate a joined TeX control word

- Recorded at: 2026-11-15T06:43:46-08:00.
- Observed correction interval:
  2026-11-15T06:43:26-08:00/2026-11-15T06:43:46-08:00 (20 seconds).
  Root's failing preflight began before this interval; its exact start was
  not measured by the author.
- Participants: OpenAI Codex, GPT-6 (root actual-scene preflight; child fix
  and joined-string audit).

## Context and decision

The first actual-construction preflight after
[preparing Sign Ratio Congruences](2026-11-15-064125-prepare-sign-ratio-congruences-video.md)
fails before producing its timing JSON. Two adjacent Python raw strings
join a final `\qquad` to an initial `b(P)`, making the undefined command
`\qquadb`. Add a literal trailing space to the first string. Preserve the
entire narration, cue metadata, mathematics, and all other scene content.

## Rationale

Python compilation accepts the joined string but does not compile its TeX.
The actual scene construction is the reproducing check. Keep that check as
the regression evidence rather than add a test mirroring the one-character
string fix, following root's explicit instruction.

## Evidence and outcome

- Root's existing RED log is
  `videos/build/sign-ratio-congruences-timing-preflight.log`. It identifies
  the quotient-types formula and reports `Undefined control sequence` at
  the actual joined `\qquadb` command.
- The AST audit independently identifies that exact combined constant.
  After the separator correction, audit all 47 AST constants containing
  TeX, including adjacent literals after Python joining. All 25 encountered
  control words are recognized; no joined `\quad`/`\qquad` command or
  unknown control word remains. This audit does not replace construction
  of the full scene, including dynamic formulas.
- Ruff, formatting, Python compilation, and scoped whitespace checks pass.
  The source is frozen for root's full-construction GREEN preflight and
  rendering. No additional narration is requested.

## Report relevance

Records a real preflight failure missed by Python-only compilation, its
minimal correction, and the distinction between a joined-source audit and
actual mathematical typesetting validation.
