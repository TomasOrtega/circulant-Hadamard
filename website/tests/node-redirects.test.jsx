import { afterEach, describe, expect, test } from "bun:test";
import { existsSync, mkdtempSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { buildNodes } from "../build-nodes.jsx";
import { loadNodes } from "../load-nodes.js";

const directories = [];
afterEach(() => {
  for (const directory of directories.splice(0))
    rmSync(directory, { recursive: true, force: true });
});

const node = (id, children = []) => ({
  id, title: id, shortTitle: id, summary: `About ${id}`,
  script: [`The explanation for ${id}.`], video: null,
  children: children.map(child => ({
    node: child, script: [`Explore ${child.id}.`], dependsOn: [], segment: null,
  })),
});

function build(root) {
  const directory = mkdtempSync(join(tmpdir(), "circulant-legacy-route-"));
  directories.push(directory);
  buildNodes({ root, outDir: directory });
  return directory;
}

function expectRedirect(directory, previousPath, destination, assetPrefix) {
  const html = readFileSync(join(directory, previousPath), "utf8");
  expect(html.includes(`http-equiv="refresh" content="0; url=${destination}"`), previousPath).toBe(true);
  expect(html).toContain(`href="${destination}"`);
  expect(html).toContain(`href="${assetPrefix}styles.css"`);
  expect(existsSync(join(directory, previousPath, "..", destination))).toBe(true);
  expect(html).not.toContain("<script");
}

describe("published proof route compatibility", () => {
  test("legacy reading-route URLs redirect to the root proof map", () => {
    const directory = build(loadNodes());
    for (const route of ["general-proof", "proof-by-example"])
      expectRedirect(directory, `nodes/${route}/index.html`, "../../index.html", "../../");
  });

  test("general-proof URLs retain main nodes and their deeper pages", () => {
    const directory = build(node("overview", [
      node("group-ring-encoding", [node("cyclic-group-ring")]),
      node("three-evaluations", [node("crt-coordinates")]),
    ]));
    expectRedirect(directory, "nodes/general-proof/group-ring-encoding/index.html",
      "../../group-ring-encoding/index.html", "../../../");
    expectRedirect(directory, "nodes/general-proof/group-ring-encoding/cyclic-group-ring/index.html",
      "../../../group-ring-encoding/cyclic-group-ring/index.html", "../../../../");
    expectRedirect(directory, "nodes/general-proof/three-evaluations/crt-coordinates/index.html",
      "../../../three-evaluations/crt-coordinates/index.html", "../../../../");
  });

  test("both earlier theorem URLs lead directly to the theorem inside Node 8", () => {
    const directory = build(node("overview", [node("final-contradiction", [node("theorem")])]));
    expectRedirect(directory, "nodes/theorem/index.html",
      "../final-contradiction/theorem/index.html", "../../");
    expectRedirect(directory, "nodes/general-proof/theorem/index.html",
      "../../final-contradiction/theorem/index.html", "../../../");
  });

  test("existing pages at legacy paths remain regular pages", () => {
    const directory = build(node("overview", [
      node("general-proof", [node("theorem")]), node("proof-by-example"),
    ]));
    for (const route of ["general-proof", "general-proof/theorem", "proof-by-example"]) {
      const html = readFileSync(join(directory, `nodes/${route}/index.html`), "utf8");
      expect(html).not.toContain('http-equiv="refresh"');
      expect(html).toContain(`<h1>${route.split("/").at(-1)}</h1>`);
    }
    expect(existsSync(join(directory, "nodes/general-proof/general-proof/index.html"))).toBe(false);
  });

  test("a tree without a theorem has no invented theorem destination", () => {
    const directory = build(node("overview", [node("other")]));
    expect(existsSync(join(directory, "nodes/theorem/index.html"))).toBe(false);
    expect(existsSync(join(directory, "nodes/general-proof/theorem/index.html"))).toBe(false);
  });

  test("a theorem still at its original top-level path is not overwritten", () => {
    const directory = build(node("overview", [node("theorem")]));
    const html = readFileSync(join(directory, "nodes/theorem/index.html"), "utf8");
    expect(html).toContain("The explanation for theorem.");
    expect(html).not.toContain('http-equiv="refresh"');
    expectRedirect(directory, "nodes/general-proof/theorem/index.html",
      "../../theorem/index.html", "../../../");
  });
});
