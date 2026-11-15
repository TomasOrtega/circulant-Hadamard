---
id: sign-ratio-congruences
title: The Ratios Have Residue One
shortTitle: Ratios Have Residue One
summary: Divisibility from the common signs survives evaluation and division by the unit denominators.
number: "6.3"
draft: true
video: null
mapPosition: [440, 200]
mapSummary: '$R\equiv W\equiv1\pmod{1+i}$'
---

## Start with exact divisibility

Node 5 established coefficientwise identities

$$
\begin{aligned}
d(P)-c(P)&=2a(P),\\
g(P)-c(P)&=(1+i)b(P),
\end{aligned}
$$

where $a(P)$ has integer coefficients and $b(P)$ has Gaussian-integer
coefficients. These exact quotients were formed before reduction.

Use the ring $A$ and evaluation notation from Node 6.2. Since each $c_S$
is a unit, define the units

$$
r_S=\frac{d_S}{c_S},\qquad w_S=\frac{g_S}{c_S}.
$$

Evaluating the identities and dividing gives

$$
\begin{aligned}
r_S-1&=2\frac{a(\zeta_S)}{c_S},\\
w_S-1&=(1+i)\frac{b(\zeta_S)}{c_S}.
\end{aligned}
$$

Both right sides belong to $(1+i)A$, because $1+i$ divides $2$.
Therefore $r_S\equiv w_S\equiv1\pmod{1+i}$ for every $S$.

## Pass to the comparison products

Unpacking the Δ-quotients gives

$$
\begin{aligned}
R&=\prod_{S\subseteq I}r_S^{(-1)^{|S|}},\\
W&=\prod_{S\subseteq I}w_S^{(-1)^{|S|}}.
\end{aligned}
$$

Each factor is a unit with residue $1$. Its inverse also has residue $1$:
reducing $r_Sr_S^{-1}=1$ shows this directly, and the same applies to
$w_S$. Thus the negative exponents cause no problem, and

$$
R\equiv W\equiv1\pmod{1+i}.
$$

For $u=3$, these products are just $r_\varnothing/r_{\{3\}}$ and
$w_\varnothing/w_{\{3\}}$, comparing the evaluations at $1$ and $\omega$.

**Output.** Both comparison products have residue $1$. This is an
algebraic condition, not a small angle or distance from $1$.

Source: [the paper, Section 4, equations (4.3)–(4.8)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
