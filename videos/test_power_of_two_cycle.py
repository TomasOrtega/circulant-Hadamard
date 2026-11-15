import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from narration.speech import AudioClip

with patch.object(sys, "argv", ["manimgl"]):
    from manimlib import Tex

    from videos.power_of_two_cycle import PowerOfTwoCycle


class LayoutCaptured(Exception):
    pass


class PowerOfTwoCycleLayoutTests(unittest.TestCase):
    def test_coefficient_sum_clears_the_polynomial_sum(self):
        scene = PowerOfTwoCycle(skip_animations=True)
        scene.setup()
        scene.narrator = Mock()
        scene.narrator.audio.return_value = AudioClip(Path("unused.wav"), 157)
        scene.add_sound = Mock()
        captured = {}
        original_show = scene.show

        def capture_layout(*objects, **kwargs):
            for obj in objects:
                if isinstance(obj, Tex):
                    if obj.tex_string.startswith(r"a_r=\sum"):
                        captured["coefficient"] = obj
                    elif obj.tex_string.startswith(r"T(X)=\sum"):
                        captured["polynomial"] = obj
            if len(captured) == 2:
                raise LayoutCaptured
            return original_show(*objects, **kwargs)

        with patch.object(scene, "show", side_effect=capture_layout):
            with self.assertRaises(LayoutCaptured):
                scene.construct()

        coefficient, polynomial = captured["coefficient"], captured["polynomial"]
        self.assertGreaterEqual(
            coefficient.get_bottom()[1] - polynomial.get_top()[1],
            0.15,
            "The two sum limits overlap",
        )


if __name__ == "__main__":
    unittest.main()
