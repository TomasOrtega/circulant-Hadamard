---
id: final-contradiction
title: The Final Contradiction
shortTitle: The Final Contradiction
summary: The general vanishing sum has residue one from the all-ones polynomial,
  excluding every odd u greater than one and leaving exactly orders 1 and 4.
number: 8
draft: true
video: null
mapPosition:
  - 250
  - 820
mapSummary: 'General $u$; only orders $1$ and $4$'
graphLayout: proof-map
graphTitle: Inside Node 8 · The Final Contradiction
children:
  - node: roots-cancel-ones
    dependsOn: []
    segment: null
    script: |
      > **Lemma (Vanishing away from one).** For
      > $J(P)=1+P+\cdots+P^{u^2-1}$ and every nonempty subset $S$ of the
      > distinct prime divisors of $u$,
      >
      > $$
      > J(\zeta_S)=0,\qquad \zeta_S=\prod_{p\in S}\zeta_p.
      > $$

      The product root has order $\prod_{p\in S}p>1$, which divides
      $u^2$. Thus $(\zeta_S-1)J(\zeta_S)=\zeta_S^{u^2}-1=0$.
      Cancel the nonzero factor $\zeta_S-1$ in characteristic zero.
      For $u=3$, the nine terms make three copies of
      $1+\omega+\omega^2=0$. These evaluations vanish exactly before
      any modular reduction.
  - node: odd-ones-at-one
    dependsOn: []
    segment: null
    script: |
      > **Lemma (The value at one).** The remaining evaluation satisfies
      >
      > $$
      > J(1)=u^2,\qquad c(1)=\pm u,\qquad
      > \frac{J(1)}{c(1)}=\pm u\equiv1\pmod{1+i}.
      > $$

      Each of the $u^2$ terms of $J(P)$ becomes one. Because $c(P)$ has
      real integer coefficients, the norm identity gives $c(1)^2=u^2$.
      This accounts for the denominator as well as the numerator. The
      integer $u$ is odd, and minus equals plus in characteristic two,
      so either sign of $u$ has residue $1$. For $u=3$, the quotient is
      $9/(\pm3)=\pm3$.
  - node: surviving-odd-term
    dependsOn:
      - roots-cancel-ones
      - odd-ones-at-one
    segment: null
    script: |
      > **Lemma (One surviving term).** The coefficient congruence
      > $E(P)\equiv J(P)\pmod{1+i}$ gives
      >
      > $$
      > \mathcal S\equiv\sum_{S\subseteq I}(-1)^{|S|}
      > \frac{J(\zeta_S)}{c(\zeta_S)}
      > =\frac{u^2}{c(1)}\equiv1\pmod{1+i}.
      > $$

      Evaluation preserves coefficient congruences. Multiplication by the
      units $c(\zeta_S)^{-1}=\overline{c(\zeta_S)}/u^2$ then preserves
      them in the same evaluation ring used in Node 7. Every nonempty-subset
      numerator is zero. The empty subset has sign $+1$, evaluates at $1$,
      and contributes $\pm u$, whose residue is one.
  - node: incompatible-residues
    dependsOn:
      - surviving-odd-term
    segment: null
    script: |
      > **Proposition (The contradiction).** No circulant Hadamard matrix
      > has order $4u^2$ with $u>1$ odd: its polynomials would satisfy
      >
      > $$
      > \mathcal S\equiv0\pmod{1+i},\qquad
      > \mathcal S\equiv1\pmod{1+i}.
      > $$

      Node 7 gives the first residue, and the all-ones evaluation gives
      the second. Both are in the same quotient of
      $\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]$. Node 6 proves that this
      quotient is nonzero, so $0\ne1$. The contradiction excludes every
      odd $u>1$. The earlier Δ-theorem requires $u>1$, so this argument
      does not exclude $u=1$.
  - node: theorem
    dependsOn:
      - incompatible-residues
    segment: null
    script: |
      > **Theorem (Circulant Hadamard).** A real circulant Hadamard matrix
      > exists if and only if its order is $1$ or $4$.

      For $n>1$, the order restriction gives $n=4u^2$ with $u$ a positive
      odd integer. The contradiction leaves $u=1$, hence $n=4$.
      Order $1$ lies outside that restriction and has the example $(1)$.
      At order $4$, use the circulant matrix with first row $(-1,1,1,1)$.
      Any two distinct rows agree twice and disagree twice, so their inner
      product is zero; each row has squared length $4$. The detailed
      statement displays and verifies both examples.
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
