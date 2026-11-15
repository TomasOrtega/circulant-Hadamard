---
id: question
title: What are we trying to prove?
shortTitle: The question
summary: "Meet the two requirements: every row is a cyclic shift, and distinct
  rows are perpendicular."
video: null
children:
  - node: one-row
    dependsOn: []
    segment: null
    script: |
      Write the first row as $(a_0, \ldots, a_{n-1})$, with each entry equal to +1 or −1. Move the final entry to the front to obtain the next row, and repeat. After n shifts, the original row returns.
  - node: orthogonality
    dependsOn: []
    segment: null
    script: |
      The (r, s) entry of $HH^{\mathsf{T}}$ is the inner product of rows r and s. Every row has squared length n because its entries are signs. The Hadamard condition asks for zero inner products between different rows.
---

A Hadamard matrix has entries +1 and −1 and mutually orthogonal rows. A circulant matrix is determined by its first row: every later row is obtained by shifting the entries around a circle.

Our question concerns matrices that satisfy both requirements. These two viewpoints are the starting point for the argument.
