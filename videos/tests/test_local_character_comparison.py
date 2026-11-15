import statistics
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from narration.speech import AudioClip

with patch.object(sys, "argv", ["manimgl"]):
    from manimlib import Text

    from videos.local_character_comparison import LocalCharacterComparison


class LabelCaptured(Exception):
    pass


class LocalCharacterComparisonLayoutTests(unittest.TestCase):
    def test_localization_prose_has_no_protruding_glyph(self):
        scene = LocalCharacterComparison(skip_animations=True)
        scene.setup()
        scene.narrator = Mock()
        scene.narrator.audio.return_value = AudioClip(Path("unused.wav"), 280)
        scene.add_sound = Mock()
        captured = []
        current_detail = None
        original_at = scene.at
        original_show = scene.show

        def track_detail(key):
            nonlocal current_detail
            current_detail = key
            return original_at(key)

        def capture_label(*objects, **kwargs):
            if current_detail == "ring_localize":
                captured.extend(obj for obj in objects if isinstance(obj, Text))
                if captured:
                    raise LabelCaptured
            return original_show(*objects, **kwargs)

        with (
            patch.object(scene, "at", side_effect=track_detail),
            patch.object(scene, "show", side_effect=capture_label),
            self.assertRaises(LabelCaptured),
        ):
            scene.construct()

        self.assertEqual(len(captured), 1)
        label = captured[0]
        glyph_heights = [
            glyph.get_height() for glyph in label if glyph.get_height() > 0.01
        ]
        self.assertLessEqual(
            label.get_height(),
            2.5 * statistics.median(glyph_heights),
            "The localization label has a glyph protruding far beyond its text line",
        )


if __name__ == "__main__":
    unittest.main()
