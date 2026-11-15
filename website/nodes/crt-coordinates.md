---
id: crt-coordinates
title: Chinese Remainder Coordinates
shortTitle: Split the Cycle
summary: Coprime cycle lengths let us label each position by a four-cycle coordinate and an odd-cycle coordinate.
number: "3.1"
draft: true
video: null
foundation: true
mapPosition: [240, 24]
mapSummary: '$4$-cycle $\times$ $u^2$-cycle'
---

## Statement

Since $u$ is odd, $\gcd(4,u^2)=1$. The Chinese remainder theorem gives

$$
C_{4u^2}\cong C_4\times C_{u^2}.
$$

A position $j$ is sent to $(j\bmod4,j\bmod u^2)$. Every pair occurs exactly
once, so this relabels the positions without changing their coefficients.

On group rings, the map sends $X$ to $ZP$. It identifies
$\mathbb Z[X]/(X^{4u^2}-1)$ with

$$
\mathbb Z[Z,P]/(Z^4-1,P^{u^2}-1).
$$

The two relations mean $Z^4=1$ and $P^{u^2}=1$. The map respects multiplication
and inversion, so it preserves $h(X)h^*(X)=4u^2$.

## The order-36 picture

For $u=3$, label each of the 36 positions by its residues modulo $4$ and $9$.
Position $1$ becomes $(1,1)$, position $4$ becomes $(0,4)$, and position $9$
becomes $(1,0)$. Thus $C_{36}\cong C_4\times C_9$.

**Output.** A two-variable polynomial $h(Z,P)$ encoding the same sign row.
The four groups are determined by residues, not by cutting the original row
into four consecutive blocks.
