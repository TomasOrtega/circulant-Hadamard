import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PDF_NAMES = ("report.pdf", "slides.pdf")
RECORD = "published-pdfs.json"


def fingerprints(root, pdfs):
    sources = {root / "Makefile", root / "published_pdfs.py"}
    for pattern in ("*.tex", "*.bib", "assets/diagrams/*.tex", "assets/images/*"):
        sources.update(
            path
            for path in root.glob(pattern)
            if path.is_file() and not path.name.startswith(".")
        )
    return {
        "sources": {
            path.relative_to(root).as_posix(): hashlib.sha256(
                path.read_bytes()
            ).hexdigest()
            for path in sorted(sources)
        },
        "pdfs": {name: hashlib.sha256(data).hexdigest() for name, data in pdfs.items()},
    }


def publish(root):
    pdfs = {name: (root / "build" / name).read_bytes() for name in PDF_NAMES}
    for name, data in pdfs.items():
        if not data.startswith(b"%PDF-"):
            raise ValueError(f"build/{name} is not a PDF")
    record = fingerprints(root, pdfs)
    for name, data in pdfs.items():
        (root / name).write_bytes(data)
    (root / RECORD).write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")


def check(root):
    recorded = json.loads((root / RECORD).read_text())
    pdfs = {name: (root / name).read_bytes() for name in PDF_NAMES}
    if recorded != fingerprints(root, pdfs):
        raise ValueError("source inputs or published PDFs changed")


def main(arguments=None):
    parser = argparse.ArgumentParser(description="Publish or check the linked PDFs.")
    parser.add_argument("action", choices=("publish", "check"))
    args = parser.parse_args(arguments)
    try:
        if args.action == "publish":
            publish(ROOT)
        else:
            check(ROOT)
    except (OSError, ValueError) as error:
        print(
            f"{error}. Run `make -C tex publish` to refresh the PDFs.", file=sys.stderr
        )
        return 1
    print("Published PDFs are up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
