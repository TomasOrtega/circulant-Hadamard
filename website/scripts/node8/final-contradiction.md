# Node 8 — The Final Contradiction

## Video 8: Finish the General Argument

## Slide 1 — One surviving term

Node 7 gives $\mathcal S\equiv0\pmod{1+i}$ for general odd $u>1$.
Now use the all-ones congruence

$$
E(P)\equiv J(P)=1+P+\cdots+P^{u^2-1}\pmod{1+i}.
$$

At every nontrivial root $\zeta_S$, the geometric sum cancels. At one,
all $u^2$ terms contribute one:

$$
J(\zeta_S)=0\quad(S\ne\varnothing),\qquad J(1)=u^2.
$$

These are exact evaluations before reduction. The denominators
$c(\zeta_S)$ remain units, so only the empty-subset term survives in
the alternating sum. Since $c(1)=\pm u$,

$$
\mathcal S\equiv\frac{J(1)}{c(1)}
=\pm u\equiv1\pmod{1+i}.
$$

The final residue is one because $u$ is odd.

*[Animation: Recall the subset-indexed sum from Node 7. Replace each
$E(\zeta_S)$ by $J(\zeta_S)$ under a “modulo $1+i$” label. Cross out
all nonempty-subset terms using their zero numerators. For the surviving
term, show $u^2/(\pm u)=\pm u$, then reduce the odd integer to $1$.]*

## Slide 2 — Only orders one and four remain

We now have two incompatible conclusions:

$$
\mathcal S\equiv0\pmod{1+i},\qquad
\mathcal S\equiv1\pmod{1+i}.
$$

Our reduction ring is nonzero, so this is a contradiction. It rules out
every odd $u>1$.

Node 2 told us that an order $n>1$ must be $4u^2$ with $u$ odd.
Only $u=1$ remains, giving $n=4$, alongside the separate case $n=1$.
Both occur: use $(1)$ at order one and our circulant example with first
row $(-1,1,1,1)$ at order four.

> **Theorem (Circulant Hadamard).** *A real circulant Hadamard matrix
> exists if and only if its order is $1$ or $4$.*

*[Animation: Bring the two residues together to show the impossible
claim $0=1$. Return to $n=4u^2$, remove $u>1$, and display $n=4$ beside
$n=1$. Recall the two example matrices and illuminate all eight proof
nodes as the theorem appears.]*

Source and production references: Steven's [supplied notes](reference/supplied-outline.md),
the [odd-ones storyboard](storyboards/odd-ones.svg), and
[the paper, Section 4, equation (4.11) and the final contradiction](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
The storyboard's nine-term example is a visual reference for the general
cancellation and oddness argument above.
