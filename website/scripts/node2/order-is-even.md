# Video 2.2 — Pair the Dot-Product Terms

## Slide 1 — Count the signs in a dot product

Suppose the order is $n>1$. We can choose two distinct rows, whose dot
product is zero. Each coordinate contributes $+1$ or $-1$, because
both entries are signs.

Our goal is to show that the number $n$ of contributions must be even.

*[Animation: Put two rows above one another and multiply each vertical
pair of entries. Move the resulting $+1$ and $-1$ terms into a dot-product
sum, keeping a counter labeled “$n$ terms.”]*

## Slide 2 — Positive and negative terms pair off

If there are $a$ positive terms and $b$ negative terms, then

$$
a-b=0,\qquad a+b=n.
$$

The first equation says $a=b$, so $n=2a$ is even. In our order-four
example, the dot product is $-1-1+1+1=0$: each negative contribution
pairs with a positive one.

*[Animation: Separate the contributions into positive and negative
columns, then pair them. Show that an unpaired term would prevent the
sum from being zero. Replace the matched counts by $a=b$ and reveal
$n=2a$.]*

## Slide 3 — Combine evenness with the square

For a circulant matrix, we already know $n=m^2$ for an integer $m>0$.
If $m$ were odd, its square would be odd. Thus $m$ is even; write
$m=2u$. We conclude

$$
\boxed{n=4u^2,\qquad u\text{ a positive integer}.}
$$

The remaining task is to prove that this same $u$ is odd.

*[Animation: Bring together the cards “$n=m^2$” and “$n$ even.”
Replace $m$ by $2u$ and expand $(2u)^2$ to $4u^2$. Leave “$u$ odd?”
as the next goal, without marking it proved yet.]*

Source: [the paper, Section 2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
