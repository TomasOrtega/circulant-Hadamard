import {
  cpSync,
  existsSync,
  mkdirSync,
  readFileSync,
  rmSync,
  writeFileSync,
} from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { renderToStaticMarkup } from "react-dom/server";
import { loadNodes, parseNode } from "./load-nodes.js";
import { mathStyles } from "./markdown.js";
import { assetRoot, collectNodes, hrefFor, pagePath } from "./node-tree.js";
import { NodePage } from "./node.jsx";

export function buildNodes({
  outDir = resolve("dist"),
  root = loadNodes(),
} = {}) {
  const entries = collectNodes(root);
  if (root.graphLayout === "proof-map") {
    for (const id of ["proof-by-example", "general-proof"]) {
      if (entries.some((entry) => pagePath(entry) === `nodes/${id}/index.html`)) continue;
      const node = parseNode(readFileSync(resolve("reading-routes", `${id}.md`), "utf8"), `${id}.md`);
      entries.push({ node, path: [id], ancestors: [entries[0]], numbers: [] });
    }
  }
  const stylesheet = mathStyles(entries);
  const template = readFileSync("index.html", "utf8");
  rmSync(resolve(outDir, "lessons"), { recursive: true, force: true });
  rmSync(resolve(outDir, "nodes"), { recursive: true, force: true });
  mkdirSync(outDir, { recursive: true });
  for (const entry of entries) {
    const title = entry.path.length
      ? `${entry.node.title} · Circulant Hadamard`
      : entry.node.title;
    const metadata = renderToStaticMarkup(
      <>
        <title>{title}</title>
        <meta name="description" content={entry.node.summary} />
      </>,
    );
    const content = renderToStaticMarkup(
      <NodePage entry={entry} entries={entries} />,
    );
    const html = template
      .replace("<!-- node-meta -->", () => metadata)
      .replaceAll("{{asset-root}}", assetRoot(entry))
      .replace("<!-- node-content -->", () => content);
    const output = resolve(outDir, pagePath(entry));
    mkdirSync(dirname(output), { recursive: true });
    writeFileSync(output, html);
  }
  const occupied = new Set(entries.map(pagePath));
  const redirects = new Map();
  const addRedirect = (path, target) => {
    const previous = { path };
    if (!occupied.has(pagePath(previous)))
      redirects.set(pagePath(previous), { previous, target });
  };
  for (const route of ["general-proof", "proof-by-example"])
    addRedirect([route], entries[0]);
  for (const entry of entries) {
    if (entry.path.length && entry.node.id !== "theorem" &&
        !["general-proof", "proof-by-example"].includes(entry.path[0]))
      addRedirect(["general-proof", ...entry.path], entry);
  }
  const theorem = entries.find(({ node }) => node.id === "theorem");
  if (theorem) {
    addRedirect(["theorem"], theorem);
    addRedirect(["general-proof", "theorem"], theorem);
  }
  for (const { previous, target } of redirects.values()) {
    const destination = hrefFor(target, previous);
    const metadata = renderToStaticMarkup(
      <>
        <title>{`${target.node.title} · Circulant Hadamard`}</title>
        <meta httpEquiv="refresh" content={`0; url=${destination}`} />
      </>,
    );
    const content = renderToStaticMarkup(
      <main className="mx-auto max-w-3xl px-6 py-16">
        <h1>This proof page has moved</h1>
        <p><a href={destination}>Continue to {target.node.title}.</a></p>
      </main>,
    );
    const html = template
      .replace("<!-- node-meta -->", () => metadata)
      .replaceAll("{{asset-root}}", assetRoot(previous))
      .replace("<!-- node-content -->", () => content);
    const output = resolve(outDir, pagePath(previous));
    mkdirSync(dirname(output), { recursive: true });
    writeFileSync(output, html);
  }
  writeFileSync(resolve(outDir, "math.css"), stylesheet);
  if (existsSync("media"))
    cpSync("media", resolve(outDir, "media"), { recursive: true });
  return entries;
}

if (
  process.argv[1] &&
  resolve(process.argv[1]) === fileURLToPath(import.meta.url)
) {
  const entries = buildNodes();
  console.log(`Built ${entries.length} node pages.`);
}
