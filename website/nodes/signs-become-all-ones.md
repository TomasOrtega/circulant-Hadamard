---
id: signs-become-all-ones
title: Signs Become All Ones
shortTitle: Signs Become All Ones
summary: The common sign array becomes an all-ones polynomial after reduction.
number: 5
draft: false
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
      > **Lemma (Integral combination).** The common sign polynomials make
      > both quotients defining $E(P)$ integral, and
      >
      > $$
      > E(P)=-H_3(P)+(i-1)\frac{H_1(P)+H_2(P)}2.
      > $$

      Indeed, substituting the definitions from Node 3 gives

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

      Each half-sum has integer coefficients because a sum of two signs is
      even. Adding the two quotients gives the displayed identity for $E(P)$.
      These are exact divisions before reduction; the norm identities are
      not needed.

  - node: gaussian-parity
    dependsOn: []
    segment: { start: 126.37, end: 157.77 }
    script: |
      > **Lemma (Gaussian parity).** Reduction modulo $1+i$ sends $a+bi$ to
      > $a+b$ modulo $2$. In particular, $i\equiv-1\equiv1\pmod{1+i}$.

      The formula

      $$
      \frac{a+bi}{1+i}=\frac{a+b}{2}+i\frac{b-a}{2}
      $$

      shows that divisibility by $1+i$ is equivalent to $a+b$ being even.
      Thus $\mathbb Z[i]/(1+i)\cong\mathbb F_2$. Apply this reduction to
      polynomial coefficients while leaving the powers of $P$ in place.
      Both $2$ and $1+i$ become zero, so the quotients defining $E(P)$ must
      be formed before reduction.

  - node: all-ones-congruence
    dependsOn:
      - form-sign-combination
      - gaussian-parity
    segment: { start: 157.77, end: 224.466667 }
    script: |
      > **Lemma (All-ones congruence).** The integral combination satisfies
      >
      > $$
      > E(P)\equiv J(P)\pmod{1+i},
      > \qquad J(P)=1+P+\cdots+P^{u^2-1}.
      > $$

      In the exact formula

      $$
      E(P)=-H_3(P)+(i-1)\frac{H_1(P)+H_2(P)}2,
      $$

      the second term vanishes because $i-1=i(1+i)$. Every coefficient of
      $-H_3(P)$ is a sign, and both signs reduce to one. This proves the
      coefficient congruence without using the norm identities or oddness.

      If $u$ is odd, evaluating at $P=1$ then gives
      $E(1)\equiv J(1)=u^2\equiv1\pmod{1+i}$. For $u=3$, four pairs of
      ones vanish and the ninth one remains. Retain the exact divisibilities
      $2\mid d(P)-c(P)$ and $1+i\mid g(P)-c(P)$ for Node 6.
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
