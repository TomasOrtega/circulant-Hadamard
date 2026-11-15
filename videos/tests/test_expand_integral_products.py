import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from narration.speech import AudioClip

with patch.object(sys, "argv", ["manimgl"]):
    from manimlib import Tex, Text

    from videos.expand_integral_products import ExpandIntegralProducts


class BoxesCaptured(Exception):
    pass


class ProductExpansionLayoutTests(unittest.TestCase):
    def test_quotient_pipeline_labels_have_padding_and_clear_each_other(self):
        scene = ExpandIntegralProducts(skip_animations=True)
        scene.setup()
        scene.narrator = Mock()
        scene.narrator.audio.return_value = AudioClip(Path("unused.wav"), 204)
        scene.add_sound = Mock()
        boxes = []
        original_box = scene.quotient_box
        original_section = scene.section

        def capture_box(*args, **kwargs):
            box = original_box(*args, **kwargs)
            boxes.append(box)
            return box

        def stop_after_pipeline(*args, **kwargs):
            if len(boxes) == 3:
                raise BoxesCaptured
            return original_section(*args, **kwargs)

        with (
            patch.object(scene, "quotient_box", side_effect=capture_box),
            patch.object(scene, "section", side_effect=stop_after_pipeline),
        ):
            with self.assertRaises(BoxesCaptured):
                scene.construct()

        self.assertEqual(len(boxes), 3)
        for index, (outline, labels) in enumerate(boxes):
            for label in labels:
                with self.subTest(stage=index, label=label):
                    self.assertGreaterEqual(
                        label.get_bottom()[1] - outline.get_bottom()[1], 0.12
                    )
                    self.assertGreaterEqual(
                        outline.get_top()[1] - label.get_top()[1], 0.12
                    )
                    self.assertGreaterEqual(
                        label.get_left()[0] - outline.get_left()[0], 0.12
                    )
                    self.assertGreaterEqual(
                        outline.get_right()[0] - label.get_right()[0], 0.12
                    )
            for upper, lower in zip(labels[:-1], labels[1:], strict=True):
                with self.subTest(stage=index):
                    self.assertGreaterEqual(
                        upper.get_bottom()[1] - lower.get_top()[1], 0.12
                    )
        inside_boxes = {member for box in boxes for member in box.get_family()}
        external_labels = [
            member
            for member in scene.body.get_family()
            if isinstance(member, (Tex, Text)) and member not in inside_boxes
        ]
        self.assertTrue(external_labels)
        for label in external_labels:
            for outline, _ in boxes:
                with self.subTest(external_label=label):
                    self.assertTrue(
                        label.get_top()[1] <= outline.get_bottom()[1] - 0.12
                        or label.get_bottom()[1] >= outline.get_top()[1] + 0.12
                        or label.get_right()[0] <= outline.get_left()[0] - 0.12
                        or label.get_left()[0] >= outline.get_right()[0] + 0.12,
                        "An external label touches a pipeline outline",
                    )


if __name__ == "__main__":
    unittest.main()
