---
id: signs-become-all-ones
title: Signs Become All Ones
shortTitle: Signs Become All Ones
summary: The common sign array becomes an all-ones polynomial after reduction.
number: 5
draft: true
video: null
mapPosition:
  - 40
  - 500
mapSummary: '$E(P)$ reduces to all ones'
---

## Guiding example: $u=3$, $n=36$

The same 36 signs produced all three polynomials. Form

$$
E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
$$

Coefficientwise divisibility makes this a Gaussian-integer polynomial. For $u=3$,

$$
E(P)\equiv J(P)=1+P+\cdots+P^8\pmod{1+i}.
$$

In particular, $E(1)\equiv9\equiv1$, whereas $E(\omega)\equiv3(1+\omega+\omega^2)=0$. These are congruences: they do not assert the complex equality $E(\omega)=0$.

## General statement

**Input:** The three objects $c,d,g$ came from one common array of signs.

**Define just one auxiliary polynomial:**
$$
E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
$$

**Statement:** Using the four expressions $H_j$,
$$
E(P)=-H_3(P)+(i-1)\frac{H_1(P)+H_2(P)}2.
$$
All the displayed quotients have Gaussian-integer coefficients. Because every coefficient of $H_3$ is $\pm1$,
$$
E(P)\equiv J(P):=1+P+\dots+P^{u^2-1}\pmod{1+i}.
$$
Also $d-c$ is divisible by $2$, while $g-c$ is divisible by $1+i$.

**Intuition:** A specially chosen combination of three substitutions becomes the uniform all-ones signal after reduction, independent of the original signs.

**Output:** The key sign congruence and divisibility for Node 6.

## Where the congruences live

For the example, all reductions take place in $\mathbb Z[i,\omega,1/3]/(1+i)$. The denominator values are units because their squared absolute values are $9$. Form divisions by $2$ and $1+i$ in characteristic zero before reducing.

## Source and status

Exposition draft based on [OpenAI, *The circulant Hadamard conjecture*, Sections 2–4 (September 23, 2026)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf). Video scripts and deeper proof graphs will be added later.
