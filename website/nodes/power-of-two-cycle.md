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

> **Lemma (Projection to the power-of-two cycle).** *Write
> $u=2^{s-1}w$, where $s\geq1$ and $w$ is odd, so $n=2^{2s}w^2$.
> Projecting a hypothetical sign polynomial $h(X)$ to the cycle of
> length $2^{2s}$ gives a polynomial $T(X)$ with odd integer coefficients and*
>
> $$
> T(X)T^*(X)=2^{2s}w^2
> \quad\text{in }\mathbb Z[X]/(X^{2^{2s}}-1).
> $$

Every positive integer $u$ has a unique power of two times an odd part.
The notation $u=2^{s-1}w$ keeps the $u$ already chosen in $n=4u^2$.

Since $2^{2s}$ divides $n$, reducing exponents modulo $2^{2s}$ defines a
ring map from $\mathbb Z[X]/(X^n-1)$ to the smaller group ring. Explicitly,

$$
T(X)=\sum_{r=0}^{2^{2s}-1}a_rX^r,
\qquad a_r=\sum_{\ell=0}^{w^2-1}h_{r+\ell2^{2s}}.
$$

Each $a_r$ is a sum of the odd number $w^2$ of signs, so it is odd.
These coefficients can exceed $1$ in absolute value; only their oddness
is needed.

The projection preserves multiplication and sends $X^{-1}$ to the inverse
of the image of $X$. It therefore commutes with star. Applying it to
$h(X)h^*(X)=n$ gives the claimed identity, with the same scalar $n$.
For $n=36$, the four residue classes modulo $4$ each collect nine signs.

Source: [the paper, Section 2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
