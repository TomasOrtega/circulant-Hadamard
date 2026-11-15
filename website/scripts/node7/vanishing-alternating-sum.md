# Video 7.4 — Identify E(P) and Add the Sums

## Slide 1 — Two sums with the same inputs

Our goal is to combine the two vanishing sums into a single expression.
Let $u>1$ be odd, let $I$ be its distinct prime divisors, and put
$\zeta_S=\prod_{p\in S}\zeta_p$, with empty product $1$.
In $A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]$, abbreviate
$c_S=c(\zeta_S)$, and similarly $d_S,g_S$.
Node 7.3 gives

$$
\sum_S(-1)^{|S|}\frac{d_S-c_S}{2c_S}\equiv0,
\qquad
\sum_S(-1)^{|S|}\frac{g_S-c_S}{(1+i)c_S}\equiv0
\pmod{1+i}.
$$

Both congruences use the same quotient ring and the same subset indices,
so we can add them term by term.

*[Animation: Arrange the two sums in rows, with matching subset cards
in vertical columns. Put one shared “modulo $1+i$” label around both
rows and align the two zero residues at the right.]*

## Slide 2 — Recognize the polynomial we constructed

Recall the definition

$$
E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
$$

At each input, the two terms in a column add to

$$
\frac{d_S-c_S}{2c_S}+\frac{g_S-c_S}{(1+i)c_S}
=\frac{E(\zeta_S)}{c(\zeta_S)}.
$$

This is an exact identity of elements of $A$. The denominator is a
unit, and the divisions in the definition of $E(P)$ are exact
coefficientwise divisions.

*[Animation: Take one column out of the sum, factor out $1/c_S$, and
match the bracketed numerator with the definition of $E(P)$ evaluated
at $\zeta_S$. Repeat the replacement across all columns.]*

## Slide 3 — The general conclusion

Adding the congruences therefore gives

$$
\boxed{\mathcal S:=\sum_{S\subseteq I}(-1)^{|S|}
\frac{E(\zeta_S)}{c(\zeta_S)}\equiv0\pmod{1+i}.}
$$

The alternating signs record which factors came from the even and odd
products. Although plus and minus coincide after reduction to
characteristic two, these signs belong to the exact sum we constructed.

This conclusion follows from product identities for every odd $u>1$.
It does not require one common rotation across all the evaluation inputs.

*[Animation: Collapse the two rows into one alternating sum. Keep the
subset labels and their signs, then box the complete formula and its
zero residue.]*

## Slide 4 — Recover the guiding example

For $u=3$, the two inputs are $1$ and $\omega=e^{2\pi i/3}$, so

$$
\mathcal S=\frac{E(1)}{c(1)}-\frac{E(\omega)}{c(\omega)}=0
$$

exactly, as the common-rotation argument showed. The overview already
uses the all-ones residues to contradict this equality. For general
$u$, Node 8 applies the same coefficient congruence to the full subset
sum and gives its incompatible residue one.

*[Animation: Reduce the subset display to its two cards for $u=3$.
Match their normalized values and cancel their difference. Restore
the general sum with residue zero and bring in the next input
$E(P)\equiv J(P)\pmod{1+i}$.]*

Detailed exposition: [Node 7.4](../../nodes/vanishing-alternating-sum.md).
Source: the paper, Section 4, the additive step leading to equation (4.11).
