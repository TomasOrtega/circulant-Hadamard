.PHONY: all clean

BUN ?= bun
FONT_FAMILIES := figtree source-serif-4 sometype-mono
FONT_FILES := $(addsuffix -latin-wght-normal.woff2,$(FONT_FAMILIES))
FONT_LICENSES := $(addsuffix -OFL.txt,$(FONT_FAMILIES))

all: dist/index.html dist/styles.css dist/3b1b-source.md dist/tailwindcss-LICENSE.txt $(addprefix dist/fonts/,$(FONT_FILES) $(FONT_LICENSES))

node_modules/.installed: package.json bun.lock
	$(BUN) install --frozen-lockfile --ignore-scripts
	touch $@

dist/index.html: index.html
	mkdir -p dist
	cp $< $@

dist/styles.css: styles.css vendor/3b1b.css index.html node_modules/.installed
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

clean:
	rm -rf dist
