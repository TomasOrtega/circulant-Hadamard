---
id: split-exact-products
title: Split the Exact Products
shortTitle: Split the Products
summary: Put the even and odd subsets on opposite sides of each exact product identity.
number: "7.1"
draft: false
video:
  src: media/split-exact-products.mp4
  poster: media/thumbnails/split-exact-products.jpg
  captions: media/split-exact-products.vtt
  duration: 153.533333
mapPosition: [40, 24]
mapSummary: '$\prod_{\mathrm{even}}r_S=\prod_{\mathrm{odd}}r_S$'
---

> **Lemma (Separate the two products).** Let $I$ be the distinct primes
> dividing an odd integer $u>1$, and let $r_S,w_S$ be units in
> $A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]$. If
> $\prod_{S\subseteq I}r_S^{(-1)^{|S|}}=
> \prod_{S\subseteq I}w_S^{(-1)^{|S|}}=1$, then
>
> $$
> \prod_{|S|\text{ even}}r_S=\prod_{|S|\text{ odd}}r_S,
> \qquad
> \prod_{|S|\text{ even}}w_S=\prod_{|S|\text{ odd}}w_S.
> $$

## The inputs from Node 6

Let $I$ be the distinct primes dividing the odd integer $u>1$.
Choose a primitive $p$th root $\zeta_p$ for each $p\in I$. For
$S\subseteq I$, put $\zeta_S=\prod_{p\in S}\zeta_p$ and
$\varepsilon_S=(-1)^{|S|}$. Write $c_S=c(\zeta_S)$, and similarly
for $d_S,g_S$. We use the same characteristic-zero domain as Node 6:

$$
A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u].
$$

Each evaluated polynomial is a unit of $A$: for example,
$c_S^{-1}=\overline{c_S}/u^2$. Thus the ratios

$$
r_S=\frac{d_S}{c_S},\qquad w_S=\frac{g_S}{c_S}
$$

are units as well. Node 6 gives the exact identities

$$
\prod_{S\subseteq I}r_S^{\varepsilon_S}=1,
\qquad
\prod_{S\subseteq I}w_S^{\varepsilon_S}=1.
$$

## Remove the negative exponents

An even-sized subset has exponent $+1$; an odd-sized subset has exponent
$-1$. Multiply by the products of the odd-subset factors. Since all those
factors are units, the two identities become

$$
\boxed{
\begin{aligned}
\prod_{\substack{S\subseteq I\\ |S|\text{ even}}}r_S
&=\prod_{\substack{S\subseteq I\\ |S|\text{ odd}}}r_S,\\
\prod_{\substack{S\subseteq I\\ |S|\text{ even}}}w_S
&=\prod_{\substack{S\subseteq I\\ |S|\text{ odd}}}w_S.
\end{aligned}
}
$$

These are equalities in $A$, before reduction. Every product now has only
positive exponents, so we can expand both sides directly.

For $u=3$, the two subsets are $\varnothing$ and $\{3\}$. Each product
contains just one factor: $r_\varnothing=r_{\{3\}}$ and
$w_\varnothing=w_{\{3\}}$. These are the equal ratios behind the common
rotation in the overview.

**Output.** Two exact equalities between even-subset and odd-subset
products, ready for the expansion in Node 7.2.

Source: [the paper, Section 4, equations (4.4) and (4.10)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
