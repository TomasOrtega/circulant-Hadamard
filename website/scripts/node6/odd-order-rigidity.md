# Node 6 — Odd-Order Rigidity

## Video 6: Three Points, One Rotation

## Slide 1 — Our goal

We have cooked up three polynomials $c(P),d(P),g(P)$. In our guiding case
$u=3$, each satisfies the norm identity

$$
f(P)f^*(P)=9\qquad(f=c,d,g).
$$

So their values at $P=1$ and $P=\omega=e^{2\pi i/3}$ lie on the circle
of radius three. Our goal is to show that all three values undergo the
same rotation when we change the input from $1$ to $\omega$.

*[Animation: Draw two circles of radius $3$, labeled “$P=1$” and
“$P=\omega$.” Label the three values on each circle. Preview one rigid
rotation carrying the left triple to the right triple, keeping the
relative angles fixed. For a schematic, use $c(1)=3$, $d(1)=-3$,
$g(1)=3i$, and rotate by $120^\circ$. Label it “illustration”: no
circulant Hadamard matrix of order $36$ exists.]*

## Slide 2 — Compare the phase changes

Recall that

$$
\Delta(f)=\frac{f(1)}{f(\omega)}.
$$

The Δ-theorem tells us that $\Delta(c),\Delta(d),\Delta(g)$ are roots
of unity of odd order. Use $c(P)$ as the reference and form

$$
R=\frac{\Delta(d)}{\Delta(c)},\qquad
W=\frac{\Delta(g)}{\Delta(c)}.
$$

These compare the phase changes of $d(P)$ and $g(P)$ with that of $c(P)$.
They are also roots of unity of odd order. In this example, the only
possibilities are $1,\omega,\omega^2$. We will show that both comparisons
must be exactly $1$.

*[Animation: Keep the two evaluation circles visible. On a smaller unit
circle, show the three candidate positions for $R$ and $W$. This circle
represents comparisons of phase changes, not the original radius-three
values. Highlight the target $R=W=1$.]*

## Slide 3 — Use the common signs

Node 5 gave us more than norm identities. Because the three polynomials
come from the same signs,

$$
2\mid d(P)-c(P),\qquad 1+i\mid g(P)-c(P).
$$

Since $1+i$ also divides $2$, both differences vanish modulo $1+i$.
We want ratios, so first check that their denominators stay invertible.
At either evaluation $P=1$ or $P=\omega$, the norm identity gives

$$
\frac1{c(P)}=\frac{\overline{c(P)}}9.
$$

We may invert the odd number nine before reducing modulo $1+i$; its
residue is $1$. The same inverse formula applies to $d(P)$ and $g(P)$
at these two inputs.
Thus the evaluated values remain units, and we can divide to obtain

$$
\frac{d(P)}{c(P)}\equiv1,\qquad
\frac{g(P)}{c(P)}\equiv1\pmod{1+i}.
$$

Now write the comparisons as

$$
R=\frac{d(1)/c(1)}{d(\omega)/c(\omega)},\qquad
W=\frac{g(1)/c(1)}{g(\omega)/c(\omega)}.
$$

Every ratio has residue $1$, so $R\equiv W\equiv1\pmod{1+i}$.

*[Animation: Show the sign divisibilities, then the inverse formula and
an “invertible” label on each denominator. Reduce the four ratios to $1$
in a separate algebra panel. Keep the circle points stationary: congruence
is an arithmetic condition, not a small angle or distance.]*

## Slide 4 — Odd order forces exact equality

Here is where the two pieces of information meet: $R$ and $W$ have odd
order, and each reduces to $1$ in characteristic two.

For example, could $R$ be $\omega$? We know that

$$
1+\omega+\omega^2=0.
$$

If $\omega$ reduced to $1$, this would give $1+1+1=0$. But modulo $1+i$,
two ones cancel, leaving $1=0$. That is a contradiction. The same
three-term sum rules out $\omega^2$.

The same argument works for any nontrivial root of odd order: its
vanishing geometric sum would become an odd number of ones. Therefore

$$
\boxed{R=W=1.}
$$

*[Animation: Combine the labels “odd order” and “residue 1.” Use the
three-term sum to rule out $\omega$ and $\omega^2$ on the comparison
circle, leaving only $1$. Keep the original three polynomial values
separate; it is their comparison of phase changes that becomes trivial.]*

## Slide 5 — All three points rotate together

Unpacking $R=W=1$ gives

$$
\frac{d(1)}{c(1)}=\frac{d(\omega)}{c(\omega)},\qquad
\frac{g(1)}{c(1)}=\frac{g(\omega)}{c(\omega)}.
$$

Each relative position is preserved when we change the input. The ratios
$d(P)/c(P)$ and $g(P)/c(P)$ need not equal each other: each keeps its own
value at the two inputs.

Let

$$
\lambda=\frac{c(\omega)}{c(1)}.
$$

Its absolute value is one. The two equalities say that this same factor
carries all three values from the left circle to the right:

$$
\begin{aligned}
c(\omega)&=\lambda c(1),\\
d(\omega)&=\lambda d(1),\\
g(\omega)&=\lambda g(1).
\end{aligned}
$$

This is one common rotation. The angles between the three points stay fixed.

*[Animation: Rotate the whole triple together. Draw an arc from $c(1)$ to
$d(1)$ and a second arc from $c(1)$ to $g(1)$; carry both arcs along unchanged.
For the schematic $\lambda=\omega$, turn counterclockwise by $120^\circ$.
Show $d(P)/c(P)=-1$ and $g(P)/c(P)=i$ at both inputs, so the two ratios
are visibly different. Label the direction $1\to\omega$ with $\lambda$;
$\Delta(c)=\lambda^{-1}$ measures the reverse rotation.]*

## Slide 6 — Why this matters for E(P)

Recall the polynomial we built in Node 5:

$$
E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
$$

It is a fixed linear combination of $c(P),d(P),g(P)$. If all three values
pick up the factor $\lambda$, so does $E(P)$:

$$
\begin{aligned}
E(\omega)
&=\frac{\lambda d(1)-\lambda c(1)}2
  +\frac{\lambda g(1)-\lambda c(1)}{1+i}\\
&=\lambda E(1).
\end{aligned}
$$

So the arrow for $E(1)$ must turn through the same angle to reach
$E(\omega)$. Dividing by the corresponding value of $c(P)$ cancels that
common rotation:

$$
\boxed{\frac{E(\omega)}{c(\omega)}=\frac{E(1)}{c(1)}.}
$$

Now recall the other description of $E(P)$: its coefficients reduce to those
of $J(P)=1+P+\cdots+P^8$. Evaluating gives

$$
E(1)\equiv1,\qquad E(\omega)\equiv0\pmod{1+i}.
$$

Here is the conflict in the picture. The common rotation requires
$E(\omega)=\lambda E(1)$, while the all-ones condition requires a nonzero
residue at $1$ and a zero residue at $\omega$. But $\lambda$ is a root of
unity, so it stays invertible modulo $1+i$: multiplying by it cannot turn
a nonzero residue into zero.

Node 7 will write this contradiction algebraically and explain what
replaces the two-circle picture in the general case.

*[Animation: Add the arrow for $E(1)$ to the first diagram and carry it
through the same rotation to $E(\omega)$; it need not lie on the
radius-three circle. Factor $\lambda$ out of the expression above, then
cancel it in $E(\omega)/c(\omega)$. Alongside the schematic, show a panel
labeled “Required by $E(P)\equiv J(P)\pmod{1+i}$,” with residues $1$ and
$0$. Mark the conflict: an invertible multiplier cannot send $1$ to $0$.
These are arithmetic requirements, not residues calculated from the
schematic arrows; do not depict zero residue as an angle or a zero-length
complex arrow.]*

For general odd $u>1$, the same argument still gives $R=W=1$.
With several distinct prime divisors, these are equalities between
alternating products. The two-circle rotation picture describes our
$u=3$ example; the deeper nodes develop the general product argument.

Source and production references: Steven's [supplied notes](reference/supplied-outline.md),
the [two-circle storyboard](storyboards/common-rotation.svg), and
[the paper, Section 4, equations (4.2)–(4.10), using Lemma 3.3(ii)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
