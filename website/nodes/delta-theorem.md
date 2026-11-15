---
id: delta-theorem
title: The Δ-Theorem
shortTitle: The Δ-Theorem
mapTitle: 'The $\Delta$-Theorem'
summary: Equal evaluation magnitudes, local arithmetic, and Kronecker's theorem
  restrict the alternating phase product to a root of unity of odd order.
number: 4
draft: false
video:
  src: media/delta-theorem.mp4
  captions: media/delta-theorem.vtt
  duration: 238.8
mapPosition:
  - 460
  - 180
mapSummary: '$\Delta(f)$ has odd order'
graphLayout: proof-map
graphTitle: Inside Node 4 · From a Circle to Roots of Unity
children:
  - node: circle-evaluations
    dependsOn: []
    segment: { start: 15.81, end: 57.83 }
    script: |
      > **Lemma (The evaluation circle).** *If
      > $f(P)f^*(P)=u^2$ in $\mathbb Z[i][P]/(P^{u^2}-1)$, then
      > $|f(\zeta)|=u$ for every $u^2$th root $\zeta$.*

      Let $u>1$ be odd. Work in $\mathbb Z[i][P]/(P^{u^2}-1)$ and suppose

      $$
      f(P)f^*(P)=u^2.
      $$

      If $\zeta^{u^2}=1$, substitution turns star into complex conjugation:

      $$
      f(\zeta)\overline{f(\zeta)}=u^2.
      $$

      Thus every evaluation is nonzero and lies on the circle of radius $u$.
      For $u=3$, the nine root-of-unity inputs give points on the circle of
      radius $3$. Different inputs may give the same point.

      This statement allows arbitrary Gaussian-integer coefficients;
      no Hadamard sign array is assumed.
  - node: alternating-phase-product
    dependsOn:
      - circle-evaluations
    segment: { start: 103.13, end: 168.05 }
    script: |
      Let $I$ be the set of distinct primes dividing $u$. Choose a primitive
      $p$th root $\zeta_p$ for each $p\in I$, and put

      $$
      \zeta_S=\prod_{p\in S}\zeta_p,\qquad \zeta_\varnothing=1.
      $$

      Define the alternating product

      $$
      \Delta(f)=\prod_{S\subseteq I}f(\zeta_S)^{(-1)^{|S|}}.
      $$

      > **Lemma (Magnitude of the alternating product).** *If
      > $f(P)f^*(P)=u^2$, then $\Delta(f)$ and all its algebraic
      > conjugates have absolute value $1$.*

      Even-sized subsets contribute numerator factors; odd-sized subsets
      contribute denominator factors. All values have magnitude $u$, and
      there are equally many factors of each kind. Hence $|\Delta(f)|=1$.
      The same reasoning applies to every algebraic conjugate.

      For $u=3$, choose $\omega=e^{2\pi i/3}$. Then

      $$
      \Delta(f)=\frac{f(1)}{f(\omega)}.
      $$

      Its angle is $\arg f(1)-\arg f(\omega)$: the rotation from the
      denominator's direction to the numerator's direction.
  - node: local-character-comparison
    dependsOn:
      - circle-evaluations
    segment: null
    script: |
      > **Lemma (Local comparison).** Fix a prime $p\mid u$. Compare two
      > character evaluations that differ only in the $p$-component: one
      > substitutes $1$ there, and the other a primitive $p$th root.
      >
      > Write $u^2=p^e b$ with $p\nmid b$. The $p$-component has order $p^e$,
      > so its order and the scalar norm have matching powers of $p$.
      > After evaluating the other components, the lemma says that the ratio
      > of these two values is a local unit with residue $1$ at each prime
      > above $p$.

      The proof shortens the $p$-power cycle one step at a time. A
      cyclotomic divisibility calculation makes one projected factor
      divisible by $p$. Divide that factor by $p$: the cycle exponent and
      scalar exponent both drop by one, while the comparison ratios stay
      unchanged. At a cycle of length $p$, one value at $1$ is a unit,
      and reducing the ratio is justified. This proves the comparison;
      simply reducing two potentially vanishing values would not suffice.
  - node: integral-delta
    dependsOn:
      - alternating-phase-product
      - local-character-comparison
    segment: { start: 188.5, end: 193.76 }
    script: |
      > **Lemma (Integrality).** *The alternating product $\Delta(f)$
      > is an algebraic integer. Above each prime dividing $u$, it is
      > a unit with residue $1$.*

      For each $p\in I$, pair the subset $S$ with $S\cup\{p\}$:

      $$
      \Delta(f)=\prod_{S\subseteq I\setminus\{p\}}
      \left(\frac{f(\zeta_S)}{f(\zeta_{S\cup\{p\}})}\right)^{(-1)^{|S|}}.
      $$

      Every paired ratio is a local unit with residue $1$ at primes above
      $p$. Changing the pairing direction leaves the same $\Delta(f)$,
      so this controls every prime dividing $u$.

      At the remaining primes, $u^2$ is a unit. The norm equation then
      makes every evaluated factor a unit. Together these statements show
      that $\Delta(f)$ lies in every localization of the cyclotomic
      coefficient ring, hence in that ring itself.

      In particular, $\Delta(f)$ is an algebraic integer. This supplies the
      missing hypothesis that a point on the unit circle need not satisfy.
  - node: kronecker-step
    dependsOn:
      - alternating-phase-product
      - integral-delta
    segment: { start: 168.05, end: 197.79 }
    script: |
      > **Kronecker's theorem.** *An algebraic integer all of whose
      > conjugates have absolute value $1$ is a root of unity.*

      We now have both hypotheses: the alternating product is an algebraic
      integer, and every conjugate lies on the unit circle. Therefore

      $$
      \Delta(f)^r=1
      \quad\text{for some positive integer }r.
      $$

      Magnitude alone did not give finite order. The integrality step is
      what makes Kronecker's theorem applicable. Its proof bounds the
      integer coefficients of the minimal polynomials of all powers.
      Only finitely many such polynomials can occur, so two powers agree.
  - node: delta-odd-order
    dependsOn:
      - local-character-comparison
      - kronecker-step
    segment: { start: 197.79, end: 216.39 }
    script: |
      > **Lemma (Odd order).** *The order of $\Delta(f)$ is a power
      > of every prime dividing $u$. In particular it is odd.*

      The local comparison also gave $\Delta(f)$ residue $1$ in
      characteristic $p$, for every $p\mid u$. A root of unity with
      residue $1$ in characteristic $p$ must have $p$-power order.
      This follows by applying the geometric-sum identity to its
      prime-to-$p$ part.

      Since every prime dividing $u$ is odd, the order is odd. In the
      guiding case $u=3$, $\Delta(f)$ lies in $\mathbb Q(i,\omega)$, whose
      odd-order roots of unity are precisely

      $$
      \Delta(f)\in\{1,\omega,\omega^2\}.
      $$

      The possible relative phases are $0^\circ$, $120^\circ$, and
      $240^\circ$. If $u$ has two distinct prime divisors, the order must
      be a power of both, forcing the stronger conclusion $\Delta(f)=1$.

      Applying the theorem to the three norm solutions from Node 3 gives
      $\Delta(c),\Delta(d),\Delta(g)$ of odd order, ready for Node 6.
---

Let $u>1$ be odd, and let $I$ be the set of distinct primes dividing $u$.
Choose a primitive $p$th root of unity $\zeta_p$ for each $p\in I$.
For every subset $S\subseteq I$, put

$$
\zeta_S=\prod_{p\in S}\zeta_p,
\qquad \zeta_\varnothing=1.
$$

For a polynomial $f(P)\in\mathbb Z[i][P]/(P^{u^2}-1)$ whose evaluations
at these roots are nonzero, define

$$
\Delta(f)=
\frac{\displaystyle\prod_{\substack{S\subseteq I\\ |S|\text{ even}}}f(\zeta_S)}
{\displaystyle\prod_{\substack{S\subseteq I\\ |S|\text{ odd}}}f(\zeta_S)}.
$$

In other words, subsets containing an **even number of primes** contribute
factors to the numerator, and subsets containing an **odd number of primes**
contribute factors to the denominator. The empty subset counts as even,
so it contributes $f(1)$ to the numerator.

**Guiding example: $u=3$.** There is only one prime in $I$, so the subsets
are $\varnothing$ and $\{3\}$. Writing $\omega=e^{2\pi i/3}$, the entire
product becomes the simple quotient

$$
\Delta(f)=\frac{f(1)}{f(\omega)}.
$$

The Δ-theorem tells us what this comparison can be when $f$ satisfies
the norm identity:

> **Theorem (The Δ-theorem).** *Let $u>1$ be odd. If
> $f(P)\in\mathbb Z[i][P]/(P^{u^2}-1)$ satisfies*
>
> $$
> f(P)f^*(P)=u^2,
> $$
>
> *then $\Delta(f)$ is a root of unity of odd order.*

For $u=3$, the norm identity puts both $f(1)$ and $f(\omega)$ on the
circle of radius $3$. Their quotient lies on the unit circle and records
the rotation from $f(\omega)$ to $f(1)$. The theorem restricts this phase to

$$
\Delta(f)\in\{1,\omega,\omega^2\}:
\qquad 0^\circ,\ 120^\circ,\ 240^\circ.
$$

**Why should this be true?** The norm identity makes every evaluation
$f(\zeta_S)$ have absolute value $u$. Since there are equally many even
and odd subsets, these magnitudes cancel, giving $|\Delta(f)|=1$.
The same reasoning puts all its algebraic conjugates on the unit circle.
An arithmetic comparison of the evaluations also shows that $\Delta(f)$
is an algebraic integer. We can therefore apply **Kronecker's theorem**:
an algebraic integer whose conjugates all have absolute value one is a
root of unity. A further congruence argument using the odd primes dividing
$u$ shows that its order is odd.

The polynomials $c(P),d(P),g(P)$ from Node 3 satisfy this norm identity,
inherited from the Hadamard condition. Thus the theorem gives three
phases $\Delta(c),\Delta(d),\Delta(g)$ of odd order, ready to compare
in Node 6.
