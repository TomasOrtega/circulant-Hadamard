# Video 8.3 — One Surviving Odd Term

## Slide 1 — Replace E(P) by the all-ones polynomial

Our goal is to evaluate the residue of

$$
\mathcal S=\sum_{S\subseteq I}(-1)^{|S|}
\frac{E(\zeta_S)}{c(\zeta_S)}.
$$

Here $u>1$ is odd, $I$ is its distinct prime divisors, and
$\zeta_S=\prod_{p\in S}\zeta_p$, with empty product $1$.
Node 5 gives $E(P)\equiv J(P)\pmod{1+i}$ coefficientwise, where
$J(P)=1+P+\cdots+P^{u^2-1}$.
Evaluation preserves this congruence in
$A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]$.

*[Animation: Display the full subset-indexed sum. Under a shared
“modulo $1+i$” label, replace every numerator $E(\zeta_S)$ with
$J(\zeta_S)$ while leaving the signs and denominators in place.]*

## Slide 2 — Why division preserves the congruence

The denominators are units, with explicit inverses

$$
c(\zeta_S)^{-1}=\frac{\overline{c(\zeta_S)}}{u^2}.
$$

Their inverses still multiply to one after reduction. Multiplying each
congruence by this inverse therefore gives

$$
\mathcal S\equiv\sum_{S\subseteq I}(-1)^{|S|}
\frac{J(\zeta_S)}{c(\zeta_S)}\pmod{1+i}.
$$

The justification is invertibility in this ring, not merely a nonzero
complex value.

*[Animation: Take one denominator out of the sum, display its inverse,
and multiply to obtain $1$. Carry that identity through the reduction
arrow, then restore the denominator to the sum.]*

## Slide 3 — Remove every nonempty-subset term

Node 8.1 proves $J(\zeta_S)=0$ exactly for every nonempty subset $S$.
All of those terms vanish. The empty subset has sign $+1$ and evaluates
at $1$. Node 8.2 gives

$$
\mathcal S\equiv\frac{J(1)}{c(1)}
=\frac{u^2}{\pm u}=\pm u\equiv1\pmod{1+i}.
$$

Thus the entire sum has residue one.

*[Animation: Cross out each nonempty-subset numerator using its exact
zero. Keep the denominator visible until the corresponding whole term
becomes zero. Enlarge the single surviving empty-subset term and
simplify it to residue $1$.]*

## Slide 4 — See the same calculation with two primes

For $u=15$, the subset signs are $+,-,-,+$. The three nonempty subsets
have orders $3$, $5$, and $15$, and all three numerators vanish. The
remaining quotient is $225/(\pm15)=\pm15$, again residue one.

Only one term survives regardless of how many distinct primes divide
$u$. This is the residue we will compare with Node 7's zero residue.

*[Animation: Display the four terms for subsets of $\{3,5\}$.
Erase the three zero terms and reduce $\pm15$ to $1$. Place this
result beside the retained formula $\mathcal S\equiv0$ from Node 7.]*

Detailed exposition: [Node 8.3](../../nodes/surviving-odd-term.md).
Source: the paper, Section 4, the final evaluation of equation (4.11).
