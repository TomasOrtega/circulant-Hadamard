---
id: restriction-on-the-order
title: Restriction on the Order
shortTitle: Restriction on the Order
summary: "Accept the order restriction, then begin with the smallest remaining
  case: u = 3."
number: 2
draft: true
video:
  src: media/restriction-on-the-order.mp4
  captions: media/restriction-on-the-order.vtt
  duration: 165.566667
mapPosition:
  - 40
  - 180
mapSummary: '$n=4u^2$, $u$ odd'
blackBox: Proposition 2.2
---

## Guiding example: $u=3$, $n=36$

The accepted order restriction leaves $n=4u^2$ with $u$ odd. The case $u=1$ gives the known order $4$; the smallest remaining candidate is $u=3$, or $n=36$. Our first complete route rules out this candidate. That example alone does not rule out every larger odd $u$.

## General statement

**Input:** $hh^*=n$, $h_j=\pm1$, $n>1$.

**Statement (accept Proposition 2.2):**
$$
n=4u^2,\qquad u\text{ odd}.
$$

**Intuition:** Trivial evaluation makes $n$ a square; orthogonality makes it even. Cyclotomic descent rules out further powers of $2$, ending with an odd-square congruence contradiction modulo $8$.

**Output:** For a counterexample other than order $4$, $u>1$ and $C_{4u^2}\cong C_4\times C_{u^2}$.

**Status:** BLACK BOX; later expand internal descent proof.

## Source and status

Exposition draft based on [OpenAI, *The circulant Hadamard conjecture*, Sections 2–4 (September 23, 2026)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf). This proposition is an **accepted black box** here; its internal proof graph will be added later.
