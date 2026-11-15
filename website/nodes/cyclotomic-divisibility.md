---
id: cyclotomic-divisibility
title: Compare Opposite Coefficients
shortTitle: Opposite Coefficients
summary: A cyclotomic divisibility lemma controls differences between positions halfway around a power-of-two cycle.
number: "2.4"
draft: true
video: null
blackBox: Lemma 2.1
mapPosition: [440, 210]
mapSummary: '$2^t$ divides opposite differences'
---

## The algebraic input

Let $k\geq1$ and $t\geq0$ be integers, and let $w$ be an odd integer.
Suppose $T(X)=\sum_{j=0}^{2^k-1}a_jX^j$ has integer coefficients and satisfies

$$
T(X)T^*(X)=2^{2t}w^2
\quad\text{in }\mathbb Z[X]/(X^{2^k}-1).
$$

The cyclotomic divisibility input gives

$$
2^t\mid a_j-a_{j+2^{k-1}}
\qquad(0\leq j<2^{k-1}).
$$

This is a general statement about integer polynomials on a power-of-two cycle.
It supplies an independent input to the folding step.

## Why order 16 is a useful example

At order $16$, the original coefficients are signs and $t=2$. The lemma says
$4\mid h_j-h_{j+8}$. A difference of signs is $-2$, $0$, or $2$, so opposite
coefficients must agree. The eighth shift then repeats the original row,
giving dot product $16$ instead of zero.

That contradiction uses the divisibility lemma. It illustrates the order-$16$
case; the general exclusion of $16\mid n$ uses the remaining graph.

**Status.** The cyclotomic proof is deferred. This consequence uses Lemma 2.1
and the primitive-root coefficient basis from
[the paper, Section 2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
