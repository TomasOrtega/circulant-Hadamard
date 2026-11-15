---
id: products-to-sums
title: From Products to Sums
shortTitle: From Products to Sums
summary: Canceling the common rotation contradicts the all-ones residues for u=3;
  exact product expansions supply the general vanishing sum.
number: 7
draft: true
video:
  src: media/products-to-sums.mp4
  captions: media/products-to-sums.vtt
  duration: 154.6
mapPosition:
  - 250
  - 660
mapSummary: '$u=3$: the algebraic contradiction'
graphLayout: proof-map
graphTitle: Inside Node 7 · From Products to Sums
children:
  - node: split-exact-products
    dependsOn: []
    segment: null
    script: |
      Let $I$ be the set of distinct primes dividing the odd integer $u>1$,
      with $\zeta_S=\prod_{p\in S}\zeta_p$ and $\zeta_\varnothing=1$.
      Recall the ratios from Node 6:

      $$
      \begin{aligned}
      r_S&=\frac{d(\zeta_S)}{c(\zeta_S)},\\
      w_S&=\frac{g(\zeta_S)}{c(\zeta_S)}.
      \end{aligned}
      $$

      The exact identities $R=W=1$ say that each even-subset product
      equals its odd-subset product:

      $$
      \begin{aligned}
      \prod_{|S|\text{ even}}r_S&=\prod_{|S|\text{ odd}}r_S,\\
      \prod_{|S|\text{ even}}w_S&=\prod_{|S|\text{ odd}}w_S.
      \end{aligned}
      $$

      For $u=3$, each side has just one factor. This is the common rotation
      from Node 6. Several distinct primes give genuine product identities.
  - node: expand-integral-products
    dependsOn: []
    segment: null
    script: |
      The sign divisibilities from Node 5 and the invertible denominators
      from Node 6 let us write

      $$
      \begin{aligned}
      r_S&=1+2\frac{d(\zeta_S)-c(\zeta_S)}{2c(\zeta_S)},\\
      w_S&=1+(1+i)\frac{g(\zeta_S)-c(\zeta_S)}{(1+i)c(\zeta_S)}.
      \end{aligned}
      $$

      Both displayed quotients belong to
      $\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]$. The divisions by $2$ and
      $1+i$ are exact coefficientwise divisions before evaluation;
      division by $c(\zeta_S)$ then uses its inverse in this ring.

      For any finite family of elements $x_j$ in the ring, multiplication
      gives an exact identity

      $$
      \prod_j(1+t x_j)=1+t\sum_jx_j+t^2Q,
      $$

      where $Q$ also belongs to the ring. Every term involving at least
      two selected factors contains $t^2$. Apply this separately with
      $t=2$ and $t=1+i$; no approximation is involved.
  - node: cancel-before-reduction
    dependsOn:
      - split-exact-products
      - expand-integral-products
    segment: null
    script: |
      Expand the equal even and odd products. Subtracting them cancels
      their constant terms and gives

      $$
      t\sum_{S\subseteq I}(-1)^{|S|}x_S+t^2Q=0.
      $$

      Cancel the nonzero factor $t$ in the original characteristic-zero
      domain. **Only then reduce modulo $1+i$.** Both choices of $t$,
      namely $2$ and $1+i$, have zero residue, so the remainder vanishes.
      The two applications give

      $$
      \sum_{S\subseteq I}(-1)^{|S|}
      \frac{d(\zeta_S)-c(\zeta_S)}{2c(\zeta_S)}\equiv0
      \pmod{1+i},
      $$

      $$
      \sum_{S\subseteq I}(-1)^{|S|}
      \frac{g(\zeta_S)-c(\zeta_S)}{(1+i)c(\zeta_S)}\equiv0
      \pmod{1+i}.
      $$

      There is no division by $2$ or $1+i$ in the reduction ring. That
      ring need not be a field: all cancellation happened beforehand.
  - node: vanishing-alternating-sum
    dependsOn:
      - cancel-before-reduction
    segment:
      start: 117.15
      end: 154.6
    script: |
      Add the two congruences. At each evaluation, the definition

      $$
      E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}
      $$

      combines their summands into $E(\zeta_S)/c(\zeta_S)$. Consequently

      $$
      \mathcal S:=\sum_{S\subseteq I}(-1)^{|S|}
      \frac{E(\zeta_S)}{c(\zeta_S)}\equiv0\pmod{1+i}.
      $$

      In the guiding example, the values of $c(P),d(P),g(P)$ share one
      rotation multiplier $\lambda$ from $P=1$ to $P=\omega$. Their
      fixed linear combination $E(P)$ satisfies
      $E(\omega)=\lambda E(1)$ too. Thus

      $$
      \frac{E(1)}{c(1)}-\frac{E(\omega)}{c(\omega)}=0
      $$

      exactly. The overview combines this equality with the all-ones
      residue to finish the $u=3$ contradiction. For general $u$, the
      product expansion establishes the congruence above; Node 8 then
      uses the all-ones residue to finish the general contradiction.
---

For our guiding case $u=3$, Node 6 established the exact equality

$$
\frac{E(\omega)}{c(\omega)}=\frac{E(1)}{c(1)},
\qquad \omega=e^{2\pi i/3}.
$$

We compare the residues of its two sides modulo $1+i$. Work in
$\mathbb Z[i,\omega,1/3]$, where the evaluated denominators are units:
for $z=1$ or $\omega$, the norm identity gives
$c(z)^{-1}=\overline{c(z)}/9$. These inverses remain valid after reduction.

Now use the all-ones congruence from Node 5,
$E(P)\equiv J(P)=1+P+\cdots+P^8\pmod{1+i}$.
At the two inputs,

$$
J(1)=9,\qquad J(\omega)=3(1+\omega+\omega^2)=0.
$$

Consequently $E(1)\equiv1$ and $E(\omega)\equiv0$ modulo $1+i$.
Moreover, $c(1)=\pm3\equiv1$, while $c(\omega)$ remains invertible.
The two equal ratios therefore have incompatible residues:

$$
\frac{E(1)}{c(1)}\equiv1,\qquad
\frac{E(\omega)}{c(\omega)}\equiv0\pmod{1+i}.
$$

This is a contradiction in the nonzero reduction ring. It rules out
$u=3$, and hence a circulant Hadamard matrix of order $36$.

For general odd $u>1$, the exact comparisons involve alternating
products over more evaluations. The deeper nodes establish the following
replacement for the vanishing difference in our example.

> **Lemma (From products to sums).** *Let $u>1$ be odd, and let
> $c(P),d(P),g(P)$ be the normalized polynomials from the common sign array.
> Define*
>
> $$
> E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
> $$
>
> *Write $I=\{p:p\mid u\}$ for the distinct prime divisors and
> $\zeta_S=\prod_{p\in S}\zeta_p$, with empty product $1$.
> The exact identities $R=W=1$ imply*
>
> $$
> \mathcal S:=\sum_{S\subseteq I}(-1)^{|S|}
> \frac{E(\zeta_S)}{c(\zeta_S)}\equiv0\pmod{1+i}.
> $$
>
> *The congruence is in $\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]$;
> every denominator $c(\zeta_S)$ is a unit there.*

Expand the equal products, cancel their common factors before reducing,
and add the resulting two sums to obtain $\mathcal S\equiv0$.
Node 8 combines this general conclusion with the all-ones polynomial
to rule out every odd $u>1$.
