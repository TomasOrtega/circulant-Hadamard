---
id: odd-order-rigidity
title: Odd-Order Rigidity
shortTitle: Odd-Order Rigidity
summary: "The arithmetic and sign branches meet: the two comparison quotients equal 1."
number: 6
draft: true
video: null
mapPosition:
  - 460
  - 500
mapSummary: '$R=W=1$'
---

## Guiding example: $u=3$, $n=36$

Compare the two evaluations by

$$
R=\frac{d(1)/c(1)}{d(\omega)/c(\omega)},\qquad
W=\frac{g(1)/c(1)}{g(\omega)/c(\omega)}.
$$

The Δ-theorem makes both roots of unity of odd order. The sign divisibilities make both congruent to $1$ modulo $1+i$, hence $R=W=1$ exactly.

To see the rigidity, a nontrivial root $\xi$ of odd order $r$ satisfies $1+\xi+\cdots+\xi^{r-1}=0$. If $\xi\equiv1$, reduction gives $r\equiv0$ in characteristic two, contradicting oddness.

## General statement

**Inputs:** Node 3 (three norm solutions), Node 4 (the Δ-theorem), Node 5 (sign divisibilities).

**Define:**
$$
R=\frac{\Delta(d)}{\Delta(c)},\qquad
W=\frac{\Delta(g)}{\Delta(c)}.
$$

**Statement:** Node 4 makes $R,W$ roots of unity of odd order. Node 5 implies $R\equiv W\equiv1\pmod{1+i}$. A root of unity of odd order that reduces to $1$ in characteristic $2$ must equal $1$ exactly. Thus
$$
R=W=1.
$$

**Intuition:** The arithmetic branch and sign branch meet here: approximate congruence becomes exact equality.

**Output:** Two exact product identities for Node 7.

## Where the congruences live

For the example, all reductions take place in $\mathbb Z[i,\omega,1/3]/(1+i)$. The denominator values are units because their squared absolute values are $9$. Form divisions by $2$ and $1+i$ in characteristic zero before reducing.

## Source and status

Exposition draft based on [OpenAI, *The circulant Hadamard conjecture*, Sections 2–4 (September 23, 2026)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf). Video scripts and deeper proof graphs will be added later.
