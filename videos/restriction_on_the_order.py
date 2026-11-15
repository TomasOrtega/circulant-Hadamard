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
    Transform,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, sign_matrix, words


class RestrictionOnTheOrder(NodeScene):
    node_id = "restriction-on-the-order"
    title = "2 · Restriction on the Order"

    def at(self, name):
        self.wait_until_narration(self.animation_cues[name])

    def present(self):
        production = ROOT / "videos/production/restriction-on-the-order.json"
        self.animation_cues = json.loads(production.read_text())["animation_cues"]
        self.section("goal", "Three restrictions on the possible order")
        assumptions = formula(r"H\text{ circulant Hadamard},\qquad n>1", size=42)
        assumptions.move_to(UP * 1.7)
        self.show(assumptions)
        steps = (
            VGroup(
                formula(r"n=m^2", size=52, color=BLUE_C),
                formula(r"m=2u", size=52, color=BLUE_C),
                formula(r"u\text{ odd}", size=52, color=BLUE_C),
            )
            .arrange(RIGHT, buff=1)
            .move_to(UP * 0.2)
        )
        for step in steps:
            self.show(step, run_time=0.7)
            self.play(FlashAround(step, color=YELLOW), run_time=0.4)
        goal = formula(
            r"\boxed{n=4u^2,\quad u\text{ a positive odd integer}}",
            size=48,
            color=YELLOW,
        ).move_to(DOWN * 1.2)
        self.show(goal)

        self.section("encoding", "Remember the polynomial identity")
        polynomial = VGroup(
            *(
                formula(term, size=40, color=BLUE_C)
                for term in [r"h_0", r"h_1", r"\cdots", r"h_{n-1}"]
            )
        )
        polynomial.arrange(RIGHT, buff=0.8).move_to(UP * 1.6)
        self.show(polynomial)
        target = formula(
            r"h(X)=h_0+h_1X+\cdots+h_{n-1}X^{n-1}", size=44, color=BLUE_C
        ).move_to(UP * 1.4)
        self.play(Transform(polynomial, target), run_time=1.5)
        self.show(formula(r"h_j=\pm1,\qquad X^n=1", size=36).move_to(UP * 0.2))
        self.at("star_appears")
        star = formula(
            r"h^*(X)=h_0+h_1X^{-1}+\cdots+h_{n-1}X^{-(n-1)}", size=42
        ).move_to(DOWN * 0.85)
        self.show(star)
        self.at("identity_appears")
        self.show(formula(r"h(X)h^*(X)=n", size=55, color=YELLOW).move_to(DOWN * 2))

        self.section("square", "Evaluate at one: the order is a square")
        h = formula(
            r"h(X)=h_0+h_1X+\cdots+h_{n-1}X^{n-1}", size=42, color=BLUE_C
        ).move_to(UP * 1.55)
        star = formula(
            r"h^*(X)=h_0+h_1X^{-1}+\cdots+h_{n-1}X^{-(n-1)}", size=42
        ).move_to(UP * 0.45)
        self.show(h, star)
        evaluation = formula(r"X\longmapsto1", size=48, color=YELLOW)
        evaluation.move_to(DOWN * 0.55)
        self.show(evaluation)
        self.at("powers_become_one")
        self.play(
            Transform(
                h,
                formula(
                    r"h(1)=h_0+h_1\cdot1+\cdots+h_{n-1}\cdot1", size=42, color=BLUE_C
                ).move_to(h),
            ),
            Transform(
                star,
                formula(r"h^*(1)=h_0+h_1\cdot1+\cdots+h_{n-1}\cdot1", size=42).move_to(
                    star
                ),
            ),
            run_time=1.6,
        )
        self.at("same_integer")
        self.play(
            Transform(
                h,
                formula(r"h(1)=h_0+h_1+\cdots+h_{n-1}", size=42, color=BLUE_C).move_to(
                    h
                ),
            ),
            Transform(
                star, formula(r"h^*(1)=h_0+h_1+\cdots+h_{n-1}", size=42).move_to(star)
            ),
            run_time=1.1,
        )
        self.at("square_product")
        equation = formula(r"n=h(1)h^*(1)", size=49, color=YELLOW)
        equation.move_to(DOWN * 1.7)
        self.show(equation)
        self.at("square_simplify")
        self.play(
            Transform(
                equation,
                formula(r"n=(h(1))^2", size=55, color=YELLOW).move_to(equation),
            ),
            run_time=1.3,
        )
        self.at("integer_square")
        self.play(
            Transform(
                evaluation, formula(r"h(1)\in\mathbb Z", size=43).move_to(evaluation)
            ),
            run_time=0.9,
        )

        self.section("parity", "Orthogonality pairs positive and negative terms")
        pair = (
            VGroup(
                formula(r"\mathrm{row}_r=(a_0,\ldots,a_{n-1})", size=39, color=BLUE_C),
                formula(r"\mathrm{row}_s=(b_0,\ldots,b_{n-1}),\quad r\ne s", size=39),
                formula(r"\sum_j a_jb_j=0,\qquad a_jb_j\in\{-1,1\}", size=41),
            )
            .arrange(DOWN, buff=0.5)
            .move_to(UP * 0.45)
        )
        self.show(pair)
        self.at("pair_signs")
        self.play(FadeOut(pair), run_time=0.5)
        self.body.remove(pair)
        signs = (
            VGroup(
                VGroup(
                    *(formula("+1", size=44, color=BLUE_C) for _ in range(3))
                ).arrange(RIGHT, buff=1),
                VGroup(*(formula("-1", size=44) for _ in range(3))).arrange(
                    RIGHT, buff=1
                ),
            )
            .arrange(DOWN, buff=0.8)
            .move_to(UP * 0.8)
        )
        self.show(signs)
        pairs_note = words(
            "Illustrative pairs; the total number of terms is n.", size=24
        ).move_to(DOWN * 1.1)
        self.show(pairs_note)
        for positive, negative in list(zip(signs[0], signs[1], strict=True)):
            zero = formula("0", size=44, color=YELLOW)
            zero.move_to((positive.get_center() + negative.get_center()) / 2)
            self.play(Transform(positive, zero), FadeOut(negative), run_time=0.6)
            signs[1].remove(negative)
        self.at("n_even")
        even = formula(
            r"\#(+1)=\#(-1)\quad\Longrightarrow\quad n\text{ even}",
            size=46,
            color=YELLOW,
        ).move_to(DOWN * 2)
        self.show(even)
        self.at("even_square")
        self.play(FadeOut(signs), FadeOut(even), FadeOut(pairs_note), run_time=0.5)
        self.body.remove(signs, even, pairs_note)
        self.show(formula(r"n=m^2,\qquad m>0", size=49, color=BLUE_C).move_to(UP * 1.2))
        root = formula(r"m\text{ even}", size=51, color=YELLOW)
        root.move_to(UP * 0.1)
        self.show(root)
        self.at("two_u")
        self.play(
            Transform(
                root,
                formula(
                    r"m=2u,\qquad u\in\mathbb Z_{>0}", size=47, color=YELLOW
                ).move_to(root),
            ),
            run_time=1.2,
        )
        self.show(formula(r"n=(2u)^2=4u^2", size=59, color=BLUE_C).move_to(DOWN * 1.4))

        self.section("oddness", "The deeper input: u is odd")
        self.show(
            self.stack(
                formula(r"n=4u^2", size=65, color=BLUE_C),
                words("Accepted input from the deeper polynomial argument", size=27),
                formula(r"u\text{ is odd}", size=56, color=YELLOW),
                words("Square and parity alone do not establish oddness.", size=25),
            ),
        )

        self.section("contradiction", "The remaining case: assume odd u > 1")
        matrix = sign_matrix().scale(0.85).move_to(LEFT * 3 + UP * 0.2)
        self.show(matrix)
        self.show(formula(r"n=1:\quad H=(1)", size=32).move_to(LEFT * 3 + UP * 2.1))
        self.show(
            formula(r"u=1\Longrightarrow n=4", size=39, color=BLUE_C).move_to(
                LEFT * 3 + DOWN * 1.8
            )
        )
        self.at("assume_counterexample")
        assumption = self.stack(
            words("Assume a circulant Hadamard matrix exists", size=24, width=6),
            formula(r"n=4u^2,\qquad u>1\text{ odd}", size=40, width=6, color=YELLOW),
        ).move_to(RIGHT * 2.8 + UP * 0.4)
        self.show(assumption)
        self.at("guiding_example")
        self.show(
            formula(
                r"u=3\quad\Longrightarrow\quad n=36", size=37, color=BLUE_C, width=6
            ).move_to(RIGHT * 2.8 + DOWN * 1.4)
        )
        self.show(
            words(
                "Guiding example; the proof must cover every odd u > 1.", size=24
            ).move_to(DOWN * 2.6)
        )
        self.play(FlashAround(assumption, color=YELLOW), run_time=0.8)
