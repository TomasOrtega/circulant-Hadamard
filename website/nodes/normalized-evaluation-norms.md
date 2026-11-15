---
id: normalized-evaluation-norms
title: Normalize the Norm Identities
shortTitle: Normalize the Norms
summary: Dividing each evaluated polynomial by two divides its product with its star by four.
number: "3.5"
draft: true
video: null
mapPosition: [240, 560]
mapSummary: '$4u^2\div4=u^2$'
---

## The normalized polynomials

Define

$$
\begin{aligned}
c(P)&=\frac{h(1,P)}2,\\
d(P)&=\frac{h(-1,P)}2,\\
g(P)&=\frac{h(i,P)}2.
\end{aligned}
$$

The parity step shows that $c(P),d(P)\in\mathbb Z[P]/(P^{u^2}-1)$ and
$g(P)\in\mathbb Z[i][P]/(P^{u^2}-1)$.

Evaluation preserves the norm identity, and star fixes the real scalar $2$.
Thus, for example,

$$
c(P)c^*(P)
=\frac{h(1,P)h^*(1,P)}4
=\frac{4u^2}{4}
=u^2.
$$

The same argument gives

$$
c(P)c^*(P)=d(P)d^*(P)=g(P)g^*(P)=u^2.
$$

For $g(P)$, star includes conjugation of its Gaussian-integer coefficients.

## The order-36 conclusion

When $u=3$, the scalar on the right is $36/4=9$. We have turned the
hypothetical Hadamard polynomial into three integral polynomials with the
same product identity.

Later we will evaluate these polynomials at roots of unity in $P$. For
example, at $P=1$ or $P=e^{2\pi i/3}$, their complex absolute values are $3$.

**Output.** Three norm-$u^2$ polynomials, supplying the inputs needed in the
following main nodes. See [the paper, Section 4, equations (4.1)–(4.2)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
