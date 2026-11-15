---
id: odd-comparison-products
title: Compare the Delta Values
shortTitle: Compare the Delta Values
mapTitle: 'Compare the $\Delta$-Values'
summary: The two comparison products inherit odd order from the Delta theorem.
number: "6.1"
draft: true
video: null
mapPosition: [40, 24]
mapSummary: '$R,W$ have odd order'
---

## The arithmetic input

Let $u>1$ be odd. Node 3 supplies $c(P),d(P),g(P)$ with

$$
c(P)c^*(P)=d(P)d^*(P)=g(P)g^*(P)=u^2
$$

in $\mathbb Z[i][P]/(P^{u^2}-1)$. Their evaluations at the roots used
in Node 4 are nonzero. The Δ-theorem therefore applies to all three:
$\Delta(c),\Delta(d),\Delta(g)$ are roots of unity of odd order.

Define

$$
\begin{aligned}
R&=\frac{\Delta(d)}{\Delta(c)},\\
W&=\frac{\Delta(g)}{\Delta(c)}.
\end{aligned}
$$

If roots of unity $\alpha,\beta$ have odd orders $m,n$, then
$(\alpha/\beta)^{mn}=1$. Thus their quotient has order dividing the odd
integer $mn$. Applying this to each comparison shows that $R$ and $W$
also have odd order. Order $1$ is allowed.

## The guiding case

For $u=3$, let $\omega=e^{2\pi i/3}$. The alternating product has just
two factors, so

$$
\begin{aligned}
R&=\frac{d(1)/c(1)}{d(\omega)/c(\omega)},\\
W&=\frac{g(1)/c(1)}{g(\omega)/c(\omega)}.
\end{aligned}
$$

Each belongs to $\{1,\omega,\omega^2\}$, since the three Δ-values do.
These ratios compare the phase changes of the evaluations of $d(P)$ and
$g(P)$ with those of $c(P)$. They do not say that the three evaluated
points coincide.

**Output.** Two roots of unity of odd order. The separate sign input will
give their residues, and the rigidity step will combine the two facts.

Source: [the paper, Proposition 3.4 and Section 4 before equation (4.3)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
