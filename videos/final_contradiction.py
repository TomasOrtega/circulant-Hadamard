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
    Circle,
    Cross,
    LaggedStart,
    Matrix,
    Transform,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, sign_matrix, words


class FinalContradiction(NodeScene):
    node_id = "final-contradiction"
    title = "8 · The Final Contradiction"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/final-contradiction.json").read_text()
        )["detail_cues"]

        self.section("opening", "Evaluate the same sum a second way")
        self.show(
            formula(
                r"\mathcal S=\sum_{S\subseteq I}(-1)^{|S|}"
                r"\frac{E(\zeta_S)}{c(\zeta_S)}\equiv0\pmod{1+i}",
                size=43,
                color=BLUE_C,
            ).move_to(UP * 1.2),
            words("From Node 7", size=24).move_to(UP * 2.15),
        )
        self.at("all_ones")
        self.show(
            formula(
                r"E(P)\equiv J(P)=1+P+\cdots+P^{u^2-1}\pmod{1+i}",
                size=39,
            ).move_to(DOWN * 0.8),
            words("From Node 5 · all coefficients become one", size=24).move_to(
                DOWN * 1.75
            ),
        )

        self.section("roots", "Exact cancellation at every nonempty subset")
        self.show(
            formula(
                r"u>1\text{ odd},\quad I=\{p:p\mid u,\ p\text{ prime}\}", size=38
            ).move_to(UP * 1.95),
            formula(r"\zeta_S=\prod_{p\in S}\zeta_p", size=39, color=BLUE_C).move_to(
                UP * 0.85
            ),
        )
        self.at("empty")
        empty = formula(r"\zeta_\varnothing=1", size=37)
        empty.move_to(RIGHT * 2.8 + DOWN * 3.0)
        self.show(
            empty,
            formula(
                r"S\ne\varnothing:\quad d=\operatorname{ord}(\zeta_S)>1,"
                r"\quad d\mid u^2",
                size=34,
                width=8,
                color=BLUE_C,
            ).move_to(RIGHT * 2.6 + DOWN * 0.4),
        )
        self.at("geometric")
        self.show(
            formula(
                r"J(\zeta_S)=\frac{u^2}{d}"
                r"\underbrace{(1+\zeta_S+\cdots+\zeta_S^{d-1})}_{0}=0",
                size=33,
                width=9,
            ).move_to(RIGHT * 2.8 + DOWN * 1.6)
        )
        point = LEFT * 6.3 + DOWN * 2.5
        arrows = VGroup()
        for k in range(5):
            following = point + cos(TAU * k / 5) * RIGHT + sin(TAU * k / 5) * UP
            arrows.add(Arrow(point, following, buff=0).set_color(BLUE_C))
            point = following
        self.show(arrows, run_time=1.5)
        self.show(
            words("Closed sum · illustration d = 5", size=20, width=4).move_to(
                LEFT * 5.6 + DOWN * 3.25
            )
        )
        self.at("value_at_one")
        self.play(
            Transform(
                empty,
                formula(
                    r"\zeta_\varnothing=1\quad\Longrightarrow\quad J(1)=u^2",
                    size=36,
                    color=YELLOW,
                ).move_to(empty),
            ),
            run_time=1.2,
        )

        self.section("units", "Reduce the numerators; retain the unit denominators")
        expression = formula(
            r"\mathcal S=\frac{E(1)}{c(1)}+"
            r"\sum_{\varnothing\ne S\subseteq I}(-1)^{|S|}"
            r"\frac{E(\zeta_S)}{c(\zeta_S)}",
            size=39,
        ).move_to(UP * 1.25)
        self.show(expression)
        self.play(
            Transform(
                expression,
                formula(
                    r"\mathcal S\equiv\frac{J(1)}{c(1)}+"
                    r"\sum_{\varnothing\ne S\subseteq I}(-1)^{|S|}"
                    r"\frac{J(\zeta_S)}{c(\zeta_S)}\pmod{1+i}",
                    size=39,
                ).move_to(expression),
            ),
            run_time=1.5,
        )
        self.at("inverse")
        self.show(
            formula(
                r"\frac1{c(\zeta_S)}=\frac{\overline{c(\zeta_S)}}{u^2}",
                size=43,
                color=BLUE_C,
            ).move_to(DOWN * 0.55),
            words(
                "Invert odd u before reducing · every denominator is a unit", size=25
            ).move_to(DOWN * 1.55),
        )
        self.at("discard")
        self.play(
            Transform(
                expression,
                formula(
                    r"\mathcal S\equiv\frac{J(1)}{c(1)}+0\pmod{1+i}",
                    size=49,
                    color=YELLOW,
                ).move_to(expression),
            ),
            run_time=1.5,
        )
        self.show(words("Only the empty subset survives", size=27).move_to(DOWN * 2.75))

        self.section("survivor", "An odd integer leaves residue one")
        survivor = formula(r"\mathcal S\equiv\frac{J(1)}{c(1)}", size=51, color=BLUE_C)
        survivor.move_to(UP * 1.4)
        self.show(survivor)
        self.at("signed_u")
        self.play(
            Transform(
                survivor,
                formula(r"\frac{J(1)}{c(1)}=\frac{u^2}{\pm u}=\pm u", size=51).move_to(
                    survivor
                ),
            ),
            run_time=1.3,
        )
        self.at("parity")
        self.show(
            formula(r"u=2k+1,\qquad -1\equiv1\pmod{1+i}", size=40).move_to(UP * 0.1)
        )
        pairs = VGroup(*(formula(r"(1+1)", size=35) for _ in range(3)))
        tail = VGroup(formula(r"\cdots", size=36), formula("1", size=45, color=YELLOW))
        chain = VGroup(*pairs, *tail).arrange(RIGHT, buff=0.4).move_to(DOWN * 1.4)
        self.show(chain)
        self.play(
            LaggedStart(
                *(
                    Transform(pair, formula("0", size=35).move_to(pair))
                    for pair in pairs
                ),
                lag_ratio=0.2,
            ),
            run_time=1.6,
        )
        self.show(
            formula(r"\mathcal S\equiv1\pmod{1+i}", size=49, color=YELLOW).move_to(
                DOWN * 2.8
            )
        )

        self.section("conflict", "One sum cannot have two different residues")
        zero = formula(r"\mathcal S\equiv0", size=56, color=BLUE_C).move_to(
            LEFT * 3.8 + UP * 0.8
        )
        one = formula(r"\mathcal S\equiv1", size=56, color=YELLOW).move_to(
            RIGHT * 3.8 + UP * 0.8
        )
        self.show(
            zero,
            one,
            words("Node 7", size=25).next_to(zero, UP, buff=0.4),
            words("The all-ones calculation", size=25).next_to(one, UP, buff=0.4),
        )
        self.at("nonzero")
        distinct = formula(r"0\ne1\pmod{1+i}", size=61, color=YELLOW).move_to(
            DOWN * 1.2
        )
        self.show(
            Arrow(zero.get_bottom(), distinct.get_top() + LEFT, buff=0.15).set_color(
                BLUE_C
            ),
            Arrow(one.get_bottom(), distinct.get_top() + RIGHT, buff=0.15).set_color(
                YELLOW
            ),
            distinct,
        )
        self.show(
            words(
                "The reduction ring is nonzero · every odd u > 1 is excluded", size=27
            ).move_to(DOWN * 2.9)
        )

        self.section("orders", "Return to the restriction on n")
        self.show(
            formula(
                r"n>1\quad\Longrightarrow\quad n=4u^2,\quad u\text{ odd}", size=47
            ).move_to(UP * 1.5)
        )
        candidates = VGroup(*(formula(str(u), size=43) for u in [1, 3, 5, 7]))
        candidates.add(formula(r"\cdots", size=43))
        candidates.arrange(RIGHT, buff=1.0).move_to(DOWN * 0.15)
        self.show(
            candidates, words("Possible u", size=24).move_to(LEFT * 5.6 + DOWN * 0.15)
        )
        crosses = VGroup(*(Cross(value).set_color(YELLOW) for value in candidates[1:]))
        self.show(crosses)
        self.at("u_one")
        self.focus(candidates[0])
        self.show(
            formula(
                r"u=1\Longrightarrow n=4\qquad\text{or the separate case }n=1",
                size=43,
                color=YELLOW,
            ).move_to(DOWN * 2.2)
        )

        self.section("examples", "Both remaining orders occur")
        small = Matrix([[1]]).set_color(BLUE_C).move_to(LEFT * 4.0 + UP * 0.15)
        self.show(small, formula("n=1", size=35).next_to(small, DOWN, buff=0.5))
        self.at("four_example")
        matrix = sign_matrix(size=0.7).move_to(RIGHT * 3.1 + UP * 0.15)
        self.show(matrix, formula("n=4", size=35).next_to(matrix, DOWN, buff=0.4))
        self.show(
            formula(r"HH^{\mathsf T}=4I_4", size=36, color=BLUE_C).move_to(DOWN * 2.0)
        )
        self.at("theorem")
        self.show(
            formula(
                r"\boxed{\text{A real circulant Hadamard matrix exists}"
                r"\quad\iff\quad n\in\{1,4\}}",
                size=37,
                color=YELLOW,
            ).move_to(UP * 2.0)
        )
        self.at("map")
        steps = (
            VGroup(
                *(
                    VGroup(
                        Circle(radius=0.22).set_color(BLUE_C), formula(str(k), size=21)
                    )
                    for k in range(1, 9)
                )
            )
            .arrange(RIGHT, buff=0.45)
            .move_to(DOWN * 3.0)
        )
        self.show(steps, run_time=1.5)
