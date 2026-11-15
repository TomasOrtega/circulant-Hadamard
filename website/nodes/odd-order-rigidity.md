---
id: odd-order-rigidity
title: Odd-Order Rigidity
shortTitle: Odd-Order Rigidity
summary: The arithmetic and sign branches force the comparison products to equal
  one; in the nine-position example, the three evaluations share a rotation.
number: 6
draft: true
video: null
mapPosition:
  - 460
  - 500
mapSummary: '$R=W=1$'
graphLayout: proof-map
graphTitle: Inside Node 6 · Odd-Order Rigidity
children:
  - node: odd-comparison-products
    dependsOn: []
    segment: null
    script: |
      Node 3 gives three polynomial norm solutions, and the Δ-theorem gives
      $\Delta(c),\Delta(d),\Delta(g)$ of odd order. Define

      $$
      \begin{aligned}
      R&=\frac{\Delta(d)}{\Delta(c)},\\
      W&=\frac{\Delta(g)}{\Delta(c)}.
      \end{aligned}
      $$

      A quotient of roots whose orders divide odd integers $a,b$ has order
      dividing the odd integer $ab$. Thus $R,W$ also have odd order.

      For $u=3$, each Δ-value compares the phases at $1$ and $\omega$.
      The quantities $R,W$ compare those relative rotations with the one
      belonging to $c(P)$. They are cube roots of unity in this example.
  - node: evaluation-units
    dependsOn: []
    segment: null
    script: |
      Before dividing congruences, we need invertible denominators. For
      $x(P)\in\{c(P),d(P),g(P)\}$, every evaluation from Node 4 satisfies

      $$
      x(\zeta_S)\overline{x(\zeta_S)}=u^2.
      $$

      Work in the coefficient ring

      $$
      \mathbb Z[i,\{\zeta_p:p\mid u\},1/u].
      $$

      Every such value is a unit there, with explicit inverse

      $$
      x(\zeta_S)^{-1}=\frac{\overline{x(\zeta_S)}}{u^2}.
      $$

      Its reduction modulo $1+i$ is a nonzero ring of characteristic two,
      and these units remain invertible. For $u=3$, the inverse is the
      conjugate divided by $9$; the odd denominator remains invertible
      after reduction.
  - node: sign-ratio-congruences
    dependsOn:
      - evaluation-units
    segment: null
    script: |
      The common signs in Node 5 gave coefficientwise divisibilities:

      $$
      2\mid d(P)-c(P),\qquad 1+i\mid g(P)-c(P).
      $$

      Evaluate and divide by the unit $c(\zeta_S)$. Since $2=(1+i)(1-i)$,
      both quotients have residue $1$:

      $$
      \begin{aligned}
      r_S&:=\frac{d(\zeta_S)}{c(\zeta_S)}\equiv1,\\
      w_S&:=\frac{g(\zeta_S)}{c(\zeta_S)}\equiv1
      \pmod{1+i}.
      \end{aligned}
      $$

      The comparison products are

      $$
      \begin{aligned}
      R&=\prod_{S\subseteq I}r_S^{(-1)^{|S|}},\\
      W&=\prod_{S\subseteq I}w_S^{(-1)^{|S|}},
      \end{aligned}
      $$

      where $I$ is the set of distinct primes dividing $u$. Products and
      inverses of units with residue $1$ still have residue $1$. Hence

      $$
      R\equiv W\equiv1\pmod{1+i}.
      $$

      This is an algebraic congruence, not a statement that either complex
      number is close to $1$.
  - node: residue-one-rigidity
    dependsOn:
      - odd-comparison-products
      - sign-ratio-congruences
    segment: null
    script: |
      > **Odd-order rigidity.** A root of unity of odd order in our coefficient
      > ring that reduces to $1$ in a nonzero ring of characteristic two must
      > equal $1$.

      To see this, suppose $\xi\ne1$ has odd order $r$. In the original
      characteristic-zero domain,

      $$
      1+\xi+\cdots+\xi^{r-1}=0.
      $$

      If $\xi$ reduces to $1$, this becomes a sum of an odd number of
      ones. In characteristic two that sum is $1$, contradicting $0$.

      The two branches now meet: $R,W$ have odd order and residue $1$.
      Therefore

      $$
      R=W=1.
      $$
  - node: exact-comparison-identities
    dependsOn:
      - residue-one-rigidity
    segment: null
    script: |
      For general odd $u>1$, we have two exact alternating-product
      identities. In the guiding case $u=3$, there are only two
      evaluations, so they become

      $$
      \begin{aligned}
      \frac{d(1)}{c(1)}&=\frac{d(\omega)}{c(\omega)},\\
      \frac{g(1)}{c(1)}&=\frac{g(\omega)}{c(\omega)}.
      \end{aligned}
      $$

      Put $\lambda=c(\omega)/c(1)$. Both values have modulus $3$, so
      $|\lambda|=1$, and

      $$
      \begin{aligned}
      c(\omega)&=\lambda c(1),\\
      d(\omega)&=\lambda d(1),\\
      g(\omega)&=\lambda g(1).
      \end{aligned}
      $$

      All three points on the radius-three circle undergo the same
      rotation. Their relative positions stay fixed; the points need
      not coincide. Here $\lambda=\Delta(c)^{-1}$ is itself a cube root.

      With several distinct prime divisors, $R=W=1$ compares alternating
      products over several evaluations. It does not assert that all
      evaluations share one rotation. These exact product identities
      are the input to Node 7.
---

The key idea is to combine the two branches of the proof. The Δ-theorem
makes our comparison products roots of unity of odd order, while the
arithmetic of their common signs forces them to have residue $1$ modulo $1+i$.
Odd-order rigidity rules out every nontrivial root with these properties:
the order must be one, so both comparison products equal $1$.

> **Lemma (Odd-order rigidity).** *Let $u>1$ be odd, and let
> $c(P),d(P),g(P)$ be the normalized norm solutions from the common sign
> array in Node 3. Define*
>
> $$
> R=\frac{\Delta(d)}{\Delta(c)},
> \qquad W=\frac{\Delta(g)}{\Delta(c)}.
> $$
>
> *Then*
>
> $$
> R=W=1.
> $$

To obtain the residue condition, evaluate the sign divisibilities from
Node 5 and divide by the invertible evaluations, giving
$R\equiv W\equiv1\pmod{1+i}$. The smaller nodes inside Node 6 give the
full arithmetic argument and the proof of odd-order rigidity.

In our guiding case $u=3$, put $\omega=e^{2\pi i/3}$. The identities
$R=W=1$ mean exactly

$$
\begin{aligned}
\frac{d(1)}{c(1)}&=\frac{d(\omega)}{c(\omega)},\\
\frac{g(1)}{c(1)}&=\frac{g(\omega)}{c(\omega)}.
\end{aligned}
$$

Each ratio stays the same at the two inputs; $d(1)/c(1)$ need not equal
$g(1)/c(1)$.
The six evaluations lie on circles of radius three. Set
$\lambda=c(\omega)/c(1)$. Since $|\lambda|=1$, we obtain the common
rotation

$$
\begin{aligned}
c(\omega)&=\lambda c(1),\\
d(\omega)&=\lambda d(1),\\
g(\omega)&=\lambda g(1).
\end{aligned}
$$

Thus the three points rotate together, keeping their relative angles.
Now substitute the definition

$$
E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
$$

For $z=1$ or $\omega$, the value $c(z)$ is a unit in
$\mathbb Z[i,\omega,1/3]$. Dividing the evaluated identity by $c(z)$ gives

$$
\begin{aligned}
\frac{E(z)}{c(z)}
&=\frac12\left(\frac{d(z)}{c(z)}-1\right)\\
&\quad+\frac1{1+i}\left(\frac{g(z)}{c(z)}-1\right).
\end{aligned}
$$

The divisions by $2$ and $1+i$ are the exact divisions established in
Node 5, before any modular reduction. Both ratios on the right stay the
same when $z$ changes from $1$ to $\omega$, so

$$
\boxed{\frac{E(\omega)}{c(\omega)}=\frac{E(1)}{c(1)}.}
$$

Equivalently, $E(\omega)=\lambda E(1)$: the value of $E(P)$ picks up
the same rotation. Node 7 compares this exact equality with the residues
required by $E(P)\equiv J(P)\pmod{1+i}$ to obtain the contradiction
for $u=3$.

The general case requires more care. With several distinct prime divisors
of $u$, the identities $R=W=1$ compare alternating products; we cannot
assume one shared rotation between every pair of evaluation points.
The smaller nodes in Node 7 turn those product identities into a
vanishing alternating-sum congruence, which Node 8 uses to finish the
general argument.
