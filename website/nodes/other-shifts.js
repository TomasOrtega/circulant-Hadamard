export default {
  id: "other-shifts",
  title: "Other shifts must cancel",
  shortTitle: "Nonzero shifts",
  summary: "Distinct rows must have zero inner product.",
  video: null,
  foundation: true,
  equation: "C(k) = 0,   1 ≤ k < n",
  script: [
    "For a nonzero shift, entries that agree contribute +1 and entries that disagree contribute −1. Orthogonality requires these contributions to cancel.",
    "Together with C(0) = n, these equalities describe exactly the row conditions for a circulant Hadamard matrix.",
  ],
  children: [],
};
