import { posix } from "node:path";
import { dependencyGraph } from "./dependencies.js";
import { validateVideo, validateSegment } from "./node-video.js";

export function collectNodes(root) {
  const entries = [];

  const visit = (node, path, ancestors, numbers) => {
    if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(node.id)) {
      throw new Error(`Invalid node slug: ${node.id}`);
    }
    if (!node.title || !node.shortTitle || !node.summary) {
      throw new Error(`Missing node text: ${node.id}`);
    }
    if (ancestors.some((ancestor) => ancestor.node === node)) {
      throw new Error(`Circular node hierarchy: ${node.id}`);
    }
    const children = node.children ?? [];
    if (
      !Array.isArray(node.script) ||
      !node.script.length ||
      node.script.some((text) => typeof text !== "string" || !text.trim())
    )
      throw new Error(`Missing script for ${node.id}`);
    validateVideo(node.video, node.id);
    dependencyGraph(children);
    for (const child of children) {
      validateSegment(child.segment, node.video, child.node.id);
      if (
        !Array.isArray(child.script) ||
        !child.script.length ||
        child.script.some((text) => typeof text !== "string" || !text.trim())
      )
        throw new Error(`Missing cut script for ${child.node.id}`);
    }
    if (node.foundation && children.length) {
      throw new Error(`Undergraduate foundations must be leaves: ${node.id}`);
    }

    const entry = { node, path, ancestors, numbers };
    entries.push(entry);
    children.forEach((child, index) => {
      visit(
        child.node,
        [...path, child.node.id],
        [...ancestors, entry],
        [...numbers, index + 1],
      );
    });
  };

  visit(root, [], [], []);
  return entries;
}

export const pagePath = (entry) =>
  entry.path.length ? `nodes/${entry.path.join("/")}/index.html` : "index.html";

export const hrefFor = (target, current) =>
  posix.relative(posix.dirname(pagePath(current)), pagePath(target));

export const assetRoot = (entry) =>
  entry.path.length ? "../".repeat(entry.path.length + 1) : "./";

export const nodeAnchor = (node) => `node-${node.id}`;

export const findChildEntry = (node, parent, entries) =>
  entries.find(
    (entry) => entry.node === node && entry.ancestors.at(-1) === parent,
  );
