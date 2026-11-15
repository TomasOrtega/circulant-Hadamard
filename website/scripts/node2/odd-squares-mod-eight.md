# Video 2.6 — Odd Squares Modulo 8

## Slide 1 — Read the constant coefficient

Assume $s\geq2$. The descent leaves $2^{s+1}$ odd coefficients
$b_j$ and a polynomial whose product with its star is $4w^2$.
The constant coefficient of that product is the sum of the squares:

$$
\sum_{j=0}^{2^{s+1}-1}b_j^2=4w^2.
$$

Our goal is to show that this integer equation is impossible.

*[Animation: Multiply the final polynomial by its star. Highlight
exactly the terms $b_jX^j\cdot b_jX^{-j}$ that contribute to the
identity position. Collect them into the displayed sum of squares.]*

## Slide 2 — Compare residues modulo eight

For an odd integer $b=2r+1$,

$$
b^2=4r(r+1)+1\equiv1\pmod8,
$$

because one of $r,r+1$ is even. Every square on the left therefore
contributes one modulo eight. There are $2^{s+1}$ terms, a multiple
of eight when $s\geq2$, so the left side has residue zero.

But $w$ is odd, giving $4w^2\equiv4\pmod8$. Zero cannot equal four.

*[Animation: Replace each odd square by its residue $1$. Group the
$2^{s+1}$ ones into blocks of eight, each with residue zero. On the
right, use $w^2\equiv1\pmod8$ to leave $4$. Show the conflict $0\ne4$.]*

## Slide 3 — Recover the original u

The assumption $s\geq2$ fails. Since $s\geq1$, we must have $s=1$.
Return to the notation from the beginning:

$$
u=2^{s-1}w=w.
$$

Thus the original $u$ is odd, and we have proved the order restriction

$$
\boxed{n=4u^2,\qquad u\text{ odd}.}
$$

The order-four example survives. The remaining proof will assume
$u>1$ and exclude those candidates.

*[Animation: Replace $s$ by $1$ in $u=2^{s-1}w$ and in
$n=2^{2s}w^2$. Restore the name $u$ for the odd parameter and highlight
the completed order-restriction node.]*

Source: [the paper, Section 2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
