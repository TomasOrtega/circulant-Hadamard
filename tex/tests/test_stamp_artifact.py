import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tex import stamp_artifact


class StampArtifactTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.source = "\\newcommand{\\SubmissionCommit}{To be set at submission}\n"
        self.metadata = self.root / "metadata.tex"
        self.metadata.write_text(self.source)
        self.artifact = self.root / "build/report.tex"
        self.artifact.parent.mkdir()
        self.artifact.write_text(self.source)

    def test_only_generated_source_receives_the_full_hash(self):
        commit = "1234567890abcdef" * 2 + "12345678"
        stamp_artifact.stamp(self.artifact, commit)
        self.assertEqual(
            self.artifact.read_text(),
            self.source.replace("To be set at submission", commit),
        )
        self.assertEqual(self.metadata.read_text(), self.source)

    def test_invalid_hash_keeps_the_artifact_unchanged(self):
        for commit in ("", "abc1234", "g" * 40, "a" * 40 + "\\input{secret}"):
            with self.subTest(commit=commit), self.assertRaises(ValueError):
                stamp_artifact.stamp(self.artifact, commit)
            self.assertEqual(self.artifact.read_text(), self.source)

    def test_missing_or_duplicate_definition_is_rejected_without_writing(self):
        for source in ("no definition", self.source * 2):
            self.artifact.write_text(source)
            with self.subTest(source=source), self.assertRaises(ValueError):
                stamp_artifact.stamp(self.artifact, "a" * 40)
            self.assertEqual(self.artifact.read_text(), source)

    def test_cli_stamps_the_generated_report(self):
        script = Path(stamp_artifact.__file__).resolve()
        result = subprocess.run(
            [sys.executable, str(script), "b" * 40],
            cwd=self.root,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("b" * 40, self.artifact.read_text())
        self.assertEqual(self.metadata.read_text(), self.source)


if __name__ == "__main__":
    unittest.main()
