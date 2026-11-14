# Recursive lessons

Build and check with `make -C website check all` from the repository root.
Serve `website/dist/` with a static HTTP server to preview the lesson pages.
React generates the HTML at build time; chapter navigation requires no client
JavaScript or server-side routing.

## Content

Edit [lessons.js](lessons.js). Each lesson has a stable `id`, `title`,
`shortTitle`, `summary`, `paragraphs`, `video`, `clip`, and a `chapters` array.
Children have the same structure as their parents, so the layout works at any
depth. The build generates a page for each node, its breadcrumbs, and a direct
parent button. Deeper links sit to the right of the chapter text and clip on
desktop and below them on smaller screens.

Mark an undergraduate prerequisite with `foundation: true` and leave its
`chapters` empty. The build rejects further expansion of a foundation node.
Use `draft: true` for unfinished proof sections; examples and necessary
conditions must not be presented as a completed proof.

The initial content is a draft outline approved by the user. It includes
background from the report and a directly checked order-four example. The proof
argument and all videos await the team's material.

## Videos

Leave `video` or `clip` as `null` for a labeled empty slot. `video` is the
overview on the lesson's own page; `clip` is its short preview on its parent's
page. Configure them independently.

- YouTube: `{ youtubeId: "YOUR_VIDEO_ID" }`, with an 11-character ID.
- Hosted file: `{ src: "https://example.com/lesson.mp4" }`.
- Local file: `{ src: "media/lesson.mp4", captions: "media/lesson.vtt" }`.

Place local video and caption files in `website/media/`; the build copies that
directory. Paths are relative to the website root and work at every depth.
Native players use controls without autoplay, and YouTube embeds use its
privacy-enhanced domain. Empty slots contain no active playback control.

The shared layout is in [lesson.jsx](lesson.jsx), with styles from the pinned
[3Blue1Brown source](vendor/README.md) and its lesson layout/button conventions.
