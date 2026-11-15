import { afterAll, describe, expect, test } from "bun:test";
import { mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { parseNode, loadNodes } from "./load-nodes.js";
import { collectNodes } from "./node-tree.js";
import { renderMarkdown, mathStyles } from "./markdown.js";

const directories = [];
const fixture = (files) => {
  const directory = mkdtempSync(join(tmpdir(), "circulant-markdown-"));
  directories.push(directory);
  for (const [filename, content] of Object.entries(files))
    writeFileSync(join(directory, filename), content);
  return directory;
};
afterAll(() =>
  directories.forEach((directory) =>
    rmSync(directory, { recursive: true, force: true }),
  ),
);

describe("Markdown node authoring", () => {
  test("a minimal YAML header and prose need no JavaScript", () => {
    const node = parseNode(
      String.raw`---
title: Orthogonality
foundation: true
---
For a sign matrix $H$,

$$
H H^{\mathsf{T}} = n I_n.
$$
`,
      "orthogonality.md",
    );
    expect(node.id).toBe("orthogonality");
    expect(node.shortTitle).toBe("Orthogonality");
    expect(node.video).toBeNull();
    expect(node.children).toEqual([]);
    expect(node.script[0]).toContain(String.raw`\mathsf{T}`);
  });

  test("YAML IDs resolve shared nodes and preserve cut scripts and times", () => {
    const directory = fixture({
      "overview.md": String.raw`---
title: Overview
video: { youtubeId: abcdefghijk, duration: 100 }
children:
  - node: first
    segment: { start: 0, end: 40 }
    script: |
      The first cut uses $\frac{1}{2}$.
  - node: second
    dependsOn: [first]
    segment: { start: 40, end: 100 }
    script: |
      The second cut uses **the first**.
---
The full overview.
`,
      "first.md":
        "---\ntitle: First\nchildren:\n  - node: shared\n---\nFirst details.\n",
      "second.md":
        "---\ntitle: Second\nchildren:\n  - node: shared\n---\nSecond details.\n",
      "shared.md":
        "---\ntitle: Shared\nfoundation: true\n---\nUndergraduate background.\n",
    });
    const root = loadNodes({ directory });
    const [first, second] = root.children;
    expect(first.segment).toEqual({ start: 0, end: 40 });
    expect(first.script[0]).toContain(String.raw`$\frac{1}{2}$`);
    expect(second.dependsOn).toEqual(["first"]);
    expect(first.node.children[0].node).toBe(second.node.children[0].node);
    expect(collectNodes(root)).toHaveLength(5);
  });

  test("invalid headers, duplicate YAML keys, and empty bodies give useful errors", () => {
    expect(() => parseNode("No frontmatter", "bad.md")).toThrow(
      "YAML frontmatter",
    );
    expect(() => parseNode("---\ntitle: [broken\n---\nText", "bad.md")).toThrow(
      "bad.md",
    );
    expect(() =>
      parseNode("---\ntitle: First\ntitle: Second\n---\nText", "bad.md"),
    ).toThrow("bad.md");
    expect(() => parseNode("---\ntitle: Empty\n---\n", "empty.md")).toThrow(
      "below the frontmatter",
    );
    expect(() =>
      parseNode("---\nid: other\ntitle: Wrong\n---\nText", "wrong.md"),
    ).toThrow("match the filename");
  });

  test("expanded nodes supply their goal to parent cards while explicit excerpts take precedence", () => {
    const directory = fixture({
      "overview.md": "---\ntitle: Overview\nchildren:\n  - node: branch\n  - node: leaf\n  - node: custom\n    script: A parent-specific explanation.\n---\nIntroduction.\n",
      "branch.md": "---\ntitle: Branch\nsummary: Short branch summary.\nchildren:\n  - node: leaf\n---\n**Lemma.** The result this node establishes.\n",
      "custom.md": "---\ntitle: Custom\nchildren:\n  - node: leaf\n---\nA different goal statement.\n",
      "leaf.md": "---\ntitle: Leaf\nsummary: Short leaf summary.\n---\nThe detailed terminal proof.\n",
    });
    const { children } = loadNodes({ directory });
    expect(children[0].script).toEqual(["**Lemma.** The result this node establishes."]);
    expect(children[1].script).toEqual(["Short leaf summary."]);
    expect(children[2].script).toEqual(["A parent-specific explanation."]);
  });

  test("unknown child IDs are rejected", () => {
    const directory = fixture({
      "overview.md":
        "---\ntitle: Overview\nchildren:\n  - node: missing\n---\nText\n",
    });
    expect(() => loadNodes({ directory })).toThrow(
      "unknown child node missing",
    );
  });
});

describe("build-time Markdown and LaTeX rendering", () => {
  test("inline and display math become SVG with separate styles", () => {
    const result = renderMarkdown(String.raw`An inline $x^2$ expression.

$$
\frac{1}{2} + \sum_{j=0}^{n-1} a_j^2
$$`);
    expect([...result.html.matchAll(/<mjx-container/g)]).toHaveLength(2);
    expect(result.html).toContain('jax="SVG"');
    expect(result.html).toContain("<svg");
    expect(result.html).not.toContain("<style");
    expect(result.html).not.toContain("<script");
    expect(result.css).toContain("mjx-container");
    expect(result.html).not.toContain("language-math");
  });

  test("Markdown headings, emphasis, lists, links, and tables render normally", () => {
    const { html } = renderMarkdown(
      "## A heading\n\nA **strong** idea with [a source](https://example.com).\n\n- First\n- Second\n\n| A | B |\n| - | - |\n| 1 | 2 |\n",
    );
    expect(html).toContain("<h2>A heading</h2>");
    expect(html).toContain("<strong>strong</strong>");
    expect(html).toContain("<ul>");
    expect(html).toContain('href="https://example.com"');
    expect(html).toContain("<table>");
  });

  test("map-only math supplies shared styles and rejects malformed equations", () => {
    const node = { id: "example", script: ["Plain prose."], mapSummary: "$x^2$" };
    expect(mathStyles([{ node }])).toContain("mjx-container");
    expect(() => mathStyles([{ node: { ...node, mapSummary: String.raw`$\frac{1}{$` } }]))
      .toThrow("example.md (map summary)");
  });

  test("malformed LaTeX fails the build instead of publishing an error box", () => {
    expect(() =>
      renderMarkdown(String.raw`$$
\frac{1}{
$$`),
    ).toThrow("Invalid Markdown math");
  });

  test("separate renders do not create duplicate glyph identifiers", () => {
    const first = renderMarkdown("$x^2 + y^2$").html;
    const second = renderMarkdown("$x^2 + y^2$").html;
    const identifiers = [...(first + second).matchAll(/\bid="([^"]+)"/g)].map(
      (match) => match[1],
    );
    expect(new Set(identifiers).size).toBe(identifiers.length);
  });
});
