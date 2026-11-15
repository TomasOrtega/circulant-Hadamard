# Node 5 — Signs Become All Ones

## Video 5: Cooking Up the All-Ones Polynomial

## Slide 1 — Our goal

We have three polynomials $c(P)$, $d(P)$, and $g(P)$, all built from the
same four sign polynomials $H_0(P),H_1(P),H_2(P),H_3(P)$.

Let us use that common origin to build a new polynomial $E(P)$ whose
coefficients all become one modulo $1+i$.

In our guiding case $u=3$, the goal is

$$
E(P)\equiv1+P+\cdots+P^8\pmod{1+i}.
$$

We will call the polynomial on the right $J(P)$, the all-ones polynomial.

*[Animation: Show the four polynomials $H_0(P),\ldots,H_3(P)$ with the
label “coefficients $\pm1$,” then recall $c(P),d(P),g(P)$ beneath them.
Reveal the target congruence, with the nine coefficients of $J(P)$ each
labeled $1$. Keep this as polynomial notation; no sign grid is needed.]*

## Slide 2 — Why this combination?

We want $E(P)$ to connect two parts of the proof. Expressing it through
$c(P),d(P),g(P)$ lets us use the comparisons between those polynomials
later. Expressing it through the $H_a(P)$ will reveal its coefficients
modulo $1+i$.

The combination we choose is

$$
\boxed{E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.}
$$

Let us see why adding them gives the all-ones congruence.

*[Animation: Build the two differences $d(P)-c(P)$ and $g(P)-c(P)$,
then display their denominators and add the terms to define $E(P)$.
Recall the formulas for $c,d,g$ from Node 3 as the substitution begins.
Carry the expression in $c,d,g$ forward as a small reference on the next
slide.]*

## Slide 3 — Write E(P) in terms of the H's

Substituting the definitions of $c(P),d(P),g(P)$ cancels the $H_0(P)$
terms and gives

$$
\frac{d(P)-c(P)}2=-\frac{H_1(P)+H_3(P)}2,
$$

and

$$
\begin{aligned}
\frac{g(P)-c(P)}{1+i}
&=-\frac{H_2(P)+H_3(P)}2\\
&\quad+i\frac{H_1(P)+H_2(P)}2.
\end{aligned}
$$

Every half-sum here has integer coefficients: adding two signs always
gives an even number. Now add the two expressions and collect terms:

$$
\boxed{E(P)=-H_3(P)+(i-1)\frac{H_1(P)+H_2(P)}2.}
$$

This is the useful feature of our definition. Everything involving
$H_1(P)$ and $H_2(P)$ has collected into the second term, while the two
halves of $-H_3(P)$ combine into a whole sign polynomial.

*[Animation: Reveal the two quotient formulas in succession. Highlight
the paired sign polynomials in each numerator to justify division by two.
Then combine the two $-H_3(P)/2$ terms and collect the remaining terms
under the factor $i-1$. End with just the boxed identity.]*

## Slide 4 — Reduce the coefficients

Now reduce modulo $1+i$. Since

$$
i-1=i(1+i),
$$

the entire second term disappears, leaving $-H_3(P)$.

Every coefficient of this polynomial is $+1$ or $-1$. These signs become
the same modulo $1+i$, because their difference is

$$
2=(1+i)(1-i).
$$

Thus every coefficient becomes one. In our nine-position example,

$$
\boxed{E(P)\equiv J(P)=1+P+\cdots+P^8\pmod{1+i}.}
$$

*[Animation: In the expanded expression for $E(P)$, replace $i-1$ with
$i(1+i)$ and fade that whole term under the label “modulo $1+i$.”
Expand the remaining sign polynomial as $\pm1\pm P\pm\cdots\pm P^8$.
Replace each coefficient by $1$, keeping the powers of $P$ fixed.]*

## Slide 5 — Evaluate at one

Finally, substitute $P=1$. Each of the nine terms in $J(P)$ becomes one,
so

$$
E(1)\equiv J(1)=9\equiv1\pmod{1+i}.
$$

The same calculation works for general odd $u$: there are $u^2$ terms
in $J(P)$, so

$$
E(1)\equiv J(1)=u^2\equiv1\pmod{1+i}.
$$

*[Animation: Replace each power of $P$ in the nine-term sum by $1$.
Pair eight of the ones; each pair is $2$, which vanishes modulo $1+i$.
Leave one unpaired $1$. Then replace “nine terms” by “$u^2$ terms, odd”
and finish with $E(1)\equiv1\pmod{1+i}$ on screen.]*

In particular, $E(1)\equiv1\pmod{1+i}$, because $u$ is odd and there
is an odd number of terms.
