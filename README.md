# Circulant Hadamard

[SAIR Mathathon, problem 76](https://competition.sair.foundation/competitions/mathathon/problems/76?q=hada).

Steven Creech (Rutgers University) and Tomas Ortega (Princeton University).

- `tex/`: report, slides, and shared bibliography.
- [tex/assets/](tex/assets/README.md): shared images and diagrams.
- [rules/](rules/README.md): participant and judge rules.
- `website/`: project website.

Install uv and a TeX system with `bibtex`, `chktex`, `latexmk`, `latexpand`, and Beamer.

```sh
uv sync --locked
uv run prek install
uv run prek -a --quiet
make -C tex check
make -C tex
make -C website
```

Build files are in `tex/build/` and `website/dist/`.
We submitted `report.tex`, `report.pdf`, and `slides.pdf`.
