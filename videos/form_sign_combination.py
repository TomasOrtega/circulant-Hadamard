import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    FadeIn,
    FadeOut,
    Line,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class FormSignCombination(NodeScene):
    node_id = "form-sign-combination"
    title = "5.1 · Form the Combination"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def hide(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.35)
        self.body.remove(*objects)

    def before_reduction(self):
        return words(
            "Exact coefficient arithmetic · before reduction", size=27, color=YELLOW
        ).move_to(UP * 2.2)

    def normalized_row(self, name, terms, y):
        return (
            VGroup(
                formula(rf"{name}(P)=\frac12\bigl(", size=34),
                *(formula(term, size=34, color=BLUE_C) for term in terms),
                formula(r"\bigr)", size=34),
            )
            .arrange(RIGHT, buff=0.23)
            .set_max_width(14.8)
            .move_to(UP * y)
        )

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/form-sign-combination.json").read_text()
        )["detail_cues"]

        self.section(
            "signs", "The same four sign polynomials define all three evaluations"
        )
        self.show(
            formula(
                r"u\in\mathbb Z_{>0},\qquad\mathbb Z[i][P]/(P^{u^2}-1)", size=40
            ).move_to(UP * 2.0)
        )
        self.at("common_signs")
        self.show(
            formula(
                r"H_a(P)=\sum_{b=0}^{u^2-1}h_{a,b}P^b,\qquad h_{a,b}\in\{-1,1\}",
                size=43,
                color=BLUE_C,
            ).move_to(UP * 0.35),
            words("The same original signs define c, d, and g", size=29).move_to(
                DOWN * 1.4
            ),
        )
        self.at("normalized")
        self.hide(*list(self.body))
        originals = VGroup(
            *(
                formula(rf"H_{a}(P)", size=39, color=BLUE_C).move_to(
                    RIGHT * (-5.1 + 3.4 * a) + UP * 2.15
                )
                for a in range(4)
            )
        )
        self.show(originals, run_time=0.8)
        rows = [
            self.normalized_row("c", ["H_0(P)", "+H_1(P)", "+H_2(P)", "+H_3(P)"], 0.75),
            self.normalized_row(
                "d", ["H_0(P)", "-H_1(P)", "+H_2(P)", "-H_3(P)"], -0.55
            ),
            self.normalized_row(
                "g", ["H_0(P)", "-H_2(P)", "+iH_1(P)", "-iH_3(P)"], -1.85
            ),
        ]
        for key, row, order in zip(
            ["c_formula", "d_formula", "g_formula"],
            rows,
            [[0, 1, 2, 3], [0, 1, 2, 3], [0, 2, 1, 3]],
            strict=True,
        ):
            self.at(key)
            self.body.add(row)
            self.play(
                FadeIn(row[0]),
                FadeIn(row[-1]),
                *(
                    TransformFromCopy(originals[a], target)
                    for a, target in zip(order, row[1:-1], strict=True)
                ),
                run_time=1.15,
            )
        self.at("h0_cancels")
        same_h0 = VGroup(
            *(SurroundingRectangle(row[1], buff=0.08).set_color(YELLOW) for row in rows)
        )
        self.show(
            same_h0,
            words("H₀ cancels from d − c and g − c", size=29, color=YELLOW).move_to(
                DOWN * 3.25
            ),
            run_time=0.85,
        )

        self.section("quotients", "Justify both divisions in characteristic zero")
        badge = self.before_reduction()
        self.show(badge, run_time=0.65)
        difference = (
            VGroup(
                formula(r"d-c=\frac12[", size=36),
                *(
                    formula(term, size=36, color=BLUE_C)
                    for term in [
                        "H_0",
                        "-H_1",
                        "+H_2",
                        "-H_3",
                        "-H_0",
                        "-H_1",
                        "-H_2",
                        "-H_3",
                    ]
                ),
                formula("]", size=36),
            )
            .arrange(RIGHT, buff=0.18)
            .set_max_width(15.0)
            .move_to(UP * 0.9)
        )
        abbreviation = words("Here Hₐ means Hₐ(P)", size=25, color=BLUE_C).move_to(
            DOWN * 2.85
        )
        self.show(difference, abbreviation, run_time=0.9)
        cancellation = VGroup(
            *(
                Line(
                    term.get_corner(LEFT + DOWN), term.get_corner(RIGHT + UP)
                ).set_stroke(YELLOW, width=3)
                for term in [difference[j] for j in (1, 3, 5, 7)]
            )
        )
        self.show(cancellation, run_time=0.6)
        self.at("real_difference")
        self.hide(cancellation)
        self.play(
            Transform(difference, formula(r"d-c=-H_1-H_3", size=49).move_to(UP * 0.9)),
            run_time=1.0,
        )
        self.at("real_quotient")
        self.play(
            Transform(
                difference,
                formula(
                    r"\frac{d-c}{2}=-\frac{H_1+H_3}{2}", size=49, color=YELLOW
                ).move_to(UP * 0.6),
            ),
            run_time=1.1,
        )

        self.at("gaussian_difference")
        self.hide(difference)
        gaussian = formula(r"g-c=\frac{-H_1-2H_2-H_3+i(H_1-H_3)}2", size=46).move_to(
            UP * 0.9
        )
        self.show(gaussian, run_time=1.1)
        self.at("reciprocal")
        reciprocal = formula(r"\frac1{1+i}=\frac{1-i}{2}", size=46, color=YELLOW)
        reciprocal.move_to(DOWN * 0.9)
        self.show(reciprocal, run_time=0.8)
        self.at("multiply")
        self.play(
            Transform(
                gaussian,
                formula(
                    r"\frac{g-c}{1+i}=\frac{\bigl[-H_1-2H_2-H_3+i(H_1-H_3)\bigr](1-i)}4",
                    size=41,
                    width=14.4,
                ).move_to(UP * 0.9),
            ),
            run_time=1.2,
        )
        self.at("expand")
        self.play(
            Transform(
                gaussian,
                formula(
                    r"\frac{g-c}{1+i}=\frac{-2H_2-2H_3+i(2H_1+2H_2)}4",
                    size=46,
                ).move_to(UP * 0.9),
            ),
            run_time=1.3,
        )
        self.at("simplify")
        self.hide(reciprocal)
        self.play(
            Transform(
                gaussian,
                formula(
                    r"\frac{g-c}{1+i}=-\frac{H_2+H_3}2+i\frac{H_1+H_2}2",
                    size=47,
                    color=YELLOW,
                ).move_to(UP * 1.05),
            ),
            run_time=1.2,
        )
        self.at("sign_sums")
        sums = VGroup(
            *(
                formula(value, size=45, color=BLUE_C).move_to(
                    RIGHT * (-4 + 4 * j) + DOWN * 0.8
                )
                for j, value in enumerate(["-1-1", "-1+1", "1+1"])
            )
        )
        self.show(sums, run_time=0.85)
        self.play(
            *(
                Transform(term, formula(value, size=48, color=BLUE_C).move_to(term))
                for term, value in zip(sums, ["-2", "0", "2"], strict=True)
            ),
            run_time=0.9,
        )
        self.at("sign_halves")
        self.play(
            *(
                Transform(term, formula(value, size=45, color=YELLOW).move_to(term))
                for term, value in zip(
                    sums, [r"\frac{-2}2=-1", r"\frac02=0", r"\frac22=1"], strict=True
                )
            ),
            run_time=1.2,
        )
        self.show(
            formula(r"\frac{H_a+H_b}{2}\in\mathbb Z[P]/(P^{u^2}-1)", size=37).move_to(
                DOWN * 2.15
            ),
            run_time=0.85,
        )
        self.at("integral_quotients")
        self.hide(*(obj for obj in list(self.body) if obj is not badge))
        self.show(
            formula(r"\frac{d(P)-c(P)}2\in\mathbb Z[P]/(P^{u^2}-1)", size=44).move_to(
                UP * 0.7
            ),
            formula(
                r"\frac{g(P)-c(P)}{1+i}\in\mathbb Z[i][P]/(P^{u^2}-1)",
                size=44,
                color=BLUE_C,
            ).move_to(DOWN * 1.15),
            run_time=1.2,
        )

        self.section(
            "collect", "Add the integral quotients and collect the common half-sum"
        )
        self.show(self.before_reduction(), run_time=0.65)
        definition = formula(
            r"E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}", size=48
        ).move_to(UP * 0.85)
        self.show(definition, run_time=1.2)
        self.at("add_formulas")
        expanded = (
            VGroup(
                formula("E(P)=", size=40),
                formula(r"-\frac{H_1}2", size=40, color=BLUE_C),
                formula(r"-\frac{H_3}2", size=40, color=BLUE_C),
                formula(r"-\frac{H_2}2", size=40, color=BLUE_C),
                formula(r"-\frac{H_3}2", size=40, color=BLUE_C),
                formula(r"+i\frac{H_1+H_2}2", size=40, color=BLUE_C),
            )
            .arrange(RIGHT, buff=0.25)
            .set_max_width(14.2)
            .move_to(DOWN * 1.0)
        )
        self.body.add(expanded)
        self.play(TransformFromCopy(definition, expanded), run_time=1.1)
        self.at("two_halves")
        h3_frames = VGroup(
            *(
                SurroundingRectangle(expanded[j], buff=0.09).set_color(YELLOW)
                for j in [2, 4]
            )
        )
        self.show(h3_frames, run_time=0.7)
        combined = (
            VGroup(
                formula("E(P)=", size=41),
                formula("-H_3", size=41, color=YELLOW),
                formula(r"-\frac{H_1+H_2}2", size=41, color=BLUE_C),
                formula(r"+i\frac{H_1+H_2}2", size=41, color=BLUE_C),
            )
            .arrange(RIGHT, buff=0.3)
            .set_max_width(14.2)
            .move_to(DOWN * 1.0)
        )
        self.body.add(combined)
        self.play(
            TransformFromCopy(expanded[0], combined[0]),
            TransformFromCopy(VGroup(expanded[2], expanded[4]), combined[1]),
            TransformFromCopy(VGroup(expanded[1], expanded[3]), combined[2]),
            TransformFromCopy(expanded[5], combined[3]),
            FadeOut(expanded),
            FadeOut(h3_frames),
            run_time=1.4,
        )
        self.body.remove(expanded, h3_frames)
        self.at("collect_factor")
        self.play(
            Transform(
                combined,
                formula(
                    r"\boxed{E(P)=-H_3(P)+(i-1)\frac{H_1(P)+H_2(P)}2}",
                    size=47,
                    color=YELLOW,
                ).move_to(DOWN * 0.8),
            ),
            run_time=1.3,
        )
        self.at("correction")
        correction = formula(r"i-1=i(1+i)", size=43, color=BLUE_C).move_to(DOWN * 2.15)
        later = words("The reduction comes next", size=27).move_to(DOWN * 3.35)
        self.show(correction, later, run_time=0.9)
        self.at("divisibilities")
        self.hide(*(obj for obj in list(self.body) if obj is not combined))
        self.play(combined.animate.move_to(UP * 1.6), run_time=0.7)
        self.show(
            formula(r"2\mid d(P)-c(P)", size=44, color=BLUE_C).move_to(DOWN * 0.15),
            formula(r"1+i\mid g(P)-c(P)", size=44, color=BLUE_C).move_to(DOWN * 1.45),
            run_time=1.0,
        )
        self.at("signs_only")
        self.show(
            words(
                "Common signs only · no norm identity or oddness needed", size=29
            ).move_to(DOWN * 2.9),
            run_time=0.9,
        )
