import { describe, expect, test } from "bun:test";
import { readFileSync } from "node:fs";
import { renderToStaticMarkup } from "react-dom/server";
import { loadNodes } from "../load-nodes.js";
import { collectNodes, hrefFor } from "../node-tree.js";
import { dependencyGraph } from "../dependencies.js";
import { renderMarkdown } from "../markdown.js";
import { NodePage } from "../node.jsx";

describe("Node 7 products-to-sums refinement", () => {
  test("exact products and integral expansions meet before cancellation and addition", () => {
    const entries = collectNodes(loadNodes());
    const parent = entries.find(({ node }) => node.id === "products-to-sums");
    const ids = ["split-exact-products", "expand-integral-products", "cancel-before-reduction", "vanishing-alternating-sum"];
    expect(parent.node.children.map(({ node }) => node.id)).toEqual(ids);
    expect(parent.node.children.map(({ node }) => node.number)).toEqual(["7.1", "7.2", "7.3", "7.4"]);
    const number = id => ids.indexOf(id) + 1;
    expect(dependencyGraph(parent.node.children).edges.map(({ source, target }) => `${number(source)}->${number(target)}`)).toEqual([
      "1->3", "2->3", "3->4",
    ]);
    const html = renderToStaticMarkup(<NodePage entry={parent} entries={entries} />);
    for (const id of ids) {
      const entry = entries.find(({ node }) => node.id === id);
      expect(html).toContain(`href="${hrefFor(entry, parent)}"`);
    }
  });

  test("the overview and storyboard use compiled mathematics", () => {
    const source = readFileSync("scripts/node7/products-to-sums.md", "utf8");
    expect(source).toContain("*[Animation:");
    expect(source).toContain("storyboards/rotation-cancellation.svg");
    expect(renderMarkdown(source).html).toContain('jax="SVG"');
    const storyboard = readFileSync("scripts/node7/storyboards/rotation-cancellation.svg", "utf8");
    expect(storyboard).toContain('jax="SVG"');
    expect(storyboard).toContain("<title");
    expect(storyboard).toContain("<desc");
  });

  test("the schematic combination rotates and cancels even outside the norm circle", () => {
    const multiply = ([a, b], [c, d]) => [a * c - b * d, a * d + b * c];
    const divide = ([a, b], [c, d]) => [(a * c + b * d) / (c * c + d * d), (b * c - a * d) / (c * c + d * d)];
    const subtract = (a, b) => a.map((value, index) => value - b[index]);
    const combine = ([c, d, g]) => {
      const first = divide(subtract(d, c), [2, 0]);
      const second = divide(subtract(g, c), [1, 1]);
      return first.map((value, index) => value + second[index]);
    };
    const lambda = [-0.5, Math.sqrt(3) / 2];
    const before = [[3, 0], [-3, 0], [0, 3]];
    const after = before.map(value => multiply(lambda, value));
    const left = combine(before);
    const right = combine(after);
    expect(left).toEqual([-3, 3]);
    expect(Math.hypot(...left)).toBeGreaterThan(3);
    const rotated = multiply(lambda, left);
    for (let index = 0; index < 2; index++) expect(right[index]).toBeCloseTo(rotated[index], 12);
    const normalizedLeft = divide(left, before[0]);
    const normalizedRight = divide(right, after[0]);
    expect(normalizedLeft).toEqual([-1, 1]);
    for (let index = 0; index < 2; index++) expect(normalizedRight[index]).toBeCloseTo(normalizedLeft[index], 12);
  });
});
