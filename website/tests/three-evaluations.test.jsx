import { describe, expect, test } from "bun:test";
import { readFileSync } from "node:fs";
import { renderToStaticMarkup } from "react-dom/server";
import { loadNodes } from "../load-nodes.js";
import { collectNodes, hrefFor } from "../node-tree.js";
import { dependencyGraph } from "../dependencies.js";
import { renderMarkdown } from "../markdown.js";
import { NodePage } from "../node.jsx";

describe("Node 3 three-evaluation refinement", () => {
  test("five nodes separate evaluation from coefficient parity before normalization", () => {
    const entries = collectNodes(loadNodes());
    const parent = entries.find(({ node }) => node.id === "three-evaluations");
    const ids = ["crt-coordinates", "four-sign-polynomials", "evaluate-four-cycle", "halve-sign-sums", "normalized-evaluation-norms"];
    expect(parent.node.children.map(({ node }) => node.id)).toEqual(ids);
    expect(parent.node.children.map(({ node }) => node.number)).toEqual(["3.1", "3.2", "3.3", "3.4", "3.5"]);
    const { edges } = dependencyGraph(parent.node.children);
    const number = id => ids.indexOf(id) + 1;
    expect(edges.map(({ source, target }) => `${number(source)}->${number(target)}`)).toEqual([
      "1->2", "2->3", "2->4", "3->5", "4->5",
    ]);
    const html = renderToStaticMarkup(<NodePage entry={parent} entries={entries} />);
    expect(html).not.toContain("stroke-dasharray");
    for (const id of ids) {
      const entry = entries.find(({ node }) => node.id === id);
      expect(html).toContain(`href="${hrefFor(entry, parent)}"`);
    }
  });

  test("the overview draft renders its equations and animation cues", () => {
    const source = readFileSync("scripts/node3/three-evaluations.md", "utf8");
    expect(source).toContain("*[Animation:");
    expect(renderMarkdown(source).html).toContain('jax="SVG"');
  });

  test("CRT reindexes the sign positions and every sign column can be halved", () => {
    for (const u of [1, 3, 5]) {
      const m = u * u;
      const coordinates = Array.from({ length: 4 * m }, (_, j) => `${j % 4},${j % m}`);
      expect(new Set(coordinates).size).toBe(4 * m);
      for (let a = 0; a < 4; a++)
        expect(coordinates.filter(value => value.startsWith(`${a},`))).toHaveLength(m);
    }
    for (let mask = 0; mask < 16; mask++) {
      const [a, b, c, d] = [0, 1, 2, 3].map(bit => mask & (1 << bit) ? 1 : -1);
      const halfCoefficients = [(a + b + c + d) / 2, (a - b + c - d) / 2, (a - c) / 2, (b - d) / 2];
      expect(halfCoefficients.every(Number.isInteger)).toBe(true);
      const h = [a, b, c, d];
      const correlations = h.map((_, shift) => h.reduce((sum, value, j) => sum + value * h[(j - shift + 4) % 4], 0));
      const [cValue, dValue, gReal, gImaginary] = halfCoefficients;
      expect(cValue ** 2).toBe(correlations.reduce((sum, value) => sum + value, 0) / 4);
      expect(dValue ** 2).toBe(correlations.reduce((sum, value, j) => sum + (-1) ** j * value, 0) / 4);
      expect([gReal ** 2 + gImaginary ** 2, 0]).toEqual([
        (correlations[0] - correlations[2]) / 4,
        (correlations[1] - correlations[3]) / 4,
      ]);
    }
  });
});
