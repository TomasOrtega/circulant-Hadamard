# Video 3.4 — Parity of Sign Columns

## Slide 1 — Check one coefficient position

We want to divide $h(1,P),h(-1,P),h(i,P)$ by two while keeping integer
or Gaussian-integer coefficients. It is enough to check one power $P^b$
at a time.

Call its coefficients in the four sign polynomials $a_0,a_1,a_2,a_3$.
Each is $+1$ or $-1$, so each is odd.

*[Animation: Select the same $P^b$ term in $H_0(P),\ldots,H_3(P)$.
Bring its four coefficients into view as $a_0,a_1,a_2,a_3$, each labeled
“odd.” Keep $P^b$ fixed throughout the calculation.]*

## Slide 2 — The real combinations are even

At $Z=1$ and $Z=-1$, the two coefficients are

$$
a_0+a_1+a_2+a_3,\qquad a_0-a_1+a_2-a_3.
$$

Modulo two, changing a sign does not change its residue. Both expressions
are therefore congruent to $1+1+1+1=0$. Their halves are integers.

*[Animation: Reduce each $a_j$ to $1$ in a panel labeled “modulo $2$.”
Show that both plus and minus signs lead to the same even sum. Return
to the original integer expressions and place a division by two around
each one.]*

## Slide 3 — The Gaussian combination is even in both parts

At $Z=i$, the coefficient is

$$
(a_0-a_2)+i(a_1-a_3).
$$

Each difference of two signs is even. Hence

$$
\frac{a_0-a_2}{2}+i\frac{a_1-a_3}{2}
$$

is a Gaussian integer. For the single column $(-1,1,1,-1)$, the three
half-coefficients are $0,0,-1+i$.

The argument applies independently at every coefficient position. Thus
all three polynomials can be halved as required, using only the common
signs and no norm calculation.

*[Animation: Separate the real and imaginary differences, label both
“even,” and divide each by two. Briefly substitute the example column,
labeling it as one coefficient check rather than a Hadamard construction.
Then repeat the check symbolically across all powers of $P$.]*

Source: [the paper, Section 4, equations (4.1)–(4.2)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
