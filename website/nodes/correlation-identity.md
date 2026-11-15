---
id: correlation-identity
title: Correlation Identity
shortTitle: Correlation Identity
summary: Each coefficient of h(X)h*(X) is a dot product with a cyclic shift of the
  original row.
number: "1.4"
draft: true
video: null
mapPosition:
  - 460
  - 340
mapSummary: '$[X^a](h(X)h^*(X))=\sum_j h_jh_{j-a}$'
---

## The coefficient identity

Let $h_0,\ldots,h_{n-1}$ be arbitrary integers and set $h(X)=\sum_j h_jX^j$ in $\mathbb Z[X]/(X^n-1)$. For $0\leq a<n$, write $[X^a]F$ for the coefficient of $X^a$ in the unique representative of $F$ of degree less than $n$.

**Proposition.** With all coefficient subscripts taken modulo $n$,

$$
[X^a](h(X)h^*(X))=\sum_{j=0}^{n-1}h_jh_{j-a}.
$$

**Proof.** Expand in this group ring:

$$
h(X)h^*(X)=\left(\sum_jh_jX^j\right)\left(\sum_kh_kX^{-k}\right)
=\sum_{j,k}h_jh_kX^{j-k}.
$$

A term contributes to $X^a$ exactly when $j-k\equiv a\pmod n$. Thus $k\equiv j-a\pmod n$, which gives the formula. The list $(h_{j-a})_j$ is the original list shifted $a$ places to the right, so the sum is its dot product with the first row.

Equivalently, the complete product is

$$
h(X)h^*(X)=\sum_{a=0}^{n-1}\left(\sum_{j=0}^{n-1}h_jh_{j-a}\right)X^a.
$$

## The order-four calculation

For the first row $(-1,1,1,1)$:

| Shift $a$ | Right-shifted row | $[X^a](h(X)h^*(X))$ |
| --- | --- | --- |
| $0$ | $(-1,1,1,1)$ | $4$ |
| $1$ | $(1,-1,1,1)$ | $0$ |
| $2$ | $(1,1,-1,1)$ | $0$ |
| $3$ | $(1,1,1,-1)$ | $0$ |

Thus $h(X)h^*(X)=4$. The coefficient identity itself does not require sign coefficients; signs will enter when the constant coefficient is set equal to $n$.

**Output.** One product records all cyclic dot products, for arbitrary integer rows.
