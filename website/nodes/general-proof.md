---
id: general-proof
title: The General Odd-u Proof
shortTitle: General proof
summary: The same eight nodes, with an alternating product over subsets of the
  prime divisors.
supplemental: true
draft: true
graphLayout: proof-map
children:
  - node: group-ring-encoding
    dependsOn: []
    segment: null
  - node: restriction-on-the-order
    dependsOn:
      - group-ring-encoding
    segment: null
  - node: three-evaluations
    dependsOn:
      - restriction-on-the-order
    segment: null
  - node: delta-theorem
    dependsOn: []
    segment: null
    contextFrom:
      - group-ring-encoding
  - node: signs-become-all-ones
    dependsOn:
      - three-evaluations
    segment: null
  - node: odd-order-rigidity
    dependsOn:
      - three-evaluations
      - delta-theorem
      - signs-become-all-ones
    segment: null
  - node: products-to-sums
    dependsOn:
      - signs-become-all-ones
      - odd-order-rigidity
    segment: null
  - node: final-contradiction
    dependsOn:
      - signs-become-all-ones
      - products-to-sums
    segment: null
  - node: theorem
    dependsOn:
      - final-contradiction
    segment: null
---

[Start with the order-36 example](../proof-by-example/index.html) for the two-evaluation case.

Accept the order restriction and Δ-theorem. Suppose $n=4u^2$ for odd $u>1$ and let $h(Z,P)$ be the hypothetical sign polynomial, with $Z^4=P^{u^2}=1$.

$$
c(P)=\frac{h(1,P)}2,\quad d(P)=\frac{h(-1,P)}2,\quad g(P)=\frac{h(i,P)}2,
\qquad cc^*=dd^*=gg^*=u^2.
$$

For each distinct prime $p\mid u$, choose a primitive $p$th root $\zeta_p$. For each subset $S$ of these primes, put $\zeta_S=\prod_{p\in S}\zeta_p$ and $\zeta_\varnothing=1$. Define

$$
\Delta(f)=\prod_S f(\zeta_S)^{(-1)^{|S|}},\qquad
R=\frac{\Delta(d)}{\Delta(c)},\quad W=\frac{\Delta(g)}{\Delta(c)},
$$

and

$$
E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i},\qquad
J(P)=1+P+\cdots+P^{u^2-1}.
$$

For arbitrary odd $u>1$, use the $2^r$ substitutions $P=\zeta_S$, where $r$ is the number of distinct primes dividing $u$. The Δ-theorem and signs still give $R=W=1$. Instead of obtaining one common rotation, expand the two products to first order and obtain
$$
\sum_S(-1)^{|S|}\frac{E(\zeta_S)}{c(\zeta_S)}\equiv0\pmod{1+i}.
$$
Using $E\equiv J$, all nonempty-subset contributions disappear and $0\equiv u^2/c(1)=\pm u\equiv1$. This completes the general proof.

## Where the congruences live

For reductions, it suffices to work in
$$
A=\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]
\quad\text{modulo the ideal }(1+i).
$$
The quotient is a nonzero ring of characteristic 2. Every $c(\zeta_S)$ is invertible in $A$ because $c(\zeta_S)\overline{c(\zeta_S)}=u^2$. Likewise for $d,g$. Expressions divided by $2$ or $1+i$ are **formed in characteristic zero** using coefficientwise divisibility, not divided in the quotient.

See [From Products to Sums](products-to-sums/index.html) for the expansion step and [The Final Contradiction](final-contradiction/index.html) for the surviving term. The internal proofs of the two accepted propositions are deferred.
