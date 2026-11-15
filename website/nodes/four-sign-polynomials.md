---
id: four-sign-polynomials
title: Four Sign Polynomials
shortTitle: Four Sign Polynomials
summary: Collect the terms with the same power of Z into four polynomials in P.
number: "3.2"
draft: true
video: null
foundation: true
mapPosition: [240, 180]
mapSummary: '$h(Z,P)=H_0(P)+\cdots+Z^3H_3(P)$'
---

## Statement

In the Chinese remainder coordinates, collect terms by their power of $Z$:

$$
h(Z,P)=H_0(P)+ZH_1(P)+Z^2H_2(P)+Z^3H_3(P),
$$

where

$$
H_a(P)=\sum_{b=0}^{u^2-1}h_{a,b}P^b,
\qquad h_{a,b}\in\{-1,1\}.
$$

The relation $Z^4=1$ leaves four powers of $Z$, and $P^{u^2}=1$ leaves
$u^2$ coefficient positions in each $H_a(P)$. Uniqueness of these positions
makes the decomposition unambiguous.

## Four rows of nine signs

At order $36$, each $H_a(P)$ contains nine signs. For each fixed power $P^b$,
the four coefficients

$$
(h_{0,b},h_{1,b},h_{2,b},h_{3,b})
$$

form one sign column. Evaluating $Z$ combines these four entries; their
parity will explain why the resulting combinations can be divided by $2$.

**Output.** Four sign polynomials in one variable, ready for the evaluation
and coefficient-parity steps.
