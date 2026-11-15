---
id: odd-squares-mod-eight
title: Odd Squares Modulo 8
shortTitle: Odd Squares Modulo 8
mapTitle: 'Odd Squares Modulo $8$'
summary: The final coefficient squares would have to sum to both zero and four modulo eight.
number: "2.6"
draft: true
video: null
mapPosition: [240, 600]
mapSummary: '$s=1$, so $n=4u^2$ with $u$ odd'
---

## The final contradiction

Assume $s\geq2$. After the folding step, the constant coefficient of the
polynomial norm identity gives

$$
\sum_{j=0}^{2^{s+1}-1}b_j^2=4w^2,
\qquad b_j\text{ odd},\quad w\text{ odd}.
$$

Every odd square is $1$ modulo $8$. There are $2^{s+1}$ terms, a multiple
of $8$, so the left side is $0$ modulo $8$. The right side is $4$ modulo $8$.
This is impossible.

## The smallest instance

At $n=16$, we have $u=2$, so $s=2$ and $w=1$. One fold would leave eight odd
coefficients whose squared values sum to $4$. Their sum of squares is
$0$ modulo $8$, contradicting $4$.

**Output.** The assumption $s\geq2$ fails. Since $s\geq1$, we get $s=1$.
Thus $u=2^{s-1}w=w$ is odd, and $n=4u^2$. This leaves candidate orders
$4,36,100,196,\ldots$; the later main nodes address the candidates beyond $4$.

This conclusion uses the folding construction and its cyclotomic input.
Their detailed proofs remain to be expanded in the preceding nodes.
