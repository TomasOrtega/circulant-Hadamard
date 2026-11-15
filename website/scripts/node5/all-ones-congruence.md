# Video 5.3 — All Coefficients Become 1

## Slide 1 — Combine the two inputs

Let $u$ be a positive integer. We now combine the exact sign formula
with Gaussian parity. The first input is

$$
E(P)=-H_3(P)+(i-1)\frac{H_1(P)+H_2(P)}2.
$$

The half-sum is an integer polynomial. Since $i-1=i(1+i)$, the entire
second term vanishes modulo $1+i$. Thus

$$
E(P)\equiv-H_3(P)\pmod{1+i}.
$$

*[Animation: Bring in the exact formula from Node 5.1 and the factor
identity from Node 5.2. Label the half-sum “integer coefficients.”
Factor out $1+i$, then remove that term under a reduction label.]*

## Slide 2 — Every coefficient becomes one

Write the remaining sign polynomial as

$$
H_3(P)=\sum_{r=0}^{u^2-1}h_{3,r}P^r,
\qquad h_{3,r}\in\{-1,1\}.
$$

Both possible values of $-h_{3,r}$ have residue one. Therefore

$$
\boxed{E(P)\equiv J(P)\pmod{1+i},
\qquad J(P)=1+P+\cdots+P^{u^2-1}.}
$$

This is a statement about every coefficient position. It uses only the
common signs, not the norm identities. It also holds before we require
$u$ to be odd.

*[Animation: Expand $-H_3(P)$ as a row of terms with coefficients $\pm1$.
Replace each coefficient by $1$ without changing its power of $P$.
For $u=3$, show all nine terms; then replace the last exponent $8$ by
$u^2-1$ to display the general statement.]*

## Slide 3 — An odd number of ones at P=1

Now substitute $P=1$. Every term of $J(P)$ becomes one, so

$$
E(1)\equiv J(1)=u^2\pmod{1+i}.
$$

Here oddness matters: if $u$ is odd, the number $u^2$ is odd. Pairs of
ones vanish in characteristic two, leaving one:

$$
\boxed{E(1)\equiv1\pmod{1+i}.}
$$

In our example there are nine ones, with four pairs and one left over.
The general coefficient congruence, together with the exact sign
divisibilities, is the information carried into the later comparisons.

*[Animation: Replace every power by $1$. In the nine-term example,
bracket four pairs and label each pair $2\equiv0$. Keep the final one
visible. Repeat the count symbolically with an odd number $u^2$ of terms,
then end on the boxed congruence.]*

Source: [the paper, Section 4, equations (4.5)–(4.9)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
