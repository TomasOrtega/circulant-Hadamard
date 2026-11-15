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

> **Lemma (Chinese remainder coordinates).** *For odd $u$, the map*
>
> $$
> j\longmapsto(j\bmod4,\ j\bmod u^2)
> $$
>
> *identifies $C_{4u^2}$ with $C_4\times C_{u^2}$. On group rings it
> sends $X$ to $ZP$ and gives*
>
> $$
> \mathbb Z[X]/(X^{4u^2}-1)
> \cong\mathbb Z[Z,P]/(Z^4-1,P^{u^2}-1).
> $$

Since $u$ is odd, $\gcd(4,u^2)=1$. If two positions have the same pair
of residues, their difference is divisible by both $4$ and $u^2$, hence
by $4u^2$. Thus the map is injective. Both sides have $4u^2$ elements,
so it is bijective, and addition of positions is respected.

Consequently the monomial $X^j$ becomes $Z^{j\bmod4}P^{j\bmod u^2}$.
Every pair of exponents occurs exactly once, so coefficients are relabeled
without being added or changed. Multiplication and inversion are preserved,
and therefore so is star. In particular,

$$
h(Z,P)h^*(Z,P)=4u^2
$$

is the image of the original norm identity.

For $u=3$, positions $1,4,9$ become $(1,1),(0,4),(1,0)$, respectively.
The four groups are determined by residues; they are not four consecutive
blocks cut from the original row.

Source: [the paper, Section 4, equations (4.1)–(4.2)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
