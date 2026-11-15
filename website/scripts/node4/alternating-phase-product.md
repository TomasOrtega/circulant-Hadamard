# Video 4.2 — The Alternating Phase Product

Goal: define $\Delta(f)$ and prove that it and all its algebraic conjugates
have magnitude one.

## Slide 1 — Start with one prime

Assume $f(P)f^*(P)=u^2$ for odd $u>1$. When $u=3$, the comparison is

$$
\Delta(f)=\frac{f(1)}{f(\omega)},
\qquad \omega=e^{2\pi i/3}.
$$

Both values have magnitude three, so the quotient has magnitude one.
For general $u$, we need a comparison that includes each distinct prime
dividing $u$.

*[Animation: Recall the two output arrows from Video 4.1. Place $f(1)$
above a fraction bar and $f(\omega)$ below. Cancel their magnitude labels
$3/3$ while retaining the angle from $f(\omega)$ to $f(1)$.]*

## Slide 2 — Even subsets above, odd subsets below

Let $I$ be the set of distinct primes dividing $u$. Choose a primitive
$p$th root $\zeta_p$ for each $p\in I$, and put

$$
\zeta_S=\prod_{p\in S}\zeta_p,\qquad \zeta_\varnothing=1.
$$

For each subset $S$, evaluate $f(P)$ at $\zeta_S$. Even-sized subsets
contribute to the numerator and odd-sized subsets to the denominator:

$$
\Delta(f)=\prod_{S\subseteq I}f(\zeta_S)^{(-1)^{|S|}}.
$$

With two distinct primes $p,q$, this says simply

$$
\Delta(f)=\frac{f(1)f(\zeta_p\zeta_q)}
{f(\zeta_p)f(\zeta_q)}.
$$

*[Animation: Make four cards labeled $\varnothing,\{p\},\{q\},\{p,q\}$,
each with its evaluation. Move the two even-subset cards above a fraction
bar and the two odd-subset cards below. Keep the explicit four-factor
formula beside the compact product notation.]*

## Slide 3 — Pair the magnitudes

Fix one prime, say $p$. Adding or removing it pairs every even subset
with an odd subset. Thus the numerator and denominator contain equally
many factors. Each factor has magnitude $u$, so

$$
|\Delta(f)|=1.
$$

All the divisions are legitimate: the norm identity made every evaluated
value nonzero.

*[Animation: Join each subset card to the card obtained by toggling $p$.
Attach a magnitude label $u$ to every card. Cancel one numerator label
against one denominator label along each pair, leaving magnitude $1$.]*

## Slide 4 — Every conjugate obeys the same equation

An algebraic conjugate replaces our roots of unity by other roots while
preserving their algebraic equations. Call this replacement $\sigma$.
It commutes with complex conjugation, so the norm equation becomes

$$
\sigma(f(\zeta_S))\overline{\sigma(f(\zeta_S))}=u^2.
$$

Every transformed factor still has magnitude $u$. The same even–odd
pairing gives $|\sigma(\Delta(f))|=1$.

This supplies the circle condition for Kronecker's theorem. We must still
show that $\Delta(f)$ is an algebraic integer; being a quotient does not
give that automatically.

*[Animation: Replace each root label by its image under $\sigma$ without
moving the subset cards. Their output arrows may change direction, but
their radius labels stay $u$. Repeat the magnitude cancellation and end
with two requirements: “all conjugates on the unit circle” checked, and
“algebraic integer” carried forward to the next steps.]*

Website exposition: [The Alternating Phase Product](../../nodes/alternating-phase-product.md).
