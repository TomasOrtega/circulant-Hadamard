import { describe, expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { loadNodes } from "./load-nodes.js";
import { collectNodes } from "./node-tree.js";
import { dependencyGraph } from "./dependencies.js";
import { NodePage } from "./node.jsx";
import { renderMarkdown } from "./markdown.js";

const root = loadNodes();
const entries = collectNodes(root);
const children = root.children;
const html = renderToStaticMarkup(<NodePage entry={entries[0]} entries={entries} />);

describe("supplied eight-node proof map", () => {
  test("all logical arrows and the independent notation branch match the handoff", () => {
    const number = (id) => children.find(({ node }) => node.id === id).node.number ?? "theorem";
    const { edges, layers } = dependencyGraph(children);
    expect(edges.filter(({ kind }) => !kind).map(({ source, target }) =>
      `${number(source)}->${number(target)}`).sort()).toEqual([
      "1->2", "2->3", "3->5", "3->6", "4->6", "5->6", "5->7", "6->7", "5->8", "7->8",
    ].sort());
    expect(edges.filter(({ kind }) => kind === "context")).toEqual([
      { source: "group-ring-encoding", target: "delta-theorem", kind: "context" },
    ]);
    expect(layers[0].map(({ node }) => node.number)).toEqual([1, 4]);
    expect(html).not.toContain("stroke-dasharray");
    expect(html).toContain('data-edge-kind="context"');
    expect(html).not.toContain("stroke-arithmetic");
    expect(html.match(/<rect\b[^>]*class="([^"]+)"/)[1]).toContain("stroke-theme/40");
  });

  test("one hierarchy retains eight main statements and all local refinements", () => {
    expect(children.filter(({ node }) => node.number).map(({ node }) => node.title)).toEqual([
      "Group-Ring Encoding", "Restriction on the Order", "The Three Evaluations", "The Δ-Theorem",
      "Signs Become All Ones", "Odd-Order Rigidity", "From Products to Sums", "The Final Contradiction",
    ]);
    expect(entries.some(({ node }) => ["proof-by-example", "general-proof"].includes(node.id))).toBe(false);
    expect(html).not.toContain("Accepted black box · Proposition 2.2");
    expect(html).not.toContain("Accepted black box · Proposition 3.4");
    const counts = {
      "group-ring-encoding": 5, "restriction-on-the-order": 6, "three-evaluations": 5,
      "delta-theorem": 6, "signs-become-all-ones": 3, "odd-order-rigidity": 5,
      "products-to-sums": 4, "final-contradiction": 5,
    };
    for (const { node } of children) expect(node.children.length).toBe(counts[node.id] ?? 0);
    const theorem = entries.find(({ node }) => node.id === "theorem");
    expect(theorem.ancestors.at(-1).node.id).toBe("final-contradiction");
    expect(theorem.node.number).toBe("8.5");
  });

  test("map summaries use the article's typeset math inside each node link", () => {
    for (const { node } of children) {
      const link = html.match(new RegExp(`<a[^>]*data-node-id="${node.id}"[\\s\\S]*?</a>`))[0];
      expect(link).toContain(renderMarkdown(node.mapSummary).html);
      expect(link).toContain('jax="SVG"');
    }
  });

  test("outer connections have curved bends", () => {
    for (const [source, target] of [
      ["group-ring-encoding", "delta-theorem"],
      ["signs-become-all-ones", "final-contradiction"],
    ]) {
      const edge = html.match(new RegExp(`<path[^>]*data-source="${source}"[^>]*data-target="${target}"[^>]*>`))[0];
      const path = edge.match(/\bd="([^"]+)"/)[1];
      expect([...path.matchAll(/\bQ\b/g)]).toHaveLength(2);
    }
  });

  test("statement pages expose prerequisites without a source dropdown", () => {
    const entry = entries.find(({ node }) => node.id === "odd-order-rigidity");
    const page = renderToStaticMarkup(<NodePage entry={entry} entries={entries} />);
    const relations = page.match(/<nav aria-label="Prerequisites and notation"[\s\S]*?<\/nav>/)[0];
    for (const slug of ["three-evaluations", "delta-theorem", "signs-become-all-ones"])
      expect(relations).toContain(`../${slug}/index.html`);
    expect(relations).not.toContain("../products-to-sums/index.html");
    expect(page).not.toContain("Copyable text and LaTeX");
    expect(page).not.toContain("<pre");
  });

  test("reading-route start buttons appear only on the homepage", () => {
    for (const entry of entries) {
      const page = renderToStaticMarkup(<NodePage entry={entry} entries={entries} />);
      const homepage = entry.ancestors.length === 0;
      expect(page.includes('aria-label="Reading routes"'), entry.node.id).toBe(homepage);
      expect(page.includes("Start here · "), entry.node.id).toBe(homepage);
      expect(page.includes("Then · "), entry.node.id).toBe(homepage);
    }
  });

  test("malformed context edges cannot silently enter a proof map", () => {
    const base = { node: { id: "one" }, dependsOn: [] };
    expect(() => dependencyGraph([{ ...base, contextFrom: ["missing"] }])).toThrow("context link");
    expect(() => dependencyGraph([{ ...base, contextFrom: ["one"] }])).toThrow("context link");
  });

  test("the sign identity holds for all sixteen possible sign columns", () => {
    for (let mask = 0; mask < 16; mask++) {
      const [h0, h1, h2, h3] = [0, 1, 2, 3].map((bit) => mask & (1 << bit) ? 1 : -1);
      const c = (h0 + h1 + h2 + h3) / 2;
      const d = (h0 - h1 + h2 - h3) / 2;
      const real = (h0 - h2) / 2;
      const imaginary = (h1 - h3) / 2;
      const firstQuotient = (d - c) / 2;
      const secondReal = (real - c + imaginary) / 2;
      const secondImaginary = (imaginary - real + c) / 2;
      expect([firstQuotient, secondReal, secondImaginary].every(Number.isInteger)).toBe(true);
      expect(firstQuotient).toBe((-h1 - h3) / 2);
      expect(secondReal).toBe((-h2 - h3) / 2);
      expect(secondImaginary).toBe((h1 + h2) / 2);
      const eReal = firstQuotient + secondReal;
      const eImaginary = secondImaginary;
      expect(eReal).toBe(-h3 - (h1 + h2) / 2);
      expect(eImaginary).toBe((h1 + h2) / 2);
      expect(Number.isInteger(eReal) && Number.isInteger(eImaginary)).toBe(true);
      expect(((eReal + eImaginary) % 2 + 2) % 2).toBe(1);
    }
  });
});
