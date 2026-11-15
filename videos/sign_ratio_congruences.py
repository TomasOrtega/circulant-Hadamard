import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    FadeOut,
    Line,
    Rectangle,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class SignRatioCongruences(NodeScene):
    node_id = "sign-ratio-congruences"
    title = "6.3 · The Ratios Have Residue One"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def hide(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.35)
        self.body.remove(*objects)

    def ratio_row(self, letter, factor, numerator, center, reduced=False):
        prefix = rf"\pi({letter}_S)-1=" if reduced else rf"{letter}_S-1="
        quotient = rf"\frac{{{numerator}(\zeta_S)}}{{c_S}}"
        if reduced:
            quotient = rf"\pi({quotient})"
        return (
            VGroup(
                formula(prefix, size=35),
                formula(factor, size=35, color=YELLOW),
                formula(quotient, size=35, color=BLUE_C),
            )
            .arrange(RIGHT, buff=0.25)
            .set_max_width(7.7)
            .move_to(center)
        )

    def product_fraction(self, letter, family, x):
        label = formula(rf"{letter}=", size=41).move_to(RIGHT * (x - 3.5) + DOWN * 0.6)
        numerator = formula(
            rf"\prod_{{\substack{{S\subseteq I\\|S|\text{{ even}}}}}}{family}_S",
            size=42,
            color=BLUE_C,
        ).move_to(RIGHT * x + UP * 0.55)
        denominator = formula(
            rf"\prod_{{\substack{{S\subseteq I\\|S|\text{{ odd}}}}}}{family}_S",
            size=42,
            color=BLUE_C,
        ).move_to(RIGHT * x + DOWN * 1.8)
        bar = Line(LEFT * 2.4, RIGHT * 2.4).set_stroke(width=2)
        bar.move_to(RIGHT * x + DOWN * 0.6)
        return VGroup(label, numerator, denominator, bar)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/sign-ratio-congruences.json").read_text()
        )["detail_cues"]

        self.section("exact", "Evaluate identities already divided exactly in Node 5")
        self.show(
            formula(
                r"u>1\text{ odd},\qquad I=\{p\text{ prime}:p\mid u\}", size=38
            ).move_to(UP * 2.05)
        )
        common = formula(
            r"h_{a,b}\in\{-1,1\}\quad\text{in the same four }H_a(P)", size=35
        )
        common.move_to(DOWN * 2.55)
        self.at("common_signs")
        self.show(common, run_time=0.9)
        real_identity = formula(r"2\mid d(P)-c(P)", size=44).move_to(UP * 0.65)
        gaussian_identity = formula(r"1+i\mid g(P)-c(P)", size=44).move_to(DOWN * 0.85)
        self.show(real_identity, gaussian_identity, run_time=1.0)
        self.at("exact_quotients")
        self.play(
            Transform(
                real_identity,
                formula(r"d(P)-c(P)=2a(P)", size=44).move_to(real_identity),
            ),
            Transform(
                gaussian_identity,
                formula(r"g(P)-c(P)=(1+i)b(P)", size=44).move_to(gaussian_identity),
            ),
            run_time=1.2,
        )
        self.at("quotient_types")
        self.hide(common)
        self.show(
            formula(
                r"a(P)\in\mathbb Z[P]/(P^{u^2}-1),\qquad "
                r"b(P)\in\mathbb Z[i][P]/(P^{u^2}-1)",
                size=32,
                color=BLUE_C,
                width=14.3,
            ).move_to(DOWN * 2.4),
            words("Exact division before reduction", size=28, color=YELLOW).move_to(
                DOWN * 3.4
            ),
            run_time=1.1,
        )
        self.at("one_ring")
        self.hide(*list(self.body))
        self.show(
            formula(
                r"B=\mathbb Z[i,\{\zeta_p:p\in I\}],\qquad A=B[1/u]", size=42
            ).move_to(UP * 1.95)
        )
        self.at("subset_input")
        self.show(
            formula(
                r"\zeta_S=\prod_{p\in S}\zeta_p,\qquad S\subseteq I", size=42
            ).move_to(UP * 0.55),
            formula(
                r"c_S=c(\zeta_S),\quad d_S=d(\zeta_S),\quad g_S=g(\zeta_S)", size=38
            ).move_to(DOWN * 0.85),
        )
        self.at("units_input")
        unit = formula(
            r"c_S,d_S,g_S\in A^{\times}\qquad\text{(Node 6.2)}", size=37, color=BLUE_C
        )
        unit.move_to(DOWN * 2.05)
        self.show(
            unit,
            formula(r"A/(1+i)A\ne0\qquad\text{(Node 6.2)}", size=35).move_to(
                DOWN * 3.15
            ),
            run_time=1.0,
        )
        self.at("explicit_inverse")
        self.hide(*list(self.body))
        unit = formula(
            r"c_S\in A^{\times},\qquad c_S^{-1}=\frac{\overline{c_S}}{u^2}\in A",
            size=41,
            color=BLUE_C,
        )
        unit.move_to(UP * 1.9)
        self.show(unit)
        self.at("evaluate")
        before = VGroup(
            formula(r"d(P)-c(P)=2a(P)", size=31, width=5).move_to(
                LEFT * 4.9 + UP * 0.4
            ),
            formula(r"g(P)-c(P)=(1+i)b(P)", size=31, width=5).move_to(
                LEFT * 4.9 + DOWN * 1.2
            ),
        )
        evaluation_box = Rectangle(width=2.35, height=2.9).set_stroke(BLUE_C, width=2)
        evaluation_box.move_to(DOWN * 0.4)
        evaluation_label = formula(r"P=\zeta_S", size=35, color=YELLOW).move_to(
            evaluation_box
        )
        after = VGroup(
            formula(r"d_S-c_S=2a(\zeta_S)", size=31, width=5).move_to(
                RIGHT * 4.9 + UP * 0.4
            ),
            formula(r"g_S-c_S=(1+i)b(\zeta_S)", size=31, width=5).move_to(
                RIGHT * 4.9 + DOWN * 1.2
            ),
        )
        self.show(before, evaluation_box, evaluation_label, run_time=0.85)
        self.body.add(after)
        self.play(
            *(
                TransformFromCopy(source, target)
                for source, target in zip(before, after, strict=True)
            ),
            run_time=1.3,
        )
        self.show(
            words("Both identities stay exact in A", size=28).move_to(DOWN * 2.7),
            run_time=0.8,
        )

        self.section("ratios", "Divide by a unit, then apply the reduction map")
        unit = formula(r"c_S^{-1}\in A\qquad(A=B[1/u])", size=38, color=BLUE_C).move_to(
            UP * 2.05
        )
        self.show(unit, run_time=0.7)
        left, right = LEFT * 4.1 + UP * 0.5, RIGHT * 4.1 + UP * 0.5
        r = formula(r"r_S=\frac{d_S}{c_S}", size=46).move_to(left)
        w = formula(r"w_S=\frac{g_S}{c_S}", size=46).move_to(right)
        self.show(r, w, run_time=1.1)
        self.at("subtract_one")
        self.play(
            Transform(r, formula(r"r_S-1=\frac{d_S}{c_S}-1", size=40).move_to(left)),
            run_time=0.9,
        )
        self.at("combine_fractions")
        self.play(
            Transform(r, formula(r"r_S-1=\frac{d_S-c_S}{c_S}", size=40).move_to(left)),
            run_time=0.9,
        )
        self.at("substitute_real")
        r_exact = self.ratio_row("r", "2", "a", left)
        self.body.add(r_exact)
        self.play(TransformFromCopy(r, r_exact), FadeOut(r), run_time=1.1)
        self.body.remove(r)
        r = r_exact
        self.at("repeat_gaussian")
        self.play(
            Transform(w, formula(r"w_S-1=\frac{g_S-c_S}{c_S}", size=40).move_to(right)),
            run_time=0.9,
        )
        w_exact = self.ratio_row("w", "(1+i)", "b", right)
        self.body.add(w_exact)
        self.play(TransformFromCopy(w, w_exact), FadeOut(w), run_time=1.1)
        self.body.remove(w)
        w = w_exact
        self.at("quotients_in_ring")
        quotients = VGroup(
            formula(r"\frac{a(\zeta_S)}{c_S}\in A", size=39, color=BLUE_C).move_to(
                LEFT * 4.1 + DOWN * 1.1
            ),
            formula(r"\frac{b(\zeta_S)}{c_S}\in A", size=39, color=BLUE_C).move_to(
                RIGHT * 4.1 + DOWN * 1.1
            ),
        )
        self.body.add(quotients)
        self.play(
            TransformFromCopy(r[2], quotients[0]),
            TransformFromCopy(w[2], quotients[1]),
            run_time=1.1,
        )
        frames = VGroup(
            *(
                SurroundingRectangle(row[1], buff=0.1).set_color(YELLOW)
                for row in [r, w]
            )
        )
        self.show(frames, run_time=0.6)
        self.at("two_factors")
        two_factors = formula(r"2=-i(1+i)^2", size=43, color=YELLOW).move_to(DOWN * 2.7)
        self.show(two_factors, run_time=0.9)
        self.at("reduce_factors")
        self.hide(frames, quotients, two_factors)
        self.play(
            Transform(
                unit,
                formula(
                    r"\pi:A\longrightarrow A/(1+i)A\ne0", size=39, color=BLUE_C
                ).move_to(unit),
            ),
            Transform(r, self.ratio_row("r", "0", "a", left, reduced=True)),
            Transform(w, self.ratio_row("w", "0", "b", right, reduced=True)),
            run_time=1.3,
        )
        self.at("zero_differences")
        self.play(
            Transform(r, formula(r"\pi(r_S)-1=0", size=44).move_to(left)),
            Transform(w, formula(r"\pi(w_S)-1=0", size=44).move_to(right)),
            run_time=0.9,
        )
        self.at("ratio_residues")
        self.show(
            formula(r"r_S\equiv w_S\equiv1\pmod{1+i}", size=48, color=YELLOW).move_to(
                DOWN * 1.65
            ),
            words("Every division used the unit denominator", size=27).move_to(
                DOWN * 3.15
            ),
            run_time=1.1,
        )

        self.section("products", "Products and inverses keep residue one")
        self.show(
            formula(
                r"R=\prod_{S\subseteq I}r_S^{(-1)^{|S|}}", size=47, color=BLUE_C
            ).move_to(UP * 1.4),
            formula(
                r"W=\prod_{S\subseteq I}w_S^{(-1)^{|S|}}", size=47, color=BLUE_C
            ).move_to(DOWN * 0.3),
            run_time=1.2,
        )
        self.at("unit_factors")
        self.show(
            words(
                "Every factor is a unit of residue one", size=29, color=YELLOW
            ).move_to(DOWN * 2.35),
            run_time=0.9,
        )
        self.at("inverse_rule")
        self.hide(*list(self.body))
        self.show(
            formula(
                r"t\in\{r_S,w_S\},\qquad t\in A^{\times},\quad\pi(t)=1",
                size=40,
                color=BLUE_C,
            ).move_to(UP * 1.8)
        )
        inverse_product = formula(r"t\,t^{-1}=1", size=54).move_to(UP * 0.05)
        self.show(inverse_product, run_time=0.9)
        self.at("reduce_inverse")
        self.play(
            Transform(
                inverse_product,
                formula(r"\pi(t)\,\pi(t^{-1})=1", size=49).move_to(inverse_product),
            ),
            run_time=0.9,
        )
        self.at("inverse_one")
        self.play(
            Transform(
                inverse_product,
                formula(
                    r"1\cdot\pi(t^{-1})=1\quad\Longrightarrow\quad\pi(t^{-1})=1",
                    size=43,
                    color=YELLOW,
                ).move_to(inverse_product),
            ),
            run_time=1.1,
        )
        self.at("product_factors")
        self.hide(*list(self.body))
        reduction = formula(
            r"\pi:A\longrightarrow A/(1+i)A", size=38, color=BLUE_C
        ).move_to(UP * 2.1)
        fractions = [
            self.product_fraction("R", "r", -3.6),
            self.product_fraction("W", "w", 4.0),
        ]
        self.show(reduction, *fractions, run_time=1.1)
        self.at("all_ones")
        self.play(
            *(
                Transform(part, formula(source, size=40, color=YELLOW).move_to(part))
                for fraction, letter in zip(fractions, ["R", "W"], strict=True)
                for part, source in [
                    (fraction[0], rf"\pi({letter})="),
                    (
                        fraction[1],
                        r"\prod_{\substack{S\subseteq I\\|S|\text{ even}}}1",
                    ),
                    (
                        fraction[2],
                        r"\prod_{\substack{S\subseteq I\\|S|\text{ odd}}}1",
                    ),
                ]
            ),
            run_time=1.1,
        )
        self.play(
            *(
                Transform(part, formula("1", size=46, color=YELLOW).move_to(part))
                for fraction in fractions
                for part in [fraction[1], fraction[2]]
            ),
            run_time=0.8,
        )
        self.at("comparison_residues")
        self.hide(*list(self.body))
        conclusion = formula(
            r"\boxed{R\equiv W\equiv1\pmod{1+i}}", size=51, color=YELLOW
        ).move_to(UP * 0.8)
        self.show(conclusion, run_time=1.1)
        self.at("one_prime_example")
        self.play(conclusion.animate.scale(0.75).move_to(DOWN * 2.25), run_time=0.65)
        self.show(
            formula(
                r"u=3:\quad I=\{3\},\quad\zeta_{\varnothing}=1,\quad"
                r"\zeta_{\{3\}}=\omega=e^{2\pi i/3}",
                size=34,
                color=BLUE_C,
                width=14.4,
            ).move_to(UP * 2.0),
            formula(r"R=\frac{r_{\varnothing}}{r_{\{3\}}}", size=49).move_to(
                LEFT * 3.7 + UP * 0.4
            ),
            formula(r"W=\frac{w_{\varnothing}}{w_{\{3\}}}", size=49).move_to(
                RIGHT * 3.7 + UP * 0.4
            ),
            run_time=1.1,
        )
        self.at("more_primes")
        self.show(
            words(
                "More distinct primes give more factors · the same rule applies",
                size=27,
            ).move_to(DOWN * 1.1),
            run_time=0.9,
        )
        self.at("rigidity_next")
        self.show(
            words(
                "Algebraic residue condition · exact comparisons await "
                "odd-order rigidity",
                size=26,
            ).move_to(DOWN * 3.35),
            run_time=0.9,
        )
