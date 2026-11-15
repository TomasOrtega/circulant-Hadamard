import json

from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    Arrow,
    FadeIn,
    FadeOut,
    Matrix,
    Rectangle,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, sign_matrix, words


class Theorem(NodeScene):
    node_id = "theorem"
    title = "8.5 · Only Orders One and Four"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def hide(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.35)
        self.body.remove(*objects)

    def task_panel(self, label, center):
        border = Rectangle(width=6.4, height=1.9).set_stroke(BLUE_C, width=1.5)
        label = words(label, size=27).move_to(UP * 0.25)
        pending = words("To verify", size=25, color=BLUE_C).move_to(DOWN * 0.4)
        return VGroup(border, label, pending).move_to(center)

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/theorem.json").read_text()
        )["detail_cues"]

        self.section("conclusion", "Complete the stated proof chain in both directions")
        theorem = VGroup(
            words("A real circulant Hadamard matrix exists", size=34),
            formula(r"\Longleftrightarrow\quad n\in\{1,4\}", size=53, color=YELLOW),
        ).arrange(DOWN, buff=0.35)
        theorem.move_to(UP * 0.95)
        frame = SurroundingRectangle(theorem, buff=0.3).set_color(BLUE_C)
        self.show(theorem, frame)
        self.at("both_directions")
        exclusion_task = self.task_panel(
            "Exclude every other order", LEFT * 3.5 + DOWN * 1.8
        )
        examples_task = self.task_panel(
            "Verify orders 1 and 4", RIGHT * 3.5 + DOWN * 1.8
        )
        self.show(exclusion_task, examples_task, run_time=1.0)

        self.section(
            "restriction", "Use the earlier restriction and general contradiction"
        )
        input_order = formula(r"n>1", size=49, color=BLUE_C).move_to(
            LEFT * 5.5 + UP * 1.5
        )
        self.show(input_order)
        self.at("order_restriction")
        restricted = VGroup(
            words("Node 2 · order restriction", size=25, color=BLUE_C),
            formula(r"n=4u^2", size=46),
            formula(r"u\in\mathbb Z_{>0}\text{ odd}", size=31),
        ).arrange(DOWN, buff=0.28)
        restricted.move_to(LEFT * 0.65 + UP * 0.85)
        restriction_border = SurroundingRectangle(restricted, buff=0.3).set_color(
            BLUE_C
        )
        first_arrow = Arrow(
            input_order.get_right(), restriction_border.get_left(), buff=0.2
        ).set_color(BLUE_C)
        self.show(first_arrow, restriction_border, restricted, run_time=1.0)
        self.at("general_exclusion")
        excluded = formula(r"u>1", size=43).move_to(RIGHT * 4.6 + UP * 1.2)
        excluded_label = words("Excluded by Node 8.4", size=24, color=BLUE_C)
        excluded_label.next_to(excluded, DOWN, buff=0.3)
        second_arrow = Arrow(
            restriction_border.get_right(), excluded.get_left(), buff=0.25
        ).set_color(BLUE_C)
        strike = Arrow(
            excluded.get_corner(DOWN + LEFT),
            excluded.get_corner(UP + RIGHT),
            buff=-0.1,
        ).set_color(YELLOW)
        self.show(second_arrow, excluded, excluded_label, run_time=0.9)
        self.show(strike, run_time=0.6)
        self.at("u_one")
        survivor = formula(r"u=1\quad\Longrightarrow\quad n=4", size=46, color=YELLOW)
        survivor.move_to(DOWN * 1.2)
        self.body.add(survivor)
        self.play(TransformFromCopy(restricted[1], survivor), run_time=1.1)
        self.at("order_one_bypass")
        separate = formula(r"n=1", size=45, color=BLUE_C).move_to(
            LEFT * 5.5 + DOWN * 2.65
        )
        bypass = words("Separate case · check directly", size=29).move_to(
            RIGHT * 1.35 + DOWN * 2.65
        )
        bypass_arrow = Arrow(separate.get_right(), bypass.get_left(), buff=0.3)
        bypass_arrow.set_color(BLUE_C)
        self.show(separate, bypass_arrow, bypass, run_time=1.0)

        self.section("one", "The order-one construction")
        single = Matrix([[1]]).scale(1.3)
        for entry in single.get_entries():
            entry.set_color(BLUE_C)
        single.move_to(LEFT * 3.8 + UP * 0.45)
        self.show(single)
        self.at("one_row_length")
        length = formula(r"1^2=1", size=47).move_to(RIGHT * 3.0 + UP * 1.0)
        self.show(length, run_time=0.9)
        self.at("no_distinct_rows")
        self.show(
            words("No distinct rows to compare", size=29).move_to(
                RIGHT * 2.5 + DOWN * 0.3
            ),
            run_time=0.9,
        )
        self.at("one_cyclic_shift")
        shifted = single.copy().move_to(LEFT * 3.8 + DOWN * 1.65)
        shift_arrow = Arrow(single.get_bottom(), shifted.get_top(), buff=0.15)
        shift_arrow.set_color(YELLOW)
        shift_label = words("Cyclic shift", size=25, color=YELLOW).next_to(
            shift_arrow, RIGHT, buff=0.25
        )
        self.body.add(shifted)
        self.play(TransformFromCopy(single, shifted), FadeIn(shift_arrow), run_time=1.1)
        self.body.add(shift_arrow)
        self.show(shift_label, run_time=0.5)
        self.at("one_gram")
        identity = formula(r"(1)(1)^{\mathsf T}=(1)=I_1", size=48, color=YELLOW)
        identity.move_to(RIGHT * 2.8 + DOWN * 1.9)
        self.show(identity, run_time=1.1)
        self.at("one_verified")
        self.show(
            words("Order 1 verified", size=30, color=YELLOW).move_to(DOWN * 3.2),
            run_time=0.8,
        )

        self.section("four", "The order-four construction")
        matrix = sign_matrix().move_to(LEFT * 3.7 + UP * 0.3)
        rows = matrix.get_rows()
        matrix_label = formula("H=", size=44, color=BLUE_C).next_to(
            matrix, LEFT, buff=0.4
        )
        self.body.add(matrix)
        self.play(FadeIn(matrix.get_brackets()), FadeIn(rows[0]), run_time=1.1)
        self.show(matrix_label, run_time=0.6)
        self.at("cyclic_right_shifts")
        shift_label = words("Cyclic right shifts", size=28, color=BLUE_C).move_to(
            RIGHT * 3.0 + UP * 1.15
        )
        self.show(shift_label, run_time=0.7)
        for r in range(1, 4):
            self.play(
                *(
                    TransformFromCopy(rows[r - 1][j], rows[r][(j + 1) % 4])
                    for j in range(4)
                ),
                run_time=1.0,
            )
        self.at("negative_positions")
        negative_frames = VGroup(
            *(
                SurroundingRectangle(rows[j][j], buff=0.1).set_color(YELLOW)
                for j in range(4)
            )
        )
        self.show(negative_frames, run_time=0.7)
        self.at("compare_rows")
        self.hide(negative_frames, shift_label)
        selected = VGroup(
            SurroundingRectangle(rows[0], buff=0.1).set_color(YELLOW),
            SurroundingRectangle(rows[1], buff=0.1).set_color(YELLOW),
        )
        self.show(selected, run_time=0.6)
        upper = rows[0].copy().scale(1.2).move_to(RIGHT * 3.4 + UP * 0.9)
        lower = rows[1].copy().scale(1.2).move_to(RIGHT * 3.4 + DOWN * 0.15)
        self.body.add(upper, lower)
        self.play(
            TransformFromCopy(rows[0], upper),
            TransformFromCopy(rows[1], lower),
            run_time=1.2,
        )
        comparison = VGroup(
            *(
                SurroundingRectangle(VGroup(upper[j], lower[j]), buff=0.12).set_color(
                    YELLOW if j < 2 else BLUE_C
                )
                for j in range(4)
            )
        )
        self.show(comparison, run_time=0.7)
        self.at("dot_product")
        dot_product = formula(
            r"(-1)(1)+(1)(-1)+(1)(1)+(1)(1)", size=33, width=7.3
        ).move_to(RIGHT * 3.4 + DOWN * 1.65)
        self.show(dot_product, run_time=1.0)
        self.at("zero_dot")
        zero_dot = formula(r"-1-1+1+1=0", size=43, color=YELLOW).move_to(dot_product)
        self.play(Transform(dot_product, zero_dot), run_time=0.6)
        general_pair = words(
            "Any distinct pair: two agreements, two disagreements", size=25, width=7.2
        ).move_to(RIGHT * 3.4 + DOWN * 2.85)
        self.show(general_pair, run_time=0.6)
        self.at("four_row_length")
        self.hide(selected, upper, lower, comparison, dot_product, general_pair)
        squared_length = formula(r"(-1)^2+1^2+1^2+1^2=4", size=39, width=7.2)
        squared_length.move_to(RIGHT * 3.4 + UP * 1.55)
        self.show(squared_length, run_time=0.9)
        self.at("gram_matrix")
        gram = Matrix(
            [[4 if r == c else 0 for c in range(4)] for r in range(4)],
            h_buff=0.65,
            v_buff=0.45,
        ).scale(0.8)
        gram.move_to(RIGHT * 3.4 + DOWN * 0.35)
        self.body.add(gram)
        self.play(FadeIn(gram.get_brackets()), run_time=0.4)
        diagonal = VGroup(*(gram.get_entries()[5 * j] for j in range(4)))
        off_diagonal = VGroup(
            *(entry for j, entry in enumerate(gram.get_entries()) if j % 5)
        )
        diagonal.set_color(YELLOW)
        off_diagonal.set_color(BLUE_C)
        self.play(
            TransformFromCopy(squared_length, diagonal),
            FadeIn(off_diagonal),
            run_time=1.3,
        )
        self.at("four_identity")
        self.show(
            formula(r"HH^{\mathsf T}=4I_4", size=47, color=YELLOW).move_to(DOWN * 2.75),
            run_time=1.0,
        )
        self.at("both_exist")
        self.hide(*list(self.body))
        checks = VGroup(
            words("Order 1 · verified", size=31, color=BLUE_C),
            words("Order 4 · verified", size=31, color=BLUE_C),
        ).arrange(RIGHT, buff=2.1)
        checks.move_to(UP * 1.55)
        self.show(checks, run_time=1.0)
        self.at("u_one_exception")
        exception = formula(r"n=4\ \Longleftrightarrow\ u=1", size=42).move_to(UP * 0.3)
        hypothesis = words(
            "The earlier Delta theorem assumes u > 1", size=29, color=BLUE_C
        ).move_to(DOWN * 0.75)
        self.show(exception, hypothesis, run_time=1.0)
        self.at("stated_inputs")
        final = formula(r"n\in\{1,4\}", size=58, color=YELLOW).move_to(DOWN * 2.25)
        final_frame = SurroundingRectangle(final, buff=0.25).set_color(YELLOW)
        self.show(final, final_frame, run_time=1.1)
        self.show(
            words("Using the stated inputs from the earlier nodes", size=27).move_to(
                DOWN * 3.45
            ),
            run_time=0.7,
        )
