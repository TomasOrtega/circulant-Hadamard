# Video 3.2 — Four Sign Polynomials

## Slide 1 — Group the four powers of Z

In our new coordinates, the relation $Z^4=1$ leaves only the powers
$1,Z,Z^2,Z^3$. Our goal is to group together the terms having each of
those four powers.

Every term has the form $h_{a,b}Z^aP^b$, where $h_{a,b}$ is a sign,
$0\leq a<4$, and $0\leq b<u^2$.

*[Animation: Display representative terms $h_{a,b}Z^aP^b$ with their
$Z$ powers highlighted. Move them into four labeled groups. Keep the
coefficient and its $P$ power together as the terms move.]*

## Slide 2 — Name the four polynomials

For each $a$, collect the coefficients into

$$
H_a(P)=\sum_{b=0}^{u^2-1}h_{a,b}P^b.
$$

Then

$$
\begin{aligned}
h(Z,P)&=H_0(P)+ZH_1(P)\\
&\quad+Z^2H_2(P)+Z^3H_3(P).
\end{aligned}
$$

The monomials $Z^aP^b$ form the group-ring basis, so their coefficients
are unique. We have only regrouped terms; each $H_a(P)$ still has
$u^2$ sign coefficients.

*[Animation: Replace each group by the label $H_a(P)$, leaving its
common factor $Z^a$ outside. Re-expand one group to show that none of
its individual coefficients has changed.]*

## Slide 3 — The coefficients that will combine

At order $36$, each $H_a(P)$ has nine coefficient positions. For a
fixed power $P^b$, the four signs

$$
h_{0,b},\ h_{1,b},\ h_{2,b},\ h_{3,b}
$$

will combine when we evaluate $Z$. Their sums and differences will
also explain why division by two is integral.

Our output is the four-polynomial expression, ready for those two
independent checks: evaluation preserves the norm, and parity permits
normalization.

*[Animation: Align only the four terms containing a chosen $P^b$.
Highlight their coefficients while leaving all other powers muted.
End with two outgoing labels: “evaluate $Z$” and “check parity.”]*

Source: [the paper, Section 4, equations (4.1)–(4.2)](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
