# Video 8.5 — Only Orders One and Four

## Slide 1 — State the conclusion

Our goal is to finish both directions of the theorem.

> **Theorem (Circulant Hadamard).** A real circulant Hadamard matrix
> of positive integer order $n$ exists if and only if $n\in\{1,4\}$.

We have excluded the other orders. To complete an “if and only if”
statement, we must also check that both remaining orders occur.

*[Animation: Display the theorem in a box. Beneath it, create two
panels: “exclude every other order” and “verify orders $1$ and $4$.”
Keep both panels visible until the corresponding work is complete.]*

## Slide 2 — Combine the order restriction with the contradiction

If $n>1$, Node 2 gives

$$
n=4u^2,\qquad u\text{ a positive odd integer}.
$$

The general contradiction excludes every $u>1$. Thus $u=1$ and
$n=4$. The order-one case was outside the hypothesis $n>1$ of the
order restriction, so it remains to be checked separately.

*[Animation: Pass an order $n>1$ through the order-restriction card
and then the contradiction card. Remove $u>1$, leaving $u=1$ and
$n=4$. Bring in $n=1$ on a separate path that bypasses the restriction.]*

## Slide 3 — Verify the order-one example

At order one, use $(1)$. Its entry is a sign, its only row has squared
length one, and there are no distinct rows whose inner product must
be checked. Cyclic shifting fixes the row. Thus this matrix is
circulant and satisfies $HH^{\mathsf T}=I_1$.

*[Animation: Show the single entry $1$, apply a cyclic shift that leaves
it fixed, and multiply $(1)$ by its transpose. Mark the order-one
example as verified.]*

## Slide 4 — Verify the order-four example

At order four, return to

$$
H=\begin{pmatrix}
-1&1&1&1\\
1&-1&1&1\\
1&1&-1&1\\
1&1&1&-1
\end{pmatrix}.
$$

Every row is the cyclic right shift of the preceding row. Any two
distinct rows agree in two positions and disagree in two positions,
so their dot product is zero. Each row has squared length four.
Therefore $HH^{\mathsf T}=4I_4$.

Both remaining orders occur. The order-four example corresponds to
$u=1$, outside the earlier Δ-theorem's hypothesis, so it is consistent
with the contradiction. This completes the proof chain, using the
stated inputs developed in the earlier nodes.

*[Animation: Cycle the first row through all four rows. Select two
rows, mark two agreements and two disagreements, and sum their dot
product to zero. Fill the diagonal of $HH^{\mathsf T}$ with fours
and its other entries with zeros. Mark both existence checks and
return to the boxed theorem.]*

Detailed exposition: [Node 8.5](../../nodes/theorem.md).
Source: the paper, Theorem 1.1, Section 4, and Remark 4.2.
