# Video 1.5 — The Hadamard dictionary

Goal: prove both implications of $HH^{\mathsf T}=nI\Longleftrightarrow h(X)h^*(X)=n$.

## State the lemma precisely

Let $h_0,\ldots,h_{n-1}$ all be $+1$ or $-1$, and let $H$ be the circulant matrix whose first row is this sequence and whose successive rows are right cyclic shifts.

Set

$$
h(X)=\sum_{j=0}^{n-1}h_jX^j,\qquad h^*(X)=h(X^{-1}).
$$

Our claim is

$$
HH^{\mathsf T}=nI\quad\Longleftrightarrow\quad h(X)h^*(X)=n.
$$

The polynomial equation is in $\mathbb Z[X]/(X^n-1)$: its right-hand side is the constant polynomial $n$.

*[Animation: Put the matrix equation on the left and the group-ring equation on the right. Split the screen into two directions, each with a distinct arrow.]*

## Forward: Hadamard implies the polynomial identity

Suppose $H$ is Hadamard. Distinct rows are orthogonal, so the first row has dot product zero with every nontrivial cyclic shift.

By Video 1.4, those are precisely the nonconstant coefficients in $h(X)h^*(X)$. Every one of them is zero.

The constant coefficient is the dot product of the first row with itself:

$$
\sum_{j=0}^{n-1}h_j^2=n,
$$

because every $h_j$ is a sign. Thus the only surviving coefficient is $n$, and we get

$$
h(X)h^*(X)=n.
$$

*[Animation: Dim the coefficients of $X,X^2,\ldots,X^{n-1}$ one at a time. Keep the constant coefficient $n$ illuminated.]*

## Backward: the polynomial identity implies Hadamard

Now start with a polynomial $h(X)=\sum_{j=0}^{n-1}h_jX^j$ whose $n$ coefficients are all $+1$ or $-1$, and suppose $h(X)h^*(X)=n$ in our group ring. Form the circulant matrix from its coefficient list and the successive cyclic right shifts.

Because every element has a unique representative of degree less than $n$, this says that the coefficient of $X^a$ is zero for every $a\ne0$ among the residues $0,\ldots,n-1$.

So the first row is orthogonal to every one of its nontrivial cyclic shifts. Why does that give every pair of distinct rows?

The rows are all shifted copies of the same sequence. If row $r$ and row $s$ are compared, we can shift both back by $r$ positions without changing their dot product. What remains is the first row compared with its $(s-r)$-step shift.

In formulas, if we index rows and columns from zero,

$$
\begin{aligned}
\langle\operatorname{row}_r,\operatorname{row}_s\rangle
&=\sum_{j=0}^{n-1}h_{j-r}h_{j-s}\\
&=\sum_{k=0}^{n-1}h_kh_{k-(s-r)}.
\end{aligned}
$$

This is the coefficient of $X^{s-r}$ in $h(X)h^*(X)$, with exponents interpreted modulo $n$.

Thus, if $r\ne s$, the dot product is zero. If $r=s$, it is $n$. Therefore

$$
HH^{\mathsf T}=nI.
$$

All entries of this matrix are $\pm1$ by our starting assumption, so it is a circulant Hadamard matrix.

*[Animation: Highlight an arbitrary pair of rows $r,s$. Rotate both coefficient strips back by $r$ positions until the first becomes row zero; the offset $s-r$ remains unchanged. Then animate all off-diagonal dot products disappearing.]*

## Why the sign assumption matters

Notice that the coefficient identity itself did not require signs; it worked for arbitrary integer coefficients.

In the forward direction, the signs make the norm squared exactly $n$. In the backward direction, we need them to ensure that the matrix we construct has entries $\pm1$.

The equation alone cannot give us that. In dimension four, $h(X)=2$ satisfies $h(X)h^*(X)=4$ in $\mathbb Z[X]/(X^4-1)$. But its coefficient list is $(2,0,0,0)$, and the resulting matrix is $2I_4$. Its rows are orthogonal, but its entries are not all $\pm1$, so it is not Hadamard.

As a quick counterexample to confusing "circulant" with "Hadamard," take the all-ones row in dimension four. Then every cyclic shift is the same row, and

$$
(1+X+X^2+X^3)(1+X+X^2+X^3)=4(1+X+X^2+X^3),
$$

not $4$ in our group ring.

*[Animation: Show the all-ones matrix. The coefficient of every power is $4$, visually demonstrating why its rows are not orthogonal.]*

That finishes both directions. One polynomial equation is exactly equivalent to the original Hadamard condition for a circulant sign matrix.

In the next main node, we will ask what this equation says about $n$ itself.
