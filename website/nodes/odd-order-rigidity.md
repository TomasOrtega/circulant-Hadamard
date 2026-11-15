---
id: odd-order-rigidity
title: Odd-Order Rigidity
shortTitle: Odd-Order Rigidity
summary: The arithmetic and sign branches force the comparison products to equal
  one; in the nine-position example, the three evaluations share a rotation.
number: 6
draft: false
video:
  src: media/odd-order-rigidity.mp4
  poster: media/thumbnails/odd-order-rigidity.jpg
  captions: media/odd-order-rigidity.vtt
  duration: 261.966667
mapPosition:
  - 460
  - 500
mapSummary: '$R=W=1$'
graphLayout: proof-map
graphTitle: Inside Node 6 · Odd-Order Rigidity
children:
  - node: odd-comparison-products
    dependsOn: []
    segment: { start: 29.77, end: 55.63, poster: media/thumbnails/excerpts/odd-comparison-products.jpg }
    script: |
      > **Lemma (Odd comparison products).** The quantities
      >
      > $$
      > R=\frac{\Delta(d)}{\Delta(c)},\qquad
      > W=\frac{\Delta(g)}{\Delta(c)}
      > $$
      >
      > are roots of unity of odd order.

      The Δ-theorem supplies odd order for each individual Δ-value.
      If $\alpha^m=\beta^n=1$ with $m,n$ odd, then
      $(\alpha/\beta)^{mn}=1$. The quotient therefore has odd order too.

      For $u=3$, the comparison is between the two inputs $1$ and $\omega$:
      $R=(d(1)/c(1))/(d(\omega)/c(\omega))$, with the analogous expression
      for $W$. Both belong to $\{1,\omega,\omega^2\}$. The sign branch
      will provide their residue condition.

  - node: evaluation-units
    dependsOn: []
    segment: { start: 71.29, end: 91.99, poster: media/thumbnails/excerpts/evaluation-units.jpg }
    script: |
      > **Lemma (Unit evaluations).** For odd $u>1$, work in
      >
      > $$
      > A=\mathbb Z[i,\{\zeta_p:p\mid u\},1/u].
      > $$
      >
      > Every subset-root evaluation of $c(P),d(P),g(P)$ is a unit, and
      > $A/(1+i)A$ is a nonzero ring of characteristic two.

      For $x(P)\in\{c(P),d(P),g(P)\}$, the evaluated norm identity gives

      $$
      x(\zeta_S)^{-1}=\frac{\overline{x(\zeta_S)}}{u^2}\in A.
      $$

      These inverse identities survive reduction. To see that reduction is
      nonzero, put $B=\mathbb Z[i,\{\zeta_p:p\mid u\}]$. The finite free
      abelian group $B$ has $B/2B\ne0$. A maximal ideal above $2$ kills
      $1+i$ but not odd $u$, so its nonzero residue field is still a quotient
      after adjoining $1/u$. Thus $(1+i)A$ is proper. For $u=3$, the inverse
      of an evaluation is its conjugate divided by $9$.

  - node: sign-ratio-congruences
    dependsOn:
      - evaluation-units
    segment: { start: 55.63, end: 110.29, poster: media/thumbnails/excerpts/sign-ratio-congruences.jpg }
    script: |
      > **Lemma (Residue-one comparisons).** Every evaluated ratio
      > $d(\zeta_S)/c(\zeta_S)$ and $g(\zeta_S)/c(\zeta_S)$ has residue one.
      > Consequently $R\equiv W\equiv1\pmod{1+i}$.

      Node 5 gives exact identities

      $$
      d(P)-c(P)=2a(P),\qquad g(P)-c(P)=(1+i)b(P),
      $$

      with integral polynomial quotients. Evaluate and divide by the unit
      $c(\zeta_S)$. Subtracting one from each ratio leaves a multiple of
      $2$ or $1+i$, hence a multiple of $1+i$.

      Each factor in the alternating products defining $R,W$ therefore has
      residue one. Inverses of these units also have residue one, so both
      products do. All congruences use the single reduction ring from Node 6.2.

  - node: residue-one-rigidity
    dependsOn:
      - odd-comparison-products
      - sign-ratio-congruences
    segment: { start: 110.29, end: 145.03, poster: media/thumbnails/excerpts/residue-one-rigidity.jpg }
    script: |
      > **Lemma (Odd-order rigidity).** A root of unity of odd order in a
      > characteristic-zero domain that reduces to one in a nonzero ring
      > of characteristic two must equal one.

      Suppose instead that $\alpha\ne1$ has odd order $r$. Factor
      $\alpha^r-1$ and cancel $\alpha-1$ in the original domain to get

      $$
      1+\alpha+\cdots+\alpha^{r-1}=0.
      $$

      If $\alpha$ reduces to one, this becomes an odd number of ones,
      which sums to one in characteristic two. That contradicts zero.
      The cancellation happened before reduction; the quotient need not be
      a domain. Applying the lemma to $R,W$ gives the exact equalities
      $R=W=1$.

  - node: exact-comparison-identities
    dependsOn:
      - residue-one-rigidity
    segment: { start: 145.03, end: 218.59, poster: media/thumbnails/excerpts/exact-comparison-identities.jpg }
    script: |
      > **Proposition (Exact comparisons).** In general, $R=W=1$ equates
      > the even- and odd-subset products. For $u=3$, it gives
      >
      > $$
      > \frac{d(1)}{c(1)}=\frac{d(\omega)}{c(\omega)},\qquad
      > \frac{g(1)}{c(1)}=\frac{g(\omega)}{c(\omega)}.
      > $$

      Put $\lambda=c(\omega)/c(1)$. Both values have magnitude three, so
      $|\lambda|=1$. Rearranging shows that the same multiplier carries
      $c(1),d(1),g(1)$ to their values at $\omega$. The relative positions
      are preserved; the three points need not coincide.

      The fixed linear combination defining $E(P)$ also acquires $\lambda$.
      Dividing by the corresponding unit value of $c(P)$ gives

      $$
      \frac{E(\omega)}{c(\omega)}=\frac{E(1)}{c(1)}.
      $$

      With several distinct prime divisors, retain the exact alternating
      product identities. They do not assert a common rotation between every
      pair of inputs; Node 7 uses product expansion for that general case.
---

The key idea is to combine the two branches of the proof. The Δ-theorem
makes our comparison products roots of unity of odd order, while the
arithmetic of their common signs forces them to have residue $1$ modulo $1+i$.
Odd-order rigidity rules out every nontrivial root with these properties:
the order must be one, so both comparison products equal $1$.

> **Lemma (Odd-order rigidity).** *Let $u>1$ be odd, and let
> $c(P),d(P),g(P)$ be the normalized norm solutions from the common sign
> array in Node 3. Define*
>
> $$
> R=\frac{\Delta(d)}{\Delta(c)},
> \qquad W=\frac{\Delta(g)}{\Delta(c)}.
> $$
>
> *Then*
>
> $$
> R=W=1.
> $$

To obtain the residue condition, evaluate the sign divisibilities from
Node 5 and divide by the invertible evaluations, giving
$R\equiv W\equiv1\pmod{1+i}$. The smaller nodes inside Node 6 give the
full arithmetic argument and the proof of odd-order rigidity.

In our guiding case $u=3$, put $\omega=e^{2\pi i/3}$. The identities
$R=W=1$ mean exactly

$$
\begin{aligned}
\frac{d(1)}{c(1)}&=\frac{d(\omega)}{c(\omega)},\\
\frac{g(1)}{c(1)}&=\frac{g(\omega)}{c(\omega)}.
\end{aligned}
$$

Each ratio stays the same at the two inputs; $d(1)/c(1)$ need not equal
$g(1)/c(1)$.
The six evaluations lie on circles of radius three. Set
$\lambda=c(\omega)/c(1)$. Since $|\lambda|=1$, we obtain the common
rotation

$$
\begin{aligned}
c(\omega)&=\lambda c(1),\\
d(\omega)&=\lambda d(1),\\
g(\omega)&=\lambda g(1).
\end{aligned}
$$

Thus the three points rotate together, keeping their relative angles.
Now substitute the definition

$$
E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
$$

For $z=1$ or $\omega$, the value $c(z)$ is a unit in
$\mathbb Z[i,\omega,1/3]$. Dividing the evaluated identity by $c(z)$ gives

$$
\begin{aligned}
\frac{E(z)}{c(z)}
&=\frac12\left(\frac{d(z)}{c(z)}-1\right)\\
&\quad+\frac1{1+i}\left(\frac{g(z)}{c(z)}-1\right).
\end{aligned}
$$

The divisions by $2$ and $1+i$ are the exact divisions established in
Node 5, before any modular reduction. Both ratios on the right stay the
same when $z$ changes from $1$ to $\omega$, so

$$
\boxed{\frac{E(\omega)}{c(\omega)}=\frac{E(1)}{c(1)}.}
$$

Equivalently, $E(\omega)=\lambda E(1)$: the value of $E(P)$ picks up
the same rotation. Node 7 compares this exact equality with the residues
required by $E(P)\equiv J(P)\pmod{1+i}$ to obtain the contradiction
for $u=3$.

The general case requires more care. With several distinct prime divisors
of $u$, the identities $R=W=1$ compare alternating products; we cannot
assume one shared rotation between every pair of evaluation points.
The smaller nodes in Node 7 turn those product identities into a
vanishing alternating-sum congruence, which Node 8 uses to finish the
general argument.
