import json
from math import cos, sin

from manimlib import (
    BLUE_B,
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    TAU,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    FadeOut,
    Rotate,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


def vector_arrow(center, value, scale=0.55, color=BLUE_C):
    return Arrow(
        center, center + scale * (value.real * RIGHT + value.imag * UP), buff=0
    ).set_color(color)


def arrow_labels(arrows, argument, directions):
    return VGroup(
        *(
            formula(rf"{name}({argument})", size=26, color=arrow.get_color()).next_to(
                arrow.get_end(), direction, buff=0.2
            )
            for name, arrow, direction in zip(
                ["c", "d", "g"], arrows, directions, strict=True
            )
        )
    )


class ExactComparisonIdentities(NodeScene):
    node_id = "exact-comparison-identities"
    title = "6.5 · Exact Comparisons and a Common Rotation"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def erase(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.35)
        self.body.remove(*objects)

    def copy_to(self, source, target, run_time=1):
        self.body.add(target)
        self.play(TransformFromCopy(source, target), run_time=run_time)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/exact-comparison-identities.json").read_text()
        )["detail_cues"]
        self.section("products", "Unpack two exact alternating products")
        self.show(
            formula(
                r"u>1\text{ odd},\qquad c_S=c(\zeta_S),\ "
                r"d_S=d(\zeta_S),\ g_S=g(\zeta_S)",
                size=35,
            ).move_to(UP * 2.05),
            run_time=1,
        )
        self.at("products_input")
        self.show(formula(r"R=W=1", size=48, color=YELLOW).move_to(UP * 0.85))
        self.at("products_unpack")
        r_product = formula(
            r"\prod_{S\subseteq I}\left(\frac{d_S}{c_S}\right)^{(-1)^{|S|}}=1",
            size=44,
            color=BLUE_C,
        ).move_to(DOWN * 0.65)
        w_product = formula(
            r"\prod_{S\subseteq I}\left(\frac{g_S}{c_S}\right)^{(-1)^{|S|}}=1",
            size=44,
            color=BLUE_B,
        ).move_to(DOWN * 2.35)
        self.show(r_product, w_product)
        self.at("products_units")
        self.show(
            words(
                "All evaluated denominators are units in A = B[1/u]", size=26
            ).move_to(DOWN * 3.55),
            run_time=0.8,
        )
        self.at("products_even_odd")
        even_odd = VGroup(
            formula(
                r"\prod_{|S|\,\mathrm{even}}\frac{d_S}{c_S}=\prod_{|S|\,\mathrm{odd}}\frac{d_S}{c_S}",
                size=39,
                color=BLUE_C,
            ).move_to(r_product),
            formula(
                r"\prod_{|S|\,\mathrm{even}}\frac{g_S}{c_S}=\prod_{|S|\,\mathrm{odd}}\frac{g_S}{c_S}",
                size=39,
                color=BLUE_B,
            ).move_to(w_product),
        )
        self.play(
            Transform(r_product, even_odd[0]),
            Transform(w_product, even_odd[1]),
            run_time=1.4,
        )

        self.section("two_inputs", "For u = 3, two input ratios agree")
        self.show(
            formula(r"u=3,\qquad P=1,\omega", size=40, color=BLUE_C).move_to(UP * 2.05)
        )
        ratios = VGroup(
            formula(r"\frac{d(1)}{c(1)}=\frac{d(\omega)}{c(\omega)}", size=45).move_to(
                LEFT * 3.8 + UP * 0.6
            ),
            formula(r"\frac{g(1)}{c(1)}=\frac{g(\omega)}{c(\omega)}", size=45).move_to(
                RIGHT * 3.8 + UP * 0.6
            ),
        )
        self.at("two_ratios")
        self.show(ratios)
        self.at("lambda_define")
        multiplier = formula(
            r"\lambda=\frac{c(\omega)}{c(1)}", size=48, color=YELLOW
        ).move_to(DOWN * 1.05)
        self.show(multiplier)
        self.at("lambda_norm")
        self.show(
            formula(
                r"|c(1)|=|c(\omega)|=3\quad\Longrightarrow\quad|\lambda|=1", size=35
            ).move_to(DOWN * 2.4),
            run_time=1,
        )
        self.at("shared_multiplier")
        self.erase(*list(self.body))
        self.show(
            formula(r"c(\omega)=\lambda c(1)", size=43, color=BLUE_C).move_to(UP * 1.5),
            formula(r"d(\omega)=\lambda d(1)", size=43).move_to(UP * 0.25),
            formula(r"g(\omega)=\lambda g(1)", size=43, color=BLUE_B).move_to(DOWN * 1),
        )
        self.at("inverse_delta")
        self.show(
            formula(r"\lambda=\Delta(c)^{-1}", size=42, color=YELLOW).move_to(
                DOWN * 2.6
            )
        )

        self.section(
            "combination", "The same rotation carries the integral combination"
        )
        left = LEFT * 4.3 + DOWN * 0.1
        right = RIGHT * 4.3 + DOWN * 0.1
        values = [3 + 0j, -3 + 0j, 3j]
        colors = [BLUE_C, WHITE, BLUE_B]
        circles = VGroup(
            *(
                Circle(radius=1.3).set_color(BLUE_C).move_to(center)
                for center in [left, right]
            )
        )
        left_arrows = VGroup(
            *(
                vector_arrow(left, z, scale=1.3 / 3, color=color)
                for z, color in zip(values, colors, strict=True)
            )
        )
        right_arrows = VGroup(
            *(
                vector_arrow(right, z, scale=1.3 / 3, color=color)
                for z, color in zip(values, colors, strict=True)
            )
        )
        self.show(
            circles,
            left_arrows,
            arrow_labels(left_arrows, "1", [RIGHT, LEFT, UP]),
            run_time=0.8,
        )
        self.copy_to(left_arrows, right_arrows, run_time=0.7)
        self.play(Rotate(right_arrows, TAU / 3, about_point=right), run_time=1)
        self.show(
            arrow_labels(
                right_arrows, r"\omega", [UP + LEFT, DOWN + RIGHT, LEFT + DOWN]
            ),
            words("Schematic directions · shared multiplier λ", size=27).move_to(
                DOWN * 2.4
            ),
            words("Relative positions are preserved", size=27, color=YELLOW).move_to(
                DOWN * 3.4
            ),
            run_time=0.6,
        )
        self.at("e_definition")
        self.erase(*list(self.body))
        definition = formula(
            r"E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}", size=44
        ).move_to(UP * 1.75)
        self.show(definition)
        self.at("exact_before")
        self.show(
            words(
                "Exact integral polynomial quotients · formed before reduction",
                size=26,
                color=BLUE_C,
            ).move_to(DOWN * 3.5),
            run_time=0.8,
        )
        self.at("substitute_lambda")
        substitution = formula(
            r"E(\omega)=\frac{\lambda d(1)-\lambda c(1)}2"
            r"+\frac{\lambda g(1)-\lambda c(1)}{1+i}",
            size=39,
            width=14,
        ).move_to(DOWN * 0.15)
        self.copy_to(definition, substitution, run_time=1.2)
        self.at("factor_lambda")
        self.play(
            Transform(
                substitution,
                formula(
                    r"E(\omega)=\lambda\left[\frac{d(1)-c(1)}2+\frac{g(1)-c(1)}{1+i}\right]",
                    size=40,
                    color=YELLOW,
                ).move_to(substitution),
            ),
            run_time=1.2,
        )
        self.at("e_rotation")
        self.show(
            formula(r"\boxed{E(\omega)=\lambda E(1)}", size=47, color=YELLOW).move_to(
                DOWN * 2
            )
        )

        self.section("normalization", "Divide by c; the common multiplier cancels")
        self.show(
            formula(r"E(\omega)=\lambda E(1)", size=45, color=BLUE_B).move_to(UP * 1.9),
            formula(r"c(\omega)=\lambda c(1)", size=45, color=BLUE_C).move_to(
                UP * 0.65
            ),
        )
        normalized = formula(
            r"\frac{E(\omega)}{c(\omega)}=\frac{\lambda E(1)}{\lambda c(1)}", size=51
        ).move_to(DOWN * 1)
        self.show(normalized)
        self.at("cancel_multiplier")
        self.play(
            Transform(
                normalized,
                formula(
                    r"\boxed{\frac{E(\omega)}{c(\omega)}=\frac{E(1)}{c(1)}}",
                    size=51,
                    color=YELLOW,
                ).move_to(normalized),
            ),
            run_time=1.2,
        )
        self.at("nonzero_c")
        self.show(
            formula(
                r"c(1),c(\omega)\text{ are nonzero units}", size=35, color=BLUE_C
            ).move_to(DOWN * 2.65),
            run_time=0.9,
        )
        self.at("e_zero")
        self.show(
            words("E(1) = 0 is allowed", size=28).move_to(DOWN * 3.55), run_time=0.7
        )

        self.section("example", "Numerical schematic · not a Hadamard construction")
        self.show(
            formula(
                r"c(1)=3,\quad d(1)=-3,\quad g(1)=3i,\quad\lambda=\omega", size=34
            ).move_to(UP * 2.05),
            run_time=1,
        )
        circles = VGroup(
            *(
                Circle(radius=1.55).set_color(BLUE_C).move_to(center)
                for center in [left, right]
            )
        )
        omega = complex(cos(TAU / 3), sin(TAU / 3))
        original_arrows = VGroup(
            *(
                vector_arrow(left, z, scale=1.55 / 3, color=color)
                for z, color in zip(values, colors, strict=True)
            )
        )
        rotated_arrows = VGroup(
            *(
                vector_arrow(right, z * omega, scale=1.55 / 3, color=color)
                for z, color in zip(values, colors, strict=True)
            )
        )
        self.show(
            circles,
            original_arrows,
            arrow_labels(original_arrows, "1", [RIGHT, LEFT, UP]),
            run_time=0.8,
        )
        self.copy_to(original_arrows, rotated_arrows, run_time=1)
        self.show(
            arrow_labels(
                rotated_arrows, r"\omega", [UP + LEFT, DOWN + RIGHT, LEFT + DOWN]
            ),
            run_time=0.6,
        )
        self.at("example_e")
        e_left = vector_arrow(left, -3 + 3j, scale=1.55 / 3, color=YELLOW)
        e_right = vector_arrow(right, (-3 + 3j) * omega, scale=1.55 / 3, color=YELLOW)
        self.show(
            e_left,
            e_right,
            formula(r"E(1)=-3+3i,\qquad E(\omega)=\omega E(1)", size=36).move_to(
                DOWN * 2.6
            ),
            run_time=1,
        )
        self.at("example_normalize")
        self.erase(
            *[
                obj
                for obj in list(self.body)
                if obj is not e_left and obj is not e_right
            ]
        )
        center = DOWN * 0.35
        target = vector_arrow(center, -1 + 1j, scale=1.2, color=YELLOW)
        self.play(
            Transform(e_left, target), Transform(e_right, target.copy()), run_time=1.3
        )
        self.erase(e_right)
        self.show(
            Circle(radius=1.2).set_color(BLUE_C).move_to(center),
            formula(
                r"\frac{E(1)}{c(1)}=\frac{E(\omega)}{c(\omega)}=-1+i",
                size=44,
                color=YELLOW,
            ).move_to(UP * 1.9),
            words("The normalized E arrow can leave the unit circle", size=27).move_to(
                DOWN * 2.7
            ),
            run_time=1,
        )

        self.section("residues", "Normalized equality leaves raw residues undecided")
        self.show(
            formula(
                r"\frac{E(\omega)}{c(\omega)}=\frac{E(1)}{c(1)}", size=50, color=YELLOW
            ).move_to(UP * 1.6),
            formula(r"E(\omega)=\lambda E(1)", size=48, color=BLUE_C).move_to(
                DOWN * 0.1
            ),
        )
        self.at("raw_residues")
        self.show(
            words("The multiplier can have nontrivial residue", size=29).move_to(
                DOWN * 1.7
            )
        )
        self.at("no_schematic_residue")
        self.show(
            words(
                "No all-ones residue is assigned to the schematic",
                size=27,
                color=BLUE_C,
            ).move_to(DOWN * 3.15),
            run_time=0.9,
        )

        self.section("scope", "Carry two distinct outputs to Node 7")
        self.show(
            words("Two inputs · u = 3", size=29, color=BLUE_C).move_to(
                LEFT * 4.2 + UP * 1.8
            ),
            words("General subset products", size=29, color=BLUE_B).move_to(
                RIGHT * 4.1 + UP * 1.8
            ),
        )
        self.at("scope_products")
        self.show(
            formula(
                r"\frac{E(\omega)}{c(\omega)}=\frac{E(1)}{c(1)}", size=39, width=7
            ).move_to(LEFT * 4.2 + DOWN * 0.25),
            formula(
                r"\prod_S\left(\frac{d_S}{c_S}\right)^{(-1)^{|S|}}=1", size=34, width=7
            ).move_to(RIGHT * 4.1 + UP * 0.35),
            formula(
                r"\prod_S\left(\frac{g_S}{c_S}\right)^{(-1)^{|S|}}=1", size=34, width=7
            ).move_to(RIGHT * 4.1 + DOWN * 1.2),
        )
        self.at("scope_rotation")
        self.show(
            words(
                "Several prime divisors retain the full product identities", size=27
            ).move_to(DOWN * 2.8),
            run_time=0.9,
        )
        self.at("node_seven")
        self.show(
            words(
                "Node 7 · normalized equality and general product expansion",
                size=26,
                color=YELLOW,
            ).move_to(DOWN * 3.6),
            run_time=0.7,
        )
