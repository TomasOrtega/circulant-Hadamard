---
id: final-contradiction
title: The Final Contradiction
shortTitle: The Final Contradiction
summary: The all-ones polynomial leaves one nonzero contribution, contradicting
  the vanishing relation.
number: 8
draft: true
video: null
mapPosition:
  - 250
  - 820
mapSummary: 0 ≡ ±u ≡ 1 mod (1+i)
---

## First route: $u=3$, $n=36$

The vanishing relation and $E\equiv J$ give

$$
0\equiv\frac{J(1)}{c(1)}-\frac{J(\omega)}{c(\omega)}
=\frac9{c(1)}=\pm3\equiv1\pmod{1+i}.
$$

Here $J(1)=9$, $J(\omega)=3(1+\omega+\omega^2)=0$, and $c(1)=\pm3$.

Equivalently, the common rotation gives $E(\omega)=\lambda E(1)$. In the quotient, $E(1)$ is $1$ and $\lambda$ is a unit, so their product cannot be $0$. This contradicts $E(\omega)\equiv0$. Thus order $36$ is impossible, accepting the Δ-theorem.

## General statement

**Inputs:** Node 7's vanishing alternating sum, Node 5's $E\equiv J$, Node 3's $cc^*=u^2$.

**Statement:** Since $\zeta_\varnothing=1$ and $\zeta_S\ne1$ for nonempty $S$,
$$
J(1)=u^2,\qquad J(\zeta_S)=0\quad(S\ne\varnothing).
$$
The alternating sum collapses to
$$
0\equiv\frac{u^2}{c(1)}.
$$
But $cc^*=u^2$ gives $c(1)=\pm u$, and odd $u$ reduces to $1$, so
$$
0\equiv\pm u\equiv1\pmod{1+i}.
$$
Contradiction. Examples exist at orders 1 and 4.

**Output:** The theorem.

## Where the congruences live

For the example, all reductions take place in $\mathbb Z[i,\omega,1/3]/(1+i)$. The denominator values are units because their squared absolute values are $9$. Form divisions by $2$ and $1+i$ in characteristic zero before reducing.

## Source and status

Exposition draft based on [OpenAI, *The circulant Hadamard conjecture*, Sections 2–4 (September 23, 2026)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf). Video scripts and deeper proof graphs will be added later.
