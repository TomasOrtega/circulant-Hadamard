import { describe, expect, test } from "bun:test";
import { readFileSync } from "node:fs";
import { renderToStaticMarkup } from "react-dom/server";
import { loadNodes } from "./load-nodes.js";
import { collectNodes, hrefFor } from "./node-tree.js";
import { dependencyGraph } from "./dependencies.js";
import { renderMarkdown } from "./markdown.js";
import { NodePage } from "./node.jsx";

const entries = collectNodes(loadNodes());
const parent = entries.find(({ node }) => node.id === "group-ring-encoding");
const ids = ["cyclic-group-ring", "cyclic-shifts", "star-operation", "correlation-identity", "hadamard-dictionary"];

const product = (a, b) => {
  const result = Array(a.length).fill(0);
  a.forEach((x, j) => b.forEach((y, k) => { result[(j + k) % a.length] += x * y; }));
  return result;
};
const star = (a) => a.map((_, j) => a[(a.length - j) % a.length]);
const shift = (a, r) => a.map((_, j) => a[(j - r + a.length) % a.length]);
const dot = (a, b) => a.reduce((sum, x, j) => sum + x * b[j], 0);

describe("Node 1 supplied refinement", () => {
  test("five numbered nodes and all six connections match the PDF", () => {
    expect(parent.node.children.map(({ node }) => node.id)).toEqual(ids);
    expect(parent.node.children.map(({ node }) => node.number)).toEqual(["1.1", "1.2", "1.3", "1.4", "1.5"]);
    const { edges } = dependencyGraph(parent.node.children);
    const numbered = (id) => ids.indexOf(id) + 1;
    expect(edges.filter(({ kind }) => !kind).map(({ source, target }) => `${numbered(source)}->${numbered(target)}`)).toEqual([
      "1->2", "1->3", "3->4", "2->5", "4->5",
    ]);
    expect(edges.filter(({ kind }) => kind === "context")).toEqual([
      { source: ids[0], target: ids[3], kind: "context" },
    ]);
    const page = renderToStaticMarkup(<NodePage entry={parent} entries={entries} />);
    expect(page).toContain("Inside Node 1 · Group-Ring Encoding");
    expect(page).not.toContain("stroke-dasharray");
    for (const id of ids) {
      const entry = entries.find(({ node }) => node.id === id);
      expect(page).toContain(`href="${hrefFor(entry, parent)}"`);
      const childPage = renderToStaticMarkup(<NodePage entry={entry} entries={entries} />);
      expect(childPage).toContain(`href="${hrefFor(parent, entry)}#node-${id}"`);
      expect(childPage.includes("Show the proof map")).toBe(true);
      expect(entry.node.children).toEqual([]);
    }
    const correlation = entries.find(({ node }) => node.id === ids[3]);
    const correlationPage = renderToStaticMarkup(<NodePage entry={correlation} entries={entries} />);
    expect(correlationPage).toContain("Shared notation only from Group Ring");
  });

  test("the parent card states the dictionary and Node 1 puts exposition in its child sections", () => {
    const page = renderToStaticMarkup(<NodePage entry={parent} entries={entries} />);
    const firstSection = page.indexOf('<section id="node-cyclic-group-ring"');
    expect(firstSection).toBeGreaterThan(page.indexOf('aria-label="Node dependency graph"'));
    expect(page.slice(0, firstSection)).not.toContain(renderMarkdown(parent.node.script.join("\n\n")).html);
    for (const child of parent.node.children) {
      const section = page.split(`<section id="node-${child.node.id}"`)[1].split("</section>")[0];
      expect(section).toContain(renderMarkdown(child.script.join("\n\n")).html);
      expect(section).toContain(`aria-label="Dig in deeper: ${child.node.title}"`);
      expect(section).toContain('jax="SVG"');
    }
    const general = entries.find(({ node }) => node.id === "general-proof");
    const generalPage = renderToStaticMarkup(<NodePage entry={general} entries={entries} />);
    const card = generalPage.split('<section id="node-group-ring-encoding"')[1].split("</section>")[0];
    expect(card).toContain(renderMarkdown(parent.node.script.join("\n\n")).html);
    expect(card).toContain("Circulant Hadamard Dictionary");
  });

  test("all six production scripts retain animation cues and render their restored LaTeX", () => {
    for (const id of [parent.node.id, ...ids]) {
      const source = readFileSync(`scripts/node1/${id}.md`, "utf8");
      expect(source).toContain("*[Animation:");
      expect(renderMarkdown(source).html).toContain('jax="SVG"');
    }
  });

  test("the fixed example is unchanged by star and the all-ones counterexample fails", () => {
    const h = [-1, 1, 1, 1];
    expect(star(h)).toEqual(h);
    expect(product(h, star(h))).toEqual([4, 0, 0, 0]);
    expect(star([2, -3, 0, 5])).toEqual([2, 5, 0, -3]);
    expect(product([1, 1, 1, 1], [1, 1, 1, 1])).toEqual([4, 4, 4, 4]);
  });

  test("the coefficient identity and both dictionary implications hold for all sign rows through length six", () => {
    for (let n = 1; n <= 6; n++) {
      for (let mask = 0; mask < 2 ** n; mask++) {
        const h = Array.from({ length: n }, (_, j) => mask & (1 << j) ? 1 : -1);
        const coefficients = product(h, star(h));
        expect(coefficients).toEqual(h.map((_, a) => dot(h, shift(h, a))));
        const rows = h.map((_, r) => shift(h, r));
        const gram = rows.map((row) => rows.map((other) => dot(row, other)));
        for (let r = 0; r < n; r++) for (let s = 0; s < n; s++)
          expect(gram[r][s]).toBe(coefficients[(s - r + n) % n]);
        const hadamard = gram.every((row, r) => row.every((value, s) => value === (r === s ? n : 0)));
        const normIdentity = coefficients.every((value, a) => value === (a === 0 ? n : 0));
        expect(hadamard).toBe(normIdentity);
      }
    }
    const integers = [2, -3, 0, 5];
    expect(product(integers, star(integers))).toEqual(integers.map((_, a) => dot(integers, shift(integers, a))));
  });
});
