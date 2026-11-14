import { assetRoot, chapterAnchor, hrefFor } from "./lesson-tree.js";

const buttonBase =
  "inline-flex max-w-full items-center justify-center gap-2 rounded-md font-sans text-balance no-underline min-h-12 min-w-12 p-3 text-lg";

function LessonButton({
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

function Media({ video, title, clip = false, base }) {
  const label = clip ? "Chapter clip" : "Overview video";
  const frameClass = "aspect-video w-full rounded-md bg-black";
  if (video?.youtubeId) {
    if (!/^[A-Za-z0-9_-]{11}$/.test(video.youtubeId)) {
      throw new Error(`Invalid YouTube ID for ${title}`);
    }
    return (
      <iframe
        className={frameClass}
        src={`https://www.youtube-nocookie.com/embed/${video.youtubeId}`}
        title={`${label}: ${title}`}
        loading="lazy"
        allow="fullscreen; picture-in-picture"
        allowFullScreen
      />
    );
  }
  if (video?.src) {
    const source = /^https?:\/\//.test(video.src)
      ? video.src
      : `${base}${video.src}`;
    return (
      <video
        className={frameClass}
        controls
        preload="none"
        playsInline
        aria-label={`${label}: ${title}`}
      >
        <source src={source} />
        {video.captions && (
          <track
            kind="captions"
            src={`${base}${video.captions}`}
            srcLang="en"
            label="English"
            default
          />
        )}
        Your browser cannot play this video. <a href={source}>Open the video</a>
        .
      </video>
    );
  }
  return (
    <figure className="flex w-full flex-col gap-3">
      <div
        className={`${frameClass} flex flex-col items-center justify-center gap-4 p-8 text-center font-sans text-white`}
      >
        <span className="text-lg">{label}</span>
        <span className="text-sm text-gray">Video not added yet</span>
      </div>
      <figcaption className="text-center font-sans text-sm text-dark-gray">
        {title}
      </figcaption>
    </figure>
  );
}

function ParentButton({ entry }) {
  const parent = entry.ancestors.at(-1);
  if (!parent) return null;
  return (
    <LessonButton
      href={`${hrefFor(parent, entry)}#${chapterAnchor(entry.lesson)}`}
      aria-label={`Back to higher-level view: ${parent.lesson.title}`}
    >
      <span aria-hidden="true">←</span> Back to {parent.lesson.shortTitle}
    </LessonButton>
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
          <a href={hrefFor(ancestor, entry)}>{ancestor.lesson.shortTitle}</a>
          <span aria-hidden="true">/</span>
        </span>
      ))}
      <span aria-current="page">{entry.lesson.shortTitle}</span>
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

function Chapter({ child, entry, entries }) {
  const target = entries.find((candidate) => candidate.lesson === child);
  const count = child.chapters?.length ?? 0;
  return (
    <section id={chapterAnchor(child)} className="width-lg">
      <Heading>
        {target.numbers.join(".")}. {child.title}
      </Heading>
      <div className="grid grid-cols-[minmax(0,1fr)_14rem] items-start gap-12 max-md:grid-cols-1 max-md:gap-8">
        <div className="flex min-w-0 flex-col gap-8">
          <p>{child.summary}</p>
          <div className="w-full max-w-125 self-center">
            <Media
              video={child.clip}
              title={child.title}
              clip
              base={assetRoot(entry)}
            />
          </div>
        </div>
        <aside className="flex flex-col items-start gap-4 max-md:items-center">
          <LessonButton
            href={hrefFor(target, entry)}
            primary
            aria-label={`Dig in deeper: ${child.title}`}
          >
            Dig in deeper <span aria-hidden="true">→</span>
          </LessonButton>
          <p className="font-sans text-sm text-dark-gray">
            {child.foundation
              ? "Undergraduate foundation"
              : count
                ? `${count} subchapters`
                : "Draft proof section"}
          </p>
        </aside>
      </div>
    </section>
  );
}

export function LessonPage({ entry, entries }) {
  const { lesson } = entry;
  const root = entries[0];
  const chapters = lesson.chapters ?? [];
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
        <LessonButton href={hrefFor(root, entry)}>
          <span className="font-serif text-2xl">Circulant Hadamard</span>
        </LessonButton>
        <nav aria-label="Project links" className="flex flex-wrap gap-2">
          <LessonButton href="https://competition.sair.foundation/competitions/mathathon/problems/76">
            Problem 76
          </LessonButton>
          <LessonButton href="https://github.com/TomasOrtega/circulant-Hadamard">
            Repository
          </LessonButton>
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
                ? `Chapter ${entry.numbers.join(".")}`
                : "A lesson, one layer at a time"}
            </p>
            <h1>{lesson.title}</h1>
            <span className="text-sm text-dark-gray">
              {lesson.foundation
                ? "Undergraduate foundation"
                : lesson.draft
                  ? "Draft proof section"
                  : "Draft lesson"}
            </span>
          </hgroup>
          <div className="w-full max-w-200">
            <Media video={lesson.video} title={lesson.title} base={base} />
          </div>
          <p className="max-w-175 text-center text-lg">{lesson.summary}</p>
        </section>
        <section>
          <div className="flex flex-col gap-8">
            {lesson.paragraphs.map((paragraph) => (
              <p key={paragraph}>{paragraph}</p>
            ))}
            {lesson.equation && (
              <p role="math" className="text-center text-2xl">
                {lesson.equation}
              </p>
            )}
            {lesson.exampleRow && <Matrix row={lesson.exampleRow} />}
          </div>
          {!!chapters.length && (
            <nav
              aria-label="Chapters in this lesson"
              className="flex flex-col items-start gap-4 font-sans"
            >
              {chapters.map((chapter, index) => (
                <a key={chapter.id} href={`#${chapterAnchor(chapter)}`}>
                  {index + 1}. {chapter.title}
                </a>
              ))}
            </nav>
          )}
        </section>
        {chapters.map((chapter) => (
          <Chapter
            key={chapter.id}
            child={chapter}
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
        <p>A project for the Caltech × SAIR Mathathon.</p>
        <p>
          Steven Creech · Rutgers University
          <br />
          Tomas Ortega · Princeton University
        </p>
      </footer>
    </>
  );
}
