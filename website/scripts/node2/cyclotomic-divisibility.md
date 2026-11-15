# Video 2.4 — Compare Opposite Coefficients

## Slide 1 — The divisibility we need

Let $T(X)=\sum_{j=0}^{2^k-1}a_jX^j$ have integer coefficients on a
cycle of length $2^k$. Suppose

$$
T(X)T^*(X)=2^{2t}w^2,\qquad w\text{ odd}.
$$

We will show that opposite coefficients differ by a multiple of $2^t$:

$$
\boxed{2^t\mid a_j-a_{j+2^{k-1}}.}
$$

*[Animation: Draw a power-of-two cycle and connect opposite positions.
Label one pair $a_j,a_{j+2^{k-1}}$. Put the norm identity beside the
target divisibility; no assumption that these coefficients are signs
is needed for this lemma.]*

## Slide 2 — The cyclotomic input

Choose a primitive $2^k$th root $\xi$ and put $D=2^{k-1}$.
We use a standard cyclotomic fact, the specialization of Lemma 2.1
needed here. After allowing odd denominators, powers of $\xi-1$
measure divisibility by two through a valuation $v$, with $v(2)=1$.

The powers $1,\xi,\ldots,\xi^{D-1}$ form a basis, and

$$
v\!\left(\sum_{j=0}^{D-1}b_j\xi^j\right)\geq t
\quad\Longrightarrow\quad
2^t\mid b_j\text{ for integer }b_j.
$$

The basis comes from $\Phi_{2^k}(X)=X^D+1$. Its shift by one is
Eisenstein at two, and two is a unit times $(\xi-1)^D$. These standard
properties justify reading divisibility from the coefficients in this
basis. This is the cyclotomic input to our coefficient argument.

*[Animation: Show a row of the $D$ basis powers. Label the valuation
as a measure of powers of two, not a complex absolute value. Reveal
“valuation at least $t$” above the basis expression and “each coefficient
divisible by $2^t$” below it.]*

## Slide 3 — The norm determines the valuation

At $X=\xi$, star becomes complex conjugation:

$$
T(\xi)\overline{T(\xi)}=2^{2t}w^2.
$$

Conjugation preserves the valuation because it sends $\xi-1$ to the
unit multiple $-\xi^{-1}(\xi-1)$. The odd factor $w$ has valuation zero.
So the two factors on the left have equal valuations, whose sum is $2t$:

$$
2v(T(\xi))=2t,\qquad v(T(\xi))=t.
$$

*[Animation: Put identical valuation labels beneath $T(\xi)$ and its
conjugate. Replace the product by the sum of those labels. Cross out
only the valuation contribution of the odd factor $w^2$, leaving $2t$.]*

## Slide 4 — Opposite terms become differences

Because $\xi^D=-1$, the second half of the polynomial subtracts from
the first:

$$
T(\xi)=\sum_{j=0}^{D-1}(a_j-a_{j+D})\xi^j.
$$

We have now written the evaluation in the cyclotomic basis. Its valuation
is $t$, so the coefficient statement from Slide 2 gives
$2^t\mid a_j-a_{j+D}$ for every opposite pair. That proves our claim.

*[Animation: Move each term $a_{j+D}\xi^{j+D}$ underneath
$a_j\xi^j$. Replace $\xi^D$ by $-1$, combine the coefficients, and
apply the divisibility label to every resulting difference.]*

## Slide 5 — The order-16 illustration

For a hypothetical order-$16$ row, $t=2$ and the coefficients are signs.
Their differences are only $-2$, $0$, or $2$. The only one divisible
by four is zero, so $h_j=h_{j+8}$.

The eighth cyclic shift would repeat the row and have dot product $16$
with it, contradicting orthogonality. For the general descent, we keep
the divisibility conclusion even when the coefficients are larger odd
integers; that is what makes the folding step work.

*[Animation: Remove $-2$ and $2$ from the possible differences, leaving
zero. Superimpose the original row and its eight-step shift, then show
the conflicting dot products $16$ and $0$. Return to the general
opposite-pair divisibility for the next node.]*

Source: [the paper, Section 2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
