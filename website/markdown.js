import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import remarkRehype from "remark-rehype";
import rehypeMathjax from "rehype-mathjax/svg";
import rehypeStringify from "rehype-stringify";

function extractStyles() {
  return (tree, file) => {
    const styles = [];
    const walk = (node) => {
      if (!node.children) return;
      node.children = node.children.filter((child) => {
        if (child.type === "element" && child.tagName === "style") {
          styles.push(child.children.map((text) => text.value ?? "").join(""));
          return false;
        }
        walk(child);
        return true;
      });
    };
    walk(tree);
    file.data.mathStyles = styles.join("\n");
  };
}

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)
  .use(remarkMath)
  .use(remarkRehype)
  .use(rehypeMathjax, {
    svg: { fontCache: "none" },
    tex: {
      formatError: (_jax, error) => {
        throw error;
      },
    },
  })
  .use(extractStyles)
  .use(rehypeStringify);

const cache = new Map();

export function renderMarkdown(source, label = "Markdown") {
  if (cache.has(source)) return cache.get(source);
  const file = processor.processSync(source);
  if (file.messages.length) {
    throw new Error(
      `Invalid Markdown math in ${label}: ${file.messages.map((message) => message.cause?.message ?? message.reason).join("; ")}`,
    );
  }
  const result = { html: String(file), css: file.data.mathStyles ?? "" };
  cache.set(source, result);
  return result;
}

export function mathStyles(entries) {
  const styles = new Set();
  for (const { node } of entries) {
    styles.add(renderMarkdown(node.script.join("\n\n"), `${node.id}.md`).css);
    for (const child of node.children ?? []) {
      styles.add(
        renderMarkdown(
          child.script.join("\n\n"),
          `${node.id}.md (cut for ${child.node.id})`,
        ).css,
      );
    }
  }
  return [...styles].filter(Boolean).join("\n");
}
