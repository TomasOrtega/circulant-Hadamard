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
import { loadNodes } from "./load-nodes.js";
import { mathStyles } from "./markdown.js";
import { assetRoot, collectNodes, pagePath } from "./node-tree.js";
import { NodePage } from "./node.jsx";

export function buildNodes({
  outDir = resolve("dist"),
  root = loadNodes(),
} = {}) {
  const entries = collectNodes(root);
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
