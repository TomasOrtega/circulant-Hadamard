import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from narration.speech import AudioClip

with patch.object(sys, "argv", ["manimgl"]):
    from manimlib import Tex

    from videos.order_is_even import OrderIsEven


class LayoutCaptured(Exception):
    pass


class OrderIsEvenLayoutTests(unittest.TestCase):
    def test_multiplication_sign_is_clear_of_the_second_row_label(self):
        scene = OrderIsEven(skip_animations=True)
        scene.setup()
        scene.narrator = Mock()
        scene.narrator.audio.return_value = AudioClip(Path("unused.wav"), 130)
        scene.add_sound = Mock()
        captured = {}
        original_show = scene.show

        def capture_layout(*objects, **kwargs):
            for obj in objects:
                for member in obj.get_family():
                    if isinstance(member, Tex) and member.tex_string in {
                        r"\mathrm{row}_2",
                        r"\times",
                    }:
                        captured[member.tex_string] = member
            if len(captured) == 2:
                raise LayoutCaptured
            return original_show(*objects, **kwargs)

        with patch.object(scene, "show", side_effect=capture_layout):
            with self.assertRaises(LayoutCaptured):
                scene.construct()

        label = captured[r"\mathrm{row}_2"]
        operator = captured[r"\times"]
        gaps = [
            label.get_left()[0] - operator.get_right()[0],
            operator.get_left()[0] - label.get_right()[0],
            label.get_bottom()[1] - operator.get_top()[1],
            operator.get_bottom()[1] - label.get_top()[1],
        ]
        self.assertGreaterEqual(
            max(gaps), 0.1, "The multiplication sign overlaps the second-row label"
        )


if __name__ == "__main__":
    unittest.main()
