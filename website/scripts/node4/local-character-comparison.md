# Video 4.3 — Comparing Two Evaluations at a Prime

Goal: prove the local comparison by shortening a prime-power cycle while
preserving the two ratios. The cyclotomic basis and divisibility fact used
below are the standard input from the paper's Lemma 2.1.

## Slide 1 — What needs to be proved?

Fix a prime $p$. We work near one prime above $p$, allowing denominators
that remain nonzero there. Write $A$ for this coefficient ring; it is
obtained from roots of unity whose orders are coprime to $p$.

Suppose two polynomials on a cycle of length $p^e$ satisfy

$$
F(X)K(X)=p^e b,
$$

where $b$ is invertible in $A$. For a primitive $p$th root $\rho$, we
will prove that both $F(\rho)/F(1)$ and $K(\rho)/K(1)$ are units of
residue one. A unit means an element whose inverse is allowed in the
same ring.

The cyclotomic local ring $A[\rho]$ has maximal ideal $(\rho-1)$:
an element is a unit exactly when its residue is nonzero.

Although $\rho$ reduces to one, we cannot yet reduce these ratios:
the values downstairs might themselves vanish after reduction.

*[Animation: Show a cycle labeled $p^e$ and the product labeled $p^e b$.
Highlight the matching exponents. Display both ratios with a question
mark beneath each denominator. Keep reduction in a separate panel;
do not cancel two zero residues.]*

## Slide 2 — The cycle of length p

First take $e=1$. The product $F(1)K(1)=pb$ contains exactly one factor
of $p$. The exponents of $p$ in the two values are nonnegative integers,
so at least one value is a unit. Suppose it is $F(1)$.

Now reduction is safe:

$$
\frac{F(\rho)}{F(1)}\equiv1\pmod{\rho-1}.
$$

The two ratios multiply to one, because the evaluated products at
$\rho$ and at $1$ both equal $pb$. Therefore the other ratio is its
inverse and also has residue one.

*[Animation: Distribute one $p$-factor between two boxes for $F(1)$ and
$K(1)$. One box must receive none; mark it invertible. Reduce its ratio
to $1$, then use a product bracket labeled $1$ to identify the second
ratio as its inverse.]*

## Slide 3 — Find a factor we can divide

For $e\geq2$, evaluate at a primitive $p^e$th root $\xi$.
The $p$-divisibility exponents of $F(\xi)$ and $K(\xi)$ add to $e$.
These exponents can now be fractional, but both are nonnegative, so one
is at least one. Relabel the factors so that it is $F(\xi)$.

Divide the polynomial by the cyclotomic polynomial:

$$
F(X)=Q(X)\Phi_{p^e}(X)+R(X),\qquad
\deg R<(p-1)p^{e-1}.
$$

At $\xi$, only the remainder survives. The standard cyclotomic basis
fact says that divisibility of $R(\xi)$ by $p$ forces every coefficient
of this remainder to be divisible by $p$.

*[Animation: Show two nonnegative divisibility meters adding to $e$;
one reaches at least $1$. Perform polynomial division on that factor.
Evaluate at $\xi$ to erase the multiple of $\Phi_{p^e}$, then place a
$p$-factor on each remainder coefficient. Label this transfer from
value to coefficients “cyclotomic basis fact.”]*

## Slide 4 — Fold the cycle and divide once

Project onto the cycle of length $p^{e-1}$; call this projection $q$.
It imposes $X^{p^{e-1}}=1$. Thus

$$
\Phi_{p^e}(X)=1+X^{p^{e-1}}+\cdots+X^{(p-1)p^{e-1}}
\quad\longmapsto\quad p.
$$

Both parts of $q(F)$ are therefore divisible by $p$. Define

$$
F'(X)=q(F)/p,\qquad K'(X)=q(K).
$$

These still have coefficients in $A$, and their product is $p^{e-1}b$.
Both the cycle exponent and the scalar exponent have decreased by one.
This is exact division before any reduction.

*[Animation: Fold the $p^e$ positions onto $p^{e-1}$ positions, grouping
positions with the same new exponent. Turn the $p$ cyclotomic terms
into $p$ ones. Factor $p$ from the projected polynomial and divide only
that factor. Lower both exponent counters from $e$ to $e-1$.]*

## Slide 5 — The ratios do not change

Both inputs $1$ and $\rho$ respect the shorter cycle relation. Projection
therefore changes neither evaluation, and dividing by $p$ cancels from
the numerator and denominator:

$$
\frac{F'(\rho)}{F'(1)}=\frac{F(\rho)/p}{F(1)/p}
=\frac{F(\rho)}{F(1)}.
$$

The ratio for $K(X)$ is unchanged too. Repeat this shortening until the
cycle has length $p$. The base case then proves that both original ratios
are units of residue one. At different steps we may divide different factors.

*[Animation: Keep the two ratio cards fixed while the cycle and scalar
exponents descend together. At each step cancel the two scalar $p$'s
inside the affected ratio. Stop at exponent $1$ and bring back the
two unit/residue-$1$ labels from Slide 2.]*

## Slide 6 — Apply the comparison to f(P)

For our norm solution $f(P)f^*(P)=u^2$, the $p$-component has order
$p^e$ with exactly the same exponent of $p$ as $u^2$. Evaluate all the
other prime components first. The two resulting factors satisfy precisely
the identity we have just studied.

For any subset $S$ not containing $p$, we conclude that

$$
\frac{f(\zeta_{S\cup\{p\}})}{f(\zeta_S)}
\equiv1
$$

as a unit at each prime above $p$. Its inverse has the same property.
These are the comparisons that let us remove the denominator obstruction
from the alternating product.

*[Animation: Return to the subset cards from Video 4.2. Highlight a pair
$S,S\cup\{p\}$ and label its ratio “unit, residue $1$ above $p$.” Repeat
along that prime direction. Keep the label attached to the ratio, not
to either individual value.]*

Website exposition: [Local Character Comparison](../../nodes/local-character-comparison.md).
