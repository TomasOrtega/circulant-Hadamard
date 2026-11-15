---
id: cyclic-group-ring
title: Group Ring
shortTitle: Group Ring
summary: Cyclic positions become powers of X, with a unique coefficient list of
  length n.
number: "1.1"
draft: true
video:
  src: media/cyclic-group-ring.mp4
  captions: media/cyclic-group-ring.vtt
  duration: 120.033333
mapPosition:
  - 240
  - 24
mapSummary: '$\mathbb Z[C_n]\cong\mathbb Z[X]/(X^n-1)$'
foundation: true
---

## Definition

Let $n\geq1$ and let $C_n=\langle X\mid X^n=1\rangle$ be the cyclic group of order $n$. Its integer group ring is

$$
\mathbb Z[C_n]\cong\mathbb Z[X]/(X^n-1).
$$

The symbol $X$ marks one step around the cycle. An element is an integer linear combination of the positions $1,X,\ldots,X^{n-1}$. Addition is coefficientwise; multiplication adds exponents modulo $n$.

## Unique polynomial representatives

**Proposition.** Every element of this group ring has a unique expression

$$
a_0+a_1X+\cdots+a_{n-1}X^{n-1},\qquad a_j\in\mathbb Z.
$$

**Proof.** The relation $X^n=1$ reduces every nonnegative exponent modulo $n$, giving a representative of degree less than $n$. If two such representatives agree in this group ring, their difference is divisible by $X^n-1$. A nonzero multiple of this monic degree-$n$ polynomial has degree at least $n$, so the difference must be zero. Thus the coefficients are uniquely determined.

Also $X$ is invertible, with $X^{-1}=X^{n-1}$. For example, when $n=4$, $X^4=1$, $X^5=X$, and $X^{-1}=X^3$.

**Output.** An ordered coefficient list and a degree-less-than-$n$ representative are equivalent descriptions of the same group-ring element. This makes coefficient notation in later nodes unambiguous.
