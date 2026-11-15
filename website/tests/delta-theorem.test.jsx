import { describe, expect, test } from "bun:test";
import { readFileSync } from "node:fs";
import { renderToStaticMarkup } from "react-dom/server";
import { loadNodes } from "../load-nodes.js";
import { collectNodes, hrefFor } from "../node-tree.js";
import { dependencyGraph } from "../dependencies.js";
import { renderMarkdown } from "../markdown.js";
import { NodePage } from "../node.jsx";

describe("Node 4 circle-to-roots refinement", () => {
  test("the graph separates complex magnitude, integrality, and odd order", () => {
    const entries = collectNodes(loadNodes());
    const parent = entries.find(({ node }) => node.id === "delta-theorem");
    const ids = ["circle-evaluations", "alternating-phase-product", "local-character-comparison", "integral-delta", "kronecker-step", "delta-odd-order"];
    expect(parent.node.children.map(({ node }) => node.id)).toEqual(ids);
    expect(parent.node.children.map(({ node }) => node.number)).toEqual(["4.1", "4.2", "4.3", "4.4", "4.5", "4.6"]);
    const number = id => ids.indexOf(id) + 1;
    expect(dependencyGraph(parent.node.children).edges.map(({ source, target }) => `${number(source)}->${number(target)}`)).toEqual([
      "1->2", "1->3", "2->4", "3->4", "2->5", "4->5", "3->6", "5->6",
    ]);
    const html = renderToStaticMarkup(<NodePage entry={parent} entries={entries} />);
    for (const id of ids) {
      const entry = entries.find(({ node }) => node.id === id);
      expect(html).toContain(`href="${hrefFor(entry, parent)}"`);
    }
    expect(parent.node.children[2].node.blackBox).toBeUndefined();
    expect(parent.node.children[4].node.blackBox).toBeUndefined();
  });

  test("the overview renders its equations and the script index links the phase storyboard", () => {
    const source = readFileSync("scripts/node4/delta-theorem.md", "utf8");
    expect(source).toContain("*[Animation:");
    const html = renderMarkdown(source).html;
    expect(html).toContain('jax="SVG"');
    expect(html).not.toContain("data-mjx-error");
    const index = readFileSync("scripts/README.md", "utf8");
    expect(index).toContain("node4/storyboards/phase-circles.svg");
    expect(readFileSync("scripts/node4/storyboards/phase-circles.svg", "utf8")).toContain("<svg");
  });

  test("the concrete phase example rotates from denominator to numerator", () => {
    const values = Array.from({ length: 9 }, (_, k) => {
      const angle = Math.PI / 2 + 2 * Math.PI * k / 9;
      return [3 * Math.cos(angle), 3 * Math.sin(angle)];
    });
    for (const [real, imaginary] of values) expect(real ** 2 + imaginary ** 2).toBeCloseTo(9, 12);
    const [a, b] = values[0];
    const [c, d] = values[3];
    const ratio = [(a * c + b * d) / 9, (b * c - a * d) / 9];
    expect(ratio[0]).toBeCloseTo(-0.5, 12);
    expect(ratio[1]).toBeCloseTo(-Math.sqrt(3) / 2, 12);
    expect(Math.hypot(...ratio)).toBeCloseTo(1, 12);
  });
});
