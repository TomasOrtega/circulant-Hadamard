import json
from pathlib import Path

from manimlib import (
    BLUE_C,
    DOWN,
    GREY_B,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    Matrix,
    Tex,
    Text,
    VGroup,
)

from videos.narrated_scene import NarratedScene

ROOT = Path(__file__).resolve().parents[1]


def formula(source, size=48, color=WHITE, width=12):
    result = Tex(source, font_size=size, color=color)
    if result.get_width() > width:
        result.set_width(width)
    return result


def words(source, size=28, color=WHITE, width=12):
    result = Text(source, font_size=size, color=color)
    if result.get_width() > width:
        result.set_width(width)
    return result


def sign_matrix(first_row=(-1, 1, 1, 1), size=0.8):
    rows = [first_row[-r:] + first_row[:-r] for r in range(len(first_row))]
    matrix = Matrix(rows, h_buff=0.65, v_buff=0.45).scale(size)
    for entry, value in zip(matrix.get_entries(), sum(rows, ()), strict=True):
        entry.set_color(BLUE_C if value > 0 else WHITE)
    return matrix


class NodeScene(NarratedScene):
    node_id = ""
    title = ""
    narration_ssml = True

    def construct(self):
        production = json.loads(
            (ROOT / "videos" / "production" / f"{self.node_id}.json").read_text()
        )
        self.cues = production["cues"]
        self.body = VGroup()
        self.heading = words(self.title, size=35).to_edge(UP, buff=0.28)
        self.subtitle = words("", size=25, color=BLUE_C)
        footer = words(
            "Circulant Hadamard · proof exposition draft", size=16, color=GREY_B
        ).to_edge(DOWN, buff=0.16)
        full_script = (ROOT / "videos" / "scripts" / f"{self.node_id}.ssml").read_text()
        with self.narrate(full_script):
            self.add(self.heading, footer)
            self.present()

    def section(self, cue, title):
        self.wait_until_narration(self.cues[cue])
        if len(self.body):
            self.play(FadeOut(self.body), run_time=0.4)
        self.remove(self.subtitle)
        self.body = VGroup()
        self.subtitle = words(title, size=25, color=BLUE_C)
        self.subtitle.next_to(self.heading, DOWN, buff=0.25)
        self.play(FadeIn(self.subtitle), run_time=0.35)

    def show(self, *objects, run_time=0.7):
        self.body.add(*objects)
        self.play(*(FadeIn(obj) for obj in objects), run_time=run_time)

    def stack(self, *objects, buff=0.6):
        return VGroup(*objects).arrange(DOWN, buff=buff).move_to(DOWN * 0.25)

    def focus(self, obj):
        self.play(obj.animate.set_color(YELLOW), run_time=0.5)
