# Video 4.6 — Why the Order Is Odd

Goal: use residue one to restrict the order of the root of unity
$\Delta(f)$.

## Slide 1 — Keep the part of the order away from p

We know that $\Delta(f)$ is a root of unity and has residue one at each
prime above a divisor $p$ of $u$.

Here is the general fact we need. Work in a local domain whose residue
field has characteristic $p$, and suppose a root of unity $\xi$ has
residue one. Write its order as $p^a m$, with
$p$ not dividing $m$. Then

$$
\eta=\xi^{p^a}
$$

has order $m$ and still has residue one. We will show that $m=1$.

*[Animation: Split the order label into a $p$-power part and a part
coprime to $p$. Raise the root to $p^a$ and remove the $p$-power part
from the order. Carry the residue-$1$ label to the resulting root $\eta$.]*

## Slide 2 — A geometric sum gives the restriction

Suppose $m>1$. Then $\eta\ne1$, and the geometric-sum identity gives

$$
1+\eta+\cdots+\eta^{m-1}=0.
$$

Reduce this equality. Every term becomes one, so it says $m=0$ in
characteristic $p$. That is impossible because $p$ does not divide $m$.
Thus $m=1$: the original root has $p$-power order.

*[Animation: First show the exact geometric sum as a closed polygon
of arrows. Then move its algebraic formula into a separate reduction
panel and replace every term by $1$. Count $m$ ones and mark that the
count is not divisible by $p$. Keep the complex polygon distinct from
the residue calculation.]*

## Slide 3 — Apply the restriction at each prime

For every $p\mid u$, the local comparison puts $\Delta(f)$ in exactly
this situation. Its order must be a power of every prime dividing $u$.
All those primes are odd, so its order is odd.

If $u$ has two distinct prime divisors, the order is a power of both.
The only possibility is one, so in that case $\Delta(f)=1$.
The one-prime case can have a nontrivial rotation.

*[Animation: Put a “power of $p$” restriction beside the order. For a
second prime $q$, add “power of $q$” and intersect the two lists, leaving
only $1$. Return to the general conclusion “odd order,” which also
includes the one-prime case.]*

## Slide 4 — The three directions when u=3

For $u=3$, the quotient lies in $\mathbb Q(i,\omega)$ and has
$3$-power order. This field has degree four over $\mathbb Q$.
A primitive ninth root has degree six, so it cannot lie in this field;
higher $3$-power orders are excluded for the same reason. Therefore

$$
\boxed{\Delta(f)\in\{1,\omega,\omega^2\}.}
$$

The example $f(P)=3iP$ gives $\Delta(f)=\omega^2$, so the phase need
not be zero. Applying the theorem to $c(P),d(P),g(P)$ gives three
odd-order phases. Node 6 will use their common sign origin to compare them.

*[Animation: Mark $1,\omega,\omega^2$ on the unit circle. Briefly show
the incompatible degree labels $6$ and $4$ to exclude primitive ninth
roots. For $f(P)=3iP$, display $f(1)=3i$ and $f(\omega)=3i\omega$,
then cancel to obtain $\omega^2$. End with the three labels
$\Delta(c),\Delta(d),\Delta(g)$ and the connection to Node 6.]*

Website exposition: [Why the Order Is Odd](../../nodes/delta-odd-order.md).
