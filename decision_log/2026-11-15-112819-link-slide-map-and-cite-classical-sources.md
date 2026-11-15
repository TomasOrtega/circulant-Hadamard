# Link the slide map and cite classical sources

- Recorded at: 2026-11-15T11:28:19-08:00.
- Observed work interval: 2026-11-15T11:25:50-08:00/2026-11-15T11:28:19-08:00 (149 seconds through implementation and checks).
- Participants: Steven Creech (request); Codex/GPT-6 (research, edits, validation).

## Context and decision

Make the eight nodes on slide 2 open their corresponding inner website
pages. Add historical citations to the report for the conjecture and
classical order restriction. This follows the [report PR](2026-11-15-110657-prepare-report-and-slides-pr.md),
which GitHub now reports merged. Prepare a follow-up branch from current
main instead of updating the closed PR.

## Rationale

Use PDF hyperlinks around each graph label, targeting the site's existing
`nodes/<slug>/` routes. Keep the graph's layout and add a brief click cue.
Cite Ryser's 1963 book for the traditional attribution and Turyn's 1965
paper for oddness of u and exclusion of prime-power u greater than one.
Distinguish the historical result from the streamlined descent used in
OpenAI's Proposition 2.2. No mathematical deduction changes.

## Evidence and outcome

- Verified all eight live node URLs return HTTP 200 and HTML. The compiled
  slide's PDF annotations contain the eight distinct correct node URLs.
  Visually inspected slide 2; labels, arrows, QR, and numbering remain clear.
- Consulted Turyn's [original article](https://msp.org/pjm/1965/15-1/pjm-v15-n1-p32-p.pdf),
  especially the Hadamard difference-set discussion and Theorem 8 with its
  corollary on pages 335--336. The 2026 source also identifies Corollary 2
  to Theorem 6 on page 333 for the prime-power exclusion.
- Verified Ryser's book metadata against the publisher's Cambridge listing:
  Herbert John Ryser, Combinatorial Mathematics, Carus Mathematical
  Monographs 14, Mathematical Association of America, 1963,
  DOI 10.5948/UPO9781614440147. The conjecture attribution is corroborated
  by the source preprint; no claim of directly reading page 134 is made.
- Added both original references to the bibliography and citations at the
  introduction, historical discussion, and order-restriction statement.
- `make -C tex publish check check-pdfs`, repository lint, and whitespace
  checks pass. Fixed one nonbreaking-space warning before final publication.
  Logs have no LaTeX warnings or box overflows; report and slides remain
  16 and 18 pages. PDF freshness also passes in the isolated PR worktree.
- Preserve the local copies of the revised PDFs and sources as well as the
  follow-up branch. Separate website edits remain untouched.

## Report relevance

Improves credit for prior mathematical work and makes the visual proof map
an entry point to the detailed exposition. Adds no new theorem claim.

## Publication outcome

At 2026-11-15T11:28:35-08:00, opened [PR #27](https://github.com/TomasOrtega/circulant-Hadamard/pull/27)
from `steven/slides-links-historical-citations` to `main`. The PR includes
the rebuilt PDFs and this decision record; it has not been merged.
