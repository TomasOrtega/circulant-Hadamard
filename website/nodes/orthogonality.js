export default {
  id: "orthogonality",
  title: "Orthogonality in one equation",
  shortTitle: "Orthogonality",
  summary: "Read the matrix identity as a collection of row inner products.",
  video: null,
  foundation: true,
  equation: "HHᵀ = nIₙ",
  script: [
    "The (r, s) entry of HHᵀ is the inner product of rows r and s. Every row has squared length n because its entries are signs. The Hadamard condition asks for zero inner products between different rows.",
    "We assume familiarity with inner products, transposes, and the identity matrix from undergraduate linear algebra.",
  ],
  children: [],
};
