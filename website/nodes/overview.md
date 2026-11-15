---
id: overview
title: The circulant Hadamard conjecture
shortTitle: Proof map
summary: Start with order 36. Follow eight high-level nodes, then see how the
  same argument extends to every odd u > 1.
draft: true
graphLayout: proof-map
children:
  - node: group-ring-encoding
    dependsOn: []
    segment: null
  - node: restriction-on-the-order
    dependsOn:
      - group-ring-encoding
    segment: null
  - node: three-evaluations
    dependsOn:
      - restriction-on-the-order
    segment: null
  - node: delta-theorem
    dependsOn: []
    segment: null
    contextFrom:
      - group-ring-encoding
  - node: signs-become-all-ones
    dependsOn:
      - three-evaluations
    segment: null
  - node: odd-order-rigidity
    dependsOn:
      - three-evaluations
      - delta-theorem
      - signs-become-all-ones
    segment: null
  - node: products-to-sums
    dependsOn:
      - signs-become-all-ones
      - odd-order-rigidity
    segment: null
  - node: final-contradiction
    dependsOn:
      - signs-become-all-ones
      - products-to-sums
    segment: null
  - node: theorem
    dependsOn:
      - final-contradiction
    segment: null
  - node: proof-by-example
    dependsOn: []
    segment: null
  - node: general-proof
    dependsOn: []
    segment: null
---

## The theorem

A real circulant Hadamard matrix exists exactly at orders $n=1$ and $n=4$.

This exposition follows the supplied proof map and the cited paper, accepting **Proposition 2.2** (the order restriction) and **Proposition 3.4** (the Δ-theorem) as black boxes. Their internal proofs are not supplied here.

## Begin with the smallest remaining case

After the order restriction, $u=3$ gives the first nontrivial candidate, $n=36$. The proof by example uses only $P=1$ and $P=\omega$, where $\omega=e^{2\pi i/3}$. It rules out order $36$; the separate general route rules out all odd $u>1$.

The graph connects the eight high-level statements. The Δ-theorem is independent of the original signs; its conclusion combines with the sign identities at **Odd-Order Rigidity**.

These are high-level statement cards. Video scripts and smaller internal graphs are the next stage.

Primary source: [OpenAI, *The circulant Hadamard conjecture*, Sections 2–4 (September 23, 2026)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
