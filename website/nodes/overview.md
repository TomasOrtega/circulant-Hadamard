---
id: overview
title: The circulant Hadamard conjecture
shortTitle: Proof map
summary: A high-level overview of the proof. Explore the graph to follow each
  step in greater detail.
draft: true
video:
  src: media/overview.mp4
  captions: media/overview.vtt
  duration: 214.933333
graphLayout: proof-map
graphTitle: The proof at a glance
children:
  - node: group-ring-encoding
    dependsOn: []
    segment: { start: 94.95, end: 105.91 }
  - node: restriction-on-the-order
    dependsOn:
      - group-ring-encoding
    segment: { start: 105.91, end: 116.45 }
    script: |
      > **Lemma (Order restriction, Proposition 2.2).** *If a real circulant Hadamard
      > matrix has order $n>1$, then $n=4u^2$ for an odd positive integer $u$.*

      The first two restrictions follow directly from what we already know.
      Evaluating the group-ring identity $h(X)h^*(X)=n$ at $X=1$ gives

      $$
      n=h(1)^2,
      $$

      since $h^*(1)=h(1)$. The row sum $h(1)$ is an integer, so **$n$ is a square**.

      Orthogonality tells us that **$n$ is even**. The dot product of two distinct
      rows is a sum of $n$ terms, each $+1$ or $-1$, that equals zero. There must
      be equally many positive and negative terms, hence an even number of terms.
      Thus, $n$ is an even square, so $4$ divides it. Writing its even square root
      as $2u$, we obtain $n=4u^2$.

      Lastly, **$u$ is odd**. We use this part of the order restriction as the accepted input
      from Proposition 2.2.

      Since $u=1$ gives the known order-four case, it remains to rule out $u>1$.
      We therefore proceed by contradiction: assume that a circulant Hadamard
      matrix exists with $n=4u^2$ for an odd integer $u>1$, and seek a contradiction.
  - node: three-evaluations
    dependsOn:
      - restriction-on-the-order
    segment: { start: 116.45, end: 131.85 }
  - node: delta-theorem
    dependsOn: []
    segment: { start: 131.85, end: 145.45 }
    contextFrom:
      - group-ring-encoding
  - node: signs-become-all-ones
    dependsOn:
      - three-evaluations
    segment: { start: 145.45, end: 156.81 }
    script: |
      > **Lemma (Signs become all ones).** *Let $c(P),d(P),g(P)$ be the normalized
      > evaluations from the same four sign polynomials in Node 3. Then*
      >
      > $$
      > E(P):=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}
      > $$
      >
      > *has Gaussian-integer coefficients and satisfies*
      >
      > $$
      > E(P)\equiv1+P+\cdots+P^{u^2-1}\pmod{1+i}.
      > $$

      For $u=3$, the right side is the nine-term polynomial $1+P+\cdots+P^8$.
      The idea is to rewrite $E(P)$ as a sign polynomial plus a multiple of $1+i$.
      That multiple disappears on reduction, and both signs become $1$.
      We use $J(P)$ as shorthand for the all-ones polynomial in the later steps.
  - node: odd-order-rigidity
    dependsOn:
      - three-evaluations
      - delta-theorem
      - signs-become-all-ones
    segment: { start: 156.81, end: 170.03 }
    script: |
      > **Lemma (Odd-order rigidity).** *Let $u>1$ be odd, and let
      > $c(P),d(P),g(P)$ be the normalized norm solutions from the common sign
      > array in Node 3. Define*
      >
      > $$
      > R=\frac{\Delta(d)}{\Delta(c)},
      > \qquad W=\frac{\Delta(g)}{\Delta(c)}.
      > $$
      >
      > *Then*
      >
      > $$
      > R=W=1.
      > $$

      The Δ-theorem gives odd order. The sign divisibilities, together with
      invertibility of the evaluated denominators, give residue $1$ modulo
      $1+i$. Odd-order rigidity turns these two facts into exact equality.

      For $u=3$, the three points $c(1),d(1),g(1)$ all undergo the same rotation
      when we move to $c(\omega),d(\omega),g(\omega)$. The points keep their
      relative positions. For general $u$, the conclusion concerns alternating
      products.
  - node: products-to-sums
    dependsOn:
      - signs-become-all-ones
      - odd-order-rigidity
    segment: { start: 170.03, end: 181.41 }
    script: |
      > **Lemma (From products to sums).** *Let $u>1$ be odd, and let
      > $c(P),d(P),g(P)$ be the normalized polynomials from the common sign array.
      > Define*
      >
      > $$
      > E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
      > $$
      >
      > *Write $I=\{p:p\mid u\}$ for the distinct prime divisors and
      > $\zeta_S=\prod_{p\in S}\zeta_p$, with empty product $1$.
      > The exact identities $R=W=1$ imply*
      >
      > $$
      > \mathcal S:=\sum_{S\subseteq I}(-1)^{|S|}
      > \frac{E(\zeta_S)}{c(\zeta_S)}\equiv0\pmod{1+i}.
      > $$
      >
      > *The congruence is in $\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]$;
      > every denominator $c(\zeta_S)$ is a unit there.*

      For $u=3$, $E$ follows the common rotation of $c,d,g$ from $1$ to
      $\omega$. Dividing by $c$ cancels that rotation, giving an exact
      vanishing difference. The general argument expands the equal products, cancels before reducing, and adds the two sums.
  - node: final-contradiction
    dependsOn:
      - signs-become-all-ones
      - products-to-sums
    segment: { start: 181.41, end: 214.933333 }
    script: |
      > **Final contradiction and theorem.** *For an odd $u>1$, the polynomials
      > from a hypothetical circulant Hadamard matrix of order $4u^2$ would
      > satisfy both*
      >
      > $$
      > \mathcal S\equiv0\pmod{1+i},\qquad
      > \mathcal S\equiv1\pmod{1+i}.
      > $$
      >
      > *These are incompatible in the nonzero reduction ring. Combined with
      > the order restriction and the examples, this proves that a real
      > circulant Hadamard matrix exists if and only if its order is $1$ or $4$.*

      The all-ones polynomial vanishes at every nontrivial evaluation root.
      At $1$, it contributes $u^2/c(1)=\pm u$, an odd integer with residue $1$.
      For $u=3$, three groups of cube roots cancel while nine ones leave one
      modulo $1+i$. The same calculation for general $u$ finishes the contradiction;
      the theorem and its two examples complete this node.
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

The main overviews use the case $n=36$ as a guiding example to explain the
idea of each lemma. As we open a node and explore its smaller steps, we
develop the general statements and proofs. The example shows the shape of
the argument; those general steps establish the result for every order.

The dependency graph above organizes the proof into eight main steps and
shows how they fit together. **Click any node** to explore its statement and
the idea behind it, then go deeper into the mathematical details. This lets
you follow the overall argument first and explore individual steps in more
detail as you go.
