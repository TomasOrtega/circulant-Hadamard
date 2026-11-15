---
id: star-operation
title: Star Operation
shortTitle: Star Operation
summary: Replacing X by its inverse reverses cyclic positions while preserving
  the coefficients.
number: "1.3"
draft: true
video:
  src: media/star-operation.mp4
  captions: media/star-operation.vtt
  duration: 137.333333
mapPosition:
  - 460
  - 180
mapSummary: '$h^*(X)=h(X^{-1})$'
foundation: true
---

## Definition

For $h(X)=\sum_{j=0}^{n-1}h_jX^j$ in $\mathbb Z[X]/(X^n-1)$, define

$$
h^*(X)=h(X^{-1})=\sum_{j=0}^{n-1}h_jX^{-j}.
$$

Since $X^{-1}=X^{n-1}$, the result remains in the same group ring. In coefficient form,

$$
(h_0,h_1,\ldots,h_{n-1})\longmapsto(h_0,h_{n-1},\ldots,h_1).
$$

The coefficient at position zero stays fixed; the other cyclic positions are read in reverse order. Star does not change the signs, and $h^*$ is not the reciprocal $1/h$.

## A well-defined involution

Replacing $X$ by $X^{-1}$ respects the defining relation because $(X^{-1})^n=1$. Hence the substitution is well-defined on the quotient ring. Applying it twice returns $X$ to itself, so $(h^*)^*=h$. It preserves addition and, in this commutative group ring,

$$
(fg)^*=f^*g^*.
$$

## The corrected example

For four arbitrary coefficients, reversal is visible:

$$
a+bX+cX^2+dX^3\longmapsto a+dX+cX^2+bX^3.
$$

For our original sign row, however,

$$
h(X)=-1+X+X^2+X^3,\qquad h^*(X)=h(X).
$$

The last three coefficients are equal, so the reversal leaves this particular polynomial unchanged. We keep the original matrix and first row throughout.

**Output.** A cyclic reversal operation that will turn polynomial multiplication into dot products.
