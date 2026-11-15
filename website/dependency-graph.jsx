import { dependencyGraph } from "./dependencies.js";
import { hrefFor, findChildEntry } from "./node-tree.js";

const defaultNodeWidth = 200;
const defaultNodeHeight = 64;
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
  const proofMap = owner.node.graphLayout === "proof-map";
  const nodeWidth = proofMap ? 300 : defaultNodeWidth;
  const nodeHeight = proofMap ? 96 : defaultNodeHeight;
  const children = owner.node.children?.length
    ? owner.node.children.filter(({ node }) => !node.supplemental)
    : [{ node: entry.node, dependsOn: [] }];
  const { layers, edges } = dependencyGraph(children);
  const rows = Math.max(...layers.map((layer) => layer.length));
  const width =
    proofMap ? 800 : padding * 2 + layers.length * nodeWidth + (layers.length - 1) * columnGap;
  const height = proofMap ? 1100 : padding * 2 + rows * nodeHeight + (rows - 1) * rowGap;
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
  if (proofMap) {
    for (const { node } of children) {
      if (!Array.isArray(node.mapPosition) || node.mapPosition.length !== 2 ||
          node.mapPosition.some((value) => !Number.isFinite(value)))
        throw new Error(`Missing proof-map position: ${node.id}`);
      positions.set(node.id, { x: node.mapPosition[0], y: node.mapPosition[1] });
    }
  }
  const titleId = `dependency-title-${entry.node.id}`;
  const descriptionId = `dependency-description-${entry.node.id}`;
  const markerId = `dependency-arrow-${entry.node.id}`;
  const graph = (
    <nav
      aria-label="Node dependency graph"
      className="w-full max-w-200 font-sans"
    >
      <figure className="flex flex-col gap-4">
        <figcaption className="text-center text-sm text-dark-gray">
          {proofMap ? "Eight-node proof map · general argument" : `Draft dependency map · ${owner.node.shortTitle}`}
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
            className={proofMap ? "mx-auto block h-auto w-full min-w-180" : "mx-auto block max-w-none"}
            role="group"
            aria-labelledby={`${titleId} ${descriptionId}`}
          >
            <title id={titleId}>Dependencies between the child nodes</title>
            <desc id={descriptionId}>
              Connections show how the statements fit together.
              Each box is a link to that node.
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
            {edges.map(({ source, target, kind }, index) => {
              const from = positions.get(source);
              const to = positions.get(target);
              const startX = from.x + nodeWidth;
              const startY = from.y + nodeHeight / 2;
              const endY = to.y + nodeHeight / 2;
              const lane = 12 + (index % 3) * 10;
              let path =
                to.column - from.column > 1
                  ? `M ${startX} ${startY} C ${startX + 24} ${startY}, ${startX + 24} ${lane}, ${startX + 40} ${lane} L ${to.x - 40} ${lane} C ${to.x - 24} ${lane}, ${to.x - 24} ${endY}, ${to.x} ${endY}`
                  : `M ${startX} ${startY} C ${startX + columnGap / 2} ${startY}, ${to.x - columnGap / 2} ${endY}, ${to.x} ${endY}`;
              if (proofMap) {
                if (from.y === to.y) {
                  path = `M ${startX} ${startY} L ${to.x} ${endY}`;
                } else if (source === "signs-become-all-ones" && target === "final-contradiction") {
                  path = `M ${from.x} ${startY} H 20 V ${endY} H ${to.x}`;
                } else {
                  const x1 = from.x + nodeWidth / 2;
                  const y1 = from.y + nodeHeight;
                  const x2 = to.x + nodeWidth / 2;
                  path = `M ${x1} ${y1} L ${x2} ${to.y}`;
                }
              }
              return (
                <path
                  key={`${source}-${target}`}
                  d={path}
                  fill="none"
                  className="stroke-gray"
                  data-source={source}
                  data-target={target}
                  data-edge-kind={kind ?? "dependency"}
                  strokeWidth="1.5"
                  markerEnd={`url(#${markerId})`}
                  aria-hidden="true"
                />
              );
            })}
            {children.map(({ node, dependsOn = [], contextFrom = [] }) => {
              const position = positions.get(node.id);
              const target =
                node === entry.node
                  ? entry
                  : findChildEntry(node, owner, entries);
              const lines = wrapLabel(`${node.number ? `${node.number}. ` : ""}${node.shortTitle}`);
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
                  aria-label={`Explore node: ${node.title}${prerequisites.length ? `. Uses: ${prerequisites.join(", ")}` : ". No prerequisites in this view"}${contextFrom.length ? ". Shared notation only from Group-Ring Encoding" : ""}`}
                  data-node-id={node.id}
                >
                  <title>{`${node.title}${contextFrom.length ? ". Shared notation from Group-Ring Encoding; no sign hypothesis." : ""}`}</title>
                  <rect
                    x={position.x}
                    y={position.y}
                    width={nodeWidth}
                    height={nodeHeight}
                    rx="10"
                    className={
                      current
                        ? "fill-theme/15 stroke-theme"
                        : "fill-white stroke-theme/50 group-hocus:fill-theme/15 group-hocus:stroke-theme"
                    }
                  />
                  <text
                    x={position.x + nodeWidth / 2}
                    y={
                      position.y +
                      nodeHeight / 2 - (proofMap ? 13 : 0) -
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
                  {proofMap && (
                    <text x={position.x + nodeWidth / 2} y={position.y + 76}
                      textAnchor="middle" className="fill-dark-gray text-xs">
                      {node.mapSummary}
                    </text>
                  )}
                </a>
              );
            })}
          </svg>
        </div>
        <p className="text-center text-sm text-dark-gray">
          Click any node to read its statement.
        </p>
      </figure>
    </nav>
  );
  if (proofMap && entry !== owner) {
    return (
      <details className="w-full max-w-200 rounded-md bg-white p-4 font-sans">
        <summary className="cursor-pointer">Show the high-level proof map</summary>
        {graph}
      </details>
    );
  }
  return graph;
}
