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
import { lessons } from "./lessons.js";
import { assetRoot, collectLessons, pagePath } from "./lesson-tree.js";
import { LessonPage } from "./lesson.jsx";

export function buildLessons({
  outDir = resolve("dist"),
  root = lessons,
} = {}) {
  const entries = collectLessons(root);
  const template = readFileSync("index.html", "utf8");
  rmSync(resolve(outDir, "lessons"), { recursive: true, force: true });
  for (const entry of entries) {
    const title = entry.path.length
      ? `${entry.lesson.title} · Circulant Hadamard`
      : entry.lesson.title;
    const metadata = renderToStaticMarkup(
      <>
        <title>{title}</title>
        <meta name="description" content={entry.lesson.summary} />
      </>,
    );
    const content = renderToStaticMarkup(
      <LessonPage entry={entry} entries={entries} />,
    );
    const html = template
      .replace("<!-- lesson-meta -->", () => metadata)
      .replaceAll("{{asset-root}}", assetRoot(entry))
      .replace("<!-- lesson-content -->", () => content);
    const output = resolve(outDir, pagePath(entry));
    mkdirSync(dirname(output), { recursive: true });
    writeFileSync(output, html);
  }
  if (existsSync("media"))
    cpSync("media", resolve(outDir, "media"), { recursive: true });
  return entries;
}

if (
  process.argv[1] &&
  resolve(process.argv[1]) === fileURLToPath(import.meta.url)
) {
  const entries = buildLessons();
  console.log(`Built ${entries.length} lesson pages.`);
}
