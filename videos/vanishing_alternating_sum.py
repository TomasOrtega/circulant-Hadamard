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
    Line,
    Rectangle,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


def subset_columns():
    columns = []
    for index, (subset, subscript, sign) in enumerate(
        [
            (r"\varnothing", r"\varnothing", "+"),
            (r"\{p\}", r"\{p\}", "-"),
            (r"\{q\}", r"\{q\}", "-"),
            (r"\{p,q\}", r"\{p,q\}", "+"),
        ]
    ):
        center = RIGHT * (-5.7 + 3.8 * index) + DOWN * 0.6
        border = Rectangle(width=3.45, height=4.4).set_stroke(BLUE_C, 2)
        border.move_to(center)
        heading = formula(rf"{sign}\quad S={subset}", size=31, color=YELLOW)
        heading.move_to(center + UP * 1.7)
        first = formula(
            rf"\frac{{d_{{{subscript}}}-c_{{{subscript}}}}}{{2c_{{{subscript}}}}}",
            size=35,
            width=2.9,
        ).move_to(center + UP * 0.55)
        second = formula(
            rf"\frac{{g_{{{subscript}}}-c_{{{subscript}}}}}"
            rf"{{(1+i)c_{{{subscript}}}}}",
            size=33,
            width=2.9,
        ).move_to(center + DOWN * 1)
        divider = Line(center + LEFT * 1.4, center + RIGHT * 1.4).set_stroke(BLUE_C, 1)
        columns.append(
            {
                "frame": VGroup(border, heading, divider),
                "terms": VGroup(first, second),
                "divider": divider,
                "center": center,
                "subscript": subscript,
            }
        )
    return columns


class VanishingAlternatingSum(NodeScene):
    node_id = "vanishing-alternating-sum"
    title = "7.4 · Identify E(P) and Add the Sums"

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
            (ROOT / "videos/production/vanishing-alternating-sum.json").read_text()
        )["detail_cues"]

        self.section("setup", "One set of inputs and one common ring")
        self.show(
            formula(r"u>1\text{ odd}", size=43, color=BLUE_C).move_to(
                LEFT * 4 + UP * 1.9
            ),
            words("I: distinct prime divisors of u", size=28).move_to(
                RIGHT * 3.1 + UP * 1.9
            ),
            run_time=1,
        )
        self.at("setup_indices")
        self.show(
            formula(r"\zeta_S=\prod_{p\in S}\zeta_p", size=47).move_to(UP * 0.5),
            run_time=0.9,
        )
        self.at("setup_empty")
        self.show(
            formula(r"\zeta_{\varnothing}=1", size=43, color=BLUE_C).move_to(
                DOWN * 0.8
            ),
            run_time=0.8,
        )
        self.at("setup_ring")
        self.show(
            formula(r"A=\mathbb Z[i,\{\zeta_p:p\in I\},1/u]", size=42).move_to(
                DOWN * 2
            ),
            run_time=1,
        )
        self.at("setup_notation")
        self.show(
            formula(
                r"c_S=c(\zeta_S),\quad d_S=d(\zeta_S),\quad g_S=g(\zeta_S)",
                size=35,
                color=BLUE_C,
            ).move_to(DOWN * 3.45),
            run_time=1,
        )

        self.section("two_sums", "Node 7.3: two alternating sums with zero residue")
        first_sum = formula(
            r"\sum_{S\subseteq I}(-1)^{|S|}\frac{d_S-c_S}{2c_S}\equiv0",
            size=49,
        ).move_to(UP * 1)
        second_sum = formula(
            r"\sum_{S\subseteq I}(-1)^{|S|}\frac{g_S-c_S}{(1+i)c_S}\equiv0",
            size=49,
        ).move_to(DOWN * 0.85)
        self.at("rows_d")
        self.show(first_sum, run_time=1.1)
        self.at("rows_g")
        self.show(second_sum, run_time=1.1)
        self.at("rows_quotient")
        self.show(
            formula(r"\text{Both in }A/(1+i)A", size=39, color=YELLOW).move_to(
                DOWN * 2.6
            ),
            run_time=0.9,
        )
        self.at("rows_match")
        self.erase(*list(self.body))
        columns = subset_columns()
        self.show(
            *(item for col in columns for item in [col["frame"], col["terms"]]),
            words("Two-prime indexing illustration: I = {p, q}", size=27).move_to(
                DOWN * 3.5
            ),
            run_time=1.1,
        )
        self.play(FlashAround(columns[0]["terms"], color=YELLOW), run_time=0.8)

        self.section("identify", "Recognize the polynomial in one matching column")
        self.at("identify_definition")
        definition = formula(
            r"E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}", size=47
        ).move_to(UP * 1.65)
        self.show(definition, run_time=1.1)
        self.at("identify_exact")
        self.show(
            words("Exact coefficientwise division before reduction", size=28).move_to(
                UP * 0.25
            ),
            run_time=0.9,
        )
        self.at("identify_unit")
        unit = formula(r"c_S\in A^\times", size=37, color=BLUE_C).move_to(DOWN * 0.75)
        self.show(unit, run_time=0.8)
        self.at("identify_factor")
        factored = formula(
            r"\frac1{c_S}(\frac{d_S-c_S}{2}+\frac{g_S-c_S}{1+i})",
            size=49,
            color=YELLOW,
        ).move_to(DOWN * 2.1)
        self.show(factored, run_time=1)
        self.at("identify_numerator")
        self.show(
            formula(r"\text{Numerator: }E(\zeta_S)", size=34, color=BLUE_C).move_to(
                DOWN * 3.5
            ),
            run_time=0.8,
        )
        self.at("identify_result")
        self.erase(*list(self.body))
        identity = formula(
            r"\frac{d_S-c_S}{2c_S}+\frac{g_S-c_S}{(1+i)c_S}"
            r"=\frac{E(\zeta_S)}{c(\zeta_S)}",
            size=49,
            color=YELLOW,
            width=14,
        ).move_to(UP * 0.3)
        self.show(
            identity,
            formula(
                r"\text{Exact identity in }A;\quad c_S\in A^\times",
                size=33,
                color=BLUE_C,
            ).move_to(DOWN * 2.2),
            run_time=1.2,
        )

        self.section("assemble", "Replace every column, then add the zero residues")
        columns = subset_columns()
        self.show(
            *(item for col in columns for item in [col["frame"], col["terms"]]),
            words(
                "Two-prime illustration; the same replacement works for every S",
                size=25,
            ).move_to(DOWN * 3.5),
            run_time=0.8,
        )
        replacements = []
        for col in columns:
            target = formula(
                rf"\frac{{E(\zeta_{{{col['subscript']}}})}}"
                rf"{{c_{{{col['subscript']}}}}}",
                size=39,
                color=YELLOW,
                width=2.9,
            ).move_to(col["center"] + DOWN * 0.25)
            self.body.add(target)
            replacements.append((col["terms"], target))
        self.play(
            *(TransformFromCopy(source, target) for source, target in replacements),
            *(FadeOut(col["terms"]) for col in columns),
            *(FadeOut(col["divider"]) for col in columns),
            run_time=1,
        )
        self.body.remove(*(col["terms"] for col in columns))
        for col in columns:
            col["frame"].remove(col["divider"])
        self.at("assemble_sum")
        self.erase(*list(self.body))
        general_sum = formula(
            r"\mathcal S:=\sum_{S\subseteq I}(-1)^{|S|}"
            r"\frac{E(\zeta_S)}{c(\zeta_S)}",
            size=55,
        ).move_to(UP * 0.9)
        self.show(general_sum, run_time=1.2)
        self.at("assemble_zero")
        self.show(
            formula(
                r"\boxed{\mathcal S\equiv0\pmod{1+i}}", size=49, color=YELLOW
            ).move_to(DOWN * 1.05),
            run_time=1,
        )
        self.at("assemble_signs")
        self.show(
            formula(r"|S|\text{ even}: +", size=34, color=BLUE_C).move_to(
                LEFT * 3.7 + DOWN * 2.45
            ),
            formula(r"|S|\text{ odd}: -", size=34, color=BLUE_C).move_to(
                RIGHT * 3.7 + DOWN * 2.45
            ),
            run_time=0.9,
        )
        self.at("assemble_char2")
        self.show(
            words(
                "Signs retain the exact construction; + and − agree after reduction",
                size=26,
            ).move_to(DOWN * 3.5),
            run_time=0.9,
        )

        self.section("example", "For u = 3, the two-term difference is zero exactly")
        self.show(
            formula(
                r"u=3:\qquad\zeta_{\varnothing}=1,\quad\zeta_{\{3\}}=\omega",
                size=40,
                color=BLUE_C,
            ).move_to(UP * 1.9),
            run_time=1,
        )
        self.at("example_c")
        c_relation = formula(r"c(\omega)=\lambda c(1)", size=43).move_to(
            LEFT * 4.1 + UP * 0.45
        )
        self.show(c_relation, run_time=0.9)
        self.at("example_e")
        e_relation = formula(r"E(\omega)=\lambda E(1)", size=43).move_to(
            RIGHT * 4.1 + UP * 0.45
        )
        self.show(e_relation, run_time=0.9)
        self.at("example_cancel")
        normalized = formula(
            r"\frac{E(\omega)}{c(\omega)}"
            r"=\frac{\lambda E(1)}{\lambda c(1)}=\frac{E(1)}{c(1)}",
            size=48,
            color=YELLOW,
        ).move_to(DOWN * 1.3)
        self.copy_to(VGroup(c_relation, e_relation), normalized, run_time=1.1)
        self.at("example_zero_safe")
        self.show(
            formula(
                r"c(1)\ne0,\quad\lambda\ne0;\qquad E(1)=0\text{ is allowed}", size=32
            ).move_to(DOWN * 3),
            run_time=0.9,
        )
        self.at("example_exact")
        self.erase(*list(self.body))
        self.show(
            formula(
                r"\mathcal S=\frac{E(1)}{c(1)}-\frac{E(\omega)}{c(\omega)}=0",
                size=53,
                color=YELLOW,
            ).move_to(UP * 0.5),
            words(
                "Exact equality in this two-input case", size=30, color=BLUE_C
            ).move_to(DOWN * 1.6),
            run_time=1.1,
        )

        self.section("handoff", "General conclusion and the next coefficient input")
        self.show(
            formula(
                r"\sum_{S\subseteq I}(-1)^{|S|}\frac{E(\zeta_S)}{c(\zeta_S)}"
                r"\equiv0\pmod{1+i}",
                size=45,
                color=YELLOW,
                width=14,
            ).move_to(UP * 1.15),
            words(
                "Every odd u > 1; no common rotation across all inputs is needed",
                size=26,
            ).move_to(DOWN * 0.35),
            run_time=1.1,
        )
        self.at("handoff_coefficient")
        self.show(
            formula(r"E(P)\equiv J(P)\pmod{1+i}", size=44, color=BLUE_C).move_to(
                DOWN * 1.7
            ),
            run_time=1,
        )
        self.at("handoff_one")
        self.show(
            words("Node 8: the all-ones calculation gives residue 1", size=28).move_to(
                DOWN * 3.3
            ),
            run_time=0.9,
        )
