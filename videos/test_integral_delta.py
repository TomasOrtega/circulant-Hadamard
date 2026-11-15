import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from narration.speech import AudioClip

with patch.object(sys, "argv", ["manimgl"]):
    from manimlib import Line, SurroundingRectangle, Tex, VGroup

    from videos.integral_delta import IntegralDelta


class RatioHighlightsCaptured(Exception):
    pass


class IntegralDeltaLayoutTests(unittest.TestCase):
    def test_ratio_highlights_enclose_the_actual_fraction_bars(self):
        scene = IntegralDelta(skip_animations=True)
        scene.setup()
        scene.narrator = Mock()
        scene.narrator.audio.return_value = AudioClip(Path("unused.wav"), 181)
        scene.add_sound = Mock()
        highlights = []
        original_show = scene.show

        def capture_layout(*objects, **kwargs):
            highlights.extend(
                member
                for obj in objects
                for member in obj.get_family()
                if isinstance(member, SurroundingRectangle)
            )
            if len(highlights) == 2:
                raise RatioHighlightsCaptured
            return original_show(*objects, **kwargs)

        with patch.object(scene, "show", side_effect=capture_layout):
            with self.assertRaises(RatioHighlightsCaptured):
                scene.construct()

        bars = sorted(
            (obj for obj in scene.body if isinstance(obj, Line)),
            key=lambda obj: obj.get_center()[0],
        )
        highlights.sort(key=lambda obj: obj.get_center()[0])
        self.assertEqual(len(bars), 2)
        for index, (bar, highlight) in enumerate(zip(bars, highlights, strict=True)):
            for side, gap in [
                ("left", bar.get_left()[0] - highlight.get_left()[0]),
                ("right", highlight.get_right()[0] - bar.get_right()[0]),
            ]:
                with self.subTest(ratio=index, side=side):
                    self.assertGreaterEqual(
                        gap, 0.1, "The fraction bar crosses the ratio highlight"
                    )

        brackets = next(
            obj
            for obj in scene.body
            if isinstance(obj, VGroup)
            and len(obj) == 3
            and isinstance(obj[0], Tex)
            and obj[0].tex_string == r"\bigg("
        )
        for side, gap in [
            (
                "left",
                min(part.get_left()[0] for part in brackets[:2])
                - highlights[1].get_left()[0],
            ),
            (
                "right",
                highlights[1].get_right()[0]
                - max(part.get_right()[0] for part in brackets[:2]),
            ),
        ]:
            with self.subTest(inverse_parentheses=side):
                self.assertGreaterEqual(
                    gap, 0.1, "The inverse parentheses cross the ratio highlight"
                )


if __name__ == "__main__":
    unittest.main()
