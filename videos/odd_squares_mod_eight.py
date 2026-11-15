import json

from manimlib import (
    BLUE_B,
    BLUE_C,
    BLUE_E,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    Arrow,
    FlashAround,
    LaggedStart,
    Rectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, sign_matrix, words


def tile(source, width=1.3, height=0.65, size=29, color=BLUE_C):
    outline = Rectangle(width=width, height=height)
    outline.set_stroke(color, width=1.5).set_fill(BLUE_E, opacity=0.12)
    label = formula(source, size=size, color=color, width=width - 0.2)
    return VGroup(outline, label)


def card(source, center, width=5, color=BLUE_C):
    outline = Rectangle(width=width, height=0.8)
    outline.set_stroke(color, width=2).set_fill(BLUE_E, opacity=0.15)
    return VGroup(outline, words(source, size=24, width=width - 0.25)).move_to(center)


def power_term(j, starred=False):
    exponent = -j if starred else j
    return rf"b_{{{j}}}X^{{{exponent}}}"


class OddSquaresModEight(NodeScene):
    node_id = "odd-squares-mod-eight"
    title = "2.6 · Odd Squares Modulo 8"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/odd-squares-mod-eight.json").read_text()
        )["detail_cues"]

        self.section("endpoint", "Test the endpoint forced by the preceding descent")
        n = formula(r"n=2^{2s}w^2,\qquad s\ge1,\quad w\text{ odd}", size=45)
        n.move_to(UP * 1.85)
        self.show(n)
        self.show(
            words("Earlier reductions for n > 1", size=24, color=BLUE_C).move_to(
                UP * 0.9
            )
        )
        u = formula(r"u=2^{s-1}w", size=49, color=BLUE_C).move_to(
            LEFT * 3.7 + DOWN * 0.25
        )
        self.at("endpoint_u")
        self.show(u)
        self.at("endpoint_assume")
        assumption = card("Suppose s ≥ 2", RIGHT * 3.7 + DOWN * 0.25, color=YELLOW)
        self.show(assumption)
        self.at("endpoint_descent")
        endpoint = (
            VGroup(
                formula(r"M=2^{s+1}", size=42),
                formula(r"TT^*=4w^2", size=42),
                words("All coefficients are odd", size=24),
            )
            .arrange(DOWN, buff=0.3)
            .move_to(RIGHT * 3.7 + DOWN * 2.25)
        )
        self.show(
            Arrow(assumption.get_bottom(), endpoint.get_top(), buff=0.12).set_color(
                YELLOW
            ),
            endpoint,
        )
        self.show(
            words("Conditional consequence of Node 2.5", size=23, color=BLUE_C).move_to(
                LEFT * 3.7 + DOWN * 2.5
            )
        )

        self.section(
            "constant", "Only matching indices return to the identity position"
        )
        self.show(
            formula(r"TT^*=4w^2,\qquad M=2^{s+1}\quad(s\ge2)", size=43).move_to(
                UP * 2.0
            )
        )
        self.show(
            words(
                "M = 8 illustrates the smallest endpoint · all coefficients odd",
                size=23,
                color=BLUE_C,
            ).move_to(UP * 1.25)
        )
        upper = (
            VGroup(*(tile(power_term(j)) for j in range(8)))
            .arrange(RIGHT, buff=0.12)
            .move_to(UP * 0.55)
        )
        lower = (
            VGroup(*(tile(power_term(j, True), color=BLUE_B) for j in range(8)))
            .arrange(RIGHT, buff=0.12)
            .move_to(DOWN * 0.4)
        )
        self.show(upper, lower)
        self.show(
            formula("T", size=33).next_to(upper, LEFT, buff=0.3),
            formula(r"T^*", size=33).next_to(lower, LEFT, buff=0.3),
        )
        self.at("constant_product")
        product = formula(
            r"(b_jX^j)(b_\ell X^{-\ell})=b_jb_\ell X^{j-\ell}", size=37
        ).move_to(DOWN * 1.25)
        self.show(product)
        self.at("constant_identity")
        condition = formula(r"j-\ell\equiv0\pmod M", size=38, color=YELLOW).move_to(
            product
        )
        self.play(Transform(product, condition), run_time=0.9)
        self.at("constant_indices")
        self.play(
            Transform(
                product,
                formula(
                    r"j-\ell\equiv0\pmod M,\quad 0\le j,\ell<M"
                    r"\quad\Longrightarrow\quad j=\ell",
                    size=31,
                    width=12,
                    color=YELLOW,
                ).move_to(product),
            ),
            run_time=0.9,
        )
        self.play(
            FlashAround(upper[3], color=YELLOW),
            FlashAround(lower[3], color=YELLOW),
            run_time=0.8,
        )
        self.at("constant_collect")
        squares = (
            VGroup(*(tile(rf"b_{{{j}}}^2", width=1.1, size=38) for j in range(8)))
            .arrange(RIGHT, buff=0.13)
            .move_to(DOWN * 2.05)
        )
        self.body.add(squares)
        self.play(
            LaggedStart(
                *(
                    TransformFromCopy(VGroup(upper[j], lower[j]), squares[j])
                    for j in range(8)
                ),
                lag_ratio=0.15,
            ),
            run_time=3,
        )
        self.at("constant_sum")
        self.show(
            formula(r"\sum_{j=0}^{M-1}b_j^2=4w^2", size=43, color=YELLOW).move_to(
                DOWN * 3.2
            )
        )

        self.section("odd_square", "Every odd square leaves one modulo eight")
        self.show(
            formula(r"b=2r+1,\qquad r\in\mathbb Z", size=47, color=BLUE_C).move_to(
                UP * 1.7
            )
        )
        square = formula(r"b^2=(2r+1)^2", size=53).move_to(UP * 0.55)
        self.show(square)
        self.at("odd_expand")
        self.play(
            Transform(square, formula(r"b^2=4r(r+1)+1", size=53).move_to(square)),
            run_time=1,
        )
        self.at("odd_consecutive")
        parity = (
            VGroup(
                VGroup(
                    words("r even", size=25), formula(r"r+1\text{ odd}", size=32)
                ).arrange(DOWN, buff=0.2),
                VGroup(
                    words("r odd", size=25), formula(r"r+1\text{ even}", size=32)
                ).arrange(DOWN, buff=0.2),
            )
            .arrange(RIGHT, buff=2.2)
            .move_to(DOWN * 1.05)
        )
        self.show(parity)
        self.show(
            formula(r"r(r+1)=2k", size=40, color=BLUE_C).move_to(DOWN * 2.15),
            run_time=0.9,
        )
        self.at("odd_multiple_eight")
        self.play(
            Transform(square, formula(r"b^2=8k+1", size=55).move_to(square)),
            run_time=0.9,
        )
        self.at("odd_residue")
        self.show(
            formula(r"\boxed{b^2\equiv1\pmod8}", size=49, color=YELLOW).move_to(
                DOWN * 3.25
            ),
            run_time=0.9,
        )

        self.section("blocks", "The left side breaks into complete blocks of eight")
        equality = formula(r"\sum_{j=0}^{M-1}b_j^2=4w^2", size=45).move_to(UP * 1.9)
        cells = (
            VGroup(
                *(
                    tile(rf"b_{{{j}}}^2", width=0.9, height=0.8, size=35)
                    for j in range(8)
                )
            )
            .arrange(RIGHT, buff=0.12)
            .move_to(DOWN * 0.15)
        )
        self.show(equality, cells, run_time=0.8)
        self.at("blocks_ones")
        self.play(
            *(
                Transform(cell[1], formula("1", size=42).move_to(cell[1]))
                for cell in cells
            ),
            run_time=0.8,
        )
        self.at("blocks_count")
        self.show(
            formula(r"M=2^{s+1}=8\cdot2^{s-2}", size=41, color=BLUE_C).move_to(
                UP * 0.85
            ),
            run_time=0.8,
        )
        self.at("blocks_group")
        grid = (
            cells.copy()
            .arrange_in_grid(n_rows=2, n_cols=4, buff=0.2)
            .move_to(LEFT * 3.6 + DOWN * 0.65)
        )
        self.play(Transform(cells, grid), run_time=1)
        frame = (
            Rectangle(width=4.6, height=2.2).set_stroke(YELLOW, width=2).move_to(cells)
        )
        self.show(frame, run_time=0.6)
        self.show(
            words("One complete block of eight", size=24).move_to(
                LEFT * 3.6 + DOWN * 2.15
            ),
            run_time=0.6,
        )
        self.at("blocks_zero")
        zero = formula("0", size=100, color=YELLOW).move_to(cells)
        self.play(Transform(cells, zero), run_time=0.8)
        self.show(
            formula(r"2^{s-2}\text{ such blocks}", size=35).move_to(
                RIGHT * 3.4 + DOWN * 0.65
            ),
            run_time=0.7,
        )
        self.show(
            formula(r"\sum_j b_j^2\equiv0\pmod8", size=47, color=YELLOW).move_to(
                DOWN * 3.15
            ),
            run_time=0.8,
        )

        self.section("right_side", "The right side leaves four")
        equality = formula(r"\sum_j b_j^2=4w^2", size=50).move_to(UP * 1.8)
        left = formula(r"\text{Left side}\equiv0", size=45, color=BLUE_C).move_to(
            LEFT * 3.65 + UP * 0.3
        )
        right = formula(r"4w^2", size=55).move_to(RIGHT * 3.65 + UP * 0.3)
        self.show(equality, left, right, run_time=1)
        self.at("right_odd")
        self.show(
            formula(
                r"w\text{ odd}\quad\Longrightarrow\quad w^2\equiv1\pmod8",
                size=37,
                color=BLUE_C,
            ).move_to(DOWN * 1.0),
            run_time=0.8,
        )
        self.at("right_four")
        self.play(
            Transform(
                right, formula(r"4\cdot1\equiv4", size=50, color=YELLOW).move_to(right)
            ),
            run_time=1,
        )
        conflict = formula("0=4", size=76, color=YELLOW).move_to(DOWN * 2.25)
        self.show(conflict, run_time=0.8)
        self.at("right_conflict")
        self.play(
            Transform(
                conflict,
                formula(r"0\not\equiv4\pmod8", size=65, color=YELLOW).move_to(conflict),
            ),
            run_time=0.8,
        )
        self.show(
            words("The conditional endpoint cannot exist", size=25).move_to(
                DOWN * 3.45
            ),
            run_time=0.8,
        )

        self.section("recover", "Return to the original parameter u")
        possibilities = formula(r"s\ge1,\qquad s<2", size=52).move_to(UP * 1.7)
        u = formula(r"u=2^{s-1}w", size=58, color=BLUE_C).move_to(UP * 0.15)
        self.show(possibilities, u)
        self.at("recover_one")
        self.play(
            Transform(
                possibilities,
                formula(r"s=1", size=64, color=YELLOW).move_to(possibilities),
            ),
            run_time=0.8,
        )
        self.at("recover_substitute")
        self.play(
            Transform(
                u, formula(r"u=2^{1-1}w=2^0w=w", size=55, color=BLUE_C).move_to(u)
            ),
            run_time=1.1,
        )
        self.show(
            words("w is odd, so u is odd", size=27).move_to(DOWN * 1.05), run_time=0.8
        )
        self.at("recover_order")
        n = formula(r"n=2^{2s}w^2", size=48).move_to(DOWN * 2.15)
        self.show(n, run_time=0.7)
        self.play(
            Transform(
                n,
                formula(
                    r"\boxed{n=4u^2,\qquad u\text{ odd}}", size=50, color=YELLOW
                ).move_to(n),
            ),
            run_time=1,
        )
        self.show(
            words("Order restriction complete", size=25, color=BLUE_C).move_to(
                DOWN * 3.45
            ),
            run_time=0.8,
        )

        self.section("order_four", "Order four survives")
        self.show(
            formula(r"u=1\quad\Longrightarrow\quad n=4", size=48, color=BLUE_C).move_to(
                LEFT * 3.5 + UP * 0.75
            )
        )
        self.show(
            words("Allowed by this restriction", size=25).move_to(
                LEFT * 3.5 + DOWN * 0.55
            )
        )
        self.at("four_matrix")
        matrix = sign_matrix(size=0.8).move_to(RIGHT * 3.5)
        self.show(matrix)
        self.show(
            formula(r"HH^{\mathsf T}=4I_4", size=40).move_to(RIGHT * 3.5 + DOWN * 2.35),
            run_time=0.8,
        )
        self.at("four_next")
        self.show(
            card(
                "Next: exclude the candidates with u > 1",
                DOWN * 3.35,
                width=9,
                color=YELLOW,
            ),
            run_time=1,
        )
