export default {
  id: "zero-shift",
  title: "The zero shift fixes the length",
  shortTitle: "Zero shift",
  summary: "Comparing a sign sequence with itself gives n.",
  video: null,
  foundation: true,
  equation: "C(0) = Σⱼ aⱼ² = n",
  script: [
    "Every squared entry equals 1, so this sum has n terms equal to 1. This accounts for the diagonal of HHᵀ.",
    "The diagonal is fixed automatically. The nonzero shifts carry the remaining restrictions.",
  ],
  children: [],
};
