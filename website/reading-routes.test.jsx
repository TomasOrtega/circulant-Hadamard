import { afterAll, describe, expect, test } from "bun:test";
import { existsSync, mkdtempSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { pathToFileURL } from "node:url";
import { buildNodes } from "./build-nodes.jsx";
import { loadNodes } from "./load-nodes.js";
import { collectNodes, pagePath } from "./node-tree.js";

const directory = mkdtempSync(join(tmpdir(), "circulant-reading-routes-"));
buildNodes({ outDir: directory });
afterAll(() => rmSync(directory, { recursive: true, force: true }));
const page = (path) => readFileSync(join(directory, path), "utf8");

describe("homepage reading routes", () => {
  test("the homepage offers visible example and general proof start buttons", () => {
    const html = page("index.html");
    const routes = html.match(/<nav aria-label="Reading routes"[\s\S]*?<\/nav>/)?.[0];
    expect(routes).toBeDefined();
    expect(routes).toContain('href="nodes/proof-by-example/index.html"');
    expect(routes).toContain("Start here · Proof by Example: n = 36");
    expect(routes).toContain('href="nodes/general-proof/index.html"');
    expect(routes).toContain("Then · The General Odd-u Proof");
    for (const entry of collectNodes(loadNodes()).filter(({ path }) => path.length)) {
      expect(page(pagePath(entry))).not.toContain('aria-label="Reading routes"');
    }
  });

  test("reading-route buttons share a neutral default appearance", () => {
    const routes = page("index.html").match(/<nav aria-label="Reading routes"[\s\S]*?<\/nav>/)[0];
    const links = [...routes.matchAll(/<a\b[^>]*>/g)].map(([link]) => link);
    expect(links).toHaveLength(2);
    const classes = links.map((link) => link.match(/\bclass="([^"]+)"/)[1]);
    expect(classes[0]).toBe(classes[1]);
  });

  test("the order-36 button opens the readable example proof instead of redirecting", () => {
    const html = page("nodes/proof-by-example/index.html");
    expect(html).not.toContain('http-equiv="refresh"');
    expect(html).toContain("<h1>Proof by Example: n = 36</h1>");
    expect(html).toContain("The following route derives a contradiction");
    expect(html).toContain("Arithmetic setting");
    expect(html).toContain("Contradiction.");
    expect(html).toContain('jax="SVG"');
    expect(html).toContain('href="../three-evaluations/index.html"');
    expect(html).toContain('href="../../index.html#node-proof-by-example"');
  });

  test("the general button opens its own argument and links into the common proof map", () => {
    const html = page("nodes/general-proof/index.html");
    expect(html).not.toContain('http-equiv="refresh"');
    expect(html).toContain("<h1>The General Odd-u Proof</h1>");
    expect(html).toContain("For each distinct prime");
    expect(html).toContain("Where the congruences live");
    expect(html).toContain('href="../products-to-sums/index.html"');
    expect(html).toContain('href="../final-contradiction/index.html"');
    expect(html).toContain('href="../../index.html#node-group-ring-encoding"');
  });

  test("reading-guide links and return anchors resolve without client routing", () => {
    for (const path of ["index.html", "nodes/proof-by-example/index.html", "nodes/general-proof/index.html"]) {
      const filename = join(directory, path);
      for (const [, href] of page(path).matchAll(/<a\b[^>]*\bhref="([^"]+)"/g)) {
        if (/^https?:/.test(href)) continue;
        const target = new URL(href, pathToFileURL(filename));
        expect(existsSync(decodeURIComponent(target.pathname)), `${path} → ${href}`).toBe(true);
        if (target.hash && target.pathname.endsWith(".html"))
          expect(readFileSync(target, "utf8")).toContain(`id="${target.hash.slice(1)}"`);
      }
    }
  });
});
