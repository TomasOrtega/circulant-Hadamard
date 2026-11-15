import sys
from pathlib import Path

from narration.__main__ import main as speech_main
from narration.speech import Voice

DEMO_VOICE = Voice()
DEMO_SCRIPT = Path(__file__).with_name("achird-demo.ssml")
DEMO_TEXT = DEMO_SCRIPT.read_text().strip()
DEMO_RECORDING = Path(__file__).with_name("achird-demo.wav")
DEMO_AUDIO = Path(__file__).with_name("build") / "achird-demo-ssml.wav"


def main():
    return speech_main(
        [
            str(DEMO_SCRIPT),
            "--ssml",
            "--import-audio",
            str(DEMO_RECORDING),
            "--output",
            str(DEMO_AUDIO),
            *sys.argv[1:],
        ]
    )


if __name__ == "__main__":
    raise SystemExit(main())
