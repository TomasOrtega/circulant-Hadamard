---
id: four-sign-polynomials
title: Four Sign Polynomials
shortTitle: Four Sign Polynomials
summary: Collect the terms with the same power of Z into four polynomials in P.
number: "3.2"
draft: false
video:
  src: media/four-sign-polynomials.mp4
  poster: media/thumbnails/four-sign-polynomials.jpg
  captions: media/four-sign-polynomials.vtt
  duration: 150.9
foundation: true
mapPosition: [240, 180]
mapSummary: '$h(Z,P)=H_0(P)+\cdots+Z^3H_3(P)$'
---

> **Lemma (Four sign polynomials).** *A polynomial $h(Z,P)$ with sign
> coefficients in $\mathbb Z[Z,P]/(Z^4-1,P^{u^2}-1)$ has a unique
> expression*
>
> $$
> h(Z,P)=\sum_{a=0}^{3}Z^aH_a(P),
> \qquad H_a(P)=\sum_{b=0}^{u^2-1}h_{a,b}P^b,
> $$
>
> *where every $h_{a,b}$ is $+1$ or $-1$.*

The group elements $Z^aP^b$, with $0\leq a<4$ and $0\leq b<u^2$,
are an integer basis of the group ring. Grouping its coefficients with
fixed $a$ gives the four polynomials $H_a(P)$. Since basis coefficients
are unique, the decomposition is unique. No coefficients are added to
one another in this step, so they remain signs.

In expanded form,

$$
\begin{aligned}
h(Z,P)&=H_0(P)+ZH_1(P)\\
&\quad+Z^2H_2(P)+Z^3H_3(P).
\end{aligned}
$$

At order $36$, each $H_a(P)$ has nine coefficient positions. For a fixed
power $P^b$, the four entries $h_{0,b},h_{1,b},h_{2,b},h_{3,b}$ are the
four signs that will combine when we substitute a value for $Z$.
This grouping uses only the coordinate description, not the norm identity.

Source: [the paper, Section 4, equations (4.1)–(4.2)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
