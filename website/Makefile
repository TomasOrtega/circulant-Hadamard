.PHONY: all check clean

BUN ?= bun
FONT_FAMILIES := figtree source-serif-4 sometype-mono
FONT_FILES := $(addsuffix -latin-wght-normal.woff2,$(FONT_FAMILIES))
FONT_LICENSES := $(addsuffix -OFL.txt,$(FONT_FAMILIES))
NODE_SOURCES := $(wildcard nodes/*.md)

all: dist/index.html dist/styles.css dist/math.css dist/page-controls.js dist/video-player.js dist/phase-explorer.js dist/3b1b-source.md dist/tailwindcss-LICENSE.txt dist/mathjax-LICENSE.txt $(addprefix dist/fonts/,$(FONT_FILES) $(FONT_LICENSES))

node_modules/.installed: package.json bun.lock
	$(BUN) install --frozen-lockfile --ignore-scripts
	touch $@

dist/index.html: index.html $(NODE_SOURCES) load-nodes.js markdown.js node-tree.js node.jsx dependencies.js dependency-graph.jsx phase-explorer.jsx phase-model.js node-video.js build-nodes.jsx node_modules/.installed $(wildcard media/* media/thumbnails/* media/thumbnails/excerpts/*)
	$(BUN) run --bun build:nodes

dist/math.css: dist/index.html
	$(BUN) run --bun build:nodes

dist/styles.css: styles.css vendor/3b1b.css index.html node.jsx dependency-graph.jsx phase-explorer.jsx page-controls.js node_modules/.installed
	mkdir -p dist
	$(BUN) run --bun build:css

dist/page-controls.js: page-controls.js node_modules/.installed
	mkdir -p dist
	$(BUN) build page-controls.js --target browser --format iife --outfile $@ --minify

dist/video-player.js: video-player.js node_modules/.installed
	mkdir -p dist
	$(BUN) run --bun build:player

dist/phase-explorer.js: phase-explorer.js phase-model.js node_modules/.installed
	mkdir -p dist
	$(BUN) build phase-explorer.js --target browser --format iife --outfile $@ --minify

dist/3b1b-source.md: vendor/README.md
	mkdir -p dist
	cp $< $@

dist/tailwindcss-LICENSE.txt: node_modules/.installed
	mkdir -p dist
	cp node_modules/tailwindcss/LICENSE $@

dist/mathjax-LICENSE.txt: node_modules/.installed
	mkdir -p dist
	cp node_modules/mathjax-full/LICENSE $@

dist/fonts/%-latin-wght-normal.woff2: node_modules/.installed
	mkdir -p dist/fonts
	cp node_modules/@fontsource-variable/$*/files/$*-latin-wght-normal.woff2 $@

dist/fonts/%-OFL.txt: node_modules/.installed
	mkdir -p dist/fonts
	cp node_modules/@fontsource-variable/$*/LICENSE $@

check: node_modules/.installed
	$(BUN) test

clean:
	rm -rf dist
