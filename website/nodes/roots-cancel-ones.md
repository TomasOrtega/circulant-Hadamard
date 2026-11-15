---
id: roots-cancel-ones
title: The Nontrivial Roots Cancel the Ones
shortTitle: Roots Cancel the Ones
summary: Every nonempty subset gives a nontrivial root at which the all-ones polynomial vanishes exactly.
number: "8.1"
draft: true
video: null
mapPosition: [40, 24]
mapSummary: '$J(\zeta_S)=0\quad(S\ne\varnothing)$'
---

## The all-ones polynomial

Let $u>1$ be odd, let $I$ be its distinct prime divisors, and use the
primitive roots $\zeta_p$ from Node 4. Define

$$
J(P)=1+P+\cdots+P^{u^2-1},
\qquad
\zeta_S=\prod_{p\in S}\zeta_p.
$$

The empty product is $\zeta_\varnothing=1$. For a nonempty subset $S$,
put $m_S=\prod_{p\in S}p$. The orders of these roots are pairwise
coprime, so $\zeta_S$ has order exactly $m_S$.

To check this, its order divides $m_S$. For any $p\in S$, raising
$\zeta_S$ to the power $m_S/p$ kills all the other factors and leaves
$\zeta_p^{m_S/p}\ne1$, since $p$ does not divide $m_S/p$.
Thus its order contains every prime factor of the squarefree integer
$m_S$, and must be $m_S$.

In particular, $\zeta_S\ne1$ and $\zeta_S^{u^2}=1$, because $m_S$
divides $u^2$.

## A finite geometric sum

The polynomial identity

$$
(P-1)J(P)=P^{u^2}-1
$$

therefore gives

$$
(\zeta_S-1)J(\zeta_S)=0.
$$

This is an exact equality in the characteristic-zero domain

$$
A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]\subseteq\mathbb C.
$$

Cancel the nonzero factor $\zeta_S-1$ in this domain to obtain

$$
\boxed{J(\zeta_S)=0\qquad(S\ne\varnothing).}
$$

No cancellation in the reduction ring is needed. The value is already
zero before reducing modulo $1+i$.

## Nine terms in three groups

For $u=3$ and $\omega=e^{2\pi i/3}$, the nine terms are three copies
of the same three roots:

$$
J(\omega)=3(1+\omega+\omega^2)=0.
$$

Each group of three complex vectors closes into an equilateral triangle.
The general geometric-sum identity is the same cancellation for every
nontrivial evaluation used in the proof.

**Output.** Every nonempty-subset evaluation of $J(P)$ vanishes exactly.

Source: [the paper, Section 4, the evaluation of the all-ones sum after equation (4.11)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
