# Manim videos

Read the copied [3Blue1Brown animation guide](reference/3b1b-animation-guide.md)
before authoring scenes. Its source revision and license are in
[reference/README.md](reference/README.md). This guide adapts its scene, layout,
color, and preview conventions for this project.

Use ManimGL, the 3Blue1Brown engine. Use `Tex` for
formulas, `Text` for prose, explicit imports from `manimlib`, and the commands
in [README.md](README.md). The upstream guide's editor plugins, Dropbox paths,
and `manim_imports_ext` belong to the upstream repository.

- Derive narrated scenes from [NarratedScene](narrated_scene.py). Put the spoken
  script in `with self.narrate(text)` blocks, with animations inside. Size an
  animation against the returned clip's duration when it should fill the block.
- Achird US English is the approved voice. Keep voice settings and caching in
  [narration/speech.py](../narration/speech.py). Use offline previews while
  iterating on visuals, and read formulas as spoken mathematics.
- Use a black background, light text, and consistent colors for mathematical
  objects. Reserve yellow for the current focus; use blue for recurring objects.
  Introduce and transform objects to explain their relationships.
- Prefer `VGroup`, `.arrange()`, `.next_to()`, and `.move_to()` for layout. Keep
  formulas as raw LaTeX strings and scene constants near their use.
- Preserve draft/proof status from the source material. Verify numerical
  examples before animating them.
- Render and inspect representative frames after scene changes. Verify that
  the exported MP4 contains audio and that its duration covers the narration.
  Run `make -C videos check` for narration or timing changes.
- Keep generated videos, TeX intermediates, and caches under ignored build or
  cache directories. Put approved final videos in `website/media/` when they
  are ready to be included in the site.

The adapted guidance in this file is licensed under CC BY-NC-SA 4.0, following
the attribution and license in [reference/README.md](reference/README.md).
