# Supplied Node 8 outline

Transcribed from Steven's inline message. Wording and animation cues are
preserved below; pasted math delimiters and surrounding parentheses are
normalized to Markdown LaTeX. The edited production script is separate.

---

# Node 8 — The Final Contradiction

### Video 8: Why an Odd Number of Ones Finishes the Proof

## Scene 1 — Recall What We Know

*[Animation: Highlight Node 7 and display its conclusion.]*

In the previous video, we showed that a certain expression involving our polynomial $E(P)$ must be zero modulo $1+i$.

In our example, where $u=3$, this expression is

$$
\boxed{
\frac{E(1)}{c(1)}-\frac{E(\omega)}{c(\omega)}
\equiv 0\pmod{1+i}.
}
$$

But remember why we constructed $E(P)$ in the first place.

In Node 5, we showed that all its coefficients become one when reduced modulo $1+i$.

Thus, for our example, we can replace $E(P)$, modulo $1+i$, with

$$
\boxed{J(P)=1+P+P^2+\cdots+P^8.}
$$

Let's see what happens when we evaluate this polynomial at our two special values.

## Scene 2 — Evaluating at a Root of Unity

*[Animation: Draw the complex plane and display the three cube roots of unity $1,\omega,\omega^2$, represented by equally spaced arrows.]*

First, suppose we substitute $P=\omega$, a primitive cube root of unity.

Recall that

$$
1+\omega+\omega^2=0.
$$

And because our polynomial contains nine terms, we can group them into three copies of this sum.

Thus,

$$
\boxed{J(\omega)=0.}
$$

*[Animation: Display nine arrows arranged into three groups of three. Each group forms an equilateral triangle, and its arrows cancel to zero.]*

## Scene 3 — Evaluating at One

But what happens when we substitute $P=1$?

Now every term is one.

And since there are nine terms, we get

$$
J(1)=9.
$$

But nine is odd!

So when we reduce modulo $1+i$, we obtain

$$
\boxed{J(1)\equiv1\pmod{1+i}.}
$$

*[Animation: All nine arrows now point in the same direction. Count them, then illustrate that an odd number of ones reduces to one.]*

## Scene 4 — The Contradiction

So we've discovered that our polynomial behaves very differently at these two values.

At $\omega$, the terms cancel to zero.

But at one, an odd number of terms remains, which is nonzero modulo $1+i$.

Returning to our expression from Node 7, and accounting for its nonzero denominators, this tells us that

$$
\boxed{\mathcal S\equiv1\pmod{1+i}.}
$$

But Node 7 told us that

$$
\boxed{\mathcal S\equiv0\pmod{1+i}.}
$$

A contradiction!

*[Animation: Display the two conclusions side by side. Bring them together to reveal $0\equiv1$.]*

The same argument works for any odd $u>1$. The nontrivial roots of unity give zero, while substituting one gives an odd number of ones.

Thus, $u$ cannot be greater than one.

And since we already showed that any nontrivial circulant Hadamard matrix must have dimension $4u^2$, we conclude that the only possible dimensions are

$$
\boxed{n=1\quad\text{or}\quad n=4.}
$$

*[Animation: Return to the original $4\times4$ matrix. Illuminate all eight nodes of the proof dependency graph, then display the theorem.]*
