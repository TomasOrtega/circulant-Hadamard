import { describe, expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { loadNodes } from "./load-nodes.js";
import { collectNodes } from "./node-tree.js";
import { dependencyGraph } from "./dependencies.js";
import { NodePage } from "./node.jsx";
import { renderMarkdown } from "./markdown.js";

const root = loadNodes();
const entries = collectNodes(root);
const children = root.children.filter(({ node }) => !node.supplemental);
const html = renderToStaticMarkup(<NodePage entry={entries[0]} entries={entries} />);

describe("supplied eight-node proof map", () => {
  test("all logical arrows and the independent notation branch match the handoff", () => {
    const number = (id) => children.find(({ node }) => node.id === id).node.number ?? "theorem";
    const { edges, layers } = dependencyGraph(children);
    expect(edges.filter(({ kind }) => !kind).map(({ source, target }) =>
      `${number(source)}->${number(target)}`).sort()).toEqual([
      "1->2", "2->3", "3->5", "3->6", "4->6", "5->6", "5->7", "6->7", "5->8", "7->8", "8->theorem",
    ].sort());
    expect(edges.filter(({ kind }) => kind === "context")).toEqual([
      { source: "group-ring-encoding", target: "delta-theorem", kind: "context" },
    ]);
    expect(layers[0].map(({ node }) => node.number)).toEqual([1, 4]);
    expect(html).not.toContain("stroke-dasharray");
    expect(html).toContain('data-edge-kind="context"');
    expect(html).not.toContain("stroke-arithmetic");
    expect(html).toContain("fill-white stroke-transparent");
  });

  test("the example comes first, all eight titles remain, and only supplied refinements appear", () => {
    expect(children.filter(({ node }) => node.number).map(({ node }) => node.title)).toEqual([
      "Group-Ring Encoding", "Restriction on the Order", "The Three Evaluations", "The Δ-Theorem",
      "Signs Become All Ones", "Odd-Order Rigidity", "From Products to Sums", "The Final Contradiction",
    ]);
    expect(html.indexOf("Start here · Proof by Example: n = 36")).toBeLessThan(html.indexOf("Then · The General Odd-u Proof"));
    expect(html).toContain("Accepted black box · Proposition 2.2");
    expect(html).toContain("Accepted black box · Proposition 3.4");
    for (const { node } of children) {
      if (node.id !== "group-ring-encoding") expect(node.children).toEqual([]);
    }
    expect(entries.find(({ node }) => node.id === "proof-by-example").node.script.join(" ")).not.toContain("\\zeta_S");
  });

  test("map summaries use the article's typeset math inside each node link", () => {
    for (const { node } of children) {
      const link = html.match(new RegExp(`<a[^>]*data-node-id="${node.id}"[\\s\\S]*?</a>`))[0];
      expect(link).toContain(renderMarkdown(node.mapSummary).html);
      expect(link).toContain('jax="SVG"');
    }
  });

  test("statement pages expose incoming and outgoing links without a source dropdown", () => {
    const entry = entries.find(({ node }) => node.id === "odd-order-rigidity");
    const page = renderToStaticMarkup(<NodePage entry={entry} entries={entries} />);
    const relations = page.match(/<nav aria-label="Incoming and outgoing dependencies"[\s\S]*?<\/nav>/)[0];
    for (const slug of ["three-evaluations", "delta-theorem", "signs-become-all-ones", "products-to-sums"])
      expect(relations).toContain(`../${slug}/index.html`);
    expect(page).not.toContain("Copyable text and LaTeX");
    expect(page).not.toContain("<pre");
  });

  test("the highlighted reading route matches the current page", () => {
    for (const entry of entries.filter(({ node }) => node.supplemental)) {
      const page = renderToStaticMarkup(<NodePage entry={entry} entries={entries} />);
      const navigation = page.match(/<nav aria-label="Reading routes"[\s\S]*?<\/nav>/)[0];
      const links = [...navigation.matchAll(/<a\b([^>]*)>([^<]*)<\/a>/g)];
      const highlighted = links.filter(([, attributes]) =>
        attributes.match(/class="([^"]*)"/)[1].split(/\s+/).includes("bg-theme"));
      expect(highlighted).toHaveLength(1);
      expect(highlighted[0][1]).toContain('aria-current="page"');
      expect(highlighted[0][2]).toEndWith(entry.node.title);
      expect(links.filter(([, attributes]) => attributes.includes('aria-current="page"'))).toHaveLength(1);
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
      const eReal = (d - c) / 2 + (real - c + imaginary) / 2;
      const eImaginary = (imaginary - real + c) / 2;
      expect(eReal).toBe(-h3 - (h1 + h2) / 2);
      expect(eImaginary).toBe((h1 + h2) / 2);
      expect(Number.isInteger(eReal) && Number.isInteger(eImaginary)).toBe(true);
      expect(((eReal + eImaginary) % 2 + 2) % 2).toBe(1);
    }
  });
});
