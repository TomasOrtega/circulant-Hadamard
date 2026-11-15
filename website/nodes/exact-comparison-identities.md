---
id: exact-comparison-identities
title: Exact Comparisons and a Common Rotation
shortTitle: Exact Comparisons
summary: The comparison products equal one; in the two-evaluation example this means one common rotation of all three points.
number: "6.5"
draft: true
video:
  src: media/exact-comparison-identities.mp4
  captions: media/exact-comparison-identities.vtt
  duration: 209.133333
mapPosition: [240, 560]
mapSummary: '$R=W=1$; one rotation when $u=3$'
---

> **Proposition (Exact comparisons).** *For the polynomials in Node 6,
> $R=W=1$ gives exact alternating-product identities. When $u=3$, put
> $\lambda=c(\omega)/c(1)$, where $\omega=e^{2\pi i/3}$. Then*
>
> $$
> \begin{aligned}
> c(\omega)&=\lambda c(1),\\
> d(\omega)&=\lambda d(1),\\
> g(\omega)&=\lambda g(1),\\
> E(\omega)&=\lambda E(1),
> \end{aligned}
> \qquad |\lambda|=1.
> $$
>
> *In particular, $E(\omega)/c(\omega)=E(1)/c(1)$.*

## The general output

For any odd $u>1$, the conclusion $R=W=1$ is the pair of exact identities

$$
\begin{aligned}
\prod_{S\subseteq I}\left(\frac{d_S}{c_S}\right)^{(-1)^{|S|}}&=1,\\
\prod_{S\subseteq I}\left(\frac{g_S}{c_S}\right)^{(-1)^{|S|}}&=1.
\end{aligned}
$$

Here $I$ is the set of distinct primes dividing $u$, and $c_S,d_S,g_S$
are evaluations at the subset roots from Node 4. These multiplicative
identities are what the next node receives.

## Two evaluations give a common rotation

For $u=3$, there are just the evaluations at $1$ and
$\omega=e^{2\pi i/3}$. The two identities become

$$
\begin{aligned}
\frac{d(1)}{c(1)}&=\frac{d(\omega)}{c(\omega)},\\
\frac{g(1)}{c(1)}&=\frac{g(\omega)}{c(\omega)}.
\end{aligned}
$$

Define

$$
\lambda=\frac{c(\omega)}{c(1)}.
$$

Both values have magnitude $3$, so $|\lambda|=1$. Rearranging the ratio
identities gives

$$
\begin{aligned}
c(\omega)&=\lambda c(1),\\
d(\omega)&=\lambda d(1),\\
g(\omega)&=\lambda g(1).
\end{aligned}
$$

All three points undergo the same rotation from the evaluation at $1$
to the evaluation at $\omega$. Their relative positions remain fixed;
the points need not coincide. Also $\lambda=\Delta(c)^{-1}$, so in this
example $\lambda\in\{1,\omega,\omega^2\}$.

## The same rotation for the sign combination

Recall the polynomial defined by exact integral quotients in Node 5:

$$
E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
$$

Substitute the three shared-rotation identities. Both differences acquire
the same factor $\lambda$, giving $E(\omega)=\lambda E(1)$. Since
$c(\omega)=\lambda c(1)$ and these values are units, division gives

$$
\frac{E(\omega)}{c(\omega)}
=\frac{\lambda E(1)}{\lambda c(1)}
=\frac{E(1)}{c(1)}.
$$

The divisions defining $E(P)$ were made before reduction. This conclusion
does not divide by $E(1)$, so it also covers a zero value of $E(1)$.
Nor does it assert $E(1)\equiv E(\omega)$: the multiplier $\lambda$ may
have nontrivial residue. Node 7 compares the normalized equality with the
additional all-ones congruence.

## Keep the example separate from the general conclusion

When $u$ has several distinct prime divisors, $R=W=1$ compares alternating
products over several evaluations. It does not by itself say that one
rotation carries every evaluated triple to every other triple. The simple
two-circle picture describes the one-prime example.

**Output.** $R=W=1$ in general, with the common-rotation interpretation
for the guiding case $u=3$.

Source: [the paper, Section 4, equations (4.3), (4.4), and (4.10)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
