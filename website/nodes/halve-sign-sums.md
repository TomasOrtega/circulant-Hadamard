---
id: halve-sign-sums
title: Parity of Sign Columns
shortTitle: Parity of Sign Columns
summary: Four signs have even sums, and two signs have even differences, so the normalized coefficients remain integral.
number: "3.4"
draft: true
video: null
mapPosition: [440, 360]
mapSummary: Even sums and differences
---

## A fact about four signs

Let $a_0,a_1,a_2,a_3\in\{-1,1\}$. Since each sign is odd, both

$$
\begin{aligned}
\frac{a_0+a_1+a_2+a_3}{2}&\in\mathbb Z,\\
\frac{a_0-a_1+a_2-a_3}{2}&\in\mathbb Z.
\end{aligned}
$$

The difference of two signs is also even. Therefore

$$
\frac{a_0-a_2}{2}+i\frac{a_1-a_3}{2}\in\mathbb Z[i].
$$

This is a coefficientwise parity argument. It does not need the norm identity
or the evaluation lemma.

## Apply it to each column

Use the four coefficients of $P^b$ in $H_0(P),H_1(P),H_2(P),H_3(P)$ as the
four signs above. The three combinations are exactly the coefficients obtained
by dividing $h(1,P),h(-1,P),h(i,P)$ by $2$.

For an individual column $(-1,1,1,1)$, the normalized coefficients are
$1,-1,-1$, respectively. This illustrates the calculation for a column; it
does not specify all nine columns of a hypothetical order-36 matrix.

**Output.** The first two normalized polynomials have integer coefficients,
and the third has Gaussian-integer coefficients. Division by $2$ introduces
no fractional coefficients.
