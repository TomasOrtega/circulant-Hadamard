# Video 2.5 — Fold the Cycle

## Slide 1 — One step of the descent

Suppose $T(X)$ has odd coefficients on a cycle of length $2^k$, with

$$
T(X)T^*(X)=2^{2t}w^2,\qquad t\geq2,\quad w\text{ odd}.
$$

Our goal is to halve the cycle while keeping odd coefficients and
dividing the scalar norm by four.

*[Animation: Put the cycle length $2^k$ and norm $2^{2t}w^2$ beside
a circle with opposite positions paired. Preview the updates
$k\mapsto k-1$ and $t\mapsto t-1$.]*

## Slide 2 — Average opposite coefficients

The comparison lemma says opposite coefficients agree modulo $2^t$,
and hence modulo four. Write the pair as $a_j$ and $a_j+4r_j$.
Their average is

$$
b_j=\frac{a_j+(a_j+4r_j)}2=a_j+2r_j,
$$

which is still odd. For instance, the average of $3$ and $7$ is $5$.
Apply this to every opposite pair.

*[Animation: Fold the circle so each opposite pair meets. Show a pair
as “odd $a_j$” and “$a_j+4r_j$,” add them, then divide by two.
Highlight the remaining odd term plus an even term.]*

## Slide 3 — Check the new norm

Let $q$ project onto the half-length cycle, and let $T_1(X)$ have the
averages as its coefficients. Opposite coefficients add under projection,
so $q(T(X))=2T_1(X)$. Projection respects star and multiplication:

$$
4T_1(X)T_1^*(X)=2^{2t}w^2.
$$

Dividing the integer coefficients by four gives

$$
T_1(X)T_1^*(X)=2^{2(t-1)}w^2.
$$

Thus one fold has exactly the two effects we wanted.

*[Animation: Apply the projection to both factors of the norm identity.
Replace each projected factor by twice the averaged polynomial. Combine
the two factors of two into four and divide both sides by four.]*

## Slide 4 — Repeat with the indices visible

Start at $k=2s$ and $t=s$, assuming $s\geq2$. After $j$ folds,

$$
k=2s-j,\qquad t=s-j.
$$

The initial case $j=0$ is Node 2.3's projection. Whenever $j<s-1$,
we have $t\geq2$, so the same folding argument proves the next step
and keeps every coefficient odd.

After $s-1$ folds, the length is $2^{s+1}$ and the norm is $4w^2$.
The next node shows why that endpoint is impossible.

*[Animation: Build a table with columns “folds,” “length,” and “norm.”
Start with $0,2^{2s},2^{2s}w^2$, advance the general row $j$, and end
at $s-1,2^{s+1},4w^2$. Keep “all coefficients odd” beside every row.
Stop there rather than applying a step with $t=1$.]*

Source: [the paper, Section 2](https://github.com/openai/math/blob/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf).
