import json
import shutil
import subprocess
import unittest
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "videos" / "build" / "rendered" / "AchirdDemo.mp4"


@unittest.skipUnless(
    VIDEO.is_file() and shutil.which("ffmpeg"), "Render the demo first"
)
class DemoRenderTests(unittest.TestCase):
    def test_export_contains_video_and_the_complete_approved_narration(self):
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_streams", "-of", "json", str(VIDEO)],
            capture_output=True,
            text=True,
            check=True,
        )
        streams = json.loads(result.stdout)["streams"]
        audio = next(stream for stream in streams if stream["codec_type"] == "audio")
        video = next(stream for stream in streams if stream["codec_type"] == "video")
        with wave.open(
            str(ROOT / "narration" / "achird-math-sample.wav"), "rb"
        ) as sample:
            duration = sample.getnframes() / sample.getframerate()
        self.assertGreaterEqual(float(audio["duration"]), duration - 0.02)
        self.assertGreaterEqual(float(video["duration"]), duration - 0.02)

    def test_title_remains_visible_during_matrix_highlights(self):
        for second in (6, 9, 15, 24):
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


if __name__ == "__main__":
    unittest.main()
