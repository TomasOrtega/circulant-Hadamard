# Video 7.2 — Expand Products with Exact Quotients

## Slide 1 — Identify the factors we will expand

Our goal is an exact expansion of each product from Node 7.1. Continue
in $A=\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]$ for odd $u>1$.
For the subset roots $\zeta_S$, abbreviate
$c_S=c(\zeta_S)$, $d_S=d(\zeta_S)$, and $g_S=g(\zeta_S)$.
Then $r_S=d_S/c_S$ and $w_S=g_S/c_S$.

The common sign array supplies exact polynomial quotients

$$
\frac{d(P)-c(P)}2\in\mathbb Z[P]/(P^{u^2}-1),\qquad
\frac{g(P)-c(P)}{1+i}\in\mathbb Z[i][P]/(P^{u^2}-1).
$$

Evaluate these quotients first, then multiply by the unit $c_S^{-1}$.
This puts $(d_S-c_S)/(2c_S)$ and $(g_S-c_S)/((1+i)c_S)$ in $A$.

*[Animation: Show three successive boxes: “exact coefficientwise
division,” “evaluate at $\zeta_S$,” and “multiply by $c_S^{-1}$.”
Carry each of the two quotients through them. Do not draw an inverse
of $2$ or of $1+i$.]*

## Slide 2 — Write each factor as one plus a multiple

We can now write, exactly,

$$
\begin{aligned}
r_S&=1+2\frac{d_S-c_S}{2c_S},\\
w_S&=1+(1+i)\frac{g_S-c_S}{(1+i)c_S}.
\end{aligned}
$$

Both have the form $1+t x_S$ with $x_S\in A$. For the first family,
$t=2$; for the second, $t=1+i$.

*[Animation: In each row, separate the initial $1$, the factor $t$,
and the bracketed element $x_S$. Use matching outlines for the two
instances of the pattern $1+t x_S$.]*

## Slide 3 — Multiply without approximation

For two factors, ordinary multiplication gives

$$
(1+t x_1)(1+t x_2)
=1+t(x_1+x_2)+t^2x_1x_2.
$$

For any finite collection, choose either $1$ or $t x_j$ from each
factor. Choosing no $x_j$ gives $1$. Choosing exactly one gives
$t\sum_jx_j$. Every other choice includes at least two copies of $t$.
Collecting those terms gives

$$
\boxed{\prod_j(1+t x_j)=1+t\sum_jx_j+t^2Q,\qquad Q\in A.}
$$

The remainder is retained exactly; it contains every term with two
or more selected factors. With one factor, $Q=0$.

*[Animation: Expand two factors in a multiplication table. Then show
three factors with terms grouped by how many $t x_j$ choices were made.
Move the terms with two or three choices into a bracket labelled
$t^2Q$. Leave an equals sign, never an approximation sign.]*

## Slide 4 — Keep the two sides separate

Apply the expansion to the even-subset product and the odd-subset
product separately. They have their own linear sums and remainders.
For $u=15$, for example, the $r_S$ identity has two factors on each
side. For $u=3$, each side has one factor and no remainder.

The next step subtracts the expanded products and cancels a common
factor before any modular reduction.

*[Animation: Return to the two product rows from Node 7.1. Expand each
side beneath it into a constant, a linear sum, and a remainder. Keep
all terms on screen and add a next-step label “subtract, then cancel.”]*

Detailed exposition: [Node 7.2](../../nodes/expand-integral-products.md).
Source: the finite-product calculation underlying the paper's Lemma 4.1.
