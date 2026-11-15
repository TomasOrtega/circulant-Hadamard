import { afterAll, describe, expect, test } from "bun:test";
import { existsSync, mkdtempSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { pathToFileURL } from "node:url";
import { buildNodes } from "./build-nodes.jsx";
import { loadNodes } from "./load-nodes.js";
import { collectNodes, pagePath } from "./node-tree.js";

const directory = mkdtempSync(join(tmpdir(), "circulant-reading-routes-"));
const entries = buildNodes({ outDir: directory });
afterAll(() => rmSync(directory, { recursive: true, force: true }));
const page = (path) => readFileSync(join(directory, path), "utf8");

describe("single proof journey", () => {
  test("the build contains only the shared proof hierarchy", () => {
    expect(entries.map(pagePath)).toEqual(collectNodes(loadNodes()).map(pagePath));
    expect(entries.some(({ node }) => ["proof-by-example", "general-proof"].includes(node.id))).toBe(false);
  });

  test("the homepage leads directly into its proof map without parallel reading routes", () => {
    const html = page("index.html");
    expect(html).not.toContain('aria-label="Reading routes"');
    expect(html).not.toContain('href="nodes/proof-by-example/index.html"');
    expect(html).not.toContain('href="nodes/general-proof/index.html"');
    for (const entry of collectNodes(loadNodes()).filter(({ path }) => path.length)) {
      expect(page(pagePath(entry))).not.toContain('aria-label="Reading routes"');
    }
  });

  test("both retired reading routes redirect to the same proof map", () => {
    for (const route of ["proof-by-example", "general-proof"]) {
      const html = page(`nodes/${route}/index.html`);
      expect(html).toContain('http-equiv="refresh" content="0; url=../../index.html"');
      expect(html).toContain('href="../../index.html"');
    }
  });

  test("proof-map links and legacy redirects resolve without client routing", () => {
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
