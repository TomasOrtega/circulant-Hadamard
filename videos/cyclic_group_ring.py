from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    PI,
    RIGHT,
    TAU,
    UP,
    YELLOW,
    Circle,
    Dot,
    FadeOut,
    Rotate,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import NodeScene, formula, sign_matrix, words


class CyclicGroupRing(NodeScene):
    node_id = "cyclic-group-ring"
    title = "1.1 · What is the group ring?"

    def circle(self):
        center = LEFT * 3 + DOWN * 0.3
        circle = Circle(radius=1.5).set_color(BLUE_C).move_to(center)
        labels = VGroup(
            formula("1").move_to(center + UP * 1.95),
            formula("X").move_to(center + RIGHT * 1.95),
            formula("X^2").move_to(center + DOWN * 1.95),
            formula("X^3").move_to(center + LEFT * 1.95),
        )
        pointer = Dot(center + UP * 1.5, radius=0.11).set_color(YELLOW)
        return center, circle, labels, pointer

    def present(self):
        self.section("cycle", "One matrix, one cyclic row")
        matrix = sign_matrix(size=0.55).move_to(LEFT * 3.4 + UP * 0.2)
        highlight = SurroundingRectangle(matrix.get_rows()[0], buff=0.1)
        highlight.set_color(YELLOW)
        row = VGroup(*(entry.copy() for entry in matrix.get_rows()[0]))
        row.scale(1.45).arrange(RIGHT, buff=0.55).move_to(RIGHT * 2.8)
        description = words("One row determines the matrix", size=26)
        description.move_to(RIGHT * 2.8 + UP * 1.2)
        self.show(matrix, run_time=0.75)
        self.show(highlight, run_time=0.35)
        self.play(
            *(
                TransformFromCopy(source, target)
                for source, target in zip(matrix.get_rows()[0], row, strict=True)
            ),
            run_time=1.2,
        )
        self.body.add(row)
        self.show(description, run_time=0.55)
        self.wait(1.2)
        self.play(
            FadeOut(matrix), FadeOut(highlight), FadeOut(description), run_time=0.45
        )
        self.body.remove(matrix, highlight, description)
        center, circle, labels, pointer = self.circle()
        self.show(circle, labels, run_time=0.65)
        self.play(
            *(
                Transform(entry, entry.copy().move_to(center + direction * 1.1))
                for entry, direction in zip(row, [UP, RIGHT, DOWN, LEFT], strict=True)
            ),
            run_time=1.2,
        )
        self.show(pointer, run_time=0.35)
        self.show(
            words("n = 4 illustration", size=25).move_to(RIGHT * 2.8 + UP * 0.8),
            formula(r"X^4=1", color=YELLOW, size=60).move_to(RIGHT * 2.8 + DOWN * 0.6),
            run_time=0.65,
        )
        for _ in range(4):
            self.play(Rotate(pointer, -PI / 2, about_point=center), run_time=0.7)

        self.section("ring", "The cyclic group")
        self.show(
            self.stack(
                formula(r"C_n=\langle X\mid X^n=1\rangle", color=BLUE_C),
                formula(r"1,\ X,\ X^2,\ldots,\ X^{n-1}", size=55),
                words("X records one step around the cycle.", size=29),
            )
        )

        self.section("integers", "Attach an integer to every position")
        self.show(
            self.stack(
                formula(r"a_0+a_1X+\cdots+a_{n-1}X^{n-1}", size=48),
                formula(r"a_j\in\mathbb Z,\qquad X^n=1", color=BLUE_C),
                formula(
                    r"\mathbb Z[C_n]\cong\mathbb Z[X]/(X^n-1)", size=49, color=YELLOW
                ),
                words("Add normally. Multiply and reduce exponents.", size=27),
            )
        )

        self.section("wrap", "An exponent records position modulo four")
        center, circle, labels, pointer = self.circle()
        self.show(circle, labels, pointer)
        term = formula(r"3X^5", color=YELLOW, size=66).move_to(RIGHT * 2.8 + UP * 0.4)
        self.show(term)
        self.play(Rotate(pointer, -TAU, about_point=center), run_time=1.8)
        self.play(Rotate(pointer, -PI / 2, about_point=center), run_time=0.6)
        self.play(
            Transform(term, formula(r"3X^5=3X", color=YELLOW, size=55).move_to(term)),
            run_time=0.9,
        )
        self.show(formula(r"X^{-1}=X^3", size=45).move_to(RIGHT * 2.8 + DOWN * 1.3))

        self.section("existence", "Existence of a reduced representative")
        self.show(
            self.stack(
                formula(r"X^{qn+r}=(X^n)^qX^r=X^r,\quad 0\le r<n", size=46),
                formula(
                    r"f(X)\equiv a_0+a_1X+\cdots+a_{n-1}X^{n-1}", size=43, color=YELLOW
                ),
                words("Reduce exponents, then collect equal positions.", size=29),
            )
        )

        self.section("unique", "Uniqueness: two reduced expressions must agree")
        self.show(
            self.stack(
                formula(r"\deg f,\deg g<n,\qquad f-g=q(X)(X^n-1)", size=43),
                formula(
                    r"q\ne0\quad\Longrightarrow\quad\deg(f-g)=\deg q+n\ge n",
                    size=40,
                    color=YELLOW,
                ),
                words("A nonzero difference cannot have degree below n.", size=27),
                formula(r"q=0\quad\Longrightarrow\quad f=g", color=BLUE_C),
            )
        )

        self.section("row", "A row and a group ring element contain the same data")
        self.show(
            self.stack(
                formula(r"(a_0,\ldots,a_{n-1})", color=BLUE_C, size=58),
                formula(r"\Updownarrow", color=YELLOW),
                formula(r"a_0+a_1X+\cdots+a_{n-1}X^{n-1}", size=50),
                words("Next: multiplying by X shifts the row.", size=30),
            )
        )
