import json
import math

import numpy as np
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
    LaggedStart,
    Line,
    Rectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class PowerOfTwoCycle(NodeScene):
    node_id = "power-of-two-cycle"
    title = "2.3 · Project to a power-of-two cycle"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/power-of-two-cycle.json").read_text()
        )["detail_cues"]

        self.section("factor", "Separate the power of two from the odd part")
        order = formula(r"n=4u^2", size=61, color=BLUE_C).move_to(UP * 1.8)
        self.show(order)
        factor = formula(r"u=2^{s-1}w", size=59).move_to(UP * 0.25)
        self.at("factor_u")
        self.show(factor)
        self.show(formula(r"s\geq1,\qquad w\text{ odd}", size=36).move_to(DOWN * 0.8))
        self.at("substitute")
        self.play(
            Transform(
                order,
                formula(r"n=4(2^{s-1}w)^2", size=61).move_to(order),
            ),
            run_time=1.3,
        )
        self.play(
            Transform(
                order,
                formula(r"n=2^{2s}w^2", size=61, color=BLUE_C).move_to(order),
            ),
            run_time=1.3,
        )
        self.at("cycle_length")
        self.show(
            formula(
                r"2^{2s}\text{ positions}\qquad w^2\text{ signs per position}",
                size=37,
            ).move_to(DOWN * 2.4)
        )

        self.section("buckets", "Example of the grouping · hypothetical order 36")
        self.show(
            formula(r"u=3,\quad s=1,\quad w=3,\quad 36=4\cdot9", size=35).move_to(
                UP * 2.0
            )
        )
        columns = VGroup()
        boxes = VGroup()
        labels = VGroup()
        for residue in range(4):
            x = (residue - 1.5) * 3.6
            box = Rectangle(width=2.9, height=4.35).move_to(RIGHT * x + DOWN * 0.6)
            box.set_stroke(BLUE_C, width=2)
            label = formula(rf"r={residue}", size=32, color=BLUE_C).move_to(
                RIGHT * x + UP * 1.35
            )
            column = VGroup(
                *(
                    formula(rf"h_{{{residue + 4 * ell}}}", size=26).move_to(
                        RIGHT * x + UP * (0.82 - ell * 0.39)
                    )
                    for ell in range(9)
                )
            )
            boxes.add(box)
            labels.add(label)
            columns.add(column)
        targets = {
            id(term): term.get_center().copy() for column in columns for term in column
        }
        for residue, column in enumerate(columns):
            for ell, term in enumerate(column):
                index = residue + 4 * ell
                term.move_to(
                    RIGHT * ((index % 6 - 2.5) * 1.45)
                    + UP * (0.9 - (index // 6) * 0.57)
                )
        self.show(*columns, run_time=1.4)
        self.at("four_positions")
        self.show(boxes, labels, run_time=0.9)
        self.at("zero_bucket")
        self.play(
            LaggedStart(
                *(term.animate.move_to(targets[id(term)]) for term in columns[0]),
                lag_ratio=0.12,
            ),
            run_time=2.2,
        )
        self.at("other_buckets")
        self.play(
            LaggedStart(
                *(
                    term.animate.move_to(targets[id(term)])
                    for column in columns[1:]
                    for term in column
                ),
                lag_ratio=0.04,
            ),
            run_time=2.2,
        )
        self.at("symbolic")
        self.show(
            words("Nine symbolic signs in each residue class", size=26).move_to(
                DOWN * 3.25
            )
        )

        self.section("odd_coefficients", "Each bucket becomes one odd integer")
        sum_formula = formula(
            r"a_r=\sum_{\ell=0}^{w^2-1}h_{r+\ell2^{2s}}", size=49
        ).move_to(UP * 1.75)
        self.show(sum_formula)
        self.at("new_polynomial")
        self.show(
            formula(r"T(X)=\sum_{r=0}^{2^{2s}-1}a_rX^r", size=43, color=BLUE_C).move_to(
                DOWN * 0.05
            )
        )
        self.at("mod_two")
        signs = formula(r"+1\equiv-1\equiv1\pmod2", size=42).move_to(DOWN * 1.55)
        self.show(signs)
        self.at("odd_sum")
        self.play(
            Transform(
                signs,
                formula(r"a_r\equiv w^2\equiv1\pmod2", size=43, color=YELLOW).move_to(
                    signs
                ),
            ),
            run_time=1.3,
        )
        self.at("not_signs")
        self.show(
            words(
                "Odd integers · they can have magnitude greater than 1", size=27
            ).move_to(DOWN * 2.75)
        )

        self.section("ring_map", "Projection preserves the algebra")
        domain = formula(r"\mathbb Z[X]/(X^n-1)", size=44).move_to(
            LEFT * 4.2 + UP * 1.65
        )
        codomain = formula(r"\mathbb Z[X]/(X^{2^{2s}}-1)", size=42).move_to(
            RIGHT * 3.8 + UP * 1.65
        )
        self.show(domain, codomain)
        self.show(Arrow(LEFT * 1.2 + UP * 1.65, RIGHT * 0.7 + UP * 1.65))
        self.show(formula(r"2^{2s}\mid n", size=36, color=BLUE_C).move_to(UP * 0.5))
        self.at("inverse")
        self.show(
            formula(r"X^j\longmapsto X^{j\bmod2^{2s}}", size=42).move_to(DOWN * 0.65),
            formula(r"\phi(X^{-1})=\phi(X)^{-1}", size=41).move_to(DOWN * 1.9),
        )
        self.at("star_map")
        self.show(
            formula(r"\phi(h)=T,\qquad\phi(h^*)=T^*", size=43, color=YELLOW).move_to(
                DOWN * 3.0
            )
        )

        self.section("norm", "A shorter cycle · exactly the same scalar norm")
        left = formula(r"h(X)", size=56, color=BLUE_C).move_to(LEFT * 4 + UP * 1.4)
        star = formula(r"h^*(X)", size=56, color=BLUE_C).move_to(LEFT * 0.5 + UP * 1.4)
        scalar = formula(r"=2^{2s}w^2", size=56, color=YELLOW).move_to(
            RIGHT * 4 + UP * 1.4
        )
        self.show(left, star, scalar)
        self.at("map_product")
        target = formula(r"T(X)", size=56, color=BLUE_C).move_to(LEFT * 4 + DOWN * 0.6)
        target_star = formula(r"T^*(X)", size=56, color=BLUE_C).move_to(
            LEFT * 0.5 + DOWN * 0.6
        )
        self.body.add(target, target_star)
        self.show(
            Arrow(left.get_bottom(), target.get_top(), buff=0.15),
            Arrow(star.get_bottom(), target_star.get_top(), buff=0.15),
        )
        self.play(
            TransformFromCopy(left, target),
            TransformFromCopy(star, target_star),
            run_time=1.4,
        )
        self.at("same_scalar")
        scalar_copy = scalar.copy().move_to(RIGHT * 4 + DOWN * 0.6)
        self.body.add(scalar_copy)
        self.play(TransformFromCopy(scalar, scalar_copy), run_time=1.3)
        self.show(
            formula(r"\text{in }\mathbb Z[X]/(X^{2^{2s}}-1)", size=39).move_to(
                DOWN * 2.35
            )
        )

        self.section("descent", "Ready to compare opposite coefficients")
        center = LEFT * 3.5 + DOWN * 0.4
        circle = Circle(radius=1.65).move_to(center).set_stroke(BLUE_C, width=2)
        dots = VGroup(
            *(
                Dot(
                    center
                    + 1.65
                    * np.array(
                        [math.cos(j * math.pi / 4), math.sin(j * math.pi / 4), 0]
                    ),
                    radius=0.065,
                    color=BLUE_C,
                )
                for j in range(8)
            )
        )
        self.show(circle, dots)
        self.show(
            words("Schematic power-of-two cycle", size=23).move_to(
                LEFT * 3.5 + DOWN * 2.7
            ),
            formula(r"2^{2s}\text{ odd coefficients}", size=36).move_to(
                RIGHT * 3.0 + UP * 1.1
            ),
            formula(r"TT^*=2^{2s}w^2", size=42, color=BLUE_C).move_to(
                RIGHT * 3.0 + DOWN * 0.1
            ),
        )
        self.at("opposite")
        pairs = VGroup(
            *(
                Line(dots[j].get_center(), dots[j + 4].get_center()).set_stroke(
                    YELLOW, width=2
                )
                for j in range(4)
            )
        )
        self.show(pairs, run_time=1.4)
        self.at("force_s")
        conclusion = formula(r"s\geq2\quad\Longrightarrow\quad\text{descent}", size=37)
        conclusion.move_to(RIGHT * 3.0 + DOWN * 1.4)
        self.show(conclusion)
        self.at("u_odd")
        self.show(
            formula(
                r"\text{Goal: }s=1\ \Longrightarrow\ u=w\text{ odd}",
                size=36,
                color=YELLOW,
            ).move_to(DOWN * 3.3)
        )
