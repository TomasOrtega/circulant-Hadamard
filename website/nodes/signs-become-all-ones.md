---
id: signs-become-all-ones
title: Signs Become All Ones
shortTitle: Signs Become All Ones
summary: The common sign array becomes an all-ones polynomial after reduction.
number: 5
draft: true
video:
  src: media/signs-become-all-ones.mp4
  captions: media/signs-become-all-ones.vtt
  duration: 224.466667
mapPosition:
  - 40
  - 500
mapSummary: '$E(P)$ reduces to all ones'
graphLayout: proof-map
graphTitle: Inside Node 5 · Signs Become All Ones
children:
  - node: form-sign-combination
    dependsOn: []
    segment: { start: 29.47, end: 126.37 }
    script: |
      The three polynomials $c(P),d(P),g(P)$ came from the same four
      sign polynomials $H_0(P),\ldots,H_3(P)$. Define

      $$
      E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
      $$

      Both quotients have Gaussian-integer coefficients. To see why,
      substitute the definitions from Node 3:

      $$
      \frac{d(P)-c(P)}2=-\frac{H_1(P)+H_3(P)}2,
      $$

      $$
      \begin{aligned}
      \frac{g(P)-c(P)}{1+i}
      &=-\frac{H_2(P)+H_3(P)}2\\
      &\quad+i\frac{H_1(P)+H_2(P)}2.
      \end{aligned}
      $$

      Each half-sum has integer coefficients because the sum of two signs
      is even. Adding these expressions gives the useful identity

      $$
      E(P)=-H_3(P)+(i-1)\frac{H_1(P)+H_2(P)}2.
      $$

      We form these exact quotients first, before reducing any coefficients.
  - node: gaussian-parity
    dependsOn: []
    segment: { start: 126.37, end: 157.77 }
    script: |
      Two Gaussian integers are congruent modulo $1+i$ when their difference
      is a Gaussian-integer multiple of $1+i$. For example,

      $$
      2=(1+i)(1-i),\qquad i-1=i(1+i).
      $$

      Thus $2\equiv0$ and $i\equiv1$. In particular, both $+1$ and $-1$
      have residue $1$. Reducing a polynomial means applying this rule
      separately to each coefficient.

      Congruence does not mean equality: $i\equiv1\pmod{1+i}$,
      even though $i\ne1$.
  - node: all-ones-congruence
    dependsOn:
      - form-sign-combination
      - gaussian-parity
    segment: { start: 157.77, end: 224.466667 }
    script: |
      In the exact expression

      $$
      E(P)=-H_3(P)+(i-1)\frac{H_1(P)+H_2(P)}2,
      $$

      the second term vanishes modulo $1+i$. Every coefficient of $-H_3(P)$
      is a sign, so every coefficient has residue $1$. In our nine-position
      example, this gives

      $$
      E(P)\equiv1+P+\cdots+P^8\pmod{1+i}.
      $$

      In general there are $u^2$ positions. Write

      $$
      J(P):=1+P+\cdots+P^{u^2-1}.
      $$

      Then $E(P)\equiv J(P)\pmod{1+i}$ in
      $\mathbb Z[i][P]/(P^{u^2}-1)$, with coefficients reduced modulo $1+i$.
      The symbol $J(P)$ is just shorthand for this all-ones polynomial.

      This calculation uses the common sign array. It also gives the
      divisibilities needed in Node 6: $d(P)-c(P)$ is divisible by $2$,
      and $g(P)-c(P)$ is divisible by $1+i$.
---

We now build a polynomial $E(P)$ from the differences $d(P)-c(P)$ and
$g(P)-c(P)$, so that later comparisons among $c(P),d(P),g(P)$ also give
information about $E(P)$. We choose the combination so that, modulo $1+i$,
it becomes the all-ones polynomial

$$
J(P):=1+P+\cdots+P^{u^2-1}.
$$

> **Lemma (Signs become all ones).** *Let $u$ be a positive odd integer,
> and let $c(P),d(P),g(P)$ be the normalized evaluations from the same four
> sign polynomials $H_0(P),\ldots,H_3(P)$ in Node 3. Then*
>
> $$
> E(P):=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}
> $$
>
> *has Gaussian-integer coefficients, belongs to
> $\mathbb Z[i][P]/(P^{u^2}-1)$, and satisfies*
>
> $$
> E(P)\equiv J(P)\pmod{1+i}.
> $$

Substituting the definitions of $c(P),d(P),g(P)$ gives the exact identity

$$
E(P)=-H_3(P)+(i-1)\frac{H_1(P)+H_2(P)}2.
$$

Every coefficient of $H_1(P)+H_2(P)$ is a sum of two signs, so the half-sum
has integer coefficients. This proves that $E(P)$ has Gaussian-integer
coefficients. Since $i-1=i(1+i)$, the second term vanishes modulo $1+i$.
The remaining coefficients of $-H_3(P)$ are all $+1$ or $-1$, and both
reduce to $1$ because

$$
2=(1+i)(1-i).
$$

Thus every coefficient becomes one. In our guiding case $u=3$, this says

$$
\begin{aligned}
E(P)&\equiv J(P)\pmod{1+i},\\
J(P)&=1+P+\cdots+P^8.
\end{aligned}
$$

Finally, evaluating at $P=1$ gives $J(1)=u^2$. Since $u$ is odd, so is
$u^2$, and therefore

$$
\boxed{\begin{aligned}
E(1)&\equiv J(1)=u^2\\
&\equiv1\pmod{1+i}.
\end{aligned}}
$$
