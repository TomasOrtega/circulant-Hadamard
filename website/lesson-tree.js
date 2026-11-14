import { posix } from "node:path";

export function collectLessons(root) {
  const entries = [];

  const visit = (lesson, path, ancestors, numbers) => {
    if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(lesson.id)) {
      throw new Error(`Invalid lesson slug: ${lesson.id}`);
    }
    if (!lesson.title || !lesson.shortTitle || !lesson.summary) {
      throw new Error(`Missing lesson text: ${lesson.id}`);
    }
    if (ancestors.some((ancestor) => ancestor.lesson === lesson)) {
      throw new Error(`Circular lesson hierarchy: ${lesson.id}`);
    }
    const chapters = lesson.chapters ?? [];
    if (lesson.foundation && chapters.length) {
      throw new Error(`Undergraduate foundations must be leaves: ${lesson.id}`);
    }
    if (
      new Set(chapters.map((chapter) => chapter.id)).size !== chapters.length
    ) {
      throw new Error(`Duplicate chapter slugs: ${lesson.id}`);
    }

    const entry = { lesson, path, ancestors, numbers };
    entries.push(entry);
    chapters.forEach((chapter, index) => {
      visit(
        chapter,
        [...path, chapter.id],
        [...ancestors, entry],
        [...numbers, index + 1],
      );
    });
  };

  visit(root, [], [], []);
  return entries;
}

export const pagePath = (entry) =>
  entry.path.length
    ? `lessons/${entry.path.join("/")}/index.html`
    : "index.html";

export const hrefFor = (target, current) =>
  posix.relative(posix.dirname(pagePath(current)), pagePath(target));

export const assetRoot = (entry) =>
  entry.path.length ? "../".repeat(entry.path.length + 1) : "./";

export const chapterAnchor = (lesson) => `chapter-${lesson.id}`;
