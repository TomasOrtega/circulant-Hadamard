# Restore visible map borders and round arrow bends

- Recorded at: 2026-11-14T21:24:04-08:00
- Observed work interval: 2026-11-14T21:18:20-08:00/2026-11-14T21:24:04-08:00
  (344 seconds through this record, overlapping the issue fixes).
- Participants: user (visual correction); OpenAI Codex, GPT-6 (implementation
  and validation).

## Context and decision

The user reported invisible node borders and overly sharp arrow corners after
the [proof-map restyling](2026-11-14-211554-align-proof-map-with-upstream-style.md).
Restore persistent blue outlines at 40% opacity in the shared graph renderer.
Replace the two outer elbow routes with quadratic bends of radius 12 SVG units.
Retain the stronger current, hover, and keyboard-focus treatment.

This revises the earlier choice to reserve outlines for interaction. That first
implementation was committed and pushed as
[91b7939](https://github.com/TomasOrtega/circulant-Hadamard/commit/91b793945f8feb1c6db71f77c0fbe4124f392073);
the push and matching local/remote tips were observed at 21:17:09-08:00.

## Rationale

Visible outlines distinguish white nodes inside the white parent-map disclosure.
Rounded stroke joins alone only soften corners by the stroke width; curved
path segments give the larger, visible bends the user requested. Preserve the
arrow endpoints, positions, and dependency semantics.

## Evidence and outcome

- Before implementation, the updated border check and new curved-route check
  failed: the border was transparent and both bends lacked quadratic segments.
- The combined final website check passed: 46 tests, 5,129 assertions, and
  17 generated pages. Repository lint and whitespace checks passed.
- Safari inspection confirmed the blue outlines and visibly curved outer
  connections. Reload From Origin refreshed previously cached compiled CSS.
  Mathematical statements, node positions, and graph connections are unchanged.

## Report relevance

This is a user-directed correction to the AI-assisted visual design. It records
the revised choice and observed result without claiming new mathematics.
