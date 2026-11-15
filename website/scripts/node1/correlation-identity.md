# Video 1.4 — A product that records every dot product

Goal: compute the coefficient of $X^a$ in $h(X)h^*(X)$ for general $n$.

## Expand the two polynomials

We have

$$
h(X)=\sum_{j=0}^{n-1}h_jX^j,\qquad h^*(X)=\sum_{k=0}^{n-1}h_kX^{-k}.
$$

Multiply them as ordinary sums:

$$
\begin{aligned}
h(X)h^*(X)&=\left(\sum_jh_jX^j\right)\left(\sum_kh_kX^{-k}\right)\\
&=\sum_{j,k}h_jh_kX^{j-k}.
\end{aligned}
$$

The only special rule is that the exponent $j-k$ is interpreted modulo $n$.

*[Animation: Expand a small $4\times4$ grid of pairwise products $h_jh_kX^{j-k}$. Color the cells by the exponent $j-k$ modulo four.]*

## Collect one coefficient at a time

Fix an exponent $a$. A term contributes to $X^a$ exactly when

$$
j-k\equiv a\pmod n.
$$

That is the same as $k\equiv j-a\pmod n$. So the coefficient of $X^a$ in $h(X)h^*(X)$ is

$$
[X^a](h(X)h^*(X))=\sum_{j=0}^{n-1}h_jh_{j-a}.
$$

Here $[X^a]F$ means "the coefficient of $X^a$ in the degree-less-than-$n$ representative of $F$."

Now look at the shifted row from Video 1.2. Its $j$-th entry is $h_{j-a}$. Thus the right-hand side is precisely the dot product of the first row with its $a$-step right shift.

*[Animation: Turn the terms carrying $X^a$ into two aligned coefficient rows, and show the multiplication and summation for the dot product.]*

## A four-dimensional check

For our original row $(-1,1,1,1)$, the four coefficients are

| $a$ | Right-shifted row | $[X^a](h(X)h^*(X))$ |
| --- | --- | --- |
| $0$ | $(-1,1,1,1)$ | $4$ |
| $1$ | $(1,-1,1,1)$ | $0$ |
| $2$ | $(1,1,-1,1)$ | $0$ |
| $3$ | $(1,1,1,-1)$ | $0$ |

Therefore

$$
h(X)h^*(X)=4+0X+0X^2+0X^3=4.
$$

*[Animation: Display the four shifted rows against the fixed first row. Compute each dot product; place the results $4,0,0,0$ as the coefficients of the product.]*

The formula we've proved is the heart of the dictionary:

$$
h(X)h^*(X)=\sum_{a=0}^{n-1}\left(\sum_{j=0}^{n-1}h_jh_{j-a}\right)X^a.
$$

Notice that the identity works for arbitrary integer coefficients. The extra assumption $h_j=\pm1$ will enter when we set the constant coefficient equal to $n$.
