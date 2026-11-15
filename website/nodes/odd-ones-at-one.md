---
id: odd-ones-at-one
title: An Odd Number of Ones at One
shortTitle: Odd Ones at One
summary: At one the all-ones polynomial is u squared, and its denominator is plus or minus u.
number: "8.2"
draft: true
video:
  src: media/odd-ones-at-one.mp4
  captions: media/odd-ones-at-one.vtt
  duration: 135.333333
mapPosition: [440, 24]
mapSummary: '$J(1)=u^2,\quad c(1)=\pm u$'
---

> **Lemma (The value at one).** Let $u>1$ be odd, let
> $J(P)=1+P+\cdots+P^{u^2-1}$, and suppose
> $c(P)\in\mathbb Z[P]/(P^{u^2}-1)$ satisfies
> $c(P)c^*(P)=u^2$. Then
>
> $$
> J(1)=u^2,\qquad c(1)=\pm u,\qquad
> \frac{J(1)}{c(1)}=\pm u\equiv1\pmod{1+i}.
> $$
>
> The congruence is in the common evaluation ring with $1/u$ adjoined.

## Every term becomes one

For an odd integer $u>1$, the all-ones polynomial has $u^2$ terms:

$$
J(P)=1+P+\cdots+P^{u^2-1}.
$$

At $P=1$, every term equals $1$. Consequently

$$
\boxed{J(1)=u^2.}
$$

Since $u$ is odd, $u^2$ is odd too. In the nonzero characteristic-two
ring used in Node 6, an even number of ones sums to zero and an odd
number sums to one. Thus $J(1)\equiv1\pmod{1+i}$.

## Account for the denominator

The alternating sum contains $J(1)/c(1)$, so we also need the value of
$c(1)$. Node 3 gives

$$
c(P)c^*(P)=u^2,
\qquad c(P)\in\mathbb Z[P]/(P^{u^2}-1).
$$

Because $c(P)$ has real integer coefficients, $c^*(1)=c(1)$. Evaluation
at $1$ gives

$$
c(1)^2=u^2,
\qquad\boxed{c(1)=\pm u.}
$$

Therefore, in the evaluation ring
$A=\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]$,

$$
\frac{J(1)}{c(1)}=\frac{u^2}{\pm u}=\pm u.
$$

Its residue modulo $(1+i)A$ is $1$: $u$ is odd, and minus equals plus
in characteristic two. This is stronger than merely knowing that
$c(1)$ is nonzero. Node 6 also establishes that this denominator is
a unit before and after reduction.

For $u=3$, the calculation is $J(1)=9$, $c(1)=\pm3$, and
$J(1)/c(1)=\pm3\equiv1\pmod{1+i}$. Pairing the nine ones leaves
one unpaired; after accounting for $c(1)$, the residue is still one.

**Output.** The empty-subset term has residue $1$.

Source: [the paper, equation (4.2) and the conclusion after equation (4.11)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf). The real value $c(1)=\pm u$ makes the surviving residue explicit.
