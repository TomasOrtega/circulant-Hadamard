export default {
  id: "one-row",
  title: "One row determines the matrix",
  shortTitle: "Cyclic shifts",
  summary: "Use a cyclic shift to build every row from a single sign sequence.",
  video: null,
  foundation: true,
  script: [
    "Write the first row as (a₀, …, aₙ₋₁), with each entry equal to +1 or −1. Move the final entry to the front to obtain the next row, and repeat. After n shifts, the original row returns.",
    "The same sign sequence contains all the information in the matrix.",
  ],
  children: [],
};
