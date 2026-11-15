# Circulant Hadamard

[SAIR Mathathon, problem 76](https://competition.sair.foundation/competitions/mathathon/problems/76?q=hada).

Steven Creech (Rutgers University) and Tomas Ortega (Princeton University).

- [tex/](tex/): report, slides, and shared bibliography.
- [rules/](rules/): participant and judge rules, taken from the competition website.
- [website/](website/): project website.
- [videos/](videos/README.md): narrated ManimGL scenes with Google Achird.
- [GLOSSARY.md](GLOSSARY.md): the proof exposition's shared vocabulary.
- [decision_log/](decision_log/): timestamped decisions and evidence for the report.

<details>
<summary>Installation and local build</summary>

To build locally, install uv, Bun 1.4.4, and a TeX system with `bibtex`, `chktex`,
`latexmk`, `latexpand`, and Beamer, and run:

```sh
uv sync --locked
uv run prek install
uv run prek -a --quiet
make -C tex check
make -C tex
make -C website check
make -C website
```

Build files are in `tex/build/` and `website/dist/`.

</details>

We submitted `report.tex`, `report.pdf`, and `slides.pdf`.
