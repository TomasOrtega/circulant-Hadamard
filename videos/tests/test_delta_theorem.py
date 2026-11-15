import sys
import unittest
from math import hypot
from unittest.mock import patch

with patch.object(sys, "argv", ["manimgl"]):
    from manimlib import ORIGIN, PI

    from videos.delta_theorem import arithmetic_caption, plot, vector


def overlaps(first, second):
    return min(first.get_right()[0], second.get_right()[0]) > max(
        first.get_left()[0], second.get_left()[0]
    ) and min(first.get_top()[1], second.get_top()[1]) > max(
        first.get_bottom()[1], second.get_bottom()[1]
    )


class DeltaLabelTests(unittest.TestCase):
    def test_cardinal_value_labels_stay_outside_the_circle(self):
        for angle, label in [(0, r"\text{reference}"), (PI / 2, r"f(1)=3i")]:
            with self.subTest(label=label):
                _, value = vector(ORIGIN, angle, label)
                nearest_x = min(max(0, value.get_left()[0]), value.get_right()[0])
                nearest_y = min(max(0, value.get_bottom()[1]), value.get_top()[1])
                self.assertGreater(hypot(nearest_x, nearest_y), 1.55)

    def test_arithmetic_caption_clears_the_vertical_conclusion_arrow(self):
        caption = arithmetic_caption()
        crosses_shaft = (
            caption.get_left()[0] <= 0 <= caption.get_right()[0]
            and caption.get_top()[1] > -2.4
            and caption.get_bottom()[1] < -0.625
        )
        self.assertFalse(crosses_shaft)

    def test_value_labels_do_not_overlap_the_axis_labels(self):
        plane = plot(ORIGIN)
        for angle, label, axis in [
            (0, r"\text{reference}", plane[2][0]),
            (PI / 2, r"f(1)=3i", plane[2][1]),
        ]:
            with self.subTest(label=label):
                _, value_label = vector(ORIGIN, angle, label)
                self.assertFalse(overlaps(value_label, axis))


if __name__ == "__main__":
    unittest.main()
