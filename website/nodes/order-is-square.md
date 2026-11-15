---
id: order-is-square
title: Evaluate at 1
shortTitle: Evaluate at 1
mapTitle: 'Evaluate at $1$'
summary: Substituting 1 turns the polynomial identity into the square of the row sum.
number: "2.1"
draft: false
video:
  src: media/order-is-square.mp4
  poster: media/thumbnails/order-is-square.jpg
  captions: media/order-is-square.vtt
  duration: 96.933333
foundation: true
mapPosition: [40, 24]
mapSummary: '$n=h(1)^2$'
---

> **Lemma (The order is a square).** *If a circulant Hadamard matrix has
> first-row polynomial $h(X)$ and order $n$, then*
>
> $$
> n=h(1)^2=\left(\sum_{j=0}^{n-1}h_j\right)^2.
> $$

Write $h(X)=\sum_{j=0}^{n-1}h_jX^j$, with $h_j=\pm1$. The encoding from
Node 1 gives $h(X)h^*(X)=n$ in $\mathbb Z[X]/(X^n-1)$, where star reverses
powers. Substitution $X=1$ is valid because $1^n-1=0$.

Every positive or negative power of $1$ is $1$, so

$$
h^*(1)=\sum_jh_j1^{-j}=\sum_jh_j=h(1).
$$

Evaluating the product therefore gives $n=h(1)h^*(1)=h(1)^2$.
The row sum $h(1)$ is an integer, hence $n$ is a perfect square.

For $(-1,1,1,1)$ the sum is $2$, giving $n=4$. A hypothetical order-$36$
row must sum to $6$ or $-6$; this is a necessary condition, not a construction.

Source: [the paper, Section 2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
