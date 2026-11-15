import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    Arrow,
    Circle,
    Dot,
    FadeOut,
    FlashAround,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class EvaluateFourCycle(NodeScene):
    node_id = "evaluate-four-cycle"
    title = "3.3 · Evaluate at 1, −1, and i"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def columns(self):
        positions = [-4.8, -1.6, 1.6, 4.8]
        polynomials = VGroup(
            *(
                formula(rf"H_{a}(P)", size=42, color=BLUE_C).move_to(
                    RIGHT * x + UP * 0.95
                )
                for a, x in enumerate(positions)
            )
        )
        weights = VGroup(
            *(
                formula(tex, size=47).move_to(RIGHT * x + DOWN * 0.1)
                for x, tex in zip(positions, ["1", "Z", "Z^2", "Z^3"], strict=True)
            )
        )
        return VGroup(polynomials, weights), weights

    def replace_weights(self, weights, values):
        self.play(
            *(
                Transform(weight, formula(value, size=47, color=YELLOW).move_to(weight))
                for weight, value in zip(weights, values, strict=True)
            ),
            run_time=1.1,
        )

    def copy_term(self, source, target, run_time=0.9):
        self.body.add(target)
        self.play(TransformFromCopy(source, target), run_time=run_time)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/evaluate-four-cycle.json").read_text()
        )["detail_cues"]

        self.section("goal", "Substitute only Z; keep the polynomial variable P")
        center = LEFT * 3.7 + DOWN * 0.1
        roots = VGroup(
            *(
                Dot(center + 1.35 * direction, radius=0.065).set_color(BLUE_C)
                for direction in [RIGHT, UP, LEFT, DOWN]
            )
        )
        circle = Circle(radius=1.35).move_to(center).set_stroke(BLUE_C, width=2)
        labels = VGroup(
            *(
                formula(tex, size=39, color=BLUE_C).next_to(point, direction, buff=0.15)
                for tex, point, direction in zip(
                    ["1", "i", "-1", "-i"], roots, [RIGHT, UP, LEFT, DOWN], strict=True
                )
            )
        )
        self.show(
            circle,
            roots,
            labels,
            formula("Z^4=1", size=45).move_to(LEFT * 3.7 + UP * 2.25),
            run_time=1,
        )
        value = formula("h(Z,P)", size=62, color=BLUE_C).move_to(
            RIGHT * 3.4 + UP * 0.65
        )
        self.show(value, run_time=0.8)
        self.at("goal_keep_p")
        self.show(
            words("P stays unchanged", size=31, color=YELLOW).move_to(
                RIGHT * 3.4 + DOWN * 0.65
            ),
            formula(r"P^{u^2}=1", size=36, color=BLUE_C).move_to(
                RIGHT * 3.4 + DOWN * 1.7
            ),
            run_time=0.8,
        )
        self.at("goal_roots")
        for index in [0, 2, 1]:
            self.play(
                roots[index].animate.set_color(YELLOW),
                labels[index].animate.set_color(YELLOW),
                run_time=0.3,
            )
        self.at("goal_maps")
        self.play(
            Transform(
                value, formula(r"h(\epsilon,P)", size=62, color=BLUE_C).move_to(value)
            ),
            run_time=0.9,
        )
        self.show(
            formula(r"\epsilon\in\{1,-1,i\}", size=40, color=YELLOW).move_to(
                RIGHT * 3.4 + UP * 1.8
            ),
            run_time=0.8,
        )

        self.section("at_one", "At Z = 1: add all four sign polynomials")
        decomposition = formula(
            r"h(Z,P)=H_0(P)+ZH_1(P)+Z^2H_2(P)+Z^3H_3(P)", size=33
        ).move_to(UP * 2.05)
        columns, weights = self.columns()
        self.show(decomposition, columns, run_time=1)
        self.show(
            words(
                "Each H-polynomial is multiplied by its weight below.", size=25
            ).move_to(DOWN * 1.05),
            run_time=0.7,
        )
        self.at("one_weights")
        self.replace_weights(weights, ["1", "1", "1", "1"])
        self.at("one_sum")
        self.show(
            formula(
                r"h(1,P)=H_0(P)+H_1(P)+H_2(P)+H_3(P)", size=44, color=YELLOW
            ).move_to(DOWN * 2.2),
            run_time=1,
        )

        self.section("at_minus_one", "At Z = −1: alternate the weights")
        columns, weights = self.columns()
        self.show(
            columns,
            formula("Z=-1", size=48, color=BLUE_C).move_to(UP * 2.05),
            run_time=0.9,
        )
        self.at("minus_weights")
        self.replace_weights(weights, ["1", "-1", "1", "-1"])
        self.at("minus_sum")
        self.show(
            formula(
                r"h(-1,P)=H_0(P)-H_1(P)+H_2(P)-H_3(P)", size=43, color=YELLOW
            ).move_to(DOWN * 1.7),
            run_time=1,
        )
        self.at("minus_integer")
        self.show(
            words(
                "Both real substitutions have integer coefficients.", size=25
            ).move_to(DOWN * 2.8),
            run_time=0.8,
        )

        self.section("at_i", "At Z = i: separate real and imaginary parts")
        columns, weights = self.columns()
        self.show(
            columns,
            formula(r"i^2=-1,\qquad i^3=-i", size=42, color=BLUE_C).move_to(UP * 2.05),
            run_time=0.9,
        )
        self.at("i_weights")
        self.replace_weights(weights, ["1", "i", "-1", "-i"])
        real = formula(r"H_0(P)-H_2(P)", size=43, color=BLUE_C)
        imaginary = formula(r"i(H_1(P)-H_3(P))", size=43, color=YELLOW)
        result = (
            VGroup(formula("h(i,P)=", size=43), real, formula("+", size=43), imaginary)
            .arrange(RIGHT, buff=0.3)
            .move_to(DOWN * 1.65)
        )
        if result.get_width() > 12:
            result.set_width(12)
        self.at("i_collect_real")
        self.show(result[0], real, run_time=0.8)
        self.at("i_collect_imaginary")
        self.show(result[2], imaginary, run_time=0.8)
        self.at("i_gaussian")
        self.show(
            words("Gaussian-integer coefficients", size=29, color=BLUE_C).move_to(
                DOWN * 2.85
            ),
            run_time=0.8,
        )

        self.section(
            "coefficient_conjugation", "The fourth evaluation is already determined"
        )
        original = formula(
            r"h(i,P)=H_0(P)-H_2(P)+i(H_1(P)-H_3(P))", size=43, color=BLUE_C
        ).move_to(UP * 1.5)
        conjugate = original.copy().move_to(UP * 0.1)
        self.show(original, conjugate, run_time=0.8)
        self.at("conjugation_coefficients")
        self.play(
            Transform(
                conjugate,
                formula(
                    r"h(-i,P)=H_0(P)-H_2(P)-i(H_1(P)-H_3(P))", size=43, color=YELLOW
                ).move_to(conjugate),
            ),
            run_time=1.1,
        )
        self.at("conjugation_p_fixed")
        self.show(
            formula(r"P^b\longmapsto P^b", size=43, color=BLUE_C).move_to(DOWN * 1.25),
            run_time=0.8,
        )
        self.at("conjugation_star")
        self.play(FadeOut(self.body), run_time=0.4)
        self.body = VGroup()
        self.show(
            formula(
                r"f^*(P)=\sum_b\overline{f_b}P^{-b}", size=50, color=YELLOW
            ).move_to(UP * 1.55),
            run_time=0.8,
        )
        self.show(
            words("Coefficient conjugation", size=26).move_to(LEFT * 3.7 + UP * 0.25),
            words("Star", size=26).move_to(RIGHT * 3.7 + UP * 0.25),
            formula(r"P^b\mapsto P^b", size=46, color=BLUE_C).move_to(
                LEFT * 3.7 + DOWN * 0.9
            ),
            formula(r"P^b\mapsto P^{-b}", size=46, color=YELLOW).move_to(
                RIGHT * 3.7 + DOWN * 0.9
            ),
            run_time=0.9,
        )
        self.show(
            words(
                "Both conjugate the coefficients; star also reverses P.", size=25
            ).move_to(DOWN * 2.45),
            run_time=0.8,
        )

        self.section(
            "evaluate_then_star",
            "Follow the same real-coefficient term along two paths",
        )
        self.show(
            formula(
                r"\epsilon\in\{1,-1,i\},\qquad h_{a,b}\text{ real}",
                size=31,
                color=BLUE_C,
            ).move_to(UP * 2.2),
            run_time=0.8,
        )
        term = formula(r"h_{a,b}Z^aP^b", size=54, color=BLUE_C).move_to(UP * 1.15)
        self.at("path_original")
        self.show(term, run_time=0.8)
        evaluated = formula(r"h_{a,b}\epsilon^aP^b", size=46, color=BLUE_C).move_to(
            LEFT * 3.5 + DOWN * 0.35
        )
        left_endpoint = formula(
            r"h_{a,b}\overline{\epsilon}^{\,a}P^{-b}", size=45, color=YELLOW
        ).move_to(LEFT * 3.5 + DOWN * 2)
        self.at("path_evaluate")
        self.show(
            Arrow(term.get_bottom(), evaluated.get_top(), buff=0.18).set_color(BLUE_C),
            words("evaluate Z", size=23).move_to(LEFT * 2.85 + UP * 0.65),
            run_time=0.6,
        )
        self.copy_term(term, evaluated)
        self.at("path_star_after")
        self.show(
            Arrow(evaluated.get_bottom(), left_endpoint.get_top(), buff=0.18).set_color(
                BLUE_C
            ),
            words("star", size=24).move_to(LEFT * 4.75 + DOWN * 1.15),
            run_time=0.6,
        )
        self.copy_term(evaluated, left_endpoint)

        self.wait_until_narration(self.cues["star_then_evaluate"])
        self.play(
            Transform(
                self.subtitle,
                words(
                    "The two paths have equal endpoints", size=25, color=BLUE_C
                ).next_to(self.heading, DOWN, buff=0.25),
            ),
            run_time=0.35,
        )
        starred = formula(r"h_{a,b}Z^{-a}P^{-b}", size=46, color=BLUE_C).move_to(
            RIGHT * 3.5 + DOWN * 0.35
        )
        right_endpoint = formula(
            r"h_{a,b}\epsilon^{-a}P^{-b}", size=45, color=YELLOW
        ).move_to(RIGHT * 3.5 + DOWN * 2)
        self.at("path_star_first")
        self.show(
            Arrow(term.get_bottom(), starred.get_top(), buff=0.18).set_color(BLUE_C),
            words("star", size=24).move_to(RIGHT * 2.85 + UP * 0.65),
            run_time=0.6,
        )
        self.copy_term(term, starred)
        self.at("path_evaluate_after")
        self.show(
            Arrow(starred.get_bottom(), right_endpoint.get_top(), buff=0.18).set_color(
                BLUE_C
            ),
            words("evaluate Z", size=23).move_to(RIGHT * 5.1 + DOWN * 1.15),
            run_time=0.6,
        )
        self.copy_term(starred, right_endpoint)
        identity = formula(
            r"\overline{\epsilon}=\epsilon^{-1}", size=42, color=BLUE_C
        ).move_to(DOWN * 3.15)
        self.at("path_equal")
        self.show(
            identity,
            formula("=", size=52, color=YELLOW).move_to(DOWN * 2),
            run_time=0.8,
        )
        self.play(
            Transform(
                right_endpoint,
                formula(
                    r"h_{a,b}\overline{\epsilon}^{\,a}P^{-b}", size=45, color=YELLOW
                ).move_to(right_endpoint),
            ),
            run_time=0.8,
        )
        self.at("path_commutes")
        self.play(
            Transform(
                identity,
                formula(
                    r"h^*(\epsilon,P)=(h(\epsilon,P))^*", size=41, color=BLUE_C
                ).move_to(identity),
            ),
            run_time=0.9,
        )

        self.section("norm", "Evaluation preserves multiplication and star")
        product = formula(r"h(Z,P)h^*(Z,P)=4u^2", size=55, color=BLUE_C).move_to(
            UP * 1.15
        )
        self.show(product, run_time=0.9)
        self.at("norm_evaluate")
        self.play(
            Transform(
                product,
                formula(
                    r"h(\epsilon,P)h^*(\epsilon,P)=4u^2", size=52, color=BLUE_C
                ).move_to(product),
            ),
            run_time=1,
        )
        self.at("norm_own_star")
        self.play(
            Transform(
                product,
                formula(
                    r"h(\epsilon,P)(h(\epsilon,P))^*=4u^2", size=50, color=YELLOW
                ).move_to(product),
            ),
            run_time=1,
        )
        self.at("norm_p_relation")
        self.show(
            formula(r"P^{u^2}=1", size=45, color=BLUE_C).move_to(DOWN * 0.3),
            run_time=0.8,
        )
        self.at("norm_three")
        self.show(
            formula(r"\epsilon\in\{1,-1,i\}", size=43).move_to(DOWN * 1.45),
            run_time=0.8,
        )
        self.show(
            words("The same scalar 4u² survives all three maps.", size=27).move_to(
                DOWN * 2.6
            ),
            run_time=0.8,
        )

        self.section("preview", "Parity must justify the next normalization")
        preview = formula(
            r"u=3:\qquad h(\epsilon,P)(h(\epsilon,P))^*=36", size=49, color=BLUE_C
        ).move_to(UP * 0.9)
        self.show(preview, run_time=0.9)
        self.at("preview_parity")
        condition = words(
            "Next: parity permits integral halving", size=29, color=YELLOW
        ).move_to(UP * 2.05)
        self.show(condition, run_time=0.8)
        self.at("preview_halve")
        halved = formula(
            r"\frac{h(\epsilon,P)}2\,\frac{(h(\epsilon,P))^*}2=\frac{36}4=9",
            size=49,
            color=BLUE_C,
        ).move_to(DOWN * 0.55)
        self.show(halved, run_time=1)
        self.at("preview_next")
        self.show(
            words("Integrality is proved in the next node.", size=27).move_to(
                DOWN * 2.1
            ),
            run_time=0.8,
        )
        self.play(FlashAround(condition, color=YELLOW), run_time=0.8)
