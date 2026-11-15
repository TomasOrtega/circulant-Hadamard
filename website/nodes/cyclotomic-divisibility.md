---
id: cyclotomic-divisibility
title: Compare Opposite Coefficients
shortTitle: Opposite Coefficients
summary: A cyclotomic divisibility lemma controls differences between positions halfway around a power-of-two cycle.
number: "2.4"
draft: true
video:
  src: media/cyclotomic-divisibility.mp4
  captions: media/cyclotomic-divisibility.vtt
  duration: 228.066667
blackBox: Lemma 2.1
mapPosition: [440, 210]
mapSummary: '$2^t$ divides opposite differences'
---

> **Lemma (Opposite-coefficient divisibility).** *Let $k\geq1$, $t\geq0$,
> and let $w$ be odd. If $T(X)=\sum_{j=0}^{2^k-1}a_jX^j$ has integer
> coefficients and satisfies $T(X)T^*(X)=2^{2t}w^2$ on the cycle of
> length $2^k$, then*
>
> $$
> 2^t\mid a_j-a_{j+2^{k-1}}
> \qquad(0\leq j<2^{k-1}).
> $$

Put $D=2^{k-1}$ and choose a primitive $2^k$th root $\xi$. We use the
following standard cyclotomic fact, the $p=2$, $L=1$ case of Lemma 2.1.
Write $\mathbb Z_{(2)}$ for rational numbers with odd denominators.
The ring $\mathbb Z_{(2)}[\xi]$ has basis $1,\xi,\ldots,\xi^{D-1}$.
Its powers of $\xi-1$ give an additive valuation $v$, normalized by
$v(2)=1$. For integers $b_j$ and $\ell\geq0$, the condition

$$
v\!\left(\sum_{j=0}^{D-1}b_j\xi^j\right)\geq\ell
$$

holds exactly when $2^\ell$ divides every coefficient $b_j$.

This is the needed passage from divisibility of a root evaluation to
ordinary integer divisibility of its basis coefficients. Its cyclotomic
input is that $\Phi_{2^k}(X)=X^D+1$, the shifted polynomial
$\Phi_{2^k}(1+Y)$ is Eisenstein at $2$, and $2$ is a unit times
$(\xi-1)^D$ in this local ring. Lemma 2.1 proves the general form.
These properties let us read divisibility from the coefficients in the
specified basis.

Conjugation preserves the valuation: it sends $\xi-1$ to
$-\xi^{-1}(\xi-1)$, differing by a unit. Evaluating the norm identity gives

$$
T(\xi)\overline{T(\xi)}=2^{2t}w^2.
$$

Since $w$ is odd, the right side has valuation $2t$. Both factors on the
left have the same valuation, so $v(T(\xi))=t$.

Finally, $\xi^D=-1$ combines opposite positions:

$$
T(\xi)=\sum_{j=0}^{D-1}(a_j-a_{j+D})\xi^j.
$$

This expression uses exactly the cyclotomic basis. Its valuation is $t$,
so the coefficient statement gives $2^t\mid a_j-a_{j+D}$ for every $j$.

At order $16$, take $k=4,t=2,w=1$ and sign coefficients. A difference of
signs is $-2$, $0$, or $2$; divisibility by $4$ forces it to be zero.
The eight-step shift would then repeat the row, contradicting orthogonality.
The folding nodes extend the obstruction to all larger powers of two.

Source: [the paper, Section 2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
