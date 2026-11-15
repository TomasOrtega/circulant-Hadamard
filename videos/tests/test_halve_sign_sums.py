import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from narration.speech import AudioClip

with patch.object(sys, "argv", ["manimgl"]):
    from manimlib import SurroundingRectangle, Tex, VGroup

    from videos.halve_sign_sums import HalveSignSums


class HighlightsCaptured(Exception):
    pass


class IntegerHalvesReached(Exception):
    pass


class HalveSignSumsLayoutTests(unittest.TestCase):
    def test_selected_coefficients_clear_neighboring_terms(self):
        scene = HalveSignSums(skip_animations=True)
        scene.setup()
        scene.narrator = Mock()
        scene.narrator.audio.return_value = AudioClip(Path("unused.wav"), 128)
        scene.add_sound = Mock()
        rows, highlights = [], []
        original_show = scene.show

        def capture_layout(*objects, **kwargs):
            for obj in objects:
                for member in obj.get_family():
                    if (
                        isinstance(member, VGroup)
                        and len(member) == 4
                        and all(isinstance(part, Tex) for part in member)
                        and member[0].tex_string.startswith("H_")
                    ):
                        rows.append(member)
                    if isinstance(member, SurroundingRectangle):
                        highlights.append(member)
            if len(highlights) == 4:
                raise HighlightsCaptured
            return original_show(*objects, **kwargs)

        with patch.object(scene, "show", side_effect=capture_layout):
            with self.assertRaises(HighlightsCaptured):
                scene.construct()

        self.assertEqual(len(rows), 4)
        for index, (row, highlight) in enumerate(zip(rows, highlights, strict=True)):
            for side, gap in [
                ("prefix", highlight.get_left()[0] - row[0].get_right()[0]),
                ("suffix", row[-1].get_left()[0] - highlight.get_right()[0]),
            ]:
                with self.subTest(row=index, neighbor=side):
                    self.assertGreaterEqual(
                        gap,
                        0.1,
                        f"The selected-coefficient highlight overlaps its {side}",
                    )

    def test_pair_frames_clear_when_the_residue_sum_becomes_zero(self):
        scene = HalveSignSums(skip_animations=True)
        scene.setup()
        scene.narrator = Mock()
        scene.narrator.audio.return_value = AudioClip(Path("unused.wav"), 128)
        scene.add_sound = Mock()
        original_at = scene.at

        def capture_integer_halves(key):
            if key == "integer_halves":
                raise IntegerHalvesReached
            return original_at(key)

        with patch.object(scene, "at", side_effect=capture_integer_halves):
            with self.assertRaises(IntegerHalvesReached):
                scene.construct()

        self.assertFalse(
            any(
                isinstance(member, SurroundingRectangle)
                for member in scene.body.get_family()
            ),
            "The old pair frames cross the collapsed residue zero",
        )


if __name__ == "__main__":
    unittest.main()
