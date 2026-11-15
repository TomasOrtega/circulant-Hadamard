---
id: group-ring-encoding
title: Group-Ring Encoding
shortTitle: Group-Ring Encoding
summary: One polynomial records the first row; its product with its cyclic
  reversal records every dot product.
number: 1
draft: true
video: null
mapPosition:
  - 240
  - 24
mapSummary: '$h(X)h^*(X)=n$'
graphLayout: proof-map
graphTitle: Inside Node 1 · Group-Ring Encoding
children:
  - node: cyclic-group-ring
    dependsOn: []
    segment: null
    script: |
      Let $C_n=\langle X\mid X^n=1\rangle$. Its integer group ring is

      $$
      \mathbb Z[C_n]\cong\mathbb Z[X]/(X^n-1).
      $$

      The powers $1,X,\ldots,X^{n-1}$ mark the positions in a cyclic row.
      The relation $X^n=1$ makes the positions wrap around. Every element
      has a unique representative of degree less than $n$, so its
      coefficient list is unambiguous.

      Encode the first row $(h_0,\ldots,h_{n-1})$ by

      $$
      h(X)=\sum_{j=0}^{n-1}h_jX^j,\qquad h_j\in\{-1,1\}.
      $$

      Here $X$ is a formal position marker. For the order-four example
      with first row $(-1,1,1,1)$,

      $$
      h(X)=-1+X+X^2+X^3.
      $$
  - node: cyclic-shifts
    dependsOn:
      - cyclic-group-ring
    segment: null
    script: |
      Multiplication by $X$ shifts the coefficient list one position to
      the right. Reducing $X^n$ to $1$ gives

      $$
      Xh(X)=h_{n-1}+h_0X+\cdots+h_{n-2}X^{n-1}.
      $$

      Thus the rows of a circulant matrix correspond to
      $h(X),Xh(X),\ldots,X^{n-1}h(X)$. In our order-four example,

      $$
      Xh(X)=1-X+X^2+X^3,
      $$

      whose coefficients form the next row, $(1,-1,1,1)$.

      With rows numbered from $1$, row $j$ corresponds to $X^{j-1}h(X)$.
      With rows and columns numbered from $0$, the same rule is
      $H_{rj}=h_{j-r}$. All coefficient subscripts are reduced modulo $n$.
  - node: star-operation
    dependsOn:
      - cyclic-group-ring
    segment: null
    script: |
      Define the star operation by

      $$
      h^*(X)=h(X^{-1})=\sum_{j=0}^{n-1}h_jX^{-j}.
      $$

      This stays in the same group ring, since $X^{-1}=X^{n-1}$. Star reverses cyclic
      positions while leaving the coefficient at position zero fixed.
      It does not change the signs and is not the reciprocal $1/h(X)$.

      For four arbitrary coefficients, the reversal is

      $$
      (a,b,c,d)\longmapsto(a,d,c,b).
      $$

      Our fixed row $(-1,1,1,1)$ is symmetric under this reversal, so

      $$
      h^*(X)=h(X)=-1+X+X^2+X^3.
      $$
  - node: correlation-identity
    dependsOn:
      - star-operation
    contextFrom:
      - cyclic-group-ring
    segment: null
    script: |
      Multiplying by the reversed polynomial records all the cyclic dot
      products at once. For $0\leq a<n$,

      $$
      [X^a]\bigl(h(X)h^*(X)\bigr)=\sum_{j=0}^{n-1}h_jh_{j-a}.
      $$

      Here $[X^a]$ means the coefficient in the representative of degree
      less than $n$, and the subscripts are taken modulo $n$. The sum is
      the dot product of the first row with its $a$-step right shift.
      This coefficient identity holds for arbitrary integer coefficients.

      For the first row $(-1,1,1,1)$:

      | Shift $a$ | Right-shifted row | Dot product |
      | --- | --- | --- |
      | $0$ | $(-1,1,1,1)$ | $4$ |
      | $1$ | $(1,-1,1,1)$ | $0$ |
      | $2$ | $(1,1,-1,1)$ | $0$ |
      | $3$ | $(1,1,1,-1)$ | $0$ |

      Therefore $h(X)h^*(X)=4$ in $\mathbb Z[X]/(X^4-1)$: the constant coefficient is $4$
      and all other coefficients are zero.
  - node: hadamard-dictionary
    dependsOn:
      - cyclic-shifts
      - correlation-identity
    segment: null
    script: |
      > **Lemma (Circulant Hadamard Dictionary).** *Let $h(X)=\sum_{j=0}^{n-1}h_jX^j$
      > with every $h_j=\pm1$, and let $H$ be the circulant matrix whose first row is
      > $(h_0,\ldots,h_{n-1})$.
      > Then*
      >
      > $$
      > HH^{\mathsf T}=nI_n\quad\Longleftrightarrow\quad h(X)h^*(X)=n
      > \text{ in }\mathbb Z[X]/(X^n-1).
      > $$

      If the rows are orthogonal, the correlation identity makes every
      nonconstant coefficient zero. The constant coefficient is
      $\sum_j h_j^2=n$ because the coefficients are signs. Thus the
      product is the constant polynomial $n$.

      Conversely, that polynomial identity says the first row is
      orthogonal to every nontrivial shift. Any pair of distinct rows
      has the same dot product as the first row and one such shift, so
      all distinct rows are orthogonal. Because every coefficient $h_j$ is
      assumed to be $\pm1$, every matrix entry is $\pm1$ as well. Thus $H$ is
      Hadamard. The polynomial identity alone does not imply the sign condition.

      | Matrix language | Polynomial language |
      | --- | --- |
      | First row $(h_0,\ldots,h_{n-1})$ | $h(X)=\sum_jh_jX^j$ |
      | Shift right by one | Multiply by $X$ |
      | Row $j$, numbered from $1$ | $X^{j-1}h(X)$ |
      | Reverse cyclic positions | Replace $X$ by $X^{-1}$ |
      | Dot product with the $a$-step shift | $[X^a](h(X)h^*(X))$ |
      | Orthogonal rows, each with squared length $n$ | $h(X)h^*(X)=n$ |
---

Let $H$ be an $n\times n$ circulant matrix with entries $\pm1$, and encode
its first row $(h_0,\ldots,h_{n-1})$ by

$$
h(X)=\sum_{j=0}^{n-1}h_jX^j
\quad\text{in }\mathbb Z[X]/(X^n-1).
$$

Define $h^*(X)=h(X^{-1})$, which reverses cyclic positions.

> **Lemma (Circulant Hadamard Dictionary).** *The matrix $H$ is Hadamard
> if and only if*
>
> $$
> h(X)h^*(X)=n\quad\text{in }\mathbb Z[X]/(X^n-1).
> $$
>
> *Equivalently, $HH^{\mathsf T}=nI_n$ if and only if $h(X)h^*(X)=n$.*
>
> *Conversely, any polynomial $h(X)=\sum_{j=0}^{n-1}h_jX^j$ with all $n$
> coefficients $h_j=\pm1$ satisfying this identity determines a circulant
> Hadamard matrix by taking its coefficient list and successive cyclic right
> shifts as the rows.*

The right-hand side is the constant polynomial $n$. This identity translates
row orthogonality into a single equation in the group ring.
