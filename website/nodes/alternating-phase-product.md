---
id: alternating-phase-product
title: The Alternating Phase Product
shortTitle: Alternating Product
summary: Pair the prime-indexed evaluations to cancel their magnitudes and compare their phases.
number: "4.2"
draft: true
video: null
mapPosition: [40, 200]
mapSummary: 'All conjugates have modulus $1$'
---

## Define the alternating product

Let $I$ be the nonempty set of distinct primes dividing the odd integer
$u>1$. For each $p\in I$, choose a primitive $p$th root $\zeta_p$.
For a subset $S\subseteq I$, put

$$
\zeta_S=\prod_{p\in S}\zeta_p,
\qquad \zeta_\varnothing=1.
$$

Each $\zeta_S$ is a $u^2$th root, so the evaluation from Node 4.1 is
defined and nonzero. Define

$$
\Delta(f)=\prod_{S\subseteq I}f(\zeta_S)^{(-1)^{|S|}}.
$$

Even-sized subsets contribute to the numerator; odd-sized subsets
contribute to the denominator. With one distinct prime this is

$$
\Delta(f)=\frac{f(1)}{f(\zeta_p)}.
$$

With two distinct primes $p,q$, it is

$$
\Delta(f)=\frac{f(1)f(\zeta_p\zeta_q)}
{f(\zeta_p)f(\zeta_q)}.
$$

Under the Chinese remainder decomposition of the cycle, these are precisely
the characters that turn each prime component on or off. Choose the
component generators so that their product is the original generator $P$.

> **Lemma (Magnitude of the alternating product).** *If
> $f(P)f^*(P)=u^2$, then $\Delta(f)$ and all its algebraic conjugates
> have absolute value $1$.*

## Pair even and odd subsets

Fix one prime in $I$. Adding or removing that prime pairs each even-sized
subset with an odd-sized subset. There are therefore equally many factors
upstairs and downstairs. Every factor has magnitude $u$, so these magnitudes
cancel and $|\Delta(f)|=1$.

## The same argument works for every conjugate

All values belong to the cyclotomic ring

$$
B=\mathbb Z[i,\{\zeta_p:p\in I\}],
$$

so $\Delta(f)$ is initially a quotient of elements of this ring. An algebraic
conjugate is obtained by replacing the generating roots of unity by other
roots in a way that respects their algebraic equations. Write $\sigma$ for
such a replacement. Since conjugating a root of unity means inverting it,
$\sigma$ commutes with complex conjugation. Applying it to
$f(\zeta_S)\overline{f(\zeta_S)}=u^2$ gives
$|\sigma(f(\zeta_S))|=u$.

The same pairing of subsets therefore gives

$$
|\sigma(\Delta(f))|
=u^{\sum_{S\subseteq I}(-1)^{|S|}}=1.
$$

All conjugates lie on the unit circle. We next need to prove that the
quotient is an algebraic integer; a ratio of algebraic integers need not be one.

Source: [the paper, Section 3, equations (3.1)–(3.3) and Proposition 3.4](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
