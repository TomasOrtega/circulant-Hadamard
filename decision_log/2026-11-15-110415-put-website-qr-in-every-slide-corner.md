# Put the website QR in every slide corner

- Recorded at: 2026-11-15T11:04:15-08:00.
- Observed work interval: 2026-11-15T10:56:39-08:00/2026-11-15T11:04:15-08:00 (456 seconds through implementation and final rendered QR verification).
- Participants: Steven Creech (request); Codex/GPT-6 (implementation and review); Codex/GPT-6 subagent (independent QR, link, and layout audit).

## Context and decision

Following the [talk deck decision](2026-11-15-105439-create-visual-mathathon-talk-slides.md),
the user requested the website QR code in a bottom corner of every slide.
Use a shared bottom-right placement in [slides.tex](../tex/slides.tex),
including the plain opening and all backup frames. Remove the old large
opening and closing copies so each of the 18 pages has exactly one QR.
Reflow those two frames and preserve their visible website links.

## Rationale

A shared Beamer background keeps the linked QR in the same location on
all pages. Use a 1.05 cm square, 1.5 mm from the right and 1 mm from the
bottom. Move page numbers left and reserve a 12 mm right-hand gutter in
source credits and takeaway boxes. This keeps existing text sizes and
provides the QR's white border without reducing the whole slide's content
height. Update asset documentation and speaker notes accordingly.

## Evidence and outcome

- An initial rendered check found that callout boxes on pages 7 and 12
  covered part of the QR. The final gutter fixes this; all 18 full-page
  renders at 1920 pixels wide now independently decode exactly one QR to
  `https://tomasortega.net/circulant-Hadamard/` using Apple's Vision decoder.
- PDFKit confirms each QR occupies the bottom-right corner and has exactly
  one enclosing link annotation to that same URL, entirely within the page.
- Independent visual review of dense frames 7, 10, 11, and 12 confirms
  readable text, unobstructed QR margins, and no footer collisions. The
  delegated audit ran 2026-11-15T10:58:07-08:00/2026-11-15T11:04:07-08:00
  (360 seconds including rebuild waits; overlaps the main interval).
- Visual review caught Beamer consuming the closing frame's first grouped
  text as a subtitle after its columns were removed. An explicit paragraph
  restores the metric line. Opening and closing content remains visible;
  the opening runtime is placed on its own line.
- `make -C tex publish check check-pdfs`, `uv run --locked prek -a --quiet`,
  and `git diff --check` pass. The slide log has no LaTeX warnings or
  overfull/underfull boxes. The deck remains 18 pages.
- Final [published PDF](../tex/slides.pdf) SHA-256:
  `200ccf00c12b29967759d3c3dfbe6126b4bc96e8900e8dae63e393dde8381cfc`.
  Its fingerprints were refreshed through the existing publication command.
- Digital decoding is verified; physical scanning from an auditorium
  projection has not been measured. Mathematical content is unchanged.

## Report relevance

This is a presentation-navigation refinement following the user's request,
with AI-assisted layout work and independent rendered-output checks.
It adds convenient access to the website throughout the talk and does not
change the report's mathematical or educational claims.
