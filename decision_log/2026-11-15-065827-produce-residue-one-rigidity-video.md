# Produce the residue-one rigidity video

- Recorded at: 2026-11-15T06:58:27-08:00.
- Observed production and review interval:
  2026-11-15T06:43:25-08:00/2026-11-15T06:58:27-08:00 (902 seconds,
  including synthesis and rendering waits).
- Participants: Tomas Ortega (continuing video request); Steven Creech
  (editorial script); OpenAI Codex, GPT-6 (narration, animation, root-agent
  synthesis/rendering, author and independent mathematical/export review).
  Concurrent review intervals overlap and are not additive person-hours.

## Context and decision

Produce a final video from the [Node 6.4 script](../website/scripts/node6/residue-one-rigidity.md),
following the [Node 5–6 exposition decision](2026-11-15-031546-develop-node-five-six-child-exposition.md).
Preserve the editorial source and mathematical-status metadata. The
[scene](../videos/residue_one_rigidity.py) uses one complete 2,479-byte
default Achird synthesis, six measured sections and 27 internal phrase cues.
All visual work uses that single recording.

## Rationale

Begin with the explicitly illustrative cube roots. If either nontrivial
cube root reduces to one, both do. Reducing the exact relation
$1+\omega+\omega^2=0$ would then give $1+1+1=0$, which contradicts a
nonzero characteristic-two target ring.

Give the general proof separately. For an element $\alpha$ of odd order
$r$ in a characteristic-zero domain $A$, treat $r=1$ directly. Otherwise,
assuming $\alpha\ne1$, factor $\alpha^r-1$ and cancel the nonzero factor
$\alpha-1$ inside $A$ to obtain an exact vanishing geometric sum. Only
then apply the reduction map. If $[\alpha]=1$, the odd number of summands
reduces to one, contradicting nonzeroness. The target ring need not be a
domain; all cancellation occurs before reduction.

Apply this lemma to the existing comparison numbers
$R=\Delta(d)/\Delta(c)$ and $W=\Delta(g)/\Delta(c)$. Display their
membership in $A^\times$, the odd-order input from Node 6.1 and the
residue-one input from Node 6.3. Display the full nonzero characteristic-two
quotient from [Node 6.2](2026-11-15-064209-produce-evaluation-units-video.md).
Conclude $R=W=1$ only after combining those inputs. This is exact arithmetic
rigidity, with no claim that the original evaluation points coincide or
that residue one means complex nearness.

## Evidence and outcome

- CPU construction compiles all 40 formula objects and checks 53 shown
  objects against the frame bounds. Ruff, formatting and Python
  compilation pass. Copy targets are registered before animation and
  transient objects leave the cleanup registry after fading.
- Exact integer-polynomial arithmetic checks the telescoping factorization
  for all 25 odd orders from 3 through 51. Pair counts and numerical
  cube-root identities support the illustration. These finite calculations
  do not replace the displayed general domain/ring-map proof.
- Strict actual-scene timing preflight passes at 162.520227 seconds with
  no late events. Author review accepts 20 native frames across all six
  proof phases, including both cube-root cases, the order-one case,
  cancellation before reduction, the completed odd-pair expression,
  contradiction, and the two-input application. Intermediate animation
  frames were distinguished from completed states. No author blockers remain.
- Final MP4: **5,343,609 bytes**, **162.533333 seconds**, H.264 1920×1080
  at 30 fps; AAC lasts 162.520998 seconds. Root reports the final band scan
  exiting successfully after checking all **4,876 frames**, with maximum
  limited-range luma **16** throughout the blank lower 20%. These results
  match the final manifest. No draft footer is present.
- All 37 captions reproduce the spoken source exactly, with at most two
  lines of 42 characters, minimum duration 2.18 seconds, no overlaps and
  in-bounds times. ASR match ratio 0.9576 supports timing; it does not
  establish human listening review. Editorial, scene, layout, SSML and
  video hashes match and are saved in the manifest. The final media and
  caption audit passes.
- Root's independent export review and repository-wide checks are recorded
  with the individual commit/push after this author handoff.

## Report relevance

Records production and checking of the existing odd-order residue-rigidity
argument, including the separation of domain cancellation from reduction
into a potentially non-domain ring. This adds no new research proof or
formal verification of the conjecture.

## Independent export and repository acceptance

At 2026-11-15T07:00:38-08:00 root Codex accepted the final native MP4
frames after independently checking the scene against the editorial argument.
The final audit verifies source, scene, layout, SSML and video hashes, exact
captions, default Achird voice, audio coverage and 1080p30 H264/AAC. The full
checks passed: 20 narration tests and 39 video tests; website 183 tests with
9,265 assertions and 50 built node pages. All-frame bottom-20% scans pass
(maximum luma 16). Caption and ASR checks support timing; they are not a
human listening certification. The requested per-video commit/push follows.
