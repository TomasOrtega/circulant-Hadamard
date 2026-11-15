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
    FadeIn,
    FadeOut,
    LaggedStart,
    Rectangle,
    Rotate,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class CRTCoordinates(NodeScene):
    node_id = "crt-coordinates"
    title = "3.1 · Chinese Remainder Coordinates"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def hide(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.35)
        self.body.remove(*objects)

    def dial(self, length, center, radius=1.15):
        circle = Circle(radius=radius).set_color(BLUE_C).move_to(center)
        labels = VGroup(
            *(
                formula(str(k), size=29).move_to(
                    center
                    + (radius + 0.32)
                    * (cos(TAU * k / length) * UP + sin(TAU * k / length) * RIGHT)
                )
                for k in range(length)
            )
        )
        pointer = Dot(center + radius * UP, radius=0.085).set_color(YELLOW)
        return circle, labels, pointer

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/crt-coordinates.json").read_text()
        )["detail_cues"]

        self.section("coordinates", "One cycle, two residue dials")
        self.show(
            formula(r"n=4u^2,\qquad u\text{ odd}", size=39).move_to(
                LEFT * 4.3 + UP * 2.05
            )
        )
        long_center = LEFT * 5.7 + DOWN * 0.15
        long_circle = Circle(radius=1.0).set_color(BLUE_C).move_to(long_center)
        long_slots = VGroup(
            *(
                Dot(
                    long_center + cos(TAU * j / 36) * UP + sin(TAU * j / 36) * RIGHT,
                    radius=0.03,
                ).set_color(BLUE_C)
                for j in range(36)
            )
        )
        long_pointer = Dot(long_center + UP, radius=0.075).set_color(YELLOW)
        position = formula("j=0", size=34, color=YELLOW).move_to(long_center)
        self.show(
            long_circle,
            long_slots,
            long_pointer,
            position,
            words("36 positions", size=23).move_to(long_center + DOWN * 1.55),
            run_time=0.9,
        )
        self.at("two_coordinates")
        mapping = formula(r"j\longmapsto(j\bmod4,\ j\bmod u^2)", size=43)
        mapping.move_to(DOWN * 2.7)
        self.show(mapping)
        self.at("dials")
        four_center = LEFT * 0.6 + DOWN * 0.15
        nine_center = RIGHT * 4.4 + DOWN * 0.15
        four_circle, four_labels, four_pointer = self.dial(4, four_center)
        nine_circle, nine_labels, nine_pointer = self.dial(9, nine_center)
        self.show(
            four_circle,
            four_labels,
            four_pointer,
            nine_circle,
            nine_labels,
            nine_pointer,
            Arrow(LEFT * 4.3, LEFT * 2.25, buff=0.1).set_color(BLUE_C),
            run_time=1.1,
        )
        self.at("example_lengths")
        self.show(
            words("u = 3 illustration", size=24).move_to(UP * 2.05 + RIGHT * 2.4),
            words("mod 4", size=24).move_to(four_center + DOWN * 1.95),
            words("mod 9", size=24).move_to(nine_center + DOWN * 1.95),
            run_time=0.65,
        )
        previous = 0
        for key, value in [("one", 1), ("four", 4), ("nine", 9), ("advance", 10)]:
            self.at(key)
            delta = value - previous
            self.play(
                Rotate(long_pointer, -TAU * delta / 36, about_point=long_center),
                Rotate(four_pointer, -TAU * delta / 4, about_point=four_center),
                Rotate(nine_pointer, -TAU * delta / 9, about_point=nine_center),
                Transform(
                    position,
                    formula(f"j={value}", size=34, color=YELLOW).move_to(position),
                ),
                Transform(
                    mapping,
                    formula(
                        rf"{value}\longmapsto({value % 4},\ {value % 9})",
                        size=43,
                        color=YELLOW,
                    ).move_to(mapping),
                ),
                run_time=1.1,
            )
            previous = value

        self.section("bijection", "No positions lost, and addition preserved")
        same = words("Suppose j and k have the same pair", size=27, width=6.5)
        same.move_to(LEFT * 4.4 + UP * 1.75)
        self.at("same_pair")
        self.show(same, run_time=0.75)
        divisible = formula(r"4\mid(j-k),\qquad u^2\mid(j-k)", size=32, width=6.8)
        divisible.move_to(LEFT * 4.4 + UP * 0.8)
        self.at("divisible")
        self.show(divisible, run_time=0.85)
        coprime = formula(r"\gcd(4,u^2)=1", size=35, color=BLUE_C)
        coprime.move_to(LEFT * 4.4 + DOWN * 0.15)
        self.at("coprime")
        self.show(coprime, run_time=0.85)
        same_position = formula(
            r"4u^2\mid(j-k)\quad\Longrightarrow\quad j\equiv k\pmod{4u^2}",
            size=29,
            width=7.1,
            color=YELLOW,
        ).move_to(LEFT * 4.4 + DOWN * 1.3)
        self.at("same_position")
        self.show(same_position)

        grid_center = RIGHT * 3.65 + DOWN * 0.1
        cell_width, cell_height = 0.62, 0.65
        cells = VGroup(
            *(
                Rectangle(width=cell_width, height=cell_height)
                .set_stroke(BLUE_C, width=1)
                .set_fill(BLUE_C, opacity=0.035)
                .move_to(
                    grid_center
                    + RIGHT * (column - 4) * cell_width
                    + UP * (1.5 - row) * cell_height
                )
                for row in range(4)
                for column in range(9)
            )
        )
        row_labels = VGroup(
            *(
                formula(str(row), size=24, color=BLUE_C).next_to(
                    cells[row * 9], LEFT, buff=0.15
                )
                for row in range(4)
            )
        )
        column_labels = VGroup(
            *(
                formula(str(column), size=24, color=BLUE_C).next_to(
                    cells[column], UP, buff=0.12
                )
                for column in range(9)
            )
        )
        grid_caption = words("u = 3 · row mod 4, column mod 9", size=22, width=6.5)
        grid_caption.move_to(grid_center + DOWN * 1.8)
        self.at("counts")
        self.hide(same, divisible, coprime)
        counts = formula(r"4u^2=4\times u^2", size=40, color=BLUE_C)
        counts.move_to(LEFT * 4.4 + UP * 1.2)
        count_note = words(
            "Same finite count + injective = bijective", size=24, width=6.8
        ).move_to(LEFT * 4.4 + UP * 0.2)
        self.show(
            counts,
            count_note,
            cells,
            row_labels,
            column_labels,
            grid_caption,
            words("4 × 9 = 36 positions", size=27).move_to(grid_center + UP * 2.1),
        )
        grid_values = VGroup(
            *(
                formula(str(j), size=24, color=WHITE).move_to(
                    cells[(j % 4) * 9 + j % 9]
                )
                for j in range(36)
            )
        )
        self.at("fill_grid")
        self.body.add(grid_values)
        self.play(
            LaggedStart(*(FadeIn(value) for value in grid_values), lag_ratio=0.08),
            run_time=3.0,
        )
        self.at("add_example")
        self.hide(same_position, counts, count_note)
        addition = VGroup(
            formula("4+9=13", size=43),
            formula(r"(0,4)+(1,0)=(1,4)", size=33, color=YELLOW, width=6.9),
        ).arrange(DOWN, buff=0.55)
        addition.move_to(LEFT * 4.4 + DOWN * 0.5)
        highlights = VGroup(
            *(
                SurroundingRectangle(cells[(j % 4) * 9 + j % 9], buff=0.02).set_color(
                    YELLOW
                )
                for j in [4, 9, 13]
            )
        )
        self.show(addition, highlights, run_time=1.2)
        self.at("addition")
        self.show(
            formula(r"(a,b)+(a',b')=(a+a'\bmod4,\ b+b'\bmod u^2)", size=32).move_to(
                DOWN * 2.8
            )
        )
        self.at("isomorphism")
        self.show(
            formula(r"C_{4u^2}\cong C_4\times C_{u^2}", size=43, color=YELLOW).move_to(
                DOWN * 3.5
            ),
            run_time=0.9,
        )

        self.section("polynomial", "The same coefficients, relabelled")
        self.at("variables")
        ring = formula(
            r"\mathbb Z[Z,P]/(Z^4-1,\ P^{u^2}-1)", size=43, color=BLUE_C
        ).move_to(UP * 1.95)
        self.show(ring)
        self.at("generator")
        generator = formula(r"X\longmapsto ZP", size=48)
        generator.move_to(UP * 0.7)
        self.show(generator)
        original = VGroup(
            formula("h_j", size=49, color=YELLOW),
            formula("X^j", size=49, color=BLUE_C),
        ).arrange(RIGHT, buff=0.12)
        original.move_to(LEFT * 3.8 + DOWN * 0.65)
        relabelled = VGroup(
            formula("h_j", size=49, color=YELLOW),
            formula("Z^jP^j", size=49, color=BLUE_C),
        ).arrange(RIGHT, buff=0.12)
        relabelled.move_to(RIGHT * 3.8 + DOWN * 0.65)
        relabel_arrow = Arrow(LEFT * 1.7 + DOWN * 0.65, RIGHT * 1.6 + DOWN * 0.65)
        relabel_arrow.set_color(BLUE_C)
        self.at("monomial")
        self.show(original, relabel_arrow, run_time=0.7)
        self.play(
            *(
                TransformFromCopy(old, new)
                for old, new in zip(original, relabelled, strict=True)
            ),
            run_time=1.2,
        )
        self.body.add(relabelled)
        self.at("reduce")
        reduced = VGroup(
            formula("h_j", size=42, color=YELLOW),
            formula(r"Z^{j\bmod4}P^{j\bmod u^2}", size=42, color=BLUE_C),
        ).arrange(RIGHT, buff=0.12)
        reduced.set_max_width(6.2).move_to(relabelled)
        self.play(Transform(relabelled, reduced), run_time=1.1)
        self.at("coefficient")
        self.show(
            SurroundingRectangle(original[0], buff=0.12).set_color(YELLOW),
            SurroundingRectangle(relabelled[0], buff=0.12).set_color(YELLOW),
            words("The same coefficient stays attached", size=28).move_to(DOWN * 1.9),
            run_time=0.8,
        )
        self.at("unchanged")
        self.show(
            words("One new label per sign · no coefficients added", size=27).move_to(
                DOWN * 2.75
            ),
            run_time=0.8,
        )

        self.at("multiplication")
        self.hide(*[obj for obj in self.body if obj is not ring])
        multiplication = formula(
            r"(Z^aP^b)(Z^{a'}P^{b'})=Z^{a+a'}P^{b+b'}", size=42
        ).move_to(UP * 0.65)
        self.show(multiplication)
        self.at("inversion")
        inversion = formula(
            r"(Z^aP^b)^{-1}=Z^{-a}P^{-b}", size=42, color=BLUE_C
        ).move_to(DOWN * 0.55)
        self.show(inversion)
        self.at("star")
        star = formula(r"h^*(Z,P)=h(Z^{-1},P^{-1})", size=38)
        star.move_to(DOWN * 1.75)
        self.show(star)
        self.at("norm")
        self.hide(multiplication, inversion, star)
        norm = formula(r"h(X)h^*(X)=4u^2", size=49).move_to(DOWN * 0.1)
        self.show(norm, run_time=0.75)
        self.play(
            Transform(
                norm,
                formula(r"h(Z,P)h^*(Z,P)=4u^2", size=49, color=YELLOW).move_to(norm),
            ),
            run_time=1.3,
        )
        self.at("relations")
        self.show(
            formula(r"Z^4=1,\qquad P^{u^2}=1", size=46, color=BLUE_C).move_to(
                DOWN * 1.55
            )
        )
        self.at("same_data")
        self.show(
            words("Same sign data · same norm identity", size=30).move_to(DOWN * 2.8)
        )
