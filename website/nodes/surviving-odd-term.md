---
id: surviving-odd-term
title: One Surviving Odd Term
shortTitle: One Surviving Term
summary: Substitute the all-ones polynomial into the alternating sum; only the empty subset survives, with residue one.
number: "8.3"
draft: false
video:
  src: media/surviving-odd-term.mp4
  captions: media/surviving-odd-term.vtt
  duration: 190.966667
mapPosition: [240, 220]
mapSummary: '$\mathcal S\equiv\pm u\equiv1$'
---

> **Lemma (Only the empty subset survives).** Let $u>1$ be odd,
> let $I$ be its distinct prime divisors, and put
> $\zeta_S=\prod_{p\in S}\zeta_p$, with empty product $1$.
> Suppose $E(P)\equiv J(P)\pmod{1+i}$ coefficientwise, where
> $J(P)=1+P+\cdots+P^{u^2-1}$. For the norm solution $c(P)$
> from Node 3,
>
> $$
> \mathcal S:=\sum_{S\subseteq I}(-1)^{|S|}
> \frac{E(\zeta_S)}{c(\zeta_S)}
> \equiv\frac{u^2}{c(1)}=\pm u\equiv1\pmod{1+i}.
> $$
>
> All divisions use units of
> $A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]$.

## Substitute the coefficient congruence

Let $I$ be the distinct prime divisors of the odd integer $u>1$ and
$\zeta_S=\prod_{p\in S}\zeta_p$, with empty product $1$. Recall

$$
\mathcal S=\sum_{S\subseteq I}(-1)^{|S|}
\frac{E(\zeta_S)}{c(\zeta_S)}.
$$

Node 5 gives the coefficientwise congruence

$$
E(P)\equiv J(P)\pmod{1+i},
\qquad J(P)=1+P+\cdots+P^{u^2-1}.
$$

Evaluation preserves this congruence in
$A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]$. Node 6 gives an inverse
for every denominator:

$$
c(\zeta_S)^{-1}=\frac{\overline{c(\zeta_S)}}{u^2}.
$$

Multiplying by these inverses preserves the congruences. Hence

$$
\mathcal S\equiv
\sum_{S\subseteq I}(-1)^{|S|}
\frac{J(\zeta_S)}{c(\zeta_S)}
\pmod{1+i}.
$$

## All but one term vanish

Node 8.1 proves $J(\zeta_S)=0$ whenever $S\ne\varnothing$.
The only surviving term belongs to the empty subset. Its sign is
$(-1)^0=1$ and its evaluation is at $1$. Node 8.2 therefore gives

$$
\begin{aligned}
\mathcal S&\equiv\frac{J(1)}{c(1)}\\
&=\frac{u^2}{\pm u}=\pm u\\
&\equiv1\pmod{1+i}.
\end{aligned}
$$

In the guiding case $u=3$, this reads

$$
\begin{aligned}
\mathcal S&\equiv\frac9{c(1)}-\frac0{c(\omega)}\\
&=\pm3\equiv1\pmod{1+i}.
\end{aligned}
$$

The zero term remains zero because its denominator is a unit. The
surviving term has the explicit residue $1$, not just an unspecified
nonzero value.

**Output.** $\mathcal S\equiv1\pmod{1+i}$ in the same ring as Node 7.

Source: [the paper, Section 4, equation (4.11) and its final evaluation](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
