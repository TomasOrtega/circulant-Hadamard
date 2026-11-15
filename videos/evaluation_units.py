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
    Rectangle,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class EvaluationUnits(NodeScene):
    node_id = "evaluation-units"
    title = "6.2 · Why We Can Divide"

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
            (ROOT / "videos/production/evaluation-units.json").read_text()
        )["detail_cues"]

        self.section("ring", "Put every evaluation in one ring")
        self.show(
            formula(
                r"u>1\text{ odd},\qquad I=\{p\text{ prime}:p\mid u\}", size=39
            ).move_to(UP * 2.05),
            run_time=1,
        )
        self.at("ring_roots")
        roots_note = words("Use the chosen roots from Node 4", size=26, color=BLUE_C)
        roots_note.move_to(UP * 1.05)
        self.show(
            roots_note,
            run_time=0.8,
        )
        self.at("ring_b")
        outline = Rectangle(width=13, height=1.2).set_stroke(BLUE_C, 2)
        outline.move_to(DOWN * 0.35)
        ring = formula(r"B=\mathbb Z[i,\{\zeta_p:p\in I\}]", size=46, color=BLUE_C)
        ring.move_to(outline)
        self.show(outline, ring, run_time=1.2)
        self.at("ring_a")
        self.erase(roots_note)
        larger = Rectangle(width=14, height=3.45).set_stroke(BLUE_C, 2)
        larger.move_to(DOWN * 0.55)
        self.play(
            Transform(outline, larger),
            Transform(
                ring,
                formula(r"A=B[1/u]", size=49, color=BLUE_C).move_to(UP * 0.35),
            ),
            run_time=1.2,
        )
        denominator_card = formula(r"\frac1u", size=49, color=YELLOW).move_to(
            RIGHT * 5.5 + DOWN * 0.7
        )
        self.show(
            denominator_card,
            words("Powers of u are allowed denominators", size=27).move_to(DOWN * 1.7),
            run_time=0.9,
        )
        self.at("ring_subset")
        self.show(
            formula(
                r"\zeta_S=\prod_{p\in S}\zeta_p,\qquad\zeta_\varnothing=1", size=39
            ).move_to(DOWN * 3.1),
            run_time=1,
        )
        self.at("ring_values")
        self.erase(denominator_card)
        values = VGroup(
            *(
                formula(tex, size=36).move_to(RIGHT * x + DOWN * 0.7)
                for tex, x in zip(
                    [r"c_S=c(\zeta_S)", r"d_S=d(\zeta_S)", r"g_S=g(\zeta_S)"],
                    [-4.5, 0, 4.5],
                    strict=True,
                )
            )
        )
        self.show(values, run_time=1.1)

        self.section("inverse", "The norm gives an inverse inside A")
        norm = formula(r"x_S\overline{x_S}=u^2", size=55, color=BLUE_C).move_to(
            UP * 1.75
        )
        self.show(
            norm,
            formula(r"x_S\in\{c_S,d_S,g_S\}", size=37).move_to(UP * 0.6),
            run_time=1,
        )
        self.at("inverse_conjugate")
        closure = formula(
            r"\overline{\zeta_p}=\zeta_p^{-1}\in B,\qquad\overline i=-i\in B", size=36
        ).move_to(DOWN * 0.65)
        self.show(closure, run_time=1)
        self.at("inverse_divide")
        inverse = formula(
            r"x_S^{-1}=\frac{\overline{x_S}}{u^2}\in A", size=48, color=YELLOW
        )
        inverse.move_to(DOWN * 2.1)
        self.copy_to(norm, inverse, run_time=1.1)
        self.at("inverse_product")
        self.erase(closure)
        product = formula(
            r"x_S\cdot\frac{\overline{x_S}}{u^2}=\frac{u^2}{u^2}=1", size=43
        ).move_to(DOWN * 0.65)
        self.copy_to(norm, product, run_time=1)
        self.at("inverse_inside")
        self.show(
            SurroundingRectangle(inverse, buff=0.22).set_stroke(YELLOW, 2),
            words("An inverse in A, with its location proved", size=27).move_to(
                DOWN * 3.45
            ),
            run_time=0.9,
        )

        self.section("example", "The same inverse when u = 3")
        self.show(
            formula(
                r"A=\mathbb Z[i,\omega,1/3],\qquad\omega=e^{2\pi i/3}",
                size=44,
                color=BLUE_C,
            ).move_to(UP * 1.6),
            run_time=1,
        )
        self.at("example_inverse")
        inverse = formula(
            r"c(\omega)^{-1}=\frac{\overline{c(\omega)}}9", size=57, color=YELLOW
        )
        inverse.move_to(DOWN * 0.2)
        self.show(inverse, run_time=1.2)
        self.at("example_all")
        self.show(
            formula(
                r"x_S^{-1}=\overline{x_S}/9\qquad(x_S=c_S,d_S,g_S)", size=39
            ).move_to(DOWN * 2.05),
            words("Every subset · every evaluated polynomial", size=28).move_to(
                DOWN * 3.4
            ),
            run_time=1,
        )

        self.section(
            "finite_free", "First show that reduction does not collapse the ring"
        )
        self.show(
            formula(r"A/(1+i)A", size=49, color=BLUE_C).move_to(UP * 1.85),
            run_time=0.9,
        )
        self.at("finite_two")
        self.show(
            formula(
                r"2=(1+i)(1-i)\quad\Longrightarrow\quad2=0\text{ in the quotient}",
                size=37,
            ).move_to(UP * 0.55),
            words("We still need 1 ≠ 0", size=28, color=YELLOW).move_to(DOWN * 0.6),
            run_time=1,
        )
        self.at("finite_generators")
        self.erase(*list(self.body))
        self.show(
            words(
                "Root orders bound the monomial exponents", size=30, color=BLUE_C
            ).move_to(UP * 1.95),
            formula(
                r"i^a\prod_{p\in I}\zeta_p^{b_p},\qquad0\le a<4,\quad0\le b_p<p",
                size=40,
            ).move_to(UP * 0.55),
            run_time=1.2,
        )
        self.at("finite_span")
        self.show(
            words("Finitely many monomials span B over the integers", size=28).move_to(
                DOWN * 0.75
            ),
            run_time=0.9,
        )
        self.at("finite_torsion")
        self.show(
            formula(
                r"B\subset\mathbb C\quad\Longrightarrow\quad "
                r"B\text{ has no additive torsion}",
                size=34,
            ).move_to(DOWN * 2),
            run_time=1,
        )
        self.at("finite_free")
        self.erase(*list(self.body))
        self.show(
            formula(
                r"B\cong\mathbb Z^r\text{ additively},\qquad r\ge1",
                size=44,
                color=BLUE_C,
            ).move_to(UP * 1.25),
            run_time=1,
        )
        self.at("finite_modtwo")
        quotient = formula(
            r"B/2B\cong(\mathbb Z/2\mathbb Z)^r\ne0\text{ additively}",
            size=42,
            color=YELLOW,
        ).move_to(DOWN * 0.5)
        self.show(
            quotient,
            words("Finite rank and torsion-free are both needed", size=27).move_to(
                DOWN * 2.4
            ),
            run_time=1,
        )

        self.section(
            "residue_field", "Use a nonzero residue field to witness noncollapse"
        )
        self.show(
            formula(
                r"2\in\mathfrak m\in\operatorname{Max}(B),\qquad k=B/\mathfrak m",
                size=43,
            ).move_to(UP * 1.85),
            words(
                "k is a nonzero field of characteristic 2", size=29, color=BLUE_C
            ).move_to(UP * 0.65),
            run_time=1.1,
        )
        self.at("field_square")
        squared = formula(r"(1+i)^2=2i=0\text{ in }k", size=48, color=YELLOW).move_to(
            DOWN * 0.7
        )
        self.show(squared, run_time=1)
        self.at("field_no_squarezero")
        self.show(
            words("In a field, y² = 0 forces y = 0", size=30).move_to(DOWN * 1.9),
            run_time=0.9,
        )
        self.at("field_pi_zero")
        self.play(
            Transform(
                squared,
                formula(r"1+i=0\text{ in }k", size=49, color=YELLOW).move_to(squared),
            ),
            run_time=0.9,
        )
        self.at("field_u_one")
        self.show(
            formula(
                r"u\text{ odd}\quad\Longrightarrow\quad u=1\text{ in }k",
                size=40,
                color=BLUE_C,
            ).move_to(DOWN * 3.25),
            run_time=1,
        )

        self.section("nonzero_quotient", "Extend the same map after inverting u")
        b = formula("B", size=58, color=BLUE_C).move_to(LEFT * 4.7 + UP * 1.4)
        a = formula(r"A=B[1/u]", size=47, color=BLUE_C).move_to(RIGHT * 3.8 + UP * 1.4)
        k = formula(r"k\ne0", size=56, color=YELLOW).move_to(DOWN * 1.1)
        self.show(b, a, k, run_time=1)
        self.show(
            Arrow(b.get_right(), a.get_left(), buff=0.35).set_color(BLUE_C),
            Arrow(b.get_bottom(), k.get_left(), buff=0.3).set_color(BLUE_C),
            run_time=0.9,
        )
        self.at("extend_inverse")
        self.show(
            Arrow(a.get_bottom(), k.get_right(), buff=0.3).set_color(YELLOW),
            formula(r"u\mapsto1,\qquad1/u\mapsto1", size=34).move_to(
                RIGHT * 4.1 + DOWN * 0.15
            ),
            run_time=1,
        )
        self.at("extend_kills")
        self.show(
            formula(r"1+i\mapsto0", size=37, color=YELLOW).move_to(
                LEFT * 4.3 + DOWN * 0.2
            ),
            run_time=0.8,
        )
        self.at("extend_factors")
        self.erase(*list(self.body))
        quotient_map = formula(
            r"A/(1+i)A\ \longrightarrow\ k\ne0", size=48, color=BLUE_C
        )
        quotient_map.move_to(UP * 1.2)
        self.show(quotient_map, run_time=1)
        self.at("extend_one")
        self.show(
            formula(r"1\longmapsto1\ne0", size=49, color=YELLOW).move_to(DOWN * 0.35),
            run_time=0.9,
        )
        self.at("extend_conclude")
        self.show(
            formula(r"\boxed{A/(1+i)A\ne0}", size=44, color=YELLOW).move_to(
                DOWN * 1.65
            ),
            formula(r"\operatorname{char}(A/(1+i)A)=2", size=36).move_to(DOWN * 2.65),
            words("No field assumption is needed", size=27).move_to(DOWN * 3.5),
            run_time=1,
        )

        self.section("survive", "A ring map preserves the inverse identity")
        identity = formula(
            r"x_Sx_S^{-1}=1\quad\text{in }A", size=50, color=BLUE_C
        ).move_to(UP * 1.75)
        self.show(identity, run_time=1)
        self.at("survive_product")
        reduced = formula(r"[x_S][x_S^{-1}]=1", size=49, color=YELLOW).move_to(UP * 0.2)
        self.copy_to(identity, reduced, run_time=1)
        self.at("survive_units")
        self.show(
            SurroundingRectangle(reduced, buff=0.22).set_stroke(YELLOW, 2),
            words("All evaluated denominators remain units", size=29).move_to(
                DOWN * 1.2
            ),
            formula(r"\text{In }A/(1+i)A", size=36, color=BLUE_C).move_to(DOWN * 2.45),
            run_time=0.9,
        )
        self.at("survive_c")
        self.erase(*list(self.body))
        self.show(
            formula(r"A/(1+i)A", size=43, color=BLUE_C).move_to(UP * 2.05),
            formula(r"[c_S]\text{ is a unit}", size=43, color=BLUE_C).move_to(
                LEFT * 4 + UP * 0.9
            ),
            words("Can divide", size=29, color=BLUE_C).move_to(LEFT * 4 + DOWN * 0.3),
            run_time=0.9,
        )
        self.at("survive_zero")
        self.show(
            formula(r"2=0,\qquad1+i=0", size=40, color=YELLOW).move_to(
                RIGHT * 3.3 + UP * 0.9
            ),
            words("No division by zero residues", size=27).move_to(
                RIGHT * 3.3 + DOWN * 0.3
            ),
            run_time=1,
        )
        self.at("survive_order")
        self.show(
            words(
                "Exact integral quotients first → reduce coefficients second", size=28
            ).move_to(DOWN * 2),
            formula(
                r"\operatorname{char}(A/(1+i)A)=2,\qquad1\ne0", size=37, color=BLUE_C
            ).move_to(DOWN * 3.35),
            run_time=1,
        )
