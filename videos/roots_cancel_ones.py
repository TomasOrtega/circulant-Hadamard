import json
from math import cos, sin

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    TAU,
    UP,
    YELLOW,
    Arrow,
    FadeOut,
    Line,
    RoundedRectangle,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class RootsCancelOnes(NodeScene):
    node_id = "roots-cancel-ones"
    title = "8.1 · Nontrivial roots cancel the ones"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def erase(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.4)
        self.body.remove(*objects)

    def input_card(self, subset, value, center):
        outline = RoundedRectangle(width=3.3, height=1.3, corner_radius=0.1)
        outline.set_stroke(BLUE_C, 2)
        return VGroup(
            outline,
            formula(subset, size=32).move_to(UP * 0.3),
            formula(value, size=37, color=BLUE_C).move_to(DOWN * 0.3),
        ).move_to(center)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/roots-cancel-ones.json").read_text()
        )["detail_cues"]

        self.section("inputs", "Separate the nonempty subsets from the input one")
        conditions = formula(
            r"u>1\text{ odd},\qquad I=\{p:p\mid u\}", size=40, color=BLUE_C
        ).move_to(UP * 2.05)
        polynomial = formula(r"J(P)=\sum_{r=0}^{u^2-1}P^r", size=52).move_to(UP * 0.5)
        roots = formula(
            r"\zeta_S=\prod_{p\in S}\zeta_p,\quad\operatorname{ord}(\zeta_p)=p",
            size=42,
            color=BLUE_C,
        ).move_to(DOWN * 1.2)
        self.show(conditions, run_time=0.8)
        self.at("input_polynomial")
        self.show(polynomial, run_time=1)
        self.at("input_roots")
        self.show(roots, run_time=1)
        self.at("input_empty")
        self.erase(conditions, polynomial, roots)
        empty = self.input_card(r"S=\varnothing", "P=1", LEFT * 3.7 + UP * 0.6)
        nonempty = self.input_card(
            r"S\ne\varnothing", r"P=\zeta_S", RIGHT * 3.7 + UP * 0.6
        )
        self.show(empty, nonempty, run_time=1)
        self.show(
            words("Waiting for Node 8.2", size=27, color=BLUE_C).move_to(
                LEFT * 3.7 + DOWN * 1
            ),
            run_time=0.8,
        )
        self.at("input_target")
        self.show(
            formula(
                r"J(\zeta_S)=0\quad(S\ne\varnothing)", size=47, color=YELLOW
            ).move_to(RIGHT * 1.8 + DOWN * 2.35),
            run_time=1,
        )

        self.section("order_proof", "The order is the product of the distinct primes")
        self.show(
            formula(
                r"m=\prod_{p\in S}p\quad\text{squarefree},\qquad S\ne\varnothing",
                size=40,
                color=BLUE_C,
            ).move_to(UP * 1.95),
            run_time=1,
        )
        self.at("order_divides")
        self.show(
            formula(
                r"\zeta_S^m=1\quad\Longrightarrow"
                r"\quad\operatorname{ord}(\zeta_S)\mid m",
                size=43,
            ).move_to(UP * 0.6),
            run_time=1,
        )
        isolated = formula(
            r"\zeta_S^{m/p}=\zeta_p^{m/p}\prod_{q\in S\setminus\{p\}}\zeta_q^{m/p}",
            size=42,
            color=BLUE_C,
        ).move_to(DOWN * 0.8)
        self.at("order_fix_prime")
        self.show(isolated, run_time=1.1)
        self.at("order_kill")
        self.play(
            Transform(
                isolated,
                formula(
                    r"\zeta_S^{m/p}=\zeta_p^{m/p}\cdot1", size=51, color=BLUE_C
                ).move_to(isolated),
            ),
            run_time=1,
        )
        self.at("order_nontrivial")
        self.play(
            Transform(
                isolated,
                formula(
                    r"\zeta_S^{m/p}=\zeta_p^{m/p}\ne1", size=51, color=YELLOW
                ).move_to(isolated),
            ),
            run_time=0.9,
        )
        reason = formula(r"p\nmid m/p", size=39).move_to(DOWN * 2)
        self.show(reason, run_time=0.7)
        self.at("order_all_primes")
        self.play(
            Transform(
                reason,
                formula(
                    r"p\mid\operatorname{ord}(\zeta_S)\quad\text{for every }p\in S",
                    size=38,
                ).move_to(reason),
            ),
            run_time=1,
        )
        self.show(
            formula(r"\operatorname{ord}(\zeta_S)=m", size=47, color=YELLOW).move_to(
                DOWN * 3.1
            ),
            run_time=0.9,
        )

        self.section("order_example", "Isolate each prime-root factor · u = 15")
        title = formula(
            r"u=15,\quad S=\{3,5\},\quad\eta=\zeta_3\zeta_5", size=43, color=BLUE_C
        ).move_to(UP * 2)
        self.show(title, run_time=1)
        fifth = formula(r"\eta^5=\zeta_3^5\zeta_5^5", size=45).move_to(
            LEFT * 3.5 + UP * 0.45
        )
        third = formula(r"\eta^3=\zeta_3^3\zeta_5^3", size=45).move_to(
            RIGHT * 3.5 + UP * 0.45
        )
        self.at("example_fifth")
        self.show(fifth, run_time=0.8)
        self.play(
            Transform(
                fifth,
                formula(r"\eta^5=\zeta_3^5\ne1", size=47, color=YELLOW).move_to(fifth),
            ),
            run_time=0.9,
        )
        self.at("example_third")
        self.show(third, run_time=0.8)
        self.play(
            Transform(
                third,
                formula(r"\eta^3=\zeta_5^3\ne1", size=47, color=YELLOW).move_to(third),
            ),
            run_time=0.9,
        )
        order = formula(
            r"\eta^{15}=1,\quad\eta^5\ne1,\quad\eta^3\ne1"
            r"\quad\Longrightarrow\quad\operatorname{ord}(\eta)=15",
            size=35,
            color=BLUE_C,
        ).move_to(DOWN * 1.2)
        self.at("example_order")
        self.show(order, run_time=1)
        self.at("example_general")
        self.erase(fifth, third, order)
        self.play(
            Transform(
                title,
                formula(
                    r"S\ne\varnothing:\qquad1<m\mid u^2", size=47, color=BLUE_C
                ).move_to(title),
            ),
            run_time=0.8,
        )
        self.show(
            formula(r"\zeta_S\ne1", size=58, color=YELLOW).move_to(
                LEFT * 3.2 + DOWN * 0.15
            ),
            formula(r"\zeta_S^{u^2}=1", size=58, color=YELLOW).move_to(
                RIGHT * 3.2 + DOWN * 0.15
            ),
            run_time=1.1,
        )

        self.section(
            "geometric_identity", "A formal polynomial identity, before evaluation"
        )
        self.show(
            formula(
                r"N=u^2,\qquad J(P)=\sum_{r=0}^{N-1}P^r", size=40, color=BLUE_C
            ).move_to(UP * 2.05),
            run_time=1,
        )
        xs = [2.04 * (r - 2.5) for r in range(6)]
        upper_tex = [None, "P", "+P^2", r"+\cdots", "+P^{N-1}", "+P^N"]
        lower_tex = ["-1", "-P", "-P^2", r"-\cdots", "-P^{N-1}", None]
        upper = {
            r: formula(tex, size=36, color=BLUE_C).move_to(RIGHT * xs[r] + UP * 0.55)
            for r, tex in enumerate(upper_tex)
            if tex is not None
        }
        lower = {
            r: formula(tex, size=36).move_to(RIGHT * xs[r] + DOWN * 0.8)
            for r, tex in enumerate(lower_tex)
            if tex is not None
        }
        upper_row = VGroup(*upper.values())
        lower_row = VGroup(*lower.values())
        row_labels = VGroup(
            formula("PJ", size=32, color=BLUE_C).move_to(LEFT * 7.2 + UP * 0.55),
            formula("-J", size=32).move_to(LEFT * 7.2 + DOWN * 0.8),
        )
        self.at("geometric_shift")
        self.show(upper_row, row_labels[0], run_time=1)
        self.at("geometric_subtract")
        self.show(lower_row, row_labels[1], run_time=1)
        self.at("geometric_cancel")
        middle = [upper[r] for r in range(1, 5)] + [lower[r] for r in range(1, 5)]
        strikes = VGroup(
            *(
                Line(
                    term.get_corner(UP + LEFT) + LEFT * 0.04,
                    term.get_corner(DOWN + RIGHT) + RIGHT * 0.04,
                ).set_stroke(YELLOW, 2)
                for term in middle
            )
        )
        self.show(strikes, run_time=0.8)
        self.play(*(FadeOut(term) for term in middle), run_time=0.8)
        upper_row.remove(*(upper[r] for r in range(1, 5)))
        lower_row.remove(*(lower[r] for r in range(1, 5)))
        self.at("geometric_endpoints")
        identity = formula(r"(P-1)J(P)=P^N-1", size=56, color=YELLOW).move_to(
            DOWN * 2.5
        )
        self.body.add(identity)
        self.play(TransformFromCopy(VGroup(upper[5], lower[0]), identity), run_time=1.2)
        self.erase(upper_row, lower_row, *row_labels, strikes)
        self.play(identity.animate.move_to(DOWN * 0.2), run_time=0.8)

        self.section(
            "exact_zero", "Evaluate first; cancel the nonzero factor in the domain"
        )
        self.show(
            formula(
                r"S\ne\varnothing,\qquad\zeta_S^{u^2}=1", size=45, color=BLUE_C
            ).move_to(UP * 2.05),
            run_time=1,
        )
        factor = formula(r"(\zeta_S-1)", size=53, color=YELLOW)
        value = formula(r"J(\zeta_S)", size=53, color=BLUE_C)
        rhs = formula("=0", size=53)
        equation = (
            VGroup(factor, value, rhs).arrange(RIGHT, buff=0.3).move_to(UP * 0.45)
        )
        self.at("zero_equation")
        self.show(equation, run_time=1.1)
        self.at("zero_domain")
        self.show(
            formula(
                r"A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]\subseteq\mathbb C",
                size=36,
                color=BLUE_C,
            ).move_to(DOWN * 0.85),
            run_time=1,
        )
        self.at("zero_factor")
        self.show(
            formula(r"\zeta_S-1\ne0", size=41, color=YELLOW).move_to(DOWN * 1.9),
            run_time=0.8,
        )
        self.at("zero_cancel")
        strike = Line(
            factor.get_corner(UP + LEFT) + LEFT * 0.06,
            factor.get_corner(DOWN + RIGHT) + RIGHT * 0.06,
        ).set_stroke(YELLOW, 3)
        self.show(strike, run_time=0.5)
        self.play(FadeOut(factor), run_time=0.6)
        equation.remove(factor)
        self.erase(equation, strike)
        self.show(
            formula(r"J(\zeta_S)=0", size=65, color=YELLOW).move_to(UP * 0.45),
            run_time=1,
        )
        self.at("zero_exact")
        self.show(
            words("Exact zero · before reducing modulo 1 + i", size=29).move_to(
                DOWN * 3.1
            ),
            run_time=0.9,
        )

        self.section("nine_powers", "Nine powers repeat the same three roots")
        self.show(
            formula(
                r"u=3,\qquad\omega=e^{2\pi i/3},\qquad\omega^3=1", size=42, color=BLUE_C
            ).move_to(UP * 2.05),
            run_time=1,
        )
        powers = VGroup(
            *(
                formula(
                    "1" if r == 0 else r"\omega" if r == 1 else rf"\omega^{r}",
                    size=35,
                    color=BLUE_C,
                ).move_to(RIGHT * (1.3 * (r - 4)) + UP * 0.15)
                for r in range(9)
            )
        )
        self.at("nine_repeat")
        self.show(powers, run_time=1.1)
        values = ["1", r"\omega", r"\omega^2"] * 3
        self.play(
            *(
                Transform(power, formula(tex, size=35, color=YELLOW).move_to(power))
                for power, tex in zip(powers, values, strict=True)
            ),
            run_time=1.2,
        )
        self.at("nine_groups")
        brackets = VGroup(
            *(
                SurroundingRectangle(
                    VGroup(*powers[3 * j : 3 * j + 3]), buff=0.18
                ).set_stroke(BLUE_C, 2)
                for j in range(3)
            )
        )
        self.show(brackets, run_time=0.8)
        self.show(
            formula(r"J(\omega)=3(1+\omega+\omega^2)=0", size=49, color=YELLOW).move_to(
                DOWN * 1.8
            ),
            run_time=1,
        )

        self.section(
            "triangles", "Complex vectors close before any residue calculation"
        )
        centers = [LEFT * 4.3 + DOWN * 0.8, DOWN * 0.8, RIGHT * 4.3 + DOWN * 0.8]
        directions = [
            cos(TAU * k / 3) * RIGHT + sin(TAU * k / 3) * UP for k in range(3)
        ]
        triples = VGroup(
            *(
                VGroup(
                    *(
                        Arrow(center, center + 1.25 * direction, buff=0).set_color(
                            BLUE_C
                        )
                        for direction in directions
                    )
                )
                for center in centers
            )
        )
        self.show(triples, run_time=0.6)
        self.at("triangle_head_tail")
        targets = []
        for center in centers:
            start = center + LEFT * 0.625 + DOWN * 0.36
            points = [
                start,
                start + 1.25 * directions[0],
                start + 1.25 * directions[0] + 1.25 * directions[1],
                start,
            ]
            targets.append(
                VGroup(
                    *(
                        Arrow(a, b, buff=0).set_color(BLUE_C)
                        for a, b in zip(points[:-1], points[1:], strict=True)
                    )
                )
            )
        self.play(
            *(
                Transform(triple, target)
                for triple, target in zip(triples, targets, strict=True)
            ),
            run_time=1.1,
        )
        self.at("triangle_closed")
        labels = VGroup(
            *(
                formula(r"1+\omega+\omega^2=0", size=27, color=BLUE_C).move_to(
                    center + DOWN * 1.3
                )
                for center in centers
            )
        )
        self.show(labels, run_time=0.8)
        self.at("triangle_vanish")
        self.erase(labels)
        self.play(
            *(
                Transform(triple, formula("0", size=59, color=YELLOW).move_to(center))
                for triple, center in zip(triples, centers, strict=True)
            ),
            run_time=1.1,
        )
        self.at("triangle_general")
        self.show(
            formula(
                r"J(\zeta_S)=0\qquad(S\ne\varnothing)", size=49, color=YELLOW
            ).move_to(UP * 1.7),
            run_time=1,
        )
        self.at("triangle_waiting")
        self.erase(triples)
        waiting = self.input_card(r"S=\varnothing", "P=1", LEFT * 3.5 + DOWN * 0.7)
        self.show(
            waiting,
            words("Excluded from the nonempty-subset conclusion", size=25).move_to(
                RIGHT * 2.5 + DOWN * 0.7
            ),
            run_time=1,
        )
        self.at("triangle_next")
        self.show(
            words(
                "Next · Node 8.2 evaluates the waiting input", size=29, color=BLUE_C
            ).move_to(DOWN * 2.65),
            run_time=0.9,
        )
