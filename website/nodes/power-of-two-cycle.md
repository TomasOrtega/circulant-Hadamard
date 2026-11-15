---
id: power-of-two-cycle
title: Project to a Power-of-Two Cycle
shortTitle: Power-of-Two Cycle
summary: Group positions by their residue on a shorter cycle; each new coefficient is an odd sum of signs.
number: "2.3"
draft: true
video: null
mapPosition: [40, 210]
mapSummary: Odd coefficients; same norm
---

## Statement

The square and parity steps give $n=4u^2$, without yet knowing that $u$ is odd.
Write $u=2^{s-1}w$, where $s\geq1$ and $w$ is odd. Then

$$
n=2^{2s}w^2.
$$

Reduce exponents modulo $2^{2s}$, collecting the coefficients in each residue
class. This gives a polynomial $T(X)$ in $\mathbb Z[X]/(X^{2^{2s}}-1)$ with

$$
T(X)T^*(X)=2^{2s}w^2.
$$

Each new coefficient is the sum of $w^2$ signs, hence is an odd integer.
The projection respects multiplication and star, so it preserves the scalar
on the right of the identity.

## A picture at order 36

For a hypothetical order-$36$ matrix, $36=4\cdot9$. Collect positions with the
same residue modulo $4$: each of the four new coefficients sums nine signs.
This illustrates the projection; it does not construct a Hadamard matrix of
order $36$.

**Output.** A power-of-two cycle with odd coefficients and the same scalar
norm identity. The detailed projection argument can be expanded here later.
