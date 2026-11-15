---
id: fold-and-divide
title: Fold the Cycle
shortTitle: Fold the Cycle
summary: Average opposite coefficients to halve the cycle while preserving oddness and dividing the scalar norm by four.
number: "2.5"
draft: true
video: null
mapPosition: [240, 420]
mapSummary: 'Halve length; divide norm by $4$'
---

## The step to repeat

Suppose $T(X)$ has odd coefficients $a_j$ on a cycle of length $2^k$, and
$T(X)T^*(X)=2^{2t}w^2$, with $t\geq2$ and $w$ odd.
The divisibility input makes opposite coefficients congruent modulo $4$.
Therefore the averages

$$
b_j=\frac{a_j+a_{j+2^{k-1}}}{2}
$$

are odd integers. Fold opposite positions together and divide the resulting
polynomial by two. The new polynomial $S(X)$ satisfies

$$
S(X)S^*(X)=2^{2(t-1)}w^2
\quad\text{in }\mathbb Z[X]/(X^{2^{k-1}}-1).
$$

The cycle length halves, and the scalar norm is divided by four.

## The averaging idea

For an individual pair, $3$ and $7$ agree modulo $4$, and their average is
$5$, still odd. The divisibility lemma ensures this behavior simultaneously
for every opposite pair in the polynomial.

**Output.** If $s\geq2$, start at $(k,t)=(2s,s)$ and repeat this step $s-1$
times. There are then $2^{s+1}$ odd coefficients with scalar norm $4w^2$.
This iteration belongs inside the node; it does not create a loop in the graph.
The detailed induction will be developed here later.
