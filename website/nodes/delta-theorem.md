---
id: delta-theorem
title: The Δ-Theorem
shortTitle: The Δ-Theorem
summary: An independent arithmetic statement about norm solutions, with no sign
  hypothesis.
number: 4
draft: true
video: null
mapPosition:
  - 460
  - 180
mapSummary: Δ(f) has odd order
blackBox: Proposition 3.4
---

## First route: $u=3$, $n=36$

Accept Proposition 3.4 in the case $u=3$: for any Gaussian-integer polynomial modulo $P^9-1$ with $ff^*=9$,

$$
\Delta(f)=\frac{f(1)}{f(\omega)}
$$

is a root of unity of odd order. Apply this to $c,d,g$. The value may be $1$; it need not be a primitive root. This accepted black box does not assume that $f$ came from signs.

## General statement

**Input:** Arbitrary $f\in\mathbb Z[i][P]/(P^{u^2}-1)$ with $ff^*=u^2$, for odd $u>1$. It does **not** require sign coefficients or a Hadamard matrix.

**Definitions:** For each prime $p\mid u$, fix a primitive $p$th root $\zeta_p$. For each subset $S$ of the distinct prime divisors, let $\zeta_S=\prod_{p\in S}\zeta_p$ and $\zeta_\varnothing=1$. Define
$$
\Delta(f)=\prod_{S\subseteq\{p:p\mid u\}}
f(\zeta_S)^{(-1)^{|S|}}.
$$

**Statement (accept Proposition 3.4):** $\Delta(f)$ is a root of unity of **odd order**. It need not be a *primitive* root and can equal $1$.

**Intuition:** The alternating product is a ratio for one prime and a ratio of ratios for two primes. It cancels common complex magnitudes, while local prime-by-prime arithmetic removes denominators. Integral algebraic numbers whose conjugates have absolute value 1 are roots of unity.

**Output:** Apply later to $c,d,g$, then take ratios of their Δ-values.

**Status:** BLACK BOX; later expand local character-comparison and integrality proof.

## Source and status

Exposition draft based on [OpenAI, *The circulant Hadamard conjecture*, Sections 2–4 (September 23, 2026)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf). This proposition is an **accepted black box** here; its internal proof graph will be added later.
