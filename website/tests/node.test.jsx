import { afterAll, describe, expect, test } from "bun:test";
import { existsSync, mkdtempSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { renderToStaticMarkup } from "react-dom/server";
import { buildNodes } from "../build-nodes.jsx";
import { collectNodes, hrefFor, pagePath, nodeAnchor } from "../node-tree.js";
import { NodePage } from "../node.jsx";
import { loadNodes } from "../load-nodes.js";
import { renderMarkdown } from "../markdown.js";

const rootNode = loadNodes();

const output = mkdtempSync(join(tmpdir(), "circulant-nodes-"));
const entries = buildNodes({ outDir: output });
afterAll(() => rmSync(output, { recursive: true, force: true }));

describe("recursive node navigation", () => {
  test("the main map has one hierarchy with eight proof nodes", () => {
    expect(rootNode.graphLayout).toBe("proof-map");
    expect(rootNode.children.map(({ node }) => node.id)).toEqual([
      "group-ring-encoding", "restriction-on-the-order", "three-evaluations",
      "delta-theorem", "signs-become-all-ones", "odd-order-rigidity",
      "products-to-sums", "final-contradiction",
    ]);
    expect(collectNodes(rootNode).some(({ node }) => ["proof-by-example", "general-proof"].includes(node.id))).toBe(false);
    expect(entries.map(({ node }) => node.id)).toEqual(collectNodes(rootNode).map(({ node }) => node.id));
    for (const entry of entries.filter(({ ancestors }) => ancestors.length)) {
      expect(entry.ancestors[0], entry.node.id).toBe(entries[0]);
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      const breadcrumbs = html.match(/<nav aria-label="Breadcrumb"[\s\S]*?<\/nav>/)[0];
      expect(breadcrumbs).toContain(`href="${hrefFor(entries[0], entry)}"`);
      expect(html).not.toContain('aria-label="Reading routes"');
    }
  });

  test("page headings contain only the node title", () => {
    for (const entry of entries) {
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      const heading = html.match(/<hgroup\b[\s\S]*?<\/hgroup>/)[0];
      expect(heading.replace(/<[^>]+>/g, ""), entry.node.id).toBe(renderToStaticMarkup(<>{entry.node.title}</>));
    }
  });

  test("each page has one appearance switch in its masthead", () => {
    for (const entry of entries) {
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      const masthead = html.slice(html.indexOf("<header"), html.indexOf("</header>"));
      expect(masthead, entry.node.id).toContain('id="dark-mode-toggle"');
      expect(masthead, entry.node.id).toContain('role="switch"');
      expect([...html.matchAll(/id="dark-mode-toggle"/g)], entry.node.id).toHaveLength(1);
    }
  });

  test("breadcrumbs match the surrounding navigation typography and link style", () => {
    for (const entry of entries.filter(({ ancestors }) => ancestors.length)) {
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      const breadcrumbs = html.match(/<nav aria-label="Breadcrumb"[\s\S]*?<\/nav>/)[0];
      const parentButton = html.match(/<a\b[^>]*aria-label="Back to higher-level view:[^"]*"[^>]*>/)[0];
      const parentClasses = parentButton.match(/\bclass="([^"]+)"/)[1];
      expect(breadcrumbs.match(/^<nav\b[^>]*>/)[0], entry.node.id).toContain("font-sans text-lg");
      for (const [link] of breadcrumbs.matchAll(/<a\b[^>]*>/g)) {
        expect(link.match(/\bclass="([^"]+)"/)?.[1], entry.node.id).toBe(parentClasses);
      }
    }
  });

  test("published local overview players resolve their videos, captions, and posters", () => {
    for (const entry of entries.filter(({ node }) => node.video?.src?.startsWith("media/"))) {
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      const player = html.match(/<video\b[^>]*aria-label="Overview video:[^"]*"[^>]*>[\s\S]*?<\/video>/)?.[0];
      expect(player, entry.node.id).toBeDefined();
      const source = player.match(/<source\b[^>]*src="([^"]+)"/)?.[1];
      const captions = player.match(/<track\b[^>]*kind="captions"[^>]*src="([^"]+)"/)?.[1];
      const poster = player.match(/\bposter="([^"]+)"/)?.[1];
      expect(source?.endsWith(entry.node.video.src), entry.node.id).toBe(true);
      expect(captions?.endsWith(entry.node.video.captions), entry.node.id).toBe(true);
      expect(entry.node.video.poster, entry.node.id).toBe(`media/thumbnails/${entry.node.id}.jpg`);
      expect(poster?.endsWith(entry.node.video.poster), entry.node.id).toBe(true);
      const page = pathToFileURL(resolve(output, pagePath(entry)));
      expect(existsSync(decodeURIComponent(new URL(source, page).pathname)), entry.node.id).toBe(true);
      expect(readFileSync(decodeURIComponent(new URL(captions, page).pathname), "utf8").startsWith("WEBVTT\n"), entry.node.id).toBe(true);
      const image = readFileSync(decodeURIComponent(new URL(poster, page).pathname));
      expect([...image.subarray(0, 3)], entry.node.id).toEqual([0xff, 0xd8, 0xff]);
      expect(entry.node.video.duration, entry.node.id).toBeGreaterThan(0);
    }
  });

  test("every published native excerpt has its own reachable JPEG poster", () => {
    for (const entry of entries.filter(({ node }) => node.video?.src?.startsWith("media/"))) {
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      const players = [...html.matchAll(/<video\b[^>]*aria-label="Node excerpt:[^"]*"[^>]*>[\s\S]*?<\/video>/g)];
      const cuts = entry.node.children.filter(({ segment }) => segment);
      expect(players, entry.node.id).toHaveLength(cuts.length);
      cuts.forEach(({ node, segment }, index) => {
        const poster = players[index][0].match(/\bposter="([^"]+)"/)?.[1];
        expect(segment.poster, node.id).toBe(`media/thumbnails/excerpts/${node.id}.jpg`);
        expect(poster?.endsWith(segment.poster), node.id).toBe(true);
        const page = pathToFileURL(resolve(output, pagePath(entry)));
        const image = readFileSync(decodeURIComponent(new URL(poster, page).pathname));
        expect([...image.subarray(0, 3)], node.id).toEqual([0xff, 0xd8, 0xff]);
      });
    }
  });

  test("every node has its own page, a deeper link, and a direct parent link", () => {
    expect(
      Math.max(...entries.map((entry) => entry.path.length)),
    ).toBe(2);
    for (const entry of entries) {
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      const heading = html.match(/<hgroup\b[\s\S]*?<\/hgroup>/)[0];
      expect(heading).toContain(renderToStaticMarkup(<h1>{entry.node.title}</h1>));
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
      const children = entry.node.children ?? [];
      const cuts = children.filter(({ segment }) => segment);
      expect(html).toContain("Overview video");
      const graph = html.indexOf('aria-label="Node dependency graph"');
      const script = entry.ancestors.length && children.length
        ? children[0].script
        : entry.node.script;
      const explanation = html.indexOf(renderMarkdown(script.join("\n\n")).html);
      const owner = entry.node.children.length ? entry : entry.ancestors.at(-1);
      const hasGraph = owner.node.children.length > 0;
      if (hasGraph) expect(graph).toBeGreaterThan(html.indexOf("Overview video"));
      else expect(graph).toBe(-1);
      expect(explanation).toBeGreaterThan(hasGraph ? graph : html.indexOf("Overview video"));
      expect([...html.matchAll(/(?:>Node excerpt<|aria-label="Node excerpt:)/g)]).toHaveLength(
        cuts.length,
      );
      expect([...html.matchAll(/aria-label="Dig in deeper:/g)]).toHaveLength(
        children.length,
      );
      const players = 1 + cuts.length;
      expect([...html.matchAll(/<iframe\b/g)]).toHaveLength(
        entry.node.video?.youtubeId ? players : 0,
      );
      expect([...html.matchAll(/<video\b/g)]).toHaveLength(
        entry.node.video?.src ? players : 0,
      );
      expect([...html.matchAll(/<script\b/g)]).toHaveLength(
        2 + (entry.node.video?.src && cuts.length ? 1 : 0)
          + (children.some(({ node }) => ["odd-order-rigidity", "exact-comparison-identities", "products-to-sums", "vanishing-alternating-sum"].includes(node.id)) ? 1 : 0),
      );
      for (const [, source] of html.matchAll(/<(?:source|track)\b[^>]*\bsrc="([^"]+)"/g)) {
        if (/^https?:/.test(source)) continue;
        const asset = new URL(source, pathToFileURL(join(output, pagePath(entry))));
        expect(existsSync(decodeURIComponent(asset.pathname)), source).toBe(true);
      }
    }
  });

  test("each deeper button shares a header with its heading before the explanation", () => {
    for (const entry of entries) {
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      for (const child of entry.node.children) {
        const section = html.match(new RegExp(`<section id="${nodeAnchor(child.node)}"[\\s\\S]*?</section>`))[0];
        const button = section.indexOf('aria-label="Dig in deeper:');
        const explanation = section.indexOf(renderMarkdown(child.script.join("\n\n")).html);
        const header = section.match(/<header\b[\s\S]*?<\/header>/)?.[0] ?? "";
        expect(header, child.node.id).toContain("<h2");
        expect(header, child.node.id).toContain('aria-label="Dig in deeper:');
        expect(header, child.node.id).not.toContain("video script pending");
        expect(button, child.node.id).toBeGreaterThan(section.indexOf("</h2>"));
        expect(explanation, child.node.id).toBeGreaterThan(button);
        expect(section.includes("<aside"), child.node.id).toBe(false);
      }
    }
  });

  test("pages omit the redundant dependency panel", () => {
    for (const entry of entries) {
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      expect(html.includes('aria-label="Prerequisites and notation"'), entry.node.id).toBe(false);
      expect(html.includes("<strong>Uses:"), entry.node.id).toBe(false);
      expect(html.includes("Used by:"), entry.node.id).toBe(false);
      expect(/<section\b[^>]*>\s*<\/section>/.test(html), entry.node.id).toBe(false);
    }
  });

  test.each(entries)("$node.id keeps its graph in a collapsed dropdown", (entry) => {
    const html = readFileSync(join(output, pagePath(entry)), "utf8");
    const graphs = html.match(/<nav aria-label="Node dependency graph"[\s\S]*?<\/nav>/g) ?? [];
    const dropdowns = (html.match(/<details\b[^>]*>[\s\S]*?<\/details>/g) ?? [])
      .filter(markup => markup.includes('aria-label="Node dependency graph"'));
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
      video: { src: "media/test.mp4", captions: "media/test.vtt", poster: "media/thumbnails/test.jpg" },
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
    expect(childHtml).toContain('poster="../../media/thumbnails/test.jpg"');
    expect(childHtml).toContain("controls");
  });
});
