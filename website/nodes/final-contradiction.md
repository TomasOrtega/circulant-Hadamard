---
id: final-contradiction
title: The Final Contradiction
shortTitle: The Final Contradiction
summary: The general vanishing sum has residue one from the all-ones polynomial,
  excluding every odd u greater than one and leaving exactly orders 1 and 4.
number: 8
draft: true
video:
  src: media/final-contradiction.mp4
  captions: media/final-contradiction.vtt
  duration: 162.333333
mapPosition:
  - 250
  - 820
mapSummary: 'General $u$; only orders $1$ and $4$'
graphLayout: proof-map
graphTitle: Inside Node 8 · The Final Contradiction
children:
  - node: roots-cancel-ones
    dependsOn: []
    segment: { start: 17.47, end: 49.59 }
    script: |
      Recall the all-ones polynomial from Node 5:

      $$
      J(P)=1+P+\cdots+P^{u^2-1}.
      $$

      For $u=3$, substituting the primitive cube root $\omega$ groups
      its nine terms into three copies of $1+\omega+\omega^2=0$.
      Therefore $J(\omega)=0$ exactly.

      In general, let $I$ be the distinct primes dividing $u$ and
      $\zeta_S=\prod_{p\in S}\zeta_p$. For a nonempty subset $S$,
      this root has order $\prod_{p\in S}p>1$, which divides $u^2$.
      The geometric sum gives

      $$
      (\zeta_S-1)J(\zeta_S)=\zeta_S^{u^2}-1=0.
      $$

      Since $\zeta_S\ne1$, cancellation in the original
      characteristic-zero domain yields

      $$
      J(\zeta_S)=0\qquad(S\ne\varnothing).
      $$

      This exact evaluation happens before reduction modulo $1+i$.
  - node: odd-ones-at-one
    dependsOn: []
    segment: { start: 76.37, end: 97.43 }
    script: |
      At $P=1$, every term contributes one:

      $$
      J(1)=u^2.
      $$

      There are nine ones in the guiding example. After reduction modulo
      $1+i$, each pair adds to zero because $2=(1+i)(1-i)$. Nine ones
      leave one; so does every odd number $u^2$ of ones.

      We must also account for the denominator. The polynomial $c(P)$
      has real integer coefficients, so its norm identity at $P=1$ gives

      $$
      c(1)^2=u^2,\qquad c(1)=\pm u.
      $$

      Hence $J(1)/c(1)=\pm u$, which also has residue $1$ for odd $u$.
      When $u=3$, the surviving value is $9/(\pm3)=\pm3$.
  - node: surviving-odd-term
    dependsOn:
      - roots-cancel-ones
      - odd-ones-at-one
    segment: { start: 49.59, end: 97.43 }
    script: |
      Node 5 gives $E(P)\equiv J(P)\pmod{1+i}$ coefficient by
      coefficient. Evaluate and divide by the units $c(\zeta_S)$
      established in Node 6. In the ring
      $\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]$, this gives

      $$
      \begin{aligned}
      \mathcal S
      &\equiv\sum_{S\subseteq I}(-1)^{|S|}
      \frac{J(\zeta_S)}{c(\zeta_S)}\\
      &=\frac{u^2}{c(1)}=\pm u\equiv1\pmod{1+i}.
      \end{aligned}
      $$

      All nonempty-subset terms vanish. The empty subset has sign $+1$
      and gives the single surviving contribution. For $u=3$, this is

      $$
      \frac9{c(1)}-\frac0{c(\omega)}=\pm3\equiv1\pmod{1+i}.
      $$

      The denominators are units in this coefficient ring and remain
      units after reduction; nonzero complex values alone would not
      justify dividing congruences.
  - node: incompatible-residues
    dependsOn:
      - surviving-odd-term
    segment: { start: 97.43, end: 115.83 }
    script: |
      Node 7 and the all-ones calculation give two incompatible residues
      for the same element:

      $$
      \mathcal S\equiv0\pmod{1+i},\qquad
      \mathcal S\equiv1\pmod{1+i}.
      $$

      The reduction ring is nonzero and has characteristic two, as
      established in Node 6. Its zero and one are distinct, so this
      would force the contradiction $0=1$.

      The argument assumed an odd $u>1$. It rules out every such $u$,
      including the guiding case $u=3$, and therefore order $36$.
  - node: theorem
    dependsOn:
      - incompatible-residues
    segment: { start: 115.83, end: 162.333333 }
    script: |
      > **Theorem.** A real circulant Hadamard matrix exists exactly at
      > orders $1$ and $4$.

      For an order $n>1$, Node 2 gives $n=4u^2$ with $u$ a positive
      odd integer. The contradiction excludes $u>1$, leaving $u=1$
      and $n=4$. Order $1$ is the separate trivial case.

      Both orders occur: $(1)$ gives order $1$, and the original
      circulant matrix with first row $(-1,1,1,1)$ gives order $4$.
      Its distinct rows agree twice and disagree twice, so their dot
      products are zero. The deeper statement below displays it again.

      This finishes the eight-node argument. The theorem is the
      conclusion of this node.
---

Node 7 completes the contradiction for $u=3$ and supplies its general
replacement: for every odd $u>1$, the alternating sum $\mathcal S$ has
residue zero. We now finish the argument for all such $u$.

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

Let $I$ be the set of distinct primes dividing $u$, and write
$\zeta_S=\prod_{p\in S}\zeta_p$, with $\zeta_\varnothing=1$.
The all-ones polynomial

$$
J(P)=1+P+\cdots+P^{u^2-1}
$$

vanishes at every nontrivial evaluation root $\zeta_S$. At $1$, it has
value $u^2$. Since $E(P)\equiv J(P)\pmod{1+i}$ and all denominators are units,
only the empty-subset term survives:

$$
\begin{aligned}
\mathcal S
&\equiv\sum_{S\subseteq I}(-1)^{|S|}
\frac{J(\zeta_S)}{c(\zeta_S)}\\
&=\frac{u^2}{c(1)}=\pm u\equiv1\pmod{1+i}.
\end{aligned}
$$

Here $c(1)=\pm u$, and $u$ is odd. This contradicts
$\mathcal S\equiv0$ from Node 7, so no odd $u>1$ is possible.

Finally, Node 2 gives $n=4u^2$ for every order $n>1$. The contradiction
leaves $u=1$, hence $n=4$, alongside the separate order-$1$ case.
Both occur: $(1)$ is an order-$1$ example, and the circulant matrix with
first row $(-1,1,1,1)$ is an order-$4$ example. Thus the only possible
orders are exactly $1$ and $4$.
