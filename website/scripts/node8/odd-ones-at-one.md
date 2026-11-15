# Video 8.2 — An Odd Number of Ones at One

## Slide 1 — Count the ones

Our goal is the evaluation at $P=1$, including its denominator.
For odd $u>1$, the all-ones polynomial has $u^2$ terms:

$$
J(P)=1+P+\cdots+P^{u^2-1}.
$$

Substituting $P=1$ makes every term one, so $J(1)=u^2$.
For $u=3$, that is nine ones. In characteristic two, pairs of ones
cancel and an odd number leaves one. Thus $J(1)\equiv1\pmod{1+i}$.

*[Animation: Replace every power of $P$ by $1$. In the nine-term
example, count the ones before moving to a separate residue panel.
Pair eight of them there and leave one, using
$2=(1+i)(1-i)\equiv0$.]*

## Slide 2 — Evaluate the denominator too

Our sum contains $J(1)/c(1)$. The polynomial $c(P)$ has real integer
coefficients and satisfies

$$
c(P)c^*(P)=u^2.
$$

At $P=1$, reversing powers changes nothing, and conjugating real
coefficients changes nothing. Hence $c^*(1)=c(1)$, giving

$$
c(1)^2=u^2,\qquad \boxed{c(1)=\pm u.}
$$

The real-coefficient condition matters: the norm identity here fixes
$c(1)$ to these two real values.

*[Animation: Substitute $P=1$ into both polynomial factors. Show the
reversed powers becoming ones, merge $c^*(1)$ with $c(1)$, and display
the two real possibilities $u$ and $-u$.]*

## Slide 3 — The quotient still has residue one

In the evaluation ring with $1/u$ adjoined, $c(1)=\pm u$ is a unit.
Therefore

$$
\frac{J(1)}{c(1)}=\frac{u^2}{\pm u}=\pm u
\equiv1\pmod{1+i}.
$$

The last step uses oddness of $u$ and the equality of plus and minus
in characteristic two. For $u=3$, the exact quotient is $9/(\pm3)=\pm3$.
Either sign reduces to one. This is the contribution of the empty
subset to our alternating sum.

*[Animation: Keep the denominator visible while simplifying
$u^2/(\pm u)$ to $\pm u$. Show both signs passing to residue $1$,
then place that value on the empty-subset card labelled $P=1$.]*

Detailed exposition: [Node 8.2](../../nodes/odd-ones-at-one.md).
Source: the paper, equation (4.2) and the final evaluation after (4.11).
