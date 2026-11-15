import json
from math import cos, sin

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    TAU,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    Dot,
    FadeOut,
    LaggedStart,
    Line,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class FoldAndDivide(NodeScene):
    node_id = "fold-and-divide"
    title = "2.5 · Fold the Cycle"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def hide(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.35)
        self.body.remove(*objects)

    def pair_diagram(self, center):
        radius = 1.35
        circle = Circle(radius=radius).set_color(BLUE_C).move_to(center)
        directions = [
            cos(TAU * j / 8) * UP + sin(TAU * j / 8) * RIGHT for j in range(8)
        ]
        points = VGroup(
            *(
                Dot(center + radius * direction, radius=0.065).set_color(BLUE_C)
                for direction in directions
            )
        )
        labels = VGroup(
            *(
                formula(
                    rf"a_{j}" if j < 4 else ("a_D" if j == 4 else rf"a_{{D+{j - 4}}}"),
                    size=28,
                ).move_to(center + 1.85 * direction)
                for j, direction in enumerate(directions)
            )
        )
        links = VGroup(
            *(
                Line(points[j].get_center(), points[j + 4].get_center()).set_stroke(
                    YELLOW, width=2, opacity=0.5
                )
                for j in range(4)
            )
        )
        return circle, points, labels, links

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/fold-and-divide.json").read_text()
        )["detail_cues"]

        self.section("setup", "One fold: halve the length, divide the norm by four")
        center = LEFT * 4.4 + DOWN * 0.25
        circle, points, labels, links = self.pair_diagram(center)
        self.show(
            circle,
            points,
            labels,
            words("Opposite-pair schematic", size=24).move_to(center + DOWN * 2.5),
            formula(r"D=2^{k-1}", size=32, color=BLUE_C).move_to(center + UP * 2.5),
        )
        self.at("hypothesis")
        self.show(
            formula(r"T(X)T^*(X)=2^{2t}w^2", size=41, width=7.5).move_to(
                RIGHT * 3.7 + UP * 1.5
            ),
            formula(r"t\ge2,\qquad w\text{ odd}", size=37, color=YELLOW).move_to(
                RIGHT * 3.7 + UP * 0.4
            ),
            words("Every coefficient is odd", size=27).move_to(
                RIGHT * 3.7 + DOWN * 0.65
            ),
        )
        self.at("goal")
        self.show(links, run_time=0.8)
        self.show(
            formula(r"2^k\longmapsto2^{k-1}", size=41, color=BLUE_C).move_to(
                RIGHT * 3.7 + DOWN * 1.7
            ),
            formula(r"(k,t)\longmapsto(k-1,t-1)", size=36, color=YELLOW).move_to(
                RIGHT * 3.7 + DOWN * 2.75
            ),
        )

        self.section("averages", "Average opposite coefficients before folding")
        circle, points, labels, links = self.pair_diagram(center)
        self.show(
            circle,
            points,
            labels,
            links,
            words("Opposite-pair schematic", size=23).move_to(center + DOWN * 2.5),
        )
        congruence = formula(
            r"a_{j+D}\equiv a_j\pmod{2^t},\qquad D=2^{k-1}", size=35, width=13
        ).move_to(UP * 2.4)
        self.at("comparison")
        self.show(congruence)
        mod_four = formula(
            r"t\ge2\quad\Longrightarrow\quad a_{j+D}\equiv a_j\pmod4", size=32
        )
        mod_four.move_to(RIGHT * 3.7 + UP * 1.45)
        self.at("mod_four")
        self.show(mod_four)
        pair = formula(r"a_j,\qquad a_j+4r_j", size=40, color=BLUE_C)
        pair.move_to(RIGHT * 3.7 + UP * 0.4)
        self.at("pair")
        self.show(pair)
        average = formula(r"b_j=\frac{a_j+(a_j+4r_j)}2", size=40, width=7.5)
        average.move_to(RIGHT * 3.7 + DOWN * 0.8)
        self.at("average")
        self.show(average, run_time=0.9)
        self.play(
            Transform(
                average,
                formula(r"b_j=a_j+2r_j", size=43, color=YELLOW).move_to(average),
            ),
            run_time=1.1,
        )
        odd_note = words("odd + even = odd", size=28)
        odd_note.move_to(RIGHT * 3.7 + DOWN * 1.75)
        self.at("odd_average")
        self.show(odd_note, run_time=0.8)
        example = formula(r"\frac{3+7}{2}=5", size=39, color=BLUE_C)
        example.move_to(RIGHT * 3.7 + DOWN * 2.8)
        self.at("pair_example")
        self.show(example)
        self.at("all_pairs")
        self.hide(mod_four, pair, average, odd_note, example)
        target_center = RIGHT * 3.7 + DOWN * 0.25
        target_circle = Circle(radius=1.1).set_color(BLUE_C).move_to(target_center)
        target_points = VGroup(
            *(
                Dot(
                    target_center
                    + 1.1 * (cos(TAU * j / 4) * UP + sin(TAU * j / 4) * RIGHT),
                    radius=0.08,
                ).set_color(YELLOW)
                for j in range(4)
            )
        )
        target_labels = VGroup(
            *(
                formula(rf"b_{j}", size=31, color=YELLOW).move_to(
                    target_center
                    + 1.5 * (cos(TAU * j / 4) * UP + sin(TAU * j / 4) * RIGHT)
                )
                for j in range(4)
            )
        )
        self.show(
            target_circle,
            words("One odd average per new position", size=25, width=7).move_to(
                target_center + UP * 2.1
            ),
            run_time=0.65,
        )
        self.body.add(target_points)
        self.play(
            LaggedStart(
                *(
                    TransformFromCopy(
                        VGroup(points[j], points[j + 4]), target_points[j]
                    )
                    for j in range(4)
                ),
                lag_ratio=0.18,
            ),
            run_time=2.5,
        )
        self.show(target_labels, run_time=0.75)
        self.show(
            formula(
                r"2^k\text{ positions}\longmapsto2^{k-1}\text{ positions}", size=35
            ).move_to(DOWN * 3.4),
            run_time=0.8,
        )

        self.section("norm", "Projection respects multiplication and star")
        projection = formula(r"q:X^{j+D}\longmapsto X^j,\qquad D=2^{k-1}", size=39)
        projection.move_to(UP * 1.95)
        self.at("projection")
        self.show(projection)
        coefficient = formula(
            r"a_jX^j+a_{j+D}X^{j+D}\longmapsto(a_j+a_{j+D})X^j", size=36
        )
        coefficient.move_to(UP * 0.55)
        self.at("coefficients_add")
        self.show(coefficient)
        twice = formula(r"q(T)=2T_1", size=48, color=YELLOW).move_to(DOWN * 0.85)
        self.at("twice")
        self.show(twice)
        properties = formula(r"q(TT^*)=q(T)q(T)^*", size=43, color=BLUE_C)
        properties.move_to(DOWN * 2.3)
        self.at("preserves")
        self.show(properties)
        self.at("project_norm")
        self.hide(projection, coefficient, properties)
        self.play(twice.animate.move_to(UP * 1.85), run_time=0.5)
        norm = formula(r"q(T)q(T)^*=2^{2t}w^2", size=46).move_to(UP * 0.4)
        self.show(norm, run_time=0.85)
        self.play(
            Transform(
                norm,
                formula(r"4T_1T_1^*=2^{2t}w^2", size=49, color=BLUE_C).move_to(norm),
            ),
            run_time=1.2,
        )
        self.at("divide_four")
        self.show(
            Arrow(DOWN * 0.25, DOWN * 0.8, buff=0.05).set_color(YELLOW),
            words("Divide coefficientwise by 4", size=27).move_to(
                RIGHT * 3.6 + DOWN * 0.5
            ),
            run_time=0.8,
        )
        basis_note = words("Valid in the free integer group ring", size=27)
        basis_note.move_to(DOWN * 2.9)
        self.at("free_basis")
        self.show(basis_note, run_time=0.85)
        self.at("new_norm")
        new_norm = formula(r"T_1T_1^*=2^{2(t-1)}w^2", size=49, color=YELLOW)
        new_norm.move_to(DOWN * 1.55)
        self.body.add(new_norm)
        self.play(TransformFromCopy(norm, new_norm), run_time=1.3)

        self.section("iteration", "Repeat only while t is at least two")
        self.show(formula(r"s\ge2", size=41, color=YELLOW).move_to(UP * 2.15))
        x_positions = [-6.8, -3.65, -0.25, 3.1, 6.5]
        headers = VGroup(
            *(
                words(label, size=24).move_to(RIGHT * x + UP * 1.3)
                for label, x in zip(
                    ["folds", "(k, t)", "length", "norm", "coefficients"],
                    x_positions,
                    strict=True,
                )
            )
        )
        self.show(headers, run_time=0.8)

        def table_row(values, y, color=WHITE):
            return VGroup(
                *(
                    formula(value, size=32, color=color, width=3.0).move_to(
                        RIGHT * x + UP * y
                    )
                    for value, x in zip(values, x_positions, strict=True)
                )
            )

        initial = table_row(
            ["0", "(2s,s)", "2^{2s}", "2^{2s}w^2", r"\text{odd}"], 0.3, BLUE_C
        )
        general = table_row(
            ["j", "(2s-j,s-j)", "2^{2s-j}", "2^{2(s-j)}w^2", r"\text{odd}"], -0.85
        )
        endpoint = table_row(
            ["s-1", "(s+1,1)", "2^{s+1}", "4w^2", r"\text{odd}"], -2.0, YELLOW
        )
        self.at("initial")
        self.show(initial)
        self.at("after_j")
        self.body.add(general)
        self.play(TransformFromCopy(initial, general), run_time=1.2)
        allowed = formula(
            r"j<s-1\quad\Longrightarrow\quad t=s-j\ge2", size=36, color=BLUE_C
        )
        allowed.move_to(DOWN * 3.2)
        self.at("allowed")
        self.show(allowed)
        self.at("endpoint")
        self.hide(allowed)
        self.body.add(endpoint)
        self.play(TransformFromCopy(general, endpoint), run_time=1.3)
        self.show(
            SurroundingRectangle(endpoint, buff=0.18).set_color(YELLOW), run_time=0.8
        )
        self.at("stop")
        self.show(
            words(
                "STOP at t = 1 · no further oddness-preserving fold", size=28
            ).move_to(DOWN * 3.05),
            run_time=0.85,
        )
        self.at("next")
        self.show(
            words(
                "Next: the endpoint contradicts odd squares modulo 8", size=25
            ).move_to(DOWN * 3.65),
            run_time=0.85,
        )
