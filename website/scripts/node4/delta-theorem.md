# Node 4 — The Δ-Theorem

## Video 4: From a Circle to Roots of Unity

*[Animation: Highlight Node 4, the independent arithmetic branch of the
proof map. Leave the branch from the Hadamard sign array visible but muted.]*

In this video, we're going to explain a general result about elements of
a group ring. We allow Gaussian-integer coefficients because the polynomial
$g(P)$ we constructed in Node 3 already has coefficients in $\mathbb Z[i]$.

The result applies to any such polynomial satisfying the required norm
identity, so it also applies beyond our Hadamard construction. To understand
it, let's begin with a concrete example.

## 1. Evaluations on a circle

Consider the cyclic group of order nine, allowing Gaussian-integer
coefficients. We work in

$$
\mathbb Z[i][P]/(P^9-1).
$$

Suppose a polynomial $f(P)$ satisfies

$$
f(P)f^*(P)=9.
$$

Now substitute any ninth root of unity $\zeta$. Since
$\zeta^{-1}=\overline\zeta$, the star evaluates to
$\overline{f(\zeta)}$. Our polynomial identity gives

$$
f(\zeta)\overline{f(\zeta)}=9,
$$

so

$$
\boxed{|f(\zeta)|=3.}
$$

Every one of these evaluations lies on the complex circle of radius three.

*[Animation: On a small input circle, mark the ninth roots of unity. Send
each input through a box labeled $f$ into a separate output plane. Draw the
output circle with radius labeled $3$. The dots on this larger circle are
the values $f(\zeta)$, not the roots $\zeta$ themselves.]*

For example, take $f(P)=3iP$. Its star is $f^*(P)=-3iP^{-1}$,
so their product is indeed $9$. Multiplying a ninth root by $3i$ rotates
it by $90^\circ$ and scales its distance from the origin by a factor of three.

*[Animation: Use $\zeta_9=e^{2\pi i/9}$ and plot
$f(\zeta_9^k)=3i\zeta_9^k$ for $k=0,\ldots,8$. These nine output points
are equally spaced for this particular polynomial. A general $f$ need not
produce equally spaced or distinct output points. Label this as a Gaussian
group-ring example; it is not a Hadamard sign row.]*

Now let us compare the phases of two evaluations, at $P=1$ and
$P=\omega=e^{2\pi i/3}$. Both values lie on the circle of radius three.
To compare their phases, take their quotient and define

$$
\boxed{\Delta(f)=\frac{f(1)}{f(\omega)}.}
$$

Their magnitudes cancel, giving $|\Delta(f)|=1$. The quotient records the
rotation that carries $f(\omega)$ to $f(1)$: the numerator's phase minus
the denominator's phase.

*[Animation: Keep just the two output arrows. Label their angles
$\theta_1$ and $\theta_\omega$. Divide both lengths by three, then show
the directed arc from the denominator's arrow to the numerator's arrow.
On a separate unit circle, draw $\Delta(f)$ at angle
$\theta_1-\theta_\omega$. The direction matters: reversing the quotient
would reverse the rotation.]*

For our polynomial $f(P)=3iP$, the first angle is $90^\circ$ and the second
is $210^\circ$. Their difference is $-120^\circ$, or equivalently
$240^\circ$. Indeed,

$$
\Delta(f)=\frac{3i}{3i\omega}=\omega^2.
$$

In this example, the quotient is a root of unity of odd order. This is
no coincidence. The Δ-theorem says that the norm identity
$f(P)f^*(P)=9$, together with the Gaussian-integer coefficients, forces
the relative phase to be a root of unity of odd order for every such $f$.

*[Animation: Turn clockwise by $120^\circ$ from $f(\omega)$ to $f(1)$.
Copy that same rotation onto the positive real direction on the unit
circle. Its endpoint is $\omega^2$. Do not place the quotient at either
of the two original evaluation points.]*

## 2. The general theorem

For general odd $u>1$, we may have several distinct prime divisors.
We combine more evaluations to capture the same kind of phase information.

Let $I$ be the set of distinct primes dividing $u$. For each $p\in I$,
choose a primitive $p$th root of unity $\zeta_p$. For every subset
$S\subseteq I$, define

$$
\zeta_S=\prod_{p\in S}\zeta_p,
\qquad \zeta_\varnothing=1.
$$

Suppose

$$
f(P)\in\mathbb Z[i][P]/(P^{u^2}-1),
$$

$$
f(P)f^*(P)=u^2.
$$

Each $\zeta_S$ is a $u^2$th root of unity, so we can evaluate $f$ at it.
The norm identity makes every evaluation nonzero. Define the alternating
product

$$
\boxed{\Delta(f)=\prod_{S\subseteq I}f(\zeta_S)^{(-1)^{|S|}}.}
$$

In this product, an evaluation goes in the numerator when its subset
contains an even number of primes, and in the denominator when it contains
an odd number. The empty subset contributes $f(1)$ to the numerator.

When $u=3$, there is just one prime, and this is our original ratio
$f(1)/f(\omega)$. With two distinct primes $p,q$, it becomes

$$
\Delta(f)=\frac{f(1)f(\zeta_p\zeta_q)}
{f(\zeta_p)f(\zeta_q)}.
$$

The general Δ-theorem says that this alternating product is a root of
unity of odd order.

*[Animation: Start with two cards, labeled by the subsets $\varnothing$
and $\{3\}$, with numerator and denominator positions. For two distinct
primes, expand to a square labeled $\varnothing$, $\{p\}$, $\{q\}$,
$\{p,q\}$. Put the even subsets on one diagonal and the odd subsets on
the other. Show multiplication adding their phases and division subtracting
them. This is a ratio of ratios; it is not the sum of the four complex
evaluation vectors. Repeated powers of one prime do not add new subset
directions.]*

## 3. Why should this be true?

The main idea is to apply **Kronecker's theorem**: an algebraic integer
whose algebraic conjugates all have absolute value one is a root of unity.

For $\Delta(f)$, our norm identity tells us that all its algebraic
conjugates lie on the unit circle. An arithmetic comparison of the
evaluations also shows that $\Delta(f)$ is an algebraic integer.
Kronecker's theorem therefore tells us that $\Delta(f)$ is a root of unity.

*[Animation: Keep the ratio $f(1)/f(\omega)$ visible beside the unit
circle. Display the two conditions “algebraic integer” and “every
conjugate has modulus 1,” then use an arrow labeled “Kronecker's theorem”
to reveal the conclusion “root of unity.”]*

A further congruence argument, using the odd primes dividing $u$, shows
that this root of unity has odd order.

For our nine-position example, the full argument leaves just three
possibilities:

$$
\boxed{\Delta(f)\in\{1,\omega,\omega^2\}.}
$$


*[Animation: Follow the Kronecker conclusion with a separate step labeled
“Congruences force odd order.” Then return to the unit circle and reveal
the three allowed directions for $u=3$. Keep the arrows on the radius-three
circle separate from the quotient on the unit circle.]*

## 4. Why this matters

Return to the Hadamard problem. In Node 3, we constructed three polynomials
satisfying

$$
c(P)c^*(P)=d(P)d^*(P)=g(P)g^*(P)=u^2.
$$

The Δ-theorem applies to all three, because its assumptions are exactly
what these norm identities give us. Thus

$$
\Delta(c),\qquad\Delta(d),\qquad\Delta(g)
$$

are roots of unity of odd order.

*[Animation: Return to the main proof map. Carry the three labels
$\Delta(c),\Delta(d),\Delta(g)$ along the arrow from Node 4 to Node 6.
The branch through Node 5 brings a different input: the congruences coming
from the common signs. Let the two inputs meet without revealing Node 6's
conclusion yet.]*
