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
    FlashAround,
    Rectangle,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class GaussianParity(NodeScene):
    node_id = "gaussian-parity"
    title = "5.2 · Gaussian Parity"

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
            (ROOT / "videos/production/gaussian-parity.json").read_text()
        )["detail_cues"]

        self.section("division", "Test divisibility in the Gaussian integers")
        self.show(
            formula(r"z=a+bi,\qquad a,b\in\mathbb Z", size=47, color=BLUE_C).move_to(
                UP * 1.9
            ),
            run_time=1,
        )
        self.at("division_difference")
        congruence = formula(
            r"z\equiv w\pmod{1+i}\quad\Longleftrightarrow\quad "
            r"z-w=(1+i)k,\quad k\in\mathbb Z[i]",
            size=36,
            width=15,
        ).move_to(UP * 0.65)
        self.show(congruence, run_time=1.2)
        self.at("division_multiply")
        quotient = formula(r"\frac{a+bi}{1+i}", size=56).move_to(DOWN * 1.2)
        self.show(quotient, run_time=0.9)
        multiplied = formula(
            r"\frac{(a+bi)(1-i)}{(1+i)(1-i)}", size=53, color=BLUE_C
        ).move_to(quotient)
        self.play(Transform(quotient, multiplied), run_time=1)
        self.at("division_denominator")
        denominator_two = formula(r"\frac{(a+bi)(1-i)}{2}", size=56).move_to(quotient)
        self.play(Transform(quotient, denominator_two), run_time=1)
        self.at("division_collect")
        parts = VGroup(
            formula(r"\frac{a+b}{2}", size=57, color=YELLOW),
            formula("+", size=50),
            formula(r"i\frac{b-a}{2}", size=57, color=YELLOW),
        ).arrange(RIGHT, buff=0.35)
        parts.move_to(quotient)
        self.body.add(parts)
        self.play(TransformFromCopy(quotient, parts), FadeOut(quotient), run_time=1.2)
        self.body.remove(quotient)
        self.show(
            words("Real part", size=26).next_to(parts[0], DOWN, buff=0.45),
            words("Imaginary part", size=26).next_to(parts[2], DOWN, buff=0.45),
            run_time=0.8,
        )

        self.section("parities", "Both halves must be integers")
        halves = formula(
            r"\frac{a+b}{2},\qquad\frac{b-a}{2}", size=53, color=BLUE_C
        ).move_to(UP * 1.8)
        self.show(halves, run_time=1)
        headers = VGroup(
            words("a", size=29).move_to(LEFT * 4.4 + UP * 0.6),
            words("b", size=29).move_to(LEFT * 1.2 + UP * 0.6),
            words("Both halves", size=29).move_to(RIGHT * 3.4 + UP * 0.6),
        )
        self.show(headers, run_time=0.8)
        rows = []
        for a, b, result, y in [
            ("even", "even", "integers", -0.25),
            ("odd", "odd", "integers", -1.1),
            ("even", "odd", "nonintegers", -1.95),
            ("odd", "even", "nonintegers", -2.8),
        ]:
            row = VGroup(
                words(a, size=29).move_to(LEFT * 4.4 + UP * y),
                words(b, size=29).move_to(LEFT * 1.2 + UP * y),
                words(result, size=29, color=YELLOW).move_to(RIGHT * 3.4 + UP * y),
            )
            rows.append(row)
        self.at("parities_even")
        self.show(rows[0], run_time=0.7)
        self.at("parities_odd")
        self.show(rows[1], run_time=0.7)
        self.at("parities_different")
        self.show(rows[2], rows[3], run_time=0.9)
        self.at("parities_criterion")
        self.erase(headers, *rows)
        criterion = formula(
            r"(1+i)\mid(a+bi)\quad\Longleftrightarrow\quad a+b\text{ is even}",
            size=45,
            color=YELLOW,
            width=14,
        ).move_to(DOWN * 0.6)
        self.show(criterion, run_time=1)
        self.show(SurroundingRectangle(criterion, buff=0.25).set_stroke(YELLOW, 2))

        self.section("map", "Two residues, determined by one parity")
        self.show(
            formula(
                r"\mathbb Z[i]/(1+i)\cong\mathbb F_2", size=52, color=BLUE_C
            ).move_to(UP * 1.8),
            run_time=1,
        )
        self.at("map_define")
        mapping = formula(r"\varphi(a+bi)=a+b\pmod2", size=46).move_to(UP * 0.65)
        self.show(mapping, run_time=1)
        examples = []
        for source, total, residue, y in [
            ("3+i", "4", "0", -0.75),
            ("3+2i", "5", "1", -2.1),
        ]:
            example = VGroup(
                formula(source, size=48, color=BLUE_C).move_to(LEFT * 4.6 + UP * y),
                formula(total, size=48).move_to(UP * y),
                formula(residue, size=54, color=YELLOW).move_to(RIGHT * 4.3 + UP * y),
            )
            examples.append(example)
        for cue, example in zip(
            ["map_example_zero", "map_example_one"], examples, strict=True
        ):
            self.at(cue)
            self.show(example[0], run_time=0.5)
            self.copy_to(example[0], example[1], run_time=0.7)
            self.show(
                Arrow(
                    example[0].get_right(), example[1].get_left(), buff=0.3
                ).set_color(BLUE_C),
                run_time=0.4,
            )
            self.copy_to(example[1], example[2], run_time=0.7)
            self.show(
                Arrow(
                    example[1].get_right(), example[2].get_left(), buff=0.3
                ).set_color(YELLOW),
                run_time=0.4,
            )
        self.at("map_scope")
        self.show(
            words("Arithmetic reduction · not a complex rotation", size=27).move_to(
                DOWN * 3.5
            ),
            run_time=0.8,
        )

        self.section("homomorphism", "The parity rule respects the ring operations")
        self.show(
            formula(
                r"\varphi(z+w)=\varphi(z)+\varphi(w)", size=44, color=BLUE_C
            ).move_to(UP * 1.8),
            run_time=1,
        )
        self.at("homomorphism_product")
        product = formula(r"(a+bi)(c+di)=(ac-bd)+i(ad+bc)", size=43, width=14).move_to(
            UP * 0.35
        )
        self.show(product, run_time=1.2)
        self.at("homomorphism_modtwo")
        reduced = formula(
            r"ac-bd+ad+bc\equiv(a+b)(c+d)\pmod2", size=42, color=YELLOW, width=14
        ).move_to(DOWN * 1.1)
        self.copy_to(product, reduced, run_time=1)
        self.show(
            formula(r"\varphi(zw)=\varphi(z)\varphi(w)", size=43, color=BLUE_C).move_to(
                DOWN * 2.25
            ),
            run_time=0.9,
        )
        self.at("homomorphism_onto")
        self.show(
            formula(
                r"\operatorname{im}\varphi=\mathbb F_2,\qquad"
                r"\ker\varphi=(1+i)\mathbb Z[i]",
                size=34,
            ).move_to(DOWN * 3.5),
            run_time=1,
        )

        self.section("units", "Both signs and all four Gaussian units reduce to one")
        sources = VGroup(
            *(
                formula(label, size=46, color=BLUE_C).move_to(LEFT * 3.7 + UP * y)
                for label, y in zip(
                    ["1", "-1", "i", "-i"], [1.7, 0.55, -0.6, -1.75], strict=True
                )
            )
        )
        one = formula("1", size=70, color=YELLOW).move_to(RIGHT * 3.2 + UP * 0.1)
        self.show(sources, one, run_time=1)
        self.show(
            *(
                Arrow(source.get_right(), one.get_left(), buff=0.3).set_color(BLUE_C)
                for source in sources
            ),
            run_time=1.1,
        )
        self.at("units_identity")
        self.erase(
            sources, one, *(obj for obj in list(self.body) if isinstance(obj, Arrow))
        )
        identities = VGroup(
            formula(r"i-1=i(1+i)", size=48).move_to(UP * 1.5),
            formula(r"2=(1+i)(1-i)", size=48).move_to(UP * 0.1),
        )
        self.show(identities, run_time=1.2)
        self.at("units_signs")
        self.show(
            formula(
                r"\boxed{i\equiv-1\equiv1\pmod{1+i}}", size=49, color=YELLOW
            ).move_to(DOWN * 1.6),
            words("Arithmetic residues", size=26, color=BLUE_C).move_to(DOWN * 3.3),
            run_time=1,
        )

        self.section("polynomials", "Change coefficients; keep the cycle relation")
        self.show(
            formula(r"u\in\mathbb Z_{>0}", size=41, color=BLUE_C).move_to(UP * 2.05),
            run_time=0.8,
        )
        self.at("polynomials_apply")
        rings = formula(
            r"\mathbb Z[i][P]/(P^{u^2}-1)\ \longrightarrow\ "
            r"\mathbb F_2[P]/(P^{u^2}-1)",
            size=40,
            width=15,
        ).move_to(UP * 0.9)
        self.show(rings, run_time=1)
        self.at("polynomials_powers")
        relation = formula(
            r"P^{u^2}=1\quad\longmapsto\quad P^{u^2}=1", size=42
        ).move_to(DOWN * 0.4)
        self.show(relation, run_time=0.9)
        self.at("polynomials_only")
        self.show(
            words("Reduce every coefficient; retain the powers of P", size=28).move_to(
                DOWN * 1.65
            ),
            run_time=0.8,
        )
        self.at("polynomials_example")
        example = (
            VGroup(
                formula("i", size=48, color=BLUE_C),
                formula("-", size=48),
                formula("P", size=48),
            )
            .arrange(RIGHT, buff=0.2)
            .move_to(DOWN * 2.75)
        )
        reduced = VGroup(
            formula("1", size=48, color=YELLOW).move_to(example[0]),
            formula("+", size=48, color=YELLOW).move_to(example[1]),
            formula("P", size=48).move_to(example[2]),
        )
        self.show(example, run_time=0.7)
        self.play(Transform(example, reduced), run_time=1.2)
        self.at("polynomials_uone")
        self.play(FlashAround(relation, color=YELLOW), run_time=0.8)
        self.show(
            formula(r"u=1:\quad P=1,\quad1+P=0\text{ in }\mathbb F_2", size=27).move_to(
                DOWN * 3.6
            ),
            run_time=0.7,
        )

        self.section("ordering", "Form exact integral quotients, then reduce")
        first = Rectangle(width=6.1, height=1.35).move_to(LEFT * 4.15 + UP * 0.9)
        first.set_stroke(BLUE_C, 2)
        first_label = words("Form integral quotients", size=29).move_to(first)
        second = Rectangle(width=6.1, height=1.35).move_to(RIGHT * 3.9 + UP * 0.9)
        second.set_stroke(YELLOW, 2)
        second_label = words("Reduce coefficients", size=29).move_to(second)
        self.at("ordering_exact")
        self.show(first, first_label, run_time=1)
        self.at("ordering_reduce")
        self.show(
            Arrow(first.get_right(), second.get_left(), buff=0.15).set_color(BLUE_C),
            second,
            second_label,
            run_time=1,
        )
        self.at("ordering_zero")
        self.show(
            formula(
                r"2\equiv0,\qquad1+i\equiv0\pmod{1+i}", size=39, color=YELLOW
            ).move_to(DOWN * 0.7),
            words("No division by these zero residues", size=28).move_to(DOWN * 1.85),
            run_time=1,
        )
        self.at("ordering_outputs")
        self.show(
            formula(
                r"i-1\equiv0,\qquad+1\equiv-1\equiv1\pmod{1+i}",
                size=40,
                color=BLUE_C,
                width=14,
            ).move_to(DOWN * 3.3),
            run_time=1,
        )
