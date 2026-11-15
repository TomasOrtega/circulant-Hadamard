# Video 6.1 — Compare the Delta Values

## Slide 1 — Recall the arithmetic input

Let $u>1$ be odd. The polynomials $c(P),d(P),g(P)$ satisfy

$$
c(P)c^*(P)=d(P)d^*(P)=g(P)g^*(P)=u^2.
$$

Let $I$ be the set of distinct primes dividing $u$. Choose a primitive
$p$th root $\zeta_p$ for each $p\in I$, and put
$\zeta_S=\prod_{p\in S}\zeta_p$, with $\zeta_\varnothing=1$.

Every evaluation has magnitude $u$, so none is zero. For any of our
three polynomials, Node 4 defines

$$
\Delta(f)=\prod_{S\subseteq I}f(\zeta_S)^{(-1)^{|S|}}
$$

and proves that it is a root of unity of odd order. That theorem is
the input for this step.

*[Animation: Show one card for each subset $S$. Place even subsets in
the numerator and odd subsets in the denominator. Send the three
polynomials through the same construction and attach “odd order” to
each resulting Δ-value.]*

## Slide 2 — Compare with c(P)

We want to compare the phase information for the three polynomials.
Use $c(P)$ as the reference and define

$$
R=\frac{\Delta(d)}{\Delta(c)},\qquad
W=\frac{\Delta(g)}{\Delta(c)}.
$$

Both are well-defined complex numbers. The question is whether dividing
two odd-order roots of unity preserves odd order.

*[Animation: Keep $\Delta(c)$ at the center of the calculation. Draw
two comparison arrows, one from $\Delta(d)$ and one from $\Delta(g)$,
and write the quotient attached to each arrow. These compare Δ-values,
not individual polynomial coefficients.]*

## Slide 3 — A common odd exponent

Suppose $\alpha^m=1$ and $\beta^n=1$, with $m,n$ odd. Then

$$
\left(\frac{\alpha}{\beta}\right)^{mn}
=\frac{(\alpha^m)^n}{(\beta^n)^m}=1.
$$

Thus the order of the quotient divides the odd number $mn$ and is
itself odd. Applying this to both comparisons proves that $R$ and $W$
are roots of unity of odd order. Order one is included.

*[Animation: Raise the quotient to the exponent $mn$, regroup the powers,
and replace numerator and denominator by $1$. Highlight that the product
of the two odd exponents remains odd. Carry this conclusion to both
$R$ and $W$.]*

## Slide 4 — The two-input example

For $u=3$, write $\omega=e^{2\pi i/3}$. There are just two subset roots,
$1$ and $\omega$, and the comparisons become

$$
R=\frac{d(1)/c(1)}{d(\omega)/c(\omega)},\qquad
W=\frac{g(1)/c(1)}{g(\omega)/c(\omega)}.
$$

Each lies in $\{1,\omega,\omega^2\}$. A comparison equal to one says
that its relative ratio is unchanged between the two inputs. We have
not yet forced that equality; the sign information will supply a
second condition.

*[Animation: Display the two input cards and unpack each Δ-quotient into
the shown ratio of ratios. Put the three candidate values on a separate
unit circle. Leave all candidates available and highlight the next
branch, which brings in the signs.]*

Source: [the paper, Proposition 3.4 and Section 4 before equation (4.3)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
