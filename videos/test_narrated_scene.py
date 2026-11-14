import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from narration.speech import AudioClip

# ManimGL parses command-line arguments during import.
with patch.object(sys, "argv", ["manimgl"]):
    from videos.achird_demo import FIRST_ROW, circulant_rows
    from videos.narrated_scene import NarratedScene


class SceneTimeline:
    def __init__(self):
        self.time = 3.0
        self.sounds = []
        self.waits = []
        self.narrator = Mock()
        self.narrator.audio.return_value = AudioClip(Path("voice.wav"), 10)

    def add_sound(self, path):
        self.sounds.append((self.time, path))

    def wait(self, seconds):
        self.waits.append(seconds)
        self.time += seconds


class NarratedSceneTests(unittest.TestCase):
    def test_audio_starts_with_animation_and_scene_waits_for_remaining_narration(self):
        scene = SceneTimeline()
        with NarratedScene.narrate(scene, "The script.") as clip:
            self.assertEqual(clip.duration, 10)
            scene.time += 4
        self.assertEqual(scene.sounds, [(3.0, "voice.wav")])
        self.assertEqual(scene.waits, [6])
        self.assertEqual(scene.time, 13)

    def test_longer_animation_keeps_its_timeline(self):
        scene = SceneTimeline()
        with NarratedScene.narrate(scene, "The script."):
            scene.time += 12
        self.assertEqual(scene.waits, [])
        self.assertEqual(scene.time, 15)

    def test_example_is_circulant_and_satisfies_the_displayed_hadamard_identity(self):
        rows = circulant_rows(FIRST_ROW)
        for previous, following in zip(rows, rows[1:], strict=False):
            self.assertEqual(following, previous[-1:] + previous[:-1])
        for index, row in enumerate(rows):
            for other_index, other in enumerate(rows):
                dot = sum(a * b for a, b in zip(row, other, strict=True))
                self.assertEqual(dot, 4 if index == other_index else 0)


if __name__ == "__main__":
    unittest.main()
