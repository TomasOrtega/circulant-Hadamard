import json
from math import cos, sin

from manimlib import (
    BLUE_A,
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
    Dot,
    FadeIn,
    FlashAround,
    LaggedStart,
    Line,
    Rotate,
    Square,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


def crt_grid(center):
    rows = VGroup()
    for a in range(4):
        cells = VGroup()
        for b in range(9):
            j = (9 * a + 28 * b) % 36
            box = Square().set_width(0.65)
            box.set_stroke(BLUE_C, width=1).set_fill(BLUE_E, opacity=0.12)
            cells.add(VGroup(box, formula(rf"h_{{{j}}}", size=24, color=BLUE_C)))
        rows.add(cells.arrange(RIGHT, buff=0.06))
    rows.arrange(DOWN, buff=0.06).move_to(center)
    column_labels = VGroup(
        *(
            formula("1" if b == 0 else ("P" if b == 1 else rf"P^{b}"), size=25).next_to(
                rows[0][b], UP, buff=0.14
            )
            for b in range(9)
        )
    )
    row_labels = VGroup(
        *(
            formula("1" if a == 0 else ("Z" if a == 1 else rf"Z^{a}"), size=28).next_to(
                rows[a], LEFT, buff=0.25
            )
            for a in range(4)
        )
    )
    return VGroup(rows, column_labels, row_labels), rows


def output_plane(center, radius=1.55):
    circle = Circle(radius=radius).set_color(BLUE_C).move_to(center)
    axes = VGroup(
        Line(center + LEFT * 1.95, center + RIGHT * 1.95),
        Line(center + DOWN * 1.95, center + UP * 1.95),
    ).set_stroke(GREY_B, width=1)
    labels = VGroup(
        formula(r"\operatorname{Re}", size=20).next_to(axes[0], RIGHT, buff=0.1),
        formula(r"\operatorname{Im}", size=20).next_to(axes[1], UP, buff=0.1),
    )
    return VGroup(axes, circle, labels)


def output_value(center, angle, label, color, radius=1.55):
    endpoint = center + radius * (cos(angle) * RIGHT + sin(angle) * UP)
    arrow = Arrow(center, endpoint, buff=0).set_color(color)
    point = Dot(endpoint, radius=0.07).set_color(color)
    text = formula(label, size=25, color=color)
    text.next_to(point, UP, buff=0.1)
    text.add_updater(lambda mob: mob.next_to(point, UP, buff=0.1))
    return VGroup(arrow, point), text


class ThreeEvaluations(NodeScene):
    node_id = "three-evaluations"
    title = "3 · The Three Evaluations"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/three-evaluations.json").read_text()
        )["detail_cues"]
        self.section("hypothesis", "A hypothetical order-36 matrix")
        center = LEFT * 3.9 + DOWN * 0.3
        circle = Circle(radius=1.75).set_color(BLUE_C).move_to(center)
        points = VGroup(
            *(
                Dot(
                    center
                    + 1.75
                    * (
                        cos(PI / 2 - TAU * j / 36) * RIGHT
                        + sin(PI / 2 - TAU * j / 36) * UP
                    ),
                    radius=0.045,
                ).set_color(BLUE_C)
                for j in range(36)
            )
        )
        self.show(circle)
        self.body.add(points)
        self.play(
            LaggedStart(*(FadeIn(point) for point in points), lag_ratio=0.06),
            run_time=1.8,
        )
        self.show(
            words("36 hypothetical sign coefficients", size=24).next_to(
                circle, DOWN, buff=0.35
            ),
            self.stack(
                formula(r"u=3\quad\Longrightarrow\quad n=4u^2=36", size=40),
                formula(r"h_j\in\{-1,1\}", size=42, color=BLUE_C),
            ).move_to(RIGHT * 2.4),
        )
        self.at("hypothesis_norm")
        self.show(
            formula(r"hh^*=36", size=65, color=YELLOW).move_to(RIGHT * 2.4 + DOWN * 1.4)
        )
        self.show(
            formula(r"\text{in }\mathbb Z[X]/(X^{36}-1)", size=35).move_to(
                RIGHT * 2.4 + DOWN * 2.6
            )
        )

        self.section("crt", "One cyclic position becomes two coordinates")
        source_center = LEFT * 4.5 + DOWN * 0.4
        ring = Circle(radius=1.5).set_color(BLUE_C).move_to(source_center)
        points = VGroup(
            *(
                Dot(
                    source_center
                    + 1.5
                    * (
                        cos(PI / 2 - TAU * j / 36) * RIGHT
                        + sin(PI / 2 - TAU * j / 36) * UP
                    ),
                    radius=0.045,
                ).set_color(BLUE_C)
                for j in range(36)
            )
        )
        grid, cells = crt_grid(RIGHT * 2.6 + DOWN * 0.4)
        self.show(ring, points, grid)
        self.at("crt_map")
        self.show(
            formula(
                r"X\mapsto ZP,\qquad j\mapsto(j\bmod4,j\bmod9)", size=36, color=YELLOW
            ).move_to(UP * 1.9)
        )
        target = cells[13 % 4][13 % 9]
        self.at("crt_move")
        self.play(
            FlashAround(points[13], color=YELLOW),
            FlashAround(target, color=YELLOW),
            run_time=0.8,
        )
        self.show(formula(r"13\mapsto(1,4)", size=28).move_to(LEFT * 4.5 + DOWN * 2.4))
        self.play(
            LaggedStart(
                *(
                    Transform(point, point.copy().move_to(cells[j % 4][j % 9]))
                    for j, point in enumerate(points)
                ),
                lag_ratio=0.035,
            ),
            run_time=3,
        )
        self.remove(points)
        self.body.remove(points)
        self.show(
            words(
                "Same 36 coefficients; grid rows are not matrix rows.", size=24
            ).move_to(DOWN * 2.7)
        )
        self.show(
            formula(r"C_{36}\cong C_4\times C_9,\quad Z^4=P^9=1", size=33).move_to(
                DOWN * 3.25
            )
        )

        self.section("collect", "Collect the four powers of Z")
        grid, rows = crt_grid(LEFT * 1 + UP * 0.1)
        self.show(grid)
        for a, row in enumerate(rows):
            coefficients = VGroup(*(cell[1] for cell in row))
            self.play(coefficients.animate.set_color(YELLOW), run_time=0.35)
            target = formula(rf"H_{a}(P)", size=34, color=BLUE_C)
            target.next_to(row, RIGHT, buff=0.7)
            self.body.add(target)
            self.play(TransformFromCopy(coefficients, target), run_time=0.8)
            self.play(coefficients.animate.set_color(BLUE_C), run_time=0.3)
        self.at("collect_sum")
        self.show(
            formula(
                r"h(Z,P)=H_0(P)+ZH_1(P)+Z^2H_2(P)+Z^3H_3(P)", size=40, color=YELLOW
            ).move_to(DOWN * 2.35),
            words("Each H has nine coefficients, all ±1.", size=26).move_to(DOWN * 3.0),
        )

        self.section("evaluate", "Substitute fourth roots of unity")
        self.show(
            formula(r"Z^4=1:\quad Z=1,-1,i,-i", size=43, color=BLUE_C).move_to(UP * 1.8)
        )
        evaluations = [
            (r"Z=1:\ (1,1,1,1)", r"h(1,P)=H_0+H_1+H_2+H_3"),
            (r"Z=-1:\ (1,-1,1,-1)", r"h(-1,P)=H_0-H_1+H_2-H_3"),
            (r"Z=i:\ (1,i,-1,-i)", r"h(i,P)=H_0-H_2+i(H_1-H_3)"),
        ]
        for index, (weights, equation) in enumerate(evaluations):
            self.at(["evaluate_one", "evaluate_minus", "evaluate_i"][index])
            y = 0.8 - 1.15 * index
            source = formula(r"(1,Z,Z^2,Z^3)", size=28, color=BLUE_C)
            source.move_to(LEFT * 4.3 + UP * y)
            self.show(source)
            replacement = formula(weights, size=28, color=YELLOW).move_to(source)
            self.play(Transform(source, replacement), run_time=0.75)
            self.show(formula(equation, size=34, width=8).move_to(RIGHT * 2.4 + UP * y))
        self.at("evaluate_conjugate")
        self.show(
            words(
                "At −i: coefficientwise conjugation of the i evaluation.", size=23
            ).move_to(DOWN * 2.7)
        )

        self.section("normalize", "Two denominators of two remove the factor four")
        definitions = formula(
            r"c=\frac{h(1,P)}2,\qquad d=\frac{h(-1,P)}2,"
            r"\qquad g=\frac{h(i,P)}2",
            size=48,
            color=BLUE_C,
        )
        definitions.move_to(UP * 1.5)
        self.show(definitions)
        norm = formula(r"cc^*=\frac{h(1,P)}2\frac{h^*(1,P)}2", size=55)
        norm.move_to(DOWN * 0.1)
        self.at("normalize_pair")
        self.show(norm)
        for source in [r"cc^*=\frac{36}{2\cdot2}", r"cc^*=\frac{36}{4}"]:
            self.play(
                Transform(norm, formula(source, size=60, color=YELLOW).move_to(norm)),
                run_time=0.8,
            )
        self.at("normalize_nine")
        self.play(
            Transform(norm, formula(r"cc^*=9", size=60, color=YELLOW).move_to(norm)),
            run_time=0.8,
        )
        self.show(
            formula(r"cc^*=dd^*=gg^*=9", size=53, color=YELLOW).move_to(DOWN * 1.65)
        )
        self.at("normalize_star")
        self.show(formula(r"f^*(P)=\overline{f(P^{-1})}", size=36).move_to(DOWN * 2.9))

        self.section("integral", "Division by two retains integral coefficients")
        column = VGroup(
            *(formula(rf"a_{a}\in\{{-1,1\}}", size=35, color=BLUE_C) for a in range(4))
        ).arrange(DOWN, buff=0.35)
        column.move_to(LEFT * 4.5)
        self.show(column)
        self.show(words("Fix one power of P", size=25).move_to(LEFT * 4.5 + UP * 1.9))
        sums = [
            r"[P^b]c=\frac{a_0+a_1+a_2+a_3}{2}\in\mathbb Z",
            r"[P^b]d=\frac{a_0-a_1+a_2-a_3}{2}\in\mathbb Z",
            r"[P^b]g=\frac{a_0-a_2}{2}+i\frac{a_1-a_3}{2}\in\mathbb Z[i]",
        ]
        for index, source in enumerate(sums):
            if index < 2:
                self.wait_until_narration(self.details["integral_cd"] + index * 3)
            else:
                self.at("integral_g")
            target = formula(source, size=37, width=9)
            target.move_to(RIGHT * 1.8 + UP * (1.25 - index * 1.3))
            self.body.add(target)
            self.play(TransformFromCopy(column, target), run_time=1.2)
        self.at("integral_result")
        self.show(
            words(
                "Four-sign sums and two-sign differences are even.",
                size=27,
                color=YELLOW,
            ).move_to(DOWN * 2.9)
        )

        self.section(
            "geometry", "At a ninth-root input, every output has modulus three"
        )
        center = LEFT * 3.9 + DOWN * 0.5
        self.show(output_plane(center))
        self.show(
            formula(r"\zeta^9=1", size=44, color=BLUE_C).move_to(
                RIGHT * 2.7 + DOWN * 0.1
            )
        )
        norm = formula(r"c(\zeta)\overline{c(\zeta)}=9", size=43, color=BLUE_C)
        norm.move_to(RIGHT * 2.7 + UP * 1.3)
        self.at("geometry_star")
        self.show(norm)
        self.play(
            Transform(
                norm, formula(r"|c(\zeta)|^2=9", size=52, color=YELLOW).move_to(norm)
            ),
            run_time=0.9,
        )
        self.wait_until_narration(self.details["geometry_points"] - 2)
        self.play(
            Transform(
                norm, formula(r"|c(\zeta)|=3", size=52, color=YELLOW).move_to(norm)
            ),
            run_time=0.9,
        )
        self.at("geometry_points")
        for angle, label, color in [
            (0.2, r"c(\zeta)", BLUE_C),
            (2.4, r"d(\zeta)", BLUE_B),
            (4.6, r"g(\zeta)", BLUE_A),
        ]:
            vector, text = output_value(center, angle, label, color)
            self.show(vector, text)
        self.show(
            words("Permitted inputs: ninth roots of unity", size=26).move_to(
                RIGHT * 2.7 + DOWN * 1.3
            )
        )
        self.show(words("Output positions are schematic.", size=25).move_to(DOWN * 2.9))

        self.section("general", "The same construction works for every odd u")
        self.show(
            formula(r"cc^*=dd^*=gg^*=u^2", size=56, color=BLUE_C).move_to(UP * 1.4)
        )
        self.wait_until_narration(self.cues["general"] + 4.5)
        self.show(
            formula(
                r"\zeta^{u^2}=1\quad\Longrightarrow\quad"
                r"|c(\zeta)|=|d(\zeta)|=|g(\zeta)|=u",
                size=43,
            ).move_to(UP * 0.2)
        )
        self.at("general_return")
        self.show(
            formula(
                r"u=3:\quad P=1,\ \omega=e^{2\pi i/3};\quad\omega^9=1",
                size=44,
                color=YELLOW,
            ).move_to(DOWN * 1.1)
        )
        self.at("general_phase")
        self.show(
            words(
                "The norm fixes distance. Next, compare phase changes.", size=28
            ).move_to(DOWN * 2.5)
        )

        self.section("preview", "Coming in Node 6 · one common rotation")
        left, right = LEFT * 3.8 + DOWN * 0.55, RIGHT * 3.8 + DOWN * 0.55
        self.show(output_plane(left, radius=1.4), output_plane(right, radius=1.4))
        self.show(
            formula(r"P=1", size=37).move_to(LEFT * 3.8 + UP * 2.1),
            formula(r"P=\omega", size=37).move_to(RIGHT * 3.8 + UP * 2.1),
        )
        pairs = []
        for name, angle, color in [
            ("c", 0, BLUE_C),
            ("d", PI, BLUE_B),
            ("g", PI / 2, BLUE_A),
        ]:
            source, source_text = output_value(left, angle, rf"{name}(1)", color, 1.4)
            target, target_text = output_value(
                right, angle, rf"{name}(\omega)", color, 1.4
            )
            self.show(source, source_text, target, target_text)
            pairs.append(target)
        self.show(
            words("Schematic starting values: 3, −3, 3i", size=25).move_to(DOWN * 2.9)
        )
        self.show(
            formula(r"120^\circ\ \text{illustration}", size=30, color=YELLOW).move_to(
                UP * 1.7
            )
        )
        self.at("preview_rotation")
        self.play(
            *(Rotate(pair, TAU / 3, about_point=right) for pair in pairs), run_time=3
        )
        angle = Arc(start_angle=0, angle=TAU / 3, radius=0.75)
        angle.set_color(YELLOW).shift(right)
        self.show(angle)
        self.at("preview_result")
        self.show(
            words(
                "The common rotation uses more than the norm identity.", size=26
            ).move_to(DOWN * 3.45)
        )
