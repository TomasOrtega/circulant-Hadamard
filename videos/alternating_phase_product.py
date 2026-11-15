import json
from math import sqrt

from manimlib import (
    BLUE_B,
    BLUE_C,
    DOWN,
    LEFT,
    PI,
    RIGHT,
    UP,
    YELLOW,
    Arc,
    Arrow,
    Circle,
    FadeOut,
    Line,
    Rectangle,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


def subset_card(subset, evaluation, center, magnitude=False):
    frame = Rectangle(width=4.85, height=1.35).set_stroke(BLUE_C, width=1.5)
    label = formula(subset, size=28, color=BLUE_C).move_to(UP * 0.38)
    if magnitude:
        value = VGroup(
            formula(rf"|{evaluation}|=", size=32),
            formula("u", size=39, color=YELLOW),
        ).arrange(RIGHT, buff=0.15)
    else:
        value = formula(evaluation, size=35)
    value.move_to(DOWN * 0.25)
    return VGroup(frame, label, value).move_to(center)


def four_cards(magnitude=False):
    return VGroup(
        *(
            subset_card(subset, evaluation, center, magnitude)
            for subset, evaluation, center in [
                (r"\varnothing", "f(1)", LEFT * 3.3 + UP * 0.9),
                (r"\{p\}", r"f(\zeta_p)", RIGHT * 3.3 + UP * 0.9),
                (r"\{q\}", r"f(\zeta_q)", LEFT * 3.3 + DOWN * 1.15),
                (r"\{p,q\}", r"f(\zeta_p\zeta_q)", RIGHT * 3.3 + DOWN * 1.15),
            ]
        )
    )


class AlternatingPhaseProduct(NodeScene):
    node_id = "alternating-phase-product"
    title = "4.2 · The Alternating Phase Product"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def clear_body(self):
        self.play(FadeOut(self.body), run_time=0.4)
        self.body = VGroup()

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/alternating-phase-product.json").read_text()
        )["detail_cues"]

        self.section("example", "Cancel the lengths and retain the relative angle")
        self.show(
            formula(r"f(P)f^*(P)=u^2,\qquad u>1\text{ odd}", size=42).move_to(UP * 1.9)
        )
        quotient = formula(r"u=3:\qquad\Delta(f)=\frac{f(1)}{f(\omega)}", size=55)
        quotient.move_to(UP * 0.15)
        self.at("one_prime")
        self.show(quotient)
        self.show(
            formula(r"\omega=e^{2\pi i/3},\qquad|f(1)|=|f(\omega)|=3", size=37).move_to(
                DOWN * 1.65
            )
        )
        self.at("actual_example")
        self.clear_body()
        self.show(
            formula(r"f(P)=3iP,\qquad f(P)f^*(P)=9", size=44, color=BLUE_C).move_to(
                UP * 2.1
            )
        )
        left, right = LEFT * 3.9 + DOWN * 0.2, RIGHT * 3.7 + DOWN * 0.2
        self.show(
            Circle(radius=1.6).move_to(left).set_stroke(BLUE_C, width=2),
            Circle(radius=1.4).move_to(right).set_stroke(BLUE_C, width=2),
        )
        numerator = Arrow(left, left + UP * 1.6, buff=0).set_color(BLUE_C)
        denominator = Arrow(
            left, left + LEFT * 0.8 * sqrt(3) + DOWN * 0.8, buff=0
        ).set_color(BLUE_B)
        self.show(
            numerator,
            denominator,
            formula("3i", size=35, color=BLUE_C).next_to(
                numerator.get_end(), UP, buff=0.15
            ),
            formula(r"3i\omega", size=33, color=BLUE_B).next_to(
                denominator.get_end(), LEFT, buff=0.15
            ),
            words("Values · magnitude 3", size=26).move_to(LEFT * 3.9 + DOWN * 2.5),
        )
        ratio = Arrow(
            right, right + LEFT * 0.7 + DOWN * 0.7 * sqrt(3), buff=0
        ).set_color(YELLOW)
        self.at("example_ratio")
        self.show(
            ratio,
            formula(r"\Delta(f)=\omega^{-1}", size=39, color=YELLOW).move_to(
                RIGHT * 4.2 + UP * 1.65
            ),
            formula(r"\frac{3}{3}=1", size=49).move_to(RIGHT * 3.7 + DOWN * 2.55),
        )
        self.at("relative_angle")
        self.show(
            Arc(start_angle=7 * PI / 6, angle=-2 * PI / 3, radius=0.65)
            .shift(left)
            .set_color(YELLOW),
            Arc(start_angle=0, angle=-2 * PI / 3, radius=0.65)
            .shift(right)
            .set_color(YELLOW),
            words("One norm-solution example", size=25).move_to(DOWN * 3.5),
        )

        self.section("subsets", "Use each distinct prime dividing u")
        self.show(
            formula(
                r"I=\{p:p\mid u\},\qquad I\ne\varnothing", size=46, color=BLUE_C
            ).move_to(UP * 1.8)
        )
        self.at("choose_roots")
        self.show(
            formula(
                r"\zeta_p\text{ primitive of order }p\quad(p\in I)", size=41
            ).move_to(UP * 0.5)
        )
        self.at("subset_input")
        self.show(
            formula(
                r"\zeta_S=\prod_{p\in S}\zeta_p,\qquad\zeta_\varnothing=1",
                size=47,
                color=YELLOW,
            ).move_to(DOWN * 1.1)
        )
        self.at("allowed_input")
        self.show(
            formula(
                r"\operatorname{ord}(\zeta_S)\mid\prod_{p\in I}p\mid u^2", size=38
            ).move_to(DOWN * 2.75),
            words("Every subset gives an allowed input", size=25).move_to(DOWN * 3.6),
        )

        self.section("product", "Even subsets above; odd subsets below")
        definition = formula(
            r"\Delta(f)=\prod_{S\subseteq I}f(\zeta_S)^{(-1)^{|S|}}",
            size=49,
            color=BLUE_C,
        )
        definition.move_to(UP * 1.1)
        self.show(definition)
        roles = VGroup(
            words("even → numerator", size=29).move_to(LEFT * 3.4 + DOWN * 0.5),
            words("odd → denominator", size=29).move_to(RIGHT * 3.4 + DOWN * 0.5),
        )
        self.show(roles)
        self.at("two_primes")
        self.play(
            FadeOut(roles),
            definition.animate.scale(0.7).move_to(UP * 2.25),
            run_time=0.65,
        )
        self.body.remove(roles)
        cards = four_cards()
        self.show(cards, run_time=1.2)
        self.at("fraction_roles")
        self.play(
            cards[0].animate.move_to(LEFT * 3.3 + UP * 0.9),
            cards[3].animate.move_to(RIGHT * 3.3 + UP * 0.9),
            cards[1].animate.move_to(LEFT * 3.3 + DOWN * 1.15),
            cards[2].animate.move_to(RIGHT * 3.3 + DOWN * 1.15),
            run_time=1.8,
        )
        self.show(
            Line(LEFT * 6.1 + DOWN * 0.13, RIGHT * 6.1 + DOWN * 0.13).set_stroke(
                YELLOW, width=2
            )
        )
        self.show(
            formula(
                r"\Delta(f)=\frac{f(1)f(\zeta_p\zeta_q)}{f(\zeta_p)f(\zeta_q)}",
                size=41,
                color=YELLOW,
            ).move_to(DOWN * 2.95)
        )

        self.section(
            "pairing", "Toggle p · two-prime illustration of the general pairing"
        )
        cards = four_cards(magnitude=True)
        cards[3].move_to(RIGHT * 3.3 + UP * 0.9)
        cards[1].move_to(LEFT * 3.3 + DOWN * 1.15)
        cards[2].move_to(RIGHT * 3.3 + DOWN * 1.15)
        self.show(cards)
        self.at("toggle")
        connectors = VGroup(
            *(
                Line(RIGHT * x + UP * 0.2, RIGHT * x + DOWN * 0.45).set_stroke(
                    YELLOW, width=3
                )
                for x in (-3.3, 3.3)
            )
        )
        self.show(
            connectors,
            words("toggle p", size=24, color=YELLOW).move_to(LEFT * 4.5 + DOWN * 0.1),
            words("toggle p", size=24, color=YELLOW).move_to(RIGHT * 4.5 + DOWN * 0.1),
        )
        self.at("equal_counts")
        self.show(
            formula(
                r"r=|I|\ge1:\quad\#\text{even}=\#\text{odd}=2^{r-1}",
                size=34,
                color=BLUE_C,
            ).move_to(UP * 2.3)
        )
        self.at("cancel_magnitudes")
        strikes = VGroup(
            *(
                Line(
                    card[2][1].get_corner(LEFT + DOWN),
                    card[2][1].get_corner(RIGHT + UP),
                )
                for card in cards
            )
        ).set_stroke(YELLOW, width=3)
        self.show(strikes, run_time=0.8)
        self.show(
            formula(
                r"|\Delta(f)|=\frac{u^{2^{r-1}}}{u^{2^{r-1}}}=1", size=48, color=YELLOW
            ).move_to(DOWN * 3.05)
        )

        self.section("nonzero", "The norm makes every denominator nonzero")
        norm = formula(
            r"f(\zeta_S)\overline{f(\zeta_S)}=u^2", size=54, color=BLUE_C
        ).move_to(UP * 1.5)
        self.show(norm)
        self.at("nonzero_conclusion")
        self.show(
            formula(
                r"u>0\quad\Longrightarrow\quad f(\zeta_S)\ne0", size=49, color=YELLOW
            ).move_to(DOWN * 0.1),
            words(
                "Every division is between nonzero algebraic numbers", size=27
            ).move_to(DOWN * 1.65),
            words(
                "Arithmetic reduction has not been used", size=25, color=BLUE_C
            ).move_to(DOWN * 2.9),
        )

        self.section("conjugates", "Apply the embedding to coefficients and inputs")
        roots = formula(
            r"i,\ \zeta_p\quad\longmapsto\quad\sigma(i),\ \sigma(\zeta_p)",
            size=43,
            color=BLUE_C,
        ).move_to(UP * 1.7)
        self.show(roots)
        self.at("coefficients_too")
        self.show(
            words("σ acts on the whole roots-of-unity field", size=27).move_to(UP * 0.7)
        )
        self.at("commutes_conjugation")
        inversion = formula(
            r"\sigma(\zeta^{-1})=\sigma(\zeta)^{-1}=\overline{\sigma(\zeta)}", size=43
        )
        inversion.move_to(DOWN * 0.5)
        self.show(inversion)
        self.at("conjugate_norm")
        self.clear_body()
        norm_image = formula(
            r"\sigma(f(\zeta_S))\overline{\sigma(f(\zeta_S))}=u^2",
            size=49,
            color=BLUE_C,
        ).move_to(UP * 1.55)
        self.show(norm_image)
        self.show(
            formula(r"|\sigma(f(\zeta_S))|=u", size=49, color=YELLOW).move_to(UP * 0.05)
        )
        self.at("conjugate_delta")
        self.show(
            formula(r"\boxed{|\sigma(\Delta(f))|=1}", size=57, color=YELLOW).move_to(
                DOWN * 1.55
            ),
            words(
                "The same even–odd pairing works for every embedding", size=25
            ).move_to(DOWN * 3),
        )

        self.section(
            "handoff", "One Kronecker hypothesis is ready; integrality is next"
        )
        self.show(
            formula(
                r"|\sigma(\Delta(f))|=1\quad\text{for every }\sigma",
                size=48,
                color=YELLOW,
            ).move_to(UP * 1.35),
            words("All conjugates lie on the unit circle", size=30).move_to(UP * 0.15),
        )
        self.at("integral_pending")
        self.show(
            words(
                "Next: prove Δ(f) is an algebraic integer", size=31, color=BLUE_C
            ).move_to(DOWN * 1.45),
            words(
                "A quotient of algebraic integers needs this separate proof", size=25
            ).move_to(DOWN * 2.95),
        )
