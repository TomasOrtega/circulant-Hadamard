import math
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from narration.speech import AudioClip

with patch.object(sys, "argv", ["manimgl"]):
    from manimlib import Circle, Tex

    from videos.exact_comparison_identities import ExactComparisonIdentities


class DiagramsCaptured(Exception):
    pass


class ExactComparisonLayoutTests(unittest.TestCase):
    def test_value_labels_clear_the_circle_outlines(self):
        scene = ExactComparisonIdentities(skip_animations=True)
        scene.setup()
        scene.narrator = Mock()
        scene.narrator.audio.return_value = AudioClip(Path("unused.wav"), 210)
        scene.add_sound = Mock()
        states = []
        original_show = scene.show

        def capture_diagrams(*objects, **kwargs):
            family = [member for obj in objects for member in obj.get_family()]
            circles = [obj for obj in family if isinstance(obj, Circle)]
            labels = [obj for obj in family if isinstance(obj, Tex)]
            if len(circles) == 2 and len(labels) == 3:
                states.append((circles, labels))
                if len(states) == 2:
                    raise DiagramsCaptured
            return original_show(*objects, **kwargs)

        with patch.object(scene, "show", side_effect=capture_diagrams):
            with self.assertRaises(DiagramsCaptured):
                scene.construct()

        self.assertEqual(len(states), 2)
        for index, (circles, labels) in enumerate(states):
            for label in labels:
                left, right = label.get_left()[0], label.get_right()[0]
                bottom, top = label.get_bottom()[1], label.get_top()[1]
                for circle in circles:
                    x, y = circle.get_center()[:2]
                    nearest_x = min(right, max(left, x))
                    nearest_y = min(top, max(bottom, y))
                    nearest = math.hypot(nearest_x - x, nearest_y - y)
                    farthest = max(
                        math.hypot(px - x, py - y)
                        for px in [left, right]
                        for py in [bottom, top]
                    )
                    radius = circle.get_width() / 2
                    with self.subTest(diagram=index, label=label.tex_string):
                        self.assertTrue(
                            nearest >= radius + 0.04 or farthest <= radius - 0.04,
                            "A circle outline intersects a value label",
                        )


if __name__ == "__main__":
    unittest.main()
