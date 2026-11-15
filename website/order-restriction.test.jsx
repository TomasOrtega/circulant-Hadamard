import { describe, expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { loadNodes } from "./load-nodes.js";
import { collectNodes, hrefFor } from "./node-tree.js";
import { dependencyGraph } from "./dependencies.js";
import { NodePage } from "./node.jsx";

describe("Node 2 order-restriction refinement", () => {
  test("the two elementary steps and independent divisibility input feed the descent", () => {
    const entries = collectNodes(loadNodes());
    const parent = entries.find(({ node }) => node.id === "restriction-on-the-order");
    const ids = ["order-is-square", "order-is-even", "power-of-two-cycle", "cyclotomic-divisibility", "fold-and-divide", "odd-squares-mod-eight"];
    expect(parent.node.children.map(({ node }) => node.id)).toEqual(ids);
    expect(parent.node.children.map(({ node }) => node.number)).toEqual(["2.1", "2.2", "2.3", "2.4", "2.5", "2.6"]);
    const { edges, layers } = dependencyGraph(parent.node.children);
    const number = (id) => ids.indexOf(id) + 1;
    expect(edges.map(({ source, target }) => `${number(source)}->${number(target)}`)).toEqual([
      "1->3", "2->3", "3->5", "4->5", "5->6",
    ]);
    expect(layers[0].map(({ node }) => node.id)).toEqual([ids[0], ids[1], ids[3]]);
    expect(parent.node.children[3].node.blackBox).toBe("Lemma 2.1");
    const html = renderToStaticMarkup(<NodePage entry={parent} entries={entries} />);
    expect(html).toContain("Inside Node 2 · Restriction on the Order");
    expect(html).not.toContain("stroke-dasharray");
    for (const id of ids) {
      const entry = entries.find(({ node }) => node.id === id);
      expect(html).toContain(`href="${hrefFor(entry, parent)}"`);
      expect(entry.node.children).toEqual([]);
      expect(entry.node.video).toBeNull();
    }
  });
});
