export function dependencyGraph(children) {
  const ids = children.map(({ node }) => node.id);
  if (new Set(ids).size !== ids.length)
    throw new Error("Duplicate child node IDs");
  const known = new Set(ids);
  const edges = [];
  for (const child of children) {
    const prerequisites = child.dependsOn ?? [];
    if (
      !Array.isArray(prerequisites) ||
      new Set(prerequisites).size !== prerequisites.length
    ) {
      throw new Error(`Invalid dependencies for ${child.node.id}`);
    }
    for (const source of prerequisites) {
      if (!known.has(source)) throw new Error(`Unknown dependency: ${source}`);
      edges.push({ source, target: child.node.id });
    }
  }
  const remaining = new Set(ids);
  const layers = [];
  while (remaining.size) {
    const ready = children.filter(
      ({ node, dependsOn = [] }) =>
        remaining.has(node.id) && dependsOn.every((id) => !remaining.has(id)),
    );
    if (!ready.length) throw new Error("Circular node dependencies");
    layers.push(ready);
    ready.forEach(({ node }) => remaining.delete(node.id));
  }
  return { layers, edges };
}
