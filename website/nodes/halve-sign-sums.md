---
id: halve-sign-sums
title: Parity of Sign Columns
shortTitle: Parity of Sign Columns
summary: Four signs have even sums, and two signs have even differences, so the normalized coefficients remain integral.
number: "3.4"
draft: false
video:
  src: media/halve-sign-sums.mp4
  poster: media/thumbnails/halve-sign-sums.jpg
  captions: media/halve-sign-sums.vtt
  duration: 127.466667
mapPosition: [440, 360]
mapSummary: Even sums and differences
---

> **Lemma (Integral half-evaluations).** *If the coefficients of the four
> polynomials $H_a(P)$ are signs, then $h(1,P)/2$ and $h(-1,P)/2$
> have integer coefficients, while $h(i,P)/2$ has Gaussian-integer
> coefficients.*

Fix a power $P^b$ and call its four coefficients $a_0,a_1,a_2,a_3$.
Every $a_j$ is congruent to $1$ modulo $2$. Hence both
$a_0+a_1+a_2+a_3$ and $a_0-a_1+a_2-a_3$ are even. These are the
coefficients in the first two evaluated polynomials.

For the third evaluation, the coefficient is

$$
(a_0-a_2)+i(a_1-a_3).
$$

Both differences are even, so after division by two the real and
imaginary parts are integers. Applying this argument separately at
every power $P^b$ proves the claim.

For the single sign column $(-1,1,1,-1)$, the three half-coefficients
are $0,0,-1+i$. This illustrates coefficient parity, not a full
Hadamard row or a norm solution. The proof uses the common signs alone;
it does not need $h(Z,P)h^*(Z,P)=4u^2$.

Source: [the paper, Section 4, equations (4.1)–(4.2)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
