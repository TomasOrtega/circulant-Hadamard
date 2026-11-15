# Video 3.1 — Chinese Remainder Coordinates

## Slide 1 — Split the position into two coordinates

We have order $n=4u^2$ with $u$ odd. Our goal is to describe the same
cycle using a four-position coordinate and a $u^2$-position coordinate:

$$
j\longmapsto(j\bmod4,\ j\bmod u^2).
$$

Because $4$ and $u^2$ are coprime, the Chinese remainder theorem says
that this gives a bijection.

*[Animation: Start with a single labeled position $j$ on the long cycle.
Send it to two residue dials, one with four positions and one with
$u^2$ positions. For $u=3$, show $j=1,4,9$ mapping to
$(1,1),(0,4),(1,0)$.]*

## Slide 2 — Why no positions are lost

If two positions have the same pair of residues, their difference is
divisible by both $4$ and $u^2$. Coprimality makes it divisible by
$4u^2$, so they were already the same position on the original cycle.

The two descriptions each contain $4u^2$ positions. Thus every pair
occurs exactly once. Addition of positions is preserved, giving

$$
C_{4u^2}\cong C_4\times C_{u^2}.
$$

*[Animation: Show two positions feeding into the same pair. Mark their
difference as a multiple of both lengths, hence of the full length.
Then compare the counts $4u^2$ and $4\times u^2$ to complete the bijection.]*

## Slide 3 — Translate the polynomial

Introduce $Z$ and $P$ for the two coordinates. The generator $X$ maps
to $ZP$, so $X^j$ becomes $Z^jP^j$, with exponents reduced separately.
We now work in

$$
\mathbb Z[Z,P]/(Z^4-1,P^{u^2}-1).
$$

Every sign keeps its own position under this relabeling; no signs are
added. The map preserves multiplication and inversion, hence also star.
Our identity therefore becomes

$$
h(Z,P)h^*(Z,P)=4u^2.
$$

*[Animation: Transform $h_jX^j$ into $h_jZ^jP^j$, leaving the sign
$h_j$ attached. Reduce the two exponents on their own dials. Carry the
norm identity through the coordinate change and finish with the two
relations $Z^4=1$ and $P^{u^2}=1$.]*

Source: [the paper, Section 4, equations (4.1)–(4.2)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
