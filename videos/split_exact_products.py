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


class SplitExactProducts(NodeScene):
    node_id = "split-exact-products"
    title = "7.1 · Split the Exact Products"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def hide(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.35)
        self.body.remove(*objects)

    def product_source(self, family, parity):
        return (
            r"\prod_{\substack{S\subseteq I\\|S|\text{ "
            + parity
            + "}}}"
            + family
            + "_S"
        )

    def parity_product(self, family, parity, size=43):
        return formula(self.product_source(family, parity), size=size, color=BLUE_C)

    def product_equality(self, family, size=43):
        return formula(
            self.product_source(family, "even")
            + "="
            + self.product_source(family, "odd"),
            size=size,
            color=YELLOW,
            width=14.5,
        )

    def subset_card(self, subset, family, center, height=1.4):
        border = Rectangle(width=4.4, height=height).set_stroke(BLUE_C, width=1.5)
        label = formula(subset, size=27, color=BLUE_C).move_to(UP * (height / 2 - 0.32))
        value = formula(family, size=40, width=3.95).move_to(DOWN * 0.22)
        return VGroup(border, label, value).move_to(center)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/split-exact-products.json").read_text()
        )["detail_cues"]

        self.section("inputs", "All subset ratios are units of one evaluation ring")
        self.show(
            formula(
                r"u>1\text{ odd},\qquad I=\{p\text{ prime}:p\mid u\}", size=38
            ).move_to(UP * 2.05)
        )
        self.at("subset_roots")
        general_input = self.subset_card(
            r"S\subseteq I",
            r"P=\zeta_S=\prod_{p\in S}\zeta_p",
            LEFT * 3.5 + UP * 0.3,
            height=2.1,
        )
        empty_input = self.subset_card(
            r"S=\varnothing",
            r"P=\zeta_{\varnothing}=1",
            RIGHT * 3.5 + UP * 0.3,
            height=2.1,
        )
        self.show(general_input, run_time=1.0)
        self.at("empty_input")
        self.show(empty_input, run_time=0.9)
        self.at("ratio_definitions")
        ratios = VGroup(
            formula(r"r_S=\frac{d(\zeta_S)}{c(\zeta_S)}", size=43).move_to(
                LEFT * 3.7 + DOWN * 1.65
            ),
            formula(r"w_S=\frac{g(\zeta_S)}{c(\zeta_S)}", size=43).move_to(
                RIGHT * 3.7 + DOWN * 1.65
            ),
        )
        self.body.add(ratios)
        self.play(TransformFromCopy(general_input[2], ratios), run_time=1.3)
        self.at("one_ring")
        self.hide(*list(self.body))
        ring = formula(
            r"A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]", size=44, color=BLUE_C
        ).move_to(UP * 2.05)
        self.show(ring, run_time=1.1)
        ratios = VGroup(
            formula(r"r_S=\frac{d(\zeta_S)}{c(\zeta_S)}", size=45).move_to(
                LEFT * 3.7 + UP * 0.2
            ),
            formula(r"w_S=\frac{g(\zeta_S)}{c(\zeta_S)}", size=45).move_to(
                RIGHT * 3.7 + UP * 0.2
            ),
        )
        self.show(ratios, run_time=0.9)
        self.at("norm_units")
        self.show(
            formula(
                r"c(\zeta_S),d(\zeta_S),g(\zeta_S)\in A^{\times}", size=40, color=BLUE_C
            ).move_to(DOWN * 1.45),
            run_time=1.0,
        )
        self.at("explicit_inverse")
        self.show(
            formula(
                r"c(\zeta_S)^{-1}=\frac{\overline{c(\zeta_S)}}{u^2}\in A",
                size=40,
                color=YELLOW,
            ).move_to(DOWN * 3.0),
            run_time=1.1,
        )

        self.section("separate", "Move the odd-subset units to the other side")
        alternating = formula(
            r"\prod_{S\subseteq I}r_S^{(-1)^{|S|}}=1", size=49, color=BLUE_C
        ).move_to(UP * 1.95)
        self.show(alternating)
        even = self.parity_product("r", "even").move_to(LEFT * 3.7 + DOWN * 0.45)
        odd = self.parity_product("r", "odd").move_to(RIGHT * 3.7 + DOWN * 0.45)
        self.at("even_exponent")
        even_label = formula(r"|S|\text{ even}:\ +1", size=34, color=YELLOW).move_to(
            LEFT * 3.7 + UP * 0.8
        )
        self.show(even_label, even, run_time=0.9)
        self.at("odd_exponent")
        odd_label = formula(r"|S|\text{ odd}:\ -1", size=34, color=YELLOW).move_to(
            RIGHT * 3.7 + UP * 0.8
        )
        self.show(odd_label, odd, run_time=0.9)
        self.at("fraction")
        self.hide(even_label, odd_label, alternating)
        bar = Line(LEFT * 2.7, RIGHT * 2.7).set_stroke(width=2)
        bar.move_to(DOWN * 0.45)
        equals = formula("=1", size=46).move_to(RIGHT * 4.0 + DOWN * 0.45)
        self.play(
            even.animate.move_to(UP * 0.65),
            odd.animate.move_to(DOWN * 1.55),
            run_time=1.1,
        )
        self.show(bar, equals, run_time=0.65)
        self.at("multiply_units")
        instruction = words(
            "Multiply both sides by the odd-subset product", size=29
        ).move_to(UP * 2.05)
        denominator_unit = formula(
            r"D=\prod_{\substack{S\subseteq I\\|S|\text{ odd}}}r_S\in A^{\times}",
            size=35,
            color=BLUE_C,
        ).move_to(DOWN * 3.1)
        focus = SurroundingRectangle(odd, buff=0.13).set_color(YELLOW)
        self.show(instruction, denominator_unit, focus, run_time=1.0)
        self.at("cancel_denominator")
        right_product = self.parity_product("r", "odd").move_to(
            RIGHT * 3.8 + DOWN * 0.35
        )
        self.body.add(right_product)
        self.play(
            TransformFromCopy(odd, right_product),
            even.animate.move_to(LEFT * 3.8 + DOWN * 0.35),
            Transform(equals, formula("=", size=48).move_to(DOWN * 0.35)),
            FadeOut(bar),
            FadeOut(odd),
            FadeOut(focus),
            run_time=1.5,
        )
        self.body.remove(bar, odd, focus)
        self.play(
            Transform(
                denominator_unit,
                formula(r"D^{-1}D=1", size=38, color=BLUE_C).move_to(denominator_unit),
            ),
            run_time=0.7,
        )
        self.at("exact_equality")
        equality_frame = SurroundingRectangle(
            VGroup(even, equals, right_product), buff=0.2
        ).set_color(YELLOW)
        self.show(
            equality_frame,
            words(
                "Exact equality in A · before reduction", size=29, color=YELLOW
            ).move_to(DOWN * 2.2),
            run_time=0.9,
        )

        self.section("examples", "One prime gives two factors; two primes give four")
        example_label = formula(r"u=3,\qquad I=\{3\}", size=43, color=BLUE_C).move_to(
            UP * 2.1
        )
        cards = VGroup(
            self.subset_card(
                r"\varnothing", r"r_{\varnothing}", LEFT * 3.4 + UP * 0.25
            ),
            self.subset_card(r"\{3\}", r"r_{\{3\}}", RIGHT * 3.4 + UP * 0.25),
        )
        self.show(example_label, cards, run_time=1.0)
        self.at("one_prime_equality")
        one_prime = formula(
            r"r_{\varnothing}=r_{\{3\}}", size=52, color=YELLOW
        ).move_to(DOWN * 1.75)
        self.show(one_prime, run_time=1.0)
        self.at("two_primes")
        self.hide(cards, one_prime)
        self.play(
            Transform(
                example_label,
                formula(r"u=15,\qquad I=\{3,5\}", size=43, color=BLUE_C).move_to(
                    example_label
                ),
            ),
            run_time=0.8,
        )
        square = VGroup(
            *(
                self.subset_card(subset, ratio, center)
                for subset, ratio, center in [
                    (r"\varnothing", r"r_{\varnothing}", LEFT * 3.4 + UP * 0.75),
                    (r"\{3\}", r"r_{\{3\}}", RIGHT * 3.4 + UP * 0.75),
                    (r"\{5\}", r"r_{\{5\}}", LEFT * 3.4 + DOWN * 1.0),
                    (r"\{3,5\}", r"r_{\{3,5\}}", RIGHT * 3.4 + DOWN * 1.0),
                ]
            )
        )
        self.show(square, run_time=1.1)
        self.at("pair_products")
        product_row = (
            VGroup(
                formula(r"r_{\varnothing}", size=43, color=BLUE_C),
                formula(r"r_{\{3,5\}}", size=43, color=BLUE_C),
                formula("=", size=43),
                formula(r"r_{\{3\}}", size=43, color=BLUE_C),
                formula(r"r_{\{5\}}", size=43, color=BLUE_C),
            )
            .arrange(RIGHT, buff=0.3)
            .move_to(DOWN * 2.65)
        )
        self.body.add(product_row)
        self.play(
            TransformFromCopy(square[0][2], product_row[0]),
            TransformFromCopy(square[3][2], product_row[1]),
            TransformFromCopy(square[1][2], product_row[3]),
            TransformFromCopy(square[2][2], product_row[4]),
            run_time=1.3,
        )
        self.play(FadeIn(product_row[2]), run_time=0.5)
        self.at("individual_ratios")
        self.show(
            words(
                "Equal products · individual ratios may differ", size=27, color=YELLOW
            ).move_to(DOWN * 3.55),
            run_time=0.9,
        )

        self.section("other", "Repeat for the w ratios and keep both exact equalities")
        w_product = formula(
            r"\prod_{S\subseteq I}w_S^{(-1)^{|S|}}=1", size=49, color=BLUE_C
        ).move_to(UP * 0.6)
        self.show(w_product)
        self.at("move_w_factors")
        self.play(
            Transform(
                w_product,
                formula(
                    r"\frac{\prod_{\substack{S\subseteq I\\|S|\text{ even}}}w_S}"
                    r"{\prod_{\substack{S\subseteq I\\|S|\text{ odd}}}w_S}=1",
                    size=44,
                ).move_to(UP * 0.35),
            ),
            run_time=1.1,
        )
        self.at("w_equality")
        self.play(
            Transform(w_product, self.product_equality("w").move_to(DOWN * 0.6)),
            run_time=1.2,
        )
        self.at("both_equalities")
        self.play(w_product.animate.move_to(DOWN * 1.2), run_time=0.7)
        self.show(self.product_equality("r").move_to(UP * 0.95), run_time=1.1)
        self.show(
            words("Exact equalities in A", size=29, color=BLUE_C).move_to(UP * 2.15),
            run_time=0.7,
        )
        self.at("positive_exponents")
        self.show(
            words(
                "Finite products · positive exponents · ready to expand", size=29
            ).move_to(DOWN * 3.2),
            run_time=0.9,
        )
