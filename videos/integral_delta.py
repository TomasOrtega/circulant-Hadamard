import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    Arrow,
    Ellipse,
    FadeOut,
    Line,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class IntegralDelta(NodeScene):
    node_id = "integral-delta"
    title = "4.4 · Why the Product Is Integral"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def hide(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.35)
        self.body.remove(*objects)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/integral-delta.json").read_text()
        )["detail_cues"]

        self.section("regroup", "Pair subsets in one prime direction")
        self.show(
            formula(r"u>1\text{ odd},\qquad f(P)f^*(P)=u^2", size=39).move_to(
                UP * 2.05
            ),
            formula(
                r"f\in\mathbb Z[i][P]/(P^{u^2}-1),\qquad I=\{p\text{ prime}:p\mid u\}",
                size=32,
            ).move_to(UP * 0.95),
        )
        self.at("ring")
        ring = formula(r"B=\mathbb Z[i,\{\zeta_p:p\in I\}]", size=41, color=BLUE_C)
        ring.move_to(DOWN * 0.35)
        self.show(ring)
        self.at("pair")
        pairing = formula(
            r"S\longleftrightarrow S\cup\{p\}\qquad(p\notin S)",
            size=40,
            color=YELLOW,
        ).move_to(DOWN * 1.6)
        self.show(pairing, run_time=0.9)
        self.at("paired_product")
        paired_product = formula(
            r"\Delta(f)=\prod_{\substack{S\subseteq I\\p\notin S}}"
            r"\left(\frac{f(\zeta_S)}{f(\zeta_{S\cup\{p\}})}\right)^{(-1)^{|S|}}",
            size=43,
        ).move_to(DOWN * 2.9)
        self.show(paired_product, run_time=1.4)

        self.at("two_primes")
        self.hide(*list(self.body))
        direction = words(
            "Two distinct primes p, q · original alternating product", size=27
        )
        direction.move_to(UP * 2.05)
        delta = formula(r"\Delta(f)", size=45, color=BLUE_C).move_to(
            LEFT * 6.5 + DOWN * 0.25
        )
        equals = formula("=", size=45).next_to(delta, RIGHT, buff=0.3)
        positions = {
            "upper_left": LEFT * 2.2 + UP * 0.7,
            "lower_left": LEFT * 2.2 + DOWN * 1.25,
            "upper_right": RIGHT * 3.3 + UP * 0.7,
            "lower_right": RIGHT * 3.3 + DOWN * 1.25,
        }
        values = {
            "one": formula(r"f(1)", size=43, color=BLUE_C).move_to(
                positions["upper_left"]
            ),
            "p": formula(r"f(\zeta_p)", size=43, color=BLUE_C).move_to(
                positions["lower_left"]
            ),
            "q": formula(r"f(\zeta_q)", size=43, color=BLUE_C).move_to(
                positions["lower_right"]
            ),
            "pq": formula(r"f(\zeta_p\zeta_q)", size=43, color=BLUE_C).move_to(
                positions["upper_right"]
            ),
        }
        whole_bar = Line(LEFT * 4.4, RIGHT * 5.5).set_stroke(width=2)
        whole_bar.move_to(RIGHT * 0.55 + DOWN * 0.25)
        self.show(direction, delta, equals, *values.values(), whole_bar, run_time=1.2)
        self.at("inverted")
        left_bar = Line(LEFT * 1.8, RIGHT * 1.8).set_stroke(width=2)
        left_bar.move_to(LEFT * 2.2 + DOWN * 0.25)
        right_bar = Line(LEFT * 2.05, RIGHT * 2.05).set_stroke(width=2)
        right_bar.move_to(RIGHT * 3.3 + DOWN * 0.25)
        brackets = VGroup(
            formula(r"\bigg(", size=67).move_to(RIGHT * 0.95 + DOWN * 0.25),
            formula(r"\bigg)^{-1}", size=67, color=YELLOW).move_to(
                RIGHT * 5.85 + UP * 0.05
            ),
            formula(r"\cdot", size=45).move_to(LEFT * 0.05 + DOWN * 0.25),
        )
        self.body.add(right_bar, brackets)
        self.play(
            Transform(whole_bar, left_bar),
            values["q"].animate.move_to(positions["upper_right"]),
            values["pq"].animate.move_to(positions["lower_right"]),
            Transform(
                direction,
                words("Same four factors · paired in the p direction", size=28).move_to(
                    direction
                ),
            ),
            run_time=1.5,
        )
        self.show(right_bar, brackets, run_time=0.6)
        self.at("same_number")
        fixed_number = words("One fixed Δ(f) · only the grouping changes", size=29)
        fixed_number.move_to(DOWN * 2.8)
        self.show(fixed_number, run_time=0.8)

        carried = [
            direction,
            delta,
            equals,
            *values.values(),
            whole_bar,
            right_bar,
            brackets,
        ]
        self.body.remove(*carried)
        self.section("local", "Use the local comparison above every divisor of u")
        self.body.add(*carried)
        self.at("local_ratio")
        frames = VGroup(
            SurroundingRectangle(
                VGroup(values["one"], values["p"], whole_bar), buff=0.18
            ).set_color(YELLOW),
            SurroundingRectangle(
                VGroup(values["q"], values["pq"], right_bar, brackets[0], brackets[1]),
                buff=0.18,
            ).set_color(YELLOW),
        )
        statuses = VGroup(
            words("unit · residue 1", size=27, color=YELLOW).move_to(
                LEFT * 2.2 + DOWN * 2.3
            ),
            words("unit · residue 1", size=27, color=YELLOW).move_to(
                RIGHT * 3.3 + DOWN * 2.3
            ),
        )
        self.show(frames, statuses, run_time=1.0)
        self.at("unit_inverse")
        inverse_note = formula(
            r"r\equiv1\quad\Longrightarrow\quad r^{-1}\equiv1",
            size=34,
            color=YELLOW,
        ).move_to(DOWN * 3.3)
        self.show(inverse_note, run_time=0.8)
        self.at("delta_unit")
        self.hide(frames, inverse_note)
        self.play(
            Transform(
                statuses,
                formula(
                    r"\Delta(f)\in B_{\mathfrak m}^{\times},\qquad"
                    r"\Delta(f)\equiv1\pmod{\mathfrak m}\quad(\mathfrak m\ni p)",
                    size=36,
                    color=YELLOW,
                ).move_to(DOWN * 2.7),
            ),
            run_time=1.0,
        )
        self.at("q_direction")
        self.hide(statuses)
        self.play(
            values["p"].animate.move_to(positions["upper_right"]),
            values["q"].animate.move_to(positions["lower_left"]),
            Transform(
                direction,
                words("Same four factors · paired in the q direction", size=28).move_to(
                    direction
                ),
            ),
            run_time=1.6,
        )
        self.show(
            formula(
                r"\mathfrak m\ni q:\quad\text{each ratio is a unit of residue }1",
                size=35,
                color=YELLOW,
            ).move_to(DOWN * 2.6),
            run_time=0.9,
        )
        self.at("all_divisors")
        self.show(
            formula(
                r"\forall p\mid u,\ \forall\mathfrak m\ni p:\quad"
                r"\Delta(f)\in B_{\mathfrak m}^{\times},\quad\Delta(f)\equiv1",
                size=34,
                color=BLUE_C,
            ).move_to(DOWN * 3.5),
            run_time=1.1,
        )

        self.section("other", "At the remaining maximal ideals, u is invertible")
        self.show(
            formula(r"\mathfrak m\in\operatorname{Max}(B)", size=39).move_to(UP * 2.05),
            formula(r"p\mid u,\ p\in\mathfrak m", size=35, color=BLUE_C).move_to(
                LEFT * 4.15 + UP * 1.0
            ),
            words("paired ratios: already checked", size=25, color=BLUE_C).move_to(
                LEFT * 4.15 + UP * 0.2
            ),
            formula(r"p\notin\mathfrak m\text{ for every }p\mid u", size=35).move_to(
                RIGHT * 3.75 + UP * 1.0
            ),
        )
        self.at("u_invertible")
        self.show(
            formula(r"u^2\in B_{\mathfrak m}^{\times}", size=40, color=YELLOW).move_to(
                RIGHT * 3.75 + UP * 0.15
            ),
            run_time=0.85,
        )
        self.at("explicit_inverse")
        value = formula(r"f(\zeta_S)", size=45, color=BLUE_C)
        inverse = formula(r"\frac{\overline{f(\zeta_S)}}{u^2}", size=45, color=YELLOW)
        product = VGroup(value, formula(r"\cdot", size=45), inverse)
        product.arrange(RIGHT, buff=0.7).move_to(DOWN * 1.15)
        inverse_label = words("explicit inverse", size=25, color=YELLOW)
        inverse_label.next_to(inverse, DOWN, buff=0.4)
        self.show(product, inverse_label, run_time=1.1)
        self.at("multiply_inverse")
        self.hide(inverse_label)
        self.play(
            Transform(
                product,
                formula(
                    r"\frac{f(\zeta_S)\overline{f(\zeta_S)}}{u^2}"
                    r"=\frac{u^2}{u^2}=1",
                    size=45,
                    color=YELLOW,
                ).move_to(DOWN * 1.15),
            ),
            run_time=1.3,
        )
        self.at("all_factors")
        self.show(
            formula(
                r"f(\zeta_S)^{-1}=\frac{\overline{f(\zeta_S)}}{u^2}", size=36
            ).move_to(DOWN * 2.45),
            run_time=0.9,
        )
        self.at("every_local")
        self.show(
            formula(
                r"\Delta(f)\in B_{\mathfrak m}\qquad"
                r"\text{for every maximal ideal }\mathfrak m",
                size=37,
                color=BLUE_C,
            ).move_to(DOWN * 3.5),
            run_time=1.0,
        )

        self.section(
            "global", "A denominator obstruction cannot survive every local check"
        )
        self.at("suppose_outside")
        assumption = formula(r"z=\Delta(f)\notin B\quad\text{(suppose)}", size=40)
        assumption.move_to(UP * 2.05)
        self.show(assumption, run_time=0.9)
        self.at("clearing_ideal")
        ideal = formula(r"J=\{b\in B:bz\in B\}", size=42, color=BLUE_C)
        ideal.move_to(UP * 0.95)
        self.show(ideal)
        self.at("proper")
        proper = formula(r"1\notin J\quad\Longrightarrow\quad J\subsetneq B", size=38)
        proper.move_to(DOWN * 0.25)
        self.show(proper, run_time=0.9)
        self.at("maximal")
        self.hide(proper)
        maximal_boundary = Ellipse(width=5.1, height=3.2).set_stroke(BLUE_C, width=2)
        maximal_boundary.move_to(LEFT * 3.8 + DOWN * 1.45)
        ideal_boundary = Ellipse(width=2.8, height=1.65).set_stroke(YELLOW, width=2)
        ideal_boundary.move_to(LEFT * 3.8 + DOWN * 1.55)
        maximal_label = formula(r"\mathfrak m", size=40, color=BLUE_C).move_to(
            LEFT * 5.55 + DOWN * 0.7
        )
        ideal_label = formula("J", size=36, color=YELLOW).move_to(
            LEFT * 4.5 + DOWN * 1.35
        )
        self.show(maximal_boundary, ideal_boundary, maximal_label, ideal_label)
        self.at("local_fraction")
        fraction = formula(r"z=\frac as,\qquad a,s\in B", size=40)
        fraction.move_to(RIGHT * 3.6 + DOWN * 0.2)
        outside = formula(r"s\notin\mathfrak m", size=37, color=YELLOW)
        outside.move_to(RIGHT * 3.6 + DOWN * 1.3)
        denominator = formula("s", size=48, color=YELLOW).move_to(
            RIGHT * 1.75 + DOWN * 2.25
        )
        self.show(fraction, outside, denominator, run_time=1.1)
        self.at("clears")
        clears = formula(r"sz=a\in B", size=39, color=YELLOW).move_to(
            RIGHT * 3.9 + DOWN * 2.5
        )
        self.show(clears, run_time=0.8)
        self.at("inside")
        inside = formula("s", size=48, color=YELLOW).move_to(LEFT * 3.35 + DOWN * 1.6)
        arrow = Arrow(denominator.get_left(), inside.get_right(), buff=0.15).set_color(
            YELLOW
        )
        self.body.add(inside)
        self.play(TransformFromCopy(denominator, inside), run_time=1.0)
        self.show(
            arrow,
            formula(
                r"s\in J\subseteq\mathfrak m\quad\text{but}\quad s\notin\mathfrak m",
                size=36,
                color=YELLOW,
            ).move_to(DOWN * 3.55),
            run_time=0.9,
        )
        self.at("contradiction")
        self.hide(*(obj for obj in list(self.body) if obj is not assumption))
        self.play(
            Transform(
                assumption,
                formula(r"\boxed{\Delta(f)\in B}", size=48, color=YELLOW).move_to(
                    UP * 2.05
                ),
            ),
            run_time=1.1,
        )
        self.at("generators")
        self.show(
            formula(
                r"B=\mathbb Z[i,\{\zeta_p:p\in I\}]", size=38, color=BLUE_C
            ).move_to(UP * 0.95),
            words(
                "Roots of unity → algebraic integers → sums and products", size=27
            ).move_to(DOWN * 0.1),
            run_time=1.1,
        )
        self.at("integral")
        integral = words("Δ(f) is an algebraic integer", size=31, color=YELLOW)
        integral.move_to(DOWN * 1.15)
        self.show(integral, run_time=0.85)
        self.at("circle")
        circle = formula(
            r"\text{Previously proved: }|\sigma(\Delta(f))|=1"
            r"\quad\text{for every }\sigma",
            size=35,
            color=BLUE_C,
        ).move_to(DOWN * 2.2)
        self.show(circle, run_time=0.95)
        self.at("kronecker")
        self.show(
            words("Both hypotheses ready for Kronecker's theorem", size=28).move_to(
                DOWN * 3.15
            ),
            run_time=0.9,
        )
        self.at("residue")
        self.hide(*list(self.body))
        self.show(
            formula(
                r"\Delta(f)\text{ is an algebraic integer}", size=43, color=BLUE_C
            ).move_to(UP * 1.6),
            formula(
                r"\Delta(f)\equiv1\pmod{\mathfrak m}\qquad"
                r"(p\mid u,\ \mathfrak m\ni p)",
                size=42,
                color=YELLOW,
            ).move_to(DOWN * 0.2),
            words(
                "Carry the local residue forward · the order restriction comes later",
                size=27,
            ).move_to(DOWN * 2.0),
            run_time=1.2,
        )
