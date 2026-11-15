# Video 1 — Group-Ring Encoding

## From the matrix to a polynomial

Example-first script. The main proof graph stops at the dictionary lemma.

## Opening: one row determines everything

Recall our original four-by-four circulant Hadamard matrix:

$$
H=\begin{pmatrix}
-1&1&1&1\\
1&-1&1&1\\
1&1&-1&1\\
1&1&1&-1
\end{pmatrix}.
$$

The first row determines every row: each row is obtained by shifting the preceding row one position to the right.

Throughout this series, we will keep the original first row

$$
(-1,1,1,1).
$$

*[Animation: Show the familiar $4\times4$ matrix. Highlight its original first row $(-1,1,1,1)$; do not rearrange the rows. Animate the circular movement that produces each subsequent row.]*

Our goal is to replace this matrix by a single algebraic object that remembers all its cyclic shifts.

## One polynomial for the first row

Take the entries of the first row and use them as the coefficients of a polynomial:

$$
h(X)=-1+X+X^2+X^3.
$$

We will work with polynomials where $X^4=1$. So after a power reaches four, it wraps around.

More generally, in dimension $n$ we use the ring

$$
\mathbb Z[C_n]\cong\mathbb Z[X]/(X^n-1).
$$

The group ring is just a way to keep track of cyclic positions algebraically.

*[Animation: Pull the original row $(-1,1,1,1)$ into the coefficients of $-1+X+X^2+X^3$. Draw four slots labeled $1,X,X^2,X^3$ around a circle; place $X^4=1$ in the middle.]*

## Multiplication is a shift

Watch what happens when we multiply by $X$:

$$
Xh(X)=-X+X^2+X^3+X^4=1-X+X^2+X^3.
$$

The four coefficients changed from $(-1,1,1,1)$ to $(1,-1,1,1)$. That's exactly a cyclic shift one position to the right!

Multiply by $X$ again, and we get the next row. Keep going, and we get all the rows of the matrix. In fact, the $j$-th row corresponds to $X^{j-1}h(X)$, and after the $n$-th row, multiplying by $X$ takes us right back to the beginning.

*[Animation: Move the rightmost coefficient into the leftmost slot every time an $X$ appears. Stack successive coefficient rows into a matrix, and close the loop at $X^nh(X)=h(X)$.]*

So we can describe every row just by multiplying our original polynomial by powers of $X$.

## Reversing the circle

But a Hadamard matrix isn't just about shifts. It's about dot products between shifts. How do we encode those?

Introduce a new operation, called star. We replace $X$ by $X^{-1}$:

$$
h^*(X)=h(X^{-1}).
$$

Visually, this keeps the constant coefficient fixed and reverses the circular order of the other coefficients.

To see this reversal clearly, imagine four arbitrary coefficients:

$$
a+bX+cX^2+dX^3\longmapsto a+dX+cX^2+bX^3.
$$

For our actual example, the last three coefficients happen to be equal. So the reversal leaves it unchanged:

$$
h(X)=-1+X+X^2+X^3,\qquad h^*(X)=h(X).
$$

*[Animation: First reflect a generic four-position coefficient circle $(a,b,c,d)$ into $(a,d,c,b)$, keeping $a$ fixed. Then restore the original signs $(-1,1,1,1)$ and show that this symmetric row stays unchanged.]*

## One product contains the dot products

Now multiply the polynomials $h(X)$ and $h^*(X)$ in the group ring.

Here comes the key observation: the coefficient of each power $X^a$ is the dot product of the first row with the row shifted $a$ positions.

For the constant term, we are taking the dot product of the row with itself:

$$
(-1)^2+1^2+1^2+1^2=4.
$$

For the coefficient of $X$, we compare the first row with its one-step shift:

$$
(-1,1,1,1)\cdot(1,-1,1,1)=-1-1+1+1=0.
$$

Exactly the same cancellation happens for the two-step and three-step shifts.

*[Animation: Show four labeled slots $1,X,X^2,X^3$. For each slot, turn it into a dot-product calculation. Keep the constant result $4$ and dim the three zeros. Do not show the double sum yet.]*

So the whole product collapses to

$$
h(X)h^*(X)=4.
$$

One equation has encoded every orthogonality condition for our four-by-four example.

## The general dictionary

What we've seen is not peculiar to dimension four. The same construction works for any circulant sign matrix.

Start with the first row $(h_0,\ldots,h_{n-1})$, where every entry is $+1$ or $-1$. Turn it into the polynomial $h(X)=\sum_{j=0}^{n-1}h_jX^j$, and define $h^*(X)=h(X^{-1})$.

For this circulant matrix with entries $\pm1$, the Hadamard condition becomes

$$
HH^{\mathsf T}=nI\quad\Longleftrightarrow\quad h(X)h^*(X)=n.
$$

The right-hand equation is an equality in $\mathbb Z[X]/(X^n-1)$. We multiply the two polynomials, reduce powers using $X^n=1$, and obtain the constant polynomial $n$.

The converse matters too. Start with a polynomial whose $n$ coefficients, in positions $1,X,\ldots,X^{n-1}$, are all $+1$ or $-1$, and suppose $h(X)h^*(X)=n$. The product's nonconstant coefficients vanish, so the first row is orthogonal to every nontrivial cyclic shift. Any two distinct cyclic rows have the same dot product as the first row and one such shift, so they are mutually orthogonal. Since all their entries are already $\pm1$, these rows form a circulant Hadamard matrix.

That sign condition is part of the dictionary: the polynomial equation gives orthogonality, but it does not by itself force the coefficients to be $\pm1$.

*[Animation: Place the matrix equation and the group-ring equation on opposite sides of the screen. Animate a double arrow. Beneath it, reveal a small "Open proof" symbol pointing to subnodes 1.1–1.5.]*

This is our first dictionary: a problem about many rows becomes a single polynomial equation. In the next main node, we'll use that equation to restrict the possible size of the matrix.
