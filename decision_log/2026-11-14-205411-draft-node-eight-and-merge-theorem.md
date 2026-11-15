# Draft Node 8 and make the theorem its conclusion

- Recorded at: 2026-11-14T20:54:11-08:00
- Observed work interval: 2026-11-14T20:48:30-08:00/2026-11-14T20:54:11-08:00 (341 seconds through this record).
- Participants: Steven Creech (supplied four-scene outline and proposed
  combining the theorem with the contradiction); OpenAI Codex, GPT-6
  (integration, delegated mathematical review, script/storyboard/leaf
  drafting, route preservation, and validation).
- Delegated observed intervals: mathematical review,
  2026-11-14T20:49:01-08:00/2026-11-14T20:49:21-08:00 (20 seconds);
  leaf authoring and checks,
  2026-11-14T20:49:21-08:00/2026-11-14T20:51:07-08:00 (106 seconds);
  script/storyboard,
  2026-11-14T20:48:49-08:00/2026-11-14T20:51:50-08:00 (181 seconds);
  route preservation,
  2026-11-14T20:49:22-08:00/2026-11-14T20:50:08-08:00 (46 seconds).
  These overlap the primary interval and are not additive person-hours.

## Context and decision

Steven supplied the final video's outline in chat: recall the vanishing
sum, evaluate the nine-term all-ones polynomial at a cube root and at one,
obtain incompatible residues, and finish with orders 1 and 4. Save the
edited [four-scene script](../website/scripts/node8/final-contradiction.md)
and a [reference transcription](../website/scripts/node8/reference/supplied-outline.md).
The transcription preserves the supplied narration and cues with pasted
mathematical delimiters normalized to LaTeX; it is labelled accordingly.
Continue the example-led production workflow from
[Node 7](2026-11-14-204711-draft-node-seven-rotation-cancellation.md).

Accept Steven's suggestion to combine the theorem with Node 8. This
revises the [original map](2026-11-14-151609-eight-node-proof-map.md), which
had an additional theorem box after the eight main nodes. The main map
now ends at Node 8; the theorem remains a detailed statement as its final
child, 8.5. It is the conclusion of the same video, avoiding another
main-level step for the conclusion just reached. The front-page theorem
statement remains in place.

Expand [Node 8](../website/nodes/final-contradiction.md) into five steps:
nontrivial roots cancel the ones; an odd number of ones at one; one
surviving term; incompatible residues; and the theorem. Edges are
8.1→8.3, 8.2→8.3, 8.3→8.4, and 8.4→8.5. A four-step alternative
combining both evaluations was considered. Keep them separate because
the user's second and third scenes teach different pictures that meet
in the same calculation. Put general exposition in each child section
and the final result in the parent body shown on the main page.

Preserve the old /nodes/theorem/ URL with a static HTML redirect and
ordinary fallback link to /nodes/final-contradiction/theorem/. The
[builder](../website/build-nodes.jsx) derives the relative destination
from the existing route helpers, uses no client JavaScript, and does not
replace an occupied old route or invent a destination when no theorem
exists. Update the authoring and script indexes.

## Rationale

Make the denominator step explicit. The coefficient congruence E≡J may
be evaluated and divided because each c(ζS) is a unit in the evaluation
ring A=Z[i,{ζp},1/u], established in Node 6. Nonzero complex values alone
would not justify division after reduction. The real integer coefficients
of c imply c(1)²=u², hence c(1)=±u. The empty-subset term is therefore
u²/c(1)=±u≡1 modulo 1+i. For u=3 this is 9/(±3)=±3≡1.

For a nonempty subset S, ζS has exact order equal to the product of its
distinct primes, greater than one and dividing u². The geometric-sum
identity gives J(ζS)=0 exactly by cancellation in the original domain,
before reduction. Every nonempty-subset contribution vanishes, while
the empty subset has sign +1. The same sum consequently has residues
zero and one in the nonzero quotient ring from Node 6. This excludes
odd u>1. Node 2 leaves n=4 for n>1, and n=1 is the separate trivial case.
Keep u>1 visible so the argument does not appear to exclude the known
order-four example.

The [storyboard](../website/scripts/node8/storyboards/odd-ones.svg) separates
exact complex-vector cancellation from algebraic reduction. Three groups
of cube-root arrows close into triangles. Nine parallel arrows sum to
nine, then a separate residue calculation pairs eight ones and leaves
one. The final panel accounts for c(1) and compares the incompatible
residues. Mathematical labels use the shared MathJax renderer, with an
editable SVG generator and the existing blue/white production palette.

**Consistency correction:** the theorem leaf now uses the same first
row (−1,1,1,1) as the main page and Node 1, replacing the old cyclically
shifted representative. It no longer describes Proposition 3.4 as an
unexpanded accepted input: Node 4 now develops the Δ-theorem with its
stated technical inputs. No new mathematical assumption is introduced.

## Evidence and outcome

- Independent written review checked the root orders, geometric sums,
  unit denominators, real c(1), residue calculation, and remaining orders
  against the local primary paper's final Section 4 and earlier website
  nodes. This exposition depends on the previous proof chain; it is not
  a new Lean verification of the theorem.
- The new main-map test failed before integration because the main map
  still had nine boxes. The old-theorem-route test also failed before
  its redirect existed. Final checks pass: 65 tests, 6,928 assertions,
  and 48 compiled node pages plus the compatibility redirect.
- Tests cover the new graph and nested theorem, preserved links, script
  and storyboard MathJax, and the unchanged order-four matrix. Bounded
  numerical root-sum checks use u=3,5,9,15,21 and all their nonempty
  distinct-prime subsets; they validate illustrations of the written
  geometric-sum proof. Both signs of c(1) give the expected odd residue.
  The storyboard's 51 compiled math fragments, SVG/XML structure, and
  accessible title/description were checked.
- Required all-files lint noticed the two previously archived unstaged
  paths and trimmed one trailing ASCII space in the concurrently edited
  Node 1 script. Restored that exact space from the agent's captured
  pre-lint output, preserving all user edits. Explicit lint then passed
  for all 219 other existing files, including every Node 8 change;
  whitespace checks pass with that concurrent file excluded. Its
  pre-existing trailing-space notice remains outside this task.
- Browser inspection confirms eight boxes on the main map, five steps
  inside Node 8, readable LaTeX, the storyboard, and fitting equations
  at 500px width. Graphs retain their existing horizontal scrolling on
  narrow screens. Temporary screenshots remain outside the repository.
- The main page, Node 8, its five children, and the old theorem URL
  returned HTTP 200; the old page contains the correct refresh and
  fallback destination. Opened the updated local Node 8 page.
- Videos and cut timings remain unset. No recording, video render,
  commit, push, PR update, or hosted deployment was performed.

## Report relevance

This records user-led development of the final narration and the decision
to end the eight-node journey with its theorem. It documents AI assistance,
mathematical clarification of the surviving residue, route preservation,
and checks that distinguish the general proof from bounded illustrations.
