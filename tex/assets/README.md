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

`images/sair.jpg`: [official SAIR logo](https://media.sair.foundation/images/mathathon-logos/sair.jpg), used on the title slide.
