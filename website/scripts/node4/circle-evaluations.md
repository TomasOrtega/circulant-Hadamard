# Video 4.1 — Evaluations on a Circle

Goal: show why the polynomial norm identity puts every allowed evaluation
on the circle of radius $u$.

## Slide 1 — Which inputs can we use?

Let $u>1$ be odd. Our polynomial has Gaussian integer coefficients and
satisfies

$$
f(P)f^*(P)=u^2
\quad\text{in }\mathbb Z[i][P]/(P^{u^2}-1).
$$

We may substitute any $u^2$th root of unity for $P$: these are exactly
the complex numbers that respect the relation $P^{u^2}=1$.
Our goal is to find the distance of each resulting value from the origin.

*[Animation: Draw the allowed inputs on a small unit circle, labeled
“inputs.” For $u=3$, show the nine ninth roots. Highlight the equation
$P^{u^2}=1$ as each input passes through a box labeled $f(P)$. Leave the
larger output plane empty for now.]*

## Slide 2 — Star becomes complex conjugation

Write $f(P)=\sum_j a_jP^j$. Star conjugates the coefficients and reverses
the powers:

$$
f^*(P)=\sum_j\overline{a_j}P^{-j}.
$$

For a root of unity $\zeta$, we have $\zeta^{-1}=\overline\zeta$.
Therefore

$$
f^*(\zeta)
=\sum_j\overline{a_j}\,\overline\zeta^{\,j}
=\overline{f(\zeta)}.
$$

The polynomial star and complex conjugation are different operations,
but they agree after this substitution.

*[Animation: Follow one term $a_jP^j$. Conjugate its coefficient and
reverse its exponent, then substitute $P=\zeta$. Reflect the resulting
complex arrow across the real axis to match conjugating $a_j\zeta^j$.
Combine the terms into the displayed identity.]*

## Slide 3 — The radius is fixed

Now evaluate the norm identity:

$$
f(\zeta)\overline{f(\zeta)}=u^2,
\qquad \boxed{|f(\zeta)|=u.}
$$

Every value is nonzero and lies on the circle of radius $u$.
Its angle can vary with the input, but its distance from the origin cannot.
For $u=3$, the valid example $f(P)=3iP$ places the nine outputs on a
circle of radius three. This example has Gaussian coefficients; it is
not a Hadamard sign row.

Two outputs of equal magnitude have a quotient of magnitude one. That
quotient records the rotation from the denominator's arrow to the
numerator's arrow, which is the comparison we will use next.

*[Animation: Draw the output circle of radius $u$, then specialize its
label to $3$. Use $f(P)=3iP$ to send each input to an output: rotate by
$90^\circ$ and scale by three. Highlight two output arrows and show their
quotient on a separate unit circle. Keep input roots and output values
clearly labeled.]*

Website exposition: [Evaluations on a Circle](../../nodes/circle-evaluations.md).
