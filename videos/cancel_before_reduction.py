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
    RoundedRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
    Write,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class CancelBeforeReduction(NodeScene):
    node_id = "cancel-before-reduction"
    title = "7.3 · Cancel before reducing"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def erase(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.4)
        self.body.remove(*objects)

    def box(self, label, center, width=3.6):
        outline = RoundedRectangle(width=width, height=0.85, corner_radius=0.1)
        outline.set_stroke(BLUE_C, 2)
        return VGroup(outline, words(label, size=22, width=width - 0.3)).move_to(center)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/cancel-before-reduction.json").read_text()
        )["detail_cues"]

        self.section(
            "original_ring", "The divided differences already belong to the domain"
        )
        self.show(
            formula(
                r"A=\mathbb Z[i,\{\zeta_p:p\mid u\},1/u]\subseteq\mathbb C",
                size=40,
                color=BLUE_C,
            ).move_to(UP * 1.9),
            formula(r"u>1\text{ odd},\qquad I=\{p:p\mid u\}", size=37).move_to(
                UP * 0.9
            ),
            run_time=1.1,
        )
        self.at("ring_quotients")
        steps = VGroup(
            self.box("Exact coefficient quotient", LEFT * 4.7 + DOWN * 0.4),
            self.box("Evaluate at the subset root", DOWN * 0.4),
            self.box("Multiply by the unit inverse", RIGHT * 4.7 + DOWN * 0.4),
        )
        self.show(steps[0], run_time=0.7)
        self.at("ring_evaluate")
        self.show(
            steps[1],
            Arrow(steps[0].get_right(), steps[1].get_left(), buff=0.15).set_color(
                BLUE_C
            ),
            run_time=0.5,
        )
        self.at("ring_unit")
        self.show(
            steps[2],
            Arrow(steps[1].get_right(), steps[2].get_left(), buff=0.15).set_color(
                BLUE_C
            ),
            run_time=0.7,
        )
        self.show(
            formula(
                r"c_S^{-1}=\overline{c_S}/u^2,\qquad x_S\in A", size=43, color=YELLOW
            ).move_to(DOWN * 1.9),
            run_time=0.9,
        )

        self.section("exact_expansions", "Keep both exact remainders")
        product = formula(
            r"\prod_{|S|\ \mathrm{even}}(1+tx_S)=\prod_{|S|\ \mathrm{odd}}(1+tx_S)",
            size=41,
            color=BLUE_C,
        ).move_to(UP * 2.05)
        self.show(product, run_time=1.1)
        constant_e = formula("1", size=43)
        linear_e = formula(r"+t\sum_{|S|\ \mathrm{even}}x_S", size=43, color=BLUE_C)
        remainder_e = formula(r"+t^2Q_e", size=43, color=YELLOW)
        even = (
            VGroup(constant_e, linear_e, remainder_e)
            .arrange(RIGHT, buff=0.35)
            .move_to(UP * 0.55)
        )
        constant_o = formula("1", size=43)
        linear_o = formula(r"+t\sum_{|S|\ \mathrm{odd}}x_S", size=43, color=BLUE_C)
        remainder_o = formula(r"+t^2Q_o", size=43, color=YELLOW)
        odd = (
            VGroup(constant_o, linear_o, remainder_o)
            .arrange(RIGHT, buff=0.35)
            .move_to(DOWN * 0.9)
            .align_to(even, LEFT)
        )
        self.at("expand_both")
        self.show(even, odd, run_time=1.3)
        exact_note = words(
            "Exact equalities · no terms discarded", size=29, color=BLUE_C
        ).move_to(DOWN * 2.5)
        self.at("expand_exact")
        self.show(exact_note, run_time=0.9)

        self.wait_until_narration(self.cues["subtract"])
        self.play(
            Transform(
                self.subtitle,
                words(
                    "Subtract the odd side from the even side", size=25, color=BLUE_C
                ).next_to(self.heading, DOWN, buff=0.25),
            ),
            run_time=0.35,
        )
        self.erase(product, exact_note)
        minus = formula("-", size=53, color=YELLOW).next_to(odd, LEFT, buff=0.35)
        rule = Line(
            even.get_left() + LEFT * 0.8 + DOWN * 2.2,
            even.get_right() + RIGHT * 0.15 + DOWN * 2.2,
        ).set_stroke(BLUE_C, 2)
        self.show(minus, rule, run_time=0.7)
        self.at("subtract_constants")
        strikes = VGroup(
            *(
                Line(
                    c.get_corner(UP + LEFT) + LEFT * 0.08,
                    c.get_corner(DOWN + RIGHT) + RIGHT * 0.08,
                ).set_stroke(YELLOW, 3)
                for c in [constant_e, constant_o]
            )
        )
        self.show(strikes, run_time=0.6)
        self.play(FadeOut(constant_e), FadeOut(constant_o), run_time=0.5)
        even.remove(constant_e)
        odd.remove(constant_o)
        self.at("subtract_collect")
        result = (
            VGroup(
                formula("tL", size=55, color=BLUE_C),
                formula(r"+t^2Q", size=55, color=YELLOW),
                formula("=0", size=55),
            )
            .arrange(RIGHT, buff=0.25)
            .move_to(DOWN * 2.6)
        )
        self.body.add(result)
        self.play(
            TransformFromCopy(VGroup(linear_e, linear_o), result[0]),
            TransformFromCopy(VGroup(remainder_e, remainder_o), result[1]),
            Write(result[2]),
            run_time=1.3,
        )
        self.erase(even, odd, minus, rule, strikes)
        self.play(result.animate.move_to(UP * 1.35), run_time=0.8)
        self.at("subtract_l")
        self.show(
            formula(
                r"L=\sum_{S\subseteq I}(-1)^{|S|}x_S", size=48, color=BLUE_C
            ).move_to(DOWN * 0.2),
            run_time=1,
        )
        self.at("subtract_q")
        self.show(
            formula(r"Q=Q_e-Q_o\in A", size=46, color=YELLOW).move_to(DOWN * 1.7),
            run_time=0.9,
        )
        self.at("subtract_families")
        self.show(
            words("Each family has its own L and Q", size=28).move_to(DOWN * 2.9),
            run_time=0.8,
        )

        self.section("cancel", "Cancel a nonzero scalar in the original domain")
        self.show(
            formula(r"t=2\ (r_S),\qquad t=1+i\ (w_S)", size=42, color=BLUE_C).move_to(
                UP * 2.05
            ),
            run_time=1,
        )
        self.at("cancel_nonzero")
        self.show(
            formula(
                r"t\ne0\quad\text{in the domain }A\subseteq\mathbb C",
                size=40,
                color=YELLOW,
            ).move_to(UP * 0.9),
            run_time=1,
        )
        factored = (
            VGroup(
                formula("t", size=60, color=YELLOW),
                formula("(L+tQ)", size=60),
                formula("=0", size=60),
            )
            .arrange(RIGHT, buff=0.25)
            .move_to(DOWN * 0.55)
        )
        self.at("cancel_factor")
        self.show(factored, run_time=1.1)
        self.at("cancel_scalar")
        strike = Line(
            factored[0].get_corner(UP + LEFT) + LEFT * 0.08,
            factored[0].get_corner(DOWN + RIGHT) + RIGHT * 0.08,
        ).set_stroke(YELLOW, 3)
        self.show(strike, run_time=0.45)
        leading_t = factored[0]
        self.play(FadeOut(leading_t), run_time=0.45)
        factored.remove(leading_t)
        self.erase(factored, strike)
        self.show(
            formula("L=-tQ", size=64, color=YELLOW).move_to(DOWN * 0.55), run_time=1
        )
        self.at("cancel_domain")
        self.show(
            words("Domain cancellation · t need not be a unit", size=29).move_to(
                DOWN * 2.1
            ),
            run_time=0.9,
        )
        self.at("cancel_before")
        self.show(
            words("No division by a residue", size=27, color=BLUE_C).move_to(
                DOWN * 3.1
            ),
            run_time=0.8,
        )

        self.section("reduce", "Now map both exact equations to one quotient ring")
        self.show(
            formula(r"A\longrightarrow A/(1+i)A", size=48, color=BLUE_C).move_to(
                UP * 2.05
            ),
            run_time=1,
        )
        r_equation = formula(r"L_r=-2Q_r", size=51, color=BLUE_C).move_to(
            LEFT * 3.4 + UP * 0.6
        )
        w_equation = formula(r"L_w=-(1+i)Q_w", size=49, color=BLUE_C).move_to(
            RIGHT * 3.4 + UP * 0.6
        )
        self.show(r_equation, w_equation, run_time=1)
        self.at("reduce_two")
        self.show(
            formula(r"2=(1+i)(1-i)", size=41, color=YELLOW).move_to(DOWN * 0.8),
            run_time=0.8,
        )
        self.at("reduce_zero")
        images = (
            VGroup(formula(r"2\mapsto0", size=39), formula(r"1+i\mapsto0", size=39))
            .arrange(RIGHT, buff=2.2)
            .move_to(DOWN * 1.8)
        )
        self.show(images, run_time=0.9)
        self.at("reduce_l")
        self.play(
            Transform(
                r_equation,
                formula(r"L_r\equiv0", size=59, color=YELLOW).move_to(r_equation),
            ),
            Transform(
                w_equation,
                formula(r"L_w\equiv0", size=59, color=YELLOW).move_to(w_equation),
            ),
            run_time=1,
        )
        self.at("reduce_ring")
        self.show(
            words(
                "The same quotient; it need not be a field or a domain",
                size=26,
                color=BLUE_C,
            ).move_to(DOWN * 3),
            run_time=0.9,
        )

        self.section(
            "two_sums", "Reduce existing ring elements, not formal zero denominators"
        )
        self.show(
            formula(
                r"c_S=c(\zeta_S),\quad d_S=d(\zeta_S),\quad g_S=g(\zeta_S)",
                size=36,
                color=BLUE_C,
            ).move_to(UP * 2.15),
            run_time=1.1,
        )
        self.at("sums_first")
        first = formula(
            r"\sum_{S\subseteq I}(-1)^{|S|}\frac{d_S-c_S}{2c_S}\equiv0\pmod{1+i}",
            size=45,
            color=BLUE_C,
        ).move_to(UP * 0.5)
        self.show(first, run_time=1.2)
        self.at("sums_second")
        second = formula(
            r"\sum_{S\subseteq I}(-1)^{|S|}\frac{g_S-c_S}{(1+i)c_S}\equiv0\pmod{1+i}",
            size=45,
            color=YELLOW,
        ).move_to(DOWN * 1.3)
        self.show(second, run_time=1.2)
        self.at("sums_existing")
        self.show(
            words(
                "Exact divided differences in A, formed before reduction", size=27
            ).move_to(DOWN * 3.05),
            run_time=0.9,
        )

        self.section("early_reduction", "Early reduction loses the linear information")
        early = formula(
            r"\prod_{|S|\ \mathrm{even}}(1+tx_S)=\prod_{|S|\ \mathrm{odd}}(1+tx_S)",
            size=42,
            color=BLUE_C,
        ).move_to(UP * 1.25)
        self.show(early, run_time=1)
        self.at("early_one")
        self.play(
            Transform(early, formula("1=1", size=76, color=YELLOW).move_to(early)),
            run_time=1,
        )
        lost = words("The linear information has disappeared", size=30).move_to(
            DOWN * 0.2
        )
        self.at("early_lost")
        self.show(lost, run_time=0.8)
        self.at("early_order")
        self.erase(early, lost)
        steps = VGroup(
            *(
                self.box(label, RIGHT * x + DOWN * 0.2, width=2.5)
                for label, x in zip(
                    ["Expand", "Subtract", "Cancel in A", "Reduce"],
                    [-4.5, -1.5, 1.5, 4.5],
                    strict=True,
                )
            )
        )
        self.show(
            words(
                "Preserve the information in this order", size=29, color=BLUE_C
            ).move_to(UP * 1.35),
            steps,
            run_time=1,
        )
        self.show(
            *(
                Arrow(a.get_right(), b.get_left(), buff=0.08).set_color(BLUE_C)
                for a, b in zip(steps[:-1], steps[1:], strict=True)
            ),
            run_time=0.8,
        )
        self.play(FlashAround(steps[2], color=YELLOW), run_time=0.6)

        self.section(
            "one_factor",
            "The two-input case is exact; the general output is a congruence",
        )
        title = formula(r"u=3,\qquad I=\{3\}", size=44, color=BLUE_C).move_to(UP * 2.05)
        single = formula(r"1+tx_{\varnothing}=1+tx_{\{3\}}", size=51).move_to(UP * 0.65)
        self.show(title, single, run_time=1.1)
        self.at("single_remainders")
        zeros = formula(
            r"Q_e=Q_o=0\quad\Longrightarrow\quad Q=0", size=43, color=YELLOW
        ).move_to(DOWN * 0.85)
        self.show(zeros, run_time=1)
        self.at("single_exact")
        exact = formula(
            r"L=x_{\varnothing}-x_{\{3\}}=0", size=51, color=YELLOW
        ).move_to(DOWN * 2.25)
        self.show(exact, run_time=1)
        self.at("single_general")
        self.erase(title, single, zeros, exact)
        self.show(
            words("u = 3: exact", size=30, color=BLUE_C).move_to(LEFT * 3.5 + UP * 1.4),
            words("General conclusion", size=30, color=BLUE_C).move_to(
                RIGHT * 3.5 + UP * 1.4
            ),
            formula(r"L_r=L_w=0", size=47).move_to(LEFT * 3.5 + DOWN * 0.1),
            formula(r"L_r\equiv0,\quad L_w\equiv0", size=43, color=YELLOW).move_to(
                RIGHT * 3.5 + DOWN * 0.1
            ),
            run_time=1.1,
        )
        self.at("single_next")
        self.show(
            formula(
                r"\text{Both congruences in }A/(1+i)A", size=37, color=BLUE_C
            ).move_to(DOWN * 1.55),
            words("Next: add them term by term in this same quotient", size=28).move_to(
                DOWN * 2.85
            ),
            run_time=1,
        )
