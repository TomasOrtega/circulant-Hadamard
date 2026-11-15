# Video 3.5 — Normalize the Norm Identities

## Slide 1 — Bring the two checks together

Evaluation gave three polynomials with norm $4u^2$. The parity check
showed that their coefficients can be divided by two. Define

$$
\begin{aligned}
c(P)&=\frac{h(1,P)}2,\\
d(P)&=\frac{h(-1,P)}2,\\
g(P)&=\frac{h(i,P)}2.
\end{aligned}
$$

The first two have integer coefficients; the third has Gaussian-integer
coefficients. Our goal is to compute their new norms.

*[Animation: Bring together the cards “norm $4u^2$” and “coefficients
divisible by $2$.” Display the three definitions, labeling the coefficient
rings $\mathbb Z$, $\mathbb Z$, and $\mathbb Z[i]$.]*

## Slide 2 — Divide both factors by two

Star fixes the real number two. Thus dividing a polynomial by two also
divides its star by two. For example,

$$
c(P)c^*(P)
=\frac{h(1,P)\bigl(h(1,P)\bigr)^*}{4}
=u^2.
$$

The same calculation applies to $d(P)$ and $g(P)$, giving

$$
\boxed{c(P)c^*(P)=d(P)d^*(P)=g(P)g^*(P)=u^2.}
$$

For $g(P)$, star includes conjugation of the Gaussian coefficients.

*[Animation: Put a factor $1/2$ on the evaluated polynomial and another
on its star. Multiply them to $1/4$, then cancel the factor four in
$4u^2$. In the guiding case, display $36/4=9$.]*

## Slide 3 — The circle consequence

Choose any $u^2$th root of unity $\zeta$. At that input, star becomes
complex conjugation, so each norm identity says the squared absolute
value is $u^2$. Therefore

$$
|c(\zeta)|=|d(\zeta)|=|g(\zeta)|=u.
$$

For $u=3$, all these outputs lie on the circle of radius three. Their
lengths are fixed; the later nodes will compare their phases.

*[Animation: Send allowed inputs $\zeta$, with $\zeta^{u^2}=1$, through
three boxes labeled $c(P),d(P),g(P)$. Put the output values on a circle
of radius $u$, then specialize its label to $3$. Keep input roots and
output values in separate planes; do not move $P$ through arbitrary
complex inputs.]*

Source: [the paper, Section 4, equations (4.1)–(4.2)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
