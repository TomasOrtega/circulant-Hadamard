import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    Arrow,
    Circle,
    FadeOut,
    FlashAround,
    Rectangle,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class LocalCharacterComparison(NodeScene):
    node_id = "local-character-comparison"
    title = "4.3 · Compare two evaluations at a prime"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def copy_to(self, source, target, run_time=0.9):
        self.body.add(target)
        self.play(TransformFromCopy(source, target), run_time=run_time)

    def erase(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.45)
        self.body.remove(*objects)

    def ratio_pair(self, y=0.1):
        return VGroup(
            formula(r"r_F=\frac{F(\rho)}{F(1)}", size=47, color=BLUE_C).move_to(
                LEFT * 3.4 + UP * y
            ),
            formula(r"r_K=\frac{K(\rho)}{K(1)}", size=47, color=BLUE_C).move_to(
                RIGHT * 3.4 + UP * y
            ),
        )

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/local-character-comparison.json").read_text()
        )["detail_cues"]

        self.section("local_ring", "The coefficient ring and the supplied input")
        ring = formula(r"\mathbb Z[\eta]", size=56, color=BLUE_C).move_to(
            LEFT * 3.8 + UP * 0.9
        )
        local = formula(
            r"A=\mathbb Z[\eta]_{\mathfrak p}", size=51, color=BLUE_C
        ).move_to(RIGHT * 3.3 + UP * 0.9)
        self.show(
            ring,
            formula(r"(\operatorname{ord}(\eta),p)=1", size=38).move_to(
                LEFT * 3.8 + DOWN * 0.4
            ),
            run_time=0.9,
        )
        self.at("ring_localize")
        self.show(
            Arrow(ring.get_right(), local.get_left(), buff=0.25).set_color(BLUE_C),
            local,
            words("Localize at the chosen prime", size=25).move_to(
                RIGHT * 3.3 + DOWN * 0.4
            ),
            run_time=1,
        )
        self.at("ring_input")
        self.show(
            words(
                "Supplied cyclotomic facts · Lemma 2.1", size=28, color=YELLOW
            ).move_to(DOWN * 1.7),
            run_time=0.8,
        )
        self.at("ring_valuation")
        self.show(
            formula(
                r"v(p)=1,\qquad v(A\setminus\{0\})=\mathbb Z_{\ge0}", size=40
            ).move_to(DOWN * 2.8),
            words("A is unramified at p", size=27, color=BLUE_C).move_to(UP * 2.1),
            run_time=1,
        )

        self.section("goal", "Matching exponents; two ratios to control")
        cycle = (
            Circle(radius=0.85).move_to(LEFT * 4.5 + UP * 1.25).set_stroke(BLUE_C, 2)
        )
        cycle_label = formula("p^e", size=49, color=YELLOW).move_to(cycle)
        self.show(
            cycle,
            cycle_label,
            words("cycle length", size=23).next_to(cycle, DOWN, buff=0.2),
            formula(r"F(X)K(X)=p^e b", size=54).move_to(RIGHT * 1.8 + UP * 1.3),
            formula(r"e\ge1,\quad b\in A^\times", size=35, color=BLUE_C).move_to(
                RIGHT * 1.8 + UP * 0.2
            ),
            run_time=1,
        )
        ratios = self.ratio_pair(y=-1.15)
        self.at("goal_ratios")
        self.show(ratios, run_time=1)
        warning = words(
            "Nonzero denominators; their residues may be zero", size=26
        ).move_to(DOWN * 2.5)
        self.at("goal_denominators")
        self.show(warning, run_time=0.8)
        self.at("goal_unsafe")
        self.play(
            Transform(
                warning,
                words(
                    "ρ ≡ 1 does not justify division of zero residues",
                    size=27,
                    color=YELLOW,
                ).move_to(warning),
            ),
            run_time=0.9,
        )

        self.section("base_case", "At exponent one, one denominator is a unit")
        self.show(
            formula(
                r"A[\rho]:\quad\mathfrak m=(\rho-1)", size=43, color=BLUE_C
            ).move_to(UP * 2.1),
            words("Unit ⇔ nonzero residue", size=28).move_to(UP * 1.15),
            run_time=1,
        )
        boxes = VGroup(
            Rectangle(width=3.5, height=1.2).move_to(LEFT * 3.3 + DOWN * 0.25),
            Rectangle(width=3.5, height=1.2).move_to(RIGHT * 3.3 + DOWN * 0.25),
        ).set_stroke(BLUE_C, 2)
        value_labels = VGroup(
            formula("F(1)", size=34).next_to(boxes[0], UP, buff=0.18),
            formula("K(1)", size=34).next_to(boxes[1], UP, buff=0.18),
        )
        token = formula("p", size=51, color=YELLOW).move_to(boxes[1])
        valuation_sum = formula(r"v(F(1))+v(K(1))=1", size=42).move_to(DOWN * 1.5)
        self.at("base_integer")
        self.show(
            boxes,
            value_labels,
            token,
            valuation_sum,
            run_time=1,
        )
        self.play(token.animate.move_to(boxes[0]), run_time=0.7)
        self.play(token.animate.move_to(boxes[1]), run_time=0.7)
        self.at("base_unit")
        unit = words("unit", size=30, color=YELLOW).move_to(boxes[0])
        self.show(unit, run_time=0.7)
        self.at("base_safe")
        self.erase(boxes, value_labels, token, unit, valuation_sum)
        self.show(
            formula(
                r"r_F=\frac{F(\rho)}{F(1)}\equiv1\pmod{\rho-1}", size=45, color=YELLOW
            ).move_to(DOWN * 0.25),
            run_time=1,
        )
        self.at("base_product")
        self.show(
            formula(r"r_F r_K=\frac{pb}{pb}=1", size=44).move_to(DOWN * 1.65),
            run_time=0.9,
        )
        self.at("base_inverse")
        self.show(
            formula(
                r"r_K=r_F^{-1}\in A[\rho]^\times,\qquad r_K\equiv1",
                size=40,
                color=BLUE_C,
            ).move_to(DOWN * 2.85),
            run_time=1,
        )

        self.section("choose_factor", "Extended valuations may be fractional")
        self.show(
            formula(
                r"e\ge2,\qquad \xi\text{ primitive of order }p^e", size=39, color=BLUE_C
            ).move_to(UP * 2.05),
            run_time=0.9,
        )
        alpha = formula(r"\alpha=v(F(\xi))\ge0", size=43).move_to(LEFT * 3.3 + UP * 0.7)
        beta = formula(r"\beta=v(K(\xi))\ge0", size=43).move_to(RIGHT * 3.3 + UP * 0.7)
        self.at("choose_sum")
        self.show(alpha, beta, run_time=0.9)
        self.show(
            formula(r"\alpha+\beta=e\ge2", size=51, color=BLUE_C).move_to(DOWN * 0.6),
            run_time=0.8,
        )
        self.at("choose_fractional")
        bound = formula(
            r"\alpha<1,\ \beta<1\quad\Longrightarrow\quad\alpha+\beta<2", size=39
        ).move_to(DOWN * 1.9)
        self.show(bound, run_time=1)
        self.at("choose_relabel")
        self.play(
            Transform(
                bound,
                formula(
                    r"\text{Relabel:}\qquad v(F(\xi))\ge1", size=46, color=YELLOW
                ).move_to(bound),
            ),
            run_time=1,
        )
        self.play(FlashAround(alpha, color=YELLOW), run_time=0.8)

        self.section(
            "remainder_input", "The supplied basis fact transfers divisibility"
        )
        division = formula(r"F=Q\Phi_{p^e}+R", size=53, color=BLUE_C).move_to(UP * 1.6)
        degree = formula(r"\deg R<D=(p-1)p^{e-1}", size=39).move_to(UP * 0.5)
        self.show(
            division,
            degree,
            run_time=1,
        )
        self.at("remainder_evaluate")
        evaluated = formula(
            r"F(\xi)=R(\xi),\qquad v(R(\xi))\ge1", size=44, color=YELLOW
        ).move_to(DOWN * 0.7)
        self.copy_to(division, evaluated)
        self.at("remainder_basis")
        self.erase(division, degree, evaluated)
        basis = formula(
            r"1,\ \xi,\ \ldots,\ \xi^{D-1}\quad\text{is an }A\text{-basis}", size=40
        ).move_to(UP * 1.6)
        self.show(
            basis,
            formula(r"A[\xi]:\quad\mathfrak m=(\xi-1)", size=36, color=BLUE_C).move_to(
                UP * 0.5
            ),
            run_time=1,
        )
        coefficients = VGroup(
            *(
                formula(tex, size=41).move_to(RIGHT * x + DOWN * 0.7)
                for tex, x in zip(
                    ["r_0", "r_1", r"\cdots", "r_{D-1}"],
                    [-4.4, -1.5, 1.5, 4.4],
                    strict=True,
                )
            )
        )
        self.show(coefficients, run_time=0.9)
        self.at("remainder_divisible")
        self.play(
            *(
                Transform(obj, formula(tex, size=41, color=YELLOW).move_to(obj))
                for obj, tex in zip(
                    coefficients, ["pa_0", "pa_1", r"\cdots", "pa_{D-1}"], strict=True
                )
            ),
            run_time=1.1,
        )
        self.show(
            words("Supplied Lemma 2.1 input ⇒ R = pR₀", size=28, color=YELLOW).move_to(
                DOWN * 1.9
            ),
            run_time=0.9,
        )
        self.at("remainder_arithmetic")
        self.show(
            words(
                "Arithmetic divisibility, independent of complex magnitude", size=25
            ).move_to(DOWN * 3),
            run_time=0.8,
        )

        self.section("project_divide", "Fold first, then divide exactly one factor")
        self.show(
            formula(r"q:\quad X^{p^{e-1}}=1", size=43, color=BLUE_C).move_to(UP * 2.1),
            run_time=0.9,
        )
        phi = formula(
            r"\Phi_{p^e}=1+X^{p^{e-1}}+\cdots+X^{(p-1)p^{e-1}}", size=38
        ).move_to(UP * 0.85)
        self.show(phi, run_time=1)
        self.at("project_terms")
        self.play(
            Transform(
                phi,
                formula(
                    r"q(\Phi_{p^e})=\underbrace{1+1+\cdots+1}_{p\ \mathrm{terms}}=p",
                    size=42,
                    color=YELLOW,
                ).move_to(phi),
            ),
            run_time=1.1,
        )
        projected = formula(r"q(F)=p\,q(Q)+p\,q(R_0)", size=45, color=BLUE_C).move_to(
            DOWN * 0.6
        )
        self.at("project_divisible")
        self.show(projected, run_time=1)
        self.at("project_define")
        self.play(
            Transform(
                projected,
                formula(r"F'=q(F)/p,\qquad K'=q(K)", size=46, color=YELLOW).move_to(
                    projected
                ),
            ),
            run_time=1,
        )
        self.at("project_product")
        self.show(
            formula(
                r"F'K'=p^{e-1}b\quad\text{on a cycle of length }p^{e-1}", size=38
            ).move_to(DOWN * 1.85),
            run_time=1,
        )
        self.at("project_exact")
        self.show(
            words(
                "Cancel scalar p in the free A-module; reduce residues later",
                size=26,
                color=YELLOW,
            ).move_to(DOWN * 3),
            run_time=0.9,
        )

        self.section("ratios", "Both evaluations survive projection")
        self.show(
            formula(
                r"1^{p^{e-1}}=\rho^{p^{e-1}}=1\qquad(e\ge2)", size=41, color=BLUE_C
            ).move_to(UP * 2.1),
            run_time=0.9,
        )
        self.at("ratios_projection")
        self.show(
            formula(r"q(F)(1)=F(1),\qquad q(F)(\rho)=F(\rho)", size=40).move_to(
                UP * 0.95
            ),
            run_time=1,
        )
        ratio = formula(
            r"\frac{F'(\rho)}{F'(1)}=\frac{F(\rho)/p}{F(1)/p}", size=49, color=BLUE_C
        ).move_to(DOWN * 0.6)
        self.at("ratios_cancel")
        self.show(ratio, run_time=1)
        self.play(
            Transform(
                ratio,
                formula(
                    r"\frac{F'(\rho)}{F'(1)}=\frac{F(\rho)}{F(1)}=r_F",
                    size=49,
                    color=YELLOW,
                ).move_to(ratio),
            ),
            run_time=1.1,
        )
        self.at("ratios_k")
        self.show(
            formula(
                r"\frac{K'(\rho)}{K'(1)}=\frac{K(\rho)}{K(1)}=r_K",
                size=46,
                color=YELLOW,
            ).move_to(DOWN * 2.2),
            run_time=1,
        )

        self.section("induction", "Two exponents descend; both ratios stay fixed")
        ratios = self.ratio_pair(y=1.3)
        self.show(ratios, run_time=1)
        cycle = formula(r"\text{cycle: }p^e", size=42, color=BLUE_C).move_to(
            LEFT * 3.3 + DOWN * 0.15
        )
        scalar = formula(r"\text{scalar: }p^e b", size=42, color=BLUE_C).move_to(
            RIGHT * 3.3 + DOWN * 0.15
        )
        self.show(cycle, scalar, run_time=0.9)
        self.at("induction_descend")
        self.play(
            Transform(
                cycle,
                formula(r"\text{cycle: }p^{e-1}", size=42, color=BLUE_C).move_to(cycle),
            ),
            Transform(
                scalar,
                formula(r"\text{scalar: }p^{e-1}b", size=42, color=BLUE_C).move_to(
                    scalar
                ),
            ),
            run_time=1,
        )
        choice = words("Divide F or K, as its valuation permits", size=28).move_to(
            DOWN * 1.5
        )
        self.at("induction_either")
        self.show(choice, run_time=0.9)
        self.at("induction_stop")
        self.play(
            Transform(
                cycle, formula(r"\text{cycle: }p", size=42, color=BLUE_C).move_to(cycle)
            ),
            Transform(
                scalar,
                formula(r"\text{scalar: }pb", size=42, color=BLUE_C).move_to(scalar),
            ),
            Transform(
                choice,
                words(
                    "Stop at exponent 1 · use the base case", size=28, color=YELLOW
                ).move_to(choice),
            ),
            run_time=1,
        )
        self.at("induction_conclude")
        for ratio in ratios:
            self.show(
                SurroundingRectangle(ratio, buff=0.2).set_stroke(YELLOW, 2),
                run_time=0.45,
            )
        self.show(
            words(
                "Both original ratios are units of residue 1", size=31, color=YELLOW
            ).move_to(DOWN * 2.8),
            run_time=0.9,
        )

        self.section(
            "application", "The norm identity has exactly the required exponents"
        )
        norm = formula(
            r"f(P)f^*(P)=u^2,\qquad u>1\text{ odd}", size=44, color=BLUE_C
        ).move_to(UP * 1.95)
        self.show(norm, run_time=1)
        self.at("application_component")
        self.show(
            formula(r"p\mid u,\qquad e=v_p(u^2)", size=43).move_to(UP * 0.75),
            run_time=0.9,
        )
        component = formula(
            r"\text{remaining cycle: }p^e", size=42, color=YELLOW
        ).move_to(DOWN * 0.5)
        self.show(component, run_time=0.8)
        self.at("application_others")
        self.show(
            words(
                "Evaluate the other components; localize their coefficient ring",
                size=25,
            ).move_to(DOWN * 1.6),
            words("Their root orders are coprime to p", size=25, color=BLUE_C).move_to(
                DOWN * 2.45
            ),
            run_time=1,
        )
        self.at("application_unit")
        self.erase(norm)
        self.show(
            formula(r"b=\frac{u^2}{p^e}\in A^\times", size=47, color=YELLOW).move_to(
                UP * 1.95
            ),
            run_time=1,
        )
        self.at("application_match")
        self.play(
            Transform(
                component,
                formula(
                    r"F K=p^e b\quad\text{on the }p^e\text{ cycle}",
                    size=43,
                    color=YELLOW,
                ).move_to(component),
            ),
            run_time=1,
        )

        self.section("subset_ratio", "Attach the conclusion to the ratio")
        left = formula(r"f(\zeta_S)", size=46, color=BLUE_C).move_to(
            LEFT * 3.6 + UP * 1.1
        )
        right = formula(r"f(\zeta_{S\cup\{p\}})", size=46, color=BLUE_C).move_to(
            RIGHT * 3.6 + UP * 1.1
        )
        self.show(
            left,
            right,
            formula(r"p\notin S", size=35).move_to(UP * 2.2),
            run_time=1,
        )
        quotient = formula(
            r"r=\frac{f(\zeta_{S\cup\{p\}})}{f(\zeta_S)}", size=53, color=YELLOW
        ).move_to(DOWN * 0.7)
        self.copy_to(VGroup(left, right), quotient, run_time=1)
        self.at("subset_unit")
        box = SurroundingRectangle(quotient, buff=0.23).set_stroke(YELLOW, 2)
        self.show(
            box,
            words(
                "Unit, residue 1 at every prime above p", size=29, color=YELLOW
            ).move_to(DOWN * 2.05),
            run_time=1,
        )
        self.at("subset_inverse")
        self.show(
            formula(r"r^{-1}\text{ is also a unit of residue }1", size=37).move_to(
                DOWN * 3.1
            ),
            run_time=0.9,
        )
        self.at("subset_only_ratio")
        self.play(FlashAround(box, color=YELLOW), run_time=0.8)
        self.at("subset_next")
        self.erase(left, right)
        self.show(
            words(
                "Next: remove denominators from the alternating product",
                size=28,
                color=BLUE_C,
            ).move_to(UP * 1.1),
            run_time=1,
        )
