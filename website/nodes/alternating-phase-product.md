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
defined and nonzero. Write $f_S=f(\zeta_S)$ and define

$$
\Delta(f)=\prod_{S\subseteq I}f_S^{(-1)^{|S|}}.
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

## Every conjugate has magnitude one

All values belong to the cyclotomic ring

$$
B=\mathbb Z[i,\{\zeta_p:p\in I\}],
$$

so $\Delta(f)$ initially belongs to its fraction field. Every embedding
of this field into $\mathbb C$ sends the root generators to roots of unity
and commutes with complex conjugation. The norm equations therefore give
$|\sigma(f_S)|=u$ for every $S$ and every such embedding $\sigma$.

There are equally many even- and odd-sized subsets: toggling any fixed
prime pairs them. Hence

$$
|\sigma(\Delta(f))|
=u^{\sum_{S\subseteq I}(-1)^{|S|}}=1.
$$

**Output.** An algebraic number whose conjugates all lie on the unit circle.
Its integrality still needs proof; being a ratio of algebraic integers
does not supply that fact.

Source: [the paper, Section 3, equations (3.1)–(3.3) and Proposition 3.4](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
