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


class GroupRingEncoding(NodeScene):
    node_id = "group-ring-encoding"
    title = "1 · Group-Ring Encoding"

    def present(self):
        self.section("opening", "One row determines every row")
        matrix = sign_matrix().shift(LEFT * 2.8)
        self.show(matrix)
        first = SurroundingRectangle(matrix.get_rows()[0], color=YELLOW)
        self.show(first)
        self.show(
            formula(r"(-1,1,1,1)", color=BLUE_C).move_to(RIGHT * 2.6),
            words("Keep the original row", size=25).move_to(RIGHT * 2.6 + DOWN),
        )
        for row in matrix.get_rows()[1:]:
            self.play(
                Transform(first, SurroundingRectangle(row, color=YELLOW)), run_time=0.8
            )

        self.section("ring", "1.1 · Encode cyclic positions")
        coefficients = formula(r"(-1,\quad1,\quad1,\quad1)", color=BLUE_C)
        coefficients.move_to(UP * 1.4)
        polynomial = formula(r"h(X)=-1+X+X^2+X^3").move_to(UP * 0.2)
        self.show(coefficients)
        self.show(polynomial)
        self.show(
            formula(r"X^4=1", color=YELLOW).move_to(DOWN * 1),
            formula(r"\mathbb Z[C_n]\cong\mathbb Z[X]/(X^n-1)", size=40).move_to(
                DOWN * 2.3
            ),
        )

        self.section("shifts", "1.2 · Multiplication is a right shift")
        strip = VGroup(*(formula(v, color=BLUE_C) for v in ["-1", "1", "1", "1"]))
        strip.arrange(RIGHT, buff=0.9).move_to(UP * 1.1)
        self.show(strip)
        positions = [item.get_center().copy() for item in strip]
        self.play(
            *(
                Transform(
                    entry,
                    entry.copy().move_to(positions[(i + 1) % 4]),
                    path_arc=-1.5 if i == 3 else 0,
                )
                for i, entry in enumerate(strip)
            ),
            run_time=1.5,
        )
        self.show(
            self.stack(
                formula(r"Xh=-X+X^2+X^3+X^4", size=40),
                formula(r"=1-X+X^2+X^3", size=40, color=YELLOW),
                formula(
                    r"\text{row }j\longleftrightarrow X^{j-1}h,\quad X^nh=h", size=38
                ),
            ).shift(DOWN * 0.8)
        )

        self.section("star", "1.3 · Reverse the circle")
        generic = VGroup(*(formula(v, color=BLUE_C) for v in ["a", "b", "c", "d"]))
        generic.arrange(RIGHT, buff=0.9).move_to(UP * 1.2)
        self.show(generic)
        positions = [item.get_center().copy() for item in generic]
        self.play(
            Transform(
                generic[1], generic[1].copy().move_to(positions[3]), path_arc=1.5
            ),
            Transform(
                generic[3], generic[3].copy().move_to(positions[1]), path_arc=1.5
            ),
            run_time=1.8,
        )
        self.show(
            self.stack(
                formula(r"h^*(X)=h(X^{-1})", color=YELLOW),
                formula(r"h=-1+X+X^2+X^3=h^*", size=40),
                words("This particular row is symmetric.", size=25),
            ).shift(DOWN * 0.8)
        )

        self.section("correlations", "1.4 · One product records every dot product")
        rows = [r"(-1,1,1,1)", r"(1,-1,1,1)", r"(1,1,-1,1)", r"(1,1,1,-1)"]
        equations = (
            VGroup(
                *(
                    formula(
                        r"[X^{"
                        + str(i)
                        + r"}](hh^*)=(-1,1,1,1)\cdot"
                        + row
                        + "="
                        + str(4 if i == 0 else 0),
                        size=33,
                    )
                    for i, row in enumerate(rows)
                )
            )
            .arrange(DOWN, buff=0.65)
            .move_to(DOWN * 0.2)
        )
        for equation in equations:
            self.show(equation)
            self.play(FlashAround(equation, color=YELLOW), run_time=0.6)

        self.section("product", "The example collapses to one equation")
        self.show(
            self.stack(
                formula(r"hh^*=4+0X+0X^2+0X^3", size=48),
                formula(r"\boxed{hh^*=4}", size=76, color=YELLOW),
                words("Equality modulo X⁴ − 1", size=28),
            )
        )

        self.section("dictionary", "1.5 · The general dictionary")
        self.show(
            self.stack(
                formula(r"h_j\in\{-1,1\}\quad(0\le j<n)", color=BLUE_C),
                formula(
                    r"HH^{\mathsf T}=nI_n\quad\Longleftrightarrow\quad hh^*=n",
                    size=47,
                    color=YELLOW,
                ),
                formula(
                    r"\langle\mathrm{row}_r,\mathrm{row}_s\rangle"
                    r"=\sum_k h_kh_{k-(s-r)}=[X^{s-r}](hh^*)",
                    size=36,
                ),
                words("All subscripts and exponents are read modulo n.", size=25),
            )
        )

        self.section("signs", "The sign hypothesis is part of the lemma")
        self.show(
            self.stack(
                formula(r"h(X)=2\quad\Longrightarrow\quad hh^*=4", size=48),
                formula(r"(2,0,0,0)\quad\Longrightarrow\quad H=2I_4", size=46),
                words("Orthogonal rows, but the entries are not signs.", size=27),
                formula(
                    r"h_j=\pm1:\quad HH^{\mathsf T}=nI_n\iff hh^*=n",
                    size=43,
                    color=YELLOW,
                ),
            )
        )
