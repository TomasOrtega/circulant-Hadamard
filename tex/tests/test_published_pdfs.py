import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tex import published_pdfs


class PublishedPdfTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for name in (
            "Makefile",
            "published_pdfs.py",
            "report.tex",
            "slides.tex",
            "preamble.tex",
            "metadata.tex",
            "references.bib",
            "assets/diagrams/workflow.tex",
            "assets/images/sair.jpg",
        ):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(name)
        (self.root / "build").mkdir()
        for name in ("report.pdf", "slides.pdf"):
            (self.root / "build" / name).write_bytes(b"%PDF-1.7\n" + name.encode())
        published_pdfs.publish(self.root)

    def test_publishing_copies_both_builds_and_passes_the_check(self):
        for name in ("report.pdf", "slides.pdf"):
            self.assertEqual(
                (self.root / name).read_bytes(),
                (self.root / "build" / name).read_bytes(),
            )
        published_pdfs.check(self.root)

    def test_changes_to_document_shared_and_build_inputs_are_rejected(self):
        for name in (
            "report.tex",
            "slides.tex",
            "preamble.tex",
            "metadata.tex",
            "references.bib",
            "Makefile",
            "published_pdfs.py",
            "assets/diagrams/workflow.tex",
            "assets/images/sair.jpg",
        ):
            with self.subTest(name=name):
                path = self.root / name
                original = path.read_bytes()
                path.write_bytes(original + b"changed")
                with self.assertRaises(ValueError):
                    published_pdfs.check(self.root)
                path.write_bytes(original)
                published_pdfs.check(self.root)

    def test_added_and_removed_inputs_are_rejected(self):
        added = self.root / "assets/images/new.png"
        added.write_bytes(b"new asset")
        with self.assertRaises(ValueError):
            published_pdfs.check(self.root)
        added.unlink()
        (self.root / "preamble.tex").unlink()
        with self.assertRaises(ValueError):
            published_pdfs.check(self.root)

    def test_altered_and_missing_published_pdfs_are_rejected(self):
        for name in ("report.pdf", "slides.pdf"):
            with self.subTest(name=name):
                path = self.root / name
                original = path.read_bytes()
                path.write_bytes(original + b"changed")
                with self.assertRaises(ValueError):
                    published_pdfs.check(self.root)
                path.unlink()
                with self.assertRaises(OSError):
                    published_pdfs.check(self.root)
                path.write_bytes(original)

    def test_missing_and_invalid_records_are_rejected(self):
        record = self.root / "published-pdfs.json"
        record.unlink()
        with self.assertRaises(OSError):
            published_pdfs.check(self.root)
        record.write_text("invalid JSON")
        with self.assertRaises(ValueError):
            published_pdfs.check(self.root)

    def test_failed_publication_keeps_existing_copies_and_record(self):
        names = ("report.pdf", "slides.pdf", "published-pdfs.json")
        original = {name: (self.root / name).read_bytes() for name in names}
        (self.root / "build/report.pdf").write_bytes(b"%PDF-1.7\nnew report")
        (self.root / "build/slides.pdf").write_bytes(b"invalid PDF")
        with self.assertRaises(ValueError):
            published_pdfs.publish(self.root)
        self.assertEqual(
            {name: (self.root / name).read_bytes() for name in names}, original
        )

    def test_cli_failure_explains_how_to_refresh_the_pdfs(self):
        (self.root / "report.tex").write_text("changed source")
        error = io.StringIO()
        with patch.object(published_pdfs, "ROOT", self.root):
            with contextlib.redirect_stderr(error):
                self.assertEqual(published_pdfs.main(["check"]), 1)
        self.assertIn("make -C tex publish", error.getvalue())


if __name__ == "__main__":
    unittest.main()
