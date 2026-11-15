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
    Dot,
    FadeOut,
    FlashAround,
    Line,
    Rectangle,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


def cube_candidates(center, radius=1.25):
    circle = Circle(radius=radius).set_color(BLUE_C).move_to(center)
    dots = VGroup()
    labels = VGroup()
    for index, label in enumerate(["1", r"\omega", r"\omega^2"]):
        direction = cos(TAU * index / 3) * RIGHT + sin(TAU * index / 3) * UP
        dot = Dot(center + radius * direction, radius=0.07).set_color(BLUE_C)
        dots.add(dot)
        labels.add(formula(label, size=34).next_to(dot, direction, buff=0.18))
    return circle, dots, labels


class ResidueOneRigidity(NodeScene):
    node_id = "residue-one-rigidity"
    title = "6.4 · Odd Order Forces Equality"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def copy_to(self, source, target, run_time=1):
        self.body.add(target)
        self.play(TransformFromCopy(source, target), run_time=run_time)

    def erase(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.4)
        self.body.remove(*objects)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/residue-one-rigidity.json").read_text()
        )["detail_cues"]

        self.section("cube_roots", "Two arithmetic inputs will force exact equality")
        self.show(
            words("Odd order", size=33, color=BLUE_C).move_to(LEFT * 4 + UP * 1.95),
            words("Residue 1 modulo 1+i", size=31, color=BLUE_C).move_to(
                RIGHT * 3.5 + UP * 1.95
            ),
            run_time=1,
        )
        self.at("cube_begin")
        circle, dots, labels = cube_candidates(LEFT * 4.45 + DOWN * 0.55)
        self.show(circle, dots, labels, run_time=1.1)
        self.show(
            formula(r"\omega=e^{2\pi i/3}", size=42).move_to(RIGHT * 3.2 + UP * 0.5),
            words("Cube-root illustration", size=27).move_to(LEFT * 4.45 + DOWN * 2.65),
            run_time=0.8,
        )
        self.at("cube_relation")
        relation = formula(r"1+\omega+\omega^2=0", size=49, color=YELLOW)
        relation.move_to(RIGHT * 3.1 + DOWN * 1.1)
        self.show(
            relation,
            words("An exact relation, before reduction", size=27).move_to(DOWN * 3.5),
            run_time=1,
        )

        self.section("cube_reduction", "Assume a nontrivial cube root has residue one")
        circle, dots, labels = cube_candidates(LEFT * 4.9 + DOWN * 0.45, radius=1.15)
        assumption = formula(r"[\omega]=1", size=47, color=BLUE_C).move_to(
            RIGHT * 2.8 + UP * 1.55
        )
        self.show(circle, dots, labels, assumption, run_time=0.8)
        self.at("cube_square")
        powers = formula(r"[\omega^2]=[\omega]^2=1", size=42).move_to(
            RIGHT * 2.8 + UP * 0.25
        )
        self.show(powers, run_time=0.9)
        self.at("cube_other")
        self.play(
            Transform(
                assumption,
                formula(r"[\omega^2]=1", size=47, color=BLUE_C).move_to(assumption),
            ),
            Transform(
                powers, formula(r"[\omega]=[\omega^2]^2=1", size=42).move_to(powers)
            ),
            run_time=1,
        )
        self.at("cube_reduce")
        self.erase(assumption, powers)
        ones = (
            VGroup(
                *(
                    formula(label, size=52, color=YELLOW)
                    for label in ["1", "+", "1", "+", "1", "=", "0"]
                )
            )
            .arrange(RIGHT, buff=0.2)
            .move_to(RIGHT * 2.65 + UP * 0.65)
        )
        self.show(ones, run_time=1)
        self.at("cube_pair")
        pair = SurroundingRectangle(VGroup(*ones[:3]), buff=0.15).set_stroke(BLUE_C, 2)
        self.show(pair, run_time=0.5)
        self.show(
            formula(r"1+1=0\quad\text{in characteristic }2", size=34).move_to(
                RIGHT * 2.65 + DOWN * 0.7
            ),
            run_time=0.8,
        )
        self.at("cube_contradiction")
        self.erase(ones, pair)
        contradiction = formula(r"1=0", size=62, color=YELLOW).move_to(
            RIGHT * 2.7 + UP * 0.65
        )
        self.show(
            contradiction,
            words("Impossible in the nonzero target ring", size=27).move_to(
                RIGHT * 2.4 + DOWN * 1.85
            ),
            run_time=1,
        )
        self.at("cube_exclude")
        crosses = VGroup(
            *(
                Line(
                    label.get_corner(LEFT + DOWN), label.get_corner(RIGHT + UP)
                ).set_color(YELLOW)
                for label in labels[1:]
            )
        )
        self.show(
            crosses,
            words("Exclude ω and ω² using arithmetic", size=27, color=BLUE_C).move_to(
                DOWN * 3.45
            ),
            run_time=0.9,
        )
        self.play(FlashAround(labels[0], color=YELLOW), run_time=0.6)

        self.section("hypotheses", "The general lemma needs a domain before reduction")
        a_box = Rectangle(width=6.6, height=2.3).set_stroke(BLUE_C, 2)
        a_box.move_to(LEFT * 4.1 + UP * 0.6)
        target_box = Rectangle(width=6.6, height=2.3).set_stroke(YELLOW, 2)
        target_box.move_to(RIGHT * 4.1 + UP * 0.6)
        self.show(
            a_box,
            target_box,
            words("A: characteristic-zero domain", size=27).move_to(a_box),
            words("Nonzero ring · characteristic 2", size=27).move_to(target_box),
            Arrow(a_box.get_right(), target_box.get_left(), buff=0.15).set_color(
                BLUE_C
            ),
            run_time=1.1,
        )
        self.at("hypotheses_alpha")
        self.show(
            formula(
                r"\alpha\in A,\qquad\operatorname{ord}(\alpha)=r\text{ odd},\qquad "
                r"[\alpha]=1",
                size=39,
            ).move_to(DOWN * 1.6),
            run_time=1,
        )
        self.at("hypotheses_orderone")
        self.show(
            formula(
                r"r=1\quad\Longrightarrow\quad\alpha=1", size=40, color=BLUE_C
            ).move_to(DOWN * 2.65),
            run_time=0.8,
        )
        self.at("hypotheses_suppose")
        self.erase(*list(self.body))
        self.show(
            formula(
                r"\alpha\ne1,\qquad r>1\text{ odd}\quad\text{(suppose)}",
                size=45,
                color=YELLOW,
            ).move_to(UP * 0.7),
            words("Keep the cancellation in A", size=30, color=BLUE_C).move_to(
                DOWN * 1.4
            ),
            run_time=1,
        )

        self.section("domain", "In A: cancel a nonzero factor in the original domain")
        polynomial = formula(
            r"\alpha^r-1=(\alpha-1)\sum_{j=0}^{r-1}\alpha^j", size=52
        ).move_to(UP * 1.1)
        self.show(polynomial, run_time=1.2)
        self.at("domain_power")
        self.play(
            Transform(
                polynomial,
                formula(r"0=(\alpha-1)\sum_{j=0}^{r-1}\alpha^j", size=52).move_to(
                    polynomial
                ),
            ),
            run_time=1,
        )
        self.at("domain_nonzero")
        self.show(
            formula(r"\alpha-1\ne0", size=46, color=BLUE_C).move_to(
                LEFT * 3.8 + DOWN * 0.65
            ),
            words("A has no zero divisors", size=29).move_to(RIGHT * 3.2 + DOWN * 0.65),
            run_time=0.9,
        )
        self.at("domain_sumzero")
        sum_zero = formula(
            r"\sum_{j=0}^{r-1}\alpha^j=0", size=57, color=YELLOW
        ).move_to(DOWN * 2.15)
        self.copy_to(polynomial, sum_zero, run_time=1)
        self.at("domain_before")
        self.show(
            words(
                "Exact cancellation before the ring map", size=28, color=BLUE_C
            ).move_to(DOWN * 3.5),
            run_time=0.8,
        )

        self.section("reduction", "Now reduce the exact vanishing sum")
        original = formula(
            r"\sum_{j=0}^{r-1}\alpha^j=0\quad\text{in }A", size=46, color=BLUE_C
        ).move_to(UP * 1.8)
        self.show(original, run_time=1)
        self.at("reduction_each")
        each_one = formula(
            r"[\alpha]=1\quad\Longrightarrow\quad[\alpha^j]=1", size=40
        ).move_to(UP * 0.5)
        self.show(each_one, run_time=0.9)
        self.at("reduction_odd")
        r_odd = formula(r"r=2k+1", size=46, color=BLUE_C).move_to(
            LEFT * 4.8 + DOWN * 1.1
        )
        reduced = formula(r"0=\sum_{j=0}^{r-1}1", size=49, color=YELLOW).move_to(
            RIGHT * 2 + DOWN * 1.1
        )
        self.show(r_odd, run_time=0.7)
        self.copy_to(original, reduced, run_time=0.8)
        self.at("reduction_pairs")
        paired = formula(r"0=k(1+1)+1", size=49, color=YELLOW).move_to(reduced)
        self.play(Transform(reduced, paired), run_time=1)
        self.show(
            words("k pairs vanish; one term remains", size=27).move_to(DOWN * 2.5),
            run_time=0.7,
        )
        self.at("reduction_contradiction")
        self.play(
            Transform(reduced, formula(r"0=1", size=62, color=YELLOW).move_to(reduced)),
            run_time=0.9,
        )
        self.show(
            words("Contradiction: the target ring is nonzero", size=28).move_to(
                DOWN * 3.5
            ),
            run_time=0.8,
        )
        self.at("reduction_alphaone")
        self.erase(*list(self.body))
        self.show(
            formula(r"\boxed{\alpha=1}", size=65, color=YELLOW).move_to(UP * 0.6),
            run_time=1,
        )
        self.at("reduction_target")
        self.show(
            words("The target ring need not be a domain", size=31).move_to(DOWN * 1.1),
            words("All cancellation occurred in A", size=29, color=BLUE_C).move_to(
                DOWN * 2.5
            ),
            run_time=0.9,
        )

        self.section(
            "application", "Apply the two inputs to each comparison separately"
        )
        comparisons = VGroup(
            formula(r"R=\frac{\Delta(d)}{\Delta(c)}", size=49, color=BLUE_C).move_to(
                LEFT * 4.1 + UP * 1.75
            ),
            formula(r"W=\frac{\Delta(g)}{\Delta(c)}", size=49, color=BLUE_C).move_to(
                RIGHT * 4.1 + UP * 1.75
            ),
        )
        self.show(comparisons, run_time=1)
        self.at("application_membership")
        self.show(
            formula(r"R,W\in A^\times", size=43).move_to(UP * 0.35),
            run_time=0.9,
        )
        self.at("application_odd")
        odd = words("6.1: odd order", size=31, color=BLUE_C).move_to(
            LEFT * 4.2 + DOWN * 0.9
        )
        self.show(odd, run_time=0.8)
        self.at("application_residue")
        residue = words("6.3: residue 1", size=31, color=BLUE_C).move_to(
            RIGHT * 4.2 + DOWN * 0.9
        )
        self.show(
            residue,
            formula(
                r"A/(1+i)A\ne0,\qquad\operatorname{char}(A/(1+i)A)=2", size=32
            ).move_to(DOWN * 2.15),
            run_time=1,
        )
        self.at("application_exact")
        self.erase(*list(self.body))
        inputs = VGroup(
            words("Odd order", size=32).move_to(LEFT * 4.3 + UP * 1.6),
            words("Residue 1", size=32).move_to(RIGHT * 4.3 + UP * 1.6),
        )
        lemma = words("Odd-order rigidity", size=34, color=BLUE_C).move_to(UP * 0.2)
        self.show(
            inputs,
            lemma,
            Arrow(inputs[0].get_bottom(), lemma.get_left(), buff=0.25).set_color(
                BLUE_C
            ),
            Arrow(inputs[1].get_bottom(), lemma.get_right(), buff=0.25).set_color(
                BLUE_C
            ),
            run_time=0.9,
        )
        result = formula(r"\boxed{R=1,\qquad W=1}", size=58, color=YELLOW).move_to(
            DOWN * 1.5
        )
        self.copy_to(lemma, result, run_time=0.9)
        self.at("application_arithmetic")
        self.show(
            words("Exact arithmetic equality", size=29, color=BLUE_C).move_to(
                DOWN * 2.65
            ),
            run_time=0.8,
        )
        self.at("application_points")
        self.show(
            words("The original evaluation points remain distinct", size=28).move_to(
                DOWN * 3.5
            ),
            run_time=0.8,
        )
