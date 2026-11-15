# The Circulant Hadamard Conjecture
### Video 0 — Introduction and Proof Roadmap

## Part 1 — A Special Matrix

*[Animation: A blank \(4\times4\) grid appears. Fill the diagonal entries with \(-1\), and every other entry with \(+1\).]*

Consider the following \(4\times4\) matrix.

We put negative ones along the diagonal and fill every other entry with positive ones.

\[
H=
\begin{pmatrix}
-1&1&1&1\\
1&-1&1&1\\
1&1&-1&1\\
1&1&1&-1
\end{pmatrix}.
\]

This matrix has a rather special property: every row is perpendicular to every other row.

To see this, let's take the dot product of any two different rows.

*[Animation: Highlight two rows. Multiply the corresponding entries, producing two \(-1\)'s and two \(+1\)'s.]*

There are exactly two positions where the signs disagree, each contributing negative one, and two positions where the signs agree, each contributing positive one.

Thus, their dot product is zero.

And this works for every pair of distinct rows.

Furthermore, since every entry is either positive or negative one, the squared length of each row is exactly four.

We can combine these observations into one equation:

\[
HH^{\mathsf T}=4I.
\]

*[Animation: Multiply the matrix by its transpose. The off-diagonal entries cancel, leaving four along the diagonal.]*

Matrices with entries positive or negative one whose rows are mutually orthogonal are called **Hadamard matrices**.

Now, we could ask whether there are other \(4\times4\) matrices with this property.

We can certainly construct some by permuting the rows or columns of our matrix, or by changing all the signs in any row or column.

Each of these operations preserves orthogonality.

*[Animation: Rearrange rows and columns and flip signs. The matrix changes while the equation \(HH^{\mathsf T}=4I\) remains on screen.]*

In fact, every \(4\times4\) Hadamard matrix can be obtained from our example through these operations.

But what happens in other dimensions?

## Part 2 — The Hadamard Conjecture

For which positive integers \(n\) can we construct an \(n\times n\) matrix whose entries are all positive or negative one, satisfying

\[
HH^{\mathsf T}=nI?
\]

When \(n=1\), the problem is trivial. We can simply take the matrix whose only entry is one.

When \(n=2\), we can also construct such a matrix.

For larger dimensions, one can show that \(n\) must be divisible by four.

The famous **Hadamard conjecture** asserts that this condition is also sufficient: a Hadamard matrix should exist in every dimension divisible by four.

Remarkably, this conjecture remains open today.

*[Animation: Display dimensions \(1,2,4,8,12,16,20,\ldots\), highlighting the multiples of four.]*

But let's return to our original matrix.

It has another curious property that we haven't mentioned.

Look at the first row.

If we shift every entry cyclically one position to the right, we obtain the second row.

If we shift again, we obtain the third row.

And one more shift gives us the fourth row.

*[Animation: Arrange the entries of the first row around a circle. Rotate the entries one position at a time, with each rotation generating another row of the matrix.]*

Thus, **the entire matrix is determined by its first row!**

Matrices with this property are called **circulant matrices**.

And this leads us to a much more restrictive version of Hadamard's original problem.

In 1963, Ryser conjectured that if we demand this additional cyclic symmetry, then the only possible dimensions are one and four.

This became known as the **circulant Hadamard conjecture**.

*[Animation: Display a large circulant matrix, emphasizing the repeating cyclic pattern. Then highlight the conjecture \(n=1\) or \(n=4\).]*

For more than sixty years, this conjecture remained unsolved.

Then, on October 6, 2026, OpenAI publicly released a proof.

Our goal is to understand how such a simple question about matrices with positive and negative ones can be answered using some surprisingly beautiful ideas from algebra and number theory.

---

## Part 3 — The Proof Dependency Graph

*[Animation: The full eight-node proof dependency graph appears below the video.]*

We have broken the proof into eight main mathematical components, which you can see in the graph below.

Each node represents a step in the proof. We will explore each of these in a separate video, and you can zoom into any node to reveal a more detailed proof dependency graph.

But first, let's get a bird's-eye view of how all these ideas fit together.

### Node 1 — Group-Ring Encoding

*[Highlight Node 1.]*

We begin by introducing the **group ring**, an algebraic tool that allows us to encode the cyclic nature of our matrix.

Using this, we will turn all the orthogonality conditions into a single algebraic equation.

### Node 2 — Restriction on the Order

*[Highlight Node 2.]*

Next, we use this algebraic formulation to restrict the possible dimensions of a circulant Hadamard matrix.

In particular, we will show that the dimension must be four times an odd square:

\[
n=4u^2,\qquad u\text{ odd}.
\]

Thus, to prove our theorem, it will remain to show that \(u=1\).

### Node 3 — The Three Evaluations

*[Highlight Node 3.]*

We now assume that our matrix has dimension \(4u^2\), where \(u\) is odd.

We separate its cyclic structure into a part of size four and a part of odd size.

Using this, we construct a polynomial from our matrix and evaluate it at three special values: \(1\), \(-1\), and \(i\).

This produces three new polynomials, which we call \(c\), \(d\), and \(g\).

Remarkably, all three inherit the same important algebraic identity from our original matrix.

*[Animation: The original polynomial splits into three branches labeled \(c\), \(d\), and \(g\).]*

### Node 4 — The Δ-Theorem

*[The proof graph branches. Highlight Node 4 on the right.]*

Here, we temporarily forget about our original matrix and prove a much more general theorem.

We show that whenever a polynomial satisfies a certain algebraic identity, we can construct a special product of its values at roots of unity, and this product must itself be a root of unity of odd order.

The crucial observation is that **all three polynomials we constructed in Node 3 satisfy the conditions of this theorem**.

This is the main number-theoretic ingredient of the proof.

### Node 5 — Signs Become All Ones

*[Highlight Node 5 on the other branch.]*

Meanwhile, we return to our three polynomials \(c\), \(d\), and \(g\).

Our goal is to combine them into one new polynomial, which we will call \(E(P)\), whose special properties will eventually give us our contradiction.

The remarkable observation is that, because every entry of our original matrix was either positive or negative one, the coefficients of this new polynomial all become one when we reduce modulo \(1+i\).

In other words, after this reduction, we are left with a polynomial whose coefficients are all ones.

*[Animation: The coefficients of \(E(P)\) simplify until they all become \(1\).]*

### Node 6 — Odd-Order Rigidity

*[The two branches converge at Node 6.]*

Now we bring these two ideas together.

We apply the general theorem from Node 4 to the three polynomials constructed in Node 3.

This gives us certain roots of unity of odd order.

But the special properties coming from the original signs tell us that these same numbers must be congruent to one modulo \(1+i\).

And we show that **the only way both properties can hold is if these numbers are actually equal to one**.

This gives us some surprisingly rigid relationships between our three polynomials.

### Node 7 — From Products to Sums

*[Highlight Node 7.]*

Next, we take these relationships, which involve products of numbers, and turn them into relationships involving sums.

In particular, we show that a certain alternating sum involving our polynomial \(E(P)\) must be congruent to zero modulo \(1+i\).

*[Animation: Display a symbolic sum \(\mathcal S\), then reveal \(\mathcal S\equiv0\pmod{1+i}\).]*

This is the key relationship that will lead to our contradiction.

### Node 8 — The Final Contradiction

*[Highlight Node 8.]*

Finally, we use the fact that the coefficients of \(E(P)\) are all congruent to one modulo \(1+i\).

When we evaluate at nontrivial roots of unity, these ones cancel. But when we substitute \(P=1\), we are adding an **odd number of ones**, which is not zero modulo \(1+i\).

*[Animation: Show the roots of unity arranged around a circle, with their contributions canceling. Then substitute \(P=1\), where all the terms point in the same direction and their number is odd.]*

This forces the alternating sum from Node 7 to be nonzero modulo \(1+i\).

But Node 7 told us that this sum must be zero!

*[Animation: Display the two conclusions side by side.]*

\[
\mathcal S\equiv0\pmod{1+i}
\]

\[
\mathcal S\equiv1\pmod{1+i}
\]

A contradiction.

Thus, \(u\) cannot be greater than one, and we conclude that the only possible dimensions of a circulant Hadamard matrix are

\[
\boxed{n=1\quad\text{or}\quad n=4.}
\]

*[Animation: All eight nodes illuminate, with the final theorem appearing beneath the graph.]*
