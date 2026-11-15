---
id: fold-and-divide
title: Fold the Cycle
shortTitle: Fold the Cycle
summary: Average opposite coefficients to halve the cycle while preserving oddness and dividing the scalar norm by four.
number: "2.5"
draft: false
video:
  src: media/fold-and-divide.mp4
  captions: media/fold-and-divide.vtt
  duration: 175.333333
mapPosition: [240, 420]
mapSummary: 'Halve length; divide norm by $4$'
---

> **Lemma (One fold).** *Suppose $T(X)$ has odd coefficients on a cycle
> of length $2^k$ and $T(X)T^*(X)=2^{2t}w^2$, with $t\geq2$ and $w$
> odd. Averaging opposite coefficients gives an integer polynomial
> $T_1(X)$ with odd coefficients on the cycle of length $2^{k-1}$ and*
>
> $$
> T_1(X)T_1^*(X)=2^{2(t-1)}w^2.
> $$

Node 2.4 gives $a_{j+2^{k-1}}\equiv a_j\pmod{2^t}$, hence modulo $4$.
Write $a_{j+2^{k-1}}=a_j+4r_j$. Then

$$
b_j:=\frac{a_j+a_{j+2^{k-1}}}{2}=a_j+2r_j
$$

is an odd integer. For instance, $3$ and $7$ average to $5$.

Let $q$ reduce exponents modulo $2^{k-1}$. Opposite coefficients add under
this ring map, so $q(T(X))=2T_1(X)$, where
$T_1(X)=\sum_jb_jX^j$. Projection commutes with star, giving

$$
4T_1(X)T_1^*(X)=q\bigl(T(X)T^*(X)\bigr)=2^{2t}w^2.
$$

The integer group ring is free as an abelian group, so equality can be
divided coefficientwise by $4$. This proves the new norm identity.

For the iteration, suppose $s\geq2$ and start with Node 2.3's polynomial
$T_0(X)$, with length $2^{2s}$ and norm $2^{2s}w^2$.
Inductively, after $j$ folds, for $0\leq j\leq s-1$,

$$
\begin{aligned}
\text{length of }T_j(X)&=2^{2s-j},\\
T_j(X)T_j^*(X)&=2^{2(s-j)}w^2,
\end{aligned}
$$

and all coefficients are odd. The case $j=0$ is the projection. If
$j<s-1$, then $t=s-j\geq2$, so the one-fold lemma applies and proves
the next case. After exactly $s-1$ folds, the length is $2^{s+1}$ and
the norm is $4w^2$. This is the endpoint used in Node 2.6.

Source: [the paper, Section 2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
