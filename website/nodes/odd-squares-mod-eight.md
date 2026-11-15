---
id: odd-squares-mod-eight
title: Odd Squares Modulo 8
shortTitle: Odd Squares Modulo 8
mapTitle: 'Odd Squares Modulo $8$'
summary: The final coefficient squares would have to sum to both zero and four modulo eight.
number: "2.6"
draft: false
video:
  src: media/odd-squares-mod-eight.mp4
  poster: media/thumbnails/odd-squares-mod-eight.jpg
  captions: media/odd-squares-mod-eight.vtt
  duration: 166.233333
mapPosition: [240, 600]
mapSummary: '$s=1$, so $n=4u^2$ with $u$ odd'
---

> **Lemma (No extra power of two).** *The descent endpoint for $s\geq2$
> is impossible. Consequently a circulant Hadamard order $n>1$ has
> $n=4u^2$ with $u$ odd.*

Suppose $s\geq2$. Node 2.5 produces
$T_{s-1}(X)=\sum_{j=0}^{2^{s+1}-1}b_jX^j$, with all $b_j$ odd, and
$T_{s-1}(X)T_{s-1}^*(X)=4w^2$. The constant coefficient of this product
is the sum of the coefficient squares:

$$
\sum_{j=0}^{2^{s+1}-1}b_j^2=4w^2.
$$

Indeed, $X^jX^{-\ell}$ contributes to the identity position precisely
when $j=\ell$ among these representatives.

For any odd integer $b=2r+1$,

$$
b^2=4r(r+1)+1\equiv1\pmod8,
$$

because one of the consecutive integers $r,r+1$ is even. There are
$2^{s+1}$ such squares, a multiple of eight, so their sum is $0$ modulo
$8$. But $w$ is odd, and $4w^2\equiv4\pmod8$. This is a contradiction.

Therefore $s\geq2$ is impossible. We already know $s\geq1$, so $s=1$.
Our original parameter is $u=2^{s-1}w=w$, hence odd, and $n=4u^2$.
For the smallest excluded case $s=2,w=1$, one fold would require eight
odd squares to sum to $4$; the same residue mismatch is already visible.

Source: [the paper, Section 2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
