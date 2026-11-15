import json
from math import cos, sin

from manimlib import (
    BLUE_B,
    BLUE_C,
    BLUE_E,
    DOWN,
    GREY_B,
    LEFT,
    PI,
    RIGHT,
    TAU,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    FlashAround,
    Line,
    Rectangle,
    Square,
    Tex,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words

COLORS = (BLUE_C, BLUE_B, WHITE)


def point(center, radius, angle):
    return center + radius * (cos(angle) * RIGHT + sin(angle) * UP)


def plane(center, radius):
    axes = VGroup(
        Line(center + LEFT * (radius + 0.2), center + RIGHT * (radius + 0.2)),
        Line(center + DOWN * (radius + 0.2), center + UP * (radius + 0.2)),
    ).set_stroke(GREY_B, width=1, opacity=0.6)
    labels = VGroup(
        formula(r"\operatorname{Re}", size=19).move_to(
            center + RIGHT * (radius + 0.4) + DOWN * 0.25
        ),
        formula(r"\operatorname{Im}", size=19).move_to(
            center + UP * (radius + 0.4) + LEFT * 0.27
        ),
    )
    return VGroup(axes, labels, Circle(radius=radius).set_color(BLUE_C).move_to(center))


def value(center, radius, angle, label, color):
    endpoint = point(center, radius, angle)
    marker = Dot(endpoint, radius=0.065).set_color(color)
    ray = Arrow(center, endpoint, buff=0).set_color(color)
    text = formula(label, size=27, color=color)
    text.next_to(marker, endpoint - center, buff=0.2)
    return VGroup(ray, marker), text


def function_box(label, center, color):
    box = Rectangle(width=1.55, height=0.8)
    box.set_stroke(color, width=2).set_fill(BLUE_E, opacity=0.12)
    return VGroup(box, formula(label, size=33, color=color)).move_to(center)


class NormalizedEvaluationNorms(NodeScene):
    node_id = "normalized-evaluation-norms"
    title = "3.5 · Normalize the Norm Identities"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/normalized-evaluation-norms.json").read_text()
        )["detail_cues"]

        self.section("inputs", "Bring two independent checks together")
        self.show(formula(r"\epsilon\in\{1,-1,i\}", size=45).move_to(UP * 1.85))
        norm = formula(
            r"h(\epsilon,P)\bigl(h(\epsilon,P)\bigr)^*=4u^2", size=38, width=7
        )
        norm.move_to(LEFT * 3.8 + UP * 0.45)
        self.at("inputs_norm")
        self.show(norm)
        self.show(
            words("3.3 · Evaluation preserves the norm", size=23, width=6.7).move_to(
                LEFT * 3.8 + DOWN * 1.05
            ),
            run_time=0.8,
        )
        self.at("inputs_parity")
        real = formula(r"2a_j\ \longmapsto\ a_j", size=40).move_to(
            RIGHT * 3.6 + UP * 0.55
        )
        gaussian = formula(
            r"2(a_j+ib_j)\ \longmapsto\ a_j+ib_j", size=31, width=6.7
        ).move_to(RIGHT * 3.6 + DOWN * 0.55)
        self.show(real, gaussian)
        self.show(
            words("3.4 · Exact coefficient halves", size=23).move_to(
                RIGHT * 3.6 + DOWN * 1.55
            ),
            run_time=0.8,
        )
        self.at("inputs_join")
        self.show(
            Arrow(
                LEFT * 3.8 + DOWN * 1.5, LEFT * 0.7 + DOWN * 2.6, buff=0.12
            ).set_color(BLUE_C),
            Arrow(
                RIGHT * 3.6 + DOWN * 1.95, RIGHT * 0.7 + DOWN * 2.6, buff=0.12
            ).set_color(BLUE_C),
            words("Norm data + integral division", size=27, color=YELLOW).move_to(
                DOWN * 3.15
            ),
        )

        self.section(
            "definitions", "Define three polynomials in their coefficient rings"
        )
        sources = VGroup(
            *(
                formula(source, size=39, color=color).move_to(
                    (j - 1) * 4.7 * RIGHT + UP * 1.45
                )
                for j, (source, color) in enumerate(
                    zip([r"h(1,P)", r"h(-1,P)", r"h(i,P)"], COLORS, strict=True)
                )
            )
        )
        definitions = VGroup(
            *(
                formula(source, size=43, color=color, width=4.3).move_to(
                    (j - 1) * 4.7 * RIGHT + DOWN * 0.1
                )
                for j, (source, color) in enumerate(
                    zip(
                        [
                            r"c(P)=\frac{h(1,P)}2",
                            r"d(P)=\frac{h(-1,P)}2",
                            r"g(P)=\frac{h(i,P)}2",
                        ],
                        COLORS,
                        strict=True,
                    )
                )
            )
        )
        self.show(sources, run_time=0.8)
        self.body.add(definitions)
        self.play(
            *(
                TransformFromCopy(a, b)
                for a, b in zip(sources, definitions, strict=True)
            ),
            run_time=0.8,
        )
        self.at("definitions_d")
        self.play(FlashAround(definitions[1], color=YELLOW), run_time=0.6)
        self.at("definitions_g")
        self.play(FlashAround(definitions[2], color=YELLOW), run_time=0.6)
        self.at("definitions_real")
        self.show(
            formula(r"\text{coefficients in }\mathbb Z", size=31, color=BLUE_C).move_to(
                LEFT * 4.7 + DOWN * 1.8
            ),
            formula(r"\text{coefficients in }\mathbb Z", size=31, color=BLUE_B).move_to(
                DOWN * 1.8
            ),
            run_time=0.8,
        )
        self.at("definitions_gaussian")
        self.show(
            formula(r"\text{coefficients in }\mathbb Z[i]", size=31).move_to(
                RIGHT * 4.7 + DOWN * 1.8
            ),
            run_time=0.8,
        )
        self.at("definitions_cycle")
        self.show(
            formula(
                r"P^{u^2}=1\qquad\text{for all three polynomials}", size=35
            ).move_to(DOWN * 3.25),
            run_time=0.8,
        )

        self.section("halves", "One half on each factor gives one quarter")
        self.show(
            formula(r"c(P)c^*(P)", size=51, color=BLUE_C).move_to(
                LEFT * 2.7 + UP * 1.8
            ),
            formula(r"\left(\frac12\right)^*=\frac12", size=43, color=YELLOW).move_to(
                RIGHT * 3.5 + UP * 1.8
            ),
        )
        h = formula(r"h(1,P)", size=47, color=BLUE_C).move_to(LEFT * 2.6 + UP * 0.25)
        hstar = formula(r"\bigl(h(1,P)\bigr)^*", size=47).move_to(
            RIGHT * 2.6 + UP * 0.25
        )
        self.show(h, hstar, formula(r"\cdot", size=45).move_to(UP * 0.25))
        self.at("halves_each")
        first_half = formula(r"\frac12", size=50, color=YELLOW).next_to(
            h, LEFT, buff=0.18
        )
        second_half = formula(r"\frac12", size=50, color=YELLOW).next_to(
            hstar, LEFT, buff=0.18
        )
        self.show(first_half, second_half, run_time=0.8)
        self.at("halves_quarter")
        quarter = Tex(r"\frac14", font_size=53, isolate=["4"]).set_color(YELLOW)
        product = formula(r"h(1,P)\bigl(h(1,P)\bigr)^*", size=38, width=6.3)
        VGroup(quarter, product).arrange(RIGHT, buff=0.3).move_to(DOWN * 1.35)
        self.body.add(quarter, product)
        self.play(
            TransformFromCopy(VGroup(first_half, second_half), quarter),
            TransformFromCopy(VGroup(h, hstar), product),
            run_time=1.1,
        )
        self.at("halves_norm")
        scalar = (
            Tex(r"4u^2", font_size=53, isolate=["4"])
            .set_color(BLUE_C)
            .move_to(RIGHT * 0.65 + DOWN * 1.35)
        )
        self.body.add(scalar)
        self.play(
            TransformFromCopy(product, scalar),
            FadeOut(product),
            quarter.animate.next_to(scalar, LEFT, buff=0.3),
            run_time=1,
        )
        self.body.remove(product)
        self.at("halves_cancel")
        fours = [quarter.get_part_by_tex("4"), scalar.get_part_by_tex("4")]
        strikes = VGroup(
            *(
                Line(four.get_corner(LEFT + DOWN), four.get_corner(RIGHT + UP))
                for four in fours
            )
        ).set_stroke(YELLOW, width=3)
        self.show(strikes, run_time=0.5)
        result = formula(r"\boxed{c(P)c^*(P)=u^2}", size=51, color=YELLOW).move_to(
            DOWN * 2.85
        )
        self.body.add(result)
        self.play(TransformFromCopy(VGroup(quarter, scalar), result), run_time=1)

        self.section("all_three", "The same calculation gives all three norms")
        norms = VGroup(
            *(
                formula(source, size=46, color=color).move_to(UP * (1.65 - 1.3 * j))
                for j, (source, color) in enumerate(
                    zip(
                        [r"c(P)c^*(P)=u^2", r"d(P)d^*(P)=u^2", r"g(P)g^*(P)=u^2"],
                        COLORS,
                        strict=True,
                    )
                )
            )
        )
        self.show(norms[0])
        self.body.add(norms[1], norms[2])
        self.play(
            TransformFromCopy(norms[0], norms[1]),
            TransformFromCopy(norms[0], norms[2]),
            run_time=1.2,
        )
        self.at("all_three_gaussian")
        gaussian_star = formula(
            r"g_jP^j\ \longmapsto\ \overline{g_j}P^{-j}", size=38
        ).move_to(DOWN * 2.4)
        self.show(gaussian_star)
        self.at("all_three_scalar")
        self.show(
            words(
                "Gaussian star still fixes the real scalar 2", size=25, color=YELLOW
            ).move_to(DOWN * 3.45),
            run_time=0.8,
        )

        self.section("numbers", "In the guiding case: 36 divided by 4 is 9")
        self.show(formula(r"u=3,\qquad 4u^2=36", size=47).move_to(UP * 1.9))
        large = (
            Square(side_length=3.3)
            .set_stroke(BLUE_C, width=2)
            .set_fill(BLUE_E, opacity=0.2)
            .move_to(LEFT * 3.7 + DOWN * 0.45)
        )
        label36 = formula("36", size=72, color=BLUE_C).move_to(large)
        self.show(large, label36)
        self.at("numbers_halves")
        small = large.copy().scale(0.5).move_to(RIGHT * 3.7 + DOWN * 0.45)
        label9 = formula("9", size=65, color=YELLOW).move_to(small)
        self.body.add(small, label9)
        self.play(TransformFromCopy(large, small), FadeIn(label9), run_time=1.4)
        self.at("numbers_quarter")
        self.show(
            Arrow(
                LEFT * 1.6 + DOWN * 0.45, RIGHT * 1.6 + DOWN * 0.45, buff=0.1
            ).set_color(YELLOW),
            formula(r"\tfrac12\times\tfrac12=\tfrac14", size=37).move_to(UP * 0.3),
            run_time=0.8,
        )
        self.at("numbers_nine")
        self.show(
            formula(r"\frac{36}{4}=9", size=56, color=YELLOW).move_to(DOWN * 2.7),
            run_time=0.8,
        )
        self.show(
            words("Each factor ÷ 2 · product ÷ 4", size=23).move_to(DOWN * 3.55),
            run_time=0.6,
        )

        self.section("roots", "Evaluate only at allowed roots of unity")
        center = LEFT * 4.2 + DOWN * 0.6
        selected = Dot(point(center, 1.15, TAU / 9), radius=0.07).set_color(YELLOW)
        self.show(
            plane(center, 1.15),
            selected,
            formula(r"\zeta^{u^2}=1", size=46, color=YELLOW).move_to(
                LEFT * 4.2 + UP * 1.7
            ),
            formula(r"f\in\{c,d,g\}", size=38).move_to(RIGHT * 3.2 + UP * 1.7),
        )
        norm = formula(r"f(\zeta)f^*(\zeta)=u^2", size=46).move_to(
            RIGHT * 3.2 + UP * 0.2
        )
        self.show(norm)
        self.at("roots_conjugate")
        self.play(
            Transform(
                norm, formula(r"f(\zeta)\overline{f(\zeta)}=u^2", size=45).move_to(norm)
            ),
            run_time=0.9,
        )
        self.show(
            formula(r"f^*(\zeta)=\overline{f(\zeta)}", size=36, color=BLUE_C).move_to(
                RIGHT * 3.2 + DOWN * 1.15
            ),
            run_time=0.8,
        )
        self.at("roots_squared")
        self.play(
            Transform(norm, formula(r"|f(\zeta)|^2=u^2", size=49).move_to(norm)),
            run_time=0.8,
        )
        self.at("roots_radius")
        self.play(
            Transform(
                norm,
                formula(r"\boxed{|f(\zeta)|=u}", size=53, color=YELLOW).move_to(norm),
            ),
            run_time=0.8,
        )
        self.show(
            words("The root condition is essential", size=25, color=BLUE_C).move_to(
                DOWN * 3.2
            ),
            run_time=0.7,
        )

        self.section("circle", "Separate allowed inputs from normalized outputs")
        left, right = LEFT * 5.4 + DOWN * 0.65, RIGHT * 3.8 + DOWN * 0.65
        inputs = VGroup(
            *(
                Dot(point(left, 0.8, TAU * k / 9), radius=0.045).set_color(
                    YELLOW if k == 1 else BLUE_C
                )
                for k in range(9)
            )
        )
        boxes = VGroup(
            *(
                function_box(label, LEFT * 1.3 + UP * (1.1 - 1.45 * j), color)
                for j, (label, color) in enumerate(
                    zip(["c(P)", "d(P)", "g(P)"], COLORS, strict=True)
                )
            )
        )
        output_plane = plane(right, 1.65)
        self.show(
            plane(left, 0.8),
            inputs,
            output_plane,
            boxes,
            formula("u=3", size=44).move_to(LEFT * 1.3 + UP * 2.0),
            words("Allowed ninth-root inputs", size=23).move_to(LEFT * 5.4 + UP * 1.2),
            words("Outputs · radius 3", size=24).move_to(RIGHT * 3.8 + UP * 1.85),
            words("Phase positions are schematic", size=24, color=BLUE_C).move_to(
                DOWN * 3.6
            ),
        )
        self.at("circle_map")
        tokens = VGroup(
            *(
                inputs[1].copy().set_color(color).move_to(box)
                for box, color in zip(boxes, COLORS, strict=True)
            )
        )
        pairs = [
            value(right, 1.65, angle, label, color)
            for angle, label, color in zip(
                [PI / 6, 8 * PI / 9, 55 * PI / 36],
                [r"c(\zeta)", r"d(\zeta)", r"g(\zeta)"],
                COLORS,
                strict=True,
            )
        ]
        outputs = VGroup(*(pair[0] for pair in pairs))
        labels = VGroup(*(pair[1] for pair in pairs))
        self.body.add(tokens, outputs, labels)
        self.play(
            *(TransformFromCopy(inputs[1], token) for token in tokens), run_time=0.7
        )
        self.play(
            *(
                TransformFromCopy(token, pair[0][1])
                for token, pair in zip(tokens, pairs, strict=True)
            ),
            *(FadeIn(pair[0][0]) for pair in pairs),
            *(FadeIn(pair[1]) for pair in pairs),
            run_time=1.1,
        )
        self.play(FadeOut(tokens), run_time=0.25)
        self.body.remove(tokens)
        self.at("circle_lengths")
        self.show(
            formula(
                r"|c(\zeta)|=|d(\zeta)|=|g(\zeta)|=3", size=38, color=YELLOW, width=8
            ).move_to(LEFT * 2.0 + DOWN * 2.9),
            run_time=0.8,
        )
        self.at("circle_scope")
        self.play(FlashAround(output_plane[2], color=YELLOW), run_time=0.8)
