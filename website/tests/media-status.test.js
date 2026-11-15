import { describe, expect, test } from "bun:test";
import { createHash } from "node:crypto";
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { loadNodes } from "../load-nodes.js";
import { collectNodes } from "../node-tree.js";
import { cutVideo } from "../node-video.js";

const entries = collectNodes(loadNodes());

describe("website media completion", () => {
  test("each node has its accepted video and script or a to-do", () => {
    for (const { node } of entries) {
      const todo = `scripts/to-do/${node.id}.md`;
      if (existsSync(todo)) {
        expect(node.video, node.id).toBeNull();
        expect(readFileSync(todo, "utf8").trim().length, node.id).toBeGreaterThan(0);
        continue;
      }
      const production = JSON.parse(readFileSync(`../videos/production/${node.id}.json`, "utf8"));
      expect(production.production_status, node.id).toBe("final");
      expect(existsSync(node.video?.src ?? ""), node.id).toBe(true);
      const script = readFileSync(join("..", production.source));
      expect(script.length, node.id).toBeGreaterThan(0);
      expect(createHash("sha256").update(script).digest("hex"), node.id).toBe(production.source_sha256);
    }
  });

  test("every unavailable parent preview is tracked in the to-do folder", () => {
    const todo = readFileSync("scripts/to-do/README.md", "utf8");
    const queued = [...todo.matchAll(/^\| `([a-z0-9-]+)` \| `([a-z0-9-]+)` \|/gm)]
      .map(([, parent, child]) => `${parent}/${child}`);
    const unavailable = entries.flatMap(({ node }) => node.children
      .filter((child) => !cutVideo(node, child))
      .map((child) => `${node.id}/${child.node.id}`));
    expect(queued.sort()).toEqual(unavailable.sort());
  });
});
