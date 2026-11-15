import { describe, expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { DependencyGraph } from "../dependency-graph.jsx";
import { collectNodes, hrefFor } from "../node-tree.js";
import { mathStyles } from "../markdown.js";

const fixture = (graphLayout = "proof-map") => ({
  id: "overview", title: "Overview", shortTitle: "Overview", summary: "A map.",
  script: ["Plain prose without equations."], video: null, graphLayout,
  children: [{
    node: {
      id: "detail", title: "Delta theorem", shortTitle: "Delta theorem",
      mapTitle: String.raw`The $\Delta$-Theorem`,
      mapSummary: String.raw`$\frac{h(X)h^*(X)}{n}=1$`,
      number: 1, mapPosition: [40, 24], summary: "A statement.",
      script: ["More plain prose."], video: null, children: [],
    },
    dependsOn: [], segment: null, script: ["An excerpt without equations."],
  }],
});

describe("compiled graph mathematics", () => {
  test("titles and summaries render LaTeX while keeping node links and plain accessible names", () => {
    for (const layout of ["proof-map", null]) {
      const entries = collectNodes(fixture(layout));
      const html = renderToStaticMarkup(<DependencyGraph entry={entries[0]} entries={entries} />);
      expect(html).toContain(`href="${hrefFor(entries[1], entries[0])}"`);
      expect(html).toContain('aria-label="Explore node: Delta theorem.');
      expect([...html.matchAll(/jax="SVG"/g)]).toHaveLength(layout ? 2 : 1);
      expect(html).not.toContain(String.raw`\Delta`);
      expect(html).not.toContain(String.raw`\frac`);
      expect(html).not.toContain("<ol");
      expect(html).toContain("1. ");
    }
  });

  test("graph-only equations contribute their styles to the built stylesheet", () => {
    const css = mathStyles(collectNodes(fixture()));
    expect(css).toContain("mjx-container");
    expect(css).toContain('jax="SVG"');
  });

  test("malformed graph math fails before publishing", () => {
    for (const field of ["mapTitle", "mapSummary"]) {
      const root = fixture();
      root.children[0].node[field] = String.raw`$\frac{1}{$`;
      expect(() => mathStyles(collectNodes(root))).toThrow("Invalid Markdown math");
    }
  });
});
