import { readFileSync, readdirSync } from "node:fs";
import { basename, resolve } from "node:path";
import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkFrontmatter from "remark-frontmatter";
import { parseDocument } from "yaml";

const parser = unified().use(remarkParse).use(remarkFrontmatter);

export function parseNode(source, filename) {
  const tree = parser.parse(source);
  const frontmatter = tree.children[0];
  if (frontmatter?.type !== "yaml") {
    throw new Error(`${filename}: start the node with YAML frontmatter`);
  }
  const document = parseDocument(frontmatter.value);
  if (document.errors.length) {
    throw new Error(
      `${filename}: ${document.errors.map((error) => error.message).join("; ")}`,
    );
  }
  const metadata = document.toJS();
  if (!metadata || typeof metadata !== "object" || Array.isArray(metadata)) {
    throw new Error(`${filename}: frontmatter must be a mapping`);
  }
  const id = basename(filename, ".md");
  if (metadata.id != null && metadata.id !== id) {
    throw new Error(`${filename}: node id must match the filename`);
  }
  const body = source.slice(frontmatter.position.end.offset).trim();
  if (!body)
    throw new Error(
      `${filename}: write the node's explanation below the frontmatter`,
    );
  if (
    metadata.script != null ||
    metadata.equation != null ||
    metadata.exampleRow != null
  ) {
    throw new Error(`${filename}: write prose and LaTeX in the Markdown body`);
  }
  return {
    ...metadata,
    id,
    shortTitle: metadata.shortTitle ?? metadata.title,
    summary: metadata.summary ?? metadata.title,
    video: metadata.video ?? null,
    script: [body],
    children: metadata.children ?? [],
  };
}

export function loadNodes({
  directory = resolve("nodes"),
  rootId = "overview",
} = {}) {
  const records = new Map();
  for (const filename of readdirSync(directory)
    .filter((name) => name.endsWith(".md"))
    .sort()) {
    const node = parseNode(
      readFileSync(resolve(directory, filename), "utf8"),
      filename,
    );
    records.set(node.id, { node, children: node.children });
  }
  for (const { node, children } of records.values()) {
    if (!Array.isArray(children))
      throw new Error(`${node.id}: children must be a list`);
    node.children = children.map((child) => {
      const target = records.get(child.node)?.node;
      if (!target)
        throw new Error(`${node.id}: unknown child node ${child.node}`);
      const script = child.script ?? target.summary;
      if (typeof script !== "string" || !script.trim()) {
        throw new Error(
          `${node.id}: the cut script for ${child.node} must be Markdown text`,
        );
      }
      return { ...child, node: target, script: [script.trim()] };
    });
  }
  const root = records.get(rootId)?.node;
  if (!root) throw new Error(`Missing root node: ${rootId}.md`);
  return root;
}
