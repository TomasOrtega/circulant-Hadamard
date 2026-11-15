# Produce the nontrivial-root cancellation video

- Recorded at: 2026-11-15T07:21:02-08:00
- Observed work interval: 2026-11-15T07:06:52-08:00/2026-11-15T07:21:02-08:00
  (850 seconds, including synthesis/render waits; overlaps other videos).
- Participants: Tomas Ortega (standing final-video request); Steven Creech
  (editorial script); OpenAI Codex, GPT-6 (narration adaptation, scene,
  arithmetic, timing, and exported-frame review); Google Chirp 3 HD Achird
  (one complete take); local faster-whisper Base English (alignment).

## Context and decision

Produce final Video 8.1 from the unchanged
[four-slide script](../website/scripts/node8/roots-cancel-ones.md), following
[the refined Node 7–8 exposition decision](2026-11-15-025408-complete-node-seven-eight-child-exposition-and-scripts.md)
and [Video 7.3](2026-11-15-070636-produce-cancel-before-reduction-video.md).
Read the full script, detailed node, and following two scripts to preserve
scope. Add the [scene](../videos/roots_cancel_ones.py), frozen
[SSML](../videos/scripts/roots-cancel-ones.ssml), and measured
[production metadata](../videos/production/roots-cancel-ones.json).
Root owns synthesis, GPU construction/rendering, final
[MP4](../website/media/roots-cancel-ones.mp4),
[captions](../website/media/roots-cancel-ones.vtt), website integration,
shared checks, and separate commit/push. Preserve the editorial source,
mathematical draft metadata, parents, and shared helpers.

## Rationale

Keep the empty subset and its input one visibly separate. For nonempty S,
prove that the product of primitive prime roots has squarefree order
m = product of the distinct primes in S. Its m-th power is one. Raising
it to m/p kills the other factors and leaves a nontrivial primitive p-root
power, so its order contains every prime in S. Together these prove order m.
For u = 15, retain all three premises eta^15 = 1, eta^5 != 1, and
eta^3 != 1 before concluding order fifteen. Return to the general conditions
1 < m dividing u squared, zeta_S != 1, and zeta_S^(u squared) = 1.

Animate the formal polynomial identity by aligning PJ and minus J,
striking the matching powers, and collecting the two endpoints. Do not
cancel P minus one in the cyclic group ring. Evaluate first in the stated
characteristic-zero domain A contained in C, then cancel the nonzero
factor zeta_S minus one. This needs the domain property, not a unit claim.
State exact zero before reduction modulo 1+i.

For u = 3, transform all nine fixed-position powers into three repeated
triples, then move nine complex unit vectors head to tail into three
closed equilateral triangles. The illustration concerns complex sums,
not residue geometry. Keep the general conclusion qualified by nonempty S;
return the excluded input P = 1 to the waiting card for Node 8.2 without
evaluating it here.

The 2,800-byte SSML fits one default Achird request. Seven paragraph cues
and thirty internal cues use measured unique exact-source phrases,
anticipating each phrase by 0.2 seconds. Register copy targets before play
and remove faded terms from their owner groups. Inherited framing reserves
the bottom 20% without a footer.

## Evidence and outcome

- Strict CPU TeX construction passed for all 37 static and 23 dynamic
  strings (input cards, nine powers, and telescoping rows). Adjacent
  nine-power brackets have 0.7058 units of clearance; the lowest order
  conclusion is at y = -3.3365, above the subtitle boundary y = -4.
  Scoped Ruff, formatting, and whitespace checks pass.
- Exact rational phase computations checked all primitive-root choices
  for every nonempty prime subset for odd u from 3 through 105: 2,388
  cases. Each product has denominator m > 1 dividing u squared, and
  its m/p power has denominator p. Formal coefficient telescoping also
  passed for each N from 1 through 225. In the exact Eisenstein basis,
  the three displayed roots have norm one and sum zero. These bounded
  computations check illustrations; the source supplies the general proof.
- Root's first actual timing construction reached triangle_head_tail at
  168.98 seconds for its measured 168.60 cue (0.38 seconds late).
  Preserve this failure in ignored build/roots-cancel-ones-timing-red.json.
  Shorten only the preceding vector setup from 1.0 to 0.6 seconds.
  The actual root rerun reaches that cue at 168.58 seconds and completes
  at 189.32 seconds with no late events and all strict TeX constructions
  successful. Independently read the final JSON; an ignored green copy
  records it. The SSML, recording, and measured cues remain unchanged.
- Independently inspected 17 native actual-export frames at 31, 60, 63,
  80, 80.7, 91, 103.6, 104.75, 111, 121, 140, 150, 166, 170, 174,
  181, and 188 seconds. They cover all seven sections, the complete
  order-fifteen condition, aligned telescoping rows and cancellations,
  domain/nonzero cancellation, all nine powers, three closed triangles,
  and the excluded empty subset. Tight native crops confirm the full
  order proof, title, and triangles when broad previews drop glyphs.
  Mathematics and geometry are legible and separated. Root independently
  accepted all seven phases. No post-render change or new take was needed.
- Independently probed the final H.264 export: 1920 by 1080 at 30 fps,
  5,680 frames, 189.333333 seconds, 6,171,722 bytes. AAC lasts 189.320998
  seconds and covers the complete 189.320227-second take. Editorial,
  SSML, and MP4 SHA-256 values match the manifest. Final scene and shared
  layout hashes are recorded there. MP4 SHA-256:
  d474dae36cea09284461106d292b2afe680100c0f730f9b346d4837db644ea51.
- The 45 captions exactly reproduce the frozen SSML text, use at most two
  42-character lines, last at least 1.30 seconds, do not overlap, and end
  at 188.18 seconds. ASR supports wording and timing checks; no independent
  human listening acceptance is asserted.
- Root reports its terminal all-frame scan checks all 5,680 frames:
  maximum luma 16 in the bottom 20% (black). This is separate from the
  author's sampled visual review. Root also reports complete checks pass:
  20 narration tests and 41 video tests; website 183 tests with 9,346
  assertions and 50 built pages. The ignored final-audit JSON separates
  these root-reported checks from independently verified export facts.

## Report relevance

Records animation of a complete nontrivial-root cancellation argument,
with squarefree order proved, formal and evaluated identities separated,
exact domain cancellation preserved, and the empty input deferred.
Documents bounded example checks, measured single-take timing, an observed
late-cue failure and successful visual-only correction, direct export
review, exact captions, and full-frame subtitle-space evidence.

## Root integration acceptance

At 2026-11-15T07:21:30-08:00 root accepted the final native states and the
complete 48-video hash/caption/codec/audio/band audit. See
[the integration record](2026-11-15-072130-accept-all-scripted-node-videos.md)
for the full checks and continuing user-requested monitoring. The individual
Roots commit and push follow.
