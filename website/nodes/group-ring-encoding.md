---
id: group-ring-encoding
title: Group-Ring Encoding
shortTitle: Group-Ring Encoding
summary: Encode every cyclic row correlation in one polynomial norm identity.
number: 1
draft: true
video: null
mapPosition:
  - 240
  - 24
mapSummary: hh* = n
---

## First route: $u=3$, $n=36$

A hypothetical circulant Hadamard matrix of order $36$ has a first-row sign polynomial with $hh^*=36$. Each coefficient of the product records one cyclic correlation. After reindexing by $C_{36}\cong C_4\times C_9$, write $h(Z,P)$ with $Z^4=P^9=1$. This is an assumption for contradiction, not an example of an existing matrix.

## General statement

**Input:** A circulant $n\times n$ sign matrix $H$.

**Statement:** If its first row is $(h_0,\dots,h_{n-1})$, represent it by
$$
h(X)=\sum_{j=0}^{n-1}h_jX^j\in\mathbb Z[X]/(X^n-1),\qquad
h^*(X)=h(X^{-1}).
$$
The coefficient of $X^a$ in $hh^*$ equals the dot product with the $a$-step cyclic shift. Thus
$$
HH^{\mathsf T}=nI\quad\Longleftrightarrow\quad hh^*=n.
$$

**Intuition:** Group-ring multiplication is cyclic convolution, exactly the list of orthogonality constraints.

**Output:** One polynomial norm identity, with signs retained coefficientwise.

## Source and status

Exposition draft based on [OpenAI, *The circulant Hadamard conjecture*, Sections 2–4 (September 23, 2026)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf). Video scripts and deeper proof graphs will be added later.
