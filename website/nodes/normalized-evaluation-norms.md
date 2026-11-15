---
id: normalized-evaluation-norms
title: Normalize the Norm Identities
shortTitle: Normalize the Norms
summary: Dividing each evaluated polynomial by two divides its product with its star by four.
number: "3.5"
draft: false
video:
  src: media/normalized-evaluation-norms.mp4
  poster: media/thumbnails/normalized-evaluation-norms.jpg
  captions: media/normalized-evaluation-norms.vtt
  duration: 138.566667
mapPosition: [240, 560]
mapSummary: '$4u^2\div4=u^2$'
---

> **Lemma (Three normalized norm solutions).** *Define*
>
> $$
> \begin{aligned}
> c(P)&=\frac{h(1,P)}2,\\
> d(P)&=\frac{h(-1,P)}2,\\
> g(P)&=\frac{h(i,P)}2.
> \end{aligned}
> $$
>
> *Then $c(P),d(P)$ have integer coefficients, $g(P)$ has
> Gaussian-integer coefficients, and*
>
> $$
> c(P)c^*(P)=d(P)d^*(P)=g(P)g^*(P)=u^2
> $$
>
> *in $\mathbb Z[i][P]/(P^{u^2}-1)$.*

Two independent facts meet here. Node 3.3 shows that each evaluated
polynomial has norm $4u^2$. Node 3.4 shows its coefficients can be
divided by two in the required integer ring.

Star fixes the real number $2$. Therefore division of the polynomial
by two also divides its star by two, and, for example,

$$
c(P)c^*(P)
=\frac{h(1,P)\bigl(h(1,P)\bigr)^*}{4}
=u^2.
$$

The identical calculation works for $d(P)$ and $g(P)$. For $g(P)$,
star includes complex conjugation of its Gaussian-integer coefficients.
This proves all three identities without assuming their coefficients
are still signs.

For any $u^2$th root of unity $\zeta$, evaluation turns star into complex
conjugation. Thus each of the three values has absolute value $u$:

$$
|c(\zeta)|=|d(\zeta)|=|g(\zeta)|=u.
$$

In the guiding case $u=3$, dividing by two changes the norm from $36$
to $9$, and the evaluated values lie on the circle of radius three.
The condition $\zeta^{u^2}=1$ is essential: these are the inputs allowed
by the group-ring relation.

Source: [the paper, Section 4, equations (4.1)–(4.2)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
