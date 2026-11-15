---
id: hadamard-dictionary
title: Hadamard Dictionary
shortTitle: Hadamard Dictionary
summary: The polynomial identity and the circulant Hadamard condition imply one another.
number: "1.5"
draft: true
video: null
mapPosition:
  - 240
  - 500
mapSummary: HHᵀ = nI ⇔ h(X)h*(X) = n
---

## The dictionary lemma

Let $h_0,\ldots,h_{n-1}\in\{-1,1\}$ and let $H$ be the circulant matrix formed by their successive cyclic right shifts. Set $h(X)=\sum_jh_jX^j$ in $\mathbb Z[X]/(X^n-1)$ and define $h^*(X)=h(X^{-1})$.

> **Lemma (Circulant Hadamard Dictionary).** *The matrix $H$ is Hadamard if and only if $h(X)h^*(X)=n$ in this group ring. Equivalently,*
>
> $$
> HH^{\mathsf T}=nI_n\quad\Longleftrightarrow\quad h(X)h^*(X)=n.
> $$

## Forward implication

Suppose $HH^{\mathsf T}=nI_n$. The first row is orthogonal to each nontrivial cyclic shift. By the coefficient identity, every nonconstant coefficient of $h(X)h^*(X)$ is zero. The constant coefficient is

$$
[X^0](h(X)h^*(X))=\sum_{j=0}^{n-1}h_j^2=n,
$$

because each $h_j$ is a sign. Hence $h(X)h^*(X)=n$.

## Reverse implication

Suppose $h(X)=\sum_{j=0}^{n-1}h_jX^j$ has all $n$ coefficients $h_j=\pm1$ and satisfies $h(X)h^*(X)=n$ in this group ring. Form $H$ from the coefficient list and its successive cyclic right shifts. Uniqueness of the degree-less-than-$n$ representative makes every nonconstant coefficient zero. Therefore the first row is orthogonal to each nontrivial cyclic shift.

To compare any two rows, number rows and columns from zero. The cyclic-shift formula gives

$$
\begin{aligned}
\langle\operatorname{row}_r,\operatorname{row}_s\rangle
&=\sum_{j=0}^{n-1}h_{j-r}h_{j-s}\\
&=\sum_{k=0}^{n-1}h_kh_{k-(s-r)}\\
&=[X^{s-r}](h(X)h^*(X)),
\end{aligned}
$$

where the exponent and subscripts are interpreted modulo $n$. This is zero when $r\ne s$ and $n$ when $r=s$. Consequently $HH^{\mathsf T}=nI_n$. Every entry of $H$ is $\pm1$ by the coefficient assumption, so $H$ is a circulant Hadamard matrix.

## Why the hypotheses matter

The coefficient formula works for arbitrary integers. Signs guarantee that the row norm squared is $n$ in the forward direction and that the constructed matrix has entries $\pm1$ in the converse. The polynomial identity alone does not force sign coefficients: $h(X)=2$ satisfies $h(X)h^*(X)=4$ in $\mathbb Z[X]/(X^4-1)$, but its coefficient list $(2,0,0,0)$ gives $H=2I_4$, which is not Hadamard.

Signs and cyclic structure alone do not imply orthogonality either. For example, the all-ones row at order four gives

$$
(1+X+X^2+X^3)^2=4(1+X+X^2+X^3)\ne4
$$

in $\mathbb Z[X]/(X^4-1)$.

**Output.** Both directions of the equivalence are established. The next main node uses the resulting equation to restrict the order.
