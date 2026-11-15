import json
from math import cos, sin

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    PI,
    RIGHT,
    UP,
    YELLOW,
    Arrow,
    Circle,
    Dot,
    FadeOut,
    FlashAround,
    Line,
    Rectangle,
    SurroundingRectangle,
    Transform,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class CyclotomicDivisibility(NodeScene):
    node_id = "cyclotomic-divisibility"
    title = "2.4 · Compare Opposite Coefficients"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/cyclotomic-divisibility.json").read_text()
        )["detail_cues"]

        self.section("goal", "An integer norm identity controls opposite differences")
        self.show(
            formula(
                r"T(X)=\sum_{j=0}^{2^k-1}a_jX^j,\qquad a_j\in\mathbb Z",
                size=38,
            ).move_to(UP * 2),
            run_time=1,
        )
        center = LEFT * 4 + DOWN * 0.25
        points = [
            center + 1.3 * (RIGHT * cos(j * PI / 4) + UP * sin(j * PI / 4))
            for j in range(8)
        ]
        circle = Circle(radius=1.3).move_to(center).set_stroke(BLUE_C, width=2)
        dots = VGroup(*(Dot(point, radius=0.055).set_color(BLUE_C) for point in points))
        opposite = Line(points[1], points[5]).set_stroke(YELLOW, width=3)
        self.show(
            circle,
            dots,
            words("Cyclic positions", size=25).move_to(LEFT * 4 + UP * 1.5),
            formula(r"X^{2^k}=1", size=32, color=BLUE_C).move_to(
                LEFT * 4 + DOWN * 2.15
            ),
            words("Eight positions shown", size=23).move_to(LEFT * 4 + DOWN * 2.65),
            run_time=0.9,
        )
        self.at("goal_norm")
        self.show(
            formula(r"T(X)T^*(X)=2^{2t}w^2", size=43, color=BLUE_C).move_to(
                RIGHT * 3.3 + UP * 0.8
            ),
            formula(
                r"k\ge1,\quad t\in\mathbb Z_{\ge0},\quad w\text{ odd}", size=30
            ).move_to(RIGHT * 3.3 + DOWN * 0.2),
            run_time=0.9,
        )
        self.at("goal_opposite")
        self.show(
            opposite,
            formula(r"a_j", size=34, color=YELLOW).next_to(
                dots[1], UP + RIGHT, buff=0.1
            ),
            formula(r"a_{j+2^{k-1}}", size=32, color=YELLOW).next_to(
                dots[5], DOWN + LEFT, buff=0.1
            ),
            run_time=0.7,
        )
        self.show(
            formula(r"2^t\mid a_j-a_{j+2^{k-1}}", size=45, color=YELLOW).move_to(
                RIGHT * 3.3 + DOWN * 1.45
            ),
            run_time=0.9,
        )
        self.at("goal_not_signs")
        self.show(
            words("Integer coefficients; signs are not required.", size=24).move_to(
                DOWN * 3.15
            ),
            run_time=0.8,
        )

        self.section("basis", "Supplied cyclotomic input · Lemma 2.1")
        self.show(
            formula(
                r"\xi\text{ primitive of order }2^k", size=43, color=BLUE_C
            ).move_to(UP * 1.8),
            run_time=0.9,
        )
        self.at("basis_half")
        self.show(formula(r"D=2^{k-1}", size=51).move_to(UP * 0.65), run_time=0.8)
        powers = formula(r"1,\ X,\ \ldots,\ X^{D-1}", size=49).move_to(DOWN * 0.7)
        self.show(powers, run_time=0.8)
        self.at("basis_denominators")
        self.show(
            formula(
                r"\mathbb Z_{(2)}=\{a/b\in\mathbb Q:b\text{ odd}\}", size=37
            ).move_to(DOWN * 2.55),
            run_time=0.9,
        )
        self.at("basis_powers")
        self.play(
            Transform(
                powers,
                formula(r"1,\ \xi,\ \ldots,\ \xi^{D-1}", size=49, color=YELLOW).move_to(
                    powers
                ),
            ),
            run_time=1.1,
        )
        self.show(
            words(
                "D basis powers over the ring with odd denominators", size=24
            ).move_to(DOWN * 1.65),
            run_time=0.8,
        )

        self.section(
            "valuation_input", "Arithmetic valuation: a supplied divisibility rule"
        )
        normalization = formula(r"v(\,\cdot\,)", size=57, color=BLUE_C).move_to(
            UP * 1.85
        )
        self.show(normalization, run_time=0.8)
        self.at("valuation_normalize")
        self.play(
            Transform(
                normalization,
                formula(r"v(2)=1", size=57, color=BLUE_C).move_to(normalization),
            ),
            run_time=0.8,
        )
        self.at("valuation_arithmetic")
        self.show(
            words("Measures divisibility, not complex magnitude", size=26).move_to(
                UP * 0.9
            ),
            run_time=0.8,
        )
        summation = formula(r"\sum_{j=0}^{D-1}b_j\xi^j", size=48)
        hypothesis = (
            VGroup(
                formula("v", size=48),
                formula("(", size=48).stretch_to_fit_height(summation.get_height()),
                summation,
                formula(")", size=48).stretch_to_fit_height(summation.get_height()),
                formula(r"\ge t", size=48),
            )
            .arrange(RIGHT, buff=0.1)
            .set_color(YELLOW)
            .move_to(DOWN * 0.15)
        )
        coefficients = VGroup(
            *(
                formula(tex, size=43, color=BLUE_C)
                for tex in [r"b_0", r"b_1", r"\ldots", r"b_{D-1}"]
            )
        )
        coefficients.arrange(RIGHT, buff=1.2).move_to(DOWN * 1.6)
        self.at("valuation_hypothesis")
        self.show(hypothesis, coefficients, run_time=1)
        self.at("valuation_integer")
        self.show(
            formula(r"b_j\in\mathbb Z", size=32).move_to(RIGHT * 5.5 + DOWN * 0.3),
            run_time=0.7,
        )
        self.at("valuation_divides")
        targets = [r"2^t\mid b_0", r"2^t\mid b_1", r"\ldots", r"2^t\mid b_{D-1}"]
        self.play(
            *(
                Transform(term, formula(tex, size=37, color=YELLOW).move_to(term))
                for term, tex in zip(coefficients, targets, strict=True)
            ),
            run_time=1.2,
        )
        self.show(
            words("Supplied basis/valuation fact", size=25, color=BLUE_C).move_to(
                DOWN * 2.8
            ),
            run_time=0.7,
        )

        self.section(
            "cyclotomic_origin", "The standard cyclotomic facts behind the input"
        )
        phi = formula(r"\Phi_{2^k}(X)=X^D+1", size=55, color=BLUE_C).move_to(UP * 1.55)
        self.show(phi, run_time=1)
        self.at("origin_shift")
        shifted = formula(r"\Phi_{2^k}(1+Y)=(1+Y)^D+1", size=48).move_to(phi)
        self.play(Transform(phi, shifted), run_time=1.2)
        self.at("origin_eisenstein")
        self.show(
            words("Eisenstein at 2 · supplied fact", size=28, color=YELLOW).move_to(
                UP * 0.35
            ),
            run_time=0.8,
        )
        unit_relation = formula(
            r"2=\varepsilon(\xi-1)^D", size=59, color=BLUE_C
        ).move_to(DOWN * 1.1)
        self.at("origin_unit")
        self.show(unit_relation, run_time=1)
        self.show(
            formula(r"\varepsilon\text{ is a unit}", size=33).move_to(DOWN * 2),
            run_time=0.7,
        )
        self.at("origin_coefficients")
        self.play(FlashAround(unit_relation, color=YELLOW), run_time=0.8)
        self.show(
            words(
                "The input transfers valuation to basis coefficients.", size=25
            ).move_to(DOWN * 3.05),
            run_time=0.8,
        )

        self.section("norm", "Use the norm identity to determine the valuation")
        norm = formula(r"T(X)T^*(X)=2^{2t}w^2", size=54, color=BLUE_C).move_to(UP * 1.2)
        self.show(norm, run_time=0.9)
        self.at("norm_substitute")
        self.play(
            Transform(
                norm,
                formula(
                    r"T(\xi)\overline{T(\xi)}=2^{2t}w^2", size=54, color=BLUE_C
                ).move_to(norm),
            ),
            run_time=1.1,
        )
        valuation = formula(
            r"v(T(\xi))+v(\overline{T(\xi)})=2t\,v(2)+2v(w)", size=43
        ).move_to(DOWN * 0.4)
        self.at("norm_add")
        self.show(valuation, run_time=1)
        self.at("norm_odd")
        self.show(
            formula(
                r"w\text{ odd}\quad\Longrightarrow\quad v(w)=0", size=42, color=YELLOW
            ).move_to(DOWN * 1.8),
            run_time=0.8,
        )
        self.at("norm_value")
        self.play(
            Transform(
                valuation,
                formula(
                    r"v(T(\xi))+v(\overline{T(\xi)})=2t",
                    size=47,
                    color=YELLOW,
                ).move_to(valuation),
            ),
            run_time=1,
        )

        self.section("conjugation", "Conjugation preserves this arithmetic valuation")
        left = formula(r"v(T(\xi))", size=47, color=BLUE_C)
        right = formula(r"v(\overline{T(\xi)})", size=47, color=BLUE_C)
        sum_group = (
            VGroup(left, formula("+", size=47), right, formula("=2t", size=47))
            .arrange(RIGHT, buff=0.2)
            .move_to(UP * 1.4)
        )
        self.show(sum_group, run_time=0.9)
        conjugate = formula(r"\overline{\xi-1}=-\xi^{-1}(\xi-1)", size=51).move_to(
            DOWN * 0.15
        )
        self.at("conjugation_map")
        self.show(conjugate, run_time=0.9)
        self.at("conjugation_unit")
        self.show(
            formula(r"-\xi^{-1}\text{ is a unit}", size=36, color=YELLOW).move_to(
                DOWN * 1.2
            ),
            run_time=0.7,
        )
        self.at("conjugation_unchanged")
        self.play(
            Transform(
                right, formula(r"v(T(\xi))", size=47, color=BLUE_C).move_to(right)
            ),
            run_time=0.8,
        )
        self.at("conjugation_twice")
        self.play(
            Transform(sum_group, formula(r"2v(T(\xi))=2t", size=59).move_to(sum_group)),
            run_time=0.9,
        )
        self.at("conjugation_result")
        result = formula(r"\boxed{v(T(\xi))=t}", size=58, color=YELLOW).move_to(
            DOWN * 2.55
        )
        self.show(result, run_time=0.9)

        self.section(
            "opposite_terms", "Opposite powers combine into coefficient differences"
        )
        self.show(
            formula(r"\xi^D=-1", size=60, color=BLUE_C).move_to(UP * 1.9), run_time=0.9
        )
        first = formula(r"a_j\xi^j", size=53).move_to(LEFT * 3 + UP * 0.2)
        second = formula(r"a_{j+D}\xi^{j+D}", size=53).move_to(RIGHT * 3 + UP * 0.2)
        pair = VGroup(first, formula("+", size=53).move_to(UP * 0.2), second)
        self.at("opposite_pair")
        self.show(pair, run_time=0.9)
        self.at("opposite_factor")
        self.play(
            Transform(
                second,
                formula(r"a_{j+D}\xi^j\xi^D", size=48, color=BLUE_C).move_to(second),
            ),
            run_time=0.9,
        )
        self.at("opposite_negative")
        self.play(
            Transform(pair[1], formula("-", size=53, color=YELLOW).move_to(pair[1])),
            Transform(
                second, formula(r"a_{j+D}\xi^j", size=53, color=YELLOW).move_to(second)
            ),
            run_time=0.9,
        )
        self.at("opposite_difference")
        self.play(
            Transform(
                pair,
                formula(r"(a_j-a_{j+D})\xi^j", size=61, color=YELLOW).move_to(UP * 0.2),
            ),
            run_time=1.2,
        )
        self.at("opposite_every")
        self.show(
            formula(r"0\le j<D:\quad\text{every opposite pair}", size=37).move_to(
                DOWN * 1.6
            ),
            run_time=0.8,
        )

        self.section(
            "conclusion", "Apply the supplied input to the actual basis coefficients"
        )
        coefficient = formula(r"(a_j-a_{j+D})", size=47, color=BLUE_C)
        evaluation = (
            VGroup(
                formula(r"T(\xi)=\sum_{j=0}^{D-1}", size=47),
                coefficient,
                formula(r"\xi^j", size=47),
            )
            .arrange(RIGHT, buff=0.3)
            .move_to(UP * 1.2)
        )
        self.show(evaluation, run_time=1)
        valuation_result = formula(r"v(T(\xi))=t", size=52, color=BLUE_C).move_to(
            DOWN * 0.1
        )
        self.at("conclusion_valuation")
        self.show(valuation_result, run_time=0.8)
        self.at("conclusion_input")
        self.show(
            SurroundingRectangle(coefficient, buff=0.13).set_color(YELLOW), run_time=0.6
        )
        self.show(
            Arrow(
                valuation_result.get_top(), coefficient.get_bottom(), buff=0.15
            ).set_color(BLUE_C),
            run_time=0.6,
        )
        self.at("conclusion_divides")
        self.show(
            formula(
                r"\boxed{2^t\mid a_j-a_{j+D}}\qquad(0\le j<D)", size=48, color=YELLOW
            ).move_to(DOWN * 1.75),
            run_time=1,
        )
        self.show(
            words("By the supplied cyclotomic input", size=25).move_to(DOWN * 2.85),
            run_time=0.7,
        )

        self.section(
            "order_sixteen", "Hypothetical order 16: the coefficients are signs"
        )
        self.show(
            formula(r"k=4,\quad t=2,\quad w=1", size=39, color=BLUE_C).move_to(UP * 2),
            run_time=0.8,
        )
        divisibility = formula(r"4\mid h_j-h_{j+8}", size=55).move_to(UP * 0.95)
        self.at("sixteen_signs")
        self.show(divisibility, run_time=0.8)
        differences = (
            VGroup(
                *(formula(value, size=57, color=BLUE_C) for value in ["-2", "0", "2"])
            )
            .arrange(RIGHT, buff=1.15)
            .move_to(DOWN * 0.25)
        )
        self.at("sixteen_differences")
        self.show(differences, run_time=0.8)
        strikes = VGroup(
            *(
                Line(
                    term.get_corner(DOWN + LEFT), term.get_corner(UP + RIGHT)
                ).set_stroke(YELLOW, width=3)
                for term in [differences[0], differences[2]]
            )
        )
        self.at("sixteen_only_zero")
        self.show(strikes, run_time=0.5)
        self.play(
            differences[0].animate.set_opacity(0.2),
            differences[2].animate.set_opacity(0.2),
            differences[1].animate.set_color(YELLOW),
            run_time=0.5,
        )
        self.at("sixteen_equal")
        self.play(
            Transform(
                divisibility,
                formula(r"h_j=h_{j+8}", size=58, color=YELLOW).move_to(divisibility),
            ),
            run_time=0.9,
        )
        self.play(FadeOut(differences), FadeOut(strikes), run_time=0.4)
        self.body.remove(differences, strikes)
        blocks = VGroup(
            *(
                VGroup(
                    Rectangle(width=2.7, height=0.8).set_stroke(BLUE_C, width=2),
                    formula(r"\mathbf a", size=43),
                ).move_to(RIGHT * x + DOWN * 0.5)
                for x in [-1.6, 1.6]
            )
        )
        self.show(
            blocks,
            formula(r"\mathbf a=(h_0,\ldots,h_7)", size=32).move_to(DOWN * 1.7),
            run_time=0.8,
        )
        positions = [block.get_center().copy() for block in blocks]
        self.at("sixteen_shift")
        self.play(
            Transform(blocks[0], blocks[0].copy().move_to(positions[1]), path_arc=1),
            Transform(blocks[1], blocks[1].copy().move_to(positions[0]), path_arc=-1),
            run_time=1.1,
        )
        self.at("sixteen_dot")
        self.show(
            formula(
                r"\langle\mathrm{row},\mathrm{shift}_8(\mathrm{row})\rangle=16\ne0",
                size=40,
                color=YELLOW,
            ).move_to(DOWN * 2.65),
            run_time=0.9,
        )

        self.section("general", "Carry the divisibility into the general folding step")
        self.show(
            formula(r"2^t\mid a_j-a_{j+2^{k-1}}", size=59, color=YELLOW).move_to(
                UP * 1.25
            ),
            run_time=1,
        )
        self.at("general_odd")
        self.show(
            formula(
                r"a_j\in2\mathbb Z+1\quad\text{in the descent}", size=39, color=BLUE_C
            ).move_to(UP * 0.1),
            run_time=0.8,
        )
        next_pair = (
            VGroup(
                formula(r"a_j", size=58, color=BLUE_C),
                formula(r"a_{j+2^{k-1}}", size=58, color=BLUE_C),
            )
            .arrange(RIGHT, buff=2)
            .move_to(DOWN * 1.45)
        )
        self.at("general_fold")
        self.show(next_pair, run_time=0.8)
        self.play(
            next_pair.animate.arrange(RIGHT, buff=0.7).move_to(DOWN * 1.45), run_time=1
        )
        self.show(
            words("Next: fold and average opposite pairs", size=28).move_to(
                DOWN * 2.75
            ),
            run_time=0.8,
        )
