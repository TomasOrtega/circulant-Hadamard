# Remove the copyable-source dropdown

- Recorded at: 2026-11-14T21:04:33-08:00
- Observed work interval: 2026-11-14T21:03:47-08:00/2026-11-14T21:04:33-08:00
  (46 seconds through this record).
- Participants: user (removal and publication request); OpenAI Codex, GPT-6
  (implementation and checks).

## Context and decision

The user requested removal of the “Copyable text and LaTeX” dropdown and asked
for a commit and push. Remove it from the shared Markdown renderer in
[node.jsx](../website/node.jsx), update the existing statement-page check,
and remove its description from the website authoring guide.

This reverses the source-disclosure choice in the
[eight-node proof-map decision](2026-11-14-151609-eight-node-proof-map.md).
Include the earlier [reading-route highlight fix](2026-11-14-210008-fix-reading-route-highlight.md)
and its regression test in the requested publication on the current `main` branch.

## Rationale

Removing the shared disclosure eliminates the duplicate source interface
throughout the website. Rendered prose, equations, and parent-map disclosures
continue through their existing components. No content files or dependencies
need to change.

## Evidence and outcome

- `make -C website check all` passed: 42 tests, 5,031 assertions, and 17 built pages.
- Inspection of all 17 generated HTML pages confirmed that none contains the
  source dropdown or its preformatted source block, and all retain rendered math.
  The general proof retains its parent-map disclosure.
- Repository lint passed using `uv run --locked prek -a --quiet` with writable
  temporary `UV_CACHE_DIR` and `PREK_HOME` directories; `git diff --check` passed.
- `git fetch origin` succeeded. Local `main` and `origin/main` had no differing
  commits before publication. Commit and push outcomes will be recorded after
  those actions complete.

## Report relevance

This is a user-requested interface simplification and publication of two
AI-assisted website changes. Mathematical content and claims are unchanged.
