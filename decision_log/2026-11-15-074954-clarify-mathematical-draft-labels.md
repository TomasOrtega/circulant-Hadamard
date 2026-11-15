# Clarify mathematical draft labels

- Recorded at: 2026-11-15T07:49:54-08:00
- Observed work interval: 2026-11-15T07:49:23-08:00/2026-11-15T07:49:54-08:00 (31 seconds).
- Participants: Tomas Ortega (follow-up question); OpenAI Codex, GPT-6 (metadata and history review).

## Context and decision

Following the [video completion audit](2026-11-15-074847-audit-node-video-completion.md),
the user asked which mathematical sections are drafts. Report the existing
metadata by main section and subsection range, without treating the flags as
an independent assessment of missing arguments. Retain all current statuses.

## Rationale

[Website instructions](../website/AGENTS.md) define `draft: true` as unfinished
proof status. However, it is currently applied to every active node, including
nodes whose arguments were subsequently developed. The
[refined exposition record](2026-11-15-031809-develop-all-refined-node-exposition-and-scripts.md)
documents supplied arguments and removal of specific black-box metadata;
the [video acceptance record](2026-11-15-072130-accept-all-scripted-node-videos.md)
explicitly preserves mathematical draft status. These labels alone do not
identify particular proof gaps.

## Evidence and outcome

- The website parser confirms `draft: true` on all 48 nodes: the overview,
  eight main sections, and 39 subsections.
- Subsection ranges are 1.1–1.5, 2.1–2.6, 3.1–3.5, 4.1–4.6, 5.1–5.3,
  6.1–6.5, 7.1–7.4, and 8.1–8.5.
- Both supplementary reading guides, General Odd-u Proof and Proof by
  Example: n = 36, also retain the flag, giving 50 active pages in total.
- This was a status inventory and historical clarification, not a new
  mathematical correctness review. Only this decision record was added.

## Report relevance

Distinguishes completed explanatory media and developed written arguments
from retained draft metadata. No new proof or formal verification is claimed.
