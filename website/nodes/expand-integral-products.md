---
id: expand-integral-products
title: Expand Products with Exact Quotients
shortTitle: Expand the Products
summary: The sign divisibilities let us separate the linear terms from terms with two or more factors.
number: "7.2"
draft: true
video: null
mapPosition: [440, 24]
mapSummary: '$\prod_j(1+t x_j)=1+t\sum_jx_j+t^2Q$'
---

> **Lemma (Exact finite-product expansion).** For any finite index set
> $F$, elements $x_j$ of a commutative ring $A$, and $t\in A$, there is
> $Q\in A$ such that
>
> $$
> \prod_{j\in F}(1+t x_j)=1+t\sum_{j\in F}x_j+t^2Q.
> $$
>
> This identity applies to the evaluated ratios $r_S$ with $t=2$ and
> $w_S$ with $t=1+i$, because their divided differences belong to the
> same evaluation ring.

## The quotients already belong to the ring

Let $I$ be the distinct prime divisors of the odd integer $u>1$, and
put $\zeta_S=\prod_{p\in S}\zeta_p$. Work in
$A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]$ and write
$c_S=c(\zeta_S)$, $d_S=d(\zeta_S)$, $g_S=g(\zeta_S)$.
The ratios are $r_S=d_S/c_S$ and $w_S=g_S/c_S$.
The common sign array gives the coefficientwise divisibilities

$$
\begin{aligned}
\frac{d(P)-c(P)}{2}&\in\mathbb Z[P]/(P^{u^2}-1),\\
\frac{g(P)-c(P)}{1+i}&\in\mathbb Z[i][P]/(P^{u^2}-1).
\end{aligned}
$$

Form these exact polynomial quotients first, then evaluate at $\zeta_S$.
Finally divide by the unit $c_S$. Consequently

$$
\frac{d_S-c_S}{2c_S}\in A,
\qquad
\frac{g_S-c_S}{(1+i)c_S}\in A.
$$

This does not require $2$ or $1+i$ to be invertible in $A$. Their
divisibility was established before evaluation, and
$c_S^{-1}=\overline{c_S}/u^2$ supplies the remaining inverse.
The evaluated quotients are elements of $A$, which allows powers of $u$
in denominators.

We can therefore write the two families of factors exactly as

$$
\begin{aligned}
r_S&=1+2\frac{d_S-c_S}{2c_S},\\
w_S&=1+(1+i)\frac{g_S-c_S}{(1+i)c_S}.
\end{aligned}
$$

## An exact finite-product expansion

For a finite family $x_j\in A$ and $t\in A$, expand by choosing either
$1$ or $t x_j$ from each factor. Choosing no $t x_j$ gives $1$; choosing
exactly one gives $t\sum_jx_j$. Every other term contains at least two
factors of $t$. Thus

$$
\boxed{\prod_j(1+t x_j)=1+t\sum_jx_j+t^2Q,
\qquad Q\in A.}
$$

For example,

$$
(1+t x_1)(1+t x_2)
=1+t(x_1+x_2)+t^2x_1x_2.
$$

There is no approximation or discarded error term: $t^2Q$ collects
all the remaining terms exactly. With a single factor, $Q=0$.

Apply this expansion separately to the two sides of each equality in
Node 7.1. Use $t=2$ for the $r_S$ factors and $t=1+i$ for the $w_S$
factors, with the corresponding displayed quotients as the $x_j$.

**Output.** Each product has a constant term, a linear sum, and a
remainder divisible by $t^2$, all in the original ring $A$.

Source: [the paper, Lemma 4.1](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf). This finite-product calculation supplies the needed first-order identity directly.
