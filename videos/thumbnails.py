"""Extract the reviewed poster frames without changing the source videos."""

import argparse
import hashlib
import json
from pathlib import Path

import av

ROOT = Path(__file__).resolve().parents[1]
SELECTIONS = ROOT / "videos" / "thumbnail-selections.json"
OUTPUT = ROOT / "website" / "media" / "thumbnails"


def extract_frame(source, seconds, width=1280):
    with av.open(str(source)) as video:
        stream = video.streams.video[0]
        duration = float(stream.duration * stream.time_base)
        if not 0 <= seconds < duration:
            raise ValueError(f"Frame time outside {source.name}: {seconds}")
        video.seek(int(seconds / stream.time_base), stream=stream)
        for frame in video.decode(stream):
            if frame.time is not None and float(frame.time) >= seconds:
                height = round(frame.height * width / frame.width)
                return frame.reformat(width=width, height=height).to_image()
    raise ValueError(f"No frame at {seconds} in {source.name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("nodes", nargs="*", help="Node IDs; default: every selection")
    args = parser.parse_args()
    selections = json.loads(SELECTIONS.read_text())
    selected = args.nodes or sorted(selections["videos"])
    unknown = set(selected) - selections["videos"].keys()
    if unknown:
        parser.error(f"Unknown nodes: {', '.join(sorted(unknown))}")
    jobs = [
        (node_id, selections["videos"][node_id], OUTPUT / f"{node_id}.jpg")
        for node_id in selected
    ]
    jobs.extend(
        (choice["parent"], choice, OUTPUT / "excerpts" / f"{node_id}.jpg")
        for node_id, choice in selections["excerpts"].items()
        if choice["parent"] in selected
    )
    digests = {}
    for node_id, choice, destination in jobs:
        source = ROOT / "website" / "media" / f"{node_id}.mp4"
        if (
            "start" in choice
            and not choice["start"] <= choice["seconds"] < choice["end"]
        ):
            raise ValueError(f"Thumbnail falls outside its excerpt: {destination.name}")
        if node_id not in digests:
            digests[node_id] = hashlib.sha256(source.read_bytes()).hexdigest()
        if digests[node_id] != choice["video_sha256"]:
            raise ValueError(f"Video changed; review the thumbnail for {node_id}")
        image = extract_frame(source, choice["seconds"])
        destination.parent.mkdir(parents=True, exist_ok=True)
        image.save(destination, quality=90, optimize=True)
        print(f"{destination.relative_to(OUTPUT)}: {choice['seconds']:g}s")


if __name__ == "__main__":
    main()
