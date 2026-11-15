# Video 5.2 — Gaussian Parity

## Slide 1 — Divisibility by 1+i

We need a parity rule for Gaussian integers, numbers of the form $a+bi$
with $a,b$ integers. Reducing modulo $1+i$ identifies two numbers when
their difference is a Gaussian-integer multiple of $1+i$.

To test divisibility, calculate

$$
\frac{a+bi}{1+i}=\frac{a+b}{2}+i\frac{b-a}{2}.
$$

This quotient has integer real and imaginary parts exactly when $a$ and
$b$ have the same parity. Equivalently, $a+b$ must be even.

*[Animation: Multiply numerator and denominator by $1-i$, then separate
the real and imaginary parts. Highlight the two halves. Show a table
with “same parity” giving two integers and “different parity” giving
two nonintegers.]*

## Slide 2 — Only two residues

The residue of $a+bi$ is therefore determined by $a+b$ modulo two:

$$
a+bi\longmapsto a+b\pmod2.
$$

For example, $3+i$ has residue zero, while $3+2i$ has residue one.
This reduction respects addition and multiplication: it is the map
sending $i$ to $1$ in the two-element field $\mathbb F_2$.

In particular,

$$
\boxed{i\equiv1,\qquad -1\equiv1\pmod{1+i}.}
$$

Indeed, $i-1=i(1+i)$ and $2=(1+i)(1-i)$. Both signs have the same
residue, even though they are different Gaussian integers.

*[Animation: Send the examples through a box labeled “real part +
imaginary part, modulo 2.” Give them outputs $0$ and $1$. Then send
$1,-1,i,-i$ to residue $1$. Display the factor identities beside the
arrows; these arrows represent a reduction map, not complex rotations.]*

## Slide 3 — Reduce coefficients after dividing

For a positive integer $u$, apply this rule to each polynomial coefficient:

$$
\mathbb Z[i][P]/(P^{u^2}-1)
\longrightarrow\mathbb F_2[P]/(P^{u^2}-1).
$$

The powers of $P$ and their cycle relation remain. Only the coefficients
change. For example, $i-P$ reduces to $1+P$.

There is one ordering rule to remember. Both $2$ and $1+i$ become zero
after reduction. We cannot divide by them in the quotient. In defining
$E(P)$, we first used sign parity to form exact integral quotients, and
only then reduced their coefficients.

*[Animation: Keep the powers $1,P,P^2,\ldots$ fixed while their coefficient
labels change. Show $i-P\mapsto1+P$. End with a two-step sequence:
“form integral quotients” followed by “reduce coefficients.” Mark $2$
and $1+i$ as zero only in the second step.]*

Source: [the paper, Section 4, equations (4.5)–(4.9)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
