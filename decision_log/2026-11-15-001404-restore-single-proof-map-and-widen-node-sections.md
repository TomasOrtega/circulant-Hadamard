# Restore the single proof map and widen node sections

- Recorded at: 2026-11-15T00:14:04-08:00
- Observed work interval: 2026-11-15T00:09:03-08:00/2026-11-15T00:14:04-08:00
  (301 seconds through this record).
- Participants: Steven Creech (layout and navigation request); OpenAI Codex,
  GPT-6 (implementation, delegated routing work, preservation audit, and QA).
- Delegated route implementation: 2026-11-15T00:09:28-08:00/2026-11-15T00:11:43-08:00
  (135 seconds).
- Preservation baseline: 2026-11-15T00:10:10-08:00/2026-11-15T00:11:22-08:00
  (72 seconds). Final comparison: 2026-11-15T00:12:58-08:00/2026-11-15T00:13:19-08:00
  (21 seconds). Delegated intervals overlap the primary interval.

## Context and decision

Steven requested that “Dig in deeper” sit beneath each node heading rather
than occupy a sidebar that narrows the exposition. He also requested restoring
one proof journey: overview videos use order 36 as a guiding example, while
exploring deeper nodes develops the general case.

Move each child section's button and short status label into a wrapping row
below its heading in [node.jsx](../website/node.jsx). Let its explanation
span the section's full content width and retain its centered video excerpt.
Use the same arrangement at every depth and existing Tailwind styles.

Remove the example/general route selector and standalone route generation.
Keep the old route URLs as redirects to the homepage, including existing
compatibility redirects for deeper general-proof URLs. Preserve both guides'
source prose outside the build and update website documentation.

This restores the intent of the
[single proof journey](2026-11-14-182210-unify-example-and-general-proof-journey.md)
and supersedes the decision to retain upstream route pages during the
[latest sync](2026-11-14-231839-sync-working-checkout-with-main-and-preserve-drafts.md).

## Rationale

The sidebar reserved fourteen rem plus a gap even when it held only a button
and a short label. Moving that content above the explanation recovers the
reading width and keeps the action near the section title. Removing the
parallel routes from both renderer and build avoids separate video views,
while redirects preserve old links. Existing general statements and examples
remain in the shared node hierarchy; no mathematical content was rewritten.

Use the Sites skill's local workflow with the established repository build
and preview. No registration, hosted deployment, or Git publication is part
of this request.

## Evidence and outcome

- Added regressions before implementation. The button-order and split-selector
  tests both failed; the route agent also observed three expected failures
  for extra pages, selector visibility, and missing homepage redirects.
- `make -C website check` passes 129 tests with 7,904 assertions. The pinned
  Bun build emits 48 node pages and compatibility redirects. Both required
  Make targets complete successfully.
- Browser checks at 1440px and 390px confirm the button follows its heading,
  prose fills the available content width, no sidebar remains, and no page
  overflow occurs. A deeper Node 3 section has the same arrangement.
  Desktop and mobile screenshots were visually inspected. Temporary evidence:
  `/private/tmp/circulant-single-map-layout-qa.json` and matching PNG files.
- Independent comparison confirms all 9 video records, 18 cut timings,
  18 media-file hashes, and 27 script-file hashes are unchanged. Baseline:
  `/private/tmp/circulant-flow-preservation-20261115-001010.json`.
- Repository lint passes with mutating hooks skipped to protect unrelated
  unfinished script formatting; scoped whitespace checks also pass.
- A low-disk-space error interrupted one attempted agent launch and shell
  heredoc. Removed only the redundant temporary Bun download archive after
  confirming its extracted executable remained available; work then continued.
  Recovery snapshots and user files were preserved.
- The existing port-8000 preview returns HTTP 200 and serves the rebuilt
  site. Opened its homepage for Steven. No commit, push, or PR was created.

## Report relevance

Records user-directed refinement of the reading flow and AI-assisted layout,
redirect, and preservation checks. The changes affect presentation and
navigation, not the mathematical claims, video content, or production scripts.

Final checks observed at 2026-11-15T00:14:20-08:00 (317 seconds since task start): all applicable lint hooks passed on the edited files and this record. The temporary headless browser exited, and its disposable profile was removed; screenshots, audit data, and the existing local preview remain available.
