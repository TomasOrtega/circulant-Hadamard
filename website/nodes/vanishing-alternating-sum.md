---
id: vanishing-alternating-sum
title: Identify E(P) and Add the Sums
shortTitle: One Vanishing Sum
summary: Adding the two linear sums produces the alternating sum of normalized evaluations.
number: "7.4"
draft: false
video:
  src: media/vanishing-alternating-sum.mp4
  poster: media/thumbnails/vanishing-alternating-sum.jpg
  captions: media/vanishing-alternating-sum.vtt
  duration: 194.533333
mapPosition: [240, 420]
mapSummary: '$\mathcal S\equiv0\pmod{1+i}$'
---

> **Lemma (The vanishing alternating sum).** Let $u>1$ be odd, let
> $I$ be its distinct prime divisors, and put
> $\zeta_S=\prod_{p\in S}\zeta_p$, with empty product $1$.
> For the polynomials $c(P),d(P),g(P)$ from the common sign array, set
>
> $$
> E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
> $$
>
> The exact product identities from Node 6 imply
>
> $$
> \mathcal S:=\sum_{S\subseteq I}(-1)^{|S|}
> \frac{E(\zeta_S)}{c(\zeta_S)}\equiv0\pmod{1+i}
> $$
>
> in $A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]$.

## The same combination as Node 5

Recall the polynomial

$$
E(P)=\frac{d(P)-c(P)}{2}+\frac{g(P)-c(P)}{1+i}.
$$

Both polynomial quotients are exact, with Gaussian-integer coefficients.
Write $c_S=c(\zeta_S)$, $d_S=d(\zeta_S)$,
$g_S=g(\zeta_S)$, and $E_S=E(\zeta_S)$.
Evaluating and dividing by the unit $c_S$ gives the exact identity in $A$

$$
\frac{d_S-c_S}{2c_S}+
\frac{g_S-c_S}{(1+i)c_S}
=\frac{E_S}{c_S}.
$$

Node 7.3 shows that the alternating sum of each term on the left
vanishes modulo $1+i$. Add those two congruences in $A/(1+i)A$ and use
this identity term by term. Define

$$
\mathcal S=
\sum_{S\subseteq I}(-1)^{|S|}\frac{E(\zeta_S)}{c(\zeta_S)}.
$$

We obtain the general conclusion

$$
\boxed{\mathcal S\equiv0\pmod{1+i}.}
$$

The alternating signs come from splitting even and odd subsets before
reduction. In the characteristic-two quotient, minus and plus coincide,
but keeping these signs records how the sum arose from the exact
product identities.

## The two-evaluation picture

For $u=3$, the subsets give $\zeta_\varnothing=1$ and
$\zeta_{\{3\}}=\omega$. The sum has two terms:

$$
\mathcal S=\frac{E(1)}{c(1)}-\frac{E(\omega)}{c(\omega)}.
$$

The values of $c(P),d(P),g(P)$ acquire the same factor $\lambda$ when
passing from $P=1$ to $P=\omega$. Since $E(P)$ is a fixed complex-linear
combination of them, it also satisfies $E(\omega)=\lambda E(1)$.
The nonzero denominator satisfies $c(\omega)=\lambda c(1)$, so

$$
\frac{E(\omega)}{c(\omega)}
=\frac{\lambda E(1)}{\lambda c(1)}
=\frac{E(1)}{c(1)}.
$$

Here $\mathcal S=0$ exactly. With several distinct prime divisors, the
general argument gives the congruence above without asserting one
common rotation of all the evaluations.

**Output.** $\mathcal S\equiv0\pmod{1+i}$. This proof used the exact
quotients defining $E(P)$. The Node 7 overview already combines this with the
all-ones condition to finish $u=3$. For general odd $u$, Node 8 applies that
condition to the full alternating sum and completes the argument.

Source: [the paper, Section 4, the additive step leading to equation (4.11)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf). The general all-ones substitution is developed in Node 8.
