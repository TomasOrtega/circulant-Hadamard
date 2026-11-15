import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[2]
WORKER = r"""
import hashlib
import importlib
import json
import subprocess
import sys
import time
from pathlib import Path
from sqlite3 import ProgrammingError

directory, mode, name, nonce = sys.argv[1:]
directory = Path(directory)
sys.argv = ["manimgl"]
from diskcache import Cache
from manimlib.config import manim_config
from manimlib.utils import cache, tex_file_writing as tex

cache._cache.close()
cache._cache = Cache(str(directory / "legacy-cache"))
legacy_connection = cache._cache._con
manim_config.directories.latex_cache = str(directory / "shared-tex")
formulas = {
    "norm": r"\(ff^*=9\)",
    "ratio": r"\(\frac{E(\omega)}{c(\omega)}\)",
}
def source(label):
    if label == "invalid":
        return tex.get_full_tex(r"\(R=1,\qquadW=1\)") + f"% {nonce}\n"
    return tex.get_full_tex(formulas[label]) + f"% {nonce}\n"

def digest(svg):
    return hashlib.sha256(svg.encode()).hexdigest()

if mode == "poison":
    wrong = tex.full_tex_to_svg.__wrapped__(source("ratio"))
    args = (source("norm"),)
    key = cache.hash_string(f"full_tex_to_svg{args}{{}}")
    cache._cache.set(key, wrong)

importlib.import_module("videos.narrated_scene")
try:
    legacy_connection.execute("SELECT 1")
    legacy_closed = False
except ProgrammingError:
    legacy_closed = True

if mode == "invalid":
    previous = tex.full_tex_to_svg(source("ratio"))
    try:
        actual = tex.full_tex_to_svg(source("invalid"))
    except tex.LatexError:
        result = {"raised": True}
    else:
        result = {"raised": False, "actual": digest(actual),
                  "previous": digest(previous)}
elif mode == "expected":
    result = {key: digest(tex.full_tex_to_svg(source(key))) for key in formulas}
else:
    if mode == "parallel":
        original_run = subprocess.run
        def wait_for(paths):
            deadline = time.monotonic() + 15
            while not all(path.exists() for path in paths):
                if time.monotonic() > deadline:
                    raise TimeoutError("TeX regression barrier timed out")
                time.sleep(0.01)
        def synchronized_run(command, *args, **kwargs):
            if Path(command[0]).name == "latex":
                (directory / f"ready-{name}").touch()
                wait_for([directory / "ready-norm", directory / "ready-ratio"])
                if name == "ratio":
                    wait_for([directory / "done-norm"])
            return original_run(command, *args, **kwargs)
        subprocess.run = synchronized_run
    result = {name: digest(tex.full_tex_to_svg(source(name)))}
    (directory / f"done-{name}").touch()
result["legacy_connection_closed"] = legacy_closed
(directory / f"{mode}-{name}.json").write_text(json.dumps(result))
"""


class RenderCacheTests(unittest.TestCase):
    _expected = None

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="circulant-tex-race-")
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.nonce = uuid4().hex

    def worker(self, mode, name, nonce):
        return subprocess.Popen(
            [sys.executable, "-c", WORKER, str(self.root), mode, name, nonce],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def finished(self, process, mode, name):
        stdout, stderr = process.communicate(timeout=30)
        self.assertEqual(process.returncode, 0, stdout + stderr)
        return json.loads((self.root / f"{mode}-{name}.json").read_text())

    def expected(self):
        if type(self)._expected is not None:
            return type(self)._expected
        process = self.worker("expected", "both", self.nonce + "-expected")
        result = self.finished(process, "expected", "both")
        result.pop("legacy_connection_closed")
        self.assertNotEqual(result["norm"], result["ratio"])
        type(self)._expected = result
        return result

    def test_concurrent_compilers_return_the_requested_formulas(self):
        expected = self.expected()
        workers = {
            name: self.worker("parallel", name, self.nonce + "-parallel")
            for name in expected
        }
        actual = {}
        for name, process in workers.items():
            result = self.finished(process, "parallel", name)
            result.pop("legacy_connection_closed")
            actual.update(result)
        self.assertEqual(
            actual,
            expected,
            "Concurrent TeX compilation returned another formula's SVG",
        )

    def test_legacy_poisoned_svg_is_not_reused(self):
        expected = self.expected()
        process = self.worker("poison", "norm", self.nonce + "-poison")
        actual = self.finished(process, "poison", "norm")
        self.assertEqual(actual["norm"], expected["norm"])
        self.assertTrue(
            actual["legacy_connection_closed"],
            "Replacing the render cache left its SQLite connection open",
        )

    def test_failed_compiler_does_not_return_the_previous_formula(self):
        process = self.worker("invalid", "norm", self.nonce + "-invalid")
        actual = self.finished(process, "invalid", "norm")
        self.assertTrue(actual["raised"], f"Invalid TeX reused prior SVG: {actual}")


if __name__ == "__main__":
    unittest.main()
