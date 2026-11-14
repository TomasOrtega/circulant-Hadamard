.PHONY: all check clean

BUN ?= bun
FONT_FAMILIES := figtree source-serif-4 sometype-mono
FONT_FILES := $(addsuffix -latin-wght-normal.woff2,$(FONT_FAMILIES))
FONT_LICENSES := $(addsuffix -OFL.txt,$(FONT_FAMILIES))

all: dist/index.html dist/styles.css dist/3b1b-source.md dist/tailwindcss-LICENSE.txt $(addprefix dist/fonts/,$(FONT_FILES) $(FONT_LICENSES))

node_modules/.installed: package.json bun.lock
	$(BUN) install --frozen-lockfile --ignore-scripts
	touch $@

dist/index.html: index.html lessons.js lesson-tree.js lesson.jsx build-lessons.jsx node_modules/.installed $(wildcard media/*)
	$(BUN) run --bun build:lessons

dist/styles.css: styles.css vendor/3b1b.css index.html lesson.jsx node_modules/.installed
	mkdir -p dist
	$(BUN) run --bun build:css

dist/3b1b-source.md: vendor/README.md
	mkdir -p dist
	cp $< $@

dist/tailwindcss-LICENSE.txt: node_modules/.installed
	mkdir -p dist
	cp node_modules/tailwindcss/LICENSE $@

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
