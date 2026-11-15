---
id: order-is-even
title: Pair the Dot-Product Terms
shortTitle: Pair +1 and −1 Terms
mapTitle: 'Pair $+1$ and $-1$ Terms'
summary: Orthogonality pairs each positive contribution with a negative one, forcing an even number of terms.
number: "2.2"
draft: false
video:
  src: media/order-is-even.mp4
  poster: media/thumbnails/order-is-even.jpg
  captions: media/order-is-even.vtt
  duration: 128.666667
foundation: true
mapPosition: [440, 24]
mapSummary: '$n$ is even'
---

> **Lemma (An even square).** *A Hadamard matrix of order $n>1$ has even
> order. If it is circulant, the square restriction therefore gives*
>
> $$
> n=4u^2\qquad\text{for some positive integer }u.
> $$

Choose two distinct rows. Suppose their dot product contains $a$ positive
terms and $b$ negative terms. All entries are signs, so every product is
$+1$ or $-1$. Orthogonality and the number of positions give

$$
a-b=0,\qquad a+b=n.
$$

Thus $a=b$ and $n=2a$ is even. The order-four example illustrates this:

$$
(-1,1,1,1)\cdot(1,-1,1,1)=-1-1+1+1=0.
$$

For a circulant matrix, Node 2.1 also gives $n=m^2$ for a positive integer
$m$. An odd integer has odd square, so $m$ must be even. Write $m=2u$;
then $n=4u^2$. We have not yet proved that this same $u$ is odd.

Source: [the paper, Section 2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
