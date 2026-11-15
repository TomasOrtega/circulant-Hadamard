---
id: evaluate-four-cycle
title: Evaluate at 1, −1, and i
shortTitle: Three Evaluations
summary: Fourth roots of unity respect the four-cycle relation and carry the norm identity into one variable.
number: "3.3"
draft: false
video:
  src: media/evaluate-four-cycle.mp4
  captions: media/evaluate-four-cycle.vtt
  duration: 215.966667
mapPosition: [40, 360]
mapSummary: Evaluations preserve the norm
---

> **Lemma (Evaluation preserves the norm).** *Suppose
> $h(Z,P)h^*(Z,P)=4u^2$. For $\epsilon\in\{1,-1,i\}$, evaluation at
> $Z=\epsilon$ gives a Gaussian-integer polynomial satisfying*
>
> $$
> h(\epsilon,P)\bigl(h(\epsilon,P)\bigr)^*=4u^2
> \quad\text{in }\mathbb Z[i][P]/(P^{u^2}-1).
> $$

Each choice satisfies $\epsilon^4=1$, so substitution respects the
relation $Z^4=1$ and defines a ring map. Using the four sign polynomials,

$$
\begin{aligned}
h(1,P)&=H_0(P)+H_1(P)+H_2(P)+H_3(P),\\
h(-1,P)&=H_0(P)-H_1(P)+H_2(P)-H_3(P),\\
h(i,P)&=H_0(P)-H_2(P)\\
&\quad+i\bigl(H_1(P)-H_3(P)\bigr).
\end{aligned}
$$

For $f(P)=\sum_bf_bP^b$ with Gaussian-integer coefficients, star means

$$
f^*(P)=\sum_b\overline{f_b}P^{-b}.
$$

It must conjugate coefficients as well as invert $P$. For a term with
real coefficient $h_{a,b}$, evaluating its star gives
$h_{a,b}\epsilon^{-a}P^{-b}$. Taking star after evaluation gives
$h_{a,b}\overline{\epsilon}^{\,a}P^{-b}$. They agree because
$\epsilon^{-1}=\overline\epsilon$. Thus evaluation commutes with star;
applying it to the original product proves the lemma.

The first two evaluated polynomials have integer coefficients. The value
at $-i$ is the coefficientwise conjugate of the value at $i$, so it is
already determined. For $u=3$, every evaluated norm remains $36$.

Source: [the paper, Section 4, equations (4.1)–(4.2)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
