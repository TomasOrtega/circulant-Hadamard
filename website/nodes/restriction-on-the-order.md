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
graphLayout: proof-map
graphTitle: Inside Node 2 · Restriction on the Order
children:
  - node: order-is-square
    dependsOn: []
    segment: null
    script: |
      Substituting $X=1$ respects the relation $X^n=1$. Every positive
      and negative power becomes one, so $h^*(1)=h(1)$ and

      $$
      n=h(1)h^*(1)=h(1)^2.
      $$

      The row sum is an integer, hence $n$ is a square. The order-four
      row $(-1,1,1,1)$ has sum $2$; an order-$36$ candidate would need
      sum $6$ or $-6$.
  - node: order-is-even
    dependsOn: []
    segment: null
    script: |
      Choose two distinct rows, possible since $n>1$. If their dot
      product has $a$ positive terms and $b$ negative terms,
      orthogonality gives $a-b=0$, while $a+b=n$. Thus $n=2a$ is even.

      Since $n=m^2$ is also a square, its positive square root $m$ is
      even. Writing $m=2u$ gives

      $$
      n=4u^2,\qquad u\text{ a positive integer}.
      $$

      The remaining steps prove that this same $u$ is odd.
  - node: power-of-two-cycle
    dependsOn:
      - order-is-square
      - order-is-even
    segment: null
    script: |
      Write $u=2^{s-1}w$ with $s\geq1$ and $w$ odd. Then
      $n=2^{2s}w^2$. Reduce exponents modulo $2^{2s}$, defining

      $$
      T(X)=\sum_{r=0}^{2^{2s}-1}a_rX^r,
      \qquad a_r=\sum_{\ell=0}^{w^2-1}h_{r+\ell2^{2s}}.
      $$

      Each new coefficient sums $w^2$ signs, so it is odd. Projection
      preserves products and star, hence
      $T(X)T^*(X)=2^{2s}w^2$ on the shorter cycle. For order $36$, this
      collects nine signs into each of four positions; the resulting
      odd coefficients need not be signs.
  - node: cyclotomic-divisibility
    dependsOn: []
    segment: null
    script: |
      Suppose $T(X)T^*(X)=2^{2t}w^2$ on a cycle of length $2^k$,
      with integer coefficients and $w$ odd. Evaluate at a primitive
      $2^k$th root $\xi$. The specialized cyclotomic basis and
      valuation from Lemma 2.1 give $v(T(\xi))=t$: conjugation preserves
      $v$, and the product has valuation $2t$.

      Since $\xi^{2^{k-1}}=-1$, the basis coefficients of $T(\xi)$ are
      the opposite differences. The coefficient statement therefore gives

      $$
      2^t\mid a_j-a_{j+2^{k-1}}.
      $$

      For order $16$, divisibility by $4$ forces opposite signs to
      agree, so the eighth shift repeats the row. The leaf proves the
      general deduction and states the standard cyclotomic input precisely.
  - node: fold-and-divide
    dependsOn:
      - power-of-two-cycle
      - cyclotomic-divisibility
    segment: null
    script: |
      When $t\geq2$, opposite odd coefficients agree modulo $4$.
      Writing a pair as $a_j,a_j+4r_j$, its average is the odd integer
      $a_j+2r_j$. Project to the half-length cycle and divide by two.
      The new polynomial satisfies

      $$
      T_1(X)T_1^*(X)=2^{2(t-1)}w^2.
      $$

      Starting at $(k,t)=(2s,s)$, induction gives
      $(k,t)=(2s-j,s-j)$ after $j$ folds. Every step with $j<s-1$
      starts with $t\geq2$, so it preserves odd coefficients. After
      $s-1$ folds, the length is $2^{s+1}$ and the norm is $4w^2$.
  - node: odd-squares-mod-eight
    dependsOn:
      - fold-and-divide
    segment: null
    script: |
      If $s\geq2$, the endpoint has $2^{s+1}$ odd coefficients $b_j$.
      Taking the identity coefficient of its norm gives

      $$
      \sum_jb_j^2=4w^2.
      $$

      Every odd square is $1$ modulo $8$: for $b=2r+1$,
      $b^2=4r(r+1)+1$, and $r(r+1)$ is even. The left side is thus
      $0$ modulo $8$, since its number of terms is a multiple of eight.
      The right side is $4$ modulo $8$ because $w$ is odd.

      This contradiction forces $s=1$, so $u=2^{s-1}w=w$ is odd and
      $n=4u^2$.

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
