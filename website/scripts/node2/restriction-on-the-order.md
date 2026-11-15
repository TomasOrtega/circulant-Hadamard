# Video 2 — Restriction on the Order

## Slide 1 — Our goal: the order restriction

Our goal is to prove the order restriction: if a real circulant Hadamard
matrix has order greater than one, then its order must be four times the
square of an odd positive integer.

> **Order restriction.** If a real circulant Hadamard matrix has order $n>1$,
> then $n=4u^2$ for an odd positive integer $u$.

*[Animation: Highlight Node 2 on the main proof map, then bring the order
restriction onto the slide. Build the statement in three stages: $n$ is a
square; $n$ is even; and, after writing $n=4u^2$, $u$ is odd. Leave the full
statement visible as the goal, with its three parts highlighted in turn.]*

## Slide 2 — Recall the polynomial encoding

We saw that we can encode the first row of a circulant matrix by a
polynomial. For a row of signs, write

$$
h(X)=h_0+h_1X+\cdots+h_{n-1}X^{n-1},\qquad h_j=\pm1.
$$

The Hadamard condition implies

$$
h(X)h^*(X)=n
\qquad\text{in }\mathbb Z[X]/(X^n-1).
$$

*[Animation: Display a row of coefficient slots $h_0,h_1,\ldots,h_{n-1}$.
Move each coefficient into its term of $h(X)$. Beneath it, make a second
copy and reverse the exponents to form
$h^*(X)=h_0+h_1X^{-1}+\cdots+h_{n-1}X^{-(n-1)}$.
Pause the narration briefly while the star polynomial appears, giving
viewers time to follow the reversed exponents.
Bring the two polynomials together as $h(X)h^*(X)=n$, keeping the relation
$X^n=1$ visible. Use symbolic coefficients throughout this slide.]*

## Slide 3 — First restriction: the order is a square

We shall now plug in a value for $X$. In particular, choose $X=1$.

Reversing the powers in $h^*(X)$ does not change the value at one:
every power of one, including a negative power, is still one. Therefore

$$
h(1)=h^*(1)=h_0+h_1+\cdots+h_{n-1}.
$$

Substituting into the Hadamard identity gives

$$
n=h(1)h^*(1)=(h(1))^2
=\left(\sum_{j=0}^{n-1}h_j\right)^2.
$$

Since $h(1)$ is an integer, we have proved that $n$ is a square.

*[Animation: Keep the two expanded polynomials from Slide 2 and display
$X\mapsto1$. Replace each $X^j$ and $X^{-j}$ by $1$, leaving the
coefficients unchanged. Simplify each $h_j\cdot1$ to $h_j$, then align
the two identical sums and label them $h(1)=h^*(1)$. In the product
identity, show $n=h(1)h^*(1)$, replace the second factor by $h(1)$, and
combine the two equal factors into $(h(1))^2$. Finally write this as
$(\sum_{j=0}^{n-1}h_j)^2$ and highlight “$n$ is a square.” Keep the
calculation abstract; no particular matrix order is needed.]*

## Slide 4 — Second restriction: the square is even

We will now show that $n$ must be even. Because $n>1$, we can take two
different rows. Their dot product is zero.
Each term in that dot product is either $+1$ or $-1$.

For the total to be zero, there must be just as many positive terms as negative
terms. There are $n$ terms altogether, so $n$ is even.

We now have an even perfect square. Its square root must also be even: the
square of an odd integer would be odd. Write that even square root as $2u$.
Then

$$
n=(2u)^2=4u^2.
$$

*[Animation: Place two distinct rows one above the other. Multiply their
entries column by column to form the dot product, with each contribution
shown as $+1$ or $-1$. Pair each positive contribution with a negative
one; each pair sums to zero. Label the total number of terms $n$ and
highlight that it is even. Bring back $n=m^2$ with $m$ a positive integer,
then show $m=2u$ and $n=(2u)^2=4u^2$. At this stage label $u$ a positive
integer; its oddness is still to be established.]*

## Slide 5 — The deeper restriction: u is odd

There is one more part to the order restriction: $u$ must be odd.

This requires a deeper argument using the polynomial identity. We will
use that result here and give its proof when we zoom into Node 2.

Combining it with what we have just shown, we obtain the full conclusion:

$$
\boxed{n=4u^2,\qquad u\text{ an odd positive integer}.}
$$

*[Animation: Return to $n=4u^2$ and highlight the remaining condition
“$u$ is odd.” Briefly show the link into Node 2's smaller proof graph,
labelled “Proof of oddness,” then return to the statement and reveal
“$u$ odd.” Keep the deeper calculation off this slide.]*

## Slide 6 — Set up the contradiction

The case $u=1$ gives our known circulant Hadamard matrix of order $4$.

It remains to rule out $u>1$. We proceed by contradiction. Assume
that a circulant Hadamard matrix exists with

$$
n=4u^2,\qquad u>1\text{ odd}.
$$

The smallest possible value is $u=3$, giving $n=36$. We will use this
case as our guiding example for the remaining argument, while the
smaller nodes develop the proof for general odd $u>1$.

*[Animation: Return to the order restriction. Mark $u=1$, $n=4$ as the
known example, with $n=1$ beside it as the trivial case. Then display
“Assume for contradiction: a circulant Hadamard matrix of order $4u^2$
exists, with $u>1$ odd.” Highlight $u=3\Rightarrow n=36$ as the guiding
example and move the proof-map highlight from Node 2 to Node 3.]*
