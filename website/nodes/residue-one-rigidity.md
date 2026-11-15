---
id: residue-one-rigidity
title: Odd Order Forces Equality
shortTitle: Odd Order Forces Equality
summary: A nontrivial odd-order root of unity cannot reduce to one in characteristic two.
number: "6.4"
draft: false
video:
  src: media/residue-one-rigidity.mp4
  captions: media/residue-one-rigidity.vtt
  duration: 162.533333
foundation: true
mapPosition: [240, 380]
mapSummary: 'Odd order and residue $1$ force $1$'
---

## The elementary rigidity lemma

> **Lemma (Odd-order rigidity).** *Let $A$ be a characteristic-zero domain
> with a reduction map to a nonzero ring of characteristic two. A root of
> unity in $A$ of odd order and residue $1$ must equal $1$.*

To prove this, suppose instead that $\xi\ne1$, and let its order be the
odd integer $r>1$. We have

$$
(\xi-1)(1+\xi+\cdots+\xi^{r-1})=\xi^r-1=0.
$$

The original ring $A$ is a domain and $\xi-1\ne0$, so

$$
1+\xi+\cdots+\xi^{r-1}=0.
$$

Reduce this equality. Every summand becomes $1$, and there are an odd
number of summands. Their sum in characteristic two is $1$, contradicting
$1\ne0$ in the target ring.

The cancellation was made in the original domain, before reduction.
The target ring need not be a domain. The conclusion also allows order
$1$, which is precisely the surviving value.

## Apply the two inputs

Node 6.1 gives odd order for $R$ and $W$. Node 6.3 gives residue $1$ for
both in the nonzero characteristic-two reduction from Node 6.2.
The lemma therefore yields the exact identities

$$
\boxed{R=W=1.}
$$

For the cube-root example, a hypothetical surviving $\omega$ would give
$1+\omega+\omega^2=0$, but reduction to $1$ would give $1+1+1=1=0$.
The same argument excludes $\omega^2$.

**Output.** Exact equality follows from odd order and the algebraic
residue condition. No estimate of a complex distance is involved.

Source: [the paper, Lemma 3.3(ii) and equation (4.10)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
