import json
from math import cos, sin

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    TAU,
    UP,
    YELLOW,
    Arrow,
    Circle,
    Dot,
    FadeOut,
    FlashAround,
    Line,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class OddComparisonProducts(NodeScene):
    node_id = "odd-comparison-products"
    title = "6.1 · Compare the Delta values"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def erase(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.4)
        self.body.remove(*objects)

    def copy_to(self, source, target, run_time=0.9):
        self.body.add(target)
        self.play(TransformFromCopy(source, target), run_time=run_time)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/odd-comparison-products.json").read_text()
        )["detail_cues"]

        self.section("norm_input", "Recall the normalized norm solutions")
        self.show(
            formula(r"u>1\text{ odd},\qquad P^{u^2}=1", size=40, color=BLUE_C).move_to(
                UP * 2.1
            ),
            run_time=0.9,
        )
        norms = (
            VGroup(
                *(
                    formula(rf"{name}(P){name}^*(P)=u^2", size=42, color=BLUE_C)
                    for name in ["c", "d", "g"]
                )
            )
            .arrange(DOWN, buff=0.5)
            .move_to(LEFT * 3.7 + DOWN * 0.1)
        )
        self.at("norm_three")
        self.show(norms, run_time=1.2)
        evaluated = formula(r"|f(\zeta_S)|^2=u^2", size=46).move_to(
            RIGHT * 3.2 + UP * 0.75
        )
        self.at("norm_values")
        self.show(evaluated, run_time=0.9)
        self.play(
            Transform(
                evaluated,
                formula(r"|f(\zeta_S)|=u>0", size=46, color=YELLOW).move_to(evaluated),
            ),
            run_time=0.9,
        )
        self.show(
            formula(r"f\in\{c,d,g\}", size=36, color=BLUE_C).move_to(
                RIGHT * 3.2 + DOWN * 0.65
            ),
            run_time=0.8,
        )
        self.at("norm_nonzero")
        self.show(
            formula(r"f(\zeta_S)\ne0", size=43, color=YELLOW).move_to(
                RIGHT * 3.2 + DOWN * 2
            ),
            run_time=0.9,
        )

        self.section("delta_input", "Use the same alternating construction three times")
        primes = formula(r"I=\{p:p\mid u\}", size=42, color=BLUE_C).move_to(UP * 2.05)
        self.show(primes, run_time=0.9)
        roots = formula(
            r"\zeta_S=\prod_{p\in S}\zeta_p,\qquad\zeta_{\varnothing}=1", size=41
        ).move_to(UP * 0.8)
        self.at("delta_roots")
        self.show(roots, run_time=1)
        product = formula(
            r"\Delta(f)=\prod_{S\subseteq I}f(\zeta_S)^{(-1)^{|S|}}",
            size=46,
            color=BLUE_C,
        ).move_to(DOWN * 0.75)
        self.at("delta_product")
        self.show(product, run_time=1.1)
        self.at("delta_parity")
        self.erase(primes, roots)
        top = formula(
            r"\prod_{S\subseteq I,\ |S|\ \mathrm{even}}f(\zeta_S)",
            size=43,
            color=BLUE_C,
        ).move_to(UP * 1.05)
        bottom = formula(
            r"\prod_{S\subseteq I,\ |S|\ \mathrm{odd}}f(\zeta_S)",
            size=43,
            color=BLUE_C,
        ).move_to(DOWN * 0.7)
        self.copy_to(product, top, run_time=0.7)
        self.copy_to(product, bottom, run_time=0.7)
        self.erase(product)
        self.show(
            Line(LEFT * 2.8 + UP * 0.2, RIGHT * 2.8 + UP * 0.2).set_stroke(YELLOW, 2),
            formula(r"\Delta(f)=", size=47).move_to(LEFT * 4.1 + UP * 0.2),
            run_time=0.6,
        )
        self.at("delta_theorem")
        deltas = (
            VGroup(
                *(
                    formula(rf"\Delta({name})", size=43, color=BLUE_C)
                    for name in ["c", "d", "g"]
                )
            )
            .arrange(RIGHT, buff=1.6)
            .move_to(DOWN * 2.25)
        )
        self.show(deltas, run_time=1)
        self.show(
            words(
                "Known input from Node 4: each has odd order", size=27, color=YELLOW
            ).move_to(DOWN * 3.25),
            run_time=0.9,
        )

        self.section("comparisons", "Use Delta(c) as the reference")
        reference = formula(r"\Delta(c)", size=53, color=YELLOW).move_to(UP * 1.2)
        d_delta = formula(r"\Delta(d)", size=49, color=BLUE_C).move_to(
            LEFT * 4.4 + UP * 1.2
        )
        g_delta = formula(r"\Delta(g)", size=49, color=BLUE_C).move_to(
            RIGHT * 4.4 + UP * 1.2
        )
        self.show(reference, d_delta, g_delta, run_time=0.9)
        self.show(
            Arrow(d_delta.get_right(), reference.get_left(), buff=0.22).set_color(
                BLUE_C
            ),
            Arrow(g_delta.get_left(), reference.get_right(), buff=0.22).set_color(
                BLUE_C
            ),
            run_time=0.7,
        )
        self.at("comparison_r")
        self.show(
            formula(r"R=\frac{\Delta(d)}{\Delta(c)}", size=50, color=BLUE_C).move_to(
                LEFT * 3.5 + DOWN * 0.7
            ),
            run_time=1,
        )
        self.at("comparison_w")
        self.show(
            formula(r"W=\frac{\Delta(g)}{\Delta(c)}", size=50, color=BLUE_C).move_to(
                RIGHT * 3.5 + DOWN * 0.7
            ),
            run_time=1,
        )
        self.at("comparison_complex")
        self.show(
            words("Complex quotients of Delta values", size=30, color=YELLOW).move_to(
                DOWN * 2.1
            ),
            run_time=0.9,
        )
        self.at("comparison_coefficients")
        self.show(
            words(
                "These do not compare individual polynomial coefficients", size=25
            ).move_to(DOWN * 3.15),
            run_time=0.9,
        )

        self.section("odd_exponent", "A common odd exponent controls the quotient")
        self.show(
            formula(r"\alpha^m=1,\qquad\beta^n=1", size=49, color=BLUE_C).move_to(
                UP * 2.05
            ),
            formula(r"m,n>0\text{ odd}", size=39).move_to(UP * 0.95),
            run_time=1,
        )
        quotient = formula(r"\frac{\alpha}{\beta}", size=69, color=BLUE_C).move_to(
            DOWN * 0.6
        )
        self.show(quotient, run_time=0.8)
        self.at("exponent_raise")
        self.play(
            Transform(
                quotient,
                formula(r"(\alpha/\beta)^{mn}", size=64, color=YELLOW).move_to(
                    quotient
                ),
            ),
            run_time=1,
        )
        self.at("exponent_regroup")
        self.play(
            Transform(
                quotient,
                formula(
                    r"\frac{(\alpha^m)^n}{(\beta^n)^m}", size=61, color=YELLOW
                ).move_to(quotient),
            ),
            run_time=1.1,
        )
        self.at("exponent_ones")
        self.play(
            Transform(
                quotient, formula(r"\frac11=1", size=63, color=YELLOW).move_to(quotient)
            ),
            run_time=1,
        )
        order = formula(
            r"\operatorname{ord}(\alpha/\beta)\mid mn"
            r"\quad\Longrightarrow\quad\text{odd order}",
            size=38,
        ).move_to(DOWN * 2.2)
        self.at("exponent_order")
        self.show(order, run_time=1.1)
        self.at("exponent_apply")
        self.erase(quotient, order)
        self.show(
            formula(
                r"R,\ W:\quad\text{roots of unity of odd order}", size=43, color=YELLOW
            ).move_to(DOWN * 0.7),
            run_time=1,
        )
        self.at("exponent_one")
        self.show(
            words("Order 1 is included", size=30, color=BLUE_C).move_to(DOWN * 2.2),
            run_time=0.8,
        )

        self.section("two_inputs", "Unpack both comparisons with the same orientation")
        self.show(
            formula(r"u=3,\qquad\omega=e^{2\pi i/3}", size=45, color=BLUE_C).move_to(
                UP * 2.05
            ),
            run_time=1,
        )
        self.at("two_delta")
        self.show(
            formula(r"\Delta(f)=\frac{f(1)}{f(\omega)}", size=49).move_to(UP * 0.75),
            run_time=1,
        )
        self.at("two_r")
        r_ratio = formula(
            r"R=\frac{d(1)/c(1)}{d(\omega)/c(\omega)}", size=47, color=BLUE_C
        ).move_to(LEFT * 3.5 + DOWN * 1.1)
        self.show(r_ratio, run_time=1.1)
        self.at("two_w")
        w_ratio = formula(
            r"W=\frac{g(1)/c(1)}{g(\omega)/c(\omega)}", size=47, color=BLUE_C
        ).move_to(RIGHT * 3.5 + DOWN * 1.1)
        self.show(w_ratio, run_time=1.1)
        self.at("two_orientation")
        self.show(
            words("Input 1 above · input omega below", size=29, color=YELLOW).move_to(
                DOWN * 3
            ),
            run_time=0.9,
        )

        self.section(
            "candidates", "All three complex-phase candidates remain available"
        )
        self.show(
            formula(
                r"\Delta(c),\Delta(d),\Delta(g)\in\{1,\omega,\omega^2\}",
                size=40,
                color=BLUE_C,
            ).move_to(UP * 2.05),
            run_time=1,
        )
        center = RIGHT * 3.8 + DOWN * 0.25
        circle = Circle(radius=1.25).move_to(center).set_stroke(BLUE_C, 2)
        directions = [
            cos(TAU * k / 3) * RIGHT + sin(TAU * k / 3) * UP for k in range(3)
        ]
        dots = VGroup(
            *(
                Dot(center + 1.25 * direction, radius=0.07).set_color(BLUE_C)
                for direction in directions
            )
        )
        labels = VGroup(
            *(
                formula(tex, size=35, color=BLUE_C).next_to(dot, direction, buff=0.18)
                for tex, dot, direction in zip(
                    ["1", r"\omega", r"\omega^2"], dots, directions, strict=True
                )
            )
        )
        self.show(circle, dots, labels, run_time=1)
        self.at("candidates_divide")
        self.show(
            formula(r"\omega^a/\omega^b=\omega^{a-b}", size=44, color=BLUE_C).move_to(
                LEFT * 3.4 + UP * 0.5
            ),
            formula(r"a,b\in\{0,1,2\},\quad\omega^3=1", size=35).move_to(
                LEFT * 3.4 + DOWN * 0.65
            ),
            run_time=1,
        )
        self.at("candidates_keep")
        set_result = formula(
            r"R,W\in\{1,\omega,\omega^2\}", size=46, color=YELLOW
        ).move_to(DOWN * 2.15)
        self.show(set_result, run_time=0.7)
        self.play(FlashAround(labels, color=YELLOW), run_time=0.5)
        self.at("candidates_phases")
        self.show(
            words(
                "Complex phases · residue reduction modulo 1 + i comes later", size=25
            ).move_to(DOWN * 3.3),
            run_time=0.9,
        )

        self.section(
            "next_condition",
            "Interpret equality conditionally; keep the later steps separate",
        )
        first = formula(
            r"R=1\quad\Longrightarrow\quad\frac{d(1)}{c(1)}=\frac{d(\omega)}{c(\omega)}",
            size=47,
            color=BLUE_C,
        ).move_to(UP * 1.4)
        second = formula(
            r"W=1\quad\Longrightarrow\quad\frac{g(1)}{c(1)}=\frac{g(\omega)}{c(\omega)}",
            size=47,
            color=BLUE_C,
        ).move_to(DOWN * 0.2)
        self.show(first, run_time=1.1)
        self.at("next_w")
        self.show(second, run_time=1.1)
        self.at("next_distinct")
        distinct = words(
            "Each relative ratio would retain its own value", size=28
        ).move_to(DOWN * 1.8)
        self.show(
            distinct,
            words("The three evaluated points need not coincide", size=26).move_to(
                DOWN * 2.85
            ),
            run_time=1,
        )
        self.at("next_pending")
        self.erase(first, second, distinct)
        pending = words(
            "R = W = 1 has not yet been established", size=31, color=YELLOW
        ).move_to(UP * 1.45)
        self.show(pending, run_time=0.9)
        self.at("next_sign")
        self.show(
            words(
                "Node 6.3: the separate sign condition", size=29, color=BLUE_C
            ).move_to(DOWN * 0.1),
            run_time=0.9,
        )
        self.at("next_rigidity")
        self.show(
            words(
                "Node 6.4: combine that condition with odd order", size=27, color=BLUE_C
            ).move_to(DOWN * 1.45),
            run_time=0.9,
        )
        self.play(FlashAround(pending, color=YELLOW), run_time=0.7)
