# Isolate concurrent Manim TeX compilation

- Recorded at: 2026-11-15T03:23:34-08:00.
- Observed diagnosis and implementation interval:
  2026-11-15T03:16:22-08:00/2026-11-15T03:23:34-08:00 (432 seconds through this record).
- Participants: OpenAI Codex, GPT-6 (export inspection, diagnosis, regression
  tests, implementation, and independent root-agent review).

## Context and decision

The first Node 6 export displayed a later evaluation ratio where its opening
norm equation belonged. Publication was withheld. Using the diagnosing-bugs
skill, reproduce the wrong-formula symptom through the real compiler before
changing rendering behavior.

ManimGL at pinned revision `fafa083a4fb274bba9cabde0b6e2f50ba6da0622`
uses shared `working.tex` and `working.dvi` paths in `full_tex_to_svg`.
Concurrent processes can compile another caller's source and persist that SVG
under the requested formula's cache key.

Add [project cache configuration](../videos/render_cache.py), called once on
[NarratedScene import](../videos/narrated_scene.py). Retain a unique TeX scratch
directory for each process until exit, and use the new project-local
`videos/.cache/render-v2/svg` disk-cache namespace. Clear in-memory SVG and
typesetting reference caches on configuration. Existing cache directories,
upstream packages, scene geometry, and GPU settings remain unchanged.

## Rationale

Isolating scratch files prevents cross-process compilation races. A fresh
namespace also bypasses previously poisoned entries without deleting caches.
The integration uses the pinned library's private cache seam; retain the
regressions when upgrading it. GPU aliasing was considered but remains
unconfirmed, so it supplies no basis for renderer changes.

## Evidence and outcome

- Added [two regressions](../videos/test_render_cache.py) before the fix.
  Synchronized real compilers after writing their inputs and compared their
  returned SVGs with serial known-correct results. Both concurrent requests
  returned the norm SVG despite requesting different formulas. A separate
  injected legacy-cache entry returned the ratio SVG for the norm request.
  **Two tests failed** in 40.283 seconds.
- With isolation, **both tests pass** in 30.099 seconds. Serial fixture reuse
  reduces repeated import work. No network or GPU is needed by these tests.
- Ruff, formatting, and scoped whitespace checks pass. Ignored evidence:
  `videos/build/render-cache-regression-before.log`,
  `videos/build/render-cache-regression-after.log`, and retained failed frames.
- Root accepted the fix and will rerender Node 6 serially, inspect actual
  frames at 8, 27, and 215 seconds, and run the complete suite before publication.
  Corrected-export acceptance is pending at this record's timestamp.

## Report relevance

Records a reproducible rendering failure, its project-scoped repair, and the
distinction between passing compiler regressions and later video acceptance.
No mathematical claim or narration was changed.

## Final integration validation

Observed at 2026-11-15T03:57:10-08:00: all 20 narration and 30 video tests pass, without resource warnings; all 147 website tests pass (8,570 assertions), and the build emits 50 pages. All six new or revised scenes pass strict-compiler preflight without late animation cues. Ruff and whitespace checks pass. Current editorial, narration, scene, layout, and video hashes match all 14 final production records. Root publishes each video in its own commit.
