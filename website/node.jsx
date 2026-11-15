import { assetRoot, nodeAnchor, hrefFor, findChildEntry } from "./node-tree.js";
import { DependencyGraph } from "./dependency-graph.jsx";
import { cutVideo, mediaUrl, formatTime } from "./node-video.js";
import { renderMarkdown } from "./markdown.js";
import { PhaseExplorer } from "./phase-explorer.jsx";

const phaseExplorerStages = {
  "odd-order-rigidity": "rotation",
  "exact-comparison-identities": "rotation",
  "products-to-sums": "normalization",
  "vanishing-alternating-sum": "normalization",
};

const buttonBase =
  "inline-flex max-w-full items-center justify-center gap-2 rounded-md font-sans text-balance no-underline min-h-12 min-w-12 p-3 text-lg";

function NodeButton({ href, children, ...props }) {
  return (
    <a href={href} className={`${buttonBase} text-black hocus:bg-theme/15 hocus:text-theme`} {...props}>
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
        poster={video.poster ? mediaUrl(video.poster, base) : undefined}
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
      className="flex flex-wrap items-center gap-2 font-sans text-lg"
    >
      {entry.ancestors.map((ancestor) => (
        <span
          key={ancestor.path.join("/")}
          className="inline-flex items-center gap-2"
        >
          <NodeButton href={hrefFor(ancestor, entry)}>{ancestor.node.shortTitle}</NodeButton>
          <span aria-hidden="true" className="text-dark-gray">/</span>
        </span>
      ))}
      <span aria-current="page" className="p-3">{entry.node.shortTitle}</span>
    </nav>
  );
}

function Markdown({ script }) {
  return (
    <div className="flex min-w-0 flex-col gap-8 overflow-x-auto
      [&_blockquote]:flex [&_blockquote]:min-w-0 [&_blockquote]:flex-col
      [&_blockquote]:gap-4 [&_blockquote]:overflow-x-auto [&_blockquote]:rounded-md
      [&_blockquote]:border [&_blockquote]:border-theme/50 [&_blockquote]:bg-theme/5
      [&_blockquote]:p-6 max-md:[&_blockquote]:p-4"
      dangerouslySetInnerHTML={{ __html: renderMarkdown(script.join("\n\n")).html }} />
  );
}

function TableOfContents() {
  return (
    <>
      <button id="toc-toggle" type="button" popoverTarget="table-of-contents"
        aria-label="Table of contents" hidden
        className="fixed top-0 left-0 z-20 flex size-10 items-center justify-center bg-white text-black shadow-md hocus:text-theme print:hidden">
        <svg viewBox="0 0 24 24" className="size-6" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
          <path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01" strokeLinecap="round" />
        </svg>
      </button>
      <nav id="table-of-contents" popover="auto" aria-label="Table of contents"
        className="fixed inset-y-0 left-0 right-auto m-0 h-dvh w-80 max-w-[75vw] overflow-y-auto border-0 bg-white p-4 font-sans text-black shadow-md print:hidden">
        <div className="sticky top-0 flex items-center justify-between gap-4 bg-white">
          <span className="font-medium">Table of Contents</span>
          <button type="button" popoverTarget="table-of-contents" popoverTargetAction="hide"
            aria-label="Close table of contents" className="flex size-10 shrink-0 items-center justify-center hocus:text-theme">
            <svg viewBox="0 0 24 24" className="size-6" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
              <path d="m6 6 12 12M6 18 18 6" />
            </svg>
          </button>
        </div>
        <div id="toc-links" className="flex flex-col" />
      </nav>
    </>
  );
}

function ChildNode({ child, entry, entries }) {
  const node = child.node;
  const target = findChildEntry(node, entry, entries);
  const count = node.children?.length ?? 0;
  return (
    <section id={nodeAnchor(node)} className="width-lg">
      <header className="flex flex-col gap-4">
        <h2>
          <hr />
          <span>{node.number ? `${node.number}. ` : ""}{node.title}</span>
          <hr />
        </h2>
        <div className="flex items-center justify-end gap-4">
          <NodeButton
            href={hrefFor(target, entry)}
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
        </div>
      </header>
      <Markdown script={child.script} />
      {phaseExplorerStages[node.id] && <PhaseExplorer
        id={`phase-${node.id}`}
        stage={phaseExplorerStages[node.id]}
        nextHref={entries[0].node.children?.some(({ node }) => node.id === "products-to-sums")
          ? `${hrefFor(entries[0], entry)}#node-products-to-sums` : undefined}
      />}
      <div className="w-full max-w-175 self-center">
        <Media
          video={cutVideo(entry.node, child)}
          title={node.title}
          excerpt
          base={assetRoot(entry)}
        />
      </div>
    </section>
  );
}

function NodeDependencies({ entry, entries }) {
  const owner = entry.ancestors.at(-1);
  if (!owner) return null;
  const siblings = owner.node.children;
  const current = siblings.find(({ node }) => node === entry.node);
  if (!current) return null;
  const incoming = current.dependsOn ?? [];
  const context = current.contextFrom ?? [];
  const links = (ids) => ids.map((id, index) => {
    const node = siblings.find(({ node }) => node.id === id).node;
    const target = findChildEntry(node, owner, entries);
    return <span key={id}>{index ? ", " : ""}<a href={hrefFor(target, entry)}>{node.title}</a></span>;
  });
  return (
    <nav aria-label="Prerequisites and notation" className="w-full rounded-md bg-light-gray p-6 font-sans text-sm">
      <p><strong>Uses: </strong>{incoming.length ? links(incoming) : "No earlier proof node."}</p>
      {!!context.length && <p><strong>Shared notation only: </strong>{links(context)}</p>}
    </nav>
  );
}

export function NodePage({ entry, entries }) {
  const { node } = entry;
  const root = entries[0];
  const children = node.children ?? [];
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
      <TableOfContents />
      <main id="content" className="striped">
        <section className="items-center bg-theme/15 width-lg">
          <div className="flex w-full flex-wrap items-center justify-between gap-4">
            <Breadcrumbs entry={entry} />
            <ParentButton entry={entry} />
          </div>
          <hgroup className="flex flex-col items-center gap-4 font-sans">
            <h1>{node.title}</h1>
          </hgroup>
          {!entry.ancestors.length && (
            <p className="text-center font-sans text-lg">Steven Creech and Tomas Ortega</p>
          )}
          <div className="w-full max-w-200">
            <Media video={node.video} title={node.title} base={base} />
          </div>
          <DependencyGraph entry={entry} entries={entries} />
          {showOwnExplanation && hasOwnProofMap && (
            <div className="w-full max-w-200 rounded-md bg-white p-8 text-left max-md:p-6">
              <Markdown script={node.script} />
            </div>
          )}
          {showOwnExplanation && <p className="max-w-175 text-center text-lg">{node.summary}</p>}
        </section>
        {(entry.ancestors.length > 0 || showOwnExplanation && !hasOwnProofMap) && (
          <section>
            <NodeDependencies entry={entry} entries={entries} />
            {showOwnExplanation && !hasOwnProofMap && <Markdown script={node.script} />}
          </section>
        )}
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
            <ParentButton entry={entry} />
          </section>
        )}
      </main>
      <footer className="flex items-center justify-between gap-4 bg-alt-white p-8 text-center font-sans text-sm text-dark-gray">
        <button id="dark-mode-toggle" type="button" role="switch" aria-checked="false"
          aria-label="Toggle dark mode" title="Toggle dark mode" hidden
          className={`${buttonBase} group shrink-0 text-black hocus:bg-theme/15 hocus:text-theme print:hidden`}>
          <svg viewBox="0 0 24 24" className="size-6 group-aria-checked:hidden" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
            <path d="M21 13a9 9 0 1 1-10-10 7 7 0 0 0 10 10Z" />
          </svg>
          <svg viewBox="0 0 24 24" className="hidden size-6 group-aria-checked:block" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
            <circle cx="12" cy="12" r="4" />
            <path d="M12 1v2M12 21v2M1 12h2M21 12h2M4 4l2 2M18 18l2 2M4 20l2-2M18 6l2-2" />
          </svg>
        </button>
        <p className="flex-1">
          A project for the Caltech × SAIR Mathathon, by Steven Creech and Tomas
          Ortega
        </p>
        <span className="size-12 shrink-0 max-md:hidden print:hidden" aria-hidden="true" />
      </footer>
      <aside id="page-controls" aria-label="Page controls" hidden
        className="fixed right-2 bottom-2 z-20 flex flex-col items-end gap-2 text-[white] mix-blend-difference print:hidden">
        {[
          ["jump-to-top", "Jump to top", <path d="m6 15 6-6 6 6" />],
          ["share-page", "Share this page", <>
            <path d="m8 10 8-5M8 14l8 5" />
            <circle cx="6" cy="12" r="3" />
            <circle cx="18" cy="4" r="3" />
            <circle cx="18" cy="20" r="3" />
          </>],
          ["feedback", "Website feedback", <>
            <path d="M21 11a9 9 0 1 0-9 9h9Z" />
            <path d="M8 11h.01M12 11h.01M16 11h.01" strokeLinecap="round" />
          </>, "https://github.com/TomasOrtega/circulant-Hadamard/issues"],
        ].map(([id, label, icon, href]) => {
          const Control = href ? "a" : "button";
          return (
            <div key={id} className="group flex items-center gap-2">
              <span className="pointer-events-none font-sans opacity-0 transition group-hover:opacity-100 group-focus-within:opacity-100">{label}</span>
              <Control id={id} href={href} type={href ? undefined : "button"} aria-label={label}
                className={`${buttonBase} text-current hocus:bg-white/15`}>
                <svg viewBox="0 0 24 24" className="size-6" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
                  {icon}
                </svg>
              </Control>
            </div>
          );
        })}
      </aside>
      <script src={`${base}page-controls.js`} defer />
      {node.video?.src && children.some((child) => child.segment) && (
        <script src={`${base}video-player.js`} defer />
      )}
      {children.some(child => phaseExplorerStages[child.node.id]) && (
        <script src={`${base}phase-explorer.js`} defer />
      )}
    </>
  );
}
