# Show slide progress in the footer

- Recorded at: 2026-11-15T11:05:18-08:00.
- Observed work interval: 2026-11-15T11:04:46-08:00/2026-11-15T11:05:18-08:00 (32 seconds through build and visual verification).
- Participants: Steven Creech (request); Codex/GPT-6 (implementation and checks).

## Context and decision

The user requested slide numbers such as 1/18 and 2/18 to show progress.
Update the shared footer in [slides.tex](../tex/slides.tex) to use Beamer's
current and total frame counts. Enable the footer on the opening slide.
This follows the [corner QR change](2026-11-15-110415-put-website-qr-in-every-slide-corner.md).

## Rationale

Automatic totals stay correct if frames are added or removed. Include the
four backup slides in the total, matching the requested 18-page sequence.
Retain the reserved space beside the QR code.

## Evidence and outcome

Rebuilt and published [slides.pdf](../tex/slides.pdf). Text extraction verifies
all 18 pages show their corresponding number from 1/18 through 18/18.
The opening slide was visually inspected: its footer and QR remain clear.
`make -C tex publish check check-pdfs` passes with no LaTeX warnings or box
overflows. No mathematical content changed.

## Report relevance

A small presentation navigation improvement requested by the speaker,
implemented and checked with AI assistance.
