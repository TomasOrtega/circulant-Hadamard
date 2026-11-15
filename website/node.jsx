import { assetRoot, nodeAnchor, hrefFor, findChildEntry } from "./node-tree.js";
import { DependencyGraph } from "./dependency-graph.jsx";
import { cutVideo, mediaUrl, formatTime } from "./node-video.js";
import { renderMarkdown } from "./markdown.js";

const buttonBase =
  "inline-flex max-w-full items-center justify-center gap-2 rounded-md font-sans text-balance no-underline min-h-12 min-w-12 p-3 text-lg";

function NodeButton({
  href,
  children,
  primary = false,
  className = "",
  ...props
}) {
  const color = primary
    ? "bg-theme text-white change-ring hocus:bg-black hocus:outline-black"
    : "text-black hocus:bg-theme/15 hocus:text-theme";
  return (
    <a href={href} className={`${buttonBase} ${color} ${className}`} {...props}>
      {children}
    </a>
  );
}

function Media({ video, title, excerpt = false, base }) {
  const label = excerpt ? "Node excerpt" : "Overview video";
  const frameClass = "aspect-video w-full rounded-md bg-black";
  const segment = video?.segment;
  let player = null;
  if (video?.youtubeId) {
    const query = segment
      ? `?${new URLSearchParams({ start: segment.start, end: segment.end })}`
      : "";
    player = (
      <iframe
        className={`${frameClass} min-h-50`}
        src={`https://www.youtube-nocookie.com/embed/${video.youtubeId}${query}`}
        title={`${label}: ${title}`}
        loading="lazy"
        allow="fullscreen; picture-in-picture"
        allowFullScreen
      />
    );
  } else if (video?.src) {
    const source = mediaUrl(video.src, base);
    const cutSource = segment
      ? `${source.split("#")[0]}#t=${segment.start},${segment.end}`
      : source;
    player = (
      <video
        className={frameClass}
        controls
        preload="none"
        playsInline
        aria-label={`${label}: ${title}`}
        data-cut-start={segment?.start}
        data-cut-end={segment?.end}
      >
        <source src={cutSource} />
        {video.captions && (
          <track
            kind="captions"
            src={mediaUrl(video.captions, base)}
            srcLang="en"
            label="English"
            default
          />
        )}
        Your browser cannot play this video.{" "}
        <a href={cutSource}>Open the video</a>.
      </video>
    );
  }
  return (
    <figure className="flex w-full flex-col gap-3">
      {player ?? (
        <div
          className="min-h-32 w-full rounded-md bg-black flex flex-col items-center justify-center gap-4 p-6 text-center font-sans text-white"
        >
          <span className="text-lg">{label}</span>
          <span className="text-sm text-gray">
            {excerpt ? "Excerpt not added yet" : "Video not added yet"}
          </span>
        </div>
      )}
      <figcaption className="text-center font-sans text-sm text-dark-gray">
        {segment
          ? `Cut from the overview · ${formatTime(segment.start)}–${formatTime(segment.end)}`
          : excerpt
            ? title
            : `Full overview · ${title}`}
      </figcaption>
    </figure>
  );
}

function ParentButton({ entry }) {
  const parent = entry.ancestors.at(-1);
  if (!parent) return null;
  return (
    <NodeButton
      href={`${hrefFor(parent, entry)}#${nodeAnchor(entry.node)}`}
      aria-label={`Back to higher-level view: ${parent.node.title}`}
    >
      <span aria-hidden="true">←</span> Back to {parent.node.shortTitle}
    </NodeButton>
  );
}

function Breadcrumbs({ entry }) {
  return (
    <nav
      aria-label="Breadcrumb"
      className="flex flex-wrap items-center gap-2 font-sans text-sm"
    >
      {entry.ancestors.map((ancestor) => (
        <span
          key={ancestor.path.join("/")}
          className="inline-flex items-center gap-2"
        >
          <a href={hrefFor(ancestor, entry)}>{ancestor.node.shortTitle}</a>
          <span aria-hidden="true">/</span>
        </span>
      ))}
      <span aria-current="page">{entry.node.shortTitle}</span>
    </nav>
  );
}

function Heading({ id, children }) {
  return (
    <h2 id={id}>
      <hr />
      <span>{children}</span>
      <hr />
    </h2>
  );
}

function Markdown({ script }) {
  return (
    <>
      <div className="flex min-w-0 flex-col gap-8 overflow-x-auto"
        dangerouslySetInnerHTML={{ __html: renderMarkdown(script.join("\n\n")).html }} />
      {script.some((text) => text.includes("$")) && (
        <details className="w-full max-w-200 font-sans text-sm text-dark-gray">
          <summary className="cursor-pointer">Copyable text and LaTeX</summary>
          <pre className="mt-4 max-h-100 overflow-auto whitespace-pre-wrap rounded-md bg-light-gray p-4">{script.join("\n\n")}</pre>
        </details>
      )}
    </>
  );
}

function ChildNode({ child, entry, entries }) {
  const node = child.node;
  const target = findChildEntry(node, entry, entries);
  const count = node.children?.length ?? 0;
  return (
    <section id={nodeAnchor(node)} className="width-lg">
      <Heading>
        {node.number ? `${node.number}. ` : ""}{node.title}
      </Heading>
      <div className="grid grid-cols-[minmax(0,1fr)_14rem] items-start gap-12 max-md:grid-cols-1 max-md:gap-8">
        <div className="flex min-w-0 flex-col gap-8 [&_blockquote]:border-y [&_blockquote]:border-theme/25 [&_blockquote]:py-6">
          <Markdown script={child.script} />
          <div className="w-full max-w-125 self-center">
            <Media
              video={cutVideo(entry.node, child)}
              title={node.title}
              excerpt
              base={assetRoot(entry)}
            />
          </div>
        </div>
        <aside className="flex flex-col items-start gap-4 max-md:items-center">
          <NodeButton
            href={hrefFor(target, entry)}
            primary
            aria-label={`Dig in deeper: ${node.title}`}
          >
            Dig in deeper <span aria-hidden="true">→</span>
          </NodeButton>
          <p className="font-sans text-sm text-dark-gray">
            {node.blackBox
              ? `Accepted black box · ${node.blackBox}`
              : node.foundation
              ? "Undergraduate foundation"
              : count
                ? `${count} child nodes`
                : "Statement ready · video script pending"}
          </p>
        </aside>
      </div>
    </section>
  );
}

function ReadingRoutes({ entry, entries }) {
  const routes = entries.filter(({ node, ancestors }) => node.supplemental && ancestors.length === 1);
  if (!routes.length) return null;
  return (
    <nav aria-label="Reading routes" className="flex flex-wrap justify-center gap-4 font-sans">
      {routes.map((route, index) => (
        <NodeButton key={route.node.id} href={hrefFor(route, entry)} primary={index === 0}
          id={entry.ancestors.length ? undefined : nodeAnchor(route.node)}
          aria-current={route === entry ? "page" : undefined}>
          {index === 0 ? "Start here · " : "Then · "}{route.node.title}
        </NodeButton>
      ))}
    </nav>
  );
}

function NodeDependencies({ entry, entries }) {
  const owner = entry.ancestors.at(-1);
  if (!owner || entry.node.supplemental) return null;
  const siblings = owner.node.children;
  const current = siblings.find(({ node }) => node === entry.node);
  const incoming = current.dependsOn ?? [];
  const context = current.contextFrom ?? [];
  const outgoing = siblings.filter(({ dependsOn = [] }) => dependsOn.includes(entry.node.id));
  const notationFor = siblings.filter(({ contextFrom = [] }) => contextFrom.includes(entry.node.id));
  const links = (ids) => ids.map((id, index) => {
    const node = siblings.find(({ node }) => node.id === id).node;
    const target = findChildEntry(node, owner, entries);
    return <span key={id}>{index ? ", " : ""}<a href={hrefFor(target, entry)}>{node.title}</a></span>;
  });
  return (
    <nav aria-label="Incoming and outgoing dependencies" className="w-full rounded-md bg-light-gray p-6 font-sans text-sm">
      <p><strong>Uses: </strong>{incoming.length ? links(incoming) : "No earlier proof node."}</p>
      {!!context.length && <p><strong>Shared notation only: </strong>{links(context)}</p>}
      <p><strong>Used by: </strong>{outgoing.length ? links(outgoing.map(({ node }) => node.id)) : "Conclusion of the proof map."}</p>
      {!!notationFor.length && <p><strong>Supplies notation to: </strong>{links(notationFor.map(({ node }) => node.id))}</p>}
    </nav>
  );
}

export function NodePage({ entry, entries }) {
  const { node } = entry;
  const root = entries[0];
  const children = (node.children ?? []).filter(({ node: child }) => !child.supplemental);
  const base = assetRoot(entry);
  const hasOwnProofMap = node.graphLayout === "proof-map";
  const showOwnExplanation = !entry.ancestors.length || !children.length;
  return (
    <>
      <a
        href="#content"
        className="fixed top-0 left-0 z-50 bg-white p-2 text-black not-focus-visible:sr-only"
      >
        Jump to main content
      </a>
      <header className="dark relative flex flex-wrap items-center justify-between gap-4 bg-white p-8 text-black max-md:p-4 print:hidden">
        <NodeButton href={hrefFor(root, entry)}>
          <span className="font-serif text-2xl">Circulant Hadamard</span>
        </NodeButton>
        <nav aria-label="Project links" className="flex flex-wrap gap-2">
          <NodeButton href="https://competition.sair.foundation/competitions/mathathon/problems/76">
            Problem 76
          </NodeButton>
          <NodeButton href="https://github.com/TomasOrtega/circulant-Hadamard">
            Repository
          </NodeButton>
        </nav>
      </header>
      <main id="content" className="striped">
        <section className="items-center bg-theme/15 width-lg">
          <div className="flex w-full flex-wrap items-center justify-between gap-4">
            <Breadcrumbs entry={entry} />
            <ParentButton entry={entry} />
          </div>
          <hgroup className="flex flex-col items-center gap-4 font-sans">
            <p className="text-dark-gray">
              {node.number
                ? `Node ${node.number}`
                : "The argument, one node at a time"}
            </p>
            <h1>{node.title}</h1>
            <span className="text-sm text-dark-gray">
              {node.blackBox
                ? `Accepted black box · ${node.blackBox}`
                : node.foundation
                ? "Undergraduate foundation"
                : node.draft
                  ? "Exposition draft"
                  : "Draft node"}
            </span>
          </hgroup>
          <ReadingRoutes entry={entry} entries={entries} />
          <div className="w-full max-w-200">
            <Media video={node.video} title={node.title} base={base} />
          </div>
          <DependencyGraph entry={entry} entries={entries} />
          {showOwnExplanation && hasOwnProofMap && (
            <div className="w-full max-w-200 rounded-md bg-white p-8 text-left max-md:p-6 [&_blockquote]:border-y [&_blockquote]:border-theme/25 [&_blockquote]:py-6">
              <Markdown script={node.script} />
            </div>
          )}
          {showOwnExplanation && <p className="max-w-175 text-center text-lg">{node.summary}</p>}
        </section>
        <section>
          <NodeDependencies entry={entry} entries={entries} />
          {showOwnExplanation && !hasOwnProofMap && <Markdown script={node.script} />}
          {!!children.length && (
            <nav
              aria-label="Child nodes in this view"
              className="flex flex-col items-start gap-4 font-sans"
            >
              {children.map(({ node: child }, index) => (
                <a key={child.id} href={`#${nodeAnchor(child)}`}>
                  {child.number ? `${child.number}. ` : ""}{child.title}
                </a>
              ))}
            </nav>
          )}
        </section>
        {children.map((child) => (
          <ChildNode
            key={child.node.id}
            child={child}
            entry={entry}
            entries={entries}
          />
        ))}
        {!!entry.ancestors.length && (
          <section className="items-center bg-theme/10 text-center">
            <p>Return to the bigger picture.</p>
            <ParentButton entry={entry} />
          </section>
        )}
      </main>
      <footer className="flex flex-col items-center gap-4 bg-alt-white p-8 text-center font-sans text-sm text-dark-gray">
        <p>
          A project for the Caltech × SAIR Mathathon, by Steven Creech and Tomas
          Ortega
        </p>
      </footer>
      {node.video?.src && children.some((child) => child.segment) && (
        <script src={`${base}video-player.js`} defer />
      )}
    </>
  );
}
