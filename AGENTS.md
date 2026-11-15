# Agent instructions

## Website changes

Follow [website/AGENTS.md](website/AGENTS.md) when changing the website's markup,
styles, or assets.

## Video changes

Follow [videos/AGENTS.md](videos/AGENTS.md) when authoring or changing Manim
scenes, narration timing, or video rendering.

## Working conventions

- Keep each component's tests in its `tests/` subfolder.
- Use `python3` for scripts needing only the standard library; use `uv run` in a
  Python package. `uv run --python VERSION` selects a Python version.
- Use `prek -a --quiet` for linting, through `uv run` when using this project's
  development dependencies.
- When fixing a bug, add the regression test first and confirm it fails without
  the fix when possible.
- Keep comments short and focused on information that is not obvious. Value the
  reader's time in code and prose.
- Use conventional commits and include an
  `Assisted-by: <harness>:<model>` trailer with the actual tool and model.
- Start PR descriptions and PR comments with the line `🤖 AI text below 🤖`. Keep PR
  descriptions short; describe validation beyond what CI already runs, without
  test plans or checkboxes.
