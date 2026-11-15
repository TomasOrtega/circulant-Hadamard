# Write the Mathathon report and proof exposition

- Recorded at: 2026-11-15T10:12:32-08:00.
- Observed work interval: 2026-11-15T09:55:40-08:00/2026-11-15T10:12:32-08:00 (1012 seconds through authoring, review, compilation, and visual checks).
- Participants: Steven Creech (request, report vision, track selection); Codex/GPT-6 (integration and writing); three Codex/GPT-6 subagents (rules and workflow research, mathematical drafting and independent review, TeX environment and style checks).

## Context and decision

The user requested a report explaining the website's recursive proof-map
approach, example-led exposition, narrated animations, interactive elements,
and audio-first workflow, followed by a readable general proof. The user
selected **Algebra/Number Theory** in the clarification reply. Expand
[report.tex](../tex/report.tex), update shared metadata and bibliography, and
compile the linked PDF. This task does not publish a PR or submit the report.

Read all four participant/judge documents in [rules](../rules/README.md).
A subagent compared the live official pages against the local copies and
found no substantive differences after normalizing links and whitespace.
The rules say human judges score presentation and Q&A, while the LLM panel
reads the report without the title block; links do not replace report content.
Keep a short website route near the front, but put the mathematical argument,
evidence, contribution, and attribution in the report itself. Keep rendered
team identity and project links in the title block. The live companion site
is https://tomasortega.net/circulant-Hadamard/ (HTTP 200 confirmed after its
09:57:50-08:00 Pages deployment).

Follow the existing latexpand workflow: editable sources remain modular;
`tex/build/report.tex` is the single-file deliverable with an inline
bibliography and inline TikZ figure. Set the submission hash explicitly to
“To be set at submission”; no final submission revision has been selected.

## Mathematical and editorial choices

- Attribute the mathematics to OpenAI's September 23, 2026 preprint. Replace
  the earlier abstract's unverified October 6 release description with the
  paper's observed date. The contribution is exposition and implementation,
  not a new proof or a new nonexistence result at order 36.
- Explain the overview / eight main nodes / 39 refined nodes hierarchy and
  use the hypothetical order-36 case as a guide to the general argument.
  Describe this as a reading strategy, not an experimentally established
  learning benefit. Describe the figure in words for text-only judging.
- Preserve explicit polynomial arguments and the sign assumption in the
  matrix dictionary. Include the power-of-two descent proving oddness of u,
  CRT coordinate relabeling, exact halving, local comparison, Delta
  integrality and Kronecker, the expanded E identity, rigidity, and the
  products-to-sums contradiction for all odd u greater than one.
- An initial early-proof draft cited the entire oddness restriction. Revise
  it to supply the descent itself so that only the underlying cyclotomic
  basis/valuation facts remain cited inputs. This follows the distinction
  established in the [content-completeness review](2026-11-15-075252-review-actual-mathematical-content-completeness.md).
- State the extended valuation and the local coefficient ring explicitly.
  Require an odd prime in the counterexample to dropping the matching norm
  and cycle exponents. These clarifications came from independent review.
- Use the common ring A obtained by inverting odd u; prove its quotient
  modulo 1+i is nonzero, without assuming the quotient is a field. Establish
  denominator units and cancel scalars before reduction. In the example,
  compare normalized E values, not equal unnormalized residues. A geometric
  rotation is not a direction in which a residue becomes zero.
- Include both human editorial choices and AI assistance. Distinguish the
  production Chirp 3 HD Achird narration from earlier Gemini experiments;
  explain continuous audio first and animation timing afterward. Credit
  ManimGL, 3Blue1Brown website styles and animation guidance, and
  faster-whisper alignment. Do not claim all recordings received complete
  human listening review or that ASR establishes audibility.

These decisions build on the [refined-node exposition record](2026-11-15-031809-develop-all-refined-node-exposition-and-scripts.md),
[continuous-narration decision](2026-11-14-173541-enforce-continuous-narration.md),
and [video acceptance record](2026-11-15-072130-accept-all-scripted-node-videos.md).

## Evidence and observed outcome

- Compared the mathematics with the primary source PDF (Sections 2--4,
  Lemma 2.1, Proposition 2.2, Lemma 3.1, Proposition 3.4, and Lemma 4.1).
  Independent reviewers found no substantive errors after the clarifications.
  These are written proofs relative to stated cited facts, not Lean proofs
  or a formal certification of the source paper.
- Verified the actual node/video count and production voice metadata. The
  finite 27-case phase check is identified as evidence for the illustration,
  not for general mathematical nonexistence.
- Final `make -C tex publish check check-pdfs` passed, as did
  `uv run --locked prek -a --quiet` and `git diff --check`.
  The report is **14 pages**, with no LaTeX warnings, unresolved references,
  overfull boxes, underfull boxes, or ChkTeX warnings in the final build.
- Inspected rendered opening, graph, mathematical, and bibliography pages.
  Added explicit line breaks in graph labels to avoid awkward hyphenation.
  The flattened source has an inline bibliography and no input, include,
  or external-image dependencies.
- Added Latin Modern fonts to the shared preamble to resolve missing T1
  bitmap fonts. Followed the [PDF freshness workflow](2026-11-15-084535-publish-linked-pdfs-with-ci-freshness-checks.md):
  refreshed both checked-in PDFs and their fingerprint record. The slides'
  text remains its existing template; developing slides is a separate task.
- Missing TeX packages and helper executables were installed under
  `/private/tmp` only. User-mode tlmgr could not install nonrelocatable
  latexpand/chktex, so official CTAN archives supplied temporary helpers.
  The reproducible session environment is
  `/private/tmp/circulant-report-tools/env.sh`; no global TeX tree was changed.
- Initial build failures were a TikZ style name colliding with its built-in
  `step` key and missing fonts; rename the style and use Latin Modern.
  ChkTeX spacing/brace warnings and long-URL bibliography formatting were
  corrected without blanket lint suppressions. An initial lint run needed
  approved access to uv's existing cache and removed trailing whitespace.
- Preserved the pre-existing website navigation changes and prior decision
  records. No website source was changed by this report task.

Measured delegated intervals (all 2026-11-15, offset -08:00) overlap and
must not be added as person-hours: rules research 09:56:08--09:59:57 (229s);
early proof 09:56:22--09:59:31 (189s); late proof 09:56:39--10:02:07 (328s);
math audit and early-proof expansion 10:02:53--10:04:51 (118s);
build environment 10:03:02--10:06:05 (183s); integrated math audit
10:07:09--10:07:35 (26s); rules/factual audit 10:08:42--10:09:56 (74s);
TeX style and layout checks 10:08:21--10:10:29 (128s).

## Report relevance

This record documents preparation of the report itself during the event,
including source verification, contribution framing, AI assistance, proof
review, limitations, and deliverable checks. The source theorem and standard
arithmetic are prior work. Educational effectiveness is a design goal; no
user study, formal verification, or new theorem is claimed. The report is
ready for the user's editorial review, with its final submission hash still
pending.
