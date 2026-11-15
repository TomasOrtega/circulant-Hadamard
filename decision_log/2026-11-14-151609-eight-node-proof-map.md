# Implement the supplied eight-node proof map

- Recorded at: 2026-11-14T15:16:09-08:00
- Observed work interval: 2026-11-14T15:07:48-08:00/2026-11-14T15:16:09-08:00 (501 seconds).
- Participants: Steven Creech (request and supplied proof-map documents); Codex (GPT-6, implementation and checks).

## Context and decision

The user requested a pull before any implementation, the supplied high-level
proof graph, and a refreshed local website. Prioritize the order-36 example
($u=3$), with video scripts and smaller internal graphs deferred. Read the
local attachments `Circulant_Hadamard_Codex_Spec.md` and
`Circulant_Hadamard_Website_Proof_Map.pdf` from the user's Downloads directory.
Treat their mathematical content and design requirements as reference material
for this request, not as authorization to publish or invent further proofs.

`git pull --ff-only` completed before implementation and reported already up
to date at `13d797e`. The earlier untracked preview decision record was preserved.

Replace the active placeholder hierarchy with eight named statement nodes,
a theorem conclusion, and example/general reading routes. Preserve the former
12-node outline under [website/archive/nodes/](../website/archive/nodes/), outside
the active build. This supersedes the provisional content hierarchy in the
[recursive lesson decision](2026-11-14-002050-recursive-lesson-hierarchy.md), while
retaining the [Markdown format](2026-11-14-013449-markdown-node-authoring.md).
Active pages now have descriptive URLs; old draft URLs are not redirected.

## Rationale

Keep the existing static React rendering, MathJax, fonts, colors, and video
workflow. Use a vertical SVG map to preserve the supplied branch arrangement
without an extremely wide horizontal graph. Add only a purple arithmetic
color to the upstream palette; leave the vendored CSS untouched. Represent the
1-to-4 notation link separately as `contextFrom`, with a dashed arrow, so it
does not falsely become a logical prerequisite. The Δ-theorem remains independent
of Hadamard signs. Use stable node numbers and explicit map positions.

Supplemental example/general pages are reading routes, not extra proof nodes.
Every statement starts with the order-36 case and then gives the general
statement. Keep Propositions 2.2 and 3.4 labeled accepted black boxes, retain
empty video slots, and create no internal proof graphs. A collapsed parent-map
disclosure on statement pages improves access to their text; incoming and
outgoing dependency lists remain explicit links. Add selectable text/LaTeX
alongside the rendered equations. Compact empty video placeholders retain their
purpose while making the graph easier to reach. No video narration is authored;
unset cut scripts continue to fall back to statement summaries.

## Evidence and outcome

- Read the supplied PDF text and visually inspected its graph page.
- Retrieved the cited [primary paper](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf)
  and checked Theorem 1.1 and Propositions 2.2 and 3.4 against the supplied
  statements. This was a source/statement check, not an independent verification
  of the paper's full proof. The website attributes the exposition to this paper.
- Preserve the distinction between exact complex equality and reduction modulo
  $(1+i)$. Denominators are units after inverting odd $u$; division by 2 or
  $1+i$ is performed in characteristic zero before reduction. The order-36
  example is explicitly distinguished from the general conclusion.
- Adapted tests tied to retired placeholder content, retaining hierarchy,
  foundation, link, math-rendering, and video checks. New tests check all 11
  logical arrows, the single dashed notation arrow, branch styling, exact node
  titles, example-first navigation, deferred deeper graphs, dependency links,
  and selectable equation source.
- All 34 tests passed (955 assertions); the production build emitted 12 pages.
  Exhaustive arithmetic over the 16 possible four-sign columns checks the
  supplied coefficient identity for E. The order-four matrix's row inner
  products are also checked. Neither finite check proves the general theorem.
- The existing localhost server served the new build with HTTP 200; opened it
  in the user's browser. Desktop screenshot inspection found readable labels
  and unobstructed graph arrows. A 390-pixel screenshot appeared clipped, but
  browser measurements showed Chrome had a minimum 500-pixel viewport and no
  document overflow at that width; the narrower image was a cropped capture.
  A subsequent 500-pixel screenshot confirmed readable navigation, wrapping
  prose, and rendered equations. No 390-pixel browser validation is claimed.
- The required `uv run --locked prek -a --quiet` exited zero but reported the
  moved, unstaged old paths as missing. A follow-up lint of existing tracked
  and new files passed for all 88 existing files. Sandbox retries were approved for Git,
  network/cache access, browser launch, and local HTTP checks.
- No publication, commit, push, or change of Git remotes was requested or made.

## Report relevance

This is AI-assisted website exposition and navigation work based on the user's
supplied map and an existing cited paper. It adds no claimed new mathematics.
The accepted propositions, draft exposition status, absent video material, and
deferred internal proofs remain visible. Subsequent video-script work can edit
[the active Markdown nodes](../website/nodes/) and the overview's cut scripts.

Final verification recorded at 2026-11-14T15:16:50-08:00; follow-up interval
2026-11-14T15:16:09-08:00/2026-11-14T15:16:50-08:00. The narrow-view screenshot and
explicit-file lint checks passed; source whitespace checks also passed.
