import json
from math import sqrt

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
    RoundedRectangle,
    Transform,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class ProductsToSums(NodeScene):
    node_id = "products-to-sums"
    title = "7 · From Products to Sums"

    def at(self, cue):
        self.wait_until_narration(self.animation_cues[cue])

    def hide(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.45)
        self.body.remove(*objects)

    def triangle(self, center):
        start = center + LEFT * 0.68 + DOWN * 0.43
        middle = start + RIGHT * 1.36
        top = middle + LEFT * 0.68 + UP * (0.68 * sqrt(3))
        return VGroup(
            *(
                Arrow(a, b, buff=0, stroke_width=3).set_color(BLUE_C)
                for a, b in [(start, middle), (middle, top), (top, start)]
            )
        )

    def card(self, subset, sign, x):
        box = RoundedRectangle(width=3.1, height=1.35, corner_radius=0.12)
        box.set_stroke(BLUE_C, width=1.8).set_fill(opacity=0)
        label = formula(r"S=" + subset, size=27).move_to(UP * 0.36)
        value = formula(r"\frac{E(\zeta_S)}{c(\zeta_S)}", size=34, color=BLUE_C)
        value.move_to(DOWN * 0.27)
        signed = formula(sign, size=37, color=YELLOW).move_to(UP * 1.02)
        return VGroup(box, label, value, signed).move_to(RIGHT * x + UP * 0.95)

    def present(self):
        record = ROOT / "videos/production/products-to-sums.json"
        self.animation_cues = json.loads(record.read_text())["animation_cues"]
        self.section("equality", "An exact equality from Node 6 · u = 3")
        left = formula(r"\frac{E(\omega)}{c(\omega)}", size=60, color=BLUE_C)
        left.move_to(LEFT * 3.75 + UP * 0.65)
        right = formula(r"\frac{E(1)}{c(1)}", size=60, color=BLUE_C)
        right.move_to(RIGHT * 3.75 + UP * 0.65)
        equals = formula("=", size=62, color=YELLOW).move_to(UP * 0.65)
        ratios = VGroup(left, equals, right)
        inputs = VGroup(
            formula(r"P=\omega", size=35).move_to(LEFT * 3.75 + DOWN * 0.6),
            formula(r"P=1", size=35).move_to(RIGHT * 3.75 + DOWN * 0.6),
        )
        self.show(ratios, inputs)
        self.at("all_ones_input")
        congruence = formula(
            r"E(P)\equiv J(P)\pmod{1+i}", size=44, color=YELLOW
        ).move_to(DOWN * 1.7)
        j_polynomial = formula(r"J(P)=1+P+\cdots+P^8", size=42)
        j_polynomial.move_to(DOWN * 2.75)
        self.show(congruence, j_polynomial)

        self.wait_until_narration(self.cues["example"])
        self.play(
            Transform(
                self.subtitle,
                words(
                    "Nine terms · two exact evaluations", size=25, color=BLUE_C
                ).move_to(self.subtitle),
            ),
            ratios.animate.shift(UP),
            inputs.animate.shift(UP),
            congruence.animate.scale(0.8).move_to(DOWN * 3.2),
            run_time=1,
        )
        self.hide(j_polynomial)
        self.at("nine_ones")
        ones = VGroup(*(formula("1", size=36, color=BLUE_C) for _ in range(9)))
        ones.arrange_in_grid(n_rows=3, n_cols=3, h_buff=0.45, v_buff=0.18)
        ones.move_to(RIGHT * 3.75 + DOWN * 0.65)
        self.show(ones, run_time=1.1)
        self.at("nine_sum")
        self.play(
            Transform(ones, formula("9", size=72, color=YELLOW).move_to(ones)),
            run_time=0.9,
        )
        j_one = formula(r"J(1)=9", size=40, color=BLUE_C)
        j_one.move_to(RIGHT * 3.75 + DOWN * 2)
        self.show(j_one, run_time=0.65)
        self.at("root_groups")
        triangles = [self.triangle(LEFT * x + DOWN * 0.65) for x in [5.45, 3.75, 2.05]]
        labels = [
            formula(r"1+\omega+\omega^2", size=24, width=1.5).move_to(
                LEFT * x + DOWN * 1.45
            )
            for x in [5.45, 3.75, 2.05]
        ]
        self.show(*triangles, *labels, run_time=1)
        self.at("zero_groups")
        for triangle in triangles:
            self.play(
                Transform(
                    triangle, formula("0", size=47, color=YELLOW).move_to(triangle)
                ),
                run_time=0.5,
            )
        j_omega = formula(r"J(\omega)=3(1+\omega+\omega^2)=0", size=32, width=6)
        j_omega.move_to(LEFT * 3.75 + DOWN * 2)
        self.show(j_omega, run_time=0.7)

        self.at("raw_residues")
        self.hide(ones, j_one, *triangles, *labels, j_omega)
        panel = RoundedRectangle(width=13.5, height=3.25, corner_radius=0.15)
        panel.set_stroke(BLUE_C, width=1.5).set_fill(opacity=0)
        panel.move_to(DOWN * 1)
        arithmetic = formula(r"\text{Modulo }1+i", size=34, color=BLUE_C)
        arithmetic.move_to(DOWN * 0.35)
        left_residue = formula(r"E(\omega)\equiv0", size=44, color=YELLOW)
        left_residue.move_to(LEFT * 3.75 + DOWN * 1.2)
        right_residue = formula(r"E(1)\equiv1", size=44, color=YELLOW)
        right_residue.move_to(RIGHT * 3.75 + DOWN * 1.2)
        self.show(panel, arithmetic, left_residue, right_residue, run_time=1)
        self.at("units")
        unit_labels = VGroup(
            formula(r"c(\omega)\text{ is a unit}", size=34, color=BLUE_C).move_to(
                inputs[0]
            ),
            formula(r"c(1)=\pm3\equiv1", size=34, color=BLUE_C).move_to(inputs[1]),
        )
        self.play(Transform(inputs, unit_labels), run_time=1)
        self.at("one_ratio")
        self.play(
            Transform(
                right_residue,
                formula(r"\frac{E(1)}{c(1)}\equiv1", size=47, color=YELLOW).move_to(
                    right_residue
                ),
            ),
            run_time=0.9,
        )
        self.at("omega_ratio")
        self.play(
            Transform(
                left_residue,
                formula(
                    r"\frac{E(\omega)}{c(\omega)}\equiv0", size=47, color=YELLOW
                ).move_to(left_residue),
            ),
            run_time=0.9,
        )
        self.at("conflict")
        self.play(FlashAround(ratios, color=YELLOW), run_time=0.8)
        self.show(
            formula(r"0\ne1", size=56, color=YELLOW).move_to(DOWN * 1.95), run_time=0.7
        )
        self.at("order_36")
        self.show(
            words(
                "Contradiction · no circulant Hadamard matrix of order 36", size=25
            ).move_to(DOWN * 2.75),
            run_time=0.75,
        )

        self.section("general", "Several distinct primes give more evaluations")
        index_label = formula(r"I=\{3\}\quad\text{(the guiding case)}", size=34)
        index_label.move_to(UP * 2.2)
        cards = [self.card(r"\varnothing", "+", -2.2), self.card(r"\{3\}", "-", 2.2)]
        self.show(index_label, *cards, run_time=1)
        self.at("subset_index")
        self.play(
            Transform(
                index_label,
                formula(
                    r"I=\{3,5\}\quad\text{(subset-indexing example)}", size=32
                ).move_to(index_label),
            ),
            Transform(cards[0], self.card(r"\varnothing", "+", -5.2)),
            Transform(cards[1], self.card(r"\{3\}", "-", -1.75)),
            run_time=1.2,
        )
        cards.extend([self.card(r"\{5\}", "-", 1.75), self.card(r"\{3,5\}", "+", 5.2)])
        self.show(*cards[2:], run_time=0.8)
        self.at("products")
        products = self.stack(
            formula(
                r"\prod_{|S|\,\mathrm{even}}r_S=\prod_{|S|\,\mathrm{odd}}r_S"
                r",\qquad r_S=\frac{d(\zeta_S)}{c(\zeta_S)}",
                size=35,
            ),
            formula(
                r"\prod_{|S|\,\mathrm{even}}w_S=\prod_{|S|\,\mathrm{odd}}w_S"
                r",\qquad w_S=\frac{g(\zeta_S)}{c(\zeta_S)}",
                size=35,
            ),
            buff=0.4,
        ).move_to(DOWN * 1.15)
        self.show(products, run_time=1)
        self.at("expand")
        expansion = formula(
            r"\prod_j(1+t x_j)=1+t\sum_jx_j+t^2Q", size=45, color=BLUE_C
        ).move_to(DOWN * 0.8)
        self.play(Transform(products, expansion), run_time=1)
        t_values = formula(r"t=2\quad\text{or}\quad t=1+i", size=37)
        t_values.move_to(DOWN * 2)
        self.show(t_values, run_time=0.65)
        self.at("cancel")
        self.play(
            Transform(
                products,
                formula(
                    r"tL+t^2Q=0\quad\Longrightarrow\quad L=-tQ", size=45, color=YELLOW
                ).move_to(DOWN * 0.8),
            ),
            run_time=1,
        )
        self.play(
            Transform(
                t_values,
                words("Cancel in characteristic zero first.", size=27).move_to(
                    t_values
                ),
            ),
            run_time=0.6,
        )
        self.at("alternating_sum")
        self.hide(products, t_values)
        general_sum = formula(
            r"\mathcal S:=\sum_{S\subseteq I}(-1)^{|S|}"
            r"\frac{E(\zeta_S)}{c(\zeta_S)}",
            size=53,
            color=BLUE_C,
        ).move_to(DOWN * 0.85)
        self.show(general_sum, run_time=1)
        self.at("sum_zero")
        self.show(
            formula(
                r"\boxed{\mathcal S\equiv0\pmod{1+i}}", size=53, color=YELLOW
            ).move_to(DOWN * 2.35),
            run_time=0.9,
        )
        self.at("next_node")
        self.show(
            words("Node 8: combine this sum with E(P) ≡ J(P).", size=26).move_to(
                DOWN * 3.25
            ),
            run_time=0.8,
        )
