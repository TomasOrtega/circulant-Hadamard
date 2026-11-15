import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class OddOnesAtOne(NodeScene):
    node_id = "odd-ones-at-one"
    title = "8.2 · An Odd Number of Ones at One"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def hide(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.35)
        self.body.remove(*objects)

    def sum_row(self, powers):
        parts = []
        for j in range(9):
            if j:
                parts.append(formula("+", size=28))
            parts.append(formula(rf"P^{{{j}}}" if powers else "1", size=37))
        return VGroup(*parts).arrange(RIGHT, buff=0.17)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/odd-ones-at-one.json").read_text()
        )["detail_cues"]

        self.section("ones", "Count exactly, then pass to the common quotient")
        assumption = formula(r"u>1\text{ odd}", size=38, color=BLUE_C).move_to(
            UP * 2.05
        )
        polynomial = formula(
            r"J(P)=\sum_{j=0}^{u^2-1}P^j", size=47, color=BLUE_C
        ).move_to(UP * 0.8)
        self.show(assumption, polynomial)
        self.at("substitute_one")
        evaluation = formula(r"J(1)=\sum_{j=0}^{u^2-1}1=u^2", size=47).move_to(
            polynomial
        )
        self.play(Transform(polynomial, evaluation), run_time=1.3)
        self.at("nine_ones")
        self.hide(polynomial)
        example = words("Exact example · u = 3", size=28, color=BLUE_C).move_to(
            UP * 1.3
        )
        powers = self.sum_row(True).move_to(DOWN * 0.05)
        ones = self.sum_row(False).move_to(powers)
        self.show(example, powers, run_time=0.8)
        self.play(Transform(powers, ones), run_time=1.3)
        exact_count = formula(r"J(1)=9", size=48, color=YELLOW).move_to(DOWN * 1.25)
        self.show(exact_count, run_time=0.9)

        self.at("common_quotient")
        self.hide(assumption, powers, example)
        self.play(exact_count.animate.move_to(UP * 1.8), run_time=0.6)
        divider = Line(LEFT * 6.7, RIGHT * 6.7).set_stroke(BLUE_C, width=1.2)
        divider.move_to(UP * 1.2)
        residue_label = words(
            "Residues in the same nonzero characteristic-two ring",
            size=27,
            color=BLUE_C,
        ).move_to(UP * 0.6)
        self.show(divider, residue_label, run_time=0.8)
        residues = VGroup(*(formula("1", size=43) for _ in range(9))).arrange(
            RIGHT, buff=0.64
        )
        residues.move_to(DOWN * 1.0)
        self.body.add(residues)
        self.play(TransformFromCopy(exact_count, residues), run_time=1.2)
        self.at("pair_zero")
        pair_identity = formula(
            r"2=(1+i)(1-i)\equiv0\pmod{1+i}", size=39, color=BLUE_C
        ).move_to(DOWN * 2.75)
        self.show(pair_identity, run_time=1.0)
        self.at("pair_eight")
        pair_frames = VGroup(
            *(
                SurroundingRectangle(
                    VGroup(*residues[2 * j : 2 * j + 2]), buff=0.14
                ).set_color(YELLOW)
                for j in range(4)
            )
        )
        self.show(pair_frames, run_time=0.7)
        zeros = VGroup(
            *(
                formula("0", size=43, color=BLUE_C).move_to(frame)
                for frame in pair_frames
            )
        )
        survivor = residues[-1].copy().set_color(YELLOW)
        self.body.add(zeros, survivor)
        self.play(
            FadeOut(residues),
            FadeOut(pair_frames),
            FadeIn(zeros),
            FadeIn(survivor),
            run_time=1.2,
        )
        self.body.remove(residues, pair_frames)
        self.at("general_odd")
        self.hide(zeros, survivor, pair_identity)
        general_residue = formula(
            r"J(1)=u^2\equiv1\pmod{1+i}", size=49, color=YELLOW
        ).move_to(DOWN * 1.15)
        self.show(general_residue)

        self.section("denominator", "Real coefficients determine the value at one")
        quotient = formula(r"\frac{J(1)}{c(1)}", size=54, color=BLUE_C).move_to(
            UP * 1.8
        )
        self.show(quotient)
        self.at("real_norm")
        norm = formula(r"c(P)c^*(P)=u^2", size=47).move_to(UP * 0.35)
        real = formula(r"c(P)\in\mathbb Z[P]/(P^{u^2}-1)", size=35, color=BLUE_C)
        real.move_to(DOWN * 0.8)
        self.show(norm, real, run_time=1.1)
        self.at("star_action")
        self.hide(quotient, norm)
        self.play(real.animate.move_to(UP * 2.05), run_time=0.5)
        c_sum = formula(r"c(P)=\sum_{j=0}^{u^2-1}c_jP^j", size=40).move_to(UP * 0.7)
        star_sum = formula(r"c^*(P)=\sum_{j=0}^{u^2-1}c_jP^{-j}", size=40).move_to(
            DOWN * 0.65
        )
        self.show(c_sum, star_sum, run_time=1.1)
        self.at("reverse_at_one")
        c_at_one = formula(r"c(1)=\sum_{j=0}^{u^2-1}c_j\,1", size=40).move_to(c_sum)
        star_at_one = formula(r"c^*(1)=\sum_{j=0}^{u^2-1}c_j\,1", size=40).move_to(
            star_sum
        )
        self.play(
            Transform(c_sum, c_at_one), Transform(star_sum, star_at_one), run_time=1.4
        )
        self.at("real_unchanged")
        real_note = words(
            "Real coefficients are unchanged by conjugation", size=28, color=BLUE_C
        ).move_to(DOWN * 2.0)
        self.show(real_note, run_time=0.9)
        self.at("star_equal")
        same = formula(r"c^*(1)=c(1)", size=49, color=YELLOW).move_to(DOWN * 0.05)
        self.body.add(same)
        self.play(
            TransformFromCopy(VGroup(c_sum, star_sum), same),
            FadeOut(c_sum),
            FadeOut(star_sum),
            run_time=1.3,
        )
        self.body.remove(c_sum, star_sum)
        self.at("evaluated_norm")
        self.hide(real_note)
        norm_at_one = formula(r"c(1)c^*(1)=u^2", size=47).move_to(UP * 1.0)
        self.show(norm_at_one, run_time=0.8)
        square = formula(r"c(1)^2=u^2", size=49).move_to(norm_at_one)
        self.play(Transform(norm_at_one, square), run_time=1.1)
        self.at("two_values")
        self.hide(same)
        values = VGroup(
            formula(r"c(1)=u", size=47, color=YELLOW),
            formula(r"c(1)=-u", size=47, color=YELLOW),
        ).arrange(RIGHT, buff=2.2)
        values.move_to(DOWN * 1.0)
        self.body.add(values)
        self.play(TransformFromCopy(norm_at_one, values), run_time=1.2)
        self.at("real_matters")
        self.show(
            words("These are two real possibilities", size=29, color=BLUE_C).move_to(
                DOWN * 2.65
            ),
            run_time=0.9,
        )

        self.section("quotient", "Keep the unit denominator through the exact division")
        ring = formula(
            r"A=\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]", size=39, color=BLUE_C
        ).move_to(UP * 2.05)
        self.show(ring)
        self.at("denominator_unit")
        unit = formula(r"c(1)=\pm u\in A^\times", size=43, color=BLUE_C).move_to(
            UP * 0.85
        )
        self.show(unit, run_time=0.9)
        self.at("exact_quotient")
        exact = formula(r"\frac{J(1)}{c(1)}=\frac{u^2}{\pm u}", size=52).move_to(
            DOWN * 0.5
        )
        self.show(exact, run_time=1.0)
        self.at("exact_value")
        simplified = formula(
            r"\frac{J(1)}{c(1)}=\frac{u^2}{\pm u}=\pm u", size=51
        ).move_to(exact)
        self.play(Transform(exact, simplified), run_time=1.2)
        exact_note = words("Exact equality in A · before reduction", size=27).move_to(
            DOWN * 2.1
        )
        self.show(exact_note, run_time=0.8)
        self.at("positive_example")
        self.hide(unit, exact, exact_note)
        example = words("Exact example · u = 3", size=28, color=BLUE_C).move_to(
            UP * 1.15
        )
        positive = formula(r"\frac{9}{3}=3", size=54).move_to(LEFT * 3.15 + DOWN * 0.25)
        negative = formula(r"\frac{9}{-3}=-3", size=54).move_to(
            RIGHT * 3.15 + DOWN * 0.25
        )
        self.show(example, positive, run_time=1.0)
        self.at("negative_example")
        self.show(negative, run_time=1.0)
        self.at("take_residues")
        self.hide(example, positive, negative)
        residue_label = words("Now reduce modulo (1+i)A", size=29, color=BLUE_C)
        residue_label.move_to(UP * 0.95)
        plus = formula(r"u\equiv1", size=50).move_to(LEFT * 3.1 + DOWN * 0.25)
        minus = formula(r"-u\equiv-1=1", size=50).move_to(RIGHT * 3.1 + DOWN * 0.25)
        self.show(residue_label, plus, run_time=1.0)
        self.at("plus_minus")
        self.show(minus, run_time=1.0)
        self.at("empty_subset")
        self.hide(plus, minus, residue_label)
        border = Rectangle(width=10.6, height=3.55).set_stroke(BLUE_C, width=1.5)
        border.move_to(DOWN * 0.7)
        subset = formula(r"S=\varnothing,\qquad P=1", size=39, color=BLUE_C)
        subset.move_to(UP * 0.25)
        sign = formula(r"(-1)^{|S|}=+1", size=35).move_to(DOWN * 0.7)
        contribution = formula(
            r"\frac{J(1)}{c(1)}\equiv1\pmod{1+i}", size=48, color=YELLOW
        ).move_to(DOWN * 1.8)
        self.show(border, subset, sign, run_time=1.0)
        self.at("normalized_contribution")
        self.show(contribution, run_time=1.1)
