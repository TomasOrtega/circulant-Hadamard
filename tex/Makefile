.PHONY: all report slides publish check check-pdfs clean

all: report slides

report: build/report.pdf

slides: build/slides.pdf

publish: all
	python3 published_pdfs.py publish

check-pdfs:
	python3 published_pdfs.py check

check: build/report.tex
	chktex -q -H1 -I0 $(wildcard *.tex assets/diagrams/*.tex) build/report.tex

SHARED := preamble.tex metadata.tex references.bib $(wildcard assets/diagrams/*.tex assets/images/*)
LATEXMK_FLAGS := -pdf -interaction=nonstopmode -halt-on-error -file-line-error

build/bib/report.bbl: report.tex $(SHARED) | build
	latexmk $(LATEXMK_FLAGS) -outdir=build/bib report.tex

build/report.tex: report.tex $(SHARED) build/bib/report.bbl Makefile | build
	latexpand --fatal --empty-comments --expand-bbl build/bib/report.bbl --output $@ report.tex
	# End BibTeX commands explicitly for ChkTeX.
	perl -pi -e 's/\\newblock\b/\\newblock{}/g' $@

build/report.pdf: build/report.tex $(SHARED)
	latexmk $(LATEXMK_FLAGS) -outdir=build build/report.tex

build/slides.pdf: slides.tex $(SHARED) Makefile | build
	latexmk $(LATEXMK_FLAGS) -outdir=build slides.tex

build:
	mkdir -p build

clean:
	rm -rf build
