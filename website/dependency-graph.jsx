import { dependencyGraph } from "./dependencies.js";
import { hrefFor, findChildEntry } from "./node-tree.js";

const nodeWidth = 200;
const nodeHeight = 64;
const columnGap = 56;
const rowGap = 36;
const padding = 32;

const wrapLabel = (text) => {
  const lines = [""];
  for (const word of text.split(/\s+/)) {
    const last = lines.length - 1;
    if (lines[last] && lines[last].length + word.length > 24) lines.push(word);
    else lines[last] += `${lines[last] ? " " : ""}${word}`;
  }
  return lines;
};

export function DependencyGraph({ entry, entries }) {
  const owner = entry.node.children?.length
    ? entry
    : (entry.ancestors.at(-1) ?? entry);
  const children = owner.node.children?.length
    ? owner.node.children
    : [{ node: entry.node, dependsOn: [] }];
  const { layers, edges } = dependencyGraph(children);
  const rows = Math.max(...layers.map((layer) => layer.length));
  const width =
    padding * 2 + layers.length * nodeWidth + (layers.length - 1) * columnGap;
  const height = padding * 2 + rows * nodeHeight + (rows - 1) * rowGap;
  const positions = new Map();
  layers.forEach((layer, column) => {
    layer.forEach((child, row) =>
      positions.set(child.node.id, {
        x: padding + column * (nodeWidth + columnGap),
        y:
          padding +
          ((rows - layer.length) * (nodeHeight + rowGap)) / 2 +
          row * (nodeHeight + rowGap),
        column,
      }),
    );
  });
  const titleId = `dependency-title-${entry.node.id}`;
  const descriptionId = `dependency-description-${entry.node.id}`;
  const markerId = `dependency-arrow-${entry.node.id}`;
  return (
    <nav
      aria-label="Node dependency graph"
      className="w-full max-w-200 font-sans"
    >
      <figure className="flex flex-col gap-4">
        <figcaption className="text-center text-sm text-dark-gray">
          Draft dependency map · {owner.node.shortTitle}
        </figcaption>
        <div
          className="overflow-x-auto rounded-md bg-white p-2"
          tabIndex={0}
          aria-label="Scrollable node dependency graph"
        >
          <svg
            viewBox={`0 0 ${width} ${height}`}
            width={width}
            height={height}
            className="mx-auto block max-w-none"
            role="group"
            aria-labelledby={`${titleId} ${descriptionId}`}
          >
            <title id={titleId}>Dependencies between the child nodes</title>
            <desc id={descriptionId}>
              Arrows point from a prerequisite to the node that uses it. Each
              box is a link to that node.
            </desc>
            <defs>
              <marker
                id={markerId}
                viewBox="0 0 10 10"
                refX="9"
                refY="5"
                markerWidth="7"
                markerHeight="7"
                orient="auto-start-reverse"
              >
                <path d="M 0 0 L 10 5 L 0 10 z" className="fill-gray" />
              </marker>
            </defs>
            {edges.map(({ source, target }, index) => {
              const from = positions.get(source);
              const to = positions.get(target);
              const startX = from.x + nodeWidth;
              const startY = from.y + nodeHeight / 2;
              const endY = to.y + nodeHeight / 2;
              const lane = 12 + (index % 3) * 10;
              const path =
                to.column - from.column > 1
                  ? `M ${startX} ${startY} C ${startX + 24} ${startY}, ${startX + 24} ${lane}, ${startX + 40} ${lane} L ${to.x - 40} ${lane} C ${to.x - 24} ${lane}, ${to.x - 24} ${endY}, ${to.x} ${endY}`
                  : `M ${startX} ${startY} C ${startX + columnGap / 2} ${startY}, ${to.x - columnGap / 2} ${endY}, ${to.x} ${endY}`;
              return (
                <path
                  key={`${source}-${target}`}
                  d={path}
                  fill="none"
                  className="stroke-gray"
                  strokeWidth="1.5"
                  markerEnd={`url(#${markerId})`}
                  aria-hidden="true"
                />
              );
            })}
            {children.map(({ node, dependsOn = [] }) => {
              const position = positions.get(node.id);
              const target =
                node === entry.node
                  ? entry
                  : findChildEntry(node, owner, entries);
              const lines = wrapLabel(node.shortTitle);
              const current = node === entry.node;
              const prerequisites = dependsOn.map(
                (id) =>
                  children.find((child) => child.node.id === id).node
                    .shortTitle,
              );
              return (
                <a
                  key={node.id}
                  href={hrefFor(target, entry)}
                  tabIndex={0}
                  className={`group no-underline hocus:text-theme ${current ? "text-theme" : "text-black"}`}
                  aria-current={current ? "page" : undefined}
                  aria-label={`Explore node: ${node.title}${prerequisites.length ? `. Uses: ${prerequisites.join(", ")}` : ". No prerequisites in this view"}`}
                >
                  <title>{node.title}</title>
                  <rect
                    x={position.x}
                    y={position.y}
                    width={nodeWidth}
                    height={nodeHeight}
                    rx="10"
                    className={
                      current
                        ? "fill-theme/15 stroke-theme"
                        : "fill-white stroke-gray group-hocus:fill-theme/15 group-hocus:stroke-theme"
                    }
                  />
                  <text
                    x={position.x + nodeWidth / 2}
                    y={
                      position.y +
                      nodeHeight / 2 -
                      ((lines.length - 1) * 18) / 2
                    }
                    textAnchor="middle"
                    dominantBaseline="middle"
                    className="fill-current text-sm"
                  >
                    {lines.map((line, index) => (
                      <tspan
                        key={index}
                        x={position.x + nodeWidth / 2}
                        dy={index ? 18 : 0}
                      >
                        {line}
                      </tspan>
                    ))}
                  </text>
                </a>
              );
            })}
          </svg>
        </div>
        <p className="text-center text-sm text-dark-gray">
          Arrows point from a prerequisite to the node that uses it.
        </p>
      </figure>
    </nav>
  );
}
