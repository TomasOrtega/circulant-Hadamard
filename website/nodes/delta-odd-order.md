---
id: delta-odd-order
title: Why the Order Is Odd
shortTitle: Odd Order
summary: A root of unity with residue one in characteristic p has p-power order, and every prime dividing u is odd.
number: "4.6"
draft: false
video:
  src: media/delta-odd-order.mp4
  poster: media/thumbnails/delta-odd-order.jpg
  captions: media/delta-odd-order.vtt
  duration: 179.433333
mapPosition: [440, 560]
mapSummary: Only odd-order rotations remain
---

> **Lemma (Odd order).** *For odd $u>1$ and
> $f(P)f^*(P)=u^2$, the order of $\Delta(f)$ is a power of every prime
> dividing $u$. In particular it is odd; if $u$ has two distinct prime
> divisors, then $\Delta(f)=1$.*

The preceding nodes show that $\Delta(f)$ is a root of unity and has
residue $1$ above every prime dividing $u$. We now combine those facts.

## A vanishing sum restricts the order

Let $\xi$ be a root of unity in a local domain whose residue field has
characteristic $p$. Suppose $\xi$ has residue $1$ and order
$p^a m$, where $p\nmid m$. Then $\eta=\xi^{p^a}$ has order $m$
and still has residue $1$.

If $m>1$, we have $\eta\ne1$ and

$$
(\eta-1)(1+\eta+\cdots+\eta^{m-1})=0.
$$

The ring is a domain, so the sum in parentheses must vanish. Reducing
it gives $m=0$ in characteristic $p$, contradicting $p\nmid m$.
Thus $m=1$: the order of $\xi$ is a power of $p$. Order $1$ is allowed.

## Apply this at every prime dividing u

Kronecker has made $\Delta(f)$ a root of unity. The local comparison
and subset pairing show that it has residue $1$ at a maximal ideal
above each prime $p\mid u$. Such ideals exist: the cyclotomic ring
$B$ is a nonzero free abelian group of finite rank, so $B/pB\ne0$.

Therefore the order of $\Delta(f)$ is a power of every prime dividing
$u$. Since $u$ is odd, this proves the required odd-order conclusion.
In fact, if $u$ has two distinct prime divisors, the only possible
order is $1$, and $\Delta(f)=1$.

## The three directions for u=3

In the guiding example, $\Delta(f)=f(1)/f(\omega)$ lies in
$\mathbb Q(i,\omega)$ and has $3$-power order. This field has degree
$4$ over $\mathbb Q$, whereas a primitive ninth root already has
degree $6$; higher $3$-power roots have larger degrees. Hence

$$
\Delta(f)\in\{1,\omega,\omega^2\}.
$$

The possible phase differences are $0$, $120$, and $240$ degrees.
They need not all be zero: $f(P)=3iP$ gives $\Delta(f)=\omega^2$.

The Δ-theorem applies to every Gaussian norm solution of the
stated size. In particular, Node 3 supplies $c(P),d(P),g(P)$, so their
three Δ-values have odd order. Node 6 combines this arithmetic fact
with the separate information from signs.

Source: [the paper, Lemma 3.3(ii) and Proposition 3.4](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
