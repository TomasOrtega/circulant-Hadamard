---
id: order-is-even
title: Pair the Dot-Product Terms
shortTitle: Pair +1 and −1 Terms
mapTitle: 'Pair $+1$ and $-1$ Terms'
summary: Orthogonality pairs each positive contribution with a negative one, forcing an even number of terms.
number: "2.2"
draft: true
video: null
foundation: true
mapPosition: [440, 24]
mapSummary: '$n$ is even'
---

## Statement

If a Hadamard matrix has order $n>1$, then $n$ is even.

Choose two distinct rows. Their dot product is zero and has $n$ terms, each
equal to $+1$ or $-1$. There must be equally many positive and negative terms,
so the total number of terms is even.

## Pairing in the order-four example

The first two rows give

$$
(-1,1,1,1)\cdot(1,-1,1,1)=-1-1+1+1=0.
$$

Pair the two negative contributions with the two positive contributions.
The same counting argument applies to any pair of distinct rows at any order.

**Output.** Combining evenness with the square restriction gives
$n=4u^2$ for a positive integer $u$. Showing that $u$ is odd still requires
the remaining steps.
