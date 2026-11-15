# Video 3.3 — Evaluate at 1, −1, and i

## Slide 1 — Choose values that respect the relation

Our goal is to turn $h(Z,P)$ into polynomials in $P$ while keeping
the norm identity. The natural substitutions are fourth roots of unity,
because they satisfy $Z^4=1$.

We use $Z=1,-1,i$. Substitution by each of these values respects addition
and multiplication in the quotient ring.

*[Animation: Put the four roots $1,i,-1,-i$ on a unit circle next to
$Z^4=1$. Highlight $1,-1,i$ as the three substitutions, then keep $P$
unchanged while replacing only $Z$.]*

## Slide 2 — Compute the three combinations

Apply the substitutions to the four-polynomial decomposition:

$$
\begin{aligned}
h(1,P)&=H_0(P)+H_1(P)+H_2(P)+H_3(P),\\
h(-1,P)&=H_0(P)-H_1(P)+H_2(P)-H_3(P),\\
h(i,P)&=H_0(P)-H_2(P)\\
&\quad+i\bigl(H_1(P)-H_3(P)\bigr).
\end{aligned}
$$

The first two have integer coefficients. The third has Gaussian-integer
coefficients. Substituting $-i$ simply conjugates those coefficients,
so its polynomial is already determined by the one at $i$.

*[Animation: Under the four terms, show the weights $(1,1,1,1)$,
then $(1,-1,1,-1)$, then $(1,i,-1,-i)$. Collect the last expression
into its real and imaginary parts.]*

## Slide 3 — Check the star operation

For Gaussian coefficients, star reverses powers of $P$ and conjugates
coefficients:

$$
f^*(P)=\sum_b\overline{f_b}P^{-b}.
$$

A term $h_{a,b}Z^aP^b$ becomes $h_{a,b}\epsilon^aP^b$ after evaluation.
Taking star gives $h_{a,b}\overline\epsilon^{\,a}P^{-b}$.
Evaluating the original starred term instead gives
$h_{a,b}\epsilon^{-a}P^{-b}$. They agree because
$\overline\epsilon=\epsilon^{-1}$ on the unit circle.

*[Animation: Follow one term along two paths: “evaluate, then star”
and “star, then evaluate.” Show the endpoints matching, with
$\overline\epsilon=\epsilon^{-1}$ connecting the coefficient factors.]*

## Slide 4 — The norm is preserved

Since evaluation preserves the product and star, the identity
$h(Z,P)h^*(Z,P)=4u^2$ becomes

$$
h(\epsilon,P)\bigl(h(\epsilon,P)\bigr)^*=4u^2.
$$

This holds for each of our three choices. The norm is still $36$ in
the guiding case. Once parity permits division by two, the normalized
norm will be $9$.

*[Animation: Carry the same scalar $4u^2$ into all three evaluated
identities. For $u=3$, label it $36$. Preview division by two on both
factors, but leave that step for the normalization node.]*

Source: [the paper, Section 4, equations (4.1)–(4.2)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
