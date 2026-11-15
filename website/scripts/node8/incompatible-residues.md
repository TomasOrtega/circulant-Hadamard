# Video 8.4 — The Two Residues Cannot Agree

## Slide 1 — Two conclusions about one element

Our goal is to close the contradiction for every odd $u>1$.
Assume there is a circulant Hadamard matrix of order $4u^2$.
Its polynomials give the element

$$
\mathcal S=\sum_{S\subseteq I}(-1)^{|S|}
\frac{E(\zeta_S)}{c(\zeta_S)},
\qquad \zeta_S=\prod_{p\in S}\zeta_p,
$$

where $I$ is the set of distinct prime divisors of $u$ and the empty
product is $1$. The product argument in Node 7 proves
$\mathcal S\equiv0\pmod{1+i}$.
The all-ones calculation in Node 8.3 proves
$\mathcal S\equiv1\pmod{1+i}$.

*[Animation: Draw two short proof branches ending at the same formula
for $\mathcal S$. Label the product branch with residue $0$ and the
all-ones branch with residue $1$.]*

## Slide 2 — The residues live in the same nonzero ring

Both statements use the quotient

$$
A/(1+i)A,\qquad
A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u].
$$

Node 6 established that this quotient is nonzero, so its zero and
identity are distinct. All the denominators were units before and
after reduction. The two conclusions would therefore force $0=1$
in one and the same ring. That is impossible.

*[Animation: Put both residue statements inside a single box labelled
$A/(1+i)A$, with $0\ne1$ at its bottom. Bring the two values of
$\mathcal S$ together to reveal the incompatible equality $0=1$.]*

## Slide 3 — State exactly what the contradiction excludes

The assumed matrix cannot exist for any odd $u>1$. The example $u=3$
illustrates the mechanism, and the full subset calculation proves the
general exclusion.

This argument does not exclude $u=1$: the Δ-theorem used earlier
requires $u>1$. We now combine the exclusion with the order restriction
and verify the two remaining matrix orders.

*[Animation: Cross out the range “odd $u>1$,” including $u=3$, while
leaving $u=1$ untouched. Recall the hypothesis $u>1$ on the Δ-theorem
card, then carry the surviving case to Node 8.5.]*

Detailed exposition: [Node 8.4](../../nodes/incompatible-residues.md).
Source: the paper, Section 4, the contradiction and Remark 4.2.
