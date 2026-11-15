# Video 6.2 — Why We Can Divide

## Slide 1 — Choose one ring for the evaluations

Before dividing congruences, we need denominators that remain invertible.
Let $u>1$ be odd and let $I$ be its distinct prime divisors. Use the
roots $\zeta_p$ from Node 4 and work in

$$
B=\mathbb Z[i,\{\zeta_p:p\in I\}],\qquad A=B[1/u].
$$

This means that $A$ contains the Gaussian integers, our chosen roots,
and fractions with powers of $u$ in the denominator. For each subset
$S$, put $\zeta_S=\prod_{p\in S}\zeta_p$ and write
$c_S=c(\zeta_S)$, with analogous notation for $d_S,g_S$.

For $u=3$, put $\omega=e^{2\pi i/3}$; the ring is
$\mathbb Z[i,\omega,1/3]$.

*[Animation: Build a box containing $i$ and the chosen roots, labeled
$B$. Enlarge it to $A$ by adding $1/u$. Show evaluation cards $c_S,d_S,g_S$
entering the same box. For the example, replace the root list by $\omega$
and the denominator by $3$.]*

## Slide 2 — The norm supplies an inverse

Evaluating the polynomial norm identities gives

$$
x_S\overline{x_S}=u^2
\qquad(x_S\in\{c_S,d_S,g_S\}).
$$

The conjugate still belongs to $B$, because conjugating a root of unity
replaces it by its inverse. Since we have inverted $u$, the explicit inverse is

$$
\boxed{x_S^{-1}=\frac{\overline{x_S}}{u^2}\in A.}
$$

For the example, divide the conjugate by nine. This proves more than
nonvanishing in the complex plane: the inverse belongs to the particular
ring in which we will reduce.

*[Animation: Multiply an evaluation card by its conjugate to obtain
$u^2$, then divide by $u^2$ to show a product of $1$. Attach an
“invertible in $A$” label to each evaluation. Display $\overline{c(\omega)}/9$
as the example inverse.]*

## Slide 3 — Zero and one remain different

Reduce $A$ modulo $1+i$. The identity $2=(1+i)(1-i)$ shows that the
result has characteristic two, provided it is not the zero ring.

Here is why it is nonzero. The generators of $B$ are roots of unity,
so their powers give finitely many products spanning $B$ over $\mathbb Z$.
As a subgroup of $\mathbb C$, it has no additive torsion. Thus it is
a nonzero free abelian group of finite rank.
Consequently $B/2B$ is nonzero. Choose a maximal ideal $\mathfrak m$
containing $2$; its residue field has characteristic two.

In that field, $(1+i)^2=2i=0$, so $1+i=0$. But the odd integer $u$
has residue one. We can therefore still invert $u$, and this gives a
map from $A$ onto a nonzero field that kills $1+i$. Hence
$A/(1+i)A$ is nonzero too.

*[Animation: Show the chain from $B$ to its characteristic-two residue
field. Send $1+i$ to $0$ and odd $u$ to $1$. Extend the same map to
$A$ by sending $1/u$ to $1$. Keep distinct cards for $0$ and $1$ at
the end, showing that reduction has not collapsed the ring.]*

## Slide 4 — Inverses survive the reduction

The identity $x_Sx_S^{-1}=1$ remains true after applying a ring map.
Thus all our evaluated denominators remain units modulo $1+i$.

We can safely evaluate the sign identities and divide by $c_S$ in
this one ring. We cannot divide by $2$ or $1+i$ after reduction:
both have become zero. The exact polynomial quotients involving those
numbers were formed earlier, before reduction.

*[Animation: Carry the product $x_Sx_S^{-1}=1$ through the reduction map
and retain the inverse labels. Put $c_S$ on the “can divide” side and
$2,1+i$ on the “zero after reduction” side. End with the single ring
$A/(1+i)A$ as the setting for the next steps.]*

Source: [the paper, Section 4 before equation (4.3)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
The paper localizes at one maximal ideal above $2$; this exposition uses
the existing website ring obtained by inverting $u$.
