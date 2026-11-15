# Instructions for Codex — Node 6: Odd-Order Rigidity

Create an outline and narration script for the main-level video of Node 6, titled **Odd-Order Rigidity**.

Use our established 3Blue1Brown-style approach: visual intuition first, precise mathematical statements, and minimal technical machinery. Do not use Fourier terminology.

The video should focus on the case \(u=3\), where our group ring is based on \(C_9\). State the general conclusion as well, but leave its detailed proof to the zoomed-in nodes.

## Scene 1 — Returning to Our Three Polynomials

Recall that in Node 3, we constructed three polynomials \(c(P),d(P),g(P)\) satisfying

\[
cc^*=dd^*=gg^*=9.
\]

Thus, when we evaluate any of these polynomials at \(P=1\) or at a primitive cube root of unity \(\omega\), the resulting complex number lies on the circle of radius three.

**Animation:** Display two complex planes side by side, each with a circle of radius three.

The left circle represents evaluation at \(P=1\), and the right circle represents evaluation at \(P=\omega\).

On each circle, place three labeled points corresponding to \(c,d,g\).

These are illustrative positions, not actual values from an order-36 Hadamard matrix.

## Scene 2 — Measuring the Relative Rotations

Recall from Node 4 that we defined

\[
\Delta(f)=\frac{f(1)}{f(\omega)}.
\]

This measures the relative phase between the two evaluations.

The Δ-theorem tells us that

\[
\Delta(c),\quad\Delta(d),\quad\Delta(g)
\]

are roots of unity of odd order.

For our example, they must be cube roots of unity.

Now define two new quantities:

\[
\boxed{
R=\frac{\Delta(d)}{\Delta(c)},
\qquad
W=\frac{\Delta(g)}{\Delta(c)}.
}
\]

These compare the relative rotations of \(d\) and \(g\) with that of \(c\).

Because they are quotients of roots of unity of odd order, \(R\) and \(W\) are themselves roots of unity of odd order.

**Animation:** Use \(c\) as our reference point. Show how the relative rotations of \(d\) and \(g\) may initially differ from that of \(c\).

Display \(R\) and \(W\) as these differences in relative rotation.

## Scene 3 — The Congruence from the Original Signs

Now recall the special information from Node 5.

Because our original matrix had only positive and negative one entries, we know that

\[
d-c\equiv0\pmod2,
\qquad
g-c\equiv0\pmod{1+i}.
\]

When we evaluate at \(1\) and \(\omega\), these congruences tell us that

\[
\boxed{
R\equiv W\equiv1\pmod{1+i}.
}
\]

Thus, we have discovered that \(R\) and \(W\) satisfy two simultaneous conditions:

- They are roots of unity of odd order.
- They are congruent to one modulo \(1+i\).

**Animation:** Return to the unit circle and show the three possible cube roots of unity:

\[
1,\qquad\omega,\qquad\omega^2.
\]

Highlight the algebraic congruence condition, which singles out the value \(1\).

Important: Congruence modulo \(1+i\) does **not** mean geometrically close to one. Do not depict it as a small angular distance.

## Scene 4 — Odd-Order Rigidity

Here we use an elementary fact:

**A root of unity of odd order that is congruent to one modulo \(1+i\) must actually equal one.**

We can explain this briefly, or accept it as a black box.

Therefore,

\[
\boxed{R=W=1.}
\]

This is the key conclusion of Node 6.

**Animation:** The differences in relative rotation disappear. The three points are now constrained to rotate together.

## Scene 5 — The Common Rotation

Let's understand what \(R=W=1\) actually means.

The identity \(R=1\) implies

\[
\frac{d(1)}{c(1)}
=
\frac{d(\omega)}{c(\omega)}.
\]

Similarly, \(W=1\) implies

\[
\frac{g(1)}{c(1)}
=
\frac{g(\omega)}{c(\omega)}.
\]

Define

\[
\lambda=\frac{c(\omega)}{c(1)}.
\]

Since both values have absolute value three, \(|\lambda|=1\).

Consequently,

\[
\boxed{
(c(\omega),d(\omega),g(\omega))
=
\lambda(c(1),d(1),g(1)).
}
\]

**This is the geometric heart of the video.**

All three points undergo exactly the same rotation when we move from the evaluation at \(P=1\) to the evaluation at \(P=\omega\).

**Animation:** Display the two complex circles side by side again. Animate all three points rotating by the same angle, preserving their relative positions.

Use one arrow labeled \(\lambda\) to represent this common rotation.

## Scene 6 — Why This Matters

We have started with three apparently independent polynomials.

The Δ-theorem restricted their possible relative phases. The congruences from our original signs then forced those phase differences to disappear.

Thus, evaluating at \(P=1\) and \(P=\omega\) cannot move the three points independently. They must all undergo the same rotation.

This is a remarkably rigid constraint.

In Node 7, we will turn these multiplicative relationships into additive ones. Combined with our polynomial \(E(P)\), they will lead us to the final contradiction.

End the video by highlighting Node 7 in the proof dependency graph.

## General statement to include

For arbitrary odd \(u>1\), define

\[
R=\frac{\Delta(d)}{\Delta(c)},
\qquad
W=\frac{\Delta(g)}{\Delta(c)}.
\]

By the Δ-theorem and the sign congruences,

\[
R,W\text{ have odd order},
\qquad
R\equiv W\equiv1\pmod{1+i}.
\]

Odd-order rigidity therefore gives

\[
\boxed{R=W=1.}
\]

For general \(u\), this is a statement about alternating products over several evaluations. The simple common-rotation picture is specific to the one-prime example and should not be claimed as the literal general statement.

## Style requirements

- Prioritize the two-circle visualization.
- Keep the narration conversational and accessible.
- Do not use Fourier language.
- Do not repeat the proof of the Δ-theorem.
- Do not introduce the alternating sums from Node 7 yet.
- Distinguish algebraic congruence from geometric proximity.
- Do not call the roots of unity primitive unless primitivity is specifically required.
- End with the exact statement \(R=W=1\) and its geometric interpretation.
