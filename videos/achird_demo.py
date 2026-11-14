from pathlib import Path

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    PI,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    FadeIn,
    FadeOut,
    FlashAround,
    Matrix,
    SurroundingRectangle,
    Tex,
    Text,
    TransformFromCopy,
    VGroup,
    Write,
)

from videos.narrated_scene import NarratedScene

SAMPLE_SCRIPT = (
    Path(__file__).resolve().parents[1] / "narration" / "achird-math-sample.txt"
)
FIRST_ROW = (-1, 1, 1, 1)


def circulant_rows(first_row):
    return [first_row[-shift:] + first_row[:-shift] for shift in range(len(first_row))]


class AchirdDemo(NarratedScene):
    def construct(self):
        title = Text("The circulant Hadamard conjecture", font_size=38).to_edge(UP)
        rows = circulant_rows(FIRST_ROW)
        matrix = (
            Matrix(
                [["-1" if value < 0 else "+1" for value in row] for row in rows],
                h_buff=0.5,
                v_buff=0.35,
            )
            .scale(0.9)
            .shift(LEFT * 2.8)
        )
        for entry, value in zip(matrix.get_entries(), sum(rows, ()), strict=True):
            entry.set_color(YELLOW if value < 0 else BLUE_C)
        matrix_label = Tex("H", "=").next_to(matrix, LEFT)
        sign_label = Tex(
            r"\text{entries: } +1 \text{ or } -1", t2c={"+1": BLUE_C, "-1": YELLOW}
        )
        sign_label.scale(0.8).next_to(matrix, DOWN, buff=0.5)

        row_highlights = VGroup(
            SurroundingRectangle(matrix.get_rows()[0], color=YELLOW, buff=0.12),
            SurroundingRectangle(matrix.get_rows()[1], color=YELLOW, buff=0.12),
        )
        dot_product = Tex(r"(-1)(1)+(1)(-1)+(1)(1)+(1)(1)", "=0")
        dot_product.scale(0.54).move_to(RIGHT * 3.1 + UP * 0.6)
        dot_label = Text("Different rows are orthogonal", font_size=22)
        dot_label.next_to(dot_product, UP, buff=0.35)
        shift_label = Text("Each row is the next cyclic shift", font_size=23)
        shift_label.move_to(RIGHT * 3.1 + UP * 0.6)
        identity = Tex(r"H H^{\mathsf{T}} = 4 I_4", t2c={"H": BLUE_C})
        identity.move_to(RIGHT * 3.1 + DOWN * 0.4)
        example_label = Text("An example of order four", font_size=22, color=WHITE)
        example_label.next_to(identity, DOWN, buff=0.35)
        correlation_label = Text("One row. All cyclic correlations.", font_size=27)
        correlation_label.to_edge(DOWN, buff=0.55)

        with self.narrate(SAMPLE_SCRIPT.read_text()):
            self.play(FadeIn(title), run_time=1.2)
            self.wait(1.8)
            self.play(FadeIn(matrix), Write(matrix_label), run_time=2.5)
            self.play(Write(sign_label), run_time=1.2)
            self.play(
                FadeIn(row_highlights),
                FadeIn(dot_label),
                Write(dot_product),
                run_time=1.8,
            )
            self.wait(2)
            self.play(
                FadeOut(VGroup(row_highlights, dot_label, dot_product)), run_time=0.5
            )
            self.play(FadeIn(shift_label), run_time=0.5)
            for index in range(1, 4):
                previous = matrix.get_rows()[index - 1].copy().set_color(YELLOW)
                target = matrix.get_rows()[index].copy().set_color(YELLOW)
                self.play(
                    *(
                        TransformFromCopy(
                            previous[column],
                            target[(column + 1) % 4],
                            path_arc=-PI / 2 if column == 3 else 0,
                        )
                        for column in range(4)
                    ),
                    run_time=0.75,
                )
                self.remove(target)
            self.play(FlashAround(matrix.get_rows()[0], color=YELLOW), run_time=1.25)
            self.play(Write(identity), FadeIn(example_label), run_time=3)
            self.play(FadeIn(correlation_label), run_time=2)
