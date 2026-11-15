import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    FadeOut,
    LaggedStart,
    Rectangle,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class HalveSignSums(NodeScene):
    node_id = "halve-sign-sums"
    title = "3.4 · Parity of Sign Columns"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def hide(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.35)
        self.body.remove(*objects)

    def coefficient_strip(self):
        return VGroup(
            *(
                formula(rf"a_{j}", size=43, color=BLUE_C).move_to(
                    RIGHT * (-4.5 + 3 * j) + UP * 1.95
                )
                for j in range(4)
            )
        )

    def sum_terms(self, alternate, center):
        return (
            VGroup(
                *(
                    formula(
                        ("" if j == 0 else ("-" if alternate and j % 2 else "+"))
                        + rf"a_{j}",
                        size=38,
                        color=BLUE_C,
                    )
                    for j in range(4)
                )
            )
            .arrange(RIGHT, buff=0.12)
            .set_max_width(6.5)
            .move_to(center)
        )

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/halve-sign-sums.json").read_text()
        )["detail_cues"]

        self.section("column", "Select one common coefficient position")
        rows = VGroup(
            *(
                VGroup(
                    formula(rf"H_{j}(P)=\cdots+", size=34),
                    formula(rf"a_{j}", size=34, color=BLUE_C),
                    formula("P^b", size=34, color=YELLOW),
                    formula(r"+\cdots", size=34),
                )
                .arrange(RIGHT, buff=0.22)
                .move_to(LEFT * 3.6 + UP * (1.7 - 1.05 * j))
                for j in range(4)
            )
        )
        self.show(rows)
        self.at("fixed_power")
        highlights = VGroup(
            *(
                SurroundingRectangle(VGroup(row[1], row[2]), buff=0.09).set_color(
                    YELLOW
                )
                for row in rows
            )
        )
        self.show(
            highlights,
            formula(r"P^b\text{ stays fixed}", size=35, color=YELLOW).move_to(
                RIGHT * 3.7 + UP * 2.15
            ),
            run_time=0.85,
        )
        column = VGroup(
            *(
                formula(rf"a_{j}", size=44, color=BLUE_C).move_to(
                    RIGHT * 3.0 + UP * (1.2 - 0.9 * j)
                )
                for j in range(4)
            )
        )
        self.at("coefficients")
        self.body.add(column)
        self.play(
            LaggedStart(
                *(
                    TransformFromCopy(row[1], target)
                    for row, target in zip(rows, column, strict=True)
                ),
                lag_ratio=0.18,
            ),
            run_time=1.5,
        )
        self.at("odd_signs")
        self.show(
            VGroup(
                *(
                    words("odd", size=27).next_to(entry, RIGHT, buff=0.5)
                    for entry in column
                )
            ),
            formula(
                r"a_j\in\{-1,1\}\quad\Longrightarrow\quad a_j\equiv1\pmod2", size=35
            ).move_to(DOWN * 2.9),
        )

        self.section("real", "Both real combinations have even coefficients")
        strip = self.coefficient_strip()
        self.show(strip, run_time=0.75)
        left_center = LEFT * 3.8 + UP * 0.1
        right_center = RIGHT * 3.8 + UP * 0.1
        sums = [self.sum_terms(False, left_center), self.sum_terms(True, right_center)]
        for key, label, terms, center in zip(
            ["plus_sum", "alternating_sum"],
            [r"Z=1", r"Z=-1"],
            sums,
            [left_center, right_center],
            strict=True,
        ):
            self.at(key)
            self.show(formula(label, size=36).move_to(center + UP * 0.95), run_time=0.6)
            self.body.add(terms)
            self.play(
                *(
                    TransformFromCopy(source, target)
                    for source, target in zip(strip, terms, strict=True)
                ),
                run_time=1.1,
            )
        panel = Rectangle(width=14.9, height=1.25).set_stroke(BLUE_C, width=1.5)
        panel.move_to(DOWN * 1.75)
        reduction = formula(r"a_j\equiv-a_j\equiv1\pmod2", size=33, color=YELLOW)
        reduction.move_to(DOWN * 0.75)
        residues = VGroup(
            *(
                VGroup(
                    formula("1+1", size=38, color=YELLOW),
                    formula("+1+1", size=38, color=YELLOW),
                )
                .arrange(RIGHT, buff=0.25)
                .move_to(center + DOWN * 1.85)
                for center in [left_center, right_center]
            )
        )
        self.at("modulo_two")
        self.show(panel, reduction, run_time=0.8)
        self.body.add(residues)
        self.play(
            *(
                TransformFromCopy(source, target)
                for source, target in zip(sums, residues, strict=True)
            ),
            run_time=1.1,
        )
        pair_frames = VGroup(
            *(
                SurroundingRectangle(pair, buff=0.08).set_color(YELLOW)
                for row in residues
                for pair in row
            )
        )
        self.at("pairs")
        self.show(pair_frames, run_time=0.7)
        self.play(
            *(
                Transform(
                    pair,
                    formula("0" if j == 0 else "+0", size=38, color=YELLOW).move_to(
                        pair
                    ),
                )
                for row in residues
                for j, pair in enumerate(row)
            ),
            run_time=0.85,
        )
        self.play(
            FadeOut(pair_frames),
            *(
                Transform(row, formula("0", size=46, color=YELLOW).move_to(row))
                for row in residues
            ),
            run_time=0.75,
        )
        self.body.remove(pair_frames)
        self.at("integer_halves")
        self.hide(panel, reduction, residues)
        halves = VGroup(
            formula(
                r"\frac{a_0+a_1+a_2+a_3}{2}\in\mathbb Z", size=37, width=7.1
            ).move_to(LEFT * 3.8 + DOWN * 1.65),
            formula(
                r"\frac{a_0-a_1+a_2-a_3}{2}\in\mathbb Z", size=37, width=7.1
            ).move_to(RIGHT * 3.8 + DOWN * 1.65),
        )
        self.body.add(halves)
        self.play(
            *(
                TransformFromCopy(source, target)
                for source, target in zip(sums, halves, strict=True)
            ),
            run_time=1.3,
        )
        self.show(
            words(
                "Return to the integers · divide the even expressions by 2", size=28
            ).move_to(DOWN * 2.9),
            run_time=0.85,
        )

        self.section("gaussian", "Halve the real and imaginary differences separately")
        strip = self.coefficient_strip()
        self.show(strip, run_time=0.65)
        expression = formula(r"Z=i:\quad(a_0-a_2)+i(a_1-a_3)", size=44)
        expression.move_to(UP * 0.65)
        self.at("gaussian_expression")
        self.show(expression)
        real_pair = (
            VGroup(
                formula("a_0", size=42, color=BLUE_C),
                formula("-a_2", size=42, color=BLUE_C),
            )
            .arrange(RIGHT, buff=0.12)
            .move_to(LEFT * 3.5 + DOWN * 0.65)
        )
        imaginary_pair = (
            VGroup(
                formula("a_1", size=42, color=BLUE_C),
                formula("-a_3", size=42, color=BLUE_C),
            )
            .arrange(RIGHT, buff=0.12)
            .move_to(RIGHT * 3.5 + DOWN * 0.65)
        )
        self.at("even_differences")
        self.body.add(real_pair, imaginary_pair)
        self.play(
            TransformFromCopy(strip[0], real_pair[0]),
            TransformFromCopy(strip[2], real_pair[1]),
            TransformFromCopy(strip[1], imaginary_pair[0]),
            TransformFromCopy(strip[3], imaginary_pair[1]),
            run_time=1.1,
        )
        even_labels = VGroup(
            words("even real difference", size=25).move_to(LEFT * 3.5 + DOWN * 1.5),
            words("even imaginary difference", size=25).move_to(
                RIGHT * 3.5 + DOWN * 1.5
            ),
        )
        self.show(even_labels, run_time=0.8)
        self.at("divide_parts")
        self.play(
            Transform(
                real_pair,
                formula(
                    r"\frac{a_0-a_2}{2}\in\mathbb Z", size=40, color=YELLOW
                ).move_to(real_pair),
            ),
            Transform(
                imaginary_pair,
                formula(
                    r"\frac{a_1-a_3}{2}\in\mathbb Z", size=40, color=YELLOW
                ).move_to(imaginary_pair),
            ),
            run_time=1.2,
        )
        self.at("gaussian_integer")
        self.show(
            formula(
                r"\frac{a_0-a_2}{2}+i\frac{a_1-a_3}{2}\in\mathbb Z[i]",
                size=43,
                color=YELLOW,
            ).move_to(DOWN * 2.8)
        )

        self.at("example_column")
        self.hide(*list(self.body))
        self.show(
            words("One coefficient check at Pᵇ", size=30).move_to(UP * 2.2),
            run_time=0.7,
        )
        example = VGroup(
            *(
                VGroup(
                    formula(rf"a_{j}", size=29).move_to(
                        RIGHT * (-3 + 2 * j) + UP * 1.65
                    ),
                    formula(str(value), size=45, color=BLUE_C).move_to(
                        RIGHT * (-3 + 2 * j) + UP * 0.85
                    ),
                )
                for j, value in enumerate([-1, 1, 1, -1])
            )
        )
        self.show(example, run_time=0.8)
        for key, source, y in [
            ("first_zero", r"Z=1:\quad\frac{-1+1+1-1}{2}=0", -0.3),
            ("second_zero", r"Z=-1:\quad\frac{-1-1+1+1}{2}=0", -1.4),
            (
                "example_gaussian",
                r"Z=i:\quad\frac{-1-1}{2}+i\frac{1-(-1)}{2}=-1+i",
                -2.6,
            ),
        ]:
            self.at(key)
            self.show(
                formula(source, size=36, color=YELLOW).move_to(UP * y), run_time=0.9
            )
        self.at("coefficient_check")
        self.show(
            words(
                "One column illustrating parity · no Hadamard row constructed", size=25
            ).move_to(DOWN * 3.55),
            run_time=0.8,
        )

        self.at("every_position")
        self.hide(*list(self.body))
        powers = formula(r"\{P^b:0\le b<u^2\}", size=41, color=BLUE_C).move_to(UP * 1.9)
        self.show(powers, run_time=0.8)
        self.show(
            words("The same independent check at every position", size=28).move_to(
                UP * 0.85
            ),
            run_time=0.8,
        )
        self.at("polynomial_halves")
        self.show(
            formula(
                r"\frac{h(1,P)}2,\ \frac{h(-1,P)}2\in\mathbb Z[P]/(P^{u^2}-1)", size=41
            ).move_to(DOWN * 0.3),
            formula(
                r"\frac{h(i,P)}2\in\mathbb Z[i][P]/(P^{u^2}-1)", size=41, color=BLUE_C
            ).move_to(DOWN * 1.65),
        )
        self.at("only_signs")
        self.show(
            words("Only the common signs · no norm identity used", size=29).move_to(
                DOWN * 3.05
            )
        )
