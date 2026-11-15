---
id: three-evaluations
title: The Three Evaluations
shortTitle: The Three Evaluations
summary: Split the cyclic coordinates, evaluate the four-position factor, and
  divide by two to obtain three integral norm solutions.
number: 3
draft: true
video:
  src: media/three-evaluations.mp4
  captions: media/three-evaluations.vtt
  duration: 214.966667
mapPosition:
  - 40
  - 340
mapSummary: '$c(P)c^*(P)=d(P)d^*(P)=g(P)g^*(P)=u^2$'
graphLayout: proof-map
graphTitle: Inside Node 3 · The Three Evaluations
children:
  - node: crt-coordinates
    dependsOn: []
    segment: { start: 16.55, end: 40.81 }
    script: |
      Since $u$ is odd, $4$ and $u^2$ are coprime. The Chinese remainder
      theorem gives

      $$
      C_{4u^2}\cong C_4\times C_{u^2}.
      $$

      For our guiding example, $C_{36}\cong C_4\times C_9$.
      The position $j$ becomes the pair $(j\bmod4,j\bmod9)$.
      We have relabeled the same $36$ signs.

      In the group ring, this replaces $X$ by $ZP$, with $Z^4=1$ and
      $P^9=1$. The polynomial identity becomes

      $$
      h(Z,P)h^*(Z,P)=36
      \quad\text{in }\mathbb Z[Z,P]/(Z^4-1,P^9-1).
      $$
  - node: four-sign-polynomials
    dependsOn:
      - crt-coordinates
    segment: { start: 40.81, end: 62.83 }
    script: |
      Sort the terms by their power of $Z$:

      $$
      h(Z,P)=H_0(P)+ZH_1(P)+Z^2H_2(P)+Z^3H_3(P).
      $$

      Each $H_a(P)$ has $u^2$ coefficients, all $\pm1$.
      At order $36$, these are four polynomials with nine coefficients each.
      For any fixed power of $P$, the four coefficients form a column of signs.
  - node: evaluate-four-cycle
    dependsOn:
      - four-sign-polynomials
    segment: { start: 62.83, end: 90.45 }
    script: |
      We can substitute $Z=1,-1,i$, since each satisfies $Z^4=1$.
      This leaves polynomials in $P$:

      $$
      \begin{aligned}
      h(1,P)&=H_0(P)+H_1(P)+H_2(P)+H_3(P),\\
      h(-1,P)&=H_0(P)-H_1(P)+H_2(P)-H_3(P),\\
      h(i,P)&=H_0(P)-H_2(P)+i\bigl(H_1(P)-H_3(P)\bigr).
      \end{aligned}
      $$

      Evaluation respects the product and star. For Gaussian coefficients,
      star conjugates the coefficients and inverts $P$:

      $$
      f^*(P)=\overline{f(P^{-1})}.
      $$

      Each evaluated polynomial still has product with its star equal to
      $4u^2$, or $36$ in our example. The value at $Z=-i$ is the
      coefficientwise conjugate of the value at $Z=i$.
  - node: halve-sign-sums
    dependsOn:
      - four-sign-polynomials
    segment: { start: 115.07, end: 143.23 }
    script: |
      For a column $(a_0,a_1,a_2,a_3)$ of signs, both

      $$
      a_0+a_1+a_2+a_3,\qquad a_0-a_1+a_2-a_3
      $$

      are even. The differences $a_0-a_2$ and $a_1-a_3$ are even too.
      Thus the half-sums are integers, and

      $$
      \frac{a_0-a_2}{2}+i\,\frac{a_1-a_3}{2}
      $$

      is a Gaussian integer. This coefficient check is what lets us divide
      all three evaluated polynomials by $2$ and keep the required
      integer or Gaussian-integer coefficients.
  - node: normalized-evaluation-norms
    dependsOn:
      - evaluate-four-cycle
      - halve-sign-sums
    segment: { start: 90.45, end: 115.07 }
    script: |
      Define

      $$
      \begin{aligned}
      c(P)&=\frac{h(1,P)}2,\\
      d(P)&=\frac{h(-1,P)}2,\\
      g(P)&=\frac{h(i,P)}2.
      \end{aligned}
      $$

      The coefficient check gives integer coefficients for $c,d$ and
      Gaussian-integer coefficients for $g$. Dividing a polynomial and
      its star by $2$ divides their product by $4$. Therefore

      $$
      c(P)c^*(P)=d(P)d^*(P)=g(P)g^*(P)=u^2.
      $$

      At order $36$, the right-hand side is $9$: this is why we divide
      by $2$. We now have the three polynomials needed in the next steps.
---

We first use the **Chinese remainder theorem** to separate the two factors
of the order $n=4u^2$. Since $u$ is odd, $4$ and $u^2$ are coprime, so

$$
C_{4u^2}\cong C_4\times C_{u^2}.
$$

This means that a position $j$ in the original cycle can be described by
two coordinates: $j\bmod4$ and $j\bmod u^2$. Every pair identifies exactly
one original position. We are reorganizing the same coefficients, each
still $+1$ or $-1$.

In the group ring, introduce $Z$ for the four-position coordinate and $P$
for the $u^2$-position coordinate. Replacing $X$ by $ZP$ sends $X^j$ to
$Z^jP^j$, with the two exponents reduced separately. Thus our one-variable
polynomial becomes a two-variable polynomial $h(Z,P)$ in

$$
\mathbb Z[Z,P]/(Z^4-1,P^{u^2}-1).
$$

The relation $Z^4=1$ makes fourth roots of unity the natural choices to
substitute for $Z$. Evaluating at $1,-1,i$ leaves three polynomials in $P$;
the lemma normalizes them by dividing by $2$.

> **Lemma (The three normalized evaluations).** *Suppose $h(Z,P)$ has
> coefficients $\pm1$ and satisfies $h(Z,P)h^*(Z,P)=4u^2$. Group its terms
> by their power of $Z$:*
>
> $$
> \begin{aligned}
> h(Z,P)&=H_0(P)+H_1(P)Z\\
> &\quad+H_2(P)Z^2+H_3(P)Z^3.
> \end{aligned}
> $$
>
> *Each $H_a(P)$ collects the coefficients with $Z$-exponent $a$.
> Define $c(P),d(P),g(P)$ by*
>
> $$
> \begin{aligned}
> c(P)&=\frac{h(1,P)}2\\
> &=\frac{H_0(P)+H_1(P)+H_2(P)+H_3(P)}2,\\[6pt]
> d(P)&=\frac{h(-1,P)}2\\
> &=\frac{H_0(P)-H_1(P)+H_2(P)-H_3(P)}2,\\[6pt]
> g(P)&=\frac{h(i,P)}2\\
> &=\frac{H_0(P)-H_2(P)}2+i\frac{H_1(P)-H_3(P)}2.
> \end{aligned}
> $$
>
> *Then $c,d$ have integer coefficients, $g$ has Gaussian-integer coefficients,
> and*
>
> $$
> c(P)c^*(P)=d(P)d^*(P)=g(P)g^*(P)=u^2.
> $$

Here the identities are in $\mathbb Z[i][P]/(P^{u^2}-1)$, and
$f^*(P)=\overline{f(P^{-1})}$ conjugates coefficients and inverts $P$.

For our **guiding case $u=3$**, this splits the hypothetical order-$36$
polynomial into coordinates with $Z^4=1$ and $P^9=1$. Grouping by the four
powers of $Z$ gives four polynomials with nine sign coefficients each.
At $Z=1$ these four parts add; at $Z=-1$ they alternate in sign; at $Z=i$
they combine into real and imaginary differences.

Each evaluated polynomial still has product with its star equal to $36$.
Dividing the polynomial by $2$ also divides its star by $2$, so the product
is divided by $4$: **$36$ becomes $9$**. The coefficients remain integral
because sums of four signs and differences of two signs are even. Thus
$c,d$ have integer coefficients and $g$ has Gaussian-integer coefficients,
with

$$
c(P)c^*(P)=d(P)d^*(P)=g(P)g^*(P)=9.
$$

The takeaway is geometric. Choose **any ninth root of unity** $\zeta$, so
$\zeta^9=1$, and substitute $P=\zeta$. Star becomes complex conjugation,
giving $|c(\zeta)|^2=|d(\zeta)|^2=|g(\zeta)|^2=9$. Therefore

$$
|c(\zeta)|=|d(\zeta)|=|g(\zeta)|=3.
$$

Whichever value of $P$ we choose subject to $P^9=1$, all three output
values lie on the **circle of radius $3$ centered at the origin**. Their
distance from the origin is fixed; the next question is how their phases
compare, especially at $P=1$ and $P=\omega=e^{2\pi i/3}$.
