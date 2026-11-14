# Use ManimGL and copy 3Blue1Brown animation guidance

- Recorded at: 2026-11-14T15:44:31-08:00
- Observed work interval: 2026-11-14T15:19:39-08:00/2026-11-14T15:44:31-08:00 (24 minutes 52 seconds; overlaps narration work).
- Original decision times: unknown within the observed interval.
- Participants: Tomas Ortega (Manim, upstream guidance, and explicit ManimGL requirement); Codex (GPT-6, source checks, port, render, and inspection).

## Context and decision

The user required Manim videos and copying 3Blue1Brown's style guidance, then
explicitly rejected Manim Community with Cairo in favor of ManimGL. Replace
the initial engine choice in the
[narration setup](2026-11-14-154431-programmatic-achird-narration.md).
Use `manimlib`, `Tex`, and ManimGL rendering throughout the final implementation.
Remove the Community dependency and its audition export.

Copy the upstream `3b1b/videos/CLAUDE.md` guide and `LICENSE.txt` unchanged into
[videos/reference/](../videos/reference/README.md), pinned at revision
`3a3b934b2140249533522e3b2c4396f48b5e6c10`. Preserve its CC BY-NC-SA 4.0
attribution and license. Add a short project-specific
[AGENTS.md](../videos/AGENTS.md) and a root pointer to it. The upstream guide
has no final newline, so exclude that exact file from the newline fixer to
retain a byte-for-byte copy.

## Rationale

ManimGL matches the user's chosen engine and the upstream guide's conventions.
The PyPI 1.7.2 release failed to import because it requires the removed
`pkg_resources` module. Follow the upstream recommendation to install from
source, pinning `3b1b/manim` at
`fafa083a4fb274bba9cabde0b6e2f50ba6da0622`. Add PyAV explicitly because that
revision imports `av` without declaring it. This revision uses a hardware GPU
backend; do not describe its rendering as Cairo or infer OpenGL from its name.

Keep optional video and narration dependencies in separate uv groups. Use
`python -m manimlib` from the root so project imports work. Keep caches and
exports in ignored local directories. Make targets provide offline previews,
1080p at 30 fps, and 4K at 30 fps. The root configuration sets a black
background and Helvetica; scenes use blue and yellow mathematical objects.

## Evidence and outcome

ManimGL's sandboxed renderer found no GPU adapter. The same commands succeeded
with local GPU access. The final example is 1920 by 1080, H.264 video at
30 fps, with 44,100 Hz AAC audio. Video lasts 26.166667 seconds and its audio
26.160998 seconds, covering the approved 26.160-second narration.

Inspected four preview frames and a final 1080p frame for layout and readable
mathematics. Two export checks confirm audio/video duration and title visibility
through the animated sections. The order-four cyclic sign matrix was checked
by exact dot products, giving `H H^T = 4 I`. These are checks of an illustrative
example, not a proof of the circulant Hadamard conjecture.

Factual correction: a suspected missing-label problem in the multi-image
preview did not reproduce in saved frames. Direct inspection and pixel checks
confirmed the labels; no renderer workaround was applied. Both copied upstream
files match their fetched originals. The website's draft nodes and video slots
were not replaced by this audition.

## Report relevance

This is post-submission media tooling and visual exposition work, with AI
assistance. Preserve the abandoned engine choice and the user-directed port
as development history. The rendered audition demonstrates the pipeline and
uses a known order-four example, without adding a new mathematical result.
