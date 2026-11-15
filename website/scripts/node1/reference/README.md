# Node 1 source and production conventions

[hadamard-node-1-corrected.pdf](hadamard-node-1-corrected.pdf) is the supplied
16-page source for the main Node 1 narration, five zoom-in scripts, and refined
graph. The editable Markdown scripts restore PDF equations as LaTeX and omit
running page headers and footers. Punctuation and line wrapping are normalized.
The dictionary script makes the modulo-n exponent convention explicit.
Following Steven's subsequent notation request, the editable scripts now write
$h(X)h^*(X)$ explicitly and emphasize that the norm identity is an equality in
$\mathbb Z[X]/(X^n-1)$, with a constant polynomial on the right. The group ring
is named directly, without introducing an additional abbreviation. The archived
PDF remains unchanged.

| Source pages | Editable script |
| --- | --- |
| 3–5 | [Video 1 — Group-Ring Encoding](../group-ring-encoding.md) |
| 7–8 | [Video 1.1 — Group Ring](../cyclic-group-ring.md) |
| 8–9 | [Video 1.2 — Cyclic Shifts](../cyclic-shifts.md) |
| 10–11 | [Video 1.3 — Star Operation](../star-operation.md) |
| 12–13 | [Video 1.4 — Correlation Identity](../correlation-identity.md) |
| 14–15 | [Video 1.5 — Hadamard Dictionary](../hadamard-dictionary.md) |

Page 2 supplies the reader's dictionary, page 6 the refined graph, and page 16
the following production conventions:

- Keep the original first row $(-1,1,1,1)$, so
  $h=-1+X+X^2+X^3$ and $h^*=h$. Show reversal with generic coefficients
  $(a,b,c,d)\mapsto(a,d,c,b)$ before returning to this symmetric sign row.
- The main video demonstrates the coefficient identity at order four and
  states the general dictionary. Video 1.4 derives the general coefficient
  formula; Video 1.5 proves both implications.
- Work in $\mathbb Z[X]/(X^n-1)$. Reduce indices modulo $n$ and distinguish
  one-based narration from zero-based matrix-entry formulas. Star is not $1/h$.
- Root-of-unity evaluations and Fourier terminology do not belong in this node.
- Pair each equation with its coefficient strip or shifted row in the animation.

The five subnodes are teaching refinements supplied in this PDF, not numbered
lemmas from the research paper. Their natural-language website explanations
are adapted from these scripts. The website keeps the user's established preference
for uniform solid graph connections; the 1.1-to-1.4 connection retains its
shared-notation meaning in the data and node descriptions.
