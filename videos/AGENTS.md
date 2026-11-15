# Manim videos

Read the copied [3Blue1Brown animation guide](reference/3b1b-animation-guide.md)
before authoring scenes. Its source revision and license are in
[reference/README.md](reference/README.md). This guide adapts its scene, layout,
color, and preview conventions for this project.

Use ManimGL, the 3Blue1Brown engine. Use `Tex` for
formulas, `Text` for prose, explicit imports from `manimlib`, and the commands
in [README.md](README.md). The upstream guide's editor plugins, Dropbox paths,
and `manim_imports_ext` belong to the upstream repository.

- Use [NarratedScene](narrated_scene.py) with exactly one `self.narrate(full_script)`
  block and one synthesis request. Use `en-US-Chirp3-HD-Achird` at default settings.
- Use SSML `<break time="..."/>` for pauses in the complete `<speak>` script.
  Keep delivery natural and neutral, and read formulas as mathematics. Time
  animations to the accepted recording; see [README.md](README.md) for controls.
- Verify audible wording and voice consistency. Automated transcripts support
  review; they do not establish that every word is clearly spoken.
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
