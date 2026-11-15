import { describe, expect, test } from "bun:test";
import { readFileSync } from "node:fs";
import { renderToStaticMarkup } from "react-dom/server";
import { loadNodes } from "./load-nodes.js";
import { collectNodes, hrefFor } from "./node-tree.js";
import { dependencyGraph } from "./dependencies.js";
import { renderMarkdown } from "./markdown.js";
import { NodePage } from "./node.jsx";

describe("Node 5 all-ones refinement", () => {
  test("integral formation and Gaussian parity feed the coefficient congruence", () => {
    const entries = collectNodes(loadNodes());
    const parent = entries.find(({ node }) => node.id === "signs-become-all-ones");
    const ids = ["form-sign-combination", "gaussian-parity", "all-ones-congruence"];
    expect(parent.node.children.map(({ node }) => node.id)).toEqual(ids);
    expect(parent.node.children.map(({ node }) => node.number)).toEqual(["5.1", "5.2", "5.3"]);
    expect(dependencyGraph(parent.node.children).edges).toEqual([
      { source: ids[0], target: ids[2] },
      { source: ids[1], target: ids[2] },
    ]);
    const html = renderToStaticMarkup(<NodePage entry={parent} entries={entries} />);
    expect(html).not.toContain("stroke-dasharray");
    for (const id of ids) {
      const entry = entries.find(({ node }) => node.id === id);
      expect(html).toContain(`href="${hrefFor(entry, parent)}"`);
    }
    expect(entries.find(({ node }) => node.id === "gaussian-parity").node.foundation).toBe(true);
  });

  test("the nine-term overview draft renders its equations and animation cues", () => {
    const source = readFileSync("scripts/node5/signs-become-all-ones.md", "utf8");
    expect(source).toContain("*[Animation:");
    expect(renderMarkdown(source).html).toContain('jax="SVG"');
  });
});
