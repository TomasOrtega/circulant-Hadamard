# Video 7.3 — Cancel Before Reducing

## Slide 1 — Subtract the equal products

Our goal is to retain the linear information in the equal products.
Work in the domain $A=\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]$,
where $u>1$ is odd. The subsets of its distinct prime divisors index
our factors. Each exact divided difference $x_S$ belongs to $A$,
as established by coefficientwise division in Node 7.2. For either
family, Node 7.1 gives

$$
\prod_{|S|\text{ even}}(1+t x_S)
=\prod_{|S|\text{ odd}}(1+t x_S).
$$

Node 7.2 gives an exact expansion on each side. Subtracting cancels
the two constant terms and leaves

$$
tL+t^2Q=0,\qquad
L=\sum_S(-1)^{|S|}x_S,
$$

where $Q\in A$ is the difference of the two remainders.

*[Animation: Stack the expanded products, subtract the lower row,
and strike out the two constant terms. Gather the linear terms into
$tL$ and the remaining terms into $t^2Q$.]*

## Slide 2 — Cancel in characteristic zero

For the $r_S$ family, $t=2$. For the $w_S$ family, $t=1+i$.
Both are nonzero in the domain $A\subseteq\mathbb C$. Therefore

$$
t(L+tQ)=0\quad\Longrightarrow\quad L=-tQ.
$$

This cancellation happens before reduction. We have not divided by
the residue of either $2$ or $1+i$.

*[Animation: Put the equation inside a panel labelled “original domain
$A$.” Factor out $t$, show $t\ne0$, and cancel it. Only after the
result $L=-tQ$ appears should a reduction arrow become available.]*

## Slide 3 — Now reduce both equations in the same ring

Reduce modulo $(1+i)A$. Since $2=(1+i)(1-i)$, both choices of $t$
have zero residue. The remainder disappears, leaving $L\equiv0$.
Writing the two families out gives

$$
\sum_S(-1)^{|S|}\frac{d_S-c_S}{2c_S}\equiv0\pmod{1+i},
$$

$$
\sum_S(-1)^{|S|}\frac{g_S-c_S}{(1+i)c_S}\equiv0\pmod{1+i}.
$$

Here $c_S=c(\zeta_S)$, with the same notation for $d_S,g_S$.
The divided differences already belonged to $A$ before reduction.

*[Animation: Pass both equations through the same reduction arrow.
Show $2\mapsto0$ and $1+i\mapsto0$, erase the remainder on each
right-hand side, and retain the two alternating sums on the left.]*

## Slide 4 — Why the order of operations matters

If we reduced the original product identity first, every factor
$1+t x_S$ would become $1$. We would see only $1=1$ and lose the
linear information. Canceling the nonzero factor first preserves it.

For $u=3$, each product had one factor, so $Q=0$ and these sums are
zero exactly. For general $u$, the two congruences are enough. The
next step adds them in the same quotient ring.

*[Animation: Show a short side path where early reduction turns both
products into $1=1$. Return to the successful path “expand → subtract
→ cancel in $A$ → reduce.” Place the two surviving sums side by side.]*

Detailed exposition: [Node 7.3](../../nodes/cancel-before-reduction.md).
Source: the paper, Lemma 4.1 and its application after equation (4.10).
