import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from narration.speech import AudioClip

with patch.object(sys, "argv", ["manimgl"]):
    from manimlib import SurroundingRectangle, Tex

    from videos.cyclotomic_divisibility import CyclotomicDivisibility


class HighlightCaptured(Exception):
    pass


class CyclotomicDivisibilityLayoutTests(unittest.TestCase):
    def test_coefficient_highlight_is_clear_of_neighboring_math(self):
        scene = CyclotomicDivisibility(skip_animations=True)
        scene.setup()
        scene.narrator = Mock()
        scene.narrator.audio.return_value = AudioClip(Path("unused.wav"), 229)
        scene.add_sound = Mock()
        captured = {}
        targets = {
            r"T(\xi)=\sum_{j=0}^{D-1}": "preceding",
            r"(a_j-a_{j+D})": "coefficient",
            r"\xi^j": "following",
        }
        original_show = scene.show

        def capture_layout(*objects, **kwargs):
            for obj in objects:
                for member in obj.get_family():
                    if isinstance(member, Tex) and member.tex_string in targets:
                        captured[targets[member.tex_string]] = member
                if isinstance(obj, SurroundingRectangle) and len(captured) == 3:
                    captured["highlight"] = obj
                    raise HighlightCaptured
            return original_show(*objects, **kwargs)

        with patch.object(scene, "show", side_effect=capture_layout):
            with self.assertRaises(HighlightCaptured):
                scene.construct()

        highlight = captured["highlight"]
        for name, gap in [
            (
                "preceding sum",
                highlight.get_left()[0] - captured["preceding"].get_right()[0],
            ),
            (
                "following power",
                captured["following"].get_left()[0] - highlight.get_right()[0],
            ),
        ]:
            with self.subTest(neighbor=name):
                self.assertGreaterEqual(
                    gap, 0.1, f"The coefficient highlight overlaps the {name}"
                )


if __name__ == "__main__":
    unittest.main()
