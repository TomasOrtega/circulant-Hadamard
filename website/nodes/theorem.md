---
id: theorem
title: Only orders 1 and 4
shortTitle: Theorem
summary: The general contradiction excludes odd u greater than one; explicit examples supply the two remaining orders.
number: "8.5"
draft: true
video: null
mapPosition: [240, 620]
mapSummary: 'Exactly orders $1$ and $4$'
---

> **Theorem (Circulant Hadamard).** *Let $n$ be a positive integer.
> A real circulant Hadamard matrix of order $n$ exists if and only if
> $n\in\{1,4\}$.*

## Exclude every other order

For $n>1$, Node 2 gives the order restriction

$$
n=4u^2\qquad\text{with }u\text{ a positive odd integer}.
$$

The general contradiction in Node 8.4 excludes every $u>1$.
Thus $u=1$, giving $n=4$. The order $n=1$ is the remaining case
outside that restriction.

This conclusion uses the earlier proof chain, including the order
restriction developed in Node 2 and the Δ-theorem developed in Node 4
with its stated inputs. The nine-position example illustrates the
mechanism; the general argument is what excludes every other order.

## Verify the two examples

At order $1$, take the matrix $(1)$. Its only row has squared length
$1$, there are no two distinct rows to compare, and cyclic shifting fixes
that row. Thus it is circulant and satisfies $(1)(1)^{\mathsf T}=(1)$.
At order $4$, return to the
same example used on the main page:

$$
H=\begin{pmatrix}
-1 & 1 & 1 & 1 \\
1 & -1 & 1 & 1 \\
1 & 1 & -1 & 1 \\
1 & 1 & 1 & -1
\end{pmatrix}.
$$

Every row is the cyclic right shift of the preceding row. Two distinct
rows agree in two positions and disagree in two, so their inner product
is zero. Each row has squared length $4$. Hence

$$
HH^{\mathsf T}=4I_4.
$$

Both allowed orders therefore occur. The order-four example has $u=1$,
outside the Δ-theorem's hypothesis $u>1$, so it does not conflict with
the contradiction.
