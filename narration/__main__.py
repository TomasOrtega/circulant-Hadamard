import argparse
import sys
from pathlib import Path

from narration.speech import (
    DEFAULT_CACHE,
    GEMINI_MODELS,
    Narrator,
    Voice,
    atomic_output,
)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate cached Google Achird narration."
    )
    parser.add_argument("script", type=Path, help="UTF-8 text written for speaking")
    parser.add_argument("--output", "-o", type=Path)
    parser.add_argument("--project", help="Google Cloud quota/billing project ID")
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--rate", type=float, default=1.0)
    parser.add_argument("--model", choices=GEMINI_MODELS, help="Opt into Gemini Achird")
    parser.add_argument(
        "--ssml", action="store_true", help="Read the script as Chirp SSML"
    )
    parser.add_argument(
        "--offline", action="store_true", help="Use existing audio only"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Report requests without calling Google"
    )
    parser.add_argument(
        "--import-audio",
        type=Path,
        help="Cache a WAV already generated with these settings",
    )
    args = parser.parse_args(argv)
    try:
        text = args.script.read_text().strip()
        narrator = Narrator(
            voice=Voice(
                name="Achird" if args.model else "en-US-Chirp3-HD-Achird",
                model_name=args.model or "",
                speaking_rate=args.rate,
            ),
            project=args.project,
            cache_dir=args.cache_dir,
            offline=args.offline,
            ssml=args.ssml,
        )
        narrator.validate_text(text)
        if args.output and args.output.resolve() == args.script.resolve():
            raise ValueError("Audio output must differ from the script path.")
        if args.output and args.output.suffix.lower() != ".wav":
            raise ValueError("Audio output must use the .wav extension.")
        if args.dry_run:
            pending = (
                0 if args.import_audio else int(not narrator.cache_path(text).is_file())
            )
            print(
                f"{narrator.voice.name}: {len(text)} characters, "
                f"{pending} uncached request(s)"
            )
            return 0
        clip = (
            narrator.import_audio(text, args.import_audio)
            if args.import_audio
            else narrator.audio(text)
        )
        output = args.output or clip.path
        if output.resolve() != clip.path.resolve():
            with atomic_output(output) as temporary:
                temporary.write_bytes(clip.path.read_bytes())
        print(f"{output} ({clip.duration:.2f} seconds; {narrator.voice.name})")
        return 0
    except (OSError, ValueError, RuntimeError) as error:
        print(f"Narration: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
