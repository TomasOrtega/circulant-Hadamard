# Video 6.3 — The Ratios Have Residue One

## Slide 1 — Keep the exact divisions

Let $u>1$ be odd, and let $I$ be its set of distinct prime divisors.
Node 5 proved the coefficientwise identities

$$
d(P)-c(P)=2a(P),\qquad
g(P)-c(P)=(1+i)b(P),
$$

where $a(P)$ has integer coefficients and $b(P)$ has Gaussian-integer
coefficients. These are polynomials obtained by exact division before
any reduction.

Use the single evaluation ring
$A=\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]$ from Node 6.2. For
$\zeta_S=\prod_{p\in S}\zeta_p$, write $c_S=c(\zeta_S)$ and similarly
for $d_S,g_S$. All three evaluations are units.

*[Animation: Bring in the two divisibilities from Node 5. Replace each
divisibility symbol by an equality with an integral polynomial quotient.
Send both identities through an evaluation box labeled $P=\zeta_S$.
Keep the unit label attached to $c_S$.]*

## Slide 2 — Subtract one from each ratio

Define

$$
r_S=\frac{d_S}{c_S},\qquad w_S=\frac{g_S}{c_S}.
$$

Divide the evaluated identities by $c_S$:

$$
\begin{aligned}
r_S-1&=2\frac{a(\zeta_S)}{c_S},\\
w_S-1&=(1+i)\frac{b(\zeta_S)}{c_S}.
\end{aligned}
$$

The remaining quotients belong to $A$. Since $1+i$ divides $2$, both
right sides vanish on reduction. Therefore $r_S$ and $w_S$ each have
residue one. We have divided only by a unit, not by a zero residue.

*[Animation: Rewrite $d_S/c_S-1$ as $(d_S-c_S)/c_S$ and substitute the
first exact difference; repeat for $g_S$. Mark the factors $2$ and
$1+i$, then reduce them to zero. Leave $r_S\equiv1$ and $w_S\equiv1$
on an algebra board, separate from any phase diagram.]*

## Slide 3 — Products and inverses keep residue one

Unpacking the Δ-comparisons gives

$$
R=\prod_{S\subseteq I}r_S^{(-1)^{|S|}},\qquad
W=\prod_{S\subseteq I}w_S^{(-1)^{|S|}}.
$$

The factors are units with residue one. Their inverses also have residue
one, because reducing $r_Sr_S^{-1}=1$ gives the inverse of $1$.
Consequently every factor in both alternating products reduces to one:

$$
\boxed{R\equiv W\equiv1\pmod{1+i}.}
$$

For $u=3$, put $\omega=e^{2\pi i/3}$. Then
$R=r_\varnothing/r_{\{3\}}$ and $W=w_\varnothing/w_{\{3\}}$, using the
two inputs $P=1$ and $P=\omega$. There are more factors when $u$ has
several distinct prime divisors. The same product-and-inverse rule applies.

*[Animation: Arrange the factors in numerator and denominator rows,
according to subset parity. Replace every factor by $1$, including the
inverse factors. Collapse both rows to the boxed congruences. Keep the
equality $R=W=1$ unrevealed until odd-order rigidity is applied.]*

Source: [the paper, Section 4, equations (4.3)–(4.8)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
