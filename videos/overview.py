from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    PI,
    RIGHT,
    UP,
    YELLOW,
    Arrow,
    FlashAround,
    RoundedRectangle,
    SurroundingRectangle,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import NodeScene, formula, sign_matrix, words


class Overview(NodeScene):
    node_id = "overview"
    title = "The circulant Hadamard conjecture"

    def present(self):
        self.section("matrix", "A special four-by-four matrix")
        matrix = sign_matrix().shift(LEFT * 2.6 + DOWN * 0.2)
        self.show(matrix)
        self.show(
            words("Entries are +1 or −1", size=28).move_to(RIGHT * 2.8 + UP * 0.6)
        )
        diagonal = VGroup(*(matrix.get_rows()[i][i] for i in range(4)))
        self.play(FlashAround(diagonal, color=YELLOW), run_time=1)

        self.wait_until_narration(self.cues["orthogonality"])
        rows = VGroup(
            SurroundingRectangle(matrix.get_rows()[0], color=YELLOW),
            SurroundingRectangle(matrix.get_rows()[1], color=YELLOW),
        )
        self.show(rows)
        dot = formula(r"-1-1+1+1=0", size=37)
        dot.move_to(RIGHT * 2.8 + DOWN * 0.4)
        self.show(dot)
        self.show(
            formula(r"HH^{\mathsf T}=4I_4", color=BLUE_C, size=40).move_to(
                RIGHT * 2.8 + DOWN * 1.6
            )
        )

        self.section("hadamard", "Hadamard means orthogonal sign rows")
        self.show(
            self.stack(
                formula(r"h_{rj}\in\{-1,1\}", color=BLUE_C),
                formula(r"\langle r,s\rangle=0\quad(r\ne s)"),
                formula(r"HH^{\mathsf T}=nI_n", color=YELLOW),
            )
        )

        self.section("dimensions", "The general Hadamard question")
        self.show(
            self.stack(
                formula(r"n=1,\ 2,\ 4,\ 8,\ 12,\ 16,\ 20,\ldots"),
                words("For n > 2, divisibility by four is necessary."),
                words("Hadamard conjecture: every multiple of four works.", size=26),
            )
        )

        self.section("cyclic", "One row determines the whole matrix")
        matrix = sign_matrix().shift(LEFT * 2.7 + DOWN * 0.3)
        self.show(matrix)
        self.show(
            words("Shift one place to the right", size=26).move_to(
                RIGHT * 2.6 + UP * 1
            ),
            formula(r"(-1,1,1,1)\longmapsto(1,-1,1,1)", size=30, width=6).move_to(
                RIGHT * 2.6
            ),
        )
        for index in range(1, 4):
            before = matrix.get_rows()[index - 1]
            after = matrix.get_rows()[index]
            targets = [after[(j + 1) % 4].copy().set_color(YELLOW) for j in range(4)]
            self.play(
                *(
                    TransformFromCopy(
                        before[j],
                        targets[j],
                        path_arc=-PI / 2 if j == 3 else 0,
                    )
                    for j in range(4)
                ),
                run_time=1,
            )
            self.remove(*targets)
        self.show(
            words("Circulant", size=34, color=BLUE_C).move_to(RIGHT * 2.6 + DOWN * 1.2)
        )

        self.section("conjecture", "Add cyclic symmetry")
        self.show(
            self.stack(
                words("Circulant + Hadamard", size=38, color=BLUE_C),
                formula(r"n\in\{1,4\}", size=76, color=YELLOW),
                words("Our goal: understand the algebraic proof route.", size=25),
                words("Order restriction and Δ-theorem are accepted inputs.", size=23),
            )
        )

        self.section("roadmap", "Eight components of the proof")
        labels = [
            "Group-ring encoding",
            "Order restriction",
            "Three evaluations",
            "Δ-theorem",
            "Signs become all ones",
            "Odd-order rigidity",
            "Products to sums",
            "Final contradiction",
        ]
        locations = [
            (-4.5, 1.5),
            (-4.5, 0.2),
            (-4.5, -1.1),
            (0, 1.5),
            (0, -1.1),
            (4.5, 0.2),
            (4.5, -1.1),
            (4.5, -2.4),
        ]
        cards = VGroup()
        for number, (label, (x, y)) in enumerate(
            zip(labels, locations, strict=True), 1
        ):
            box = RoundedRectangle(width=3.7, height=0.85, corner_radius=0.12)
            box.set_stroke(BLUE_C, width=2).set_fill("#101b2b", opacity=1)
            text = words(f"{number}. {label}", size=20, width=3.4)
            cards.add(VGroup(box, text).move_to(RIGHT * x + UP * y))
        edges = VGroup()
        for source, target in [
            (0, 1),
            (1, 2),
            (2, 4),
            (2, 5),
            (3, 5),
            (4, 5),
            (4, 6),
            (5, 6),
            (4, 7),
            (6, 7),
        ]:
            start = cards[source]
            end = cards[target]
            direction = end.get_center() - start.get_center()
            edges.add(
                Arrow(
                    start.get_boundary_point(direction),
                    end.get_boundary_point(-direction),
                    buff=0.08,
                    stroke_width=2,
                    fill_color=BLUE_C,
                )
            )
        self.show(edges, cards, run_time=1.2)
        summary = None
        steps = [
            ("encoding", r"h(X)h^*(X)=n"),
            ("order", r"n=4u^2,\quad u\text{ odd}"),
            ("evaluations", r"Z=1,-1,i\quad\longmapsto\quad c,d,g"),
            ("delta", r"\Delta(f)\text{ has odd order}"),
            ("signs", r"E(P)\equiv1+P+\cdots+P^{u^2-1}\pmod{1+i}"),
            ("rigidity", r"R=W=1"),
            ("sums", r"\mathcal S\equiv0\pmod{1+i}"),
            ("contradiction", r"\mathcal S\equiv1\pmod{1+i}"),
        ]
        for index, (cue, expression) in enumerate(steps):
            self.wait_until_narration(self.cues[cue])
            if index:
                cards[index - 1][0].set_stroke(BLUE_C)
            if summary is not None:
                self.remove(summary)
            summary = formula(expression, size=34, width=7.5)
            summary.move_to(LEFT * 2.2 + DOWN * 2.9)
            self.show(summary, run_time=0.5)
            self.play(FlashAround(cards[index], color=YELLOW), run_time=0.7)
            self.play(cards[index][0].animate.set_stroke(YELLOW), run_time=0.4)

        self.section("conclusion", "An odd number of ones cannot cancel")
        self.show(
            self.stack(
                formula(r"\mathcal S\equiv0\pmod{1+i}", color=BLUE_C),
                formula(r"\mathcal S\equiv1\pmod{1+i}", color=YELLOW),
                words("Contradiction for odd u > 1", size=31),
                formula(r"\boxed{n=1\ \text{or}\ n=4}", size=60),
            )
        )
