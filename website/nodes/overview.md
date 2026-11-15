---
id: overview
title: The circulant Hadamard conjecture
shortTitle: Proof map
summary: A high-level overview of the proof. Explore the graph to follow each
  step in greater detail.
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

## Definitions and main theorem

A **Hadamard matrix of order $n$** is an $n\times n$ matrix $H$ all of whose
entries are $\pm1$ and whose distinct rows are orthogonal. Since every row
has squared length $n$, this condition is equivalent to

$$
HH^{\mathsf T}=nI_n,
$$

where $I_n$ denotes the $n\times n$ identity matrix.

A matrix is **circulant** if each row is obtained from the preceding row by
shifting its entries one position cyclically to the right. Thus it is
completely determined by its first row. A **circulant Hadamard matrix** is a
Hadamard matrix with this cyclic structure.

**Example.** The following is a circulant Hadamard matrix of order $4$:

$$
H=\begin{pmatrix}
-1 & 1 & 1 & 1 \\
1 & -1 & 1 & 1 \\
1 & 1 & -1 & 1 \\
1 & 1 & 1 & -1
\end{pmatrix}.
$$

Its rows are successive cyclic shifts of $(-1,1,1,1)$. Any two distinct rows
agree in two positions and disagree in two, so their inner product is zero.
Each row has squared length $4$, and hence $HH^{\mathsf T}=4I_4$. This gives
a circulant Hadamard matrix of order $4$; the matrix $(1)$ supplies the
order-$1$ example. The following theorem states that there are no other orders.

> **Theorem 1 (Circulant Hadamard).** *Let $n$ be a positive integer. A real
> circulant Hadamard matrix of order $n$ exists if and only if $n\in\{1,4\}$.*

We give a high-level overview of the proof presented in
[The circulant Hadamard conjecture](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
At this level, the order restriction and the Δ-theorem are used as inputs to
the main argument.

The dependency graph above organizes the proof into eight main steps and
shows how they fit together. **Click any node** to explore its statement and
the idea behind it, then go deeper into the mathematical details. This lets
you follow the overall argument first and explore individual steps in more
detail as you go.
