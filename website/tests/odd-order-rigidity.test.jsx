import { describe, expect, test } from "bun:test";
import { readFileSync } from "node:fs";
import { renderToStaticMarkup } from "react-dom/server";
import { loadNodes } from "../load-nodes.js";
import { assetRoot, collectNodes, hrefFor } from "../node-tree.js";
import { dependencyGraph } from "../dependencies.js";
import { renderMarkdown } from "../markdown.js";
import { NodePage } from "../node.jsx";
import { PhaseExplorer } from "../phase-explorer.jsx";

describe("Node 6 odd-order rigidity refinement", () => {
  test("the normalization diagram uses compiled evaluation labels without repeating the proof", () => {
    const html = renderToStaticMarkup(<PhaseExplorer id="test-phase" stage="normalization" />);
    expect(html).not.toContain("<details");
    expect(html).toContain('aria-label="Divide by c(1) on the left and c(omega) on the right"');
    expect([...html.matchAll(/data-phase-label="raw"/g)]).toHaveLength(8);
    expect([...html.matchAll(/data-phase-label="normalized"/g)]).toHaveLength(8);
    for (const formula of [String.raw`$E(1)$`, String.raw`$E(\omega)$`, String.raw`$\frac{E(\omega)}{c(\omega)}$`])
      expect(html).toContain(renderMarkdown(formula).html.slice(3, -4));
  });

  test("Node 6 previews the conflict while Node 7 owns the normalization control", () => {
    const rotation = renderToStaticMarkup(<PhaseExplorer id="rotation" stage="rotation" />);
    const algebra = renderToStaticMarkup(<PhaseExplorer id="algebra" stage="normalization" />);
    expect(rotation).not.toContain("data-phase-normalize");
    expect(rotation).toContain("The conflict suggested by the picture");
    expect(rotation).toContain("cannot carry a nonzero residue to zero");
    expect(rotation).not.toContain("The algebraic contradiction");
    expect(algebra).toContain("data-phase-normalize");
    expect(algebra).not.toContain("The algebraic contradiction");
  });

  test("the main map and Node 6 include accessible phase controls and a static diagram", () => {
    const entries = collectNodes(loadNodes());
    for (const id of ["overview", "odd-order-rigidity", "products-to-sums", "delta-theorem"]) {
      const entry = entries.find(({ node }) => node.id === id);
      const html = renderToStaticMarkup(<NodePage entry={entry} entries={entries} />);
      if (id === "delta-theorem") {
        expect(html).not.toContain("data-phase-explorer");
        expect(html).not.toContain("phase-explorer.js");
        continue;
      }
      const count = id === "overview" ? 2 : 1;
      expect([...html.matchAll(/data-phase-explorer="true"/g)]).toHaveLength(count);
      expect([...html.matchAll(/data-phase-plane=/g)]).toHaveLength(2 * count);
      expect([...html.matchAll(/data-phase-value="E"/g)]).toHaveLength(2 * count);
      expect([...html.matchAll(/type="radio"/g)]).toHaveLength(3 * count);
      expect([...html.matchAll(/data-phase-normalize="true"/g)]).toHaveLength(id === "odd-order-rigidity" ? 0 : 1);
      expect(html).toContain('aria-live="polite"');
      expect(html).toContain('<noscript>');
      expect(html).toContain(`src="${assetRoot(entry)}phase-explorer.js" defer=""`);
      expect([...html.matchAll(/<script[^>]*phase-explorer\.js/g)]).toHaveLength(1);
      expect(html).toContain("no circulant Hadamard matrix of order 36 exists");
      expect(html).toContain('jax="SVG"');
    }
  });

  test("units justify the sign ratios before the two branches meet", () => {
    const entries = collectNodes(loadNodes());
    const parent = entries.find(({ node }) => node.id === "odd-order-rigidity");
    const ids = ["odd-comparison-products", "evaluation-units", "sign-ratio-congruences", "residue-one-rigidity", "exact-comparison-identities"];
    expect(parent.node.children.map(({ node }) => node.id)).toEqual(ids);
    expect(parent.node.children.map(({ node }) => node.number)).toEqual(["6.1", "6.2", "6.3", "6.4", "6.5"]);
    const number = id => ids.indexOf(id) + 1;
    expect(dependencyGraph(parent.node.children).edges.map(({ source, target }) => `${number(source)}->${number(target)}`)).toEqual([
      "2->3", "1->4", "3->4", "4->5",
    ]);
    const html = renderToStaticMarkup(<NodePage entry={parent} entries={entries} />);
    for (const id of ids) {
      const entry = entries.find(({ node }) => node.id === id);
      expect(html).toContain(`href="${hrefFor(entry, parent)}"`);
    }
  });

  test("the overview and storyboard use compiled mathematics", () => {
    const source = readFileSync("scripts/node6/odd-order-rigidity.md", "utf8");
    expect(source).toContain("*[Animation:");
    expect(source).toContain("storyboards/common-rotation.svg");
    expect(renderMarkdown(source).html).toContain('jax="SVG"');
    const storyboard = readFileSync("scripts/node6/storyboards/common-rotation.svg", "utf8");
    expect(storyboard).toContain('jax="SVG"');
    expect(storyboard).toContain("<title");
    expect(storyboard).toContain("<desc");
  });

  test("a common rotation preserves the triple's ratios without merging its points", () => {
    const multiply = ([a, b], [c, d]) => [a * c - b * d, a * d + b * c];
    const divide = ([a, b], [c, d]) => [(a * c + b * d) / (c * c + d * d), (b * c - a * d) / (c * c + d * d)];
    const lambda = [-0.5, Math.sqrt(3) / 2];
    const left = [[3, 0], [-3, 0], [0, 3]];
    const right = left.map(value => multiply(lambda, value));
    expect(new Set(right.map(value => value.join(","))).size).toBe(3);
    const delta = left.map((value, index) => divide(value, right[index]));
    for (const [real, imaginary] of delta) {
      expect(real).toBeCloseTo(lambda[0], 12);
      expect(imaginary).toBeCloseTo(-lambda[1], 12);
    }
    for (const value of right) expect(Math.hypot(...value)).toBeCloseTo(3, 12);
    for (const index of [1, 2]) {
      const ratio = divide(delta[index], delta[0]);
      expect(ratio[0]).toBeCloseTo(1, 12);
      expect(ratio[1]).toBeCloseTo(0, 12);
      const before = divide(left[index], left[0]);
      const after = divide(right[index], right[0]);
      expect(after[0]).toBeCloseTo(before[0], 12);
      expect(after[1]).toBeCloseTo(before[1], 12);
    }
  });
});
