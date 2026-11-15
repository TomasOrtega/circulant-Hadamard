from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    FlashAround,
    SurroundingRectangle,
    Transform,
    VGroup,
)

from videos.node_scene import NodeScene, formula, sign_matrix, words


class CyclicShifts(NodeScene):
    node_id = "cyclic-shifts"
    title = "1.2 · Multiplication is a cyclic shift"

    def present(self):
        self.section("encode", "A polynomial remembers the coefficient row")
        self.show(
            self.stack(
                formula(r"(h_0,h_1,\ldots,h_{n-1})", color=BLUE_C, size=58),
                formula(r"h(X)=h_0+h_1X+\cdots+h_{n-1}X^{n-1}", size=45),
                formula(r"X^n=1", color=YELLOW, size=54),
            )
        )

        self.section("multiply", "The last coefficient wraps to the first position")
        entries = VGroup(*(formula(v, color=BLUE_C) for v in ["a", "b", "c", "d"]))
        entries.arrange(RIGHT, buff=1.1).move_to(UP * 1.3)
        self.show(entries)
        self.show(words("Four-position illustration", size=23).move_to(UP * 2.1))
        positions = [obj.get_center().copy() for obj in entries]
        self.play(
            *(
                Transform(
                    obj,
                    obj.copy().move_to(positions[(i + 1) % 4]),
                    path_arc=-1.8 if i == 3 else 0,
                )
                for i, obj in enumerate(entries)
            ),
            run_time=2,
        )
        self.show(
            self.stack(
                formula(r"Xh=h_0X+h_1X^2+\cdots+h_{n-1}X^n", size=42),
                formula(r"=h_{n-1}+h_0X+\cdots+h_{n-2}X^{n-1}", size=42, color=YELLOW),
            ).shift(DOWN * 0.8)
        )

        self.section("example", "The original example: h, then Xh")
        matrix = sign_matrix().shift(LEFT * 3 + DOWN * 0.2)
        self.show(matrix)
        highlight = SurroundingRectangle(matrix.get_rows()[0]).set_color(YELLOW)
        self.show(highlight)
        self.show(
            formula(r"h=-1+X+X^2+X^3", size=36, width=6).move_to(RIGHT * 2.7 + UP * 0.6)
        )
        self.play(
            Transform(
                highlight, SurroundingRectangle(matrix.get_rows()[1]).set_color(YELLOW)
            ),
            run_time=1,
        )
        self.show(
            formula(r"Xh=1-X+X^2+X^3", size=36, color=BLUE_C, width=6).move_to(
                RIGHT * 2.7 + DOWN * 0.7
            )
        )

        self.section("powers", "Every row is a power of X times h")
        matrix = sign_matrix().shift(LEFT * 2.4 + DOWN * 0.2)
        labels = VGroup(
            *(
                formula(text, color=BLUE_C, size=38).next_to(row, RIGHT, buff=1.2)
                for row, text in zip(
                    matrix.get_rows(), ["h", "Xh", "X^2h", "X^3h"], strict=True
                )
            )
        )
        self.show(matrix)
        for label, row in zip(labels, matrix.get_rows(), strict=True):
            self.show(label, run_time=0.6)
            self.play(FlashAround(row, color=YELLOW), run_time=0.5)
        self.show(
            formula(
                r"\text{row }j\longleftrightarrow X^{j-1}h,\quad X^nh=h",
                size=43,
                color=YELLOW,
            ).move_to(DOWN * 2.4)
        )

        self.section("indexing", "Zero-based row r and column j")
        matrix = sign_matrix().shift(LEFT * 3 + DOWN * 0.2)
        self.show(matrix)
        cell = matrix.get_rows()[2][1]
        first = matrix.get_rows()[0][3]
        self.show(
            SurroundingRectangle(cell).set_color(YELLOW),
            SurroundingRectangle(first).set_color(BLUE_C),
        )
        self.show(
            self.stack(
                formula(r"H_{rj}=h_{(j-r)\bmod n}", size=42, color=YELLOW, width=6),
                formula(r"n=4:\quad r=2,\ j=1", size=33, width=6),
                formula(r"H_{2,1}=h_{-1\bmod4}=h_3=1", size=33, width=6),
            ).move_to(RIGHT * 2.8)
        )
