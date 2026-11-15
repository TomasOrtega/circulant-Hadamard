# Node 7 — From Products to Sums

## Video 7: The Example Contradiction and the General Sum

## Slide 1 — Start from the equality

For our guiding case $u=3$, Node 6 gave the exact identity

$$
\frac{E(\omega)}{c(\omega)}=\frac{E(1)}{c(1)},
\qquad \omega=e^{2\pi i/3}.
$$

Now we will use the all-ones congruence from Node 5 to show that these
two equal quantities would have different residues modulo $1+i$.

*[Animation: Carry the normalized equality forward from Node 6.
Under its two sides, place the input labels $P=\omega$ and $P=1$.
Bring in $E(P)\equiv J(P)\pmod{1+i}$ as the next input.]*

## Slide 2 — The contradiction for u=3

Recall $J(P)=1+P+\cdots+P^8$. At our two inputs,

$$
J(1)=9,\qquad J(\omega)=3(1+\omega+\omega^2)=0.
$$

Thus $E(1)\equiv1$ and $E(\omega)\equiv0$ modulo $1+i$.
The denominators remain invertible in the reduction ring, as established
in Node 6. Since $c(1)=\pm3\equiv1$, we obtain

$$
\frac{E(1)}{c(1)}\equiv1,\qquad
\frac{E(\omega)}{c(\omega)}\equiv0\pmod{1+i}.
$$

But these quantities are equal, and zero and one are distinct in our
reduction ring. This is the contradiction: $u=3$ cannot occur, so there
is no circulant Hadamard matrix of order $36$.

*[Animation: Under $P=1$, replace the nine terms by nine ones and show
residue $1$. Under $P=\omega$, group them into three vanishing sums
$1+\omega+\omega^2$. Keep the unit denominators visible, then attach
residues $1$ and $0$ to the two sides of the original equality. Mark the
conflict. Show residues in an algebra panel, not as positions on a circle.]*

## Slide 3 — When u has several prime divisors

When $u$ has several distinct prime divisors, the comparisons involve
more evaluations. For general odd $u>1$, let $I$ be the set of distinct
primes dividing $u$, and use the roots from Node 4:

$$
\zeta_S=\prod_{p\in S}\zeta_p,
\qquad \zeta_\varnothing=1.
$$

Node 6 gives identities between alternating products. Expanding those
products and using the sign divisibilities turns them into the sum
congruence

$$
\boxed{\mathcal S:=\sum_{S\subseteq I}(-1)^{|S|}
\frac{E(\zeta_S)}{c(\zeta_S)}\equiv0\pmod{1+i}.}
$$

The smaller nodes give the exact expansions and cancellations before
reduction. With several primes, we use these product identities rather
than assuming a common rotation between every pair of inputs.

The final node combines this vanishing sum with
$E(P)\equiv J(P)\pmod{1+i}$ to finish the contradiction for every odd
$u>1$.

*[Animation: Replace the two input cards by cards indexed by the subsets
$S$, with alternating plus and minus signs. Show the transition “exact
product identities → expand and cancel → sum congruence.” Keep the
cancellation before the “modulo $1+i$” step. End with
$\mathcal S\equiv0$ and highlight Node 8.]*

Source and production references: Steven's [supplied notes](reference/supplied-outline.md),
the [earlier rotation-and-cancellation storyboard](storyboards/rotation-cancellation.svg),
and [the paper, Section 4, Lemma 4.1 and equations (4.10)–(4.11)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
The storyboard's common-rotation construction is now covered in Node 6;
this script starts from its resulting equality.
