---
id: kronecker-step
title: Kronecker's Theorem
shortTitle: Kronecker's Theorem
summary: Integrality and unit magnitude for every conjugate force the alternating product to be a root of unity.
number: "4.5"
draft: true
video: null
blackBox: Kronecker's theorem
mapPosition: [40, 560]
mapSummary: The product is a root of unity
---

## The accepted criterion

We use the following form of Kronecker's theorem as a black box:

> **Kronecker's theorem.** *If an algebraic integer has absolute value
> $1$ under every embedding of its number field into $\mathbb C$, then
> it is a root of unity.*

A root of unity is a complex number $z$ for which $z^r=1$ for some positive
integer $r$. Its powers return to $1$ after finitely many rotations.

## Both hypotheses matter

Lying on the unit circle does not by itself imply finite order. Even
requiring every conjugate to lie there is insufficient without integrality.
For example,

$$
z=\frac{3+4i}{5}
$$

and its conjugate $(3-4i)/5$ both have magnitude $1$. But their sum is
$6/5$, which is not an integer. An algebraic integer has integer trace,
so $z$ is not an algebraic integer; it is therefore not a root of unity
either, since roots of unity are algebraic integers.

This is why the denominator calculation in the preceding node cannot
be replaced by a picture of a circle.

## Apply the criterion

Node 4.2 established that every conjugate of $\Delta(f)$ has absolute
value $1$. Node 4.4 established that $\Delta(f)$ lies in
$B=\mathbb Z[i,\{\zeta_p:p\mid u\}]$, hence is an algebraic integer.
Both hypotheses now hold, and Kronecker gives

$$
\Delta(f)^r=1
\quad\text{for some positive integer }r.
$$

**Output.** The alternating product has finite order. This does not yet
specify that the order is odd; the next step uses the local residue
information retained from the integrality argument.

Source: [the paper, Lemma 3.3(i) and Proposition 3.4](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
