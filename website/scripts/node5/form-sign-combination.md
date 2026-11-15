# Video 5.1 — Form the Combination

## Slide 1 — Keep track of the same signs

Our goal is to define $E(P)$ using integral quotients and then express it
through the original sign polynomials. For a positive integer $u$, work in
$\mathbb Z[i][P]/(P^{u^2}-1)$. Each coefficient of
$H_0(P),H_1(P),H_2(P),H_3(P)$ is $+1$ or $-1$.

The normalized evaluations from Node 3 are

$$
\begin{aligned}
c(P)&=\frac{H_0(P)+H_1(P)+H_2(P)+H_3(P)}2,\\
d(P)&=\frac{H_0(P)-H_1(P)+H_2(P)-H_3(P)}2,\\
g(P)&=\frac{H_0(P)-H_2(P)}2+i\frac{H_1(P)-H_3(P)}2.
\end{aligned}
$$

Their common signs will let us divide the two differences by $2$ and
$1+i$. We will justify those divisions before reducing any coefficients.

*[Animation: Display the three formulas. Connect matching copies of each
$H_a(P)$ with the same label. Highlight the $H_0(P)$ terms and show them
cancelling when subtracting $c(P)$ from the other two polynomials.]*

## Slide 2 — The quotients are integral

Direct subtraction gives

$$
\frac{d(P)-c(P)}2=-\frac{H_1(P)+H_3(P)}2.
$$

For the second difference, multiply by $(1-i)/2$, which equals
$1/(1+i)$. Collecting real and imaginary parts gives

$$
\begin{aligned}
\frac{g(P)-c(P)}{1+i}
&=-\frac{H_2(P)+H_3(P)}2\\
&\quad+i\frac{H_1(P)+H_2(P)}2.
\end{aligned}
$$

Every half-sum has integer coefficients. At any power of $P$, adding
two signs gives $-2$, $0$, or $2$, so dividing by two gives an integer.
The first quotient is an integer polynomial, and the second is a
Gaussian-integer polynomial.

*[Animation: Expand the two subtractions in polynomial notation. For the
second quotient, show multiplication by $(1-i)/2$ and collect real and
imaginary terms. Under each half-sum, display $\{-2,0,2\}/2=\{-1,0,1\}$.
Keep the label “before reduction” visible.]*

## Slide 3 — Add and collect

We can now define

$$
E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
$$

Adding the two formulas combines the two halves of $-H_3(P)$ and gives

$$
\boxed{E(P)=-H_3(P)+(i-1)\frac{H_1(P)+H_2(P)}2.}
$$

This is why the combination is useful: all dependence on $H_1(P)$ and
$H_2(P)$ is multiplied by $i-1=i(1+i)$, leaving one sign polynomial
after reduction. The next steps explain that reduction.

We also retain $2\mid d(P)-c(P)$ and $1+i\mid g(P)-c(P)$ for Node 6.
This coefficient calculation uses the common signs; it does not need the
norm identities or the oddness of $u$.

*[Animation: Combine the two $-H_3(P)/2$ terms, then collect the remaining
half-sums under $i-1$. Box the resulting identity. Put the two exact
divisibilities beside it as the outputs of this step.]*

Source: [the paper, Section 4, equations (4.1) and (4.5)–(4.9)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
