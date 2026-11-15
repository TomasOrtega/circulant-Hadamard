# Draft Node 4 with phase-circle visuals and an inner proof outline

- Recorded at: 2026-11-14T19:51:52-08:00
- Observed work interval: 2026-11-14T19:43:59-08:00/2026-11-14T19:51:52-08:00 (473 seconds through this record).
- Participants: Steven Creech (six-section narration outline and request for
  phase visualizations); OpenAI Codex, GPT-6 (integration, delegated source
  review, script/storyboard and leaf drafting, and validation).
- Delegated intervals: mathematical review,
  2026-11-14T19:44:15-08:00/2026-11-14T19:45:35-08:00 (80 seconds);
  script/storyboard,
  2026-11-14T19:46:10-08:00/2026-11-14T19:49:29-08:00 (199 seconds);
  six leaf pages,
  2026-11-14T19:46:21-08:00/2026-11-14T19:49:00-08:00 (159 seconds).
  These overlap the primary interval and are not additive person-hours.

## Context and decision

Steven supplied a Node 4 overview titled “From a Circle to Roots of Unity”:
evaluate a norm-nine polynomial on a circle, define the relative phase,
state the Δ-theorem and its general alternating product, explain integrality
and Kronecker, then connect the result to c, d, and g. He requested visual
directions showing phases and what the plotted objects represent.

Save the edited draft in
[scripts/node4/delta-theorem.md](../website/scripts/node4/delta-theorem.md).
Preserve the six-section sequence and add detailed animation cues. Embed a
native SVG [three-panel storyboard](../website/scripts/node4/storyboards/phase-circles.svg)
for evaluation values, the quotient's angle, and the allowed cube-root
directions. Use a light background for the readable production reference;
the script retains the video's black-background production convention.
No Manim scene, narration audio, video source, or cut timing is created.

Expand [Node 4](../website/nodes/delta-theorem.md) into six general-u steps:
circle evaluations, alternating product, local character comparison,
integrality, Kronecker, and odd order. Edges are 4.1→4.2, 4.1→4.3,
4.2→4.4, 4.3→4.4, 4.2→4.5, 4.4→4.5, 4.3→4.6, and 4.5→4.6.
Keep the independent main-map branch, existing palette, solid arrows,
video/graph/subsection order, and main-page theorem card.

This refines the original
[accepted-Proposition-3.4 decision](2026-11-14-151609-eight-node-proof-map.md).
Remove the whole-node black-box label and identify the actual deferred
input inside Node 4.3: Lemma 3.1. Kronecker remains an explicit black box
as Steven requested. The general integrality and order arguments are written
out, conditional on those accepted inputs. This is an exposition outline,
not a claim that the full technical local lemma has been developed here.
Update the website and script indexes, following the
[Node 3](2026-11-14-183958-draft-node-three-evaluations-and-keep-u.md) and
[Node 5](2026-11-14-193748-draft-node-five-all-ones-congruence.md) workflow.

## Rationale

Use the exact Gaussian example f(P)=3iP. Its norm is 9; its nine evaluation
points are 3i times the ninth roots. The two chosen values have phases 90°
and 210°, so f(1)/f(ω)=ω² has phase −120°=240°. Rotate from denominator
to numerator. Distinguish root inputs from evaluated outputs and explain
that equal spacing is specific to this example. It is not a Hadamard sign
row. Label a freely rotating arrow as what magnitude alone permits, not a
family of admissible norm solutions.

The arithmetic must not be inferred from the circle picture. All conjugates
have modulus one, but integrality is a separate hypothesis. The deeper
Kronecker page includes (3+4i)/5 as a nonintegral counterexample with both
conjugates on the unit circle. The local comparison requires matching
exponents: a cyclic component of order p^e and scalar product p^e times a
unit. Comparing raw residues before dividing is insufficient.

Pairing subsets in every prime direction supplies local units of residue
one. The norm handles the remaining primes, and membership in every
localization establishes integrality. Kronecker then gives finite order.
Residue one in characteristic p forces p-power order by the geometric-sum
argument. Since p divides odd u, the order is odd. Record the stronger
consequence Δ=1 for two distinct prime divisors; keep odd order as the
main statement needed later. For u=3, the degree-four field Q(i,ω) cannot
contain a root of order 9 or a higher power of 3, leaving 1, ω, and ω².

## Evidence and outcome

- Independent mathematical review checked the claims and local hypotheses
  against the primary paper, Section 3, Lemmas 3.1 and 3.3 and Proposition 3.4.
  The pages cite the [official paper](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
  This checks the exposition against that source; it is not a new research
  result or formal verification of the full circulant Hadamard argument.
- The new graph check failed before expansion. The first full run exposed
  two existing tests that compared unescaped titles with HTML; the apostrophe
  in “Kronecker's Theorem” revealed that assumption. Use rendered text in
  those expectations, preserving the navigation and heading checks. Move
  the terminal-page fixture to the still-terminal Odd-Order Rigidity page.
- All 50 tests pass, with 6,140 assertions. The build emits 35 pages. New
  checks cover the DAG, explicit accepted inputs, script math and storyboard
  reference, nine example magnitudes, and the quotient's orientation. The
  finite complex calculations illustrate the example, not the general theorem.
- Required lint completed with the known missing-old-path notices from
  earlier unstaged route moves. Explicit lint of all 186 existing files
  passed. Whitespace checks passed. SVG XML, accessible title/description,
  and its plotted coordinates were checked during drafting.
- Browser inspection confirmed readable storyboard labels and the clockwise
  relative rotation, a six-node graph without obscured arrows, and readable
  math on the circle-evaluation page at a 500px viewport. Split the ring
  membership and norm displays to keep them narrow. Screenshots remain
  temporary artifacts outside the repository.
- The parent and all six leaf URLs returned HTTP 200. Opened the updated
  local Node 4 page for Steven. No commit, push, PR update, or hosted
  deployment was performed; prior local work is preserved.

## Report relevance

This records user-led script development and AI-assisted mathematical
exposition, storyboard construction, dependency design, and website checks.
The visuals make the phase interpretation concrete while preserving the
distinction between geometric intuition, accepted arithmetic inputs, and
the general deductions built from them.
