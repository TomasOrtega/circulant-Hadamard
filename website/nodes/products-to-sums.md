---
id: products-to-sums
title: From Products to Sums
shortTitle: From Products to Sums
summary: Turn exact product identities into the additive relation needed for the
  contradiction.
number: 7
draft: true
video: null
mapPosition:
  - 250
  - 660
mapSummary: Σ (−1)^|S| E(ζ_S)/c(ζ_S) ≡ 0
---

## First route: $u=3$, $n=36$

With only $P=1$ and $P=\omega$, the two product identities are equalities of ratios:

$$
\frac{d(1)}{c(1)}=\frac{d(\omega)}{c(\omega)},\qquad
\frac{g(1)}{c(1)}=\frac{g(\omega)}{c(\omega)}.
$$

Put $\lambda=c(\omega)/c(1)$. Then $|\lambda|=1$ and

$$
(c(\omega),d(\omega),g(\omega))=\lambda(c(1),d(1),g(1)).
$$

The triple rotates by one common angle on the radius-three circle. Since $E$ is a fixed linear combination, $E(\omega)=\lambda E(1)$, or equivalently

$$
\frac{E(1)}{c(1)}-\frac{E(\omega)}{c(\omega)}=0.
$$

For this example the additive equality is exact. With several prime divisors, the general argument below uses first-order product expansions before reduction.

## General statement

**Inputs:** $R=W=1$ from Node 6 and $E$ from Node 5.

**Statement:** Split even and odd subsets $S$ in each of the two product identities. Expand products with
$$
\prod_j(1+t x_j)=1+t\sum_j x_j+t^2(\text{integral terms}),
$$
using $t=2$ and $t=1+i$ separately. Cancel 1, divide by $t$ in characteristic zero, **then** reduce modulo $1+i$, and add:
$$
\sum_S(-1)^{|S|}\frac{E(\zeta_S)}{c(\zeta_S)}\equiv0\pmod{1+i}.
$$

**Intuition:** Exact multiplicative rigidity implies an additive relation among the first-order deviations. There is no need to expose a separate linearization lemma or introduce globally named first-order coefficients.

**Output:** Vanishing alternating sum.

## Where the congruences live

For the example, all reductions take place in $\mathbb Z[i,\omega,1/3]/(1+i)$. The denominator values are units because their squared absolute values are $9$. Form divisions by $2$ and $1+i$ in characteristic zero before reducing.

## Source and status

Exposition draft based on [OpenAI, *The circulant Hadamard conjecture*, Sections 2–4 (September 23, 2026)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf). Video scripts and deeper proof graphs will be added later.
