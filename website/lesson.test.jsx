import { afterAll, describe, expect, test } from "bun:test";
import { mkdtempSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { renderToStaticMarkup } from "react-dom/server";
import { buildLessons } from "./build-lessons.jsx";
import {
  collectLessons,
  hrefFor,
  pagePath,
  chapterAnchor,
} from "./lesson-tree.js";
import { LessonPage } from "./lesson.jsx";
import { lessons } from "./lessons.js";

const output = mkdtempSync(join(tmpdir(), "circulant-lessons-"));
const entries = buildLessons({ outDir: output });
afterAll(() => rmSync(output, { recursive: true, force: true }));

describe("recursive lesson navigation", () => {
  test("every chapter has its own page, a deeper link, and a direct parent link", () => {
    expect(
      Math.max(...entries.map((entry) => entry.path.length)),
    ).toBeGreaterThan(2);
    for (const entry of entries) {
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      expect(html).toContain(`<h1>${entry.lesson.title}</h1>`);
      const parent = entry.ancestors.at(-1);
      if (parent) {
        const parentHtml = readFileSync(join(output, pagePath(parent)), "utf8");
        expect(parentHtml).toContain(`href="${hrefFor(entry, parent)}"`);
        expect(html).toContain(
          `href="${hrefFor(parent, entry)}#${chapterAnchor(entry.lesson)}"`,
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
        expect(
          targetHtml,
          `Broken lesson link: ${filename} → ${href}`,
        ).toBeDefined();
        if (target.hash)
          expect(targetHtml).toContain(`id="${target.hash.slice(1)}"`);
      }
    }
  });

  test("every view has an overview slot, and each chapter has a clip and deeper button", () => {
    for (const entry of entries) {
      const html = readFileSync(join(output, pagePath(entry)), "utf8");
      const chapters = entry.lesson.chapters ?? [];
      expect(html).toContain("Overview video");
      expect([...html.matchAll(/>Chapter clip</g)]).toHaveLength(
        chapters.length,
      );
      expect([...html.matchAll(/aria-label="Dig in deeper:/g)]).toHaveLength(
        chapters.length,
      );
      expect(html).not.toContain("<iframe");
      expect(html).not.toContain("<video");
      expect(html).not.toContain("<script");
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
      expect(html).not.toContain("<!-- lesson-content -->");
      expect(html).not.toContain("{{asset-root}}");
    }
  });
});

describe("lesson authoring constraints", () => {
  test("undergraduate foundations are terminal views", () => {
    const foundations = entries.filter((entry) => entry.lesson.foundation);
    expect(foundations.length).toBeGreaterThan(0);
    for (const entry of foundations) {
      expect(entry.lesson.chapters).toHaveLength(0);
      expect(readFileSync(join(output, pagePath(entry)), "utf8")).not.toContain(
        "Dig in deeper",
      );
    }
    const foundation = foundations[0].lesson;
    expect(() =>
      collectLessons({ ...foundation, chapters: [foundation] }),
    ).toThrow("Undergraduate foundations must be leaves");
  });

  test("duplicate slugs and circular hierarchies fail the build", () => {
    expect(() =>
      collectLessons({
        ...lessons,
        chapters: [lessons.chapters[0], lessons.chapters[0]],
      }),
    ).toThrow("Duplicate chapter slugs");
    const circular = { ...lessons, chapters: [] };
    circular.chapters.push(circular);
    expect(() => collectLessons(circular)).toThrow("Circular lesson hierarchy");
  });

  test("the displayed order-four example has orthogonal cyclic shifts", () => {
    const firstRow = entries.find((entry) => entry.lesson.exampleRow).lesson
      .exampleRow;
    for (let shift = 0; shift < firstRow.length; shift++) {
      const correlation = firstRow.reduce(
        (sum, value, position) =>
          sum + value * firstRow[(position + shift) % firstRow.length],
        0,
      );
      expect(correlation).toBe(shift === 0 ? firstRow.length : 0);
    }
  });

  test("configured videos render real players and relative file URLs work at depth", () => {
    const child = {
      ...lessons.chapters[0].chapters[0],
      video: { src: "media/test.mp4", captions: "media/test.vtt" },
      clip: { youtubeId: "abcdefghijk" },
    };
    const configured = collectLessons({
      ...lessons,
      video: { youtubeId: "abcdefghijk" },
      chapters: [child],
    });
    const rootHtml = renderToStaticMarkup(
      <LessonPage entry={configured[0]} entries={configured} />,
    );
    const childHtml = renderToStaticMarkup(
      <LessonPage entry={configured[1]} entries={configured} />,
    );
    expect(rootHtml).toContain(
      "https://www.youtube-nocookie.com/embed/abcdefghijk",
    );
    expect(childHtml).toContain('src="../../media/test.mp4"');
    expect(childHtml).toContain('src="../../media/test.vtt"');
    expect(childHtml).toContain("controls");
  });
});
