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
    GrowArrow,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class DeltaOddOrder(NodeScene):
    node_id = "delta-odd-order"
    title = "4.6 · Why the Order Is Odd"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def copy_to(self, source, target, run_time=1):
        self.body.add(target)
        self.play(TransformFromCopy(source, target), run_time=run_time)

    def erase(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.35)
        self.body.remove(*objects)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/delta-odd-order.json").read_text()
        )["detail_cues"]
        self.section("order", "Remove the part of the order divisible by p")
        self.show(
            formula(r"\Delta(f)\text{ is a root of unity}", size=42).move_to(UP * 1.9),
            formula(
                r"\Delta(f)\equiv1\quad\text{above every }p\mid u", size=36
            ).move_to(UP * 0.85),
        )
        self.at("local_argument")
        self.erase(*list(self.body))
        self.show(
            words("Local domain · residue characteristic p", size=29).move_to(UP * 2),
            formula(r"\xi\equiv1\pmod{\mathfrak m}", size=44, color=BLUE_C).move_to(
                UP * 0.8
            ),
        )
        self.at("split_order")
        order = (
            VGroup(
                formula(r"\operatorname{ord}(\xi)=", size=47),
                formula(r"p^a", size=47, color=BLUE_C),
                formula("m", size=47, color=YELLOW),
            )
            .arrange(RIGHT, buff=0.3)
            .move_to(DOWN * 0.5)
        )
        self.show(order, formula(r"a\ge0,\qquad p\nmid m", size=35).move_to(DOWN * 1.6))
        self.at("raise_root")
        eta = formula(r"\eta=\xi^{p^a}", size=47, color=YELLOW).move_to(
            LEFT * 3.1 + DOWN * 2.8
        )
        self.copy_to(order, eta)
        self.at("eta_order")
        self.show(
            formula(r"\operatorname{ord}(\eta)=m,\qquad\eta\equiv1", size=39).move_to(
                RIGHT * 2.8 + DOWN * 2.8
            ),
            run_time=0.9,
        )

        self.section("geometric", "The exact geometric sum must vanish")
        self.show(
            formula(r"m>1\quad\Longrightarrow\quad\eta\ne1", size=42).move_to(UP * 2)
        )
        self.at("geometric_identity")
        identity = formula(r"\eta^m-1=(\eta-1)\sum_{j=0}^{m-1}\eta^j", size=48).move_to(
            UP * 0.35
        )
        self.show(identity)
        self.at("eta_power")
        self.play(
            Transform(
                identity,
                formula(r"0=(\eta-1)\sum_{j=0}^{m-1}\eta^j", size=48).move_to(identity),
            ),
            run_time=1,
        )
        self.at("domain_cancel")
        self.show(
            words("Domain · η − 1 is nonzero", size=28, color=BLUE_C).move_to(
                DOWN * 1.1
            )
        )
        vanishes = formula(r"\sum_{j=0}^{m-1}\eta^j=0", size=47, color=YELLOW)
        vanishes.move_to(DOWN * 2.6)
        self.copy_to(identity, vanishes)
        self.at("polygon")
        self.erase(*list(self.body))
        center = LEFT * 4.3 + DOWN * 0.15
        vertices = [0j]
        for j in range(5):
            vertices.append(vertices[-1] + complex(cos(TAU * j / 5), sin(TAU * j / 5)))
        vertices[-1] = vertices[0]
        middle = sum(vertices[:-1]) / 5
        points = [
            center + 1.45 * ((z - middle).real * RIGHT + (z - middle).imag * UP)
            for z in vertices
        ]
        arrows = VGroup(
            *(
                Arrow(a, b, buff=0).set_color(BLUE_C)
                for a, b in zip(points, points[1:], strict=False)
            )
        )
        self.body.add(arrows)
        for arrow in arrows:
            self.play(GrowArrow(arrow), run_time=0.3)
        self.show(
            formula(r"\sum_{j=0}^{4}\eta^j=0", size=42).move_to(RIGHT * 3.1 + UP * 0.3),
            words("Complex illustration: m = 5", size=26).move_to(
                LEFT * 4.3 + DOWN * 2.5
            ),
            words(
                "Local reduction is a separate calculation", size=28, color=YELLOW
            ).move_to(DOWN * 3.55),
            run_time=0.9,
        )

        self.section(
            "reduction", "A residue-one sum cannot vanish when p does not divide m"
        )
        original = formula(r"\sum_{j=0}^{m-1}\eta^j=0", size=46, color=BLUE_C).move_to(
            UP * 1.9
        )
        self.show(original)
        self.at("each_one")
        self.show(
            formula(
                r"\eta\equiv1\quad\Longrightarrow\quad\eta^j\equiv1", size=40
            ).move_to(UP * 0.6)
        )
        reduced = formula(
            r"\sum_{j=0}^{m-1}1=\overline m", size=48, color=YELLOW
        ).move_to(DOWN * 0.9)
        self.copy_to(original, reduced)
        self.at("m_nonzero")
        self.show(
            formula(
                r"p\nmid m\quad\Longrightarrow\quad\overline m\ne0",
                size=42,
                color=YELLOW,
            ).move_to(DOWN * 2.3),
            words("Contradiction to the reduced vanishing sum", size=27).move_to(
                DOWN * 3.5
            ),
            run_time=1,
        )
        self.at("m_one")
        self.erase(*list(self.body))
        self.show(
            formula(
                r"\boxed{m=1,\qquad\operatorname{ord}(\xi)=p^a}", size=49, color=YELLOW
            ).move_to(UP * 0.4),
            words("Order 1 is allowed: a = 0", size=29).move_to(DOWN * 1.4),
        )

        self.section("application", "Use the restriction above every prime dividing u")
        self.show(
            formula(r"u>1\text{ odd},\qquad p\mid u", size=42).move_to(UP * 2),
            formula(
                r"\Delta(f)\equiv1\pmod{\mathfrak m},\qquad\mathfrak m\ni p",
                size=42,
                color=BLUE_C,
            ).move_to(UP * 0.65),
        )
        self.at("primes_exist")
        self.show(
            formula(
                r"0\ne B\text{ finite free over }\mathbb Z"
                r"\quad\Longrightarrow\quad B/pB\ne0",
                size=35,
            ).move_to(DOWN * 0.7),
            words("A maximal ideal above p exists", size=27).move_to(DOWN * 1.7),
        )
        self.at("delta_power")
        self.show(
            formula(
                r"\operatorname{ord}(\Delta(f))=p^{a_p}\quad\text{for every }p\mid u",
                size=43,
                color=YELLOW,
            ).move_to(DOWN * 2.7)
        )
        self.at("odd_order")
        self.show(
            words("Every p is odd → the order is odd", size=29, color=YELLOW).move_to(
                DOWN * 3.6
            ),
            run_time=0.7,
        )

        self.section("two_primes", "Two distinct prime restrictions leave only one")
        self.show(formula(r"p,q\mid u,\qquad p\ne q", size=44).move_to(UP * 2))
        p_powers = formula(
            r"\{p^a:a\in\mathbb Z_{\ge0}\}", size=42, color=BLUE_C
        ).move_to(LEFT * 3.7 + UP * 0.4)
        q_powers = formula(
            r"\{q^b:b\in\mathbb Z_{\ge0}\}", size=42, color=BLUE_C
        ).move_to(RIGHT * 3.7 + UP * 0.4)
        self.show(p_powers, q_powers)
        self.at("common_one")
        one = formula(r"\{1\}", size=60, color=YELLOW).move_to(DOWN * 1)
        self.copy_to(VGroup(p_powers, q_powers), one)
        self.show(
            formula(
                r"\operatorname{ord}(\Delta(f))=1\quad\Longrightarrow\quad\Delta(f)=1",
                size=39,
            ).move_to(DOWN * 2.3)
        )
        self.at("one_prime_case")
        self.show(
            words(
                "One prime divisor can leave a nontrivial rotation",
                size=28,
                color=BLUE_C,
            ).move_to(DOWN * 3.5),
            run_time=0.8,
        )

        self.section("field", "For u = 3, the field leaves three possible directions")
        self.show(
            formula(
                r"\Delta(f)\in\mathbb Q(i,\omega),\qquad"
                r"\operatorname{ord}(\Delta(f))=3^a",
                size=43,
            ).move_to(UP * 1.9),
            formula(
                r"[\mathbb Q(i,\omega):\mathbb Q]=4", size=43, color=BLUE_C
            ).move_to(UP * 0.6),
        )
        self.at("ninth_degree")
        self.show(
            formula(
                r"[\mathbb Q(\zeta_9):\mathbb Q]=6>4", size=46, color=YELLOW
            ).move_to(DOWN * 0.7)
        )
        self.at("higher_degrees")
        self.show(
            formula(r"a\ge2:\quad\varphi(3^a)=2\cdot3^{a-1}\ge6", size=39).move_to(
                DOWN * 1.9
            ),
            run_time=0.9,
        )
        self.at("three_directions")
        self.show(
            formula(
                r"\boxed{\Delta(f)\in\{1,\omega,\omega^2\}}", size=50, color=YELLOW
            ).move_to(DOWN * 3.1)
        )

        self.section("example", "Odd order permits a nonzero phase")
        center = LEFT * 4.6 + DOWN * 0.2
        radius = 1.3
        circle = Circle(radius=radius).set_color(BLUE_C).move_to(center)
        dots = VGroup()
        labels = VGroup()
        for j, label in enumerate(["1", r"\omega", r"\omega^2"]):
            direction = cos(TAU * j / 3) * RIGHT + sin(TAU * j / 3) * UP
            point = center + radius * direction
            dots.add(Dot(point, radius=0.07).set_color(BLUE_C))
            labels.add(formula(label, size=34).next_to(dots[-1], direction, buff=0.2))
        self.show(
            circle,
            dots,
            labels,
            formula(r"f(P)=3iP,\qquad ff^*=9", size=38).move_to(RIGHT * 2.8 + UP * 1.9),
        )
        self.at("example_values")
        self.show(
            formula(r"f(1)=3i,\qquad f(\omega)=3i\omega", size=38).move_to(
                RIGHT * 2.8 + UP * 0.6
            ),
            run_time=1,
        )
        self.at("example_quotient")
        quotient = formula(
            r"\Delta(f)=\frac{3i}{3i\omega}=\omega^{-1}=\omega^2", size=43, color=YELLOW
        ).move_to(RIGHT * 2.5 + DOWN * 1)
        self.show(quotient, run_time=1.1)
        self.play(FlashAround(dots[2], color=YELLOW), run_time=0.7)
        self.at("three_phases")
        self.show(
            formula(
                r"\Delta(c),\qquad\Delta(d),\qquad\Delta(g)\quad\text{have odd order}",
                size=38,
            ).move_to(DOWN * 2.8)
        )
        self.at("sign_handoff")
        self.show(
            words(
                "Node 6 combines odd order with their common signs",
                size=27,
                color=BLUE_C,
            ).move_to(DOWN * 3.6),
            run_time=0.7,
        )
