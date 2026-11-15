import argparse
import re
from pathlib import Path


def stamp(path, commit):
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("expected a full 40-character Git commit hash")
    source, count = re.subn(
        r"(\\newcommand\{\\SubmissionCommit\}\{)[^{}]*(\})",
        lambda match: match[1] + commit + match[2],
        path.read_text(),
    )
    if count != 1:
        raise ValueError("expected exactly one SubmissionCommit definition")
    path.write_text(source)


def main():
    parser = argparse.ArgumentParser(description="Stamp the generated CI report.")
    parser.add_argument("commit")
    args = parser.parse_args()
    try:
        stamp(Path("build/report.tex"), args.commit)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
