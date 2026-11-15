---
id: cancel-before-reduction
title: Cancel Before Reducing
shortTitle: Cancel, Then Reduce
summary: Cancel the common factor in characteristic zero before reducing the two resulting sums modulo one plus i.
number: "7.3"
draft: false
video:
  src: media/cancel-before-reduction.mp4
  captions: media/cancel-before-reduction.vtt
  duration: 214.9
mapPosition: [240, 220]
mapSummary: '$tL+t^2Q=0\ \Longrightarrow\ L\equiv0$'
---

> **Lemma (Cancel before reducing).** In
> $A=\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]\subseteq\mathbb C$,
> let $t$ be either $2$ or $1+i$. If $L,Q\in A$ satisfy
> $tL+t^2Q=0$, then
>
> $$
> L=-tQ\equiv0\pmod{(1+i)A}.
> $$
>
> Applied to the equal products from Node 7.1, this makes each of the
> two alternating sums of divided differences vanish in the same
> quotient ring.

## Combine the two inputs

Let $I$ be the distinct prime divisors of $u$, put
$\zeta_S=\prod_{p\in S}\zeta_p$, and abbreviate
$c_S=c(\zeta_S)$, $d_S=d(\zeta_S)$, $g_S=g(\zeta_S)$.
Node 7.1 gives equal products over even and odd subsets. Node 7.2
expands each side exactly. For either family, subtracting the two sides
cancels the constant terms and gives an equality of the form

$$
tL+t^2Q=0,
\qquad L,Q\in A.
$$

Here $L$ is the sum of the even-subset linear terms minus the sum of the
odd-subset linear terms. The element $Q$ collects the difference of the
two remaining terms after factoring out $t^2$.

The ring $A\subseteq\mathbb C$ is a domain, and both choices of $t$,
namely $2$ and $1+i$, are nonzero. Cancel $t$ in this original ring:

$$
L=-tQ.
$$

Only now reduce modulo $(1+i)A$. Both choices of $t$ belong to this
ideal, since $2=(1+i)(1-i)$. Hence $L\equiv0\pmod{1+i}$.

## Apply this to both products

For the $r_S$ family, use $t=2$. The cancellation gives

$$
\sum_{S\subseteq I}(-1)^{|S|}\frac{d_S-c_S}{2c_S}
=-2Q_r
\equiv0\pmod{1+i}
$$

for some $Q_r\in A$. For the $w_S$ family, use $t=1+i$:

$$
\sum_{S\subseteq I}(-1)^{|S|}\frac{g_S-c_S}{(1+i)c_S}
=-(1+i)Q_w
\equiv0\pmod{1+i}
$$

for some $Q_w\in A$. The quotients in these sums were formed as elements
of $A$ in Node 7.2; we are reducing those existing elements.

Reducing the original product equality first would lose the information:
every factor becomes $1$. We cannot divide by the residue of $t$,
because that residue is zero. Cancellation in $A$ is the step that
preserves the linear terms. The quotient ring $A/(1+i)A$ need not be a
field or a domain.

When $u=3$, each side has one factor, so both remainders vanish. The
two displayed sums are then exactly zero, agreeing with the common
rotation picture.

**Output.** Two alternating sums vanish modulo $1+i$ in the same ring.
They can now be added term by term.

Source: [the paper, Lemma 4.1 and its application after equation (4.10)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
