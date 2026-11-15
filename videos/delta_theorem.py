import json
from math import cos, hypot, sin

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
    Arc,
    Arrow,
    Circle,
    Dot,
    LaggedStart,
    Line,
    Rectangle,
    Rotate,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


def position(center, radius, angle):
    return center + radius * (cos(angle) * RIGHT + sin(angle) * UP)


def plot(center, radius=1.55, unit="1"):
    circle = Circle(radius=radius).set_color(BLUE_C).move_to(center)
    axes = VGroup(
        Line(center + LEFT * (radius + 0.35), center + RIGHT * (radius + 0.35)),
        Line(center + DOWN * (radius + 0.35), center + UP * (radius + 0.35)),
    ).set_stroke(GREY_B, width=1)
    labels = VGroup(
        formula(r"\operatorname{Re}", size=20).next_to(axes[0], RIGHT, buff=0.08),
        formula(r"\operatorname{Im}", size=20).next_to(axes[1], UP, buff=0.08),
        formula(unit, size=25).move_to(center + radius * RIGHT + DOWN * 0.3),
    )
    return VGroup(axes, circle, labels)


def vector(center, angle, label, color=BLUE_C, radius=1.55):
    endpoint = position(center, radius, angle)
    point = Dot(endpoint, radius=0.065).set_color(color)
    arrow = Arrow(center, endpoint, buff=0).set_color(color)
    text = formula(label, size=27, color=color)

    def place_label(mob):
        direction = point.get_center() - center
        unit = direction / hypot(direction[0], direction[1])
        if unit[1] > 0.95 or unit[0] > 0.95:
            direction = UP + RIGHT
        mob.next_to(point, direction, buff=0.25)

    text.add_updater(place_label)
    text.update()
    return VGroup(arrow, point), text


def card(text, center, color=BLUE_C, width=4.6):
    box = Rectangle(width=width, height=0.85)
    box.set_stroke(color, width=2).set_fill(BLUE_E, opacity=0.12)
    label = words(text, size=25, color=color, width=width - 0.3)
    return VGroup(box, label).move_to(center)


def arithmetic_caption():
    return (
        VGroup(
            words("Arithmetic comparison", size=24),
            words("of the evaluations", size=24),
        )
        .arrange(DOWN, buff=0.12)
        .move_to(RIGHT * 4.8 + DOWN * 1.2)
    )


class DeltaTheorem(NodeScene):
    node_id = "delta-theorem"
    title = "4 · The Δ-Theorem"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/delta-theorem.json").read_text()
        )["detail_cues"]

        self.section("opening", "An independent arithmetic ingredient")
        arithmetic = card("4 · The Δ-theorem", RIGHT * 3.6 + UP * 0.7)
        signs = card("The original Hadamard signs", LEFT * 3.6 + UP * 0.7, GREY_B)
        congruences = card("5 · Sign congruences", LEFT * 3.6 + DOWN * 1.25, GREY_B)
        destination = card("6 · Combine the two ingredients", RIGHT * 3.6 + DOWN * 1.25)
        self.show(signs, congruences, arithmetic, destination)
        self.show(
            Arrow(signs.get_bottom(), congruences.get_top(), buff=0.12).set_color(
                GREY_B
            ),
            Arrow(arithmetic.get_bottom(), destination.get_top(), buff=0.12).set_color(
                YELLOW
            ),
            Arrow(congruences.get_right(), destination.get_left(), buff=0.15).set_color(
                GREY_B
            ),
        )
        self.at("opening_gaussian")
        self.show(
            formula(
                r"g(P)\in\mathbb Z[i][P]/(P^{u^2}-1)", size=44, color=BLUE_C
            ).move_to(DOWN * 2.85)
        )

        self.section("circle", "The norm fixes output magnitudes")
        left, right = LEFT * 4.7 + DOWN * 0.55, RIGHT * 3.7 + DOWN * 0.55
        input_plot = plot(left, radius=1.05)
        output_plot = plot(right, radius=1.55, unit="3")
        inputs = VGroup(
            *(
                Dot(position(left, 1.05, TAU * k / 9), radius=0.055).set_color(BLUE_C)
                for k in range(9)
            )
        )
        self.show(input_plot, inputs, output_plot)
        self.show(
            card("f", DOWN * 0.55, width=1.2),
            Arrow(left + RIGHT * 1.4, LEFT * 0.8 + DOWN * 0.55, buff=0.1).set_color(
                BLUE_C
            ),
            Arrow(RIGHT * 0.8 + DOWN * 0.55, right + LEFT * 1.9, buff=0.1).set_color(
                BLUE_C
            ),
        )
        self.show(
            formula(r"ff^*=9\quad\text{in }\mathbb Z[i][P]/(P^9-1)", size=44).move_to(
                UP * 1.9
            )
        )
        self.at("circle_conjugate")
        norm = formula(r"f(\zeta)\overline{f(\zeta)}=9", size=43, color=BLUE_C)
        norm.move_to(DOWN * 2.7)
        self.show(norm)
        self.at("circle_radius")
        self.play(
            Transform(
                norm, formula(r"|f(\zeta)|=3", size=53, color=YELLOW).move_to(norm)
            ),
            run_time=0.9,
        )
        representative = Dot(position(right, 1.55, PI / 2), radius=0.08)
        representative.set_color(YELLOW)
        self.show(representative)
        self.show(
            formula(r"\text{Inputs: }\zeta^9=1", size=28).move_to(left + DOWN * 1.8),
            words("Outputs: f(ζ)", size=24).move_to(right + DOWN * 2.05),
        )

        self.section("example", "A concrete Gaussian group-ring example")
        left, right = LEFT * 4.7 + DOWN * 0.75, RIGHT * 3.7 + DOWN * 0.75
        self.show(plot(left, radius=1.05), plot(right, radius=1.55, unit="3"))
        self.show(formula(r"f(P)=3iP", size=54, color=BLUE_C).move_to(UP * 2.05))
        self.at("example_star")
        self.show(
            formula(r"f^*(P)=-3iP^{-1},\qquad ff^*=9", size=43).move_to(UP * 1.15)
        )
        inputs = VGroup(
            *(
                Dot(position(left, 1.05, TAU * k / 9), radius=0.055).set_color(BLUE_C)
                for k in range(9)
            )
        )
        outputs = VGroup(
            *(
                Dot(
                    position(right, 1.55, PI / 2 + TAU * k / 9), radius=0.065
                ).set_color(BLUE_C)
                for k in range(9)
            )
        )
        self.show(
            inputs,
            VGroup(
                card("", DOWN * 0.75, width=1.5),
                formula(r"\times3i", size=34).move_to(DOWN * 0.75),
            ),
        )
        self.at("example_map")
        self.body.add(outputs)
        self.play(
            LaggedStart(
                *(
                    TransformFromCopy(a, b)
                    for a, b in zip(inputs, outputs, strict=True)
                ),
                lag_ratio=0.12,
            ),
            run_time=3,
        )
        self.show(
            formula(r"f(\zeta_9^k)=3i\zeta_9^k", size=36).move_to(right + DOWN * 2.1)
        )
        self.at("example_scope")
        self.show(
            words("Equal spacing is specific to this f.", size=24, width=6).move_to(
                LEFT * 3.7 + DOWN * 2.8
            ),
            words("Gaussian example; not a Hadamard sign row.", size=25).move_to(
                DOWN * 3.4
            ),
        )

        self.section("quotient", "Divide magnitudes; subtract phases")
        left, right = LEFT * 3.8 + DOWN * 0.7, RIGHT * 3.8 + DOWN * 0.7
        self.show(plot(left, unit="3"), plot(right))
        numerator, num_label = vector(left, PI / 2, r"f(1)", BLUE_C)
        denominator, den_label = vector(left, 7 * PI / 6, r"f(\omega)", BLUE_B)
        self.show(numerator, num_label, denominator, den_label)
        self.at("quotient_define")
        quotient = formula(r"\Delta(f)=\frac{f(1)}{f(\omega)}", size=53, color=YELLOW)
        quotient.move_to(UP * 1.9)
        self.show(quotient)
        self.show(
            formula(r"\omega=e^{2\pi i/3}", size=36, color=BLUE_C).move_to(UP * 0.55)
        )
        self.at("quotient_magnitudes")
        magnitude = formula(r"|\Delta(f)|=\frac{3}{3}=1", size=44)
        magnitude.move_to(DOWN * 2.9)
        self.show(magnitude)
        self.at("quotient_direction")
        arc = Arc(start_angle=7 * PI / 6, angle=-TAU / 3, radius=1.0)
        arc.add_tip(length=0.14, width=0.12).set_color(YELLOW).shift(left)
        self.show(arc)
        self.show(words("Denominator → numerator", size=25).move_to(right + UP * 1.95))

        self.section("direction", "The quotient is a separate point on the unit circle")
        left, right = LEFT * 3.8 + DOWN * 0.65, RIGHT * 3.8 + DOWN * 0.65
        self.show(plot(left, unit="3"), plot(right))
        numerator, num_label = vector(left, PI / 2, r"f(1)=3i", BLUE_C)
        denominator, den_label = vector(left, 7 * PI / 6, r"f(\omega)=3i\omega", BLUE_B)
        self.show(numerator, num_label, denominator, den_label)
        angle = formula(r"90^\circ-210^\circ=-120^\circ", size=43, color=YELLOW)
        angle.move_to(UP * 1.9)
        self.show(angle)
        quotient, quotient_label = vector(right, 0, r"\text{reference}", GREY_B)
        self.show(quotient, quotient_label)
        self.at("direction_turn")
        moving = denominator.copy().set_color(YELLOW)
        self.show(moving)
        quotient.set_color(YELLOW)
        self.remove(quotient_label)
        self.body.remove(quotient_label)
        self.play(
            Rotate(moving, -TAU / 3, about_point=left),
            Rotate(quotient, -TAU / 3, about_point=right),
            run_time=2.6,
        )
        delta_label = formula(r"\Delta(f)=\omega^2", size=28, color=YELLOW)
        delta_label.add_updater(
            lambda mob: mob.next_to(
                quotient[1], quotient[1].get_center() - right, buff=0.13
            )
        )
        self.show(delta_label)
        arc_left = Arc(start_angle=7 * PI / 6, angle=-TAU / 3, radius=0.95)
        arc_right = Arc(start_angle=0, angle=-TAU / 3, radius=0.95)
        self.show(
            arc_left.add_tip(length=0.14, width=0.12).set_color(YELLOW).shift(left),
            arc_right.add_tip(length=0.14, width=0.12).set_color(YELLOW).shift(right),
        )
        self.show(
            formula(
                r"\Delta(f)=\frac{3i}{3i\omega}=\omega^{-1}=\omega^2",
                size=43,
                color=YELLOW,
            ).move_to(DOWN * 3.05)
        )

        self.section(
            "primes", "Index evaluations by subsets of distinct prime divisors"
        )
        self.show(
            formula(
                r"u>1\text{ odd},\qquad I=\{p:p\mid u,\ p\text{ prime}\}",
                size=43,
                color=BLUE_C,
            ).move_to(UP * 1.65)
        )
        primes = formula(
            r"p\in I\quad\longmapsto\quad\zeta_p\text{ primitive of order }p", size=40
        ).move_to(UP * 0.35)
        self.show(primes)
        self.at("primes_subset")
        roots = formula(
            r"\zeta_S=\prod_{p\in S}\zeta_p,\qquad\zeta_\varnothing=1",
            size=48,
            color=YELLOW,
        ).move_to(DOWN * 1.1)
        self.show(roots)
        self.show(formula(r"\zeta_S^{u^2}=1", size=47).move_to(DOWN * 2.65))

        self.section("product", "Even subsets multiply; odd subsets divide")
        self.show(
            formula(
                r"f\in\mathbb Z[i][P]/(P^{u^2}-1),\quad ff^*=u^2", size=43, color=BLUE_C
            ).move_to(UP * 1.75)
        )
        self.show(formula(r"|f(\zeta_S)|=u>0", size=43).move_to(UP * 0.7))
        self.at("product_define")
        product = formula(
            r"\Delta(f)=\prod_{S\subseteq I}f(\zeta_S)^{(-1)^{|S|}}",
            size=51,
            color=YELLOW,
        ).move_to(DOWN * 0.55)
        self.show(product)
        self.play(
            Transform(
                product,
                formula(
                    r"\Delta(f)=\frac{\prod_{|S|\text{ even}}f(\zeta_S)}"
                    r"{\prod_{|S|\text{ odd}}f(\zeta_S)}",
                    size=50,
                    color=YELLOW,
                ).move_to(product),
            ),
            run_time=1.2,
        )
        self.show(
            words("The empty subset contributes f(1) above the line.", size=26).move_to(
                DOWN * 2.75
            )
        )

        self.section(
            "two_primes", "One prime gives a ratio; two give a ratio of ratios"
        )
        special = formula(
            r"u=3:\quad I=\{3\},\quad\Delta(f)=\frac{f(1)}{f(\omega)}",
            size=43,
            color=BLUE_C,
        ).move_to(UP * 1.9)
        self.show(special)
        labels = [
            r"\varnothing:\ f(1)",
            r"\{p\}:\ f(\zeta_p)",
            r"\{q\}:\ f(\zeta_q)",
            r"\{p,q\}:\ f(\zeta_p\zeta_q)",
        ]
        positions = [
            LEFT * 4.1 + UP * 0.55,
            RIGHT * 1.6 + UP * 0.55,
            LEFT * 4.1 + DOWN * 0.8,
            RIGHT * 1.6 + DOWN * 0.8,
        ]
        subsets = VGroup(
            *(
                formula(label, size=35, color=BLUE_C).move_to(point)
                for label, point in zip(labels, positions, strict=True)
            )
        )
        self.at("two_primes_square")
        self.show(subsets)
        self.play(
            subsets[0].animate.set_color(YELLOW),
            subsets[3].animate.set_color(YELLOW),
            run_time=0.5,
        )
        numerator = formula(r"f(1)f(\zeta_p\zeta_q)", size=42, color=YELLOW)
        numerator.move_to(DOWN * 1.95)
        denominator = formula(r"f(\zeta_p)f(\zeta_q)", size=42).move_to(DOWN * 2.9)
        bar = Line(LEFT * 2.7 + DOWN * 2.43, RIGHT * 2.7 + DOWN * 2.43)
        bar.set_color(WHITE)
        self.body.add(numerator, denominator)
        self.show(
            bar,
            formula(r"\Delta(f)=", size=44, color=YELLOW).move_to(
                LEFT * 4.2 + DOWN * 2.43
            ),
        )
        self.play(
            TransformFromCopy(VGroup(subsets[0], subsets[3]), numerator),
            TransformFromCopy(VGroup(subsets[1], subsets[2]), denominator),
            run_time=1.5,
        )
        self.at("two_primes_phase")
        self.show(
            words("Multiply/divide values: add/subtract phases.", size=25).move_to(
                DOWN * 3.6
            )
        )

        self.section("kronecker", "Two arithmetic inputs allow Kronecker's theorem")
        upper = card("Every conjugate has modulus 1", UP * 1.1, width=7.0)
        lower = card("Δ(f) is an algebraic integer", DOWN * 0.2, width=7.0)
        self.show(upper)
        self.at("kronecker_cancel")
        cancellation = formula(
            r"|\sigma(\Delta(f))|=\frac{u^{2^{|I|-1}}}"
            r"{u^{2^{|I|-1}}}=1",
            size=42,
            color=BLUE_C,
        )
        cancellation.move_to(RIGHT * 5.6 + UP * 0.45)
        cancellation.set_width(3.8)
        self.show(cancellation)
        self.at("kronecker_integral")
        self.show(lower)
        self.show(arithmetic_caption())
        self.at("kronecker_apply")
        conclusion = formula(
            r"\Delta(f)\text{ is a root of unity}", size=48, color=YELLOW
        ).move_to(DOWN * 2.7)
        self.show(
            Arrow(lower.get_bottom(), conclusion.get_top(), buff=0.2).set_color(YELLOW),
            conclusion,
        )
        self.show(
            words("Kronecker's theorem", size=26).move_to(LEFT * 3.5 + DOWN * 1.8)
        )

        self.section("odd_order", "Odd order needs the separate congruence argument")
        root = formula(
            r"\Delta(f)\text{ is a root of unity}", size=43, color=BLUE_C
        ).move_to(UP * 1.85)
        self.show(root)
        self.show(
            words("Congruences at the odd primes", size=26, color=YELLOW).move_to(
                UP * 0.95
            )
        )
        self.at("odd_order_conclusion")
        self.show(
            formula(
                r"\Longrightarrow\quad\Delta(f)\text{ has odd order}",
                size=34,
                color=YELLOW,
                width=7,
            ).move_to(RIGHT * 3 + UP * 0.15)
        )
        left, right = LEFT * 3.8 + DOWN * 1.0, RIGHT * 3.0 + DOWN * 1.15
        self.at("odd_order_three")
        self.show(plot(left, radius=1.35))
        for angle, label in [
            (0, "1"),
            (TAU / 3, r"\omega"),
            (2 * TAU / 3, r"\omega^2"),
        ]:
            pair, text = vector(
                left, angle, label, YELLOW if angle > PI else BLUE_C, radius=1.35
            )
            self.show(pair, text, run_time=0.6)
        self.show(
            formula(
                r"u=3:\quad\Delta(f)\in\{1,\omega,\omega^2\}",
                size=43,
                color=YELLOW,
                width=7,
            ).move_to(right)
        )
        self.show(
            words(
                "The full argument leaves these three possibilities.", size=25
            ).move_to(DOWN * 3.25)
        )

        self.section("application", "Carry the arithmetic input to Node 6")
        self.show(
            formula(r"cc^*=dd^*=gg^*=u^2", size=50, color=BLUE_C).move_to(UP * 1.85)
        )
        deltas = VGroup(
            *(
                formula(rf"\Delta({name})", size=41, color=BLUE_C)
                for name in ["c", "d", "g"]
            )
        ).arrange(DOWN, buff=0.3)
        deltas.move_to(LEFT * 4.0 + DOWN * 0.1)
        self.at("application_deltas")
        self.show(deltas)
        self.show(
            words("Roots of unity of odd order", size=25).move_to(
                LEFT * 4.0 + DOWN * 1.65
            )
        )
        node_six = card(
            "6 · Combine the two inputs", RIGHT * 3.9 + DOWN * 0.5, width=4.4
        )
        self.at("application_six")
        self.show(
            node_six,
            Arrow(deltas.get_right(), node_six.get_left(), buff=0.2).set_color(BLUE_C),
        )
        signs = card("5 · Common-sign congruences", LEFT * 3.8 + DOWN * 2.75, GREY_B)
        self.at("application_signs")
        self.show(
            signs,
            Arrow(signs.get_right(), node_six.get_bottom(), buff=0.15).set_color(
                GREY_B
            ),
        )
