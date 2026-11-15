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
    Rectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class ExpandIntegralProducts(NodeScene):
    node_id = "expand-integral-products"
    title = "7.2 · Expand Products with Exact Quotients"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def erase(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.4)
        self.body.remove(*objects)

    def copy_to(self, source, target, run_time=0.9):
        self.body.add(target)
        self.play(TransformFromCopy(source, target), run_time=run_time)

    def quotient_box(self, title, rows, x):
        outline = Rectangle(width=4.0, height=2.8).set_stroke(BLUE_C, 2)
        labels = VGroup(
            words(title, size=21, width=3.7).move_to(UP * 0.95),
            formula(rows[0], size=29, width=3.7).move_to(UP * 0.1),
            formula(rows[1], size=29, width=3.7).move_to(DOWN * 0.8),
        )
        return VGroup(outline, labels).move_to(RIGHT * x + DOWN * 0.75)

    def factor_row(self, letter, scalar, fraction, y):
        return (
            VGroup(
                formula(rf"{letter}_S=", size=45),
                formula("1+", size=45),
                formula(scalar, size=45, color=YELLOW),
                formula(fraction, size=45, color=BLUE_C),
            )
            .arrange(RIGHT, buff=0.24)
            .move_to(UP * y)
        )

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/expand-integral-products.json").read_text()
        )["detail_cues"]
        self.section(
            "quotients", "Exact division, then evaluation, then a unit inverse"
        )
        self.show(
            formula(
                r"A=\mathbb Z[i,\{\zeta_p:p\mid u\},1/u],\qquad u>1\text{ odd}",
                size=37,
                color=BLUE_C,
            ).move_to(UP * 1.9),
            formula(
                r"c_S=c(\zeta_S),\quad d_S=d(\zeta_S),\quad g_S=g(\zeta_S)", size=36
            ).move_to(UP * 1.05),
            run_time=1.1,
        )
        self.at("notation")
        ratios = formula(r"r_S=d_S/c_S,\qquad w_S=g_S/c_S", size=37).move_to(UP * 0.2)
        self.show(ratios, run_time=0.9)
        self.at("exact_quotients")
        self.erase(ratios)
        stages = [
            self.quotient_box(
                "Coefficient quotients",
                [r"a(P)=\frac{d(P)-c(P)}2", r"b(P)=\frac{g(P)-c(P)}{1+i}"],
                -4.8,
            ),
            self.quotient_box(
                "Evaluate at the subset root", [r"a(\zeta_S)", r"b(\zeta_S)"], 0
            ),
            self.quotient_box(
                "Multiply by the unit inverse",
                [r"\frac{a(\zeta_S)}{c_S}\in A", r"\frac{b(\zeta_S)}{c_S}\in A"],
                4.8,
            ),
        ]
        self.show(stages[0], run_time=0.9)
        self.at("coefficient_division")
        self.play(FlashAround(stages[0], color=YELLOW), run_time=0.8)
        self.at("evaluate")
        self.show(
            stages[1],
            Arrow(stages[0].get_right(), stages[1].get_left(), buff=0.12).set_color(
                BLUE_C
            ),
            run_time=0.8,
        )
        self.at("unit_inverse")
        self.show(
            stages[2],
            Arrow(stages[1].get_right(), stages[2].get_left(), buff=0.12).set_color(
                BLUE_C
            ),
            run_time=0.9,
        )
        self.show(
            formula(r"c_S^{-1}=\overline{c_S}/u^2", size=35, color=BLUE_C).move_to(
                DOWN * 2.7
            ),
            run_time=0.7,
        )
        self.at("no_scalar_inverse")
        self.show(
            words(
                "The coefficient divisions are already exact", size=27, color=YELLOW
            ).move_to(DOWN * 3.5),
            run_time=0.8,
        )

        self.section("factors", "Both families have the form 1 + t x")
        r = self.factor_row("r", "2", r"\frac{d_S-c_S}{2c_S}", 1.35)
        w = self.factor_row("w", "(1+i)", r"\frac{g_S-c_S}{(1+i)c_S}", -0.35)
        self.at("r_factor")
        self.show(r, run_time=0.9)
        self.at("w_factor")
        self.show(w, run_time=0.9)
        self.at("pattern")
        generic = formula(r"1+t x_S,\qquad x_S\in A", size=45, color=YELLOW).move_to(
            DOWN * 2.1
        )
        self.copy_to(VGroup(r[1], r[2], r[3]), generic)
        self.play(
            FlashAround(r[3], color=BLUE_C),
            FlashAround(w[3], color=BLUE_C),
            run_time=0.8,
        )
        self.at("family_scope")
        self.show(
            formula(r"r:\ t=2\qquad\qquad w:\ t=1+i", size=36, color=BLUE_C).move_to(
                DOWN * 3.25
            ),
            run_time=0.8,
        )

        self.section("two_factors", "Four choices in ordinary multiplication")
        product = formula(r"(1+tx_1)(1+tx_2)", size=46, color=BLUE_C).move_to(UP * 1.85)
        self.show(product, run_time=0.9)
        self.at("choose_first")
        grid = VGroup(
            *(Line(LEFT * 4 + UP * y, RIGHT * 4 + UP * y) for y in [1.0, -0.25, -1.5]),
            *(Line(RIGHT * x + UP, RIGHT * x + DOWN * 1.5) for x in [-4, 0, 4]),
        ).set_stroke(BLUE_C, 1.5)
        headers = VGroup(
            formula("1", size=31).move_to(LEFT * 2 + UP * 1.3),
            formula(r"tx_2", size=31, color=BLUE_C).move_to(RIGHT * 2 + UP * 1.3),
            formula("1", size=31).move_to(LEFT * 4.5 + UP * 0.37),
            formula(r"tx_1", size=31, color=BLUE_C).move_to(LEFT * 4.5 + DOWN * 0.88),
        )
        self.show(grid, headers, run_time=0.9)
        self.at("four_terms")
        entries = VGroup(
            formula("1", size=40).move_to(LEFT * 2 + UP * 0.37),
            formula(r"tx_2", size=40, color=BLUE_C).move_to(RIGHT * 2 + UP * 0.37),
            formula(r"tx_1", size=40, color=BLUE_C).move_to(LEFT * 2 + DOWN * 0.88),
            formula(r"t^2x_1x_2", size=40, color=YELLOW).move_to(
                RIGHT * 2 + DOWN * 0.88
            ),
        )
        self.show(entries, run_time=1.1)
        self.at("collect_two")
        self.play(
            FlashAround(entries[1], color=BLUE_C),
            FlashAround(entries[2], color=BLUE_C),
            run_time=0.8,
        )
        self.at("two_equality")
        self.copy_to(
            entries,
            formula(r"=1+t(x_1+x_2)+t^2x_1x_2", size=44).move_to(DOWN * 2.7),
            run_time=1.1,
        )

        self.section("three_factors", "Group terms by the number of selected factors")
        self.show(
            formula(r"(1+tx_1)(1+tx_2)(1+tx_3)", size=43, color=BLUE_C).move_to(
                UP * 1.95
            ),
            run_time=0.9,
        )
        choices = [
            formula("1", size=42).move_to(UP * 0.95),
            formula(r"+t(x_1+x_2+x_3)", size=42, color=BLUE_C).move_to(DOWN * 0.05),
            formula(r"+t^2(x_1x_2+x_1x_3+x_2x_3)", size=42, color=YELLOW).move_to(
                DOWN * 1.05
            ),
            formula(r"+t^3x_1x_2x_3", size=42, color=YELLOW).move_to(DOWN * 2.05),
        ]
        for key, term in zip(
            ["no_choices", "one_choice", "two_choices", "three_choices"],
            choices,
            strict=True,
        ):
            self.at(key)
            self.show(term, run_time=0.9)
        self.at("retain_four")
        outline = (
            Rectangle(width=choices[2].get_width() + 0.4, height=1.95)
            .set_stroke(YELLOW, 2)
            .move_to(DOWN * 1.55)
        )
        self.show(outline, run_time=0.7)
        self.at("q_definition")
        q = formula(
            r"+t^2Q,\qquad Q=x_1x_2+x_1x_3+x_2x_3+t x_1x_2x_3",
            size=37,
            color=YELLOW,
            width=14,
        ).move_to(DOWN * 1.55)
        self.copy_to(VGroup(choices[2], choices[3]), q)
        self.erase(choices[2], choices[3], outline)
        self.at("nothing_discarded")
        self.show(
            words("Every term is retained", size=28, color=YELLOW).move_to(DOWN * 3.2),
            run_time=0.7,
        )

        self.section("general", "An exact finite-product identity in the same ring")
        product = formula(r"\prod_{j\in F}(1+tx_j)", size=48, color=BLUE_C).move_to(
            UP * 1.75
        )
        self.show(product, run_time=0.9)
        self.at("general_identity")
        expansion = formula(
            r"=1+t\sum_{j\in F}x_j+t^2Q,\qquad Q\in A", size=44, color=YELLOW
        ).move_to(UP * 0.1)
        self.copy_to(product, expansion, run_time=1.1)
        self.at("two_copies")
        self.show(
            words("Two or more selections contribute a factor t²", size=28).move_to(
                DOWN * 1.45
            ),
            run_time=0.8,
        )
        self.at("exact_remainder")
        self.show(
            words(
                "Exact remainder · equality throughout", size=28, color=YELLOW
            ).move_to(DOWN * 2.35),
            run_time=0.8,
        )
        self.at("one_factor")
        self.show(
            formula(
                r"|F|=1\quad\Longrightarrow\quad Q=0", size=35, color=BLUE_C
            ).move_to(DOWN * 3.25),
            run_time=0.8,
        )

        self.section("sides", "Expand the even and odd sides separately")
        self.show(
            formula(
                r"\prod_{|S|\,\mathrm{even}}(1+tx_S)=\prod_{|S|\,\mathrm{odd}}(1+tx_S)",
                size=39,
                color=BLUE_C,
            ).move_to(UP * 1.95),
            run_time=0.9,
        )
        self.at("separate_sides")
        self.show(
            formula(
                r"\text{even side:}\quad1+t\sum_{|S|\,\mathrm{even}}x_S+t^2Q_e", size=39
            ).move_to(UP * 0.6),
            formula(
                r"\text{odd side:}\quad1+t\sum_{|S|\,\mathrm{odd}}x_S+t^2Q_o", size=39
            ).move_to(DOWN * 0.8),
            run_time=1.0,
        )
        self.at("families")
        self.show(
            formula(r"r:\ t=2\qquad\qquad w:\ t=1+i", size=35, color=BLUE_C).move_to(
                DOWN * 1.95
            ),
            run_time=0.8,
        )
        self.at("fifteen")
        example = words("u = 15: two factors on each side", size=27).move_to(DOWN * 2.8)
        self.show(example, run_time=0.8)
        self.at("three")
        self.play(
            Transform(
                example,
                words("u = 3: one factor on each side; Qe = Qo = 0", size=27).move_to(
                    example
                ),
            ),
            run_time=0.8,
        )
        self.at("next")
        self.show(
            words(
                "Next: subtract, then cancel in A, then reduce", size=27, color=YELLOW
            ).move_to(DOWN * 3.55),
            run_time=0.8,
        )
