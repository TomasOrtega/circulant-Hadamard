import { describe, expect, test } from "bun:test";
import { readdirSync } from "node:fs";
import { renderToStaticMarkup } from "react-dom/server";
import { loadNodes } from "../load-nodes.js";
import { dependencyGraph } from "../dependencies.js";
import { collectNodes, hrefFor } from "../node-tree.js";
import { NodePage } from "../node.jsx";

const rootNode = loadNodes();
import { cutVideo } from "../node-video.js";

const leaf = (id) => ({
  id,
  title: id,
  shortTitle: id,
  summary: `About ${id}`,
  video: null,
  script: [`Narration for ${id}`],
  children: [],
  foundation: true,
});
const child = (id, dependsOn = [], segment = null) => ({
  node: leaf(id),
  dependsOn,
  segment,
  script: [`Parent narration for ${id}`],
});
const render = (root) => {
  const entries = collectNodes(root);
  return {
    entries,
    html: renderToStaticMarkup(
      <NodePage entry={entries[0]} entries={entries} />,
    ),
  };
};

describe("node files and dependency navigation", () => {
  test("each reachable node has one content file and no legacy content fields", () => {
    const entries = collectNodes(rootNode);
    expect(
      readdirSync("nodes")
        .filter((name) => name.endsWith(".md"))
        .sort(),
    ).toEqual([...new Set(entries.map(({ node }) => `${node.id}.md`))].sort());
    for (const { node } of entries) {
      expect(node).not.toHaveProperty("chapters");
      expect(node).not.toHaveProperty("paragraphs");
      expect(node).not.toHaveProperty("clip");
    }
  });

  test("branching dependencies are ordered independently of display order", () => {
    const children = [
      child("finish", ["left", "right"]),
      child("right", ["start"]),
      child("start"),
      child("left", ["start"]),
    ];
    const graph = dependencyGraph(children);
    expect(
      graph.layers.map((layer) => layer.map(({ node }) => node.id)),
    ).toEqual([["start"], ["right", "left"], ["finish"]]);
    expect(graph.edges).toHaveLength(4);
    expect(children.map(({ node }) => node.id)).toEqual([
      "finish",
      "right",
      "start",
      "left",
    ]);
  });

  test("dependency cycles, missing references, and self-dependencies are rejected", () => {
    expect(() =>
      dependencyGraph([child("a", ["b"]), child("b", ["a"])]),
    ).toThrow("Circular node dependencies");
    expect(() => dependencyGraph([child("a", ["missing"])])).toThrow(
      "Unknown dependency",
    );
    expect(() => dependencyGraph([child("a", ["a"])])).toThrow(
      "Circular node dependencies",
    );
  });

  test("terminal statement views keep their parent graph for navigation", () => {
    const entries = collectNodes(rootNode);
    const entry = entries.find(({ node, ancestors }) => ancestors.length && !node.children.length);
    const parent = entry.ancestors.at(-1);
    const sibling = parent.node.children.find(({ node }) => node !== entry.node).node;
    const html = renderToStaticMarkup(
      <NodePage entry={entry} entries={entries} />,
    );
    expect(html).toContain('aria-label="Node dependency graph"');
    expect(html).toContain(renderToStaticMarkup(<>{`Explore node: ${sibling.title}`}</>));
    expect(html).toContain('aria-current="page"');
  });

  test.each([0, 1])("automatic layouts use a collapsed graph dropdown in view %i", (index) => {
    const { entries } = render({ ...leaf("parent"), foundation: false, children: [child("detail")] });
    const html = renderToStaticMarkup(<NodePage entry={entries[index]} entries={entries} />);
    const dropdown = html.match(/<details\b[^>]*>[\s\S]*?<\/details>/)?.[0];
    expect(dropdown).toBeDefined();
    expect(dropdown.includes('aria-label="Node dependency graph"')).toBe(true);
    expect(dropdown.match(/^<details\b[^>]*><summary\b[^>]*>([^<]*)<\/summary>/)?.[1]).toBe("Show the proof map");
    expect(/^<details\b[^>]*\bopen(?:[\s=>])/.test(dropdown)).toBe(false);
  });

  test("reused node files keep navigation in the current parent context", () => {
    const shared = leaf("shared");
    const parents = ["first", "second"].map((id) => ({
      ...child(id),
      node: {
        ...leaf(id),
        foundation: false,
        children: [
          {
            node: shared,
            script: ["Shared cut"],
            segment: null,
            dependsOn: [],
          },
        ],
      },
    }));
    const entries = collectNodes({ ...rootNode, graphLayout: null, children: parents });
    const second = entries.find((entry) => entry.node.id === "second");
    const sharedSecond = entries.find(
      (entry) => entry.path.join("/") === "second/shared",
    );
    const html = renderToStaticMarkup(
      <NodePage entry={second} entries={entries} />,
    );
    expect(html).toContain(`href="${hrefFor(sharedSecond, second)}"`);
    expect(html).not.toContain('href="../first/shared/index.html"');
  });

  test("proof graphs follow the main video and link to every proof child at every depth", () => {
    const entries = collectNodes(rootNode);
    for (const entry of entries) {
      const html = renderToStaticMarkup(
        <NodePage entry={entry} entries={entries} />,
      );
      const owner = entry.node.children.length ? entry : entry.ancestors.at(-1);
      const children = owner.node.children;
      const graphStart = html.indexOf('aria-label="Node dependency graph"');
      if (children.length) expect(graphStart).toBeGreaterThan(html.indexOf("Full overview ·"));
      else expect(graphStart).toBe(-1);
      expect([...html.matchAll(/aria-label="Explore node:/g)]).toHaveLength(
        children.length,
      );
      for (const { node } of children) {
        const target = entries.find((candidate) => candidate.node === node);
        expect(html).toContain(`href="${hrefFor(target, entry)}"`);
        expect(html).toContain(renderToStaticMarkup(<>{`Explore node: ${node.title}`}</>));
      }
    }
  });
});

describe("one long video per node", () => {
  test("child previews use timed cuts of the parent, while child pages keep their own overview", () => {
    const link = child("detail", [], { start: 20, end: 55 });
    link.node.video = { youtubeId: "lmnopqrstuv", duration: 200 };
    const parent = {
      ...rootNode, graphLayout: null,
      video: { youtubeId: "abcdefghijk", duration: 300 },
      children: [link],
    };
    const { html, entries } = render(parent);
    expect(html).toContain(
      'src="https://www.youtube-nocookie.com/embed/abcdefghijk"',
    );
    expect(html).toContain(
      'src="https://www.youtube-nocookie.com/embed/abcdefghijk?start=20&amp;end=55"',
    );
    expect(html).not.toContain("embed/lmnopqrstuv");
    expect(html).toContain("Parent narration for detail");
    expect(html).not.toContain("Narration for detail");
    const detail = renderToStaticMarkup(
      <NodePage entry={entries[1]} entries={entries} />,
    );
    expect(detail).toContain(
      'src="https://www.youtube-nocookie.com/embed/lmnopqrstuv"',
    );
    expect(detail).toContain("Narration for detail");
  });

  test("an unconfigured cut never plays the full overview as a preview", () => {
    const parent = {
      ...rootNode, graphLayout: null,
      video: { youtubeId: "abcdefghijk" },
      children: [child("detail")],
    };
    const { html } = render(parent);
    expect(cutVideo(parent, parent.children[0])).toBeNull();
    expect([...html.matchAll(/<iframe/g)]).toHaveLength(1);
    expect(html).toContain("Excerpt not added yet");
  });

  test("native cuts share the overview source and poster and include playback bounds", () => {
    const parent = {
      ...rootNode, graphLayout: null,
      video: { src: "media/long.mp4", poster: "media/thumbnails/long.jpg", duration: 300 },
      children: [child("detail", [], { start: 10.5, end: 45.5 })],
    };
    const { html } = render(parent);
    expect(html).toContain('src="./media/long.mp4#t=10.5,45.5"');
    expect([...html.matchAll(/poster="\.\/media\/thumbnails\/long\.jpg"/g)]).toHaveLength(2);
    expect(html).toContain('data-cut-start="10.5"');
    expect(html).toContain('data-cut-end="45.5"');
    expect(html).toContain('src="./video-player.js"');
    expect(html).toContain("Parent narration for detail");
  });

  test("a native excerpt can show its own frame without changing its parent video source", () => {
    const parent = {
      ...rootNode, graphLayout: null,
      video: { src: "media/long.mp4", poster: "media/thumbnails/long.jpg", duration: 300 },
      children: [child("detail", [], {
        start: 10.5, end: 45.5, poster: "media/thumbnails/excerpts/detail.jpg",
      })],
    };
    const { html } = render(parent);
    const overview = html.match(/<video\b[^>]*aria-label="Overview video:[^"]*"[^>]*>/)[0];
    const excerpt = html.match(/<video\b[^>]*aria-label="Node excerpt:[^"]*"[^>]*>[\s\S]*?<\/video>/)[0];
    expect(overview).toContain('poster="./media/thumbnails/long.jpg"');
    expect(excerpt).toContain('poster="./media/thumbnails/excerpts/detail.jpg"');
    expect(excerpt).toContain('src="./media/long.mp4#t=10.5,45.5"');
    expect(parent.video.poster).toBe("media/thumbnails/long.jpg");
  });

  test("invalid or out-of-video cut times fail before publishing", () => {
    const fixture = (
      segment,
      video = { youtubeId: "abcdefghijk", duration: 100 },
    ) => ({ ...rootNode, graphLayout: null, video, children: [child("detail", [], segment)] });
    for (const segment of [
      { start: -1, end: 20 },
      { start: 20, end: 20 },
      { start: 50, end: 20 },
      { start: 0, end: Infinity },
    ]) {
      expect(() => collectNodes(fixture(segment))).toThrow("Invalid cut range");
    }
    expect(() => collectNodes(fixture({ start: 0, end: 101 }))).toThrow(
      "Cut exceeds overview duration",
    );
    expect(() => collectNodes(fixture({ start: 0.5, end: 20 }))).toThrow(
      "whole seconds",
    );
  });
});
