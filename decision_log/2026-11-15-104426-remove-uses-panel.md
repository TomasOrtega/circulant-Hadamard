# Remove the redundant Uses panel

- Recorded at: 2026-11-15T10:44:26-08:00
- Observed implementation and validation interval: 2026-11-15T10:42:46-08:00/2026-11-15T10:44:26-08:00 (100 seconds).
- Participants: Tomas Ortega (issue and minimal-change request); OpenAI Codex,
  GPT-6 (implementation and checks).

## Context and decision

[Issue #22](https://github.com/TomasOrtega/circulant-Hadamard/issues/22)
requests removal of the website's “Uses” section. Delete the shared
`NodeDependencies` renderer and its call, including its repeated notation row.
Remove the obsolete prerequisite-panel assertions and authoring-guide sentence.
Retain dependency metadata, validation, graph links, and accessible graph labels.
This continues the simplification that
[removed the “Used by” row](2026-11-15-094840-wrap-deeper-links-beside-headings.md).

## Rationale

Removing the single-use renderer eliminates the panel and its calculations
without adding CSS or client code. The proof maps already expose dependencies
and notation links. An isolated worktree keeps this issue separate from the
concurrent page-controls work for issue #21 and preserves its
[existing deeper-link layout](2026-11-15-102040-right-align-deeper-links-and-counts.md).

## Evidence and outcome

- The rendered-page regression failed on `group-ring-encoding` before removal
  and passed afterward. All 181 website tests pass (9,666 assertions), including
  graph navigation and dependency validation.
- `make -C website -o node_modules/.installed check` and the corresponding
  website build pass. The flag prevents reinstalling the existing dependencies
  shared read-only with the main worktree.
- Inspection of all 98 generated HTML files finds no visible “Uses” text or
  prerequisite panel; all 48 active node pages retain their dependency graph.
  Redirect pages are excluded from the graph assertion.
- `uv run --locked prek -a --quiet` and `git diff --check` pass. The change
  removes 22 production lines and changes no mathematical content or assets.
- No publication or browser review was performed in this isolated task.
  Integration with issue #21 must remove the now-obsolete ancestor condition
  from its explanation-section wrapper to avoid empty sections.

## Report relevance

Records a user-directed interface removal and its automated checks. It adds
no mathematical result or proof verification claim.

## Integration with issue #21

- Recorded at: 2026-11-15T10:49:11-08:00
- Observed integration interval: 2026-11-15T10:48:18-08:00/2026-11-15T10:49:11-08:00 (53 seconds).
- Rebase onto `16b6087` and resolve the renderer overlap. The explanation
  section now renders only when `showOwnExplanation && !hasOwnProofMap`,
  and its inner Markdown needs no repeated condition. This completes the
  integration noted above while preserving the original implementation history.
- An added empty-section assertion failed on `group-ring-encoding` with the
  old ancestor condition and passes with the narrower condition.
- All 181 tests pass (9,620 assertions), the integrated website builds,
  repository lint passes, and whitespace checks pass. All 98 generated pages
  omit the panel; all 48 active pages retain their graphs, contents controls,
  dark-mode controls and bootstrap, literal-white corner controls, and no empty
  sections. The source diff preserves issue #21's scripts, styles, bootstrap,
  and documentation.
