import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from narration.speech import AudioClip

with patch.object(sys, "argv", ["manimgl"]):
    from manimlib import Tex, Text

    from videos.circle_evaluations import CircleEvaluations


class LayoutCaptured(Exception):
    pass


class CircleEvaluationsLayoutTests(unittest.TestCase):
    def test_output_question_clears_the_imaginary_axis_label(self):
        scene = CircleEvaluations(skip_animations=True)
        scene.setup()
        scene.narrator = Mock()
        scene.narrator.audio.return_value = AudioClip(Path("unused.wav"), 165)
        scene.add_sound = Mock()
        captured = {}
        original_show = scene.show

        def capture_layout(*objects, **kwargs):
            for obj in objects:
                for member in obj.get_family():
                    if (
                        isinstance(member, Tex)
                        and member.tex_string == r"\operatorname{Im}"
                        and member.get_center()[0] > 0
                    ):
                        captured["axis"] = member
                    elif (
                        isinstance(member, Text)
                        and member.get_text() == "Where can f(ζ) land?"
                    ):
                        captured["question"] = member
            if len(captured) == 2:
                raise LayoutCaptured
            return original_show(*objects, **kwargs)

        with patch.object(scene, "show", side_effect=capture_layout):
            with self.assertRaises(LayoutCaptured):
                scene.construct()

        axis, question = captured["axis"], captured["question"]
        gaps = [
            axis.get_left()[0] - question.get_right()[0],
            question.get_left()[0] - axis.get_right()[0],
            axis.get_bottom()[1] - question.get_top()[1],
            question.get_bottom()[1] - axis.get_top()[1],
        ]
        self.assertGreaterEqual(
            max(gaps), 0.1, "The output question overlaps the imaginary-axis label"
        )


if __name__ == "__main__":
    unittest.main()
