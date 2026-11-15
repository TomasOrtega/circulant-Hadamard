import atexit
import os
import re
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

from diskcache import Cache
from manimlib.config import manim_config
from manimlib.mobject.svg import svg_mobject, tex_mobject, text_mobject
from manimlib.utils import cache, tex_file_writing

_ROOT = Path(__file__).resolve().parents[1]
_configured_pid = None
_scratch = None


def full_tex_to_svg(full_tex, compiler="latex", message=""):
    if compiler not in {"latex", "xelatex"}:
        raise NotImplementedError(f"Compiler '{compiler}' is not implemented")
    with TemporaryDirectory(prefix="formula-", dir=_scratch.name) as directory:
        directory = Path(directory)
        source = directory / "working.tex"
        source.write_text(full_tex)
        result = subprocess.run(
            [
                compiler,
                *(["-no-pdf"] if compiler == "xelatex" else []),
                "-interaction=batchmode",
                "-halt-on-error",
                f"-output-directory={directory}",
                str(source),
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode:
            log = source.with_suffix(".log")
            error = re.search(r"(?m)^! .*\n.*", log.read_text() if log.exists() else "")
            raise tex_file_writing.LatexError(
                error.group() if error else result.stderr or "LaTeX compilation failed"
            )
        dvi = source.with_suffix(".dvi" if compiler == "latex" else ".xdv")
        converted = subprocess.run(
            ["dvisvgm", str(dvi), "-n", "-v", "0", "--stdout"],
            capture_output=True,
            text=True,
        )
        if converted.returncode:
            raise tex_file_writing.LatexError(converted.stderr.strip())
        return converted.stdout


def configure_render_cache():
    """Isolate Manim's fixed TeX filenames and bypass the legacy SVG cache."""
    global _configured_pid, _scratch
    pid = os.getpid()
    if _configured_pid == pid:
        return

    directory = _ROOT / "videos" / ".cache" / "render-v3"
    directory.mkdir(parents=True, exist_ok=True)
    _scratch = TemporaryDirectory(prefix=f"tex-{pid}-", dir=directory)
    manim_config.directories.latex_cache = _scratch.name
    manim_config.directories.cache = str(directory / "svg")
    previous_cache = cache._cache
    cache._cache = Cache(manim_config.directories.cache, size_limit=cache.CACHE_SIZE)
    previous_cache.close()
    atexit.register(cache._cache.close)
    tex_file_writing.full_tex_to_svg = cache.cache_on_disk(full_tex_to_svg)

    tex_file_writing.latex_to_svg.cache_clear()
    text_mobject.markup_to_svg.cache_clear()
    tex_mobject.get_tex_mob_scale_factor.cache_clear()
    text_mobject.get_text_mob_scale_factor.cache_clear()
    svg_mobject.SVG_HASH_TO_MOB_MAP.clear()
    _configured_pid = pid
