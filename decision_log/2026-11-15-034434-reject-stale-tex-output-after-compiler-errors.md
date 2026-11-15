# Reject stale TeX output after compiler errors

- Recorded at: 2026-11-15T03:44:34-08:00.
- Observed regression and repair interval:
  2026-11-15T03:41:29-08:00/2026-11-15T03:44:34-08:00 (185 seconds through this record).
- Participants: OpenAI Codex, GPT-6 (source editing, native-frame inspection,
  independent root-agent diagnosis, regression, and repair).

## Context and decision

Follow up the [concurrent TeX cache repair](2026-11-15-032334-isolate-concurrent-manim-tex-compilation.md).
A fresh Node 6 export still duplicated the preceding product formula in its
final comparison identity. Native cropped pixels confirmed this failure.

A source line split had joined `\qquad` directly to `W`, producing the
invalid command `\qquadW`. The pinned compiler raises on a failed LaTeX process
only when no DVI file exists, so the previous successful formula's DVI could
be returned and cached. Restore the separating space in Node 6.

Give every formula compilation a private temporary directory within its
process scratch directory. The project compiler wrapper rejects every nonzero
LaTeX or dvisvgm exit before returning an SVG. Use `render-v3/svg` to bypass
entries already spoiled in v2; preserve existing cache directories.

## Rationale

Process isolation protects concurrent compilation, while formula isolation and
explicit error checks prevent stale output after invalid input. Both failures
can otherwise silently publish the wrong mathematics. Scene geometry, narration,
camera settings, and GPU batching remain unchanged.

## Evidence and outcome

- Added a third real-compiler regression before either repair. A valid formula
  followed by `\qquadW` returned the identical prior SVG hash instead of raising:
  **one failure in 9.937 seconds**.
- All **three compiler regressions pass in 39.401 seconds** after the fix,
  covering concurrent requests, legacy poisoned entries, and invalid input.
  Ruff, formatting, and scoped whitespace checks pass.
- Ignored evidence: `videos/build/render-cache-invalid-before.log`,
  `videos/build/render-cache-v3-after.log`, and the native final-formula crop.
- Root will rerender Node 6 with the corrected source and fresh namespace,
  inspect the actual final identity, and complete repository checks before
  publication. Export acceptance remains pending at this timestamp.

## Report relevance

Records an AI-introduced source error, a compiler fallback that concealed it,
and failing-first evidence for the additional repair. No mathematical argument
or spoken narration changed.

## Final integration validation

Observed at 2026-11-15T03:57:10-08:00: all 20 narration and 30 video tests pass, without resource warnings; all 147 website tests pass (8,570 assertions), and the build emits 50 pages. All six new or revised scenes pass strict-compiler preflight without late animation cues. Ruff and whitespace checks pass. Current editorial, narration, scene, layout, and video hashes match all 14 final production records. Root publishes each video in its own commit.

Integration also closes the previous SQLite cache before replacement. Extending the legacy-cache regression first exposed the open connection (one failure in 2.759 seconds); after closing it, the full suite passes without the observed ResourceWarning. This changes resource cleanup, not media geometry or narration.
