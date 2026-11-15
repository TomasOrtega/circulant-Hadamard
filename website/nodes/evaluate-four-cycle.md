---
id: evaluate-four-cycle
title: Evaluate at 1, −1, and i
shortTitle: Three Evaluations
summary: Fourth roots of unity respect the four-cycle relation and carry the norm identity into one variable.
number: "3.3"
draft: true
video: null
mapPosition: [40, 360]
mapSummary: Evaluations preserve the norm
---

## The three substitutions

Each of $1,-1,i$ satisfies $Z^4=1$, so substitution gives a ring map. The
four sign polynomials become

$$
\begin{aligned}
h(1,P)&=H_0(P)+H_1(P)+H_2(P)+H_3(P),\\
h(-1,P)&=H_0(P)-H_1(P)+H_2(P)-H_3(P),\\
h(i,P)&=H_0(P)-H_2(P)+i\bigl(H_1(P)-H_3(P)\bigr).
\end{aligned}
$$

The first two have integer coefficients; the third has Gaussian-integer
coefficients. The value at $-i$ is the coefficientwise conjugate of the value
at $i$, so it does not supply another independent polynomial.

## Why star still works

For a Gaussian-integer polynomial $f(P)=\sum_b f_bP^b$, define

$$
f^*(P)=\sum_b\overline{f_b}P^{-b}.
$$

Star conjugates the coefficients as well as reversing powers. For
$\epsilon\in\{1,-1,i\}$, we have $\epsilon^{-1}=\overline{\epsilon}$, so

$$
h^*(\epsilon,P)=\overline{h(\epsilon,P^{-1})}.
$$

Here the bar conjugates coefficients, leaving the formal variable $P$ fixed.
Consequently the evaluated polynomial times its star is $4u^2$.

**Example.** At order $36$, all three evaluated products equal $36$.
The final step will divide each polynomial by $2$, changing this scalar to $9$.
