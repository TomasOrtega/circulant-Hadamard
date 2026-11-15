# Node 7 — From Products to Sums
### Video 7: One Rotation, One Vanishing Sum

## Scene 1 — Recall Our Common Rotation

*[Animation: Return to the two complex planes from Node 6. Each contains a circle of radius three, with three labeled points \(c,d,g\).]*

In the previous video, we discovered something remarkable about our three polynomials \(c\), \(d\), and \(g\).

Recall that we were working with the cyclic group of order nine, and evaluating our polynomials at two values: \(P=1\) and \(P=\omega\), where \(\omega\) is a primitive cube root of unity.

We showed that all three points undergo exactly the same rotation when we move from one evaluation to the other.

In particular, there is some complex number \(\lambda\) of absolute value one such that

\[
\boxed{
\begin{aligned}
c(\omega)&=\lambda c(1),\\
d(\omega)&=\lambda d(1),\\
g(\omega)&=\lambda g(1).
\end{aligned}
}
\]

*[Animation: Rotate all three points simultaneously through the same angle \(\lambda\). The shape formed by the points remains unchanged.]*

So although we have three different polynomials, their values cannot move independently.

They must all rotate together.

## Scene 2 — Returning to Our Polynomial E

*[Animation: Highlight Node 5 in the proof dependency graph, then return to the circles.]*

Now recall that in Node 5, we constructed a new polynomial \(E(P)\) by combining our three polynomials.

In particular, we defined

\[
\boxed{
E(P)=\frac{d(P)-c(P)}{2}
+\frac{g(P)-c(P)}{1+i}.
}
\]

Let's try to understand this geometrically.

The expression \(d(P)-c(P)\) describes the arrow going from the point \(c(P)\) to the point \(d(P)\).

Similarly, \(g(P)-c(P)\) describes the arrow from \(c(P)\) to \(g(P)\).

We scale these two arrows and add them together to obtain \(E(P)\).

*[Animation: Draw arrows from \(c\) to \(d\) and from \(c\) to \(g\). Scale them by their respective complex factors, then add them head-to-tail to construct the arrow representing \(E\).]*

Now here's the important observation.

If all three points rotate by the same angle, then the arrows joining them must rotate by that same angle.

And scaling and adding these arrows preserves that common rotation.

Therefore, our new polynomial \(E\) must also undergo exactly the same rotation!

\[
\boxed{E(\omega)=\lambda E(1).}
\]

*[Animation: Show \(E(1)\) as a fourth arrow. Rotate the entire configuration, including \(E\), by the same angle \(\lambda\).]*

## Scene 3 — Eliminating the Rotation

We now know two things:

\[
E(\omega)=\lambda E(1)
\]

and

\[
c(\omega)=\lambda c(1).
\]

Both expressions involve the same rotation.

So what happens if we divide the first by the second?

The rotation cancels!

\[
\frac{E(\omega)}{c(\omega)}
=
\frac{\lambda E(1)}{\lambda c(1)}
=
\frac{E(1)}{c(1)}.
\]

Thus,

\[
\boxed{
\frac{E(1)}{c(1)}
-
\frac{E(\omega)}{c(\omega)}
=0.
}
\]

*[Animation: Show both configurations. Rotate and normalize each one so that the \(c\)-arrow points to the same position. The two \(E\)-arrows now coincide. Subtract them, and they cancel.]*

This is the key observation of Node 7.

We started with relationships between products of algebraic numbers, and have obtained a relationship between sums.

In fact, we've shown that this particular difference is exactly zero.

So it is certainly zero modulo \(1+i\).

\[
\boxed{
\frac{E(1)}{c(1)}
-
\frac{E(\omega)}{c(\omega)}
\equiv0\pmod{1+i}.
}
\]

*[Animation: The two expressions appear with a minus sign between them, then cancel, leaving zero.]*

## Scene 4 — The General Statement

Now, our example was particularly simple because we only needed to compare two evaluations: \(P=1\) and \(P=\omega\).

For a general odd integer \(u\), we may need to evaluate at several different roots of unity.

The idea remains the same, although the algebra becomes more complicated.

Instead of a difference of two terms, we obtain an alternating sum over the roots of unity introduced in Node 4.

The general result is

\[
\boxed{
\sum_S(-1)^{|S|}
\frac{E(\zeta_S)}{c(\zeta_S)}
\equiv0\pmod{1+i}.
}
\]

Here, \(S\) runs over subsets of the distinct prime divisors of \(u\), and \(\zeta_S\) is the corresponding product of roots of unity.

We won't need the details of this more general calculation for our picture.

The important point is that the relationships from Node 6 force this alternating sum to vanish modulo \(1+i\).

*[Animation: Begin with our two evaluations \(1\) and \(\omega\). Briefly show how additional evaluations introduce more terms, with alternating plus and minus signs. Then collapse the expression into a single symbol \(\mathcal S\).]*

Thus, we have established

\[
\boxed{\mathcal S\equiv0\pmod{1+i}.}
\]

## Scene 5 — Setting Up the Contradiction

But remember why we constructed \(E(P)\) in the first place.

In Node 5, we showed that all its coefficients become one when reduced modulo \(1+i\).

We haven't used that fact yet!

And in the next video, we'll see that this forces our alternating sum to be nonzero modulo \(1+i\).

But we just proved that it must be zero.

That will give us the contradiction needed to finish the proof.

*[Animation: Highlight Node 7 and its conclusion \(\mathcal S\equiv0\). Then illuminate Node 8, leaving the contradiction unresolved until the next video.]*
