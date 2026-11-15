---
id: gaussian-parity
title: Gaussian Parity
shortTitle: Gaussian Parity
summary: Modulo 1+i, a Gaussian integer is determined by the parity of its real part plus its imaginary part.
number: "5.2"
draft: true
video: null
foundation: true
mapPosition: [440, 24]
mapSummary: 'Both signs reduce to $1$'
---

> **Lemma (Gaussian parity).** *For integers $a,b$, reduction modulo $1+i$
> sends $a+bi$ to $a+b$ modulo $2$. In particular,*
>
> $$
> \mathbb Z[i]/(1+i)\cong\mathbb F_2,
> \qquad i\equiv-1\equiv1\pmod{1+i}.
> $$

## Parity for Gaussian integers

A Gaussian integer has the form $a+bi$, where $a,b\in\mathbb Z$.
Two such numbers are congruent modulo $1+i$ when their difference is a
Gaussian-integer multiple of $1+i$.

We have

$$
\frac{a+bi}{1+i}
=\frac{a+b}{2}+i\frac{b-a}{2}.
$$

Thus $1+i$ divides $a+bi$ exactly when $a+b$ is even: in that case
$a$ and $b$ have the same parity, so both halves are integers. If the
quotient is a Gaussian integer, its real part also shows that $a+b$ is even.

Consequently, reduction modulo $1+i$ sends

$$
a+bi\longmapsto a+b\pmod2.
$$

This identifies $\mathbb Z[i]/(1+i)$ with the two-element field
$\mathbb F_2$. In particular,

$$
i\equiv1,\qquad -1\equiv1\pmod{1+i}.
$$

The factor identities behind these two congruences are

$$
i-1=i(1+i),\qquad 2=(1+i)(1-i).
$$

## Reduce polynomial coefficients

For any positive odd $u$, apply the same rule to each coefficient in
$\mathbb Z[i][P]/(P^{u^2}-1)$. The target is
$\mathbb F_2[P]/(P^{u^2}-1)$: the cycle relation stays in place, and each
Gaussian-integer coefficient is replaced by its residue $0$ or $1$.

For example, a coefficient equal to $i$ becomes $1$. A coefficient equal
to either sign $+1$ or $-1$ also becomes $1$.

## Divide before reducing

Both $2$ and $1+i$ become zero after reduction, so they cannot be used as
denominators in the quotient. In the definition of $E(P)$, first use the
sign parity to form the exact integral quotients in characteristic zero.
Only then reduce their coefficients modulo $1+i$.

**Output.** Multiples of $i-1$ disappear, and both signs have residue $1$.
These are the two facts used in the all-ones congruence.

For their role in this proof, see [the paper, Section 4, equations (4.5)–(4.9)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
