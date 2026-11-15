# Video 4.5 — Why Kronecker's Theorem Gives a Root of Unity

Goal: explain why integrality and unit magnitude for every conjugate force
some positive power to equal one.

## Slide 1 — Two hypotheses meet

We have proved that $\Delta(f)$ is an algebraic integer and that all
its algebraic conjugates have magnitude one. Kronecker's theorem says
that it must therefore be a root of unity.

Let us see why. Write $z$ for an algebraic integer with these two
properties, and let $d$ be its degree over $\mathbb Q$.
An algebraic integer satisfies a monic polynomial with integer coefficients.
That integer condition will make the possible powers a finite set.

*[Animation: Bring two result cards together: “algebraic integer” and
“all conjugates on the unit circle.” Show the powers $z,z^2,z^3,\ldots$
on a circle without yet making them repeat. Display a monic polynomial
with integer coefficient boxes alongside them.]*

## Slide 2 — Bound the coefficients

Every power $z^m$ is still an algebraic integer. Its degree is at most
$d$, and its conjugates still have magnitude one.

Its monic minimal polynomial has integer coefficients. A coefficient
$k$ places below the leading term is, up to sign, a sum of products
of $k$ distinct roots. There are at most $\binom{d}{k}$ terms, each
of magnitude one, so

$$
|\text{coefficient}|\leq\binom{d}{k}.
$$

The bound does not depend on the power $m$.

*[Animation: For three illustrative roots $\alpha,\beta,\gamma$, expand
$(X-\alpha)(X-\beta)(X-\gamma)$. Highlight the three terms in
$\alpha+\beta+\gamma$ and in $\alpha\beta+\alpha\gamma+\beta\gamma$.
Use the triangle inequality to show bounds $3,3,1$, then replace them
by the general binomial bounds.]*

## Slide 3 — Finitely many polynomials, finitely many powers

The degree is bounded, and each coefficient is an integer in a bounded
range. Only finitely many such polynomials exist. Each has only finitely
many roots, so the powers of $z$ belong to a finite set.

Two powers must agree: $z^a=z^b$ for some $a<b$. Since $z$ is nonzero,

$$
\boxed{z^{b-a}=1.}
$$

That is exactly what it means to be a root of unity.

*[Animation: Replace each bounded coefficient box by its finite list of
integer choices. Show finitely many polynomial cards, then their finite
collection of roots. Feed the powers into these slots until a slot is
reused. Cancel $z^a$ from $z^a=z^b$ and display the boxed conclusion.]*

## Slide 4 — Apply it to our product

Take $z=\Delta(f)$. The two preceding results verify both hypotheses,
so $\Delta(f)$ has finite order.

We have not yet determined whether that order is odd. The next node
uses the residue-one information from the local comparisons to show
that only odd orders remain.

*[Animation: Replace $z$ by $\Delta(f)$ in the conclusion. Close a finite
orbit on the unit circle, with its length labeled “some positive order.”
Bring back the residue-one card from Video 4.4 and highlight Node 4.6.]*

Website exposition: [Kronecker's Theorem](../../nodes/kronecker-step.md).
