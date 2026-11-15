# Video 7.1 — Split the Exact Products

## Slide 1 — Turn one alternating product into two ordinary products

Our goal is to separate the even and odd subsets in the exact identities
from Node 6. Let $u>1$ be odd and let $I$ be its distinct prime divisors.
For each subset $S$, use

$$
\zeta_S=\prod_{p\in S}\zeta_p,\qquad
r_S=\frac{d(\zeta_S)}{c(\zeta_S)},\qquad
w_S=\frac{g(\zeta_S)}{c(\zeta_S)}.
$$

The empty product is $1$. The norm identities make every evaluated
polynomial a unit in $A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]$.
For example, $c(\zeta_S)^{-1}=\overline{c(\zeta_S)}/u^2$.
All the ratios therefore make sense in this one ring.

*[Animation: Show an input card for each subset, beginning with the
empty subset labelled $P=1$. Attach its $r_S$ and $w_S$ ratios. Keep a
small panel with the explicit inverse of $c(\zeta_S)$ visible.]*

## Slide 2 — Even subsets upstairs, odd subsets downstairs

Node 6 gives

$$
\prod_{S\subseteq I}r_S^{(-1)^{|S|}}=1.
$$

An even-sized subset contributes exponent $+1$, and an odd-sized subset
contributes exponent $-1$. So the same equality reads

$$
\frac{\prod_{|S|\text{ even}}r_S}
{\prod_{|S|\text{ odd}}r_S}=1.
$$

Multiply by the denominator, a product of units. We obtain the exact
identity

$$
\boxed{\prod_{|S|\text{ even}}r_S=\prod_{|S|\text{ odd}}r_S.}
$$

*[Animation: Move the even-subset cards to the numerator and the
odd-subset cards to the denominator. Multiply both sides by the
odd-subset product, then display the two products on opposite sides
of an equals sign. Keep the label “exact equality in $A$.”]*

## Slide 3 — Two primes show the pattern

For $u=3$, there are only two subsets, so the identity is
$r_\varnothing=r_{\{3\}}$.
For $u=15$, the distinct primes are $3$ and $5$. The four subsets give

$$
r_\varnothing r_{\{3,5\}}=r_{\{3\}}r_{\{5\}}.
$$

This does not say that all four ratios are equal. It says that two
products are equal. These are the product identities we need for the
general argument.

*[Animation: First show the two cards for $u=3$. Replace them with a
square of four cards for $u=15$: $\varnothing$, $\{3\}$, $\{5\}$,
and $\{3,5\}$. Join the even corners into one product and the odd
corners into the other. Do not rotate all four evaluations together.]*

## Slide 4 — Repeat for the other family

The identity for $w_S$ has the same form. Moving its odd-subset factors
also gives

$$
\boxed{\prod_{|S|\text{ even}}w_S=\prod_{|S|\text{ odd}}w_S.}
$$

Both equalities now involve finite products with positive exponents.
We can expand each side directly and compare its linear terms.

*[Animation: Place the $r_S$ and $w_S$ product equalities in two rows.
Remove the fraction bars from the earlier display and highlight the
individual factors that will be expanded in Node 7.2.]*

Detailed exposition: [Node 7.1](../../nodes/split-exact-products.md).
Source: the paper, Section 4, equations (4.4) and (4.10).
