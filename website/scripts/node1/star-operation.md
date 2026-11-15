# Video 1.3 — The star operation

Goal: define star as cyclic reversal and verify it is a well-defined involution.

## Reversing the cyclic order

We know how to shift a row. Our next operation will reverse the order in which the cyclic positions are read.

For

$$
h(X)=\sum_{j=0}^{n-1}h_jX^j,
$$

define its star by

$$
h^*(X)=\sum_{j=0}^{n-1}h_jX^{-j}=h(X^{-1}).
$$

Since $X^{-1}=X^{n-1}$, this is still an element of the same ring.

The constant coefficient stays in place, while positions $1,2,\ldots,n-1$ are read backward. In coefficient notation,

$$
(h_0,h_1,\ldots,h_{n-1})\longmapsto(h_0,h_{n-1},\ldots,h_1).
$$

*[Animation: Show a circle with one marked starting position. Reverse the direction of the arrows around the circle; do not change the signs attached to the entries.]*

## Check the operation on our example

Let's first use four generic coefficients, so the reversal is visible:

$$
a+bX+cX^2+dX^3\longmapsto a+dX+cX^2+bX^3.
$$

Now return to the original row from our main video:

$$
h(X)=-1+X+X^2+X^3.
$$

Then

$$
\begin{aligned}
h^*(X)&=-1+X^{-1}+X^{-2}+X^{-3}\\
&=-1+X^3+X^2+X\\
&=-1+X+X^2+X^3=h(X).
\end{aligned}
$$

Our original row $(-1,1,1,1)$ is unchanged by the reversal because its final three entries are all equal.

*[Animation: First reflect the generic coefficients $(a,b,c,d)$ to $(a,d,c,b)$. Next switch to the original sign row $(-1,1,1,1)$: the reverse arrow acts, but the visible signs remain in place. Emphasize $h^*(X)=h(X)$ for this particular example.]*

## Why this is a legitimate algebraic operation

The rule works on the whole ring because if $X^n=1$, then also $(X^{-1})^n=1$. So replacing $X$ by $X^{-1}$ respects the relation that defines our ring.

Also, reversing twice gets us back where we started:

$$
(h^*)^*=h.
$$

And reversing the powers in a product reverses their exponents, so in our commutative group ring

$$
(fg)^*=f^*g^*.
$$

Thus star is an involution. It is a reversal operation, not a reciprocal $1/h$ and not a change of signs.

We introduced it because multiplying $h$ by this reversal has a remarkable effect: its coefficients encode dot products.
