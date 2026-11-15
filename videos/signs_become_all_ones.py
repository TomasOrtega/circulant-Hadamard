import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    Arrow,
    FadeOut,
    FlashAround,
    Line,
    SurroundingRectangle,
    Transform,
    VGroup,
    Write,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class SignsBecomeAllOnes(NodeScene):
    node_id = "signs-become-all-ones"
    title = "5 · Signs Become All Ones"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def sign_polynomial_row(self, label, signs, position):
        terms = VGroup(
            *(
                formula(sign + rf"H_{index}(P)", size=34, color=BLUE_C)
                for index, sign in enumerate(signs)
            )
        )
        row = VGroup(formula(label, size=34), *terms).arrange(RIGHT, buff=0.15)
        row.move_to(position)
        return row, terms

    def monomials(self, signed=False):
        powers = ["1", "P", *(f"P^{index}" for index in range(2, 9))]
        terms = VGroup(
            *(
                formula(
                    (r"\pm " if signed else ("+" if index else "")) + power,
                    size=36,
                    color=BLUE_C,
                )
                for index, power in enumerate(powers)
            )
        )
        return terms.arrange(RIGHT, buff=0.22).set_width(12)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/signs-become-all-ones.json").read_text()
        )["detail_cues"]

        self.section("goal", "Use the common origin of c(P), d(P), and g(P)")
        sources = (
            VGroup(
                *(
                    formula(rf"H_{index}(P)", size=43, color=BLUE_C)
                    for index in range(4)
                )
            )
            .arrange(RIGHT, buff=0.7)
            .move_to(UP * 1.7)
        )
        descendants = formula(r"c(P),\quad d(P),\quad g(P)", size=49)
        descendants.move_to(UP * 0.1)
        arrows = VGroup(
            *(
                Arrow(source.get_bottom(), descendants.get_top(), buff=0.2).set_color(
                    BLUE_C
                )
                for source in sources
            )
        )
        self.show(descendants)
        self.at("goal_signs")
        self.show(sources, arrows)
        self.show(
            words("Each H-polynomial has sign coefficients.", size=24).move_to(
                UP * 2.35
            )
        )
        self.at("goal_target")
        self.show(
            formula(
                r"E(P)\equiv J(P)=1+P+\cdots+P^8\pmod{1+i}", size=44, color=YELLOW
            ).move_to(DOWN * 1.7)
        )

        self.section("connection", "One expression connects the two proof branches")
        comparisons = formula(r"c(P),\ d(P),\ g(P)", size=50, color=BLUE_C)
        comparisons.move_to(LEFT * 4 + UP * 0.5)
        origin = formula(r"H_0(P),\ldots,H_3(P)", size=47, color=BLUE_C)
        origin.move_to(RIGHT * 4 + UP * 0.5)
        middle = formula(r"E(P)", size=66, color=YELLOW).move_to(UP * 0.5)
        self.show(comparisons, origin, middle)
        self.show(
            Arrow(comparisons.get_right(), middle.get_left(), buff=0.3).set_color(
                BLUE_C
            ),
            Arrow(origin.get_left(), middle.get_right(), buff=0.3).set_color(BLUE_C),
            words("Later comparisons", size=27).move_to(LEFT * 4 + DOWN * 0.8),
            words("Coefficient residues", size=27).move_to(RIGHT * 4 + DOWN * 0.8),
        )
        self.wait_until_narration(self.cues["definition"])
        self.play(FadeOut(self.body), run_time=0.4)
        self.body = VGroup()
        first_difference = formula(r"d(P)-c(P)", size=54, color=BLUE_C)
        second_difference = formula(r"g(P)-c(P)", size=54, color=BLUE_C)
        differences = VGroup(first_difference, second_difference)
        differences.arrange(RIGHT, buff=2.1).move_to(UP * 0.3)
        self.show(differences)
        self.at("definition_divide")
        definition = formula(
            r"E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}",
            size=56,
            color=YELLOW,
        )
        self.play(Transform(differences, definition), run_time=1.5)

        self.section(
            "first_quotient", "Subtract the c(P) formula from the d(P) formula"
        )
        reference = formula(
            r"E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}",
            size=27,
        ).move_to(UP * 2.25)
        d_row, d_terms = self.sign_polynomial_row(
            r"2d(P)=", ["", "-", "+", "-"], UP * 1
        )
        c_row, c_terms = self.sign_polynomial_row(
            r"2c(P)=", ["", "+", "+", "+"], DOWN * 0.4
        )
        subtraction = formula("-", size=50).next_to(c_row, LEFT, buff=0.35)
        rule = Line(
            c_row.get_left() + DOWN * 0.6,
            c_row.get_right() + DOWN * 0.6,
        ).set_stroke(BLUE_C, width=1.5)
        self.show(reference, d_row, c_row, subtraction, rule)
        strikes = VGroup(
            *(
                Line(
                    term.get_corner(LEFT + DOWN), term.get_corner(RIGHT + UP)
                ).set_stroke(YELLOW, width=3)
                for terms in [d_terms, c_terms]
                for term in [terms[0], terms[2]]
            )
        )
        self.at("first_cancel")
        self.body.add(strikes)
        self.play(Write(strikes), run_time=0.9)
        first_rhs = formula(r"-\frac{H_1(P)+H_3(P)}2", size=45)
        first_quotient = (
            VGroup(
                formula(r"\frac{d(P)-c(P)}2=", size=45),
                first_rhs,
            )
            .arrange(RIGHT, buff=0.2)
            .move_to(DOWN * 2)
        )
        self.at("first_result")
        self.show(first_quotient)

        self.wait_until_narration(self.cues["second_quotient"])
        self.play(
            FadeOut(d_row),
            FadeOut(c_row),
            FadeOut(strikes),
            FadeOut(subtraction),
            FadeOut(rule),
            run_time=0.4,
        )
        self.body.remove(d_row, c_row, strikes, subtraction, rule)
        self.play(first_quotient.animate.scale(0.83).move_to(UP), run_time=0.7)
        second_real = formula(r"-\frac{H_2(P)+H_3(P)}2", size=38)
        second_imag = formula(r"i\frac{H_1(P)+H_2(P)}2", size=38)
        second_quotient = (
            VGroup(
                formula(r"\frac{g(P)-c(P)}{1+i}=", size=38),
                second_real,
                formula("+", size=38),
                second_imag,
            )
            .arrange(RIGHT, buff=0.16)
            .move_to(DOWN * 0.6)
        )
        if second_quotient.get_width() > 12:
            second_quotient.set_width(12)
        self.show(second_quotient)
        self.wait_until_narration(self.cues["integral"])
        highlights = VGroup(
            *(
                SurroundingRectangle(term, buff=0.13).set_color(YELLOW)
                for term in [first_rhs, second_real, second_imag]
            )
        )
        self.show(highlights)
        self.show(
            words("Each half-sum has integer coefficients.", size=28).move_to(DOWN * 2)
        )

        self.section("combine", "Collect the two halves of −H₃(P)")
        halves = VGroup(
            formula(r"-\frac{H_3(P)}2", size=48, color=YELLOW),
            formula(r"-\frac{H_3(P)}2", size=48, color=YELLOW),
        ).arrange(RIGHT, buff=0.12)
        top = VGroup(formula(r"E(P)=", size=48), halves)
        top.arrange(RIGHT, buff=0.2)
        remaining = formula(
            r"-\frac{H_1(P)+H_2(P)}2+i\frac{H_1(P)+H_2(P)}2",
            size=45,
        )
        combined = VGroup(top, remaining).arrange(DOWN, buff=0.65)
        combined.move_to(DOWN * 0.1)
        self.show(combined)
        self.at("combine_halves")
        self.play(
            Transform(
                halves, formula(r"-H_3(P)", size=48, color=YELLOW).move_to(halves)
            ),
            run_time=1.2,
        )
        self.at("combine_factor")
        self.play(
            Transform(
                remaining,
                formula(r"+(i-1)\frac{H_1(P)+H_2(P)}2", size=45, color=BLUE_C).move_to(
                    remaining
                ),
            ),
            run_time=1.4,
        )
        self.at("combine_result")
        self.play(
            Transform(
                combined,
                formula(
                    r"E(P)=-H_3(P)+(i-1)\frac{H_1(P)+H_2(P)}2",
                    size=53,
                    color=YELLOW,
                ),
            ),
            run_time=1.5,
        )

        self.section("factor", "Reduce coefficients modulo 1 + i")
        lhs = formula(r"E(P)=", size=47)
        survivor = formula(r"-H_3(P)", size=47, color=BLUE_C)
        factor = formula(r"(i-1)\frac{H_1(P)+H_2(P)}2", size=47)
        identity = VGroup(lhs, survivor, formula("+", size=47), factor)
        identity.arrange(RIGHT, buff=0.18).move_to(UP * 0.9)
        self.show(identity)
        factor_identity = formula(r"i-1=i(1+i)", size=53, color=YELLOW)
        factor_identity.move_to(DOWN * 1.1)
        self.at("factor_identity")
        self.show(factor_identity)
        self.at("factor_vanish")
        self.play(
            Transform(
                factor,
                formula(
                    r"i(1+i)\frac{H_1(P)+H_2(P)}2",
                    size=47,
                    color=YELLOW,
                ).move_to(factor),
            ),
            run_time=0.8,
        )
        congruence = formula(
            r"E(P)\equiv-H_3(P)\pmod{1+i}", size=53, color=BLUE_C
        ).move_to(UP * 0.9)
        self.play(
            Transform(identity, congruence), FadeOut(factor_identity), run_time=1.3
        )
        self.body.remove(factor_identity)

        self.wait_until_narration(self.cues["signs"])
        self.play(identity.animate.move_to(UP * 1.8), run_time=0.7)
        positive = formula("+1", size=64, color=BLUE_C).move_to(LEFT * 2 + UP * 0.1)
        negative = formula("-1", size=64, color=BLUE_C).move_to(RIGHT * 2 + UP * 0.1)
        one = formula("1", size=69, color=YELLOW).move_to(DOWN * 1.2)
        self.show(positive, negative)
        self.at("sign_factor")
        self.show(formula(r"2=(1+i)(1-i)", size=43).move_to(DOWN * 2.4))
        self.at("sign_merge")
        self.show(
            Arrow(positive.get_bottom(), one.get_top(), buff=0.18).set_color(BLUE_C),
            Arrow(negative.get_bottom(), one.get_top(), buff=0.18).set_color(BLUE_C),
            one,
        )

        self.section("all_ones", "Keep the powers fixed; replace every coefficient")
        self.show(formula(r"E(P)\equiv-H_3(P)\pmod{1+i}", size=47).move_to(UP * 1.7))
        terms = self.monomials(signed=True).move_to(DOWN * 0.1)
        self.show(terms)
        powers = ["1", "P", *(f"P^{index}" for index in range(2, 9))]
        self.play(
            *(
                Transform(
                    term,
                    formula(
                        ("+" if index else "") + power, size=36, color=YELLOW
                    ).move_to(term),
                )
                for index, (term, power) in enumerate(zip(terms, powers, strict=True))
            ),
            run_time=2,
        )
        self.at("all_ones_result")
        self.play(terms.animate.set_color(BLUE_C), run_time=0.5)
        self.show(
            formula(
                r"E(P)\equiv J(P)=1+P+\cdots+P^8\pmod{1+i}", size=44, color=YELLOW
            ).move_to(DOWN * 1.9)
        )

        self.section("at_one", "Evaluate at 1: pair eight of the nine ones")
        top_label = formula(r"E(1)\equiv J(1)\pmod{1+i}", size=48, color=BLUE_C)
        top_label.move_to(UP * 1.7)
        powers = self.monomials().move_to(UP * 0.1)
        pairs = VGroup(*(VGroup(*powers[i : i + 2]) for i in range(0, 8, 2)), powers[8])
        self.show(top_label, pairs)
        self.at("at_one_replace")
        self.play(
            *(
                Transform(
                    term,
                    formula("+1" if index else "1", size=36, color=BLUE_C).move_to(
                        term
                    ),
                )
                for index, term in enumerate(powers)
            ),
            run_time=1.5,
        )
        pair_boxes = VGroup(
            *(
                SurroundingRectangle(pair, buff=0.15).set_color(YELLOW)
                for pair in pairs[:4]
            )
        )
        self.at("at_one_pair")
        self.show(pair_boxes, run_time=0.6)
        self.at("at_one_two")
        self.play(
            *(
                Transform(pair, formula("2", size=49, color=YELLOW).move_to(pair))
                for pair in pairs[:4]
            ),
            run_time=1.2,
        )
        self.at("at_one_zero")
        self.play(
            *(
                Transform(pair, formula("0", size=43).move_to(pair))
                for pair in pairs[:4]
            ),
            FadeOut(pair_boxes),
            run_time=0.8,
        )
        self.body.remove(pair_boxes)
        self.play(*(pair.animate.set_opacity(0.15) for pair in pairs[:4]), run_time=0.5)
        self.at("at_one_survivor")
        self.play(FlashAround(pairs[4], color=YELLOW), run_time=0.8)
        self.at("at_one_result")
        self.show(
            formula(
                r"E(1)\equiv J(1)=9\equiv1\pmod{1+i}", size=51, color=YELLOW
            ).move_to(DOWN * 1.9)
        )

        self.section("general", "An odd number of terms leaves residue 1")
        self.show(formula(r"u\text{ odd}", size=58, color=BLUE_C).move_to(UP * 1.6))
        self.at("general_count")
        count = formula(r"J(1)=\underbrace{1+\cdots+1}_{u^2\text{ terms}}=u^2", size=52)
        self.show(count)
        self.at("general_result")
        result = formula(
            r"E(1)\equiv J(1)=u^2\equiv1\pmod{1+i}", size=57, color=YELLOW
        ).move_to(DOWN * 1.8)
        self.show(result)
        self.play(FlashAround(result, color=YELLOW), run_time=0.8)
