import mainStep from "./main-step.js";
import conclusion from "./conclusion.js";

export default {
  id: "argument",
  title: "Build and check the argument",
  shortTitle: "The argument",
  summary:
    "Connect the hypotheses, the main step, and the conclusion. This node awaits the team's proof material.",
  video: null,
  draft: true,
  script: [
    "This node is a place for the team's argument, rather than a claim that the conjecture has been proved. The completed version will explain how each step follows and what evidence supports it.",
    "Each part can be expanded in the same way as the background nodes, stopping when the prerequisites are standard undergraduate mathematics.",
  ],
  children: [
    {
      node: mainStep,
      dependsOn: [],
      segment: null,
      script: [
        "The team will state the central claim here, give its assumptions, and explain why it advances the argument. A short clip will accompany the written explanation.",
      ],
    },
    {
      node: conclusion,
      dependsOn: ["main-step"],
      segment: null,
      script: [
        "The finished node will connect the main step back to the original question and state precisely what has been established.",
      ],
    },
  ],
};
