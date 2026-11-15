---
id: kronecker-step
title: Kronecker's Theorem
shortTitle: Kronecker's Theorem
summary: Integrality and unit magnitude for every conjugate force the alternating product to be a root of unity.
number: "4.5"
draft: false
video:
  src: media/kronecker-step.mp4
  poster: media/thumbnails/kronecker-step.jpg
  captions: media/kronecker-step.vtt
  duration: 183.933333
mapPosition: [40, 560]
mapSummary: The product is a root of unity
---

## From integrality to finite order

> **Kronecker's theorem.** *If an algebraic integer has absolute value
> $1$ under every embedding of its number field into $\mathbb C$, then
> it is a root of unity.*

A root of unity is a complex number $z$ for which $z^r=1$ for some positive
integer $r$. Its powers return to $1$ after finitely many rotations.

An algebraic integer is a root of a monic polynomial with integer
coefficients. That integer condition is what prevents indefinitely many
different powers on the unit circle.

## Only finitely many polynomials can occur

Let $d$ be the degree of $z$ over $\mathbb Q$. For every positive integer
$m$, the power $z^m$ is still an algebraic integer, has degree at most
$d$, and all its conjugates have magnitude $1$.

Its monic minimal polynomial has integer coefficients. If its roots are
$\alpha_1,\ldots,\alpha_r$, with $r\leq d$, the coefficient $k$ places
below the leading term is, up to sign, the sum of products of $k$ distinct
roots. Each product has magnitude $1$, so this coefficient has absolute
value at most $\binom{r}{k}\leq\binom{d}{k}$.

Thus the degree and every integer coefficient are bounded independently
of $m$. Only finitely many such polynomials exist, and each has finitely
many roots. All powers $z,z^2,z^3,\ldots$ therefore belong to a finite set.

## Two equal powers finish the proof

There are positive integers $a<b$ with $z^a=z^b$. Since $|z|=1$,
we can divide by $z^a$ to obtain

$$
z^{b-a}=1.
$$

This proves the criterion. Both hypotheses were needed. For example,
$(3+4i)/5$ and its conjugate both lie on the unit circle, but their trace
is $6/5$, so they are not algebraic integers and are not roots of unity.

## Apply the criterion

Node 4.2 established that every conjugate of $\Delta(f)$ has absolute
value $1$. Node 4.4 established that $\Delta(f)$ lies in
$B=\mathbb Z[i,\{\zeta_p:p\mid u\}]$, hence is an algebraic integer.
Both hypotheses now hold, and Kronecker gives

$$
\Delta(f)^r=1
\quad\text{for some positive integer }r.
$$

The alternating product has finite order. This does not yet
specify that the order is odd; the next step uses the local residue
information retained from the integrality argument.

Source: [the paper, Lemma 3.3(i) and Proposition 3.4](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
