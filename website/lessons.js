export const lessons = {
  id: "overview",
  title: "The circulant Hadamard conjecture",
  shortTitle: "Overview",
  summary:
    "A guided route through the question, the structure behind it, and the argument we are developing.",
  video: null,
  clip: null,
  paragraphs: [
    "Start with the overview, then read the chapters below. Each short clip will explain one part of the story. Follow ‘Dig in deeper’ when you want the next layer of detail, and return to the bigger picture whenever you are ready.",
    "This is a draft lesson outline. The proof chapters and videos are still being prepared; the background sections illustrate how the finished lesson will work.",
  ],
  chapters: [
    {
      id: "question",
      title: "What are we trying to prove?",
      shortTitle: "The question",
      summary:
        "Meet the two requirements: every row is a cyclic shift, and distinct rows are perpendicular.",
      video: null,
      clip: null,
      paragraphs: [
        "A Hadamard matrix has entries +1 and −1 and mutually orthogonal rows. A circulant matrix is determined by its first row: every later row is obtained by shifting the entries around a circle.",
        "Our question concerns matrices that satisfy both requirements. These two viewpoints are the starting point for the argument.",
      ],
      chapters: [
        {
          id: "one-row",
          title: "One row determines the matrix",
          shortTitle: "Cyclic shifts",
          summary:
            "Use a cyclic shift to build every row from a single sign sequence.",
          video: null,
          clip: null,
          foundation: true,
          paragraphs: [
            "Write the first row as (a₀, …, aₙ₋₁), with each entry equal to +1 or −1. Move the final entry to the front to obtain the next row, and repeat. After n shifts, the original row returns.",
            "The same sign sequence contains all the information in the matrix.",
          ],
          chapters: [],
        },
        {
          id: "orthogonality",
          title: "Orthogonality in one equation",
          shortTitle: "Orthogonality",
          summary:
            "Read the matrix identity as a collection of row inner products.",
          video: null,
          clip: null,
          foundation: true,
          equation: "HHᵀ = nIₙ",
          paragraphs: [
            "The (r, s) entry of HHᵀ is the inner product of rows r and s. Every row has squared length n because its entries are signs. The Hadamard condition asks for zero inner products between different rows.",
            "We assume familiarity with inner products, transposes, and the identity matrix from undergraduate linear algebra.",
          ],
          chapters: [],
        },
      ],
    },
    {
      id: "structure",
      title: "Translate the circulant structure",
      shortTitle: "The structure",
      summary:
        "Replace a matrix full of row comparisons with correlations of the first row and its shifts.",
      video: null,
      clip: null,
      paragraphs: [
        "Because the rows are shifts of the same sequence, their inner products depend only on the relative shift. Cyclic correlations express those comparisons directly in terms of the first row.",
        "A small example lets us check this translation before asking what restrictions it imposes in general.",
      ],
      chapters: [
        {
          id: "correlations",
          title: "Turn row comparisons into correlations",
          shortTitle: "Correlations",
          summary: "A single function records all the inner products we need.",
          video: null,
          clip: null,
          equation: "C(k) = Σⱼ aⱼ aⱼ₊ₖ",
          paragraphs: [
            "Sum over j = 0, …, n − 1, reading every subscript modulo n. Then C(k) compares the sign sequence with a cyclic shift of itself.",
            "The Hadamard condition becomes C(0) = n and C(k) = 0 for every nonzero shift k modulo n. The next two sections separate those cases.",
          ],
          chapters: [
            {
              id: "zero-shift",
              title: "The zero shift fixes the length",
              shortTitle: "Zero shift",
              summary: "Comparing a sign sequence with itself gives n.",
              video: null,
              clip: null,
              foundation: true,
              equation: "C(0) = Σⱼ aⱼ² = n",
              paragraphs: [
                "Every squared entry equals 1, so this sum has n terms equal to 1. This accounts for the diagonal of HHᵀ.",
                "The diagonal is fixed automatically. The nonzero shifts carry the remaining restrictions.",
              ],
              chapters: [],
            },
            {
              id: "other-shifts",
              title: "Other shifts must cancel",
              shortTitle: "Nonzero shifts",
              summary: "Distinct rows must have zero inner product.",
              video: null,
              clip: null,
              foundation: true,
              equation: "C(k) = 0,   1 ≤ k < n",
              paragraphs: [
                "For a nonzero shift, entries that agree contribute +1 and entries that disagree contribute −1. Orthogonality requires these contributions to cancel.",
                "Together with C(0) = n, these equalities describe exactly the row conditions for a circulant Hadamard matrix.",
              ],
              chapters: [],
            },
          ],
        },
        {
          id: "example",
          title: "Check the order-four example",
          shortTitle: "A small example",
          summary:
            "Try the first row (1, 1, 1, −1) and check its cyclic shifts.",
          video: null,
          clip: null,
          foundation: true,
          exampleRow: [1, 1, 1, -1],
          paragraphs: [
            "The matrix below is generated by cyclically shifting (1, 1, 1, −1). Each row has squared length 4, and each pair of different rows has inner product 0.",
            "This is one explicit example, checked by direct arithmetic. It does not establish a result about larger orders.",
          ],
          chapters: [],
        },
      ],
    },
    {
      id: "argument",
      title: "Build and check the argument",
      shortTitle: "The argument",
      summary:
        "Connect the hypotheses, the main step, and the conclusion. This chapter awaits the team's proof material.",
      video: null,
      clip: null,
      draft: true,
      paragraphs: [
        "This chapter is a place for the team's argument, rather than a claim that the conjecture has been proved. The completed version will explain how each step follows and what evidence supports it.",
        "Each part can be expanded in the same way as the background chapters, stopping when the prerequisites are standard undergraduate mathematics.",
      ],
      chapters: [
        {
          id: "main-step",
          title: "The main proof step",
          shortTitle: "The main step",
          summary:
            "Draft slot for the central lemma and its role in the argument.",
          video: null,
          clip: null,
          draft: true,
          paragraphs: [
            "The team will state the central claim here, give its assumptions, and explain why it advances the argument. A short clip will accompany the written explanation.",
            "No central lemma or proof has been supplied yet. Any further subchapters will explain the actual argument and stop at undergraduate prerequisites.",
          ],
          chapters: [],
        },
        {
          id: "conclusion",
          title: "What does the argument establish?",
          shortTitle: "The conclusion",
          summary:
            "Draft slot for the exact conclusion, checks, and remaining limitations.",
          video: null,
          clip: null,
          draft: true,
          paragraphs: [
            "The finished chapter will connect the main step back to the original question and state precisely what has been established.",
            "Proofs, finite computations, cited results, and conjectures will be identified separately. Limitations and unresolved steps will remain explicit.",
          ],
          chapters: [],
        },
      ],
    },
  ],
};
