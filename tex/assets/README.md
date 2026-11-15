# Shared assets

Put PNG, JPG, and PDF images in `images/`. Put TikZ code in `diagrams/`.
Use the same files in the report and slides:

```tex
\includegraphics[width=0.7\linewidth]{figure-name}
\input{assets/diagrams/workflow.tex}
```

Keep package imports and captions in the documents.
The report build copies TikZ code into one `.tex` file.
Add any image files to the submission.

`images/sair.jpg`: [official SAIR logo](https://media.sair.foundation/images/mathathon-logos/sair.jpg), available for project materials.

## Talk figures

The November 15, 2026 talk uses these local assets:

- `images/slides-website-qr.png` encodes
  `https://tomasortega.net/circulant-Hadamard/`. Generated with CoreImage at
  1032 × 1032 pixels, medium error correction, and at least four modules of
  white margin. Apple's separate Vision decoder verified the saved PNG's
  exact URL. Every slide has a clickable QR code in its bottom-right corner;
  the opening and closing slides also show the website URL.
- `images/slides-overview.jpg` is an unchanged copy of the website's overview
  thumbnail. The associated overview video lasts 214.933333 seconds.
- `images/slides-proof-map.png` and `images/slides-delta-map.png` are authentic
  captures of the local site's expanded dependency maps. The native graph
  disclosure was opened; page content and styles were not altered.
- `images/slides-node-detail.png` captures the heading, deeper-node button,
  boxed lemma, and opening equation of Node 4.1, “Evaluations on a Circle.”
  Screenshots use a 1280 CSS-pixel Chromium viewport at double pixel density.
- `diagrams/slides-main-map.tex` redraws the same eight nodes and ten proof
  dependency arrows in a wide arrangement for projection. The context-only
  link into Node 4 is not a proof dependency and is omitted.
- `diagrams/report-delta-detail.tex` and `diagrams/report-common-rotation.tex`
  are shared with the report. The latter is a schematic illustration of
  common rotation and normalization, not a valid Hadamard sign construction.

The slides contain additional native TikZ circles for the proof overview.
They retain searchable mathematical labels. The tall original map captures
are in the backup slides; the main talk uses the wider vector arrangement.
