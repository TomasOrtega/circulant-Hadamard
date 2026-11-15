---
id: order-is-square
title: Evaluate at 1
shortTitle: Evaluate at 1
mapTitle: 'Evaluate at $1$'
summary: Substituting 1 turns the polynomial identity into the square of the row sum.
number: "2.1"
draft: true
video: null
foundation: true
mapPosition: [40, 24]
mapSummary: '$n=h(1)^2$'
---

## Statement

For a circulant Hadamard matrix of order $n$, the first-row polynomial satisfies
$h(X)h^*(X)=n$ in $\mathbb Z[X]/(X^n-1)$. Substituting $X=1$ gives

$$
n=h(1)^2=\left(\sum_{j=0}^{n-1}h_j\right)^2.
$$

Thus $n$ is a perfect square. The substitution respects $X^n=1$, and
$h^*(1)=h(1)$ because $1^{-1}=1$.

## The example to keep in view

Our row $(-1,1,1,1)$ has sum $2$, so its order is $2^2=4$.
A hypothetical example of order $36$ would need row sum $6$ or $-6$.
That required sum is only a necessary condition for existence.

**Output.** The order is an integer square. The parity step will show that
its square root is even.
