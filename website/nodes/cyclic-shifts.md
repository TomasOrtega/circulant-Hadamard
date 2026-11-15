---
id: cyclic-shifts
title: Cyclic Shifts
shortTitle: Cyclic Shifts
summary: "Multiplying by X moves the last coefficient to the first position: one
  right cyclic shift."
number: "1.2"
draft: false
video:
  src: media/cyclic-shifts.mp4
  poster: media/thumbnails/cyclic-shifts.jpg
  captions: media/cyclic-shifts.vtt
  duration: 102.8
mapPosition:
  - 40
  - 180
mapSummary: 'Row $j$ $\leftrightarrow$ $X^{j-1}h(X)$'
foundation: true
---

## Multiplication implements a shift

Work in $\mathbb Z[X]/(X^n-1)$ and encode a row by

$$
h(X)=h_0+h_1X+\cdots+h_{n-1}X^{n-1}.
$$

Using $X^n=1$,

$$
Xh(X)=h_{n-1}+h_0X+\cdots+h_{n-2}X^{n-1}.
$$

The coefficient list changes from $(h_0,\ldots,h_{n-1})$ to $(h_{n-1},h_0,\ldots,h_{n-2})$. This is exactly one cyclic shift to the right.

## Any number of shifts

> **Proposition.** For any integer $r$, the coefficient of $X^j$ in $X^rh$ is $h_{j-r}$, with all subscripts reduced modulo $n$.

**Proof.** A term $h_kX^{k+r}$ contributes to position $j$ precisely when $k+r\equiv j\pmod n$, or $k\equiv j-r\pmod n$. This selects exactly one coefficient.

Consequently the $j$-th row, when rows are numbered $1,\ldots,n$, corresponds to $X^{j-1}h$. In formulas we instead number rows and columns $0,\ldots,n-1$ and write

$$
H_{rj}=h_{j-r}.
$$

For the fixed example, $h(X)=-1+X+X^2+X^3$ and $Xh(X)=1-X+X^2+X^3$, corresponding to the second row $(1,-1,1,1)$. After $n$ shifts, $X^nh(X)=h(X)$.

**Output.** Every row of the circulant matrix is represented by a power of $X$ times the same polynomial.
