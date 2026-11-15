---
id: theorem
title: Only orders 1 and 4
shortTitle: Theorem
summary: The general contradiction excludes odd u > 1; explicit examples supply
  the two remaining orders.
draft: true
mapPosition:
  - 250
  - 980
mapSummary: 'Only orders $1$ and $4$'
---

## Conclusion of the general route

A real circulant Hadamard matrix exists exactly at orders $1$ and $4$, by the high-level argument accepting Propositions 2.2 and 3.4. The order-36 example illustrates the mechanism; the general odd-$u$ argument is needed to exclude all other orders.

## The two examples

At order $1$, take $(1)$. At order $4$, take the circulant matrix

$$
H=\begin{pmatrix}
1 & 1 & 1 & -1 \\
-1 & 1 & 1 & 1 \\
1 & -1 & 1 & 1 \\
1 & 1 & -1 & 1
\end{pmatrix}.
$$

Its rows are cyclic shifts and $HH^{\mathsf T}=4I$. Here $u=1$, outside the Δ-theorem's hypothesis $u>1$.

[Read the general proof](../index.html).
