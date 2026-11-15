import { describe, expect, test } from "bun:test";
import { readFileSync } from "node:fs";
import { loadNodes } from "./load-nodes.js";
import { renderMarkdown } from "./markdown.js";

const parents = loadNodes().children.filter(({ node }) =>
  Number(node.number) >= 2 && Number(node.number) <= 8);
const scripts = parents.flatMap(({ node: parent }) =>
  parent.children.map(({ node }) => ({
    node,
    path: `node${parent.number}/${node.id}.md`,
  })));

describe("refined-node production scripts", () => {
  test("every refinement from Nodes 2–8 is represented in the script index", () => {
    expect(parents).toHaveLength(7);
    expect(scripts).toHaveLength(34);
    const index = readFileSync("scripts/README.md", "utf8");
    for (const { path } of scripts) expect(index).toContain(`](${path})`);
  });

  for (const { node, path } of scripts) {
    test(`Video ${node.number} has narration, animation directions, and valid mathematics`, () => {
      const source = readFileSync(`scripts/${path}`, "utf8");
      expect(source).toContain(`Video ${node.number}`);
      const slides = source.split(/^## Slide \d+[^\n]*$/m).slice(1);
      expect(slides.length).toBeGreaterThan(0);
      for (const slide of slides) {
        expect(slide).toContain("*[Animation:");
        expect(slide.split("*[Animation:")[0].trim().length).toBeGreaterThan(40);
      }
      const html = renderMarkdown(source).html;
      expect(html).toContain('jax="SVG"');
      expect(html).not.toContain("data-mjx-error");
    });
  }
});
