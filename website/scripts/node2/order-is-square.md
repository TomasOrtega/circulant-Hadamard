# Video 2.1 — Evaluate at 1

## Slide 1 — Our goal: the order is a square

Let $h(X)=\sum_{j=0}^{n-1}h_jX^j$ encode the first row of a circulant
Hadamard matrix. We know that

$$
h(X)h^*(X)=n
\quad\text{in }\mathbb Z[X]/(X^n-1).
$$

Our goal is to turn this polynomial equation into an ordinary integer
square. We do that by choosing $X=1$.

*[Animation: Display the first-row signs above their terms $h_jX^j$.
Bring the terms together as $h(X)$, then place the norm identity beneath
it. Highlight the substitution $X=1$.]*

## Slide 2 — Every power becomes one

This substitution respects $X^n=1$. It also makes reversing powers
irrelevant: every $1^j$ and $1^{-j}$ is one. Thus

$$
h(1)=\sum_jh_j=h^*(1).
$$

Evaluating the product now gives

$$
n=h(1)h^*(1)=h(1)^2.
$$

*[Animation: Expand $h(X)$ and $h^*(X)$ side by side. Replace each
positive and negative power of $X$ by $1$. Align the two identical sign
sums, then turn their product into a square.]*

## Slide 3 — The integer restriction

The row sum $h(1)$ is an integer, so $n$ is a perfect square.
Our order-four row $(-1,1,1,1)$ has sum $2$, and $2^2=4$.
For an order-$36$ candidate, the sum would have to be $6$ or $-6$.

This only gives a necessary restriction. The next step uses orthogonality
to show that this square must also be even.

*[Animation: Show $(-1)+1+1+1=2$ and $n=2^2=4$. Then display the
necessary order-$36$ condition $h(1)=\pm6$ without inventing a row.
Finish with the boxed statement “$n$ is a square.”]*

Source: [the paper, Section 2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
