# Video 6.5 — Exact Comparisons and a Common Rotation

## Slide 1 — Unpack the exact products

Let $u>1$ be odd, with distinct prime divisors $I$ and subset roots
$\zeta_S=\prod_{p\in S}\zeta_p$ as in Node 4. Write
$c_S=c(\zeta_S)$, and similarly $d_S,g_S$. The conclusion $R=W=1$
means

$$
\begin{aligned}
\prod_{S\subseteq I}\left(\frac{d_S}{c_S}\right)^{(-1)^{|S|}}&=1,\\
\prod_{S\subseteq I}\left(\frac{g_S}{c_S}\right)^{(-1)^{|S|}}&=1.
\end{aligned}
$$

These are exact equalities in the evaluation ring. Equivalently, each
product over even subsets equals the corresponding product over odd
subsets. Every denominator is a unit, so rearranging is legitimate.

*[Animation: Open the definitions of $R$ and $W$. Move the factors with
negative exponents to the other side. Arrange even and odd subsets in
two rows, joined by an equality sign.]*

## Slide 2 — Two inputs give one rotation

For $u=3$, the two inputs are $1$ and $\omega=e^{2\pi i/3}$. The product
identities reduce to

$$
\frac{d(1)}{c(1)}=\frac{d(\omega)}{c(\omega)},\qquad
\frac{g(1)}{c(1)}=\frac{g(\omega)}{c(\omega)}.
$$

Set $\lambda=c(\omega)/c(1)$. The norm identities give magnitude three
to both values, so $|\lambda|=1$. Rearranging yields

$$
\begin{aligned}
c(\omega)&=\lambda c(1),\\
d(\omega)&=\lambda d(1),\\
g(\omega)&=\lambda g(1).
\end{aligned}
$$

The three values share a rotation. Their relative positions are preserved;
they need not be the same point. The forward multiplier is
$\lambda=\Delta(c)^{-1}$, the inverse of the Δ-comparison.

*[Animation: Collapse each product row to its single factor. Rearrange
the resulting ratios to display the shared multiplier. Rotate the
three labeled arrows together between two radius-three circles,
preserving the arcs between them. Label the forward direction $\lambda$.]*

## Slide 3 — The combination E(P) follows

Recall the exact integral combination

$$
E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
$$

Substitution of the shared-rotation identities gives

$$
\begin{aligned}
E(\omega)
&=\frac{\lambda d(1)-\lambda c(1)}2
+\frac{\lambda g(1)-\lambda c(1)}{1+i}\\
&=\lambda E(1).
\end{aligned}
$$

Divide by $c(\omega)=\lambda c(1)$ to cancel the same multiplier:

$$
\boxed{\frac{E(\omega)}{c(\omega)}=\frac{E(1)}{c(1)}.}
$$

We divide by the nonzero unit values of $c(P)$, never by $E(1)$.
The argument therefore also covers $E(1)=0$. The divisions by $2$ and
$1+i$ defining $E(P)$ were exact divisions before reduction.

*[Animation: Insert the three copies of $\lambda$, factor them out,
and draw the resulting $E(\omega)$ arrow. It need not lie on the
radius-three circle. Divide each diagram by its own $c$-value and
show the two normalized $E$ arrows coincide.]*

## Slide 4 — What the example teaches

For a schematic, take $c(1)=3$, $d(1)=-3$, and $g(1)=3i$, and rotate
all three by $\lambda=\omega$. The combination gives $E(1)=-3+3i$;
both normalized $E$ values equal $-1+i$. These values illustrate the
shared rotation, not a construction satisfying all Hadamard conditions.

The exact normalized equality does not imply that the raw values
$E(1)$ and $E(\omega)$ are equal or have equal residues. They differ
by $\lambda$, which may have nontrivial residue.

With several distinct prime divisors of $u$, keep the general product
identities from the first slide. We cannot assume one common rotation
between every pair of inputs. Node 7 uses the normalized equality to
finish the guiding case and uses product expansion for the general case.

*[Animation: Show the schematic normalized point $-1+i$ on both planes.
Then return to the subset-indexed products for general $u$. Label the
two outputs “two-input equality” and “general product identities,” and
pass both to Node 7 without assigning all-ones residues to the schematic.]*

Source: [the paper, Section 4, equations (4.3), (4.4), and (4.10)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
