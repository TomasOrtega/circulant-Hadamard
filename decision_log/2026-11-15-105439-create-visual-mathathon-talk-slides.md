# Create the visual Mathathon talk slides

- Recorded at: 2026-11-15T10:54:39-08:00.
- Observed work interval: 2026-11-15T10:34:32-08:00/2026-11-15T10:54:39-08:00 (1207 seconds through authoring, review, rendering, and local PDF publication).
- Participants: Steven Creech (request and speaker plan); Tomas Ortega (design speaker named by the user); Codex/GPT-6 (deck integration, layout, notes, validation); three Codex/GPT-6 subagents (image/QR assets, proof frames, design frames and independent report-coverage review).

## Context and decision

The user requested a visual talk deck: begin with a QR code and website
link, open the website and show its first video, then have Tomas discuss
design principles and Steven explain the proof ideas. Use diagrams and
website images, with concise text preserving the key claims. Replace the
[slides template](../tex/slides.tex), compile [slides.pdf](../tex/slides.pdf),
and provide [timed speaker notes](../tex/talk-notes.txt).

Read the current report and prior
[report/figure decision](2026-11-15-103358-simplify-report-notation-and-add-proof-figures.md),
plus the participant and judge rules. Clarify that the LLM panel reads the
report, not the slides or presentation. Instead of crowding slides for an
LLM audience, keep important statements searchable and verify every
substantive slide claim against the report. Add the verified overview
runtime to the report so even that slide detail is represented there.

## Presentation choices

- Use a 16:9 PDF with a dark header, white background, blue highlights,
  readable equations, short takeaways, speaker-section footers, and source
  credits. No animations or external video embedding are required to read
  the PDF; the opening links to the website for playback.
- Main sequence: opening and full overview video; four design frames; eight
  proof frames; closing. Four optional backups cover the inner Delta graph,
  u=15, authentic website map captures, and sources/tools. Total: 18 pages,
  of which 14 form the main talk.
- Budget 4:25 for opening/video/brief navigation, 4:00 for Tomas, 9:00 for
  Steven, and 1:00 for closing. The notes total 18:25, leaving 1:35 within
  the twenty-minute presentation limit. The video is 214.933333 seconds,
  approximately 3:35, with a local file fallback identified in the notes.
- Put the exact website QR and clickable URL on both opening and closing
  frames. The opening thumbnail and button also link to the site.
- Use authentic website captures and native TikZ mathematical figures.
  Tall full-page maps would make labels too small in the main presentation,
  so redraw the eight-node map in a wide arrangement. Its ten dependency
  arrows exactly match website metadata; omit the context-only link into
  the independent Delta branch. Retain authentic maps as backup images.
- A focused Node 4.1 excerpt shows the deeper-node button, boxed statement,
  and written argument. A proposed Node 4.4 capture exposed a stale generic
  status label, so use the equally relevant Node 4.1 view instead. Neither
  screenshot nor website content was retouched. The status issue is outside
  this presentation task.
- Reuse the three-panel rotation/normalization figure for the design
  discussion, then show a larger two-panel rotation figure in the proof.
  Keep schematic geometry distinct from arithmetic residues and establish
  the contradiction through the normalized E-values and unit denominators.
- Mathematical review prompted explicit n-by-n dimensions, n>1 for the order
  restriction, Gaussian conjugation in star, the ring for the nine-position
  Delta theorem, the shared-sign origin of R and W's residue one, and the
  general odd-u norm and u²-term J(P) before the many-prime argument.
  Retain 1+i throughout, with no new shorthand pi. Cited arithmetic inputs,
  proof attribution, lack of Lean verification, and lack of measured
  educational outcomes remain clear.
- Credit the source proof to OpenAI's September 23, 2026 preprint. Credit
  human direction, Codex/GPT-6 assistance, ManimGL, 3Blue1Brown website and
  animation resources, Chirp 3 HD Achird, and faster-whisper in the talk and
  backups, consistent with the report.

## Evidence and observed outcome

- Both QR codes were independently decoded from the rendered final PDF
  pages 1 and 14 to `https://tomasortega.net/circulant-Hadamard/`.
  All opening/closing link annotations use that exact URL. The source QR
  was generated with CoreImage, medium error correction, a minimum four-
  module quiet zone, and no antialiasing; Apple's separate Vision decoder
  verified the saved PNG before the PDF check.
- Public HEAD requests returned HTTP 200 for the website and its opening
  video; their content types were HTML and video/mp4 respectively.
- Captures use Chromium at a 1280 CSS-pixel viewport and double pixel density.
  Only native graph disclosures were opened; assets preserve actual page
  content. The overview thumbnail is copied unchanged. Provenance is in
  [the asset README](../tex/assets/README.md).
- Independent report-coverage and mathematical reviews found no remaining
  scope gap after the explicit definitions above. All eight map nodes and
  ten proof edges were programmatically compared with website metadata.
  All fourteen timing intervals are continuous and total 18:25.
- Visually inspected every rendered slide. Initial integration produced
  several vertical overflows because the finished header and callouts were
  larger than the isolated draft wrapper. Tighten padding and remove
  duplicated prose, keeping mathematical labels and essential hypotheses.
  Translate the Beamer appendix bookmark to a plain PDF string; terminate
  template commands explicitly to satisfy ChkTeX. No blanket lint
  suppressions or frame shrink options were introduced.
- Final `make -C tex publish check check-pdfs` passes. Slides and report logs
  contain no LaTeX warnings, overfull/underfull boxes, or ChkTeX warnings.
  `uv run --locked prek -a --quiet` passes; new diagrams, image assets,
  and speaker notes were explicitly included in a second lint invocation.
  `git diff --check` passes.
- Published slides: 18 pages, 16:9. Final PDF SHA-256:
  `34ddbd849643a9ec206e2b939ea9a8a440b2b3edc5ce52eab4b9d2f6888459fc`.
  This matches the PDF independently decoded for the final QR check.
  The report remains 16 pages and its single-file flattened source remains
  available. Both PDFs and their fingerprint record were refreshed.
- Preserve pre-existing report work and website navigation edits. No
  website/video source, remote branch, PR, or competition submission was
  modified by this task. The report's final submission hash is still pending.

Delegated measured work on 2026-11-15 (offset -08:00): proof draft
10:35:23--10:43:51 (508s); visual assets 10:35:26--10:42:01 (395s);
design draft 10:35:39--10:38:08 (149s); claim/graph audit
10:44:42--10:46:03 (81s); final math/notes check
10:50:37--10:51:04 (27s); rendered QR/link audit
10:50:47--10:51:23 (36s). Intervals overlap and are not additive person-hours.

## Report relevance

Documents production of the presentation during the event and the distinction
between a visual human-facing talk and the text reviewed by the LLM panel.
The report carries all judged mathematical and expository claims. The deck
presents that work with diagrams, examples, source attribution, and a clear
speaker handoff; it does not introduce a new mathematical result or an
empirical claim about educational effectiveness.
