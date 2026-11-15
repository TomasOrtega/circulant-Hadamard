# Video 3 — The Three Evaluations

## Slide 1 — Our guiding example

Now that we know a circulant Hadamard matrix of size larger than one must
have order $4u^2$, where $u$ is odd, let us specialize to $u=3$.

This gives order $36$, the first candidate beyond our known order-four
example. Suppose, for the moment, that a circulant Hadamard matrix of order
$36$ exists. We will see what its polynomial would have to look like.

Our starting equation is

$$
h(X)h^*(X)=36
\quad\text{in }\mathbb Z[X]/(X^{36}-1).
$$

*[Animation: Bring back the order restriction, set $u=3$, and display 36
coefficient positions. Label the matrix and its sign row “hypothetical.”]*

## Slide 2 — One cycle, two coordinates

We begin with the Chinese remainder theorem to rewrite our group-ring
polynomial using two variables. Since $4$ and $9$ are coprime,

$$
C_{36}\cong C_4\times C_9.
$$

Instead of one exponent taken modulo $36$, we use two: one taken modulo
$4$, and one modulo $9$. In the group ring, we write $Z$ for the $C_4$
coordinate and $P$ for the $C_9$ coordinate, so we work in

$$
\mathbb Z[Z,P]/(Z^4-1,P^9-1).
$$

*[Animation: Show $X\mapsto ZP$, so $X^j\mapsto Z^jP^j$. Move the
coefficient at position $j$ into the grid cell $(j\bmod4,j\bmod9)$.
Label the four rows $1,Z,Z^2,Z^3$ and the nine columns $1,P,\ldots,P^8$.
This grid organizes the same 36 coefficients by their two exponents;
its rows are not rows of the Hadamard matrix or consecutive blocks
of the original coefficient list.]*

Our polynomial is now $h(Z,P)$, and the Hadamard identity becomes

$$
h(Z,P)h^*(Z,P)=36.
$$

## Slide 3 — Collect the powers of Z

Let us group the terms according to their power of $Z$. This gives four
degree-eight polynomials $H_0(P),H_1(P),H_2(P),H_3(P)$, with

$$
h(Z,P)=H_0(P)+ZH_1(P)+Z^2H_2(P)+Z^3H_3(P).
$$

Each $H_a(P)$ collects the nine coefficients with the same power of $Z$.
All of these coefficients are still $+1$ or $-1$.

This lets us work with the four-position part of the problem while leaving
the nine-position part in place.

*[Animation: Highlight the coefficients beside each $Z$-power label.
Attach the column powers $1,P,\ldots,P^8$ to those nine coefficients
to form $H_0(P),H_1(P),H_2(P),H_3(P)$ in turn. Then assemble the
four terms $H_0(P),ZH_1(P),Z^2H_2(P),Z^3H_3(P)$ into $h(Z,P)$.]*

## Slide 4 — Three useful substitutions

Since our group ring has the relation $Z^4=1$, the natural values to
substitute for $Z$ are the fourth roots of unity: $1$, $-1$, $i$, and $-i$.
Let us use the first three.

At $1$, all four parts add. At $-1$, their signs alternate. At $i$, the even
powers give the real part and the odd powers give the imaginary part.

We want to remove the factor of $4$ from $36=4\cdot9$ in the product
identity. Dividing a polynomial by $2$ also divides its star by $2$,
so their product is divided by $4$. This will turn $36$ into $9$.

With that in mind, divide each evaluation by $2$ and call the three
polynomials

$$
\begin{aligned}
c(P)&=\frac{h(1,P)}2
=\frac{H_0(P)+H_1(P)+H_2(P)+H_3(P)}2,\\
d(P)&=\frac{h(-1,P)}2
=\frac{H_0(P)-H_1(P)+H_2(P)-H_3(P)}2,\\
g(P)&=\frac{h(i,P)}2
=\frac{H_0(P)-H_2(P)}2
+i\frac{H_1(P)-H_3(P)}2.
\end{aligned}
$$

The fourth possibility, $Z=-i$, just conjugates the coefficients of the
$i$ evaluation, so it does not give us another independent polynomial.

These substitutions preserve the product identity. For the complex
coefficients, star reverses the powers of $P$ and conjugates the coefficients.
Each evaluated polynomial times its star is still $36$, so

$$
c(P)c^*(P)
=\frac{h(1,P)}2\frac{h^*(1,P)}2
=\frac{36}{4}
=9.
$$

The same calculation works for $d(P)$ and $g(P)$. We have removed the
factor of $4$, giving

$$
c(P)c^*(P)=d(P)d^*(P)=g(P)g^*(P)=9.
$$

*[Animation: Highlight $Z^4=1$ and reveal its four roots. Keep the four
terms of $h(Z,P)$ visible. Substitute $Z=1$, then $Z=-1$, then $Z=i$,
revealing the weights $(1,1,1,1)$, $(1,-1,1,-1)$, and $(1,i,-1,-i)$.
Introduce $c(P),d(P),g(P)$ one at a time with their division by $2$.
Then focus on the product $c(P)c^*(P)$: show a denominator of $2$
under each factor, combine them into $4$, and simplify $36/4$ to $9$.
Finish with all three norm-nine identities together.]*

## Slide 5 — Why division by 2 is allowed

We should check that this has not introduced fractional coefficients.

For each power of $P$, the coefficient of $c$ or $d$ is half a sum of four
signs. Such a sum is even. For $g$, each numerator is a difference of two
signs, so its real and imaginary coefficients are integers too.

So $c(P)$ and $d(P)$ have integer coefficients, and $g(P)$ has
Gaussian-integer coefficients.

*[Animation: Fix one power $P^b$ and highlight its coefficient in each
of $H_0(P),H_1(P),H_2(P),H_3(P)$. Show their four-sign sums for $c$
and $d$, then the two differences for the real and imaginary parts
of $g$. Mark each numerator even before dividing it by $2$.]*

## Slide 6 — From polynomials to points on a circle

So what have we gained? Starting from our hypothetical Hadamard matrix,
we have cooked up three polynomials with the same norm identity. That
identity gives us a geometric picture.

Choose any ninth root of unity $\zeta$, so $\zeta^9=1$, and substitute
$P=\zeta$. Star becomes complex conjugation. For $c$, this gives

$$
c(\zeta)\overline{c(\zeta)}=|c(\zeta)|^2=9,
$$

so $|c(\zeta)|=3$. The same is true for $d$ and $g$.

Thus, whenever we evaluate these polynomials at a ninth root of unity,
their values lie on the circle of radius $3$ centered at the origin.
The construction works for general odd $u$ too: the norm identity becomes
$u^2$, and evaluation at a $u^2$-th root of unity puts the values on a
circle of radius $u$.

For our example, we will focus on two inputs: $P=1$ and
$P=\omega$, where $\omega=e^{2\pi i/3}$. Both satisfy $P^9=1$.

The norm tells us how far each value is from the origin. Next we want
to compare their phases: the angles of the arrows from the origin.
How much does each arrow rotate when we change the input from $1$ to $\omega$?

Here is a preview of where we are heading. Using more of the information
inherited from our original signs, we will show in Node 6 that this phase
change is the same for all three polynomials. One common rotation carries
$c(1)$ to $c(\omega)$, $d(1)$ to $d(\omega)$, and $g(1)$ to $g(\omega)$.

*[Animation: Draw a complex plane and a circle of radius $3$. Transform
the norm identity into $|c(\zeta)|^2=9$, then $|c(\zeta)|=3$, and
place a point labeled $c(\zeta)$ on the circle. Add $d(\zeta)$ and
$g(\zeta)$, each with an arrow from the origin. Label these as output
values; the inputs satisfy $\zeta^9=1$ and are not arbitrary points
of the unit circle. Briefly show the general radius $u$, then return to $3$.
Next show two radius-three circles labeled “$P=1$” and “$P=\omega$.”
Highlight the angular change for each corresponding pair of arrows.
For the closing preview, label the scene “Coming in Node 6: one common
rotation.” Use the schematic starting positions $c(1)=3$, $d(1)=-3$,
$g(1)=3i$, and rotate all three together by $120^\circ$ to illustrate
the future conclusion. Keep each label attached to its point; the three
points need not coincide. Mark the positions as schematic, not values
from an actual order-$36$ Hadamard matrix.]*

Source: [the paper, Section 4, equations (4.1)–(4.2)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
