# Video 8.1 — The Nontrivial Roots Cancel the Ones

## Slide 1 — The evaluations we need

Our goal is to evaluate

$$
J(P)=1+P+\cdots+P^{u^2-1}
$$

at the roots used in our alternating sum. Here $u>1$ is odd, $I$ is
the set of its distinct prime divisors, and
$\zeta_S=\prod_{p\in S}\zeta_p$ for chosen primitive $p$th roots.
We will prove $J(\zeta_S)=0$ for every nonempty subset $S$.

*[Animation: Show the subset cards from the alternating sum. Move the
empty-subset card, labelled $P=1$, aside for Node 8.2. Highlight the
remaining cards and the target $J(\zeta_S)=0$.]*

## Slide 2 — Why a nonempty subset gives a nontrivial root

The order of $\zeta_S$ is the product of the distinct primes in $S$.
To see why, put $m=\prod_{p\in S}p$. We have $\zeta_S^m=1$.
For any $p\in S$, raising to $m/p$ removes the other root factors
and leaves $\zeta_p^{m/p}\ne1$.
Thus the order contains every prime in $S$ and is exactly $m$.

For nonempty $S$, this order is greater than one and divides $u^2$.
Consequently $\zeta_S\ne1$ and $\zeta_S^{u^2}=1$.

*[Animation: Use $u=15$ and $S=\{3,5\}$. Raise
$\zeta_3\zeta_5$ to the fifth power to isolate the cube-root factor,
and to the third power to isolate the fifth-root factor. Display
order $15$, then return to the general product of distinct primes.]*

## Slide 3 — Use the finite geometric sum

Multiplying the all-ones polynomial by $P-1$ gives

$$
(P-1)J(P)=P^{u^2}-1.
$$

Substitute $P=\zeta_S$. The right side is zero, so

$$
(\zeta_S-1)J(\zeta_S)=0.
$$

These values lie in a characteristic-zero domain inside $\mathbb C$.
Since $\zeta_S-1\ne0$, cancellation gives

$$
\boxed{J(\zeta_S)=0.}
$$

This is exact. We have not reduced modulo $1+i$.

*[Animation: Display the two shifted rows in $(P-1)J(P)$ and cancel
matching powers, leaving $P^{u^2}-1$. Substitute the root, then
cancel the nonzero factor in the domain. Label the result “exact zero.”]*

## Slide 4 — Nine terms make three closed triangles

For $u=3$, our nontrivial input is $\omega=e^{2\pi i/3}$.
The nine powers repeat the same three roots three times:

$$
J(\omega)=3(1+\omega+\omega^2)=0.
$$

The three vectors in each group sum to zero. The geometric-sum proof
extends this cancellation to every nonempty-subset input. The remaining
input $P=1$ behaves differently, and we examine it next.

*[Animation: Draw nine root vectors, group them into three triples,
and place each triple head to tail to form a closed equilateral
triangle. Remove the zero groups and return to the waiting $P=1$ card.]*

Detailed exposition: [Node 8.1](../../nodes/roots-cancel-ones.md).
Source: the paper, Section 4, the all-ones evaluation after equation (4.11).
