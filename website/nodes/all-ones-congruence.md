---
id: all-ones-congruence
title: All Coefficients Become 1
shortTitle: All Coefficients Become 1
mapTitle: 'All Coefficients Become $1$'
summary: The exact sign formula for E(P) reduces to a polynomial with one in every coefficient position.
number: "5.3"
draft: true
video: null
mapPosition: [240, 220]
mapSummary: The all-ones congruence
---

## Statement

Let $u$ be a positive odd integer, and let $c(P),d(P),g(P)$ come from the
same four sign polynomials as in Node 3. Define $E(P)$ by the integral
quotients from Node 5.1. In $\mathbb Z[i][P]/(P^{u^2}-1)$,

$$
E(P)\equiv1+P+\cdots+P^{u^2-1}\pmod{1+i}.
$$

We call the polynomial on the right the all-ones polynomial and use
$J(P)$ as shorthand:

$$
J(P):=1+P+\cdots+P^{u^2-1}.
$$

The congruence means that every coefficient of $E(P)-J(P)$ is divisible
by $1+i$.

## Proof from the two inputs

The exact formula from Node 5.1 is

$$
E(P)=-H_3(P)+(i-1)\frac{H_1(P)+H_2(P)}2.
$$

The half-sum has integer coefficients. Since $i-1=i(1+i)$, its whole
contribution is divisible by $1+i$. Therefore

$$
E(P)\equiv-H_3(P)\pmod{1+i}.
$$

Write

$$
H_3(P)=\sum_{r=0}^{u^2-1}h_{3,r}P^r,
\qquad h_{3,r}\in\{-1,1\}.
$$

Gaussian parity, proved in Node 5.2, says that $-h_{3,r}\equiv1$ for
every $r$. Reducing each coefficient gives the claimed all-ones polynomial.

This proves a congruence; the original coefficients of $E(P)$ need not
equal $1$. The calculation uses only the common sign array, so it does
not need the norm identities or the oddness of $u$.

## What the next nodes receive

Along with $E(P)\equiv J(P)$, retain the divisibilities established while
forming $E(P)$:

$$
2\mid d(P)-c(P),\qquad 1+i\mid g(P)-c(P).
$$

Divisibility here is coefficientwise in the group ring. These differences
supply the sign input for Node 6. The all-ones congruence will be used in
the final contradiction after the product identities have been converted
to an additive relation.

Source: [the paper, Section 4, equations (4.5)–(4.9)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
