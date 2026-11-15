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
      > **Lemma (Separate the two products).** The exact identities from
      > Node 6 give
      >
      > $$
      > \prod_{|S|\text{ even}}r_S=\prod_{|S|\text{ odd}}r_S,
      > \qquad
      > \prod_{|S|\text{ even}}w_S=\prod_{|S|\text{ odd}}w_S.
      > $$

      Let $I$ be the distinct prime divisors of the odd integer $u>1$.
      Choose primitive $p$th roots $\zeta_p$. For $S\subseteq I$, put
      $\zeta_S=\prod_{p\in S}\zeta_p$ with empty product $1$, and
      $r_S=d(\zeta_S)/c(\zeta_S)$, $w_S=g(\zeta_S)/c(\zeta_S)$.
      All factors are units in $\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]$.
      Multiply the alternating-product identity by its odd-subset product
      to remove the negative exponents. For $u=3$ this is an equality of
      two factors; with two distinct primes it is an equality of two
      products, so no common rotation across all inputs is assumed.
  - node: expand-integral-products
    dependsOn: []
    segment: null
    script: |
      > **Lemma (Exact expansion).** For a finite family $x_j$ in a
      > commutative ring and $t$ in that ring,
      >
      > $$
      > \prod_j(1+t x_j)=1+t\sum_jx_j+t^2Q
      > $$
      >
      > for an element $Q$ of the same ring.

      Choose either $1$ or $t x_j$ from each factor. Selecting none gives
      $1$; selecting one gives the sum; selecting two or more supplies a
      factor $t^2$. Nothing is discarded. Apply this with
      $t=2$, $x_S=(d(\zeta_S)-c(\zeta_S))/(2c(\zeta_S))$, and with
      $t=1+i$, $x_S=(g(\zeta_S)-c(\zeta_S))/((1+i)c(\zeta_S))$.
      These quotients are in the evaluation ring: divide the coefficientwise
      sign differences exactly first, then use the unit $c(\zeta_S)$.
  - node: cancel-before-reduction
    dependsOn:
      - split-exact-products
      - expand-integral-products
    segment: null
    script: |
      > **Lemma (Cancel before reducing).** If the two expanded products
      > give $tL+t^2Q=0$ in the characteristic-zero evaluation domain, then
      >
      > $$
      > L=-tQ\equiv0\pmod{1+i}
      > $$
      >
      > for either $t=2$ or $t=1+i$.

      Subtract the odd-subset product from the even-subset product.
      The constant terms cancel. Cancel the nonzero factor $t$ in the
      original domain, then reduce. Both $2=(1+i)(1-i)$ and $1+i$ vanish
      in the quotient. This gives a vanishing alternating sum for each
      family of exact divided differences. No division by the zero residue
      of $2$ or $1+i$ occurs.
  - node: vanishing-alternating-sum
    dependsOn:
      - cancel-before-reduction
    segment:
      start: 117.15
      end: 154.6
    script: |
      > **Lemma (The vanishing sum).** The two preceding congruences imply
      >
      > $$
      > \mathcal S:=\sum_{S\subseteq I}(-1)^{|S|}
      > \frac{E(\zeta_S)}{c(\zeta_S)}\equiv0\pmod{1+i}.
      > $$

      Add the sums term by term in their common quotient ring. Their
      summands combine because

      $$
      \frac{d(\zeta_S)-c(\zeta_S)}{2c(\zeta_S)}+
      \frac{g(\zeta_S)-c(\zeta_S)}{(1+i)c(\zeta_S)}
      =\frac{E(\zeta_S)}{c(\zeta_S)}.
      $$

      For $u=3$, both product expansions have one factor per side, so the
      sum is exactly zero. For general $u$, the congruence above is the
      conclusion needed by Node 8.
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
