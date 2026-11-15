---
id: evaluation-units
title: Why We Can Divide
shortTitle: Why We Can Divide
summary: The odd norm makes every evaluated polynomial invertible before reduction.
number: "6.2"
draft: true
video: null
mapPosition: [440, 24]
mapSummary: '$c_S^{-1}=\overline{c_S}/u^2$'
---

## A ring for all the evaluations

Let $I$ be the distinct primes dividing the odd integer $u>1$, with
the roots $\zeta_p$ chosen in Node 4. Put

$$
B=\mathbb Z[i,\{\zeta_p:p\in I\}],
\qquad A=B[1/u].
$$

The ring $A$ allows division by powers of $u$. For $S\subseteq I$, write
$\zeta_S=\prod_{p\in S}\zeta_p$ and $c_S=c(\zeta_S)$; define $d_S,g_S$
in the same way. The empty product is $1$.

The norm identities give

$$
x_S\overline{x_S}=u^2
\qquad(x_S\in\{c_S,d_S,g_S\}).
$$

Consequently every $x_S$ is a unit of $A$, with the explicit inverse

$$
x_S^{-1}=\frac{\overline{x_S}}{u^2}.
$$

This justifies division by $c_S$ before taking any congruence. For $u=3$,
the ring is $\mathbb Z[i,\omega,1/3]$, and the inverse is
$\overline{c_S}/9$.

## Reduction is nonzero and has characteristic two

We reduce $A$ modulo the ideal $(1+i)A$. Since
$2=(1+i)(1-i)$, the resulting ring has $2=0$. We must also know that
it has $1\ne0$.

The cyclotomic ring $B$ is a nonzero free abelian group of finite rank,
so $B/2B\ne0$. Choose a maximal ideal $\mathfrak m$ of $B$ containing
$2$. In its residue field, $(1+i)^2=2i=0$ forces $1+i=0$.
Thus $1+i\in\mathfrak m$. The odd integer $u$ has residue $1$, so
$u\notin\mathfrak m$.

Therefore $\mathfrak m$ remains a proper ideal after adjoining $1/u$,
and contains $(1+i)A$. This proves that $A/(1+i)A$ is a nonzero ring
of characteristic two. We do not need it to be a field or a domain.

**Output.** All the required denominators are units, and reduction takes
place in one nonzero ring of characteristic two. Algebraic congruence
here has no meaning of geometric closeness on the complex circle.

Source: [the paper, Section 4, the local-ring setup before equation (4.3)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf). The paper works in a localization at one maximal ideal above $2$; adjoining $1/u$ gives the common ring used in this exposition.
