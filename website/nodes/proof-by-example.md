---
id: proof-by-example
title: "Proof by Example: n = 36"
shortTitle: Order 36
summary: "The first complete route: two evaluations, one common rotation, and a
  contradiction."
supplemental: true
draft: true
---

Assume a circulant Hadamard matrix of order 36 exists. The following route derives a contradiction, accepting the Δ-theorem. It is a proof of this case, not by itself a proof for every order.

1. Assume $h(Z,P)h^*(Z,P)=36$ in the group ring with $Z^4=P^9=1$ and 36 sign coefficients. Define $c(P)=h(1,P)/2$, $d(P)=h(-1,P)/2$, $g(P)=h(i,P)/2$. Then $cc^*=dd^*=gg^*=9$.
2. Put $\omega=e^{2\pi i/3}$. The Δ-theorem says $\Delta(f)=f(1)/f(\omega)$ has odd order for each norm-9 element $f=c,d,g$.
3. Set
   $$
   R=\frac{d(1)/c(1)}{d(\omega)/c(\omega)},\quad
   W=\frac{g(1)/c(1)}{g(\omega)/c(\omega)}.
   $$
   Signs imply $R\equiv W\equiv1$ modulo $1+i$, hence odd-order rigidity gives $R=W=1$.
4. Put $\lambda=c(\omega)/c(1)$. Then
   $$
   (c(\omega),d(\omega),g(\omega))
   =\lambda(c(1),d(1),g(1)),\qquad |\lambda|=1.
   $$
   **Geometric interpretation:** The triple $(c,d,g)$, with all three points on the radius-3 complex circle, rotates rigidly by the same angle. $R,W$ measure *relative* distortions of the rotation; their value 1 means none.
5. Because $E$ is a fixed linear combination of $c,d,g$, $E(\omega)=\lambda E(1)$. But the signs give $E(P)\equiv1+P+\cdots+P^8$. Thus $E(1)\equiv9\equiv1$, while $E(\omega)\equiv3(1+\omega+\omega^2)=0$.
6. $\lambda$ is invertible modulo $1+i$, since the norm of $c(\omega)$ is 9 and $c(1)=\pm3$. Multiplication by a unit cannot turn a nonzero residue into zero. Contradiction.

**Complex equality versus congruence:** The $J$-arrow cancellation illustrates the *reduction* of $E$'s coefficients. It does not assert that $E(\omega)=0$ as a complex number, or that divisibility by $1+i$ geometrically means a $45^\circ$ direction.

## Arithmetic setting

Work in $\mathbb Z[i,\omega,1/3]$ modulo the ideal $(1+i)$. This is a nonzero ring of characteristic two. Every denominator above is a unit since its product with its complex conjugate is $9$. Divisions by $2$ and $1+i$ are formed in characteristic zero from the sign divisibilities, before reducing.

## Continue

[Read the general odd-$u$ proof](../general-proof/index.html) and explore its eight-step proof map. Video scripts and internal proof graphs are still to come.
