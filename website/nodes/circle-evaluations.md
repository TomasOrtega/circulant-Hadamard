---
id: circle-evaluations
title: Evaluations on a Circle
shortTitle: Circle Evaluations
summary: The polynomial norm identity puts every character value on a circle of radius u.
number: "4.1"
draft: false
video:
  src: media/circle-evaluations.mp4
  captions: media/circle-evaluations.vtt
  duration: 164.066667
foundation: true
mapPosition: [240, 24]
mapSummary: 'Every evaluation has modulus $u$'
---

> **Lemma (The evaluation circle).** *If
> $f(P)f^*(P)=u^2$ in $\mathbb Z[i][P]/(P^{u^2}-1)$, then
> $|f(\zeta)|=u$ for every $u^2$th root of unity $\zeta$.*

## Substitute a root of unity

Let $u>1$ be odd, and suppose

$$
f(P)\in\mathbb Z[i][P]/(P^{u^2}-1),
$$

$$
f(P)f^*(P)=u^2.
$$

Here star conjugates the coefficients and reverses the powers:

$$
f(P)=\sum_j a_jP^j,
\qquad f^*(P)=\sum_j\overline{a_j}P^{-j}.
$$

If $\zeta^{u^2}=1$, substitution $P=\zeta$ respects the cycle relation.
Because $\zeta^{-1}=\overline\zeta$, we have

$$
f^*(\zeta)=\overline{f(\zeta)}.
$$

Evaluating the product therefore gives

$$
|f(\zeta)|^2=u^2,
\qquad |f(\zeta)|=u.
$$

Every evaluation is nonzero and lies on the complex circle of radius $u$.
This conclusion places no sign condition on the coefficients of $f(P)$.

## Magnitude and phase

The magnitude gives the distance from the origin. The phase is the angle
of the arrow from the origin to the value, measured modulo a full turn.
Two values on this circle can be written as

$$
a=ue^{i\alpha},\qquad b=ue^{i\beta}.
$$

Their ratio is

$$
\frac ab=e^{i(\alpha-\beta)}.
$$

Thus the ratio has magnitude one and records the rotation from the
denominator's arrow to the numerator's arrow. Equal magnitudes alone
do not restrict that rotation to finitely many angles.

For the guiding case $u=3$, the polynomial $f(P)=3iP$ is a valid example:
its product with its star is $9$. Its values at the nine ninth roots lie
on the radius-three circle. This is an example with Gaussian coefficients,
not a Hadamard sign row.

We can therefore divide any two of these values and compare their phases.

Source: [the paper, Section 3, equation (3.2)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
