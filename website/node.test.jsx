import { afterAll, describe, expect, test } from "bun:test";
import { existsSync, mkdtempSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { renderToStaticMarkup } from "react-dom/server";
import { buildNodes } from "./build-nodes.jsx";
import { collectNodes, hrefFor, pagePath, nodeAnchor } from "./node-tree.js";
import { NodePage } from "./node.jsx";
import { loadNodes } from "./load-nodes.js";
import { renderMarkdown } from "./markdown.js";

const rootNode = loadNodes();

const output = mkdtempSync(join(tmpdir(), "circulant-nodes-"));
const entries = buildNodes({ outDir: output });
afterAll(() => rmSync(output, { recursive: true, force: true }));

describe("recursive node navigation", () => {
  test("all proof nodes belong to the general route, with the example separate", () => {
    expect(rootNode.children.map(({ node }) => node.id)).toEqual([
      "proof-by-example", "general-proof",
    ]);
    const general = entries.find(({ node }) => node.id === "general-proof");
    const example = entries.find(({ node }) => node.id === "proof-by-example");
    expect(general.node.graphLayout).toBe("proof-map");
    expect(general.node.children).toHaveLength(9);
    expect(example.node.children).toEqual([]);
    expect(example.ancestors.map(({ node }) => node.id)).toEqual(["overview"]);
    for (const entry of entries.filter(({ node }) => !["overview", "proof-by-example", "general-proof"].includes(node.id))) {
      expect(entry.ancestors.includes(general), entry.node.id).toBe(true);
      expect(pagePath(entry), entry.node.id).toStartWith("nodes/general-proof/");
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      const breadcrumbs = html.match(/<nav aria-label="Breadcrumb"[\s\S]*?<\/nav>/)[0];
      expect(breadcrumbs).toContain(`href="${hrefFor(general, entry)}"`);
    }
  });

  test("page headings contain only the node title", () => {
    for (const entry of entries) {
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      const heading = html.match(/<hgroup\b[\s\S]*?<\/hgroup>/)[0];
      expect(heading.replace(/<[^>]+>/g, ""), entry.node.id).toBe(entry.node.title);
    }
  });

  test("every node has its own page, a deeper link, and a direct parent link", () => {
    expect(
      Math.max(...entries.map((entry) => entry.path.length)),
    ).toBe(3);
    for (const entry of entries) {
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      const heading = html.match(/<hgroup\b[\s\S]*?<\/hgroup>/)[0];
      expect(heading).toContain(`<h1>${entry.node.title}</h1>`);
      expect(heading.includes("The argument, one node at a time"), entry.node.id).toBe(false);
      expect(heading.includes("Exposition draft"), entry.node.id).toBe(false);
      expect(html).toContain(
        "A project for the Caltech × SAIR Mathathon, by Steven Creech and Tomas Ortega",
      );
      const parent = entry.ancestors.at(-1);
      if (parent) {
        const parentHtml = readFileSync(join(output, pagePath(parent)), "utf8");
        expect(parentHtml).toContain(`href="${hrefFor(entry, parent)}"`);
        expect(html).toContain(
          `href="${hrefFor(parent, entry)}#${nodeAnchor(entry.node)}"`,
        );
        expect(html).toContain("Back to higher-level view:");
      } else {
        expect(html).not.toContain("Back to higher-level view:");
      }
    }
  });

  test("all internal links resolve, including breadcrumbs and return anchors", () => {
    const pages = new Map(
      entries.map((entry) => [
        resolve(output, pagePath(entry)),
        readFileSync(join(output, pagePath(entry)), "utf8"),
      ]),
    );
    for (const [filename, html] of pages) {
      for (const [, href] of html.matchAll(/<a\b[^>]*\bhref="([^"]+)"/g)) {
        if (/^https?:/.test(href)) continue;
        const target = new URL(href, pathToFileURL(filename));
        const targetHtml = pages.get(decodeURIComponent(target.pathname));
        if (targetHtml === undefined && !target.pathname.endsWith(".html")) {
          expect(
            existsSync(decodeURIComponent(target.pathname)),
            `Missing linked asset: ${filename} → ${href}`,
          ).toBe(true);
          continue;
        }
        expect(
          targetHtml,
          `Broken node link: ${filename} → ${href}`,
        ).toBeDefined();
        if (target.hash)
          expect(targetHtml).toContain(`id="${target.hash.slice(1)}"`);
      }
    }
  });

  test("views order video, available proof graphs, and text, with clips and deeper links", () => {
    for (const entry of entries) {
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      const children = (entry.node.children ?? []).filter(({ node }) => !node.supplemental);
      expect(html).toContain("Overview video");
      const graph = html.indexOf('aria-label="Node dependency graph"');
      const script = entry.ancestors.length && children.length && !entry.node.supplemental
        ? children[0].script
        : entry.node.script;
      const explanation = html.indexOf(renderMarkdown(script.join("\n\n")).html);
      const owner = entry.node.children.length ? entry : entry.ancestors.at(-1);
      const hasGraph = owner.node.children.some(({ node }) => !node.supplemental);
      if (hasGraph) expect(graph).toBeGreaterThan(html.indexOf("Overview video"));
      else expect(graph).toBe(-1);
      expect(explanation).toBeGreaterThan(hasGraph ? graph : html.indexOf("Overview video"));
      expect([...html.matchAll(/(?:>Node excerpt<|aria-label="Node excerpt:)/g)]).toHaveLength(
        children.length,
      );
      expect([...html.matchAll(/aria-label="Dig in deeper:/g)]).toHaveLength(
        children.length,
      );
      const cuts = children.filter(({ segment }) => segment);
      const players = 1 + cuts.length;
      expect([...html.matchAll(/<iframe\b/g)]).toHaveLength(
        entry.node.video?.youtubeId ? players : 0,
      );
      expect([...html.matchAll(/<video\b/g)]).toHaveLength(
        entry.node.video?.src ? players : 0,
      );
      expect([...html.matchAll(/<script\b/g)]).toHaveLength(
        entry.node.video?.src && cuts.length ? 1 : 0,
      );
      for (const [, source] of html.matchAll(/<(?:source|track)\b[^>]*\bsrc="([^"]+)"/g)) {
        if (/^https?:/.test(source)) continue;
        const asset = new URL(source, pathToFileURL(join(output, pagePath(entry))));
        expect(existsSync(decodeURIComponent(asset.pathname)), source).toBe(true);
      }
    }
  });

  test.each(entries)("$node.id keeps its graph in a collapsed dropdown", (entry) => {
    const html = readFileSync(join(output, pagePath(entry)), "utf8");
    const graphs = html.match(/<nav aria-label="Node dependency graph"[\s\S]*?<\/nav>/g) ?? [];
    const dropdowns = html.match(/<details\b[^>]*>[\s\S]*?<\/details>/g) ?? [];
    expect(dropdowns).toHaveLength(graphs.length);
    for (const graph of graphs) {
      const dropdown = dropdowns.find((markup) => markup.includes(graph));
      expect(dropdown).toBeDefined();
      expect(dropdown.match(/^<details\b[^>]*><summary\b[^>]*>([^<]*)<\/summary>/)?.[1]).toBe("Show the proof map");
      expect(/^<details\b[^>]*\bopen(?:[\s=>])/.test(dropdown)).toBe(false);
    }
  });

  test("deep pages point to the shared stylesheet from their own location", () => {
    for (const entry of entries) {
      const filename = join(output, pagePath(entry));
      const html = readFileSync(filename, "utf8");
      const stylesheet = html.match(/<link rel="stylesheet" href="([^"]+)"/)[1];
      expect(new URL(stylesheet, pathToFileURL(filename)).pathname).toBe(
        join(output, "styles.css"),
      );
      expect(html).not.toContain("<!-- node-content -->");
      expect(html).not.toContain("{{asset-root}}");
      const mathStylesheet = html.match(
        /<link rel="stylesheet" href="([^"]*math\.css)"/,
      )[1];
      expect(new URL(mathStylesheet, pathToFileURL(filename)).pathname).toBe(
        join(output, "math.css"),
      );
      expect(readFileSync(join(output, "math.css"), "utf8")).toContain(
        "mjx-container",
      );
    }
  });
});

describe("node authoring constraints", () => {
  test("undergraduate foundations are terminal views", () => {
    const foundation = entries.find(({ node }) => node.foundation).node;
    const [entry] = collectNodes(foundation);
    expect(entry.node.children).toHaveLength(0);
    const html = renderToStaticMarkup(<NodePage entry={entry} entries={[entry]} />);
    expect(html).not.toContain("Dig in deeper");
    expect(() =>
      collectNodes({
        ...foundation,
        children: [
          {
            node: foundation,
            script: ["Cut script"],
            segment: null,
            dependsOn: [],
          },
        ],
      }),
    ).toThrow("Undergraduate foundations must be leaves");
  });

  test("duplicate slugs and circular hierarchies fail the build", () => {
    expect(() =>
      collectNodes({
        ...rootNode, graphLayout: null,
        children: [rootNode.children[0], rootNode.children[0]],
      }),
    ).toThrow("Duplicate child node IDs");
    const circular = { ...rootNode, graphLayout: null, children: [] };
    circular.children.push({
      node: circular,
      script: ["Cut script"],
      segment: null,
      dependsOn: [],
    });
    expect(() => collectNodes(circular)).toThrow("Circular node hierarchy");
  });

  test.each(["overview", "theorem"])("the order-four example in %s has orthogonal cyclic shifts", (id) => {
    const source = entries
      .find((entry) => entry.node.id === id)
      .node.script.join("\n\n");
    const matrix = source
      .match(/\\begin\{pmatrix\}([\s\S]*?)\\end\{pmatrix\}/)[1]
      .trim()
      .split(/\\\\/)
      .map((row) => row.trim().split("&").map(Number));
    expect(matrix).toHaveLength(4);
    for (let row = 0; row < 4; row++) {
      expect(matrix[row]).toHaveLength(4);
      expect(matrix[row]).toEqual(matrix[0].map((_, column) => matrix[0][(column - row + 4) % 4]));
      for (let other = 0; other < 4; other++) {
        const product = matrix[row].reduce(
          (sum, value, column) => sum + value * matrix[other][column],
          0,
        );
        expect(product).toBe(row === other ? 4 : 0);
      }
    }
  });

  test("configured videos render real players and relative file URLs work at depth", () => {
    const child = {
      ...rootNode.children[0].node,
      video: { src: "media/test.mp4", captions: "media/test.vtt" },
    };
    const configured = collectNodes({
      ...rootNode, graphLayout: null,
      video: { youtubeId: "abcdefghijk" },
      children: [
        {
          node: child,
          script: ["Parent cut narration"],
          segment: { start: 10, end: 30 },
          dependsOn: [],
        },
      ],
    });
    const rootHtml = renderToStaticMarkup(
      <NodePage entry={configured[0]} entries={configured} />,
    );
    const childHtml = renderToStaticMarkup(
      <NodePage entry={configured[1]} entries={configured} />,
    );
    expect(rootHtml).toContain(
      "https://www.youtube-nocookie.com/embed/abcdefghijk",
    );
    expect(childHtml).toContain('src="../../media/test.mp4"');
    expect(childHtml).toContain('src="../../media/test.vtt"');
    expect(childHtml).toContain("controls");
  });
});
