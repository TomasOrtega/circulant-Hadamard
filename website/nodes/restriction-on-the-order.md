---
id: restriction-on-the-order
title: Restriction on the Order
shortTitle: Restriction on the Order
summary: Square and parity restrictions lead to a power-of-two descent, leaving
  n = 4u² with u odd.
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
graphLayout: proof-map
graphTitle: Inside Node 2 · Restriction on the Order
children:
  - node: order-is-square
    dependsOn: []
    segment: null
    script: |
      Set $X=1$ in $h(X)h^*(X)=n$. Since $h^*(1)=h(1)$, we get

      $$
      n=h(1)^2=\left(\sum_{j=0}^{n-1}h_j\right)^2.
      $$

      The row sum is an integer, so $n$ is a square. Our order-four
      example has row sum $-1+1+1+1=2$. At order $36$, a hypothetical
      row would need sum $6$ or $-6$.
  - node: order-is-even
    dependsOn: []
    segment: null
    script: |
      Since $n>1$, there are two distinct rows, and their dot product
      must be zero. Each of its $n$ terms is $+1$ or $-1$.
      Pairing positive and negative terms shows that $n$ is even.

      For our order-four example, the first two rows give
      $-1-1+1+1=0$. Combined with the square restriction, this leaves

      $$
      n=4u^2,\qquad u\text{ a positive integer}.
      $$

      The candidate orders begin $4,16,36,64,100,\ldots$.
      We still have to show that $u$ is odd.
  - node: power-of-two-cycle
    dependsOn:
      - order-is-square
      - order-is-even
    segment: null
    script: |
      Keep $u$ from $n=4u^2$ and separate its power of two by writing
      $u=2^{s-1}w$, with $s\geq1$ and $w$ odd. Then

      $$
      n=2^{2s}w^2.
      $$

      Collect coefficients whose positions agree modulo $2^{2s}$.
      This projects onto a cycle of length $2^{2s}$. Each new coefficient
      is a sum of $w^2$ signs, so it is odd, and the product identity
      is preserved.

      At order $36=4\cdot9$, this means four groups of nine signs.
      Their sums are odd integers, not necessarily signs.
      This is a construction from a hypothetical Hadamard row.
  - node: cyclotomic-divisibility
    dependsOn: []
    segment: null
    script: |
      **The extra algebraic input.** On a cycle of length $2^k$, the identity
      $T(X)T^*(X)=2^{2t}w^2$ with $w$ odd forces opposite coefficients to agree
      modulo $2^t$. This is a consequence of cyclotomic divisibility
      (Lemma 2.1), whose detailed proof will be developed inside this node.

      For a hypothetical order-$16$ Hadamard row, it gives

      $$
      4\mid h_j-h_{j+8}.
      $$

      A difference of two signs is only $-2$, $0$, or $2$, so opposite
      entries must agree. The eight-step shift repeats the first row,
      contradicting orthogonality. This is an example for the deeper proof;
      it does not by itself rule out every multiple of $16$.
  - node: fold-and-divide
    dependsOn:
      - power-of-two-cycle
      - cyclotomic-divisibility
    segment: null
    script: |
      If $s\geq2$, opposite odd coefficients agree modulo $4$.
      Replace each opposite pair by its average. The average is still
      odd: for example, $3$ and $7$ agree modulo $4$, and their average is $5$.

      This halves the cycle and divides the scalar in $T(X)T^*(X)$ by $4$.
      Repeat this step $s-1$ times. We reach $2^{s+1}$ odd coefficients
      with product identity

      $$
      T(X)T^*(X)=4w^2.
      $$

      The repetition is an induction within this step. There is no
      circular dependency in the graph.
  - node: odd-squares-mod-eight
    dependsOn:
      - fold-and-divide
    segment: null
    script: |
      Every odd square is $1$ modulo $8$. If $s\geq2$, the
      $2^{s+1}$ odd coefficients therefore have squares summing to $0$
      modulo $8$. But the constant coefficient of their product must be
      $4w^2$, which is $4$ modulo $8$.

      For $s=2$, the mismatch is already visible: eight odd squares
      cannot sum to a number congruent to $4$ modulo $8$.

      Thus $s=1$, so $u=2^{s-1}w=w$ is odd and the order is $n=4u^2$.
      The known order $4$ survives; the next candidate is $36$. The following main
      nodes address that candidate and the larger remaining orders.
---

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

Lastly, **$u$ is odd**. The smaller nodes develop the proof of this part
of the order restriction.

Since $u=1$ gives the known order-four case, it remains to rule out $u>1$.
We therefore proceed by contradiction: assume that a circulant Hadamard
matrix exists with $n=4u^2$ for an odd integer $u>1$, and seek a contradiction.
