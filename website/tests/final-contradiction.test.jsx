import { describe, expect, test } from "bun:test";
import { readFileSync } from "node:fs";
import { renderToStaticMarkup } from "react-dom/server";
import { loadNodes } from "../load-nodes.js";
import { collectNodes, hrefFor } from "../node-tree.js";
import { dependencyGraph } from "../dependencies.js";
import { renderMarkdown } from "../markdown.js";
import { NodePage } from "../node.jsx";

describe("Node 8 final contradiction and theorem", () => {
  test("the main map ends at Node 8 and its two evaluations meet before the conclusion", () => {
    const root = loadNodes();
    const entries = collectNodes(root);
    const parent = entries.find(({ node }) => node.id === "final-contradiction");
    const ids = ["roots-cancel-ones", "odd-ones-at-one", "surviving-odd-term", "incompatible-residues", "theorem"];
    expect(root.children).toHaveLength(8);
    expect(root.children.at(-1).node.id).toBe("final-contradiction");
    expect(parent.node.children.map(({ node }) => node.id)).toEqual(ids);
    expect(parent.node.children.map(({ node }) => node.number)).toEqual(["8.1", "8.2", "8.3", "8.4", "8.5"]);
    const number = id => ids.indexOf(id) + 1;
    expect(dependencyGraph(parent.node.children).edges.map(({ source, target }) => `${number(source)}->${number(target)}`)).toEqual([
      "1->3", "2->3", "3->4", "4->5",
    ]);
    const html = renderToStaticMarkup(<NodePage entry={parent} entries={entries} />);
    for (const id of ids) {
      const entry = entries.find(({ node }) => node.id === id);
      expect(html).toContain(`href="${hrefFor(entry, parent)}"`);
    }
    const theorem = entries.find(({ node }) => node.id === "theorem");
    expect(theorem.ancestors.at(-1)).toBe(parent);
    const matrix = source => source.match(/\\begin\{pmatrix\}[\s\S]*?\\end\{pmatrix\}/)[0];
    expect(matrix(theorem.node.script.join("\n"))).toBe(matrix(root.script.join("\n")));
  });

  test("the script and odd-ones storyboard compile their mathematics", () => {
    const source = readFileSync("scripts/node8/final-contradiction.md", "utf8");
    expect(source).toContain("*[Animation:");
    expect(source).toContain("storyboards/odd-ones.svg");
    expect(renderMarkdown(source).html).toContain('jax="SVG"');
    const storyboard = readFileSync("scripts/node8/storyboards/odd-ones.svg", "utf8");
    expect(storyboard).toContain('jax="SVG"');
    expect(storyboard).toContain("<title");
    expect(storyboard).toContain("<desc");
  });

  test("the nine-arrow example and several-prime examples leave only the odd term", () => {
    for (const [u, primes] of [[3, [3]], [5, [5]], [9, [3]], [15, [3, 5]], [21, [3, 7]]]) {
      for (let mask = 1; mask < 2 ** primes.length; mask++) {
        const subset = primes.filter((_, bit) => mask & (1 << bit));
        const order = subset.reduce((product, prime) => product * prime, 1);
        expect(u * u % order).toBe(0);
        const angle = 2 * Math.PI * subset.reduce((sum, prime) => sum + 1 / prime, 0);
        const values = Array.from({ length: u * u }, (_, k) => [Math.cos(k * angle), Math.sin(k * angle)]);
        const total = values.reduce(([real, imaginary], value) => [real + value[0], imaginary + value[1]], [0, 0]);
        expect(total[0]).toBeCloseTo(0, 8);
        expect(total[1]).toBeCloseTo(0, 8);
      }
      for (const sign of [-1, 1]) {
        const cAtOne = sign * u;
        expect(cAtOne ** 2).toBe(u * u);
        const survivingTerm = u * u / cAtOne;
        expect(survivingTerm).toBe(sign * u);
        expect(((survivingTerm % 2) + 2) % 2).toBe(1);
      }
    }
  });
});
