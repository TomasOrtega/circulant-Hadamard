# Video 1.2 — Multiplication is a cyclic shift

Goal: prove that the $j$-th row is represented by $X^{j-1}h$.

## Start from a coefficient row

Suppose we have an arbitrary row

$$
(h_0,h_1,\ldots,h_{n-1}).
$$

Encode it as

$$
h(X)=h_0+h_1X+\cdots+h_{n-1}X^{n-1}.
$$

Now multiply by $X$:

$$
Xh(X)=h_0X+h_1X^2+\cdots+h_{n-1}X^n.
$$

Because $X^n=1$, this becomes

$$
Xh(X)=h_{n-1}+h_0X+\cdots+h_{n-2}X^{n-1}.
$$

The coefficient list has changed from

$$
(h_0,h_1,\ldots,h_{n-1})\quad\text{to}\quad(h_{n-1},h_0,\ldots,h_{n-2}).
$$

That's one right cyclic shift.

*[Animation: Animate the last coefficient jumping to the first slot, and the other $n-1$ coefficients sliding right. Keep the polynomial and coefficient strip synchronized.]*

## Shift by any number of places

For our running example, $h(X)=-1+X+X^2+X^3$ and

$$
Xh(X)=1-X+X^2+X^3,
$$

which gives exactly the second row $(1,-1,1,1)$ of our original matrix.

*[Animation: Place the original four-by-four matrix next to the polynomial. Highlight the first row, multiply its polynomial by $X$, and highlight the unchanged second row $(1,-1,1,1)$.]*

The same reasoning works for any power $X^r$.

When we multiply $h$ by $X^r$, the coefficient of $X^j$ becomes $h_{j-r}$, with the subscript taken modulo $n$.

So $X^rh$ represents the original row shifted $r$ places to the right.

This immediately gives the entire circulant matrix. The first row is $h$, the second is $Xh$, the third is $X^2h$, and the $j$-th row is

$$
\text{row }j\quad\longleftrightarrow\quad X^{j-1}h.
$$

In particular, the $n$-th row corresponds to $X^{n-1}h$. One more multiplication returns us to

$$
X^nh(X)=h(X),
$$

so the cycle closes.

*[Animation: Construct the matrix row by row, labeling each with $h,Xh,X^2h,\ldots,X^{n-1}h$. Add an arrow from the final row back to $h$.]*

## A precise indexing formula

If rows and columns are labeled $0,\ldots,n-1$, then the entry of row $r$, column $j$ is

$$
H_{rj}=h_{(j-r)\bmod n}.
$$

This is simply another way to state the cyclic-shift rule. It will let us relate dot products of arbitrary rows to dot products with the first row.

*[Animation: Highlight a cell in row $r$, column $j$, then trace its value back to entry $j-r$ in the original row.]*

We have now translated the entire row structure into multiplication. But to understand a Hadamard matrix, we need to translate the dot products too.
