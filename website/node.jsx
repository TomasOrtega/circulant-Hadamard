import { assetRoot, nodeAnchor, hrefFor, findChildEntry } from "./node-tree.js";
import { DependencyGraph } from "./dependency-graph.jsx";
import { cutVideo, mediaUrl, formatTime } from "./node-video.js";

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
          className={`${frameClass} flex flex-col items-center justify-center gap-4 p-8 text-center font-sans text-white`}
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

function Matrix({ row }) {
  return (
    <div className="overflow-x-auto">
      <table
        className="mx-auto font-mono text-xl"
        aria-label={`Circulant matrix generated from the first row (${row.join(", ")})`}
      >
        <tbody>
          {row.map((_, rowIndex) => (
            <tr key={rowIndex}>
              {row.map((_, columnIndex) => (
                <td key={columnIndex}>
                  {row[(columnIndex - rowIndex + row.length) % row.length]}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function ChildNode({ child, entry, entries }) {
  const node = child.node;
  const target = findChildEntry(node, entry, entries);
  const count = node.children?.length ?? 0;
  return (
    <section id={nodeAnchor(node)} className="width-lg">
      <Heading>
        {target.numbers.join(".")}. {node.title}
      </Heading>
      <div className="grid grid-cols-[minmax(0,1fr)_14rem] items-start gap-12 max-md:grid-cols-1 max-md:gap-8">
        <div className="flex min-w-0 flex-col gap-8">
          {child.script.map((paragraph) => (
            <p key={paragraph}>{paragraph}</p>
          ))}
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
            {node.foundation
              ? "Undergraduate foundation"
              : count
                ? `${count} child nodes`
                : "Draft proof node"}
          </p>
        </aside>
      </div>
    </section>
  );
}

export function NodePage({ entry, entries }) {
  const { node } = entry;
  const root = entries[0];
  const children = node.children ?? [];
  const base = assetRoot(entry);
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
              {entry.numbers.length
                ? `Node ${entry.numbers.join(".")}`
                : "The argument, one node at a time"}
            </p>
            <h1>{node.title}</h1>
            <span className="text-sm text-dark-gray">
              {node.foundation
                ? "Undergraduate foundation"
                : node.draft
                  ? "Draft proof node"
                  : "Draft node"}
            </span>
          </hgroup>
          <div className="w-full max-w-200">
            <Media video={node.video} title={node.title} base={base} />
          </div>
          <DependencyGraph entry={entry} entries={entries} />
          <p className="max-w-175 text-center text-lg">{node.summary}</p>
        </section>
        <section>
          <div className="flex flex-col gap-8">
            {node.script.map((paragraph) => (
              <p key={paragraph}>{paragraph}</p>
            ))}
            {node.equation && (
              <p role="math" className="text-center text-2xl">
                {node.equation}
              </p>
            )}
            {node.exampleRow && <Matrix row={node.exampleRow} />}
          </div>
          {!!children.length && (
            <nav
              aria-label="Child nodes in this view"
              className="flex flex-col items-start gap-4 font-sans"
            >
              {children.map(({ node: child }, index) => (
                <a key={child.id} href={`#${nodeAnchor(child)}`}>
                  {index + 1}. {child.title}
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
