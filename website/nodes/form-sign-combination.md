---
id: form-sign-combination
title: Form the Combination
shortTitle: Form the Combination
summary: The common sign array makes both quotients in E(P) integral and gives an exact formula for their sum.
number: "5.1"
draft: true
video: null
mapPosition: [40, 24]
mapSummary: 'Define and simplify $E(P)$'
---

## Keep the common sign array

Let $u$ be a positive odd integer. Work in
$\mathbb Z[i][P]/(P^{u^2}-1)$, using the coefficient positions
$1,P,\ldots,P^{u^2-1}$. From Node 3, we have four polynomials

$$
H_a(P)=\sum_{r=0}^{u^2-1}h_{a,r}P^r,
\qquad h_{a,r}\in\{-1,1\}.
$$

The three normalized evaluations are

$$
c(P)=\frac{H_0(P)+H_1(P)+H_2(P)+H_3(P)}2,
$$

$$
d(P)=\frac{H_0(P)-H_1(P)+H_2(P)-H_3(P)}2,
$$

$$
g(P)=\frac{H_0(P)-H_2(P)}2
+i\frac{H_1(P)-H_3(P)}2.
$$

Their common origin is the assumption we need. The coefficient calculation
below does not require their norm identities.

## Define E(P) integrally

Set

$$
E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
$$

To justify each quotient, subtract the formulas above:

$$
\frac{d(P)-c(P)}2=-\frac{H_1(P)+H_3(P)}2,
$$

$$
\begin{aligned}
\frac{g(P)-c(P)}{1+i}
&=-\frac{H_2(P)+H_3(P)}2\\
&\quad+i\frac{H_1(P)+H_2(P)}2.
\end{aligned}
$$

Every numerator on the right is a sum of two sign polynomials. At each
coefficient position it is the sum of two odd integers, so it is even.
The first quotient therefore has integer coefficients, and the second has
Gaussian-integer coefficients. In particular,

$$
d(P)-c(P)\in2\bigl(\mathbb Z[P]/(P^{u^2}-1)\bigr),
$$

$$
g(P)-c(P)\in(1+i)\bigl(\mathbb Z[i][P]/(P^{u^2}-1)\bigr).
$$

These are exact coefficientwise divisions in characteristic zero, made
before reducing modulo $1+i$.

## Combine the terms

Adding the two quotient formulas yields

$$
E(P)=-H_3(P)+(i-1)\frac{H_1(P)+H_2(P)}2.
$$

The half-sum is an integer polynomial, and $i-1$ is a multiple of $1+i$.
This separates the term that will vanish after reduction from the sign
polynomial that remains.

**Output.** An integral definition of $E(P)$, its exact sign formula, and
the two divisibilities needed later in Node 6. The next step combines
this identity with Gaussian parity.

Source: [the paper, Section 4, equations (4.1) and (4.5)–(4.9)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
