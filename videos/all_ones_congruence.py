import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    FadeOut,
    FlashAround,
    SurroundingRectangle,
    Transform,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class AllOnesCongruence(NodeScene):
    node_id = "all-ones-congruence"
    title = "5.3 · All coefficients become 1"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def erase(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.4)
        self.body.remove(*objects)

    def change_subtitle(self, cue, title):
        self.wait_until_narration(self.cues[cue])
        self.play(
            Transform(
                self.subtitle,
                words(title, size=25, color=BLUE_C).next_to(
                    self.heading, DOWN, buff=0.25
                ),
            ),
            run_time=0.35,
        )

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/all-ones-congruence.json").read_text()
        )["detail_cues"]

        self.section("inputs", "Start with an exact identity for any positive u")
        self.show(
            formula(r"u\in\mathbb Z_{>0}", size=42, color=BLUE_C).move_to(UP * 2.05),
            run_time=0.8,
        )
        prefix = formula(r"E(P)=-H_3(P)+", size=43)
        factor = formula("(i-1)", size=43, color=YELLOW)
        half = formula(r"\frac{H_1(P)+H_2(P)}2", size=43, color=BLUE_C)
        exact = (
            VGroup(prefix, factor, half).arrange(RIGHT, buff=0.45).move_to(UP * 0.35)
        )
        if exact.get_width() > 12:
            exact.set_width(12)
        self.at("input_exact")
        self.show(exact, run_time=1.2)
        self.at("input_integral")
        self.show(
            SurroundingRectangle(half, buff=0.18).set_stroke(YELLOW, 2),
            words(
                "The half-sum has integer coefficients", size=29, color=BLUE_C
            ).move_to(DOWN * 1.45),
            run_time=0.9,
        )

        self.section("discard_term", "Factor out 1 + i, then reduce coefficients")
        self.show(
            formula(r"i-1=i(1+i)", size=48, color=YELLOW).move_to(UP * 2.05),
            run_time=0.9,
        )
        remaining = formula(r"E(P)=-H_3(P)+", size=43)
        divisible = VGroup(
            formula(r"i(1+i)", size=43, color=YELLOW),
            formula(r"\frac{H_1(P)+H_2(P)}2", size=43, color=BLUE_C),
        ).arrange(RIGHT, buff=0.25)
        factored = (
            VGroup(remaining, divisible).arrange(RIGHT, buff=0.4).move_to(UP * 0.25)
        )
        if factored.get_width() > 12:
            factored.set_width(12)
        self.show(factored, run_time=1.2)
        self.at("discard_vanish")
        reduction = words(
            "Reduce coefficients modulo 1 + i", size=29, color=YELLOW
        ).move_to(DOWN * 1.25)
        self.show(reduction, run_time=0.8)
        self.play(FadeOut(divisible), run_time=0.7)
        factored.remove(divisible)
        self.play(
            Transform(
                remaining,
                formula(r"E(P)\equiv-H_3(P)\pmod{1+i}", size=48, color=YELLOW).move_to(
                    UP * 0.25
                ),
            ),
            run_time=1,
        )
        self.at("discard_before")
        self.show(
            words(
                "Form integral quotients first → reduce coefficients second", size=27
            ).move_to(DOWN * 2.65),
            run_time=0.9,
        )

        self.section("every_coefficient", "Both possible signs have residue 1")
        sign_polynomial = formula(
            r"H_3(P)=\sum_{r=0}^{u^2-1}h_{3,r}P^r", size=47, color=BLUE_C
        ).move_to(UP * 1.8)
        self.show(sign_polynomial, run_time=1.1)
        self.at("coefficient_signs")
        signs = formula(r"h_{3,r}\in\{-1,1\}", size=44).move_to(UP * 0.55)
        self.show(signs, run_time=0.8)
        self.at("coefficient_both")
        residues = formula(
            r"-1\equiv1,\qquad +1\equiv1\pmod{1+i}", size=45, color=YELLOW
        ).move_to(DOWN * 0.8)
        self.show(residues, run_time=1)
        self.at("coefficient_j")
        self.erase(sign_polynomial, signs, residues)
        congruence = formula(
            r"E(P)\equiv J(P)\pmod{1+i}", size=53, color=YELLOW
        ).move_to(UP * 1.5)
        self.show(
            congruence,
            formula(r"J(P):=\sum_{r=0}^{u^2-1}P^r", size=49, color=BLUE_C).move_to(
                UP * 0.1
            ),
            run_time=1.1,
        )
        self.at("coefficient_difference")
        self.show(
            words(
                "Every coefficient of E(P) − J(P) is divisible by 1 + i", size=27
            ).move_to(DOWN * 1.35),
            run_time=0.9,
        )
        self.at("coefficient_scope")
        self.show(
            words(
                "Any positive u · common signs · no norm identity needed",
                size=27,
                color=BLUE_C,
            ).move_to(DOWN * 2.6),
            run_time=0.9,
        )

        self.section(
            "nine_positions", "An illustrative sign row; every power stays fixed"
        )
        example_title = formula(
            r"u=3:\quad-H_3(P)\text{ has nine positions}", size=40, color=BLUE_C
        ).move_to(UP * 2.05)
        self.show(example_title, run_time=0.9)
        positions = [1.275 * (r - 4) for r in range(9)]
        sample_signs = [1, -1, 1, 1, -1, -1, 1, -1, 1]
        coefficients = VGroup(
            *(
                formula(str(sign), size=40, color=BLUE_C).move_to(RIGHT * x + UP * 0.55)
                for sign, x in zip(sample_signs, positions, strict=True)
            )
        )
        powers = VGroup(
            *(
                formula(
                    "1" if r == 0 else "P" if r == 1 else rf"P^{r}", size=34
                ).move_to(RIGHT * x + DOWN * 0.5)
                for r, x in enumerate(positions)
            )
        )
        coefficient_label = words("coefficient", size=22).move_to(
            LEFT * 7.2 + UP * 0.55
        )
        power_label = words("power", size=22).move_to(LEFT * 7.2 + DOWN * 0.5)
        self.at("nine_row")
        self.show(coefficients, coefficient_label, run_time=1)
        self.at("nine_powers")
        self.show(powers, power_label, run_time=1)
        self.at("nine_reduce")
        self.play(
            *(
                Transform(
                    coefficient,
                    formula("1", size=40, color=YELLOW).move_to(coefficient),
                )
                for coefficient in coefficients
            ),
            run_time=1.4,
        )
        warning = words(
            "These are residues; the original coefficients need not equal 1", size=27
        ).move_to(DOWN * 2.25)
        self.at("nine_warning")
        self.show(warning, run_time=1)

        self.change_subtitle("at_one", "Now evaluate J(P) at P = 1")
        self.erase(warning)
        self.play(
            Transform(
                example_title,
                formula(r"u=3,\qquad P=1", size=43, color=BLUE_C).move_to(
                    example_title
                ),
            ),
            run_time=0.8,
        )
        self.at("one_powers")
        self.play(
            *(
                Transform(power, formula("1", size=34, color=YELLOW).move_to(power))
                for power in powers
            ),
            run_time=1.1,
        )
        self.at("one_count")
        self.erase(powers, power_label, coefficient_label)
        self.play(
            *(
                coefficient.animate.move_to(RIGHT * x + DOWN * 0.3)
                for coefficient, x in zip(coefficients, positions, strict=True)
            ),
            run_time=0.8,
        )
        pluses = VGroup(
            *(
                formula("+", size=26, color=BLUE_C).move_to(
                    RIGHT * ((a + b) / 2) + DOWN * 0.3
                )
                for a, b in zip(positions[:-1], positions[1:], strict=True)
            )
        )
        count = formula(
            r"E(1)\equiv J(1)=u^2\pmod{1+i}", size=45, color=BLUE_C
        ).move_to(UP * 1.05)
        self.show(pluses, count, run_time=1)
        distinction = words(
            "Evaluation at one follows the coefficient congruence", size=27
        ).move_to(DOWN * 2.25)
        self.at("one_distinct")
        self.show(distinction, run_time=0.9)

        self.change_subtitle(
            "odd_pairing", "Oddness is used here, after the coefficient result"
        )
        self.play(
            Transform(
                example_title,
                words("Now assume u is odd", size=32, color=YELLOW).move_to(
                    example_title
                ),
            ),
            run_time=0.8,
        )
        self.at("odd_nine")
        self.erase(distinction)
        paired = list(coefficients)[:8]
        rectangles = VGroup(
            *(
                SurroundingRectangle(
                    VGroup(coefficients[r], coefficients[r + 1]), buff=0.16
                ).set_stroke(BLUE_C, 2)
                for r in range(0, 8, 2)
            )
        )
        zeros = VGroup(
            *(
                formula(r"2\equiv0", size=31, color=BLUE_C).move_to(
                    RIGHT * ((positions[r] + positions[r + 1]) / 2) + DOWN * 1.3
                )
                for r in range(0, 8, 2)
            )
        )
        self.show(rectangles, zeros, run_time=1.1)
        self.play(
            FadeOut(VGroup(*paired)),
            FadeOut(pluses),
            FadeOut(rectangles),
            FadeOut(zeros),
            run_time=0.8,
        )
        coefficients.remove(*paired)
        self.body.remove(pluses, rectangles, zeros)
        self.play(coefficients[0].animate.move_to(DOWN * 0.3), run_time=0.8)
        self.at("odd_general")
        self.play(
            Transform(
                example_title,
                formula(r"u^2=2k+1,\qquad k\ge0", size=43, color=YELLOW).move_to(
                    example_title
                ),
            ),
            run_time=0.8,
        )
        self.show(
            formula(r"J(1)=\sum_{j=1}^{k}(1+1)+1=2k+1\equiv1", size=42).move_to(
                DOWN * 1.85
            ),
            run_time=1.1,
        )
        self.at("odd_finish")
        self.play(
            Transform(
                count,
                formula(r"E(1)\equiv1\pmod{1+i}", size=53, color=YELLOW).move_to(count),
            ),
            run_time=1,
        )
        self.play(FlashAround(count, color=YELLOW), run_time=0.7)

        self.section(
            "carry_forward", "Keep the coefficient result and the exact divisibilities"
        )
        self.show(
            formula(
                r"E(P)\equiv J(P)=\sum_{r=0}^{u^2-1}P^r\pmod{1+i}",
                size=45,
                color=YELLOW,
            ).move_to(UP * 1.6),
            run_time=1.1,
        )
        self.at("carry_two")
        self.show(
            formula(r"2\mid d(P)-c(P)", size=46, color=BLUE_C).move_to(UP * 0.1),
            run_time=0.9,
        )
        self.at("carry_pi")
        self.show(
            formula(r"1+i\mid g(P)-c(P)", size=46, color=BLUE_C).move_to(DOWN * 1.2),
            run_time=0.9,
        )
        self.at("carry_later")
        note = words(
            "Exact coefficientwise divisibility → later sign comparisons", size=26
        ).move_to(DOWN * 2.6)
        self.show(note, run_time=0.9)
        self.at("carry_final")
        self.play(
            Transform(
                note,
                words(
                    "The all-ones congruence enters the final additive contradiction",
                    size=26,
                ).move_to(note),
            ),
            run_time=1,
        )
