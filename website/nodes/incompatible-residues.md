---
id: incompatible-residues
title: The Two Residues Cannot Agree
shortTitle: The Contradiction
summary: The same alternating sum has residues zero and one in a nonzero ring, excluding every odd u greater than one.
number: "8.4"
draft: false
video:
  src: media/incompatible-residues.mp4
  captions: media/incompatible-residues.vtt
  duration: 129.4
mapPosition: [240, 420]
mapSummary: '$\mathcal S\equiv0,\quad\mathcal S\equiv1$'
---

> **Proposition (The contradiction).** The preceding product identities
> and coefficient congruence cannot hold for the polynomials from a
> circulant Hadamard matrix of order $4u^2$ with $u>1$ odd. They would
> force the same element $\mathcal S$ to have both residues $0$ and $1$
> in the same nonzero quotient ring. Thus no such matrix exists.

## Two conclusions about the same sum

Assume a circulant Hadamard matrix exists at order $4u^2$ with $u>1$
odd. The preceding nodes construct $c(P),d(P),g(P),E(P)$ and define

$$
\mathcal S=\sum_{S\subseteq I}(-1)^{|S|}
\frac{E(\zeta_S)}{c(\zeta_S)},
$$

where $I$ contains the distinct primes dividing $u$ and
$\zeta_S=\prod_{p\in S}\zeta_p$, with $\zeta_\varnothing=1$.
All denominators
are units in $A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]$.

Node 7's product-to-sum argument proves

$$
\mathcal S\equiv0\pmod{1+i}.
$$

Node 8.3's all-ones evaluation proves

$$
\mathcal S\equiv1\pmod{1+i}.
$$

Both congruences hold in the same quotient $A/(1+i)A$.
Together they would give $0=1$ there. But Node 6 established that this
quotient is a nonzero ring, so its zero and identity are distinct.
This is the contradiction.

## What has been excluded

The contradiction rules out every odd $u>1$, not only $u=3$.
The order-$36$ example shows the cancellation with nine terms, while
Nodes 8.1–8.3 establish the general calculation for all the subset roots.

The proof does not rule out $u=1$. The Δ-theorem used earlier requires
$u>1$, so its odd-order conclusion cannot be applied at $u=1$.
The next step combines the exclusion with the order restriction and
checks the remaining examples.

**Output.** No circulant Hadamard matrix has order $4u^2$ for odd $u>1$.

Source: [the paper, Section 4, the contradiction after equation (4.11) and Remark 4.2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
