.PHONY: all clean

all: dist/index.html

dist/index.html: index.html
	mkdir -p dist
	cp $< $@

clean:
	rm -rf dist
