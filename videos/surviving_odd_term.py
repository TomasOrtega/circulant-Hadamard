import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    FadeOut,
    FlashAround,
    Rectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class SurvivingOddTerm(NodeScene):
    node_id = "surviving-odd-term"
    title = "8.3 · One Surviving Odd Term"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def erase(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.4)
        self.body.remove(*objects)

    def copy_to(self, source, target, run_time=0.9):
        self.body.add(target)
        self.play(TransformFromCopy(source, target), run_time=run_time)

    def subset_sum(self, numerator, size=45):
        return formula(
            rf"\mathcal S\equiv\sum_{{S\subseteq I}}(-1)^{{|S|}}"
            rf"\frac{{{numerator}(\zeta_S)}}{{c(\zeta_S)}}\pmod{{1+i}}",
            size=size,
            width=14.6,
        )

    def example_card(self, subset, order, term, x):
        outline = Rectangle(width=3.35, height=2.6).set_stroke(BLUE_C, 2)
        contents = VGroup(
            formula(subset, size=31, color=BLUE_C).move_to(UP * 0.8),
            words(f"Order {order}", size=23).move_to(UP * 0.2),
            formula(term, size=35, color=YELLOW, width=3.0).move_to(DOWN * 0.65),
        )
        return VGroup(outline, contents).move_to(RIGHT * x + DOWN * 0.25)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/surviving-odd-term.json").read_text()
        )["detail_cues"]
        self.section("sum", "Evaluate the residue of the full subset sum")
        self.show(
            formula(
                r"u>1\text{ odd},\qquad I=\{p\text{ prime}:p\mid u\}",
                size=37,
                color=BLUE_C,
            ).move_to(UP * 1.9),
            run_time=1,
        )
        self.at("indices")
        roots = formula(r"\zeta_S=\prod_{p\in S}\zeta_p", size=43).move_to(UP * 0.65)
        self.show(roots, run_time=0.8)
        self.at("empty")
        self.show(
            formula(r"\zeta_{\varnothing}=1", size=39).move_to(RIGHT * 4.8 + UP * 0.65),
            run_time=0.8,
        )
        self.at("sum_definition")
        self.show(
            formula(
                r"\mathcal S=\sum_{S\subseteq I}(-1)^{|S|}"
                r"\frac{E(\zeta_S)}{c(\zeta_S)}",
                size=49,
            ).move_to(DOWN * 1.1),
            run_time=1.1,
        )
        self.at("ring")
        self.show(
            formula(
                r"A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]", size=36, color=BLUE_C
            ).move_to(DOWN * 2.9),
            run_time=0.9,
        )

        self.section("coefficient", "Use the coefficientwise congruence from Node 5")
        congruence = formula(
            r"E(P)\equiv J(P)\pmod{1+i}", size=48, color=BLUE_C
        ).move_to(UP * 1.5)
        self.show(congruence, run_time=1)
        self.at("all_powers")
        j = formula(r"J(P)=1+P+\cdots+P^{u^2-1}", size=43).move_to(DOWN * 0.1)
        self.show(j, run_time=0.9)
        self.at("evaluation")
        evaluated = formula(
            r"E(\zeta_S)\equiv J(\zeta_S)\pmod{1+i}", size=44, color=YELLOW
        ).move_to(DOWN * 1.8)
        self.copy_to(congruence, evaluated)
        self.at("preserve")
        self.show(
            words("Retain each subset sign and denominator", size=28).move_to(
                DOWN * 3.2
            ),
            run_time=0.8,
        )

        self.section("units", "Unit inverses preserve the normalized congruences")
        self.show(
            formula(r"c_S=c(\zeta_S)\in A^{\times}", size=43, color=BLUE_C).move_to(
                UP * 1.8
            ),
            run_time=0.9,
        )
        self.at("inverse")
        inverse = formula(r"c_S^{-1}=\frac{\overline{c_S}}{u^2}\in A", size=46).move_to(
            UP * 0.35
        )
        self.show(inverse, run_time=0.9)
        self.at("exact_unit")
        identity = formula(r"c_Sc_S^{-1}=1\quad\text{in }A", size=45).move_to(
            DOWN * 1.2
        )
        self.show(identity, run_time=0.8)
        self.at("reduce_unit")
        self.play(
            Transform(
                identity,
                formula(r"\pi(c_S)\pi(c_S^{-1})=1", size=43, color=YELLOW).move_to(
                    identity
                ),
            ),
            run_time=0.9,
        )
        self.show(
            formula(r"\pi:A\longrightarrow A/(1+i)A", size=34, color=BLUE_C).move_to(
                DOWN * 2.65
            ),
            run_time=0.7,
        )
        self.at("remains_unit")
        self.play(FlashAround(identity, color=YELLOW), run_time=0.8)
        self.at("multiply_congruence")
        self.erase(*list(self.body))
        multiplication = formula(
            r"\pi(E(\zeta_S))\pi(c_S^{-1})=\pi(J(\zeta_S))\pi(c_S^{-1})",
            size=38,
            width=14.5,
        ).move_to(UP * 1.1)
        self.show(multiplication, run_time=1)
        self.at("normalized")
        self.show(
            formula(
                r"\frac{E(\zeta_S)}{c(\zeta_S)}\equiv\frac{J(\zeta_S)}{c(\zeta_S)}\pmod{1+i}",
                size=45,
                color=YELLOW,
            ).move_to(DOWN * 0.55),
            run_time=0.9,
        )
        self.at("all_terms")
        self.show(self.subset_sum("J", size=41).move_to(DOWN * 2.55), run_time=1)

        self.section("nonempty", "Every nonempty-subset numerator is exactly zero")
        zero = formula(
            r"S\ne\varnothing\quad\Longrightarrow\quad J(\zeta_S)=0",
            size=43,
            color=BLUE_C,
        ).move_to(UP * 1.75)
        self.show(zero, run_time=1)
        self.at("whole_zero")
        term = formula(
            r"(-1)^{|S|}\frac{0}{c(\zeta_S)}=0,\qquad c(\zeta_S)\in A^{\times}", size=43
        ).move_to(UP * 0.1)
        self.copy_to(zero, term, run_time=1)
        self.at("remove")
        self.erase(term)
        self.at("only_empty")
        empty = formula(r"S=\varnothing", size=48, color=YELLOW).move_to(UP * 0.1)
        self.show(empty, run_time=0.8)
        self.at("empty_sign")
        self.show(
            formula(r"(-1)^0=+1,\qquad\zeta_{\varnothing}=1", size=39).move_to(
                DOWN * 1.1
            ),
            run_time=0.8,
        )
        self.at("survivor")
        self.show(
            formula(
                r"\mathcal S\equiv\frac{J(1)}{c(1)}\pmod{1+i}", size=49, color=YELLOW
            ).move_to(DOWN * 2.8),
            run_time=1,
        )

        self.section("odd_value", "The empty-subset quotient has residue one")
        self.show(
            formula(r"J(1)=u^2,\qquad c(1)=\pm u", size=46, color=BLUE_C).move_to(
                UP * 1.5
            ),
            run_time=1,
        )
        self.at("odd_quotient")
        value = formula(r"\frac{J(1)}{c(1)}=\frac{u^2}{\pm u}=\pm u", size=51).move_to(
            DOWN * 0.2
        )
        self.show(value, run_time=1)
        self.at("odd_residue")
        self.show(
            formula(
                r"u\text{ odd}\quad\Longrightarrow\quad\pm u\equiv1\pmod{1+i}", size=39
            ).move_to(DOWN * 1.8),
            run_time=1,
        )
        self.at("full_residue")
        self.show(
            formula(
                r"\boxed{\mathcal S\equiv1\pmod{1+i}}", size=48, color=YELLOW
            ).move_to(DOWN * 3.2),
            run_time=0.9,
        )

        self.section("example", "For u = 15, three zero terms leave one contribution")
        self.show(
            formula(r"u=15,\qquad I=\{3,5\}", size=40, color=BLUE_C).move_to(UP * 1.85),
            run_time=0.9,
        )
        self.at("four_subsets")
        cards = [
            self.example_card(r"\varnothing", 1, r"+\frac{225}{c(1)}", -5.55),
            self.example_card(r"\{3\}", 3, r"-\frac{0}{c(\zeta_3)}", -1.85),
            self.example_card(r"\{5\}", 5, r"-\frac{0}{c(\zeta_5)}", 1.85),
            self.example_card(r"\{3,5\}", 15, r"+\frac{0}{c(\zeta_3\zeta_5)}", 5.55),
        ]
        self.show(*cards, run_time=1)
        self.at("orders")
        self.play(
            *(FlashAround(card[1][1], color=BLUE_C) for card in cards), run_time=0.9
        )
        self.at("example_zero")
        self.play(
            *(FlashAround(card[1][2], color=YELLOW) for card in cards[1:]), run_time=0.8
        )
        self.erase(*cards[1:])
        self.at("example_quotient")
        result = formula(r"\frac{225}{\pm15}=\pm15", size=49).move_to(
            RIGHT * 1.5 + DOWN * 0.25
        )
        self.copy_to(cards[0][1][2], result, run_time=0.9)
        self.at("example_residue")
        self.show(
            formula(r"\pm15\equiv1\pmod{1+i}", size=43, color=YELLOW).move_to(
                DOWN * 2.2
            ),
            run_time=0.9,
        )
        self.at("one_survivor")
        self.erase(*list(self.body))
        self.show(
            words(
                "Exactly one term survives for every odd u > 1", size=30, color=BLUE_C
            ).move_to(UP * 1.4),
            run_time=0.9,
        )
        self.at("compare")
        self.show(
            formula(r"\text{Node 7:}\quad\mathcal S\equiv0", size=43).move_to(
                LEFT * 4.0 + DOWN * 0.25
            ),
            formula(
                r"\text{Node 8:}\quad\mathcal S\equiv1", size=43, color=YELLOW
            ).move_to(RIGHT * 4.0 + DOWN * 0.25),
            formula(r"\text{in the same }A/(1+i)A", size=37, color=BLUE_C).move_to(
                DOWN * 2.2
            ),
            words("Next: compare the two residues", size=27).move_to(DOWN * 3.3),
            run_time=1,
        )
