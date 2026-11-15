import json
from math import cos, sin

from manimlib import (
    BLUE_B,
    BLUE_C,
    DOWN,
    GREY_B,
    LEFT,
    ORIGIN,
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
    Rotate,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


def point(center, radius, angle):
    return center + radius * (cos(angle) * RIGHT + sin(angle) * UP)


def unit_circle(center, radius):
    return (
        VGroup(
            Line(center + LEFT * (radius + 0.15), center + RIGHT * (radius + 0.15)),
            Line(center + DOWN * (radius + 0.15), center + UP * (radius + 0.15)),
        )
        .set_stroke(GREY_B, width=1, opacity=0.5)
        .add(Circle(radius=radius).set_color(BLUE_C).move_to(center))
    )


class KroneckerStep(NodeScene):
    node_id = "kronecker-step"
    title = "4.5 · Why Kronecker Gives a Root of Unity"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def copy_to(self, source, target, run_time=1):
        self.body.add(target)
        self.play(TransformFromCopy(source, target), run_time=run_time)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/kronecker-step.json").read_text()
        )["detail_cues"]

        self.section("hypotheses", "Both hypotheses are essential")
        integral = words("Algebraic integer", size=35).move_to(LEFT * 4 + UP * 1.2)
        conjugates = words("Every algebraic conjugate", size=32).move_to(
            RIGHT * 3.7 + UP * 1.2
        )
        self.show(integral)
        self.at("hypotheses_all")
        self.show(
            conjugates,
            formula(
                r"|\sigma(z)|=1\quad\text{for every }\sigma", size=38, width=7.5
            ).move_to(RIGHT * 3.7 + UP * 0.2),
        )
        self.at("hypotheses_z")
        z = formula(r"z,\qquad d=[\mathbb Q(z):\mathbb Q]", size=46).move_to(DOWN * 1.3)
        self.show(
            Arrow(LEFT * 4 + UP * 0.6, LEFT * 1.2 + DOWN * 0.9).set_color(BLUE_C),
            Arrow(RIGHT * 3.7 + DOWN * 0.4, RIGHT * 1.2 + DOWN * 0.9).set_color(BLUE_C),
            z,
        )
        self.at("hypotheses_monic")
        self.show(
            formula(r"z^d+a_1z^{d-1}+\cdots+a_d=0", size=42).move_to(DOWN * 2.65),
            formula(
                r"a_j\in\mathbb Z\qquad\text{leading coefficient }1", size=31
            ).move_to(DOWN * 3.5),
        )

        self.section("powers", "Every power inherits the same constraints")
        center = LEFT * 4.5 + DOWN * 0.55
        circle = unit_circle(center, 1.4)
        theta = 0.81
        dots = VGroup(
            *(
                Dot(point(center, 1.4, theta * m), radius=0.06).set_color(BLUE_C)
                for m in range(1, 5)
            )
        )
        labels = VGroup(
            *(
                formula("z" if m == 1 else rf"z^{m}", size=26, color=BLUE_C).next_to(
                    dots[m - 1], point(ORIGIN, 1, theta * m), buff=0.2
                )
                for m in range(1, 5)
            )
        )
        self.show(circle, dots[0], labels[0])
        self.at("powers_inherit")
        self.body.add(dots[1:], labels[1:])
        for old, new, label in zip(dots, dots[1:], labels[1:], strict=False):
            self.play(TransformFromCopy(old, new), FadeIn(label), run_time=0.5)
        self.show(
            words("Schematic angles · no repetition assumed", size=24).move_to(
                LEFT * 4.5 + DOWN * 2.8
            ),
            run_time=0.7,
        )
        self.at("powers_degree")
        self.show(
            formula(
                r"q_m(X)=X^r+a_{m,1}X^{r-1}+\cdots+a_{m,r}", size=36, width=8.7
            ).move_to(RIGHT * 2.8 + UP * 1.0),
            formula(r"q_m(z^m)=0,\qquad r\le d", size=40).move_to(
                RIGHT * 3.0 + DOWN * 0.4
            ),
        )
        self.at("powers_integer")
        self.show(
            formula(r"a_{m,k}\in\mathbb Z", size=44, color=YELLOW).move_to(
                RIGHT * 3 + DOWN * 1.75
            ),
            words("One bound must work for every m", size=26, color=BLUE_C).move_to(
                DOWN * 3.55
            ),
        )

        self.section("three_roots", "See the coefficient bounds in degree three")
        center = LEFT * 5.25 + UP * 0.1
        angles = [PI / 9, 13 * PI / 18, 17 * PI / 12]
        colors = [BLUE_C, BLUE_B, WHITE]
        roots = VGroup()
        root_labels = VGroup()
        for name, angle, color in zip(
            [r"\alpha", r"\beta", r"\gamma"], angles, colors, strict=True
        ):
            root = Dot(point(center, 1.15, angle), radius=0.065).set_color(color)
            label = formula(name, size=34, color=color).next_to(
                root, point(ORIGIN, 1, angle), buff=0.18
            )
            roots.add(root)
            root_labels.add(label)
        self.show(unit_circle(center, 1.15), roots, root_labels)
        unit_magnitudes = formula(r"|\alpha|=|\beta|=|\gamma|=1", size=30).move_to(
            LEFT * 5.25 + DOWN * 2.1
        )
        self.show(
            unit_magnitudes,
            words(
                "Schematic roots; no integrality assumed here", size=24, width=14
            ).move_to(DOWN * 3.55),
        )
        product = formula(r"(X-\alpha)(X-\beta)(X-\gamma)", size=42).move_to(
            RIGHT * 2.1 + UP * 1.65
        )
        self.at("three_expand")
        self.copy_to(root_labels, product)
        self.show(
            formula(r"=X^3-e_1X^2+e_2X-e_3", size=42).move_to(RIGHT * 2.1 + UP * 0.55),
            run_time=0.8,
        )
        expressions = [
            ("three_first", r"|e_1|=|\alpha+\beta+\gamma|", r"|e_1|\le1+1+1=3"),
            (
                "three_second",
                r"|e_2|=|\alpha\beta+\alpha\gamma+\beta\gamma|",
                r"|e_2|\le1+1+1=3",
            ),
            ("three_third", r"|e_3|=|\alpha\beta\gamma|", r"|e_3|=1"),
        ]
        terms = VGroup()
        for index, (cue, expression, _) in enumerate(expressions):
            self.at(cue)
            term = formula(expression, size=36, width=10).move_to(
                RIGHT * 2.1 + DOWN * (0.55 + index * 1.05)
            )
            self.copy_to(root_labels, term, run_time=0.75)
            terms.add(term)
        self.at("three_products")
        self.play(FlashAround(unit_magnitudes, color=YELLOW), run_time=0.7)
        self.at("three_bounds")
        self.play(
            *(
                Transform(term, formula(bound, size=39, color=YELLOW).move_to(term))
                for term, (_, _, bound) in zip(terms, expressions, strict=True)
            ),
            run_time=1.3,
        )

        self.section("general_bounds", "Count products of distinct roots")
        self.show(
            formula(
                r"q_m(X)=\prod_{j=1}^{r}(X-\alpha_j),\qquad r\le d", size=42
            ).move_to(UP * 1.6),
            formula(r"|\alpha_j|=1", size=39, color=BLUE_C).move_to(UP * 0.45),
        )
        self.at("general_products")
        product_sum = formula(
            r"|a_{m,k}|=\left|\sum_{\substack{S\subseteq\{1,\ldots,r\}\\ |S|=k}}"
            r"\prod_{j\in S}\alpha_j\right|",
            size=44,
            width=11,
        ).move_to(DOWN * 1.0)
        self.show(product_sum)
        self.at("general_count")
        self.show(
            formula(r"\binom rk\text{ terms}", size=40).move_to(
                LEFT * 3.8 + DOWN * 2.6
            ),
            formula(r"\left|\prod_{j\in S}\alpha_j\right|=1", size=40).move_to(
                RIGHT * 3.2 + DOWN * 2.6
            ),
            run_time=1,
        )
        self.at("general_bound")
        bound = formula(r"|a_{m,k}|\le\binom rk\le\binom dk", size=48, color=YELLOW)
        bound.move_to(DOWN * 1)
        self.play(Transform(product_sum, bound), run_time=1)
        self.at("general_independent")
        self.show(
            words(
                "d is fixed · the bound is independent of m", size=27, color=BLUE_C
            ).move_to(DOWN * 3.6),
            run_time=0.8,
        )

        self.section("integer_choices", "Bounded integers leave finitely many choices")
        self.show(
            formula(r"B_k=\binom dk,\qquad a_{m,k}\in\mathbb Z", size=42).move_to(
                UP * 1.75
            ),
            formula(r"-B_k\le a_{m,k}\le B_k", size=42, color=YELLOW).move_to(UP * 0.6),
        )
        self.at("choices_lists")
        rows = VGroup()
        for j, label in enumerate(["1", "2", "r"]):
            row = (
                VGroup(
                    formula(rf"a_{{m,{label}}}\in", size=33),
                    formula(rf"\{{-B_{label},\ldots,0,\ldots,B_{label}\}}", size=33),
                )
                .arrange(RIGHT, buff=0.3)
                .move_to(DOWN * (0.65 + j * 0.85))
            )
            rows.add(row)
        self.show(rows, run_time=1.2)
        self.at("choices_monic")
        self.show(
            words(
                "Leading coefficient 1 · degree r ≤ d", size=26, color=BLUE_C
            ).move_to(DOWN * 3.5),
            run_time=0.8,
        )
        self.at("choices_polynomials")
        polynomials = VGroup(
            *(
                formula(label, size=39).move_to((j - 1.5) * 3.6 * RIGHT + DOWN * 1.3)
                for j, label in enumerate([r"q_1(X)", r"q_2(X)", r"\cdots", r"q_L(X)"])
            )
        )
        self.body.add(polynomials)
        self.play(TransformFromCopy(rows, polynomials), FadeOut(rows), run_time=1.2)
        self.body.remove(rows)
        self.show(
            words(
                "Only finitely many monic integer polynomials", size=29, color=YELLOW
            ).move_to(DOWN * 2.6),
            run_time=0.8,
        )

        self.section("finite_roots", "A finite union of finite root sets")
        polynomials = VGroup(
            *(
                formula(label, size=38).move_to((j - 1.5) * 3.6 * RIGHT + UP * 1.6)
                for j, label in enumerate([r"q_1", r"q_2", r"\cdots", r"q_L"])
            )
        )
        self.show(polynomials)
        root_sets = VGroup(
            *(
                formula(label, size=30).move_to((j - 1.5) * 3.6 * RIGHT + UP * 0.25)
                for j, label in enumerate(
                    [
                        r"\{\rho_{1,1},\ldots\}",
                        r"\{\rho_{2,1},\ldots\}",
                        r"\cdots",
                        r"\{\rho_{L,1},\ldots\}",
                    ]
                )
            )
        )
        self.at("finite_collect")
        self.copy_to(polynomials, root_sets, run_time=1.1)
        slots = VGroup(
            *(
                Circle(radius=0.35)
                .set_color(BLUE_C)
                .move_to((j - 2) * 1.5 * RIGHT + DOWN * 1.35)
                for j in range(5)
            )
        )
        slot_labels = VGroup(
            *(
                formula(label, size=27).move_to(slot)
                for label, slot in zip(
                    [r"\rho_1", r"\rho_2", r"\cdots", r"\rho_{N-1}", r"\rho_N"],
                    slots,
                    strict=True,
                )
            )
        )
        self.body.add(slots, slot_labels)
        schematic = words("Finite root slots · schematic", size=23).move_to(DOWN * 0.55)
        self.body.add(schematic)
        self.play(
            TransformFromCopy(root_sets, slot_labels),
            FadeIn(slots),
            FadeIn(schematic),
            run_time=1.1,
        )
        self.show(
            formula(
                r"S=\bigcup_{j=1}^{L}\operatorname{Roots}(q_j),\qquad |S|=N<\infty",
                size=34,
            ).move_to(DOWN * 2.5),
            run_time=0.8,
        )
        self.at("finite_powers")
        powers = formula(r"z,z^2,\ldots,z^{N+1}\in S", size=43, color=YELLOW).move_to(
            DOWN * 3.5
        )
        self.show(powers, run_time=1)
        self.at("finite_collision")
        self.play(
            FadeOut(schematic),
            Transform(slot_labels[2], formula(r"\rho_j", size=27).move_to(DOWN * 1.95)),
            run_time=0.3,
        )
        self.body.remove(schematic)
        repeated_powers = VGroup(
            formula(r"z^a", size=33, color=YELLOW).move_to(LEFT * 2 + DOWN * 0.55),
            formula(r"z^b", size=33, color=YELLOW).move_to(RIGHT * 2 + DOWN * 0.55),
        )
        self.copy_to(powers, repeated_powers, run_time=0.5)
        reused = VGroup(
            *(
                Dot(slots[2].get_center(), radius=0.055).set_color(YELLOW)
                for _ in range(2)
            )
        )
        self.body.add(reused)
        self.play(
            *(
                TransformFromCopy(power, dot)
                for power, dot in zip(repeated_powers, reused, strict=True)
            ),
            FlashAround(slots[2], color=YELLOW),
            run_time=0.9,
        )

        self.section("repeat", "Two actual powers agree; cancel a nonzero factor")
        equal = formula(r"z^a=z^b,\qquad 0<a<b", size=51).move_to(UP * 1.65)
        self.show(equal)
        self.at("repeat_nonzero")
        self.show(
            formula(
                r"|z|=1\quad\Longrightarrow\quad z\ne0", size=39, color=BLUE_C
            ).move_to(UP * 0.5),
            run_time=0.8,
        )
        self.at("repeat_factor")
        pieces = (
            VGroup(
                formula(r"z^a", size=57),
                formula("=", size=57),
                formula(r"z^a", size=57),
                formula(r"z^{b-a}", size=57),
            )
            .arrange(RIGHT, buff=0.22)
            .move_to(DOWN * 1)
        )
        self.copy_to(equal, pieces, run_time=1)
        self.at("repeat_cancel")
        strikes = VGroup(
            *(
                Line(part.get_corner(LEFT + DOWN), part.get_corner(RIGHT + UP))
                for part in [pieces[0], pieces[2]]
            )
        ).set_stroke(YELLOW, width=3)
        self.show(strikes, run_time=0.5)
        conclusion = formula(r"\boxed{z^{b-a}=1}", size=59, color=YELLOW).move_to(
            DOWN * 2.65
        )
        self.copy_to(pieces, conclusion, run_time=1)
        self.at("repeat_positive")
        self.show(
            words("b − a is a positive integer", size=26).move_to(DOWN * 3.55),
            run_time=0.8,
        )

        self.section("apply", "Apply the criterion to the alternating product")
        self.show(formula(r"z=\Delta(f)", size=48).move_to(UP * 1.65))
        self.at("apply_hypotheses")
        self.show(
            words("Algebraic integer", size=29).move_to(LEFT * 4 + UP * 0.5),
            formula(r"|\sigma(\Delta(f))|=1\quad\forall\sigma", size=36).move_to(
                RIGHT * 3.4 + UP * 0.5
            ),
        )
        self.at("apply_order")
        center = RIGHT * 4.7 + DOWN * 1.5
        circle = Circle(radius=0.95).set_color(BLUE_C).move_to(center)
        pointer = Arrow(center, center + RIGHT * 0.95, buff=0).set_color(YELLOW)
        self.show(
            formula(
                r"\Delta(f)^R=1,\qquad R\in\mathbb Z_{>0}", size=44, color=YELLOW
            ).move_to(LEFT * 2.7 + DOWN * 1),
            circle,
            pointer,
            words(
                "Schematic finite orbit · order unspecified", size=20, width=5.8
            ).move_to(RIGHT * 4.7 + DOWN * 2.9),
            run_time=1,
        )
        self.play(Rotate(pointer, TAU, about_point=center), run_time=1.3)
        self.at("apply_odd")
        self.show(
            words("Odd order still needs proof", size=29).move_to(
                LEFT * 3 + DOWN * 2.3
            ),
            run_time=0.8,
        )
        self.at("apply_next")
        self.show(
            words("Next · 4.6 uses residue one", size=27, color=BLUE_C).move_to(
                DOWN * 3.6
            ),
            run_time=0.8,
        )
