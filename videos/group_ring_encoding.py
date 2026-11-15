from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    Line,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
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
        self.body.add(polynomial)
        self.play(TransformFromCopy(coefficients, polynomial), run_time=1.6)
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
        self.show(
            formula(r"\text{entry }(a,j)=h_jh_{j-a}", size=37).move_to(UP * 2.1),
            words("Indices wrap modulo 4", size=24).move_to(RIGHT * 4.8 + UP * 2.1),
        )
        columns = [-4.55, -2.85, -1.15, 0.55]
        row_heights = [0.375, -0.475, -1.325, -2.175]
        entries = [
            [1, 1, 1, 1],
            [-1, -1, 1, 1],
            [-1, 1, -1, 1],
            [-1, 1, 1, -1],
        ]
        headings = VGroup(
            formula("a", size=35).move_to(LEFT * 6.4 + UP * 1.25),
            *(
                formula(rf"j={j}", size=30).move_to(RIGHT * x + UP * 1.25)
                for j, x in enumerate(columns)
            ),
            formula(r"\text{row sum }=[X^a](hh^*)", size=29).move_to(
                RIGHT * 4.6 + UP * 1.25
            ),
        )
        grid = VGroup(
            *(Line([x, 0.8, 0], [x, -2.6, 0]) for x in [-5.4, -3.7, -2.0, -0.3, 1.4]),
            *(Line([-5.4, y, 0], [1.4, y, 0]) for y in [0.8, -0.05, -0.9, -1.75, -2.6]),
        ).set_stroke(BLUE_C, width=1.2, opacity=0.55)
        rows = VGroup(
            *(
                VGroup(
                    formula(str(a), size=35, color=BLUE_C).move_to(LEFT * 6.4 + UP * y),
                    *(
                        formula(str(value), size=42, color=BLUE_C)
                        .move_to(RIGHT * x + UP * y)
                        .set_opacity(0.15)
                        for x, value in zip(columns, values, strict=True)
                    ),
                )
                for a, (y, values) in enumerate(zip(row_heights, entries, strict=True))
            )
        )
        results = VGroup(
            *(
                formula(rf"[X^{a}](hh^*)={sum(values)}", size=36).move_to(
                    RIGHT * 4.6 + UP * y
                )
                for a, (y, values) in enumerate(zip(row_heights, entries, strict=True))
            )
        )
        self.show(headings, grid, rows)
        self.wait_until_narration(109.46)
        focus = SurroundingRectangle(rows[0], buff=0.15).set_color(YELLOW)
        self.show(focus, run_time=0.5)
        self.play(rows[0].animate.set_opacity(1).set_color(YELLOW), run_time=0.5)
        self.wait_until_narration(112.4)
        self.show(results[0].set_color(YELLOW), run_time=0.7)

        self.wait_until_narration(114.54)
        self.play(
            rows[0].animate.set_color(BLUE_C),
            results[0].animate.set_color(BLUE_C),
            Transform(
                focus, SurroundingRectangle(rows[1], buff=0.15).set_color(YELLOW)
            ),
            run_time=0.5,
        )
        for entry, cue in zip(rows[1][1:], [115.3, 116.38, 117.4, 118.52], strict=True):
            self.wait_until_narration(cue)
            self.play(entry.animate.set_opacity(1).set_color(YELLOW), run_time=0.25)
        self.wait_until_narration(119.1)
        self.show(results[1].set_color(YELLOW), run_time=0.5)

        for a, cue in [(2, 120.66), (3, 122.0)]:
            self.wait_until_narration(cue)
            self.play(
                rows[a - 1].animate.set_color(BLUE_C),
                results[a - 1].animate.set_color(BLUE_C).set_opacity(0.5),
                Transform(
                    focus, SurroundingRectangle(rows[a], buff=0.15).set_color(YELLOW)
                ),
                rows[a].animate.set_opacity(1).set_color(YELLOW),
                run_time=0.5,
            )
            self.show(results[a].set_color(YELLOW), run_time=0.3)
        self.play(
            rows[3].animate.set_color(BLUE_C),
            results[3].animate.set_color(BLUE_C).set_opacity(0.5),
            focus.animate.set_opacity(0),
            run_time=0.4,
        )

        self.section("product", "The example collapses to one equation")
        self.show(
            self.stack(
                formula(r"hh^*=4+0X+0X^2+0X^3", size=48),
                formula(r"\boxed{hh^*=4}", size=76, color=YELLOW),
                words("Equality modulo X⁴ − 1", size=28),
            )
        )

        self.section("dictionary", "1.5 · The general dictionary")
        signs = formula(r"h_j\in\{-1,1\}\quad(0\le j<n)", color=BLUE_C)
        signs.move_to(UP * 1.6)
        equivalence = formula(
            r"HH^{\mathsf T}=nI_n\quad\Longleftrightarrow\quad hh^*=n",
            size=47,
            color=YELLOW,
        ).move_to(UP * 0.5)
        self.show(signs, equivalence)
        self.wait_until_narration(self.cues["dictionary"] + 15)
        calculation = formula(
            r"[X^0](hh^*)=n,\qquad[X^a](hh^*)=0\ (a\ne0)",
            size=39,
        ).move_to(DOWN * 0.9)
        self.show(calculation)
        self.wait_until_narration(self.cues["dictionary"] + 24)
        reindexed = formula(
            r"\langle\mathrm{row}_r,\mathrm{row}_s\rangle"
            r"=\sum_k h_kh_{k-(s-r)}=[X^{s-r}](hh^*)",
            size=36,
        ).move_to(calculation)
        self.play(Transform(calculation, reindexed), run_time=1.6)
        self.show(
            words(
                "Shift both rows together; their relative offset stays s − r.", size=24
            ).move_to(DOWN * 2)
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
