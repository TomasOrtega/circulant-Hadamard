import zeroShift from "./zero-shift.js";
import otherShifts from "./other-shifts.js";

export default {
  id: "correlations",
  title: "Turn row comparisons into correlations",
  shortTitle: "Correlations",
  summary: "A single function records all the inner products we need.",
  video: null,
  equation: "C(k) = Σⱼ aⱼ aⱼ₊ₖ",
  script: [
    "Sum over j = 0, …, n − 1, reading every subscript modulo n. Then C(k) compares the sign sequence with a cyclic shift of itself.",
    "The Hadamard condition becomes C(0) = n and C(k) = 0 for every nonzero shift k modulo n. The next two sections separate those cases.",
  ],
  children: [
    {
      node: zeroShift,
      dependsOn: [],
      segment: null,
      script: [
        "Every squared entry equals 1, so this sum has n terms equal to 1. This accounts for the diagonal of HHᵀ.",
      ],
    },
    {
      node: otherShifts,
      dependsOn: [],
      segment: null,
      script: [
        "For a nonzero shift, entries that agree contribute +1 and entries that disagree contribute −1. Orthogonality requires these contributions to cancel.",
      ],
    },
  ],
};
