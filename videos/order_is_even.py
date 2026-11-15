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
    Line,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class OrderIsEven(NodeScene):
    node_id = "order-is-even"
    title = "2.2 · Pair the Dot-Product Terms"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/order-is-even.json").read_text()
        )["detail_cues"]

        self.section("goal", "Orthogonality forces an even number of contributions")
        self.show(formula(r"n>1", size=49, color=BLUE_C).move_to(UP * 2.1))
        generic_rows = VGroup(
            formula(r"\mathrm{row}_r=(h_{r0},\ldots,h_{r,n-1})", size=39),
            formula(r"\mathrm{row}_s=(h_{s0},\ldots,h_{s,n-1})", size=39),
        ).arrange(DOWN, buff=0.55)
        generic_rows.move_to(UP * 0.35)
        self.at("goal_choose")
        self.show(generic_rows, run_time=0.8)
        orthogonal = formula(
            r"r\ne s:\quad\langle\mathrm{row}_r,\mathrm{row}_s\rangle=0",
            size=40,
            color=YELLOW,
        ).move_to(DOWN * 1.35)
        self.at("goal_zero")
        self.show(orthogonal, run_time=0.7)
        contributions = formula(
            r"\underbrace{(\pm1)+\cdots+(\pm1)}_{n\text{ terms}}=0",
            size=45,
            color=YELLOW,
        ).move_to(orthogonal)
        self.at("goal_signs")
        self.play(Transform(orthogonal, contributions), run_time=0.9)
        self.at("goal_even")
        self.show(words("Why must n be even?", size=29).move_to(DOWN * 2.6))

        self.section("example", "Multiply the two known order-four rows vertically")
        columns = [-3.15, -1.05, 1.05, 3.15]
        top = VGroup(
            *(
                formula(str(value), size=52, color=BLUE_C).move_to(RIGHT * x + UP * 1.6)
                for x, value in zip(columns, [-1, 1, 1, 1], strict=True)
            )
        )
        bottom = VGroup(
            *(
                formula(str(value), size=52, color=BLUE_C).move_to(RIGHT * x + UP * 0.4)
                for x, value in zip(columns, [1, -1, 1, 1], strict=True)
            )
        )
        self.show(formula("n=4", size=36).move_to(LEFT * 6 + UP * 2.1), run_time=0.6)
        self.at("example_rows")
        self.show(
            top,
            bottom,
            formula(r"\mathrm{row}_1", size=30).next_to(top, LEFT, buff=0.7),
            formula(r"\mathrm{row}_2", size=30).next_to(bottom, LEFT, buff=0.7),
            run_time=0.9,
        )
        products = VGroup(
            *(
                formula(value, size=52, color=YELLOW).move_to(RIGHT * x + DOWN * 1.2)
                for x, value in zip(columns, ["-1", "-1", "+1", "+1"], strict=True)
            )
        )
        focus = SurroundingRectangle(VGroup(top[0], bottom[0]), buff=0.18).set_color(
            YELLOW
        )
        self.at("example_multiply")
        self.show(
            formula(r"\times", size=46).move_to(LEFT * 5.5 + UP * 0.4),
            Line(LEFT * 4 + DOWN * 0.3, RIGHT * 4 + DOWN * 0.3).set_color(BLUE_C),
            focus,
            words("Four coordinate products", size=27).move_to(DOWN * 2.4),
            run_time=0.5,
        )
        self.body.add(products)
        for index, product in enumerate(products):
            self.at(f"example_product_{index}")
            animations = [
                TransformFromCopy(VGroup(top[index], bottom[index]), product),
                Transform(
                    focus,
                    SurroundingRectangle(
                        VGroup(top[index], bottom[index]), buff=0.18
                    ).set_color(YELLOW),
                ),
            ]
            if index:
                animations.append(products[index - 1].animate.set_color(BLUE_C))
            self.play(*animations, run_time=0.25 if index == 3 else 0.4)

        self.section("pairing", "Match each positive contribution with a negative one")
        entries = VGroup(
            *(
                formula(value, size=56, color=BLUE_C).move_to(RIGHT * x + UP * 0.4)
                for x, value in zip(columns, ["-1", "-1", "+1", "+1"], strict=True)
            )
        )
        pairs = VGroup(VGroup(entries[2], entries[0]), VGroup(entries[3], entries[1]))
        self.show(
            pairs,
            words("Positive", size=28).move_to(LEFT * 2 + UP * 1.9),
            words("Negative", size=28).move_to(RIGHT * 2 + UP * 1.9),
            run_time=0.6,
        )
        self.at("pairing_separate")
        self.play(
            entries[2].animate.move_to(LEFT * 2 + UP * 0.7),
            entries[3].animate.move_to(LEFT * 2 + DOWN * 0.6),
            entries[0].animate.move_to(RIGHT * 2 + UP * 0.7),
            entries[1].animate.move_to(RIGHT * 2 + DOWN * 0.6),
            run_time=1,
        )
        boxes = VGroup(
            *(SurroundingRectangle(pair, buff=0.2).set_color(YELLOW) for pair in pairs)
        )
        self.at("pairing_pair")
        self.show(boxes, run_time=0.6)
        self.at("pairing_zero")
        self.play(
            *(
                Transform(pair, formula("0", size=58, color=YELLOW).move_to(pair))
                for pair in pairs
            ),
            FadeOut(boxes),
            run_time=1,
        )
        self.body.remove(boxes)
        self.at("pairing_unpaired")
        self.show(
            formula(
                r"\text{unpaired contributions}\quad\Longrightarrow\quad\text{sum}\ne0",
                size=35,
            ).move_to(DOWN * 2.15),
            run_time=0.8,
        )
        self.at("pairing_match")
        self.show(
            words("The two counts must match.", size=30, color=YELLOW).move_to(
                DOWN * 3.05
            ),
            run_time=0.7,
        )

        self.section("counts", "Count positive and negative products in general")
        self.at("counts_define")
        self.show(
            formula(r"a:\ +1\text{ products}", size=41, color=BLUE_C).move_to(
                LEFT * 3.4 + UP * 1.5
            ),
            run_time=0.7,
        )
        self.at("counts_negative")
        self.show(
            formula(r"b:\ -1\text{ products}", size=41, color=BLUE_C).move_to(
                RIGHT * 3.4 + UP * 1.5
            ),
            run_time=0.7,
        )
        zero = formula("a-b=0", size=57).move_to(LEFT * 3.4 + DOWN * 0.15)
        total = formula("a+b=n", size=57).move_to(RIGHT * 3.4 + DOWN * 0.15)
        self.at("counts_zero")
        self.show(zero, run_time=0.7)
        self.at("counts_total")
        self.show(total, run_time=0.7)
        self.at("counts_equal")
        self.play(
            Transform(zero, formula("a=b", size=61, color=YELLOW).move_to(zero)),
            run_time=0.8,
        )
        self.at("counts_double")
        self.play(
            Transform(total, formula("n=a+a=2a", size=54, color=YELLOW).move_to(total)),
            run_time=1,
        )
        self.at("counts_even")
        self.show(
            formula(r"\boxed{n\text{ is even}}", size=53, color=YELLOW).move_to(
                DOWN * 2.05
            ),
            run_time=0.8,
        )

        self.section("square", "For a circulant matrix, combine this with n = m²")
        square = formula("n=m^2", size=57, color=BLUE_C).move_to(LEFT * 3.4 + UP * 1.6)
        even = formula(r"n\text{ even}", size=52, color=BLUE_C).move_to(
            RIGHT * 3.4 + UP * 1.6
        )
        self.at("square_identity")
        self.show(
            square,
            words("From the preceding node", size=24).move_to(LEFT * 3.4 + UP * 0.7),
            run_time=0.8,
        )
        self.at("square_even")
        self.show(
            even,
            words("From the pairing argument", size=24).move_to(RIGHT * 3.4 + UP * 0.7),
            run_time=0.8,
        )
        assumption = formula(r"m=2r+1\quad\text{if }m\text{ is odd}", size=44).move_to(
            DOWN * 0.4
        )
        self.at("square_assume")
        self.show(assumption, run_time=0.8)
        expanded = formula(
            r"m^2=\underbrace{4r^2+4r}_{\text{even}}+1\quad\text{odd}",
            size=44,
            color=YELLOW,
        ).move_to(DOWN * 1.65)
        self.at("square_expand")
        self.show(expanded, run_time=1)
        conflict = words("This contradicts n being even.", size=28).move_to(DOWN * 2.85)
        self.at("square_contradiction")
        self.show(conflict, run_time=0.7)
        self.at("square_conclude")
        self.play(
            Transform(
                assumption,
                formula(r"m\text{ is even}", size=58, color=YELLOW).move_to(DOWN * 0.5),
            ),
            FadeOut(expanded),
            FadeOut(conflict),
            run_time=0.9,
        )
        self.body.remove(expanded, conflict)

        self.section("substitute", "Write the even square root as m = 2u")
        self.show(
            formula("m=2u", size=62, color=BLUE_C).move_to(UP * 1.6), run_time=0.7
        )
        self.at("substitute_integer")
        self.show(
            formula(r"u\in\mathbb Z,\quad u>0", size=38).move_to(UP * 0.65),
            run_time=0.6,
        )
        result = formula("n=m^2", size=68).move_to(DOWN * 0.8)
        self.at("substitute_into")
        self.show(result, run_time=0.7)
        self.at("substitute_square")
        self.play(
            Transform(result, formula("n=(2u)^2", size=68).move_to(result)),
            run_time=0.9,
        )
        self.at("substitute_result")
        self.play(
            Transform(result, formula("n=4u^2", size=72, color=YELLOW).move_to(result)),
            run_time=0.9,
        )
        self.at("substitute_example")
        self.show(
            formula(r"n=4:\quad u=1", size=38, color=BLUE_C).move_to(DOWN * 2.35),
            run_time=0.8,
        )

        self.section("next", "The remaining task concerns this same u")
        self.show(
            formula(r"n=4u^2,\qquad u\in\mathbb Z_{>0}", size=57, color=YELLOW).move_to(
                UP * 0.75
            ),
            run_time=1,
        )
        self.at("next_odd")
        self.show(
            words("Next goal", size=28, color=BLUE_C).move_to(DOWN * 0.7), run_time=0.5
        )
        question = formula(r"u\text{ odd?}", size=58).move_to(DOWN * 1.7)
        self.show(question, run_time=0.8)
        self.play(FlashAround(question, color=YELLOW), run_time=0.7)
