import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    Arrow,
    FadeOut,
    Line,
    Rectangle,
    Transform,
    TransformFromCopy,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class IncompatibleResidues(NodeScene):
    node_id = "incompatible-residues"
    title = "8.4 · The Two Residues Cannot Agree"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def erase(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.4)
        self.body.remove(*objects)

    def copy_to(self, source, target, run_time=1):
        self.body.add(target)
        self.play(TransformFromCopy(source, target), run_time=run_time)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/incompatible-residues.json").read_text()
        )["detail_cues"]

        self.section("setup", "Assume a circulant Hadamard matrix exists")
        self.show(
            formula(r"n=4u^2,\qquad u>1\text{ odd}", size=48, color=BLUE_C).move_to(
                UP * 1.7
            ),
            run_time=1.1,
        )
        self.at("setup_indices")
        self.show(
            words("I: distinct prime divisors of u", size=30).move_to(UP * 0.25),
            run_time=0.9,
        )
        self.at("setup_roots")
        self.show(
            formula(
                r"\zeta_S=\prod_{p\in S}\zeta_p,\qquad\zeta_{\varnothing}=1", size=42
            ).move_to(DOWN * 1.1),
            run_time=1.1,
        )
        self.at("setup_sum")
        self.show(
            formula(
                r"\mathcal S=\sum_{S\subseteq I}(-1)^{|S|}"
                r"\frac{E(\zeta_S)}{c(\zeta_S)}",
                size=51,
                color=YELLOW,
            ).move_to(DOWN * 2.9),
            run_time=1.2,
        )

        self.section("branches", "Two arguments about the same element")
        self.show(
            formula(
                r"\mathcal S=\sum_{S\subseteq I}(-1)^{|S|}"
                r"\frac{E(\zeta_S)}{c(\zeta_S)}",
                size=43,
                color=BLUE_C,
            ).move_to(UP * 1.75),
            run_time=1,
        )
        self.at("branches_product")
        product = formula(r"[\mathcal S]=0", size=49, color=YELLOW).move_to(
            LEFT * 4.5 + DOWN * 0.7
        )
        self.show(
            words("Node 7 · products", size=30).move_to(LEFT * 4.5 + UP * 0.45),
            product,
            run_time=1,
        )
        self.at("branches_ones")
        ones = formula(r"[\mathcal S]=1", size=49, color=YELLOW).move_to(
            RIGHT * 4.5 + DOWN * 0.7
        )
        self.show(
            words("Node 8.3 · all ones", size=30).move_to(RIGHT * 4.5 + UP * 0.45),
            ones,
            run_time=1,
        )
        self.at("branches_same")
        common = formula(r"[\mathcal S]", size=49, color=BLUE_C).move_to(DOWN * 2.3)
        self.show(
            common,
            Arrow(product.get_bottom(), common.get_left(), buff=0.2).set_color(BLUE_C),
            Arrow(ones.get_bottom(), common.get_right(), buff=0.2).set_color(BLUE_C),
            words("One assumed matrix · the same subset inputs", size=28).move_to(
                DOWN * 3.5
            ),
            run_time=1.1,
        )

        self.section("common_ring", "The reductions and denominators share one ring")
        quotient = formula(r"A/(1+i)A", size=56, color=BLUE_C).move_to(UP * 1.8)
        self.show(quotient, run_time=1)
        self.at("ring_definition")
        self.show(
            formula(r"A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]", size=42).move_to(
                UP * 0.3
            ),
            run_time=1,
        )
        self.at("ring_nonzero")
        nonzero = formula(r"A/(1+i)A\ne0", size=45, color=YELLOW).move_to(DOWN * 1.05)
        self.copy_to(quotient, nonzero, run_time=0.9)
        self.at("ring_distinct")
        self.play(
            Transform(
                nonzero,
                formula(
                    r"A/(1+i)A\ne0\quad\Longrightarrow\quad0\ne1", size=42, color=YELLOW
                ).move_to(nonzero),
            ),
            run_time=1,
        )
        self.at("ring_units")
        self.show(
            formula(
                r"c_Sc_S^{-1}=1\quad\longmapsto\quad[c_S][c_S^{-1}]=1",
                size=37,
                color=BLUE_C,
            ).move_to(DOWN * 2.45),
            run_time=1.1,
        )
        self.at("ring_defined")
        self.show(
            words("Every normalized term remains defined", size=29).move_to(DOWN * 3.5),
            run_time=0.9,
        )

        self.section("contradiction", "The assumed matrix would identify zero and one")
        boundary = Rectangle(width=12, height=4.4).set_stroke(BLUE_C, 2)
        boundary.move_to(DOWN * 0.2)
        left_value = formula(r"[\mathcal S]=0", size=50, color=YELLOW).move_to(
            LEFT * 3.2 + UP * 0.3
        )
        right_value = formula(r"[\mathcal S]=1", size=50, color=YELLOW).move_to(
            RIGHT * 3.2 + UP * 0.3
        )
        self.show(
            boundary,
            formula(r"A/(1+i)A", size=40, color=BLUE_C).move_to(UP * 1.55),
            left_value,
            right_value,
            run_time=0.9,
        )
        self.at("contradiction_equal")
        self.erase(left_value, right_value)
        impossible = formula(r"0=1", size=74, color=YELLOW).move_to(UP * 0.3)
        self.show(impossible, run_time=0.9)
        self.at("contradiction_nonzero")
        self.show(
            Line(
                impossible.get_corner(LEFT + DOWN), impossible.get_corner(RIGHT + UP)
            ).set_stroke(YELLOW, 3),
            formula(r"0\ne1\quad\text{in this nonzero ring}", size=38).move_to(
                DOWN * 1.1
            ),
            run_time=0.9,
        )
        self.at("contradiction_char2")
        self.show(
            formula(
                r"\operatorname{char}=2:\qquad1+1=0,\qquad1\ne0", size=35, color=BLUE_C
            ).move_to(DOWN * 3.45),
            run_time=1,
        )
        self.at("contradiction_matrix")
        self.show(
            words("The assumed matrix cannot exist", size=28, color=YELLOW).move_to(
                DOWN * 2
            ),
            run_time=0.9,
        )

        self.section("scope", "Keep the exclusion inside its hypotheses")
        self.show(
            formula(
                r"\boxed{\text{No circulant Hadamard matrix of order }4u^2"
                r",\quad u>1\text{ odd}}",
                size=38,
                color=YELLOW,
                width=14,
            ).move_to(UP * 1.7),
            run_time=1.1,
        )
        self.at("scope_general")
        excluded = formula(r"u=3,5,7,9,\ldots", size=43).move_to(RIGHT * 2 + DOWN * 0.2)
        self.show(
            Rectangle(width=9, height=1.45)
            .set_stroke(BLUE_C, 2)
            .move_to(RIGHT * 2 + DOWN * 0.2),
            excluded,
            Line(
                excluded.get_corner(LEFT + DOWN), excluded.get_corner(RIGHT + UP)
            ).set_stroke(YELLOW, 3),
            run_time=1,
        )
        self.at("scope_one")
        self.show(
            Rectangle(width=3, height=1.45)
            .set_stroke(BLUE_C, 2)
            .move_to(LEFT * 5.5 + DOWN * 0.2),
            formula(r"u=1", size=43, color=BLUE_C).move_to(LEFT * 5.5 + DOWN * 0.2),
            run_time=0.9,
        )
        self.at("scope_delta")
        self.show(
            formula(
                r"\Delta\text{-theorem hypothesis: }u>1", size=39, color=BLUE_C
            ).move_to(DOWN * 1.7),
            words("Its odd-order conclusion does not apply at u = 1", size=28).move_to(
                DOWN * 2.7
            ),
            run_time=1,
        )
        self.at("scope_next")
        self.show(
            words(
                "Next: combine the order restriction and check the remaining orders",
                size=25,
            ).move_to(DOWN * 3.55),
            run_time=0.9,
        )
