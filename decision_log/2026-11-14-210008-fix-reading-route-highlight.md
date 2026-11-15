# Make the reading-route highlight follow the current page

- Recorded at: 2026-11-14T21:00:08-08:00
- Observed work interval: 2026-11-14T20:53:35-08:00/2026-11-14T21:00:08-08:00
  (393 seconds elapsed, including clarification and an interrupted turn).
- Participants: user (bug report and clarification); OpenAI Codex, GPT-6
  (diagnosis, implementation, and validation).

## Context and decision

The user reported a bug with the Proof by Example button, then clarified that
the left button still looks selected after opening the general proof using the
right button. Update [ReadingRoutes](../website/node.jsx) so its filled button
matches the current reading-route page. Retain the example's initial emphasis
on other pages and the existing current-page accessibility marker.

This corrects the navigation added in the
[eight-node proof map](2026-11-14-151609-eight-node-proof-map.md).

## Rationale

The renderer assigned primary styling by button position (`index === 0`),
while `aria-current` already followed the current page. Derive the primary
route from that page, falling back to the first route outside the reading
routes. This keeps the static links and existing styling without client state.
The failing output directly exposed this mismatch, so additional instrumentation
and speculative cause testing were unnecessary.

## Evidence and outcome

- Initial navigation checks and browser clicks confirmed that the example link
  opens the correct page. Desktop hover/focus inspection did not establish a
  hover defect. Narrow-screen inspection also found left-aligned wrapped text;
  it was not the clarified bug, and no alignment change was made.
- Added the regression test before changing the renderer. Running
  `bun test proof-map.test.jsx --test-name-pattern 'highlighted reading route'`
  failed on the general-proof page because the filled example button lacked
  `aria-current="page"`. The test covers both reading-route pages, requiring
  exactly one filled button matching the current-page marker and title.
- After the fix, `make -C website check all` passed: 42 tests, 5,031 assertions,
  and 17 generated pages. A separate check of both built route pages confirmed
  that only their current route is filled.
- Repository lint passed using `uv run --locked prek -a --quiet` with writable
  temporary `UV_CACHE_DIR` and `PREK_HOME` locations after default cache writes
  were denied by the sandbox. Source whitespace checks passed.
- Post-fix visual inspection was not completed because the active Firefox
  window changed during inspection. Verification of the corrected selection
  used the rendered HTML and production output. No commit or deployment was made.

## Report relevance

This is an AI-assisted interface correction during the event. It changes
navigation feedback, with a regression check for the reported failure; no
mathematical content or claims changed.
