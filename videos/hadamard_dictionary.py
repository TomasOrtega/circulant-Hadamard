import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    FlashAround,
    Matrix,
    SurroundingRectangle,
    Transform,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, sign_matrix, words


class HadamardDictionary(NodeScene):
    node_id = "hadamard-dictionary"
    title = "1.5 · The Hadamard dictionary"

    def beat(self, key):
        self.wait_until_narration(self.beats[key])

    def strip(self, values, center, color=BLUE_C):
        return (
            VGroup(*(formula(value, size=42, color=color) for value in values))
            .arrange(RIGHT, buff=0.7)
            .move_to(center)
        )

    def present(self):
        self.beats = json.loads(
            (ROOT / "videos/production/hadamard-dictionary.json").read_text()
        )["beats"]
        self.section("lemma", "One exact dictionary for circulant sign matrices")
        hypothesis = formula(r"h_j\in\{-1,1\}\quad(0\le j<n)", color=BLUE_C)
        hypothesis.move_to(UP * 1.8)
        matrix_equation = formula(r"HH^{\mathsf T}=nI_n", size=53)
        matrix_equation.move_to(LEFT * 3.3)
        ring_equation = formula(r"h(X)h^*(X)=n", size=53)
        ring_equation.move_to(RIGHT * 3.3)
        forward = Arrow(LEFT * 0.9 + UP * 0.18, RIGHT * 0.9 + UP * 0.18)
        forward.set_color(YELLOW)
        backward = Arrow(RIGHT * 0.9 + DOWN * 0.18, LEFT * 0.9 + DOWN * 0.18)
        backward.set_color(BLUE_C)
        self.show(hypothesis)
        self.beat("star_definition")
        self.show(
            formula(r"\mathbb Z[X]/(X^n-1),\qquad h^*(X)=h(X^{-1})", size=40).move_to(
                DOWN * 1.6
            )
        )
        self.beat("claim")
        self.show(matrix_equation, ring_equation)
        self.beat("equivalence")
        self.show(forward, backward)

        self.section("forward", "Forward · orthogonality cancels nonconstant terms")
        matrix = sign_matrix().move_to(LEFT * 3.3)
        illustration = words("n = 4 illustration", size=22).move_to(LEFT * 3.3 + UP * 2)
        terms = (
            VGroup(
                formula("C_0", size=41, color=BLUE_C),
                formula("+C_1X", size=41),
                formula("+C_2X^2", size=41),
                formula("+C_3X^3", size=41),
            )
            .arrange(RIGHT, buff=0.1)
            .set_width(6)
            .move_to(RIGHT * 3 + UP * 0.6)
        )
        first = SurroundingRectangle(matrix.get_rows()[0]).set_color(BLUE_C)
        shifted = SurroundingRectangle(matrix.get_rows()[1]).set_color(YELLOW)
        self.show(matrix, illustration, terms, first, shifted)
        definition = formula(
            r"C_a=\langle\mathrm{row}_0,\mathrm{row}_a\rangle", size=33
        )
        definition.move_to(RIGHT * 3 + DOWN * 0.7)
        self.beat("correlation")
        self.show(definition)
        for index in range(1, 4):
            self.play(
                Transform(
                    shifted,
                    SurroundingRectangle(matrix.get_rows()[index]).set_color(YELLOW),
                ),
                run_time=0.65,
            )
            self.play(FlashAround(terms[index], color=YELLOW), run_time=0.55)
            zero = formula("+0X" + (f"^{index}" if index > 1 else ""), size=41)
            zero.move_to(terms[index])
            self.play(Transform(terms[index], zero), run_time=0.7)
            self.play(terms[index].animate.set_opacity(0.18), run_time=0.4)
        constant = formula("4", size=52, color=YELLOW).move_to(terms[0])
        self.beat("sign_norm")
        self.play(Transform(terms[0], constant), run_time=0.8)
        self.beat("product")
        self.show(
            formula(
                r"\sum_jh_j^2=n\quad\Longrightarrow\quad hh^*=n", size=43, color=YELLOW
            ).move_to(DOWN * 2.2)
        )

        self.section("reverse", "Backward · read off every cyclic correlation")
        product = formula(r"hh^*=n", size=68, color=BLUE_C).move_to(UP * 1.6)
        coefficients = self.strip(["n", "0", r"\cdots", "0"], UP * 0.2)
        positions = VGroup(
            *(
                formula(label, size=26).next_to(entry, DOWN, buff=0.3)
                for label, entry in zip(
                    ["1", "X", r"\cdots", "X^{n-1}"], coefficients, strict=True
                )
            )
        )
        self.show(product)
        self.beat("unique_representative")
        self.show(coefficients, positions)
        self.beat("zero_coefficients")
        self.play(VGroup(*coefficients[1:]).animate.set_color(YELLOW), run_time=0.8)
        conclusion = formula(
            r"[X^a](hh^*)=0\quad\Longrightarrow\quad"
            r"\langle\mathrm{row}_0,\mathrm{row}_a\rangle=0\quad(0<a<n)",
            size=40,
            color=YELLOW,
        ).move_to(DOWN * 1.5)
        self.beat("first_row_orthogonal")
        self.show(conclusion)

        self.section("arbitrary", "A common shift preserves the relative offset")
        first_strip = self.strip(["1", "-1", "1", "1"], LEFT * 3 + UP * 0.9)
        second_strip = self.strip(["1", "1", "1", "-1"], LEFT * 3 + DOWN * 0.6)
        first_label = formula(r"r=1", size=29).next_to(first_strip, LEFT, buff=0.4)
        second_label = formula(r"s=3", size=29).next_to(second_strip, LEFT, buff=0.4)
        self.show(first_strip, second_strip, first_label, second_label)
        self.show(words("n = 4 illustration", size=22).move_to(LEFT * 3 + UP * 1.9))
        offset = formula(r"s-r=2", color=YELLOW, size=42).move_to(RIGHT * 3 + UP * 1.5)
        self.show(offset)
        calculation = formula(r"\sum_jh_{j-r}h_{j-s}", size=43)
        calculation.move_to(RIGHT * 3 + UP * 0.2)
        self.show(calculation)
        shifts = []
        for strip in [first_strip, second_strip]:
            positions = [entry.get_center().copy() for entry in strip]
            shifts.extend(
                Transform(
                    entry,
                    entry.copy().move_to(positions[(j - 1) % 4]),
                    path_arc=1.3 if j == 0 else 0,
                )
                for j, entry in enumerate(strip)
            )
        self.beat("common_shift")
        self.play(*shifts, run_time=1.5)
        self.beat("relative_offset")
        self.play(
            Transform(first_label, formula("0", size=29).move_to(first_label)),
            Transform(second_label, formula("2", size=29).move_to(second_label)),
            run_time=0.9,
        )
        self.beat("reindex")
        self.play(
            Transform(
                calculation,
                formula(r"\sum_kh_kh_{k-(s-r)}", size=43).move_to(calculation),
            ),
            run_time=0.9,
        )
        self.beat("coefficient")
        self.show(
            formula(r"=[X^{s-r}](hh^*)", size=43, color=YELLOW).move_to(
                RIGHT * 3 + DOWN * 1
            )
        )
        result = formula(r"r\ne s:\ 0\qquad r=s:\ n", size=40, color=YELLOW)
        result.move_to(DOWN * 2.2)
        self.beat("pairwise_results")
        self.show(result)
        self.beat("matrix_identity")
        self.play(
            Transform(
                result,
                formula(r"HH^{\mathsf T}=nI_n", size=49, color=YELLOW).move_to(result),
            ),
            run_time=0.9,
        )

        self.section("signs", "One hypothesis has two essential roles")
        sign = formula(r"h_j\in\{-1,1\}", size=64, color=YELLOW).move_to(UP * 1.8)
        norm = formula(r"h_j^2=1", size=49, color=BLUE_C).move_to(LEFT * 3 + UP * 0.1)
        entry = formula(r"H_{rj}=h_{j-r}\in\{-1,1\}", size=43, color=BLUE_C)
        entry.move_to(RIGHT * 3 + UP * 0.1)
        arrows = VGroup(
            Arrow(sign.get_bottom(), norm.get_top(), buff=0.2).set_color(BLUE_C),
            Arrow(sign.get_bottom(), entry.get_top(), buff=0.2).set_color(BLUE_C),
        )
        self.show(sign)
        self.beat("forward_sign_role")
        self.show(arrows[0], norm)
        self.show(
            formula(r"\sum_jh_j^2=n", size=46).move_to(LEFT * 3 + DOWN * 1.3),
        )
        self.beat("backward_sign_role")
        self.show(arrows[1], entry)
        self.show(
            words("Every matrix entry is a sign", size=26, width=6).move_to(
                RIGHT * 3 + DOWN * 1.3
            ),
        )

        self.section("nonsign", "The norm equation alone does not force signs")
        matrix = (
            Matrix(
                [[2 if i == j else 0 for j in range(4)] for i in range(4)],
                h_buff=0.65,
                v_buff=0.45,
            )
            .scale(0.8)
            .set_color(BLUE_C)
            .move_to(LEFT * 3)
        )
        self.show(
            formula(r"h=2,\quad hh^*=4", size=44, color=YELLOW, width=6).move_to(
                RIGHT * 3 + UP
            )
        )
        self.beat("nonsign_coefficients")
        self.show(formula(r"(2,0,0,0)", size=42).move_to(RIGHT * 3))
        self.beat("nonsign_matrix")
        self.show(matrix)
        self.show(formula(r"H=2I_4", size=43).move_to(RIGHT * 3 + DOWN))
        self.beat("nonsign_failure")
        self.show(
            words("Orthogonal rows; entries are not signs.", size=25).move_to(
                DOWN * 2.1
            )
        )
        self.play(FlashAround(matrix.get_entries()[0], color=YELLOW), run_time=0.8)
        self.play(FlashAround(matrix.get_entries()[1], color=YELLOW), run_time=0.8)

        self.section("all_ones", "All ones keep every off-diagonal dot product")
        original = sign_matrix((1, 1, 1, 1), size=0.62).move_to(LEFT * 3.5 + UP * 0.2)
        gram = Matrix([[4] * 4 for _ in range(4)], h_buff=0.65, v_buff=0.45)
        gram.scale(0.62).set_color(BLUE_C).move_to(RIGHT * 3.5 + UP * 0.2)
        arrow = Arrow(LEFT * 0.9 + UP * 0.2, RIGHT * 0.9 + UP * 0.2).set_color(WHITE)
        self.show(original)
        self.beat("all_ones_gram")
        self.show(arrow, formula(r"HH^{\mathsf T}", size=30).move_to(UP))
        self.show(gram)
        self.play(FlashAround(gram.get_entries()[1], color=YELLOW), run_time=0.8)
        self.beat("all_ones_product")
        self.show(
            formula(r"(1+X+X^2+X^3)^2=4(1+X+X^2+X^3)", size=43, color=YELLOW).move_to(
                DOWN * 2.1
            )
        )

        self.section("finish", "The exact dictionary for a circulant sign matrix")
        self.show(
            self.stack(
                formula(r"h_j=\pm1", size=56, color=BLUE_C),
                formula(
                    r"HH^{\mathsf T}=nI_n\quad\Longleftrightarrow\quad hh^*=n",
                    size=54,
                    color=YELLOW,
                ),
                words("Next: what does the equation tell us about n?", size=29),
            )
        )
