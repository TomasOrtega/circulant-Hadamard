# Video 2.3 — Project to a Power-of-Two Cycle

## Slide 1 — Separate the power of two

We know $n=4u^2$. To understand how many factors of two are possible,
write

$$
u=2^{s-1}w,\qquad s\geq1,\quad w\text{ odd}.
$$

Then $n=2^{2s}w^2$. Our goal is to keep the power-of-two cycle while
collecting the odd part into its coefficients.

*[Animation: Factor $u$ into its power of two and its odd part. Carry
the same $u$ into $n=4u^2$ and show $n=2^{2s}w^2$. Highlight the cycle
length $2^{2s}$ and the group size $w^2$.]*

## Slide 2 — Collect equal residues

Reduce the exponent of each term of $h(X)$ modulo $2^{2s}$. The new
coefficient at position $r$ is

$$
a_r=\sum_{\ell=0}^{w^2-1}h_{r+\ell2^{2s}},
\qquad
T(X)=\sum_{r=0}^{2^{2s}-1}a_rX^r.
$$

Each coefficient adds exactly $w^2$ signs. Since that number is odd,
every $a_r$ is an odd integer. It need not still be a sign.

*[Animation: Use the hypothetical order-$36$ case to send the positions
$r,r+4,\ldots,r+32$ into one of four residue buckets. Count nine signs
in each bucket. Replace each bucket by its odd sum; do not assign
invented Hadamard coefficients.]*

## Slide 3 — The norm identity survives

This reduction of exponents is a ring map because $2^{2s}$ divides $n$.
It preserves multiplication and inversion, so it also preserves star.
Applying it to $h(X)h^*(X)=n$ gives

$$
T(X)T^*(X)=2^{2s}w^2
\quad\text{in }\mathbb Z[X]/(X^{2^{2s}}-1).
$$

The cycle has become shorter, but the scalar on the right stays the same.

*[Animation: Draw arrows from $h(X)$ to $T(X)$ and from $h^*(X)$ to
$T^*(X)$. Carry the product through the same map. Keep the scalar
$2^{2s}w^2$ fixed while the displayed cycle shrinks.]*

## Slide 4 — What we carry into the descent

We now have $2^{2s}$ odd coefficients satisfying the same product
identity. If $s\geq2$, the next steps will compare opposite coefficients
and repeatedly fold the cycle. Their contradiction will force $s=1$,
which is exactly the statement that our original $u$ is odd.

*[Animation: Label the new cycle “odd coefficients” and its norm
“$2^{2s}w^2$.” Mark pairs halfway around it, ready for the comparison
lemma. Keep $u=2^{s-1}w$ visible as the final goal.]*

Source: [the paper, Section 2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
