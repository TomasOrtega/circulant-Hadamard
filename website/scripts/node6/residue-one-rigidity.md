# Video 6.4 — Odd Order Forces Equality

## Slide 1 — Why a cube root cannot survive

We have two facts about each comparison product: its order is odd,
and its residue modulo $1+i$ is one. We will prove that these force
the comparison product itself to equal one.

First consider $\omega=e^{2\pi i/3}$. It satisfies

$$
1+\omega+\omega^2=0.
$$

If either $\omega$ or $\omega^2$ had residue one, so would the other,
because each is the square of the other. Reducing the equation would
give $1+1+1=0$. In characteristic two, its left side is one. This is
impossible in a nonzero ring.

*[Animation: Show the three candidate cube roots. Write the exact
three-term sum below them, then replace both nontrivial roots by their
assumed residue $1$. Pair two ones, leave the third, and cross out the
two nontrivial candidates using the resulting contradiction.]*

## Slide 2 — The general odd-order argument

Let $A$ be a characteristic-zero domain with a reduction map into a
nonzero ring of characteristic two. Suppose $\alpha\in A$ has odd
order $r$ and residue one. If $\alpha\ne1$, then $r>1$ and

$$
(\alpha-1)(1+\alpha+\cdots+\alpha^{r-1})=\alpha^r-1=0.
$$

Cancel the nonzero factor $\alpha-1$ in the original domain to get

$$
1+\alpha+\cdots+\alpha^{r-1}=0.
$$

Now reduce. Each summand becomes one, and there are an odd number of
them. The sum becomes one, contradicting zero. Therefore $\alpha=1$.
All cancellation happened before reduction; the target ring does not
need to be a domain.

*[Animation: Factor $\alpha^r-1$, then cancel $\alpha-1$ while the board
is labeled “in $A$.” Move the remaining equality to a second board
labeled “characteristic two.” Replace every power by $1$, pair all
but one of the $r$ terms, and display the contradiction.]*

## Slide 3 — Apply both inputs

Node 6.1 proved that

$$
R=\frac{\Delta(d)}{\Delta(c)},\qquad
W=\frac{\Delta(g)}{\Delta(c)}
$$

have odd order. Node 6.3 proved that both have residue one in the
nonzero reduction ring established in Node 6.2. The lemma applies to
each separately and gives the exact identities

$$
\boxed{R=W=1.}
$$

There was no estimate of how close these complex numbers were to one.
The conclusion comes from their order and their arithmetic residues.
We can now unpack these exact comparisons.

*[Animation: Bring “odd order” and “residue 1” into the rigidity lemma
from two different branches. Reveal $R=1$ and $W=1$ as its two outputs.
Keep the original polynomial evaluation points distinct; only their
comparison products have been forced to equal one.]*

Source: [the paper, Lemma 3.3(ii) and equation (4.10)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
