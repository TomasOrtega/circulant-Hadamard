import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    Arrow,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, sign_matrix, words


class OrderIsSquare(NodeScene):
    node_id = "order-is-square"
    title = "2.1 · Evaluate at 1"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/order-is-square.json").read_text()
        )["detail_cues"]

        self.section("goal", "Turn the group-ring identity into an integer square")
        coefficients = (
            VGroup(
                *(
                    formula(term, size=45, color=BLUE_C)
                    for term in ["h_0", "h_1", r"\cdots", "h_{n-1}"]
                )
            )
            .arrange(RIGHT, buff=0.8)
            .move_to(UP * 1.45)
        )
        self.show(coefficients)
        self.show(formula(r"h_j\in\{-1,1\}", size=34).move_to(UP * 0.45))
        polynomial = formula(r"h(X)=\sum_{j=0}^{n-1}h_jX^j", size=48).move_to(
            DOWN * 0.8
        )
        self.body.add(polynomial)
        self.play(TransformFromCopy(coefficients, polynomial), run_time=1.4)
        self.at("norm_identity")
        self.show(
            formula(r"h(X)h^*(X)=n", size=49, color=YELLOW).move_to(DOWN * 2.0),
            formula(r"\text{in }\mathbb Z[X]/(X^n-1)", size=35).move_to(DOWN * 3.0),
        )

        self.section("valid_input", "The input 1 respects the cyclic relation")
        relation = formula(r"X^n=1", size=59, color=BLUE_C).move_to(UP * 1.7)
        self.show(relation)
        self.play(
            Transform(
                relation, formula(r"1^n=1", size=59, color=YELLOW).move_to(relation)
            ),
            run_time=1.2,
        )
        self.at("positive_powers")
        positive = formula(r"1^0,\quad1^1,\quad1^2,\quad\ldots,\quad1^{n-1}", size=43)
        positive.move_to(UP * 0.15)
        self.show(positive)
        self.play(
            Transform(
                positive,
                formula(r"1,\quad1,\quad1,\quad\ldots,\quad1", size=43).move_to(
                    positive
                ),
            ),
            run_time=1.2,
        )
        self.at("negative_powers")
        negative = formula(
            r"1^0,\quad1^{-1},\quad1^{-2},\quad\ldots,\quad1^{-(n-1)}", size=43
        )
        negative.move_to(DOWN * 1.4)
        self.show(negative)
        self.play(
            Transform(
                negative,
                formula(r"1,\quad1,\quad1,\quad\ldots,\quad1", size=43).move_to(
                    negative
                ),
            ),
            run_time=1.2,
        )
        self.show(
            words("Reversing powers has no effect at this input.", size=27).move_to(
                DOWN * 2.8
            )
        )

        self.section("identical_sums", "Both factors become the same row sum")
        labels = VGroup(
            formula(r"h(1)", size=53, color=BLUE_C).move_to(LEFT * 3.7 + UP * 1.4),
            formula(r"h^*(1)", size=53, color=BLUE_C).move_to(RIGHT * 3.7 + UP * 1.4),
        )
        left = formula(r"h_0+h_1+\cdots+h_{n-1}", size=37, width=6.5)
        left.move_to(LEFT * 3.7)
        right = left.copy().move_to(RIGHT * 3.7)
        self.show(labels, left, right, formula("=", size=55, color=YELLOW))
        self.at("integer_sum")
        self.show(
            formula(r"h(1)=\sum_jh_j\in\mathbb Z", size=48).move_to(DOWN * 1.6),
            words("An equality of integers", size=27).move_to(DOWN * 2.65),
        )

        self.section("square", "Evaluate the product identity")
        identity = formula(r"n=h(1)h^*(1)", size=61).move_to(UP * 1.2)
        self.show(identity)
        self.at("becomes_square")
        self.play(
            Transform(
                identity,
                formula(r"\boxed{n=h(1)^2}", size=66, color=YELLOW).move_to(identity),
            ),
            run_time=1.5,
        )
        self.show(
            formula(
                r"m=|h(1)|\in\mathbb Z_{>0},\qquad n=m^2", size=44, color=BLUE_C
            ).move_to(DOWN * 0.65),
            words("The order is a perfect square.", size=30).move_to(DOWN * 2.0),
        )

        self.section("example", "Check our actual order-four example")
        matrix = sign_matrix(size=0.65).move_to(LEFT * 3.8)
        self.show(matrix)
        highlight = SurroundingRectangle(matrix.get_rows()[0], buff=0.12).set_color(
            YELLOW
        )
        self.show(highlight)
        row_sum = formula(r"(-1)+1+1+1=2", size=43, color=BLUE_C).move_to(
            RIGHT * 3.0 + UP * 0.8
        )
        self.body.add(row_sum)
        self.play(TransformFromCopy(matrix.get_rows()[0], row_sum), run_time=1.4)
        self.at("four_squared")
        self.show(
            formula(r"n=2^2=4", size=57, color=YELLOW).move_to(
                RIGHT * 3.0 + DOWN * 0.7
            ),
            words("The size matches the row-sum square.", size=24, width=6).move_to(
                RIGHT * 3.0 + DOWN * 2.0
            ),
        )

        self.section("candidate", "A necessary condition for order 36")
        candidate = formula(
            r"n=36\quad\Longrightarrow\quad h(1)^2=36", size=48, color=BLUE_C
        )
        candidate.move_to(UP * 1.65)
        self.show(candidate)
        self.show(
            Arrow(UP * 0.95, UP * 0.3, buff=0.04).set_color(YELLOW),
            formula(r"h(1)=6\quad\text{or}\quad h(1)=-6", size=49).move_to(DOWN * 0.35),
        )
        self.at("necessary")
        self.show(
            words(
                "Necessary condition · no order-36 row has been constructed", size=25
            ).move_to(DOWN * 1.55)
        )
        self.at("next")
        self.show(
            formula(r"\boxed{n\text{ is a square}}", size=47, color=YELLOW).move_to(
                DOWN * 2.55
            ),
            words("Next, for n > 1: why must it also be even?", size=25).move_to(
                DOWN * 3.45
            ),
        )
