import json
import shutil
import subprocess
import sys
import unittest
from array import array
from pathlib import Path
from unittest.mock import patch

from narration.demo import DEMO_TEXT, DEMO_VOICE
from narration.speech import Narrator

# ManimGL parses command-line arguments during import.
with patch.object(sys, "argv", ["manimgl"]):
    from videos.achird_demo import DEMO_CUES

ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "videos" / "build" / "rendered" / "AchirdDemo.mp4"


@unittest.skipUnless(
    VIDEO.is_file() and shutil.which("ffmpeg"), "Render the demo first"
)
class DemoRenderTests(unittest.TestCase):
    def test_demo_keeps_a_conversational_length(self):
        result = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "json",
                str(VIDEO),
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertLessEqual(float(json.loads(result.stdout)["format"]["duration"]), 35)

    def test_export_contains_the_complete_single_take(self):
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_streams", "-of", "json", str(VIDEO)],
            capture_output=True,
            text=True,
            check=True,
        )
        streams = json.loads(result.stdout)["streams"]
        audio = next(stream for stream in streams if stream["codec_type"] == "audio")
        video = next(stream for stream in streams if stream["codec_type"] == "video")
        clip = Narrator(voice=DEMO_VOICE, ssml=True, offline=True).audio(DEMO_TEXT)
        self.assertGreaterEqual(float(audio["duration"]), clip.duration - 0.02)
        self.assertLessEqual(float(audio["duration"]), clip.duration + 0.05)
        self.assertGreaterEqual(float(video["duration"]), clip.duration - 0.02)

    def test_ssml_break_is_silent_before_the_result(self):
        result = subprocess.run(
            [
                "ffmpeg",
                "-v",
                "error",
                "-ss",
                str(DEMO_CUES["orthogonal"] - 0.6),
                "-i",
                str(VIDEO),
                "-t",
                "0.2",
                "-vn",
                "-f",
                "f32le",
                "-ac",
                "1",
                "pipe:1",
            ],
            capture_output=True,
            check=True,
        )
        samples = array("f", result.stdout)
        self.assertGreater(len(samples), 8000)
        self.assertLess(max(abs(sample) for sample in samples), 0.001)

    def test_title_remains_visible_during_matrix_highlights(self):
        for second in DEMO_CUES.values():
            with self.subTest(second=second):
                result = subprocess.run(
                    [
                        "ffmpeg",
                        "-v",
                        "error",
                        "-ss",
                        str(second),
                        "-i",
                        str(VIDEO),
                        "-vf",
                        "crop=iw:ih*0.14:0:0",
                        "-frames:v",
                        "1",
                        "-f",
                        "rawvideo",
                        "-pix_fmt",
                        "gray",
                        "pipe:1",
                    ],
                    capture_output=True,
                    check=True,
                )
                self.assertGreater(sum(value > 128 for value in result.stdout), 100)

    def test_example_displays_the_full_dot_product(self):
        result = subprocess.run(
            [
                "ffmpeg",
                "-v",
                "error",
                "-ss",
                str(DEMO_CUES["products"] + 1.2),
                "-i",
                str(VIDEO),
                "-vf",
                "crop=iw*0.43:ih*0.1:iw*0.55:ih*0.36",
                "-frames:v",
                "1",
                "-f",
                "rawvideo",
                "-pix_fmt",
                "gray",
                "pipe:1",
            ],
            capture_output=True,
            check=True,
        )
        self.assertGreater(
            sum(value > 128 for value in result.stdout), len(result.stdout) * 0.01
        )


if __name__ == "__main__":
    unittest.main()
