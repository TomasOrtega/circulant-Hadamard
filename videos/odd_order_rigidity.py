import json
from math import cos, sin

from manimlib import (
    BLUE_A,
    BLUE_B,
    BLUE_C,
    BLUE_E,
    DOWN,
    GREY_B,
    LEFT,
    PI,
    RIGHT,
    TAU,
    UP,
    WHITE,
    YELLOW,
    Arc,
    Arrow,
    Circle,
    Dot,
    FadeIn,
    FadeOut,
    FlashAround,
    Line,
    Rectangle,
    Rotate,
    Transform,
    TransformFromCopy,
    Triangle,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words

VALUES = {"c": 3, "d": -3, "g": 3j, "E": -3 + 3j}
COLORS = {"c": BLUE_C, "d": BLUE_B, "g": WHITE, "E": BLUE_A}


def point(center, value, radius=1.25):
    return center + radius / 3 * (value.real * RIGHT + value.imag * UP)


def plane(center, radius=1.25):
    axes = VGroup(
        Line(center + LEFT * (radius + 0.2), center + RIGHT * (radius + 0.2)),
        Line(center + DOWN * (radius + 0.2), center + UP * (radius + 0.2)),
    ).set_stroke(GREY_B, width=1, opacity=0.45)
    circle = Circle(radius=radius).set_color(BLUE_C).move_to(center)
    return VGroup(axes, circle)


def value_arrow(center, value, name, argument, radius=1.25, normalized=False):
    endpoint = point(center, value, radius)
    ray = Arrow(center, endpoint, buff=0).set_color(COLORS[name])
    marker = (
        (
            Triangle().set_height(0.16).set_fill(BLUE_A, opacity=1)
            if name == "E"
            else Dot(radius=0.06)
        )
        .set_color(COLORS[name])
        .move_to(endpoint)
    )
    label = formula(
        rf"\frac{{{name}({argument})}}{{c({argument})}}"
        if normalized
        else rf"{name}({argument})",
        size=25,
        color=COLORS[name],
    )

    def place(mob):
        direction = marker.get_center() - center
        if abs(direction[0]) < 0.1:
            direction = RIGHT + (UP if direction[1] >= 0 else DOWN)
        mob.next_to(marker, direction, buff=0.14)

    label.add_updater(place)
    label.update()
    return VGroup(ray, marker), label


def triple(center, argument, angle=0, radius=1.25, include_e=False):
    names = ["c", "d", "g", "E"] if include_e else ["c", "d", "g"]
    rotation = complex(cos(angle), sin(angle))
    pairs = {
        name: value_arrow(center, VALUES[name] * rotation, name, argument, radius)
        for name in names
    }
    return (
        VGroup(*(pairs[name][0] for name in names)),
        VGroup(*(pairs[name][1] for name in names)),
        pairs,
    )


def box(text, center, width=4.8, color=BLUE_C):
    outline = Rectangle(width=width, height=0.85)
    outline.set_stroke(color, width=2).set_fill(BLUE_E, opacity=0.12)
    return VGroup(outline, words(text, size=24, width=width - 0.3)).move_to(center)


def angle_arcs(center):
    return VGroup(
        Arc(start_angle=0, angle=PI, radius=0.65).set_color(BLUE_B),
        Arc(start_angle=0, angle=PI / 2, radius=0.9).set_color(WHITE),
    ).shift(center)


class OddOrderRigidity(NodeScene):
    node_id = "odd-order-rigidity"
    title = "6 · Odd-Order Rigidity"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/odd-order-rigidity.json").read_text()
        )["detail_cues"]
        left, right = LEFT * 3.85 + DOWN * 0.65, RIGHT * 3.85 + DOWN * 0.65

        self.section("goal", "Three distinct values; one common rotation")
        norm = formula(r"ff^*=9\qquad(f=c,d,g)", size=49, color=BLUE_C)
        norm.move_to(UP * 1.9)
        self.show(norm)
        self.at("goal_inputs")
        self.show(plane(left), plane(right))
        self.show(
            formula(r"P=1", size=33).move_to(left + UP * 1.85),
            formula(r"P=\omega=e^{2\pi i/3}", size=33).move_to(right + UP * 1.85),
        )
        left_vectors, left_labels, _ = triple(left, "1")
        right_vectors, right_labels, _ = triple(right, r"\omega")
        self.show(left_vectors, left_labels)
        self.body.add(right_vectors, right_labels)
        self.play(
            TransformFromCopy(left_vectors, right_vectors),
            FadeIn(right_labels),
            run_time=1.5,
        )
        self.at("goal_rotation")
        self.play(Rotate(right_vectors, TAU / 3, about_point=right), run_time=2.5)
        self.show(
            formula(r"c(1)=3,\qquad d(1)=-3,\qquad g(1)=3i", size=32).move_to(
                DOWN * 2.65
            )
        )
        self.at("goal_scope")
        self.show(
            words(
                "Schematic values, not an order-36 circulant Hadamard matrix", size=23
            ).move_to(DOWN * 3.45)
        )

        self.section("comparisons", "Compare phase changes on a separate unit circle")
        delta = formula(r"\Delta(f)=\frac{f(1)}{f(\omega)}", size=50, color=BLUE_C)
        delta.move_to(LEFT * 3.5 + UP * 0.95)
        self.show(delta)
        self.at("comparison_odd")
        self.show(
            words("Δ(c), Δ(d), Δ(g): odd order", size=25).move_to(
                LEFT * 3.5 + DOWN * 0.3
            )
        )
        self.at("comparison_ratios")
        comparisons = (
            VGroup(
                formula(r"R=\frac{\Delta(d)}{\Delta(c)}", size=46),
                formula(r"W=\frac{\Delta(g)}{\Delta(c)}", size=46),
            )
            .arrange(DOWN, buff=0.55)
            .move_to(LEFT * 3.5 + DOWN * 1.75)
        )
        self.show(comparisons)
        self.at("comparison_candidates")
        center = RIGHT * 3.3 + DOWN * 0.65
        self.show(plane(center, radius=1.3))
        candidates = VGroup()
        for k, label in enumerate(["1", r"\omega", r"\omega^2"]):
            direction = cos(TAU * k / 3) * RIGHT + sin(TAU * k / 3) * UP
            marker = Dot(center + 1.3 * direction, radius=0.075).set_color(BLUE_C)
            candidates.add(
                VGroup(
                    marker,
                    formula(label, size=32).next_to(marker, direction, buff=0.18),
                )
            )
        self.show(candidates)
        self.show(
            words("Candidates for R and W", size=24).move_to(center + UP * 2.0),
            formula(r"R=W=1\quad\text{is the target}", size=35, color=YELLOW).move_to(
                RIGHT * 3.3 + DOWN * 3.0
            ),
        )

        self.section("signs", "The common signs supply congruences")
        divisibilities = (
            VGroup(
                formula(r"2\mid d(P)-c(P)", size=47, color=BLUE_C),
                formula(r"1+i\mid g(P)-c(P)", size=47, color=BLUE_C),
            )
            .arrange(DOWN, buff=0.7)
            .move_to(LEFT * 3.1 + UP * 0.1)
        )
        self.show(divisibilities)
        self.show(formula(r"2=(1+i)(1-i)", size=39).move_to(RIGHT * 3.3 + UP * 1.0))
        self.at("signs_reduce")
        reduced = (
            VGroup(
                formula(r"d(P)-c(P)\equiv0", size=41),
                formula(r"g(P)-c(P)\equiv0", size=41),
            )
            .arrange(DOWN, buff=0.65)
            .move_to(RIGHT * 3.3 + DOWN * 0.65)
        )
        self.body.add(reduced)
        self.play(
            *(
                TransformFromCopy(a, b)
                for a, b in zip(divisibilities, reduced, strict=True)
            ),
            run_time=1.6,
        )
        self.show(
            formula(r"\pmod{1+i}", size=36, color=YELLOW).move_to(DOWN * 2.45),
            words("Coefficientwise arithmetic", size=25).move_to(DOWN * 3.25),
        )

        self.section("units", "Check inverses before dividing congruences")
        self.show(formula(r"z\in\{1,\omega\}", size=42).move_to(UP * 1.85))
        norm = formula(r"c(z)\overline{c(z)}=9", size=52, color=BLUE_C).move_to(
            UP * 0.55
        )
        self.show(norm)
        self.at("units_inverse")
        inverse = formula(r"c(z)\,\frac{\overline{c(z)}}9=1", size=52).move_to(norm)
        self.play(Transform(norm, inverse), run_time=1.3)
        self.show(
            formula(r"c(z)^{-1}=\frac{\overline{c(z)}}9", size=42).move_to(DOWN * 0.95),
            words("Also for d(z) and g(z)", size=25).move_to(DOWN * 2.1),
        )
        self.at("units_localize")
        self.show(
            formula(r"A=\mathbb Z[i,\omega,1/3]", size=35).move_to(
                LEFT * 3.45 + DOWN * 3.15
            ),
            formula(r"9\equiv1\pmod{1+i}", size=35, color=YELLOW).move_to(
                RIGHT * 3.45 + DOWN * 3.15
            ),
        )
        self.at("units_conclusion")
        self.play(FlashAround(norm, color=YELLOW), run_time=0.8)

        self.section("ratios", "Unit denominators turn differences into ratios")
        top = (
            VGroup(
                formula(r"r_1:=\frac{d(1)}{c(1)}\equiv1", size=39, color=BLUE_C),
                formula(
                    r"r_\omega:=\frac{d(\omega)}{c(\omega)}\equiv1",
                    size=39,
                    color=BLUE_C,
                ),
            )
            .arrange(RIGHT, buff=1.8)
            .move_to(UP * 1.4)
        )
        bottom = (
            VGroup(
                formula(r"w_1:=\frac{g(1)}{c(1)}\equiv1", size=39),
                formula(r"w_\omega:=\frac{g(\omega)}{c(\omega)}\equiv1", size=39),
            )
            .arrange(RIGHT, buff=1.8)
            .move_to(UP * 0.1)
        )
        self.show(top, bottom)
        self.at("ratios_compare")
        r = formula(r"R=\frac{r_1}{r_\omega}\equiv\frac11=1", size=44).move_to(
            LEFT * 3.35 + DOWN * 1.6
        )
        w = formula(r"W=\frac{w_1}{w_\omega}\equiv\frac11=1", size=44).move_to(
            RIGHT * 3.35 + DOWN * 1.6
        )
        self.body.add(r, w)
        self.play(TransformFromCopy(top, r), TransformFromCopy(bottom, w), run_time=2)
        self.at("ratios_conclusion")
        self.show(
            formula(r"R\equiv W\equiv1\pmod{1+i}", size=48, color=YELLOW).move_to(
                DOWN * 3.0
            )
        )

        self.section("rigidity", "Odd order + residue one ⇒ exact equality")
        center = LEFT * 4.5 + DOWN * 0.55
        self.show(plane(center, radius=1.2))
        candidates = []
        for k, label in enumerate(["1", r"\omega", r"\omega^2"]):
            direction = cos(TAU * k / 3) * RIGHT + sin(TAU * k / 3) * UP
            marker = Dot(center + 1.2 * direction, radius=0.08).set_color(BLUE_C)
            candidates.append(
                VGroup(
                    marker,
                    formula(label, size=33).next_to(marker, direction, buff=0.18),
                )
            )
        self.show(*candidates)
        self.show(words("Phase comparisons R, W", size=24).move_to(center + UP * 2.05))
        self.at("rigidity_sum")
        proof_center = RIGHT * 2.1 + UP * 0.7
        geometric = formula(r"1+\omega+\omega^2=0", size=48, color=BLUE_C).move_to(
            proof_center
        )
        self.show(geometric)
        self.at("rigidity_ones")
        ones = (
            VGroup(
                formula("1", size=48),
                formula("+", size=48),
                formula("1", size=48),
                formula("+", size=48),
                formula("1", size=48),
                formula("=0", size=48),
            )
            .arrange(RIGHT, buff=0.16)
            .move_to(RIGHT * 2.1 + DOWN * 0.65)
        )
        self.body.add(ones)
        self.play(TransformFromCopy(geometric, ones), run_time=0.8)
        self.at("rigidity_pairs")
        strikes = VGroup(
            Line(ones[0].get_corner(LEFT + DOWN), ones[0].get_corner(RIGHT + UP)),
            Line(ones[2].get_corner(LEFT + DOWN), ones[2].get_corner(RIGHT + UP)),
        ).set_stroke(YELLOW, width=3)
        self.show(strikes, run_time=0.5)
        self.play(
            Transform(
                ones,
                formula(r"1=0\quad\text{impossible}", size=43, color=YELLOW).move_to(
                    ones
                ),
            ),
            FadeOut(strikes),
            run_time=0.6,
        )
        self.at("rigidity_exclude")
        self.play(
            candidates[1].animate.set_opacity(0.15),
            candidates[2].animate.set_opacity(0.15),
            run_time=0.7,
        )
        self.at("rigidity_general")
        self.play(FadeOut(geometric), FadeOut(ones), run_time=0.4)
        equation = formula(
            r"(\eta-1)(1+\eta+\cdots+\eta^{m-1})=\eta^m-1=0",
            size=38,
            width=8.3,
        ).move_to(RIGHT * 2.05 + UP * 0.6)
        self.show(equation)
        self.show(
            formula(r"\eta\ne1,\quad m>1\text{ odd}", size=33).move_to(
                RIGHT * 2.05 + UP * 1.6
            )
        )
        self.at("rigidity_cancel")
        self.play(
            Transform(
                equation,
                formula(r"1+\eta+\cdots+\eta^{m-1}=0", size=45).move_to(equation),
            ),
            run_time=0.8,
        )
        self.show(
            words(
                "Cancel η − 1 before reduction", size=24, color=YELLOW, width=7
            ).move_to(RIGHT * 2.05 + DOWN * 0.4),
            run_time=0.7,
        )
        self.at("rigidity_reduce")
        self.show(
            formula(r"\underbrace{1+1+\cdots+1}_{m\text{ odd}}=1\ne0", size=43).move_to(
                RIGHT * 2.05 + DOWN * 1.65
            ),
            run_time=1,
        )
        self.at("rigidity_conclusion")
        self.show(
            formula(r"\boxed{R=W=1}", size=55, color=YELLOW).move_to(DOWN * 3.0),
            run_time=0.8,
        )
        self.play(candidates[0].animate.set_color(YELLOW), run_time=0.5)

        self.section("rotation", "Each relative position keeps its own value")
        self.show(plane(left), plane(right))
        left_vectors, left_labels, _ = triple(left, "1")
        right_vectors, right_labels, _ = triple(right, r"\omega")
        left_arcs, right_arcs = angle_arcs(left), angle_arcs(right)
        self.show(left_vectors, left_labels, right_vectors, right_labels)
        self.at("rotation_ratios")
        relative = formula(
            r"\frac{d(1)}{c(1)}=\frac{d(\omega)}{c(\omega)},\qquad"
            r"\frac{g(1)}{c(1)}=\frac{g(\omega)}{c(\omega)}",
            size=41,
        ).move_to(UP * 1.9)
        self.show(relative, left_arcs, right_arcs)
        self.at("rotation_distinct")
        self.show(
            formula(r"d/c=-1\qquad g/c=i", size=38).move_to(LEFT * 3.85 + DOWN * 2.55),
            formula(r"d/c=-1\qquad g/c=i", size=38).move_to(RIGHT * 3.85 + DOWN * 2.55),
        )
        self.at("rotation_lambda")
        self.show(
            formula(r"\lambda=\frac{c(\omega)}{c(1)}", size=35, color=YELLOW).move_to(
                UP * 0.15
            )
        )
        self.show(
            Arrow(
                LEFT * 1.8 + DOWN * 0.8, RIGHT * 1.8 + DOWN * 0.8, buff=0.1
            ).set_color(YELLOW)
        )
        self.at("rotation_turn")
        self.play(
            Rotate(right_vectors, TAU / 3, about_point=right),
            Rotate(right_arcs, TAU / 3, about_point=right),
            run_time=2.5,
        )
        self.show(
            formula(r"\lambda=\omega\quad(+120^\circ)", size=32, color=YELLOW).move_to(
                DOWN * 1.75
            ),
            run_time=0.8,
        )
        self.at("rotation_reverse")
        self.show(
            formula(r"\Delta(c)=\lambda^{-1}\quad\text{(reverse)}", size=34).move_to(
                DOWN * 3.45
            ),
            run_time=0.8,
        )

        self.section("combination", "A fixed linear combination inherits the rotation")
        definition = formula(
            r"E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}",
            size=44,
        ).move_to(UP * 1.9)
        self.show(definition)
        radius = 1.05
        self.show(plane(left, radius), plane(right, radius))
        left_vectors, left_labels, left_pairs = triple(left, "1", radius=radius)
        right_vectors, right_labels, right_pairs = triple(
            right, r"\omega", angle=TAU / 3, radius=radius
        )
        self.show(left_vectors, left_labels, right_vectors, right_labels)
        self.at("combination_substitute")
        expansion = formula(
            r"E(\omega)=\frac{\lambda d(1)-\lambda c(1)}2"
            r"+\frac{\lambda g(1)-\lambda c(1)}{1+i}",
            size=35,
        ).move_to(UP * 0.85)
        self.show(expansion)
        self.at("combination_factor")
        self.play(
            Transform(
                expansion,
                formula(r"E(\omega)=\lambda E(1)", size=44, color=YELLOW).move_to(
                    expansion
                ),
            ),
            run_time=1.1,
        )
        left_e, left_e_label = value_arrow(left, VALUES["E"], "E", "1", radius)
        right_e, right_e_label = value_arrow(right, VALUES["E"], "E", r"\omega", radius)
        self.body.add(left_e, left_e_label, right_e, right_e_label)
        self.play(
            FadeIn(left_e),
            FadeIn(left_e_label),
            TransformFromCopy(left_e, right_e),
            FadeIn(right_e_label),
            run_time=1.1,
        )
        self.play(Rotate(right_e, TAU / 3, about_point=right), run_time=1.8)
        self.at("combination_schematic")
        schematic = formula(r"E(1)=-3+3i", size=34, color=BLUE_A).move_to(
            LEFT * 3.85 + DOWN * 2.55
        )
        self.show(schematic)
        outside_note = words(
            "E can lie outside the radius-three circle", size=23
        ).move_to(DOWN * 3.45)
        self.show(outside_note, run_time=0.8)

        self.wait_until_narration(self.cues["normalization"])
        self.play(FadeOut(definition), FadeOut(schematic), run_time=0.4)
        self.play(
            Transform(
                expansion,
                formula(
                    r"\frac{E(\omega)}{c(\omega)}=\frac{\lambda E(1)}{\lambda c(1)}",
                    size=43,
                ).move_to(UP * 1.8),
            ),
            run_time=0.8,
        )
        self.at("normalization_cancel")
        self.play(
            Rotate(right_vectors, -TAU / 3, about_point=right),
            Rotate(right_e, -TAU / 3, about_point=right),
            run_time=1.6,
        )
        for argument, pairs, e_label in [
            ("1", left_pairs, left_e_label),
            (r"\omega", right_pairs, right_e_label),
        ]:
            pairs["E"] = (left_e if argument == "1" else right_e, e_label)
            for name, (_vector, label) in pairs.items():
                target = formula(
                    rf"\frac{{{name}({argument})}}{{c({argument})}}",
                    size=25,
                    color=COLORS[name],
                )
                target.move_to(label)
                self.play(Transform(label, target), run_time=0.12)
        self.play(
            Transform(
                expansion,
                formula(
                    r"\boxed{\frac{E(\omega)}{c(\omega)}=\frac{E(1)}{c(1)}}",
                    size=44,
                    color=YELLOW,
                ).move_to(expansion),
            ),
            run_time=0.7,
        )
        self.at("normalization_value")
        self.show(
            formula(
                r"E(1)/c(1)=E(\omega)/c(\omega)=-1+i", size=36, color=BLUE_A
            ).move_to(DOWN * 2.75),
            run_time=0.8,
        )
        self.at("normalization_exact")
        self.play(
            Transform(
                outside_note,
                words(
                    "Exact cancellation before reduction · circle radius now 1",
                    size=23,
                    color=YELLOW,
                ).move_to(outside_note),
            ),
            run_time=0.8,
        )

        self.section("conflict", "Separate arithmetic requirements from the schematic")
        self.show(
            formula(r"E(P)\equiv J(P)=1+P+\cdots+P^8\pmod{1+i}", size=42).move_to(
                UP * 1.7
            )
        )
        self.show(
            words(
                "Required by the hypothetical Hadamard construction",
                size=25,
                color=BLUE_C,
            ).move_to(UP * 0.7)
        )
        self.at("conflict_requirements")
        left_box = box("At input 1: nonzero residue", LEFT * 3.6 + DOWN * 0.65)
        right_box = box("At input ω: zero residue", RIGHT * 3.6 + DOWN * 0.65)
        self.show(left_box, right_box)
        self.show(
            formula(r"E(1)\equiv1", size=43, color=YELLOW).move_to(
                LEFT * 3.6 + DOWN * 1.7
            ),
            formula(r"E(\omega)\equiv0", size=43, color=YELLOW).move_to(
                RIGHT * 3.6 + DOWN * 1.7
            ),
        )
        self.at("conflict_schematic")
        self.show(
            words(
                "Requirements, not residues measured from the schematic", size=24
            ).move_to(DOWN * 3.4),
            run_time=0.8,
        )
        self.at("conflict_unit")
        self.show(
            Arrow(
                LEFT * 1.05 + DOWN * 0.65, RIGHT * 1.05 + DOWN * 0.65, buff=0.05
            ).set_color(YELLOW),
            formula(r"\times\lambda", size=29, color=YELLOW).move_to(DOWN * 0.12),
            formula(
                r"\lambda\text{ is a unit}\quad\Longrightarrow\quad\lambda\cdot1\ne0",
                size=38,
            ).move_to(DOWN * 2.6),
        )
        self.at("conflict_next")
        self.play(FlashAround(right_box, color=YELLOW), run_time=0.8)

        self.section("general", "The general statement compares alternating products")
        self.show(
            box("u = 3: two inputs", LEFT * 3.65 + UP * 1.5),
            box("Several distinct primes", RIGHT * 3.65 + UP * 1.5),
        )
        self.show(
            formula(r"\Delta(f)=\frac{f(1)}{f(\omega)}", size=43).move_to(
                LEFT * 3.65 + DOWN * 0.25
            )
        )
        self.at("general_products")
        self.show(
            formula(r"I=\{p:p\mid u\}", size=28).move_to(RIGHT * 3.65 + UP * 0.65),
            run_time=0.5,
        )
        self.show(
            formula(
                r"\Delta(f)=\prod_{S\subseteq I}f(\zeta_S)^{(-1)^{|S|}}", size=37
            ).move_to(RIGHT * 3.65 + DOWN * 0.25)
        )
        self.show(
            formula(
                r"R=\frac{\Delta(d)}{\Delta(c)}=1,\qquad "
                r"W=\frac{\Delta(g)}{\Delta(c)}=1",
                size=46,
                color=YELLOW,
            ).move_to(DOWN * 1.85)
        )
        self.at("general_scope")
        self.show(
            words("Two-circle rotation: the u = 3 illustration", size=26).move_to(
                DOWN * 2.9
            )
        )
        self.show(
            words(
                "The deeper nodes develop the general product argument",
                size=23,
                color=BLUE_C,
            ).move_to(DOWN * 3.55),
            run_time=0.8,
        )
