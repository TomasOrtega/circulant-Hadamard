import json
import subprocess
import sys
import unittest
import xml.etree.ElementTree as ET
from html import unescape
from pathlib import Path
from unittest.mock import Mock, patch

from narration.speech import AudioClip, Narrator
from videos.captions import spoken_paragraphs
from videos.test_captions import parse_vtt

with patch.object(sys, "argv", ["manimgl"]):
    from manimlib import BLUE_C, YELLOW, Tex

    from videos.cyclic_group_ring import CyclicGroupRing
    from videos.node_scene import formula, words
    from videos.overview import Overview

ROOT = Path(__file__).resolve().parents[1]


class NodeVideoTests(unittest.TestCase):
    def test_published_videos_leave_the_subtitle_band_empty(self):
        for path in sorted((ROOT / "videos/production").glob("*.json")):
            video = ROOT / "website/media" / f"{path.stem}.mp4"
            if not video.exists():
                continue
            with self.subTest(node=path.stem):
                result = subprocess.run(
                    [
                        "ffmpeg",
                        "-v",
                        "error",
                        "-i",
                        str(video),
                        "-vf",
                        "fps=1,crop=iw:ih*0.2:0:ih*0.8,scale=320:36",
                        "-f",
                        "rawvideo",
                        "-pix_fmt",
                        "gray",
                        "pipe:1",
                    ],
                    capture_output=True,
                    check=True,
                )
                self.assertTrue(result.stdout)
                self.assertLess(
                    max(result.stdout), 8, "Content enters the subtitle band"
                )

    def test_cycle_circle_and_marker_use_the_math_palette(self):
        _, circle, _, marker = CyclicGroupRing.circle(None)
        self.assertEqual(circle.get_color(), BLUE_C)
        self.assertEqual(marker.get_color(), YELLOW)

    def test_visible_formula_and_prose_paths_use_the_requested_colors(self):
        for obj, color in [
            (formula("h", color=BLUE_C), BLUE_C),
            (words("focus", color=YELLOW), YELLOW),
        ]:
            with self.subTest(kind=type(obj).__name__):
                visible = [m for m in obj.get_family() if m.has_points()]
                self.assertTrue(visible)
                self.assertEqual({m.get_color() for m in visible}, {color})

    def test_temporary_shift_rows_do_not_survive_into_the_conclusion(self):
        scene = Overview(skip_animations=True)
        scene.setup()
        scene.narrator = Mock()
        scene.narrator.audio.return_value = AudioClip(Path("unused.wav"), 215)
        scene.add_sound = Mock()
        scene.construct()
        final_objects = scene.body.get_family()
        leftovers = [
            obj
            for obj in scene.mobjects
            if isinstance(obj, Tex) and obj not in final_objects
        ]
        self.assertEqual(leftovers, [])
        scene.narrator.audio.assert_called_once()

    def test_published_videos_cover_their_narration_and_cues(self):
        for path in sorted((ROOT / "videos/production").glob("*.json")):
            with self.subTest(node=path.stem):
                video = ROOT / "website/media" / f"{path.stem}.mp4"
                if not video.exists():
                    continue
                data = json.loads(path.read_text())
                script = (ROOT / "videos/scripts" / f"{path.stem}.ssml").read_text()
                Narrator(ssml=True).validate_text(script)
                paragraphs = list(ET.fromstring(script))
                self.assertEqual(len(paragraphs), len(data["cues"]))
                cues = list(data["cues"].values())
                self.assertEqual(cues, sorted(cues))
                self.assertGreater(data["narration_duration"], cues[-1])
                captions = (
                    (ROOT / "website/media" / f"{path.stem}.vtt")
                    .read_text()
                    .splitlines()
                )
                caption_text = " ".join(
                    line
                    for line in captions
                    if line and line != "WEBVTT" and " --> " not in line
                )
                spoken_text = " ".join(spoken_paragraphs(script))
                self.assertEqual(unescape(caption_text), spoken_text)
                previous_end = 0
                for start, end, lines in parse_vtt("\n".join(captions)):
                    self.assertGreaterEqual(start, previous_end)
                    self.assertGreaterEqual(end - start, 0.999)
                    self.assertLessEqual(len(lines), 2)
                    self.assertTrue(all(len(line) <= 42 for line in lines))
                    previous_end = end
                result = subprocess.run(
                    [
                        "ffprobe",
                        "-v",
                        "error",
                        "-show_streams",
                        "-of",
                        "json",
                        str(video),
                    ],
                    capture_output=True,
                    text=True,
                    check=True,
                )
                streams = json.loads(result.stdout)["streams"]
                audio = next(s for s in streams if s["codec_type"] == "audio")
                picture = next(s for s in streams if s["codec_type"] == "video")
                self.assertEqual((picture["width"], picture["height"]), (1920, 1080))
                self.assertEqual(picture["avg_frame_rate"], "30/1")
                self.assertGreaterEqual(
                    float(audio["duration"]), data["narration_duration"] - 0.03
                )
                self.assertGreaterEqual(
                    float(picture["duration"]), data["narration_duration"] - 0.03
                )


if __name__ == "__main__":
    unittest.main()
