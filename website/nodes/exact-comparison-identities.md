---
id: exact-comparison-identities
title: Exact Comparisons and a Common Rotation
shortTitle: Exact Comparisons
summary: The comparison products equal one; in the two-evaluation example this means one common rotation of all three points.
number: "6.5"
draft: true
video: null
mapPosition: [240, 560]
mapSummary: '$R=W=1$; one rotation when $u=3$'
---

## The general output

For any odd $u>1$, the conclusion $R=W=1$ is the pair of exact identities

$$
\begin{aligned}
\prod_{S\subseteq I}\left(\frac{d_S}{c_S}\right)^{(-1)^{|S|}}&=1,\\
\prod_{S\subseteq I}\left(\frac{g_S}{c_S}\right)^{(-1)^{|S|}}&=1.
\end{aligned}
$$

Here $I$ is the set of distinct primes dividing $u$, and $c_S,d_S,g_S$
are evaluations at the subset roots from Node 4. These multiplicative
identities are what the next node receives.

## Two evaluations give a common rotation

For $u=3$, there are just the evaluations at $1$ and
$\omega=e^{2\pi i/3}$. The two identities become

$$
\begin{aligned}
\frac{d(1)}{c(1)}&=\frac{d(\omega)}{c(\omega)},\\
\frac{g(1)}{c(1)}&=\frac{g(\omega)}{c(\omega)}.
\end{aligned}
$$

Define

$$
\lambda=\frac{c(\omega)}{c(1)}.
$$

Both values have magnitude $3$, so $|\lambda|=1$. Rearranging the ratio
identities gives

$$
\begin{aligned}
c(\omega)&=\lambda c(1),\\
d(\omega)&=\lambda d(1),\\
g(\omega)&=\lambda g(1).
\end{aligned}
$$

All three points undergo the same rotation from the evaluation at $1$
to the evaluation at $\omega$. Their relative positions remain fixed;
the points need not coincide. Also $\lambda=\Delta(c)^{-1}$, so in this
example $\lambda\in\{1,\omega,\omega^2\}$.

## Keep the example separate from the general conclusion

When $u$ has several distinct prime divisors, $R=W=1$ compares alternating
products over several evaluations. It does not by itself say that one
rotation carries every evaluated triple to every other triple. The simple
two-circle picture describes the one-prime example.

**Output.** $R=W=1$ in general, with the common-rotation interpretation
for the guiding case $u=3$.

Source: [the paper, Section 4, equations (4.3), (4.4), and (4.10)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
