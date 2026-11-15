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
    YELLOW,
    Arc,
    Arrow,
    Circle,
    DashedLine,
    Dot,
    FadeIn,
    Line,
    Rectangle,
    Rotate,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


def point(center, radius, angle):
    return center + radius * (cos(angle) * RIGHT + sin(angle) * UP)


def plane(center, radius=1.5, circle=True):
    axes = VGroup(
        Line(center + LEFT * (radius + 0.25), center + RIGHT * (radius + 0.25)),
        Line(center + DOWN * (radius + 0.25), center + UP * (radius + 0.25)),
    ).set_stroke(GREY_B, width=1, opacity=0.6)
    labels = VGroup(
        formula(r"\operatorname{Re}", size=20).move_to(
            center + RIGHT * (radius + 0.45) + DOWN * 0.25
        ),
        formula(r"\operatorname{Im}", size=20).move_to(
            center + UP * (radius + 0.45) + LEFT * 0.28
        ),
    )
    result = VGroup(axes, labels)
    if circle:
        result.add(Circle(radius=radius).set_color(BLUE_C).move_to(center))
    return result


def roots(center, radius):
    return VGroup(
        *(
            Dot(point(center, radius, TAU * k / 9), radius=0.035).set_color(
                YELLOW if k == 0 else BLUE_C
            )
            for k in range(9)
        )
    )


def vector(center, radius, angle, label, color=BLUE_C):
    endpoint = point(center, radius, angle)
    marker = Dot(endpoint, radius=0.06).set_color(color)
    ray = Arrow(center, endpoint, buff=0).set_color(color)
    text = formula(label, size=27, color=color)

    def place(mob):
        direction = marker.get_center() - center
        if direction[1] > radius * 0.95 or direction[0] > radius * 0.95:
            direction = UP + RIGHT
        mob.next_to(marker, direction, buff=0.22)

    text.add_updater(place)
    text.update()
    return VGroup(ray, marker), text


def function_box(center, label):
    outline = Rectangle(width=1.5, height=0.85)
    outline.set_stroke(BLUE_C, width=2).set_fill(BLUE_E, opacity=0.15)
    return VGroup(outline, formula(label, size=35)).move_to(center)


class CircleEvaluations(NodeScene):
    node_id = "circle-evaluations"
    title = "4.1 · Evaluations on a Circle"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/circle-evaluations.json").read_text()
        )["detail_cues"]

        self.section("inputs", "Substitute inputs that respect the cycle relation")
        self.show(
            formula(
                r"u>1\text{ odd},\qquad f(P)\in\mathbb Z[i][P]/(P^{u^2}-1)", size=41
            ).move_to(UP * 1.9)
        )
        self.at("inputs_norm")
        self.show(formula(r"f(P)f^*(P)=u^2", size=48, color=BLUE_C).move_to(UP * 0.85))
        left, right = LEFT * 4.7 + DOWN * 1.05, RIGHT * 3.75 + DOWN * 1.05
        self.show(plane(left, radius=0.9), plane(right, radius=1.3, circle=False))
        inputs = roots(left, 0.9)
        self.show(inputs, function_box(DOWN * 1.05, "f(P)"))
        self.at("inputs_relation")
        self.show(
            formula(r"\zeta^{u^2}=1", size=37, color=YELLOW).move_to(
                left + DOWN * 1.65
            ),
            Arrow(left + RIGHT * 1.3, LEFT * 0.95 + DOWN * 1.05, buff=0.1).set_color(
                BLUE_C
            ),
        )
        self.at("inputs_nine")
        self.show(words("u = 3: nine allowed inputs", size=23).move_to(left + UP * 1.8))
        self.show(
            formula(r"\zeta_9^k=e^{2\pi i k/9}", size=30).move_to(DOWN * 3.35),
            run_time=0.8,
        )
        self.at("inputs_goal")
        token = inputs[0].copy()
        self.body.add(token)
        self.play(
            TransformFromCopy(inputs[0], token.move_to(DOWN * 1.05)), run_time=1.3
        )
        self.show(
            words("Where can f(ζ) land?", size=26).move_to(right + UP * 2.25),
            run_time=0.8,
        )

        self.section("star", "Star changes coefficients and powers")
        f = formula(r"f(P)=\sum_j a_jP^j", size=46).move_to(LEFT * 3.6 + UP * 1.2)
        self.show(f)
        coefficient = formula(r"a_j", size=63, color=BLUE_C)
        power = formula(r"P^j", size=63)
        term = (
            VGroup(coefficient, power)
            .arrange(RIGHT, buff=0.18)
            .move_to(RIGHT * 3.7 + UP * 0.7)
        )
        self.show(term)
        self.at("star_coefficient")
        self.play(
            Transform(
                coefficient,
                formula(r"\overline{a_j}", size=63, color=BLUE_C).move_to(coefficient),
            ),
            run_time=0.7,
        )
        self.at("star_power")
        self.play(
            Transform(
                power,
                formula(r"P^{-j}", size=63).next_to(coefficient, RIGHT, buff=0.12),
            ),
            run_time=0.7,
        )
        self.show(
            formula(r"a+bi\longmapsto a-bi", size=38, color=BLUE_C).move_to(
                RIGHT * 3.7 + DOWN * 0.8
            ),
            words("Conjugate the coefficient", size=25).move_to(
                RIGHT * 3.7 + DOWN * 1.65
            ),
        )
        self.show(
            words("Reverse the exponent", size=25).move_to(RIGHT * 3.7 + DOWN * 2.45)
        )
        self.at("star_sum")
        self.show(
            formula(
                r"f^*(P)=\sum_j\overline{a_j}P^{-j}", size=44, color=BLUE_C
            ).move_to(LEFT * 3.6 + DOWN * 0.9)
        )
        self.show(
            formula(r"a_j\in\mathbb Z[i]", size=36).move_to(LEFT * 3.6 + DOWN * 2.4),
            run_time=0.8,
        )

        self.section("substitute", "At roots of unity, star becomes conjugation")
        center = RIGHT * 3.8 + DOWN * 0.55
        term_arrow, term_label = vector(center, 1.35, PI * 0.3, r"a_j\zeta^j")
        self.show(
            plane(center, radius=1.35, circle=False),
            term_arrow,
            term_label,
            words("One evaluated term", size=25).move_to(RIGHT * 3.8 + UP * 1.9),
        )
        self.at("substitute_inverse")
        self.show(
            formula(r"\zeta^{-1}=\overline\zeta", size=50, color=YELLOW).move_to(
                LEFT * 3.6 + UP * 1.6
            ),
            run_time=0.8,
        )
        evaluated = formula(
            r"f^*(\zeta)=\sum_j\overline{a_j}\zeta^{-j}", size=40
        ).move_to(LEFT * 3.6 + UP * 0.1)
        self.show(evaluated, run_time=0.9)
        self.at("substitute_term")
        self.play(
            Transform(
                evaluated,
                formula(
                    r"f^*(\zeta)=\sum_j\overline{a_j}\,\overline\zeta^{\,j}", size=40
                ).move_to(evaluated),
            ),
            run_time=1.1,
        )
        self.at("substitute_reflect")
        conjugate, conjugate_label = vector(
            center, 1.35, -PI * 0.3, r"\overline{a_j\zeta^j}", BLUE_B
        )
        self.body.add(conjugate, conjugate_label)
        self.play(
            TransformFromCopy(term_arrow, conjugate),
            FadeIn(conjugate_label),
            run_time=1.7,
        )
        self.show(
            DashedLine(term_arrow[1].get_center(), conjugate[1].get_center()).set_color(
                GREY_B
            ),
            run_time=0.7,
        )
        self.show(
            words("Reflect across the real axis", size=23).move_to(
                center + DOWN * 1.95
            ),
            run_time=0.8,
        )
        self.at("substitute_sum")
        self.show(
            formula(
                r"\sum_j\overline{a_j\zeta^j}=\overline{\sum_j a_j\zeta^j}", size=36
            ).move_to(LEFT * 3.6 + DOWN * 1.3),
            run_time=1,
        )
        self.show(
            formula(
                r"\boxed{f^*(\zeta)=\overline{f(\zeta)}}", size=48, color=YELLOW
            ).move_to(DOWN * 3.2),
            run_time=1,
        )

        self.section("norm", "The norm fixes distance from the origin")
        left, right = LEFT * 4.7 + DOWN * 0.65, RIGHT * 3.75 + DOWN * 0.65
        evaluated_norm = formula(
            r"f(\zeta)\overline{f(\zeta)}=u^2", size=50, color=BLUE_C
        ).move_to(UP * 1.95)
        self.show(
            plane(left, radius=0.8),
            roots(left, 0.8),
            plane(right, radius=1.5, circle=False),
            evaluated_norm,
        )
        self.show(
            words("Allowed inputs", size=23).move_to(left + UP * 1.65), run_time=0.8
        )
        self.at("norm_squared")
        self.play(
            Transform(
                evaluated_norm,
                formula(r"|f(\zeta)|^2=u^2", size=53, color=BLUE_C).move_to(
                    evaluated_norm
                ),
            ),
            run_time=0.8,
        )
        self.at("norm_radius")
        self.play(
            Transform(
                evaluated_norm,
                formula(r"\boxed{|f(\zeta)|=u>0}", size=52, color=YELLOW).move_to(
                    evaluated_norm
                ),
            ),
            run_time=0.8,
        )
        circle = Circle(radius=1.5).set_color(BLUE_C).move_to(right)
        output, output_label = vector(right, 1.5, PI / 4, r"f(\zeta)")
        self.show(circle, output, output_label)
        self.show(
            words("Outputs: radius u · nonzero", size=25).move_to(right + DOWN * 2.1),
            run_time=0.8,
        )
        self.at("norm_phase")
        self.play(Rotate(output, PI * 0.7, about_point=right), run_time=2)
        self.show(
            words(
                "Fixed magnitude; phase unspecified by this identity", size=24
            ).move_to(DOWN * 3.4),
            run_time=0.8,
        )

        self.section("example", "A valid Gaussian example: f(P) = 3iP")
        left, right = LEFT * 4.7 + DOWN * 0.65, RIGHT * 3.75 + DOWN * 0.65
        self.show(
            formula(r"u=3,\qquad f(P)=3iP", size=51, color=BLUE_C).move_to(
                LEFT * 2 + UP * 1.95
            )
        )
        self.show(plane(left, radius=0.55), plane(right, radius=1.65))
        inputs = roots(left, 0.55)
        self.show(inputs, function_box(DOWN * 0.65, r"\times3i"))
        self.show(
            words("Inputs: |ζ| = 1", size=24).move_to(left + UP * 1.7),
            words("Outputs: |f(ζ)| = 3", size=24).move_to(right + UP * 2.55),
        )
        self.at("example_star")
        self.show(
            formula(r"f^*(P)=-3iP^{-1},\qquad ff^*=9", size=39).move_to(DOWN * 2.7),
            run_time=1,
        )
        self.at("example_scope")
        self.show(
            words("Gaussian example; not a Hadamard sign row", size=24).move_to(
                DOWN * 3.45
            ),
            run_time=0.8,
        )

        self.wait_until_narration(self.cues["map"])
        mapped = inputs.copy().shift(right - left)
        arrow = Arrow(right, right + RIGHT * 0.55, buff=0).set_color(YELLOW)
        self.body.add(mapped)
        self.play(TransformFromCopy(inputs, mapped), run_time=1.8)
        self.show(arrow, run_time=0.7)
        self.at("map_rotate")
        self.play(
            Rotate(mapped, PI / 2, about_point=right),
            Rotate(arrow, PI / 2, about_point=right),
            run_time=1.6,
        )
        self.at("map_scale")
        self.play(
            mapped.animate.scale(3, about_point=right),
            arrow.animate.scale(3, about_point=right),
            run_time=1.6,
        )
        self.at("map_outputs")
        self.show(
            formula(r"f(1)=3i", size=28, color=YELLOW).next_to(
                mapped[0], UP + RIGHT, buff=0.22
            ),
            run_time=0.8,
        )
        self.show(
            formula(r"f(\zeta_9^k)=3i\zeta_9^k", size=34).move_to(
                LEFT * 3.8 + DOWN * 2.0
            ),
            run_time=0.8,
        )

        self.section("quotient", "The quotient records denominator → numerator")
        left, right = LEFT * 3.85 + DOWN * 0.65, RIGHT * 3.85 + DOWN * 0.65
        numerator, numerator_label = vector(left, 1.5, PI / 2, r"f(1)=3i")
        denominator, denominator_label = vector(
            left, 1.5, 7 * PI / 6, r"f(\omega)", BLUE_B
        )
        quotient = formula(
            r"q=\frac{f(1)}{f(\omega)}=\frac{3i}{3i\omega}", size=47, color=YELLOW
        ).move_to(UP * 2.1)
        self.show(
            plane(left, radius=1.5),
            plane(right, radius=1.5),
            numerator,
            numerator_label,
            denominator,
            denominator_label,
            quotient,
        )
        self.at("quotient_omega")
        self.show(
            formula(r"\omega=e^{2\pi i/3}", size=31).move_to(UP * 0.25), run_time=0.8
        )
        self.at("quotient_magnitude")
        self.show(formula(r"|q|=\frac33=1", size=40).move_to(DOWN * 2.2), run_time=0.8)
        reference, reference_label = vector(right, 1.5, 0, "1", GREY_B)
        self.show(reference, reference_label, run_time=0.8)
        self.show(
            words("Original outputs · radius 3", size=24).move_to(
                LEFT * 3.85 + DOWN * 3.1
            ),
            words("Quotient · radius 1", size=24).move_to(RIGHT * 3.85 + DOWN * 3.1),
            run_time=0.8,
        )
        self.at("quotient_phase")
        phase = Arc(start_angle=7 * PI / 6, angle=-TAU / 3, radius=0.85)
        phase.add_tip(length=0.13, width=0.12).set_color(YELLOW).shift(left)
        self.show(phase, run_time=0.8)
        self.at("quotient_turn")
        q, q_label = vector(right, 1.5, 0, r"\omega^2", BLUE_C)
        q_label.set_opacity(0)
        self.body.add(q, q_label)
        self.play(TransformFromCopy(reference, q), run_time=0.4)
        self.play(Rotate(q, -TAU / 3, about_point=right), run_time=1.5)
        self.play(
            q_label.animate.set_opacity(1),
            Transform(
                quotient,
                formula(r"q=\omega^{-1}=\omega^2", size=49, color=YELLOW).move_to(
                    quotient
                ),
            ),
            run_time=0.8,
        )
        self.at("quotient_scope")
        self.show(
            words(
                "Equal magnitudes alone leave the phase unrestricted", size=23
            ).move_to(DOWN * 3.65),
            run_time=0.8,
        )
