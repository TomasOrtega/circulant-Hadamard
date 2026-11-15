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
    LaggedStart,
    Rectangle,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    VGroup,
)

from videos.node_scene import ROOT, NodeScene, formula, words


class FourSignPolynomials(NodeScene):
    node_id = "four-sign-polynomials"
    title = "3.2 · Four Sign Polynomials"

    def at(self, key):
        self.wait_until_narration(self.details[key])

    def present(self):
        self.details = json.loads(
            (ROOT / "videos/production/four-sign-polynomials.json").read_text()
        )["detail_cues"]

        self.section("coordinates", "Four powers of Z · keep the P coordinate")
        relation = formula(r"Z^4=1", size=63, color=BLUE_C).move_to(UP * 1.7)
        self.show(relation)
        self.at("four_powers")
        powers = formula(r"1,\quad Z,\quad Z^2,\quad Z^3", size=56).move_to(UP * 0.35)
        self.show(powers)
        self.at("generic_term")
        term = formula(r"h_{a,b}Z^aP^b", size=66, color=YELLOW).move_to(DOWN * 1.05)
        self.show(term)
        self.at("indices")
        self.show(
            formula(r"0\le a<4,\qquad 0\le b<u^2", size=39).move_to(DOWN * 2.4),
            formula(r"h_{a,b}\in\{-1,1\}", size=37, color=BLUE_C).move_to(DOWN * 3.25),
        )

        self.section("group", "Group by the Z power without changing a coefficient")
        caption = words(
            "Representative terms (u > 1) · omitted P powers continue", size=25
        )
        caption.move_to(DOWN * 3.1)
        self.show(caption, run_time=0.65)
        columns = VGroup(*(VGroup() for _ in range(4)))
        order = [(2, 1), (0, 0), (3, 0), (1, 1), (1, 0), (3, 1), (0, 1), (2, 0)]
        x_positions = [-5.25, -1.75, 1.75, 5.25]
        targets = {}
        for index, (a, b) in enumerate(order):
            item = VGroup(
                formula(rf"h_{{{a},{b}}}", size=29, color=BLUE_C),
                formula(rf"Z^{a}", size=29, color=YELLOW),
                formula(rf"P^{b}", size=29, color=BLUE_C),
            ).arrange(RIGHT, buff=0.05)
            item.move_to(RIGHT * x_positions[index % 4] + UP * (0.4 - index // 4 * 1.2))
            columns[a].add(item)
            targets[a, b] = RIGHT * x_positions[a] + UP * (0.4 - b * 1.2)
        self.show(columns, run_time=1.3)
        labels = VGroup(
            *(
                formula("1" if a == 0 else rf"Z^{a}", size=41, color=YELLOW).move_to(
                    RIGHT * x + UP * 1.65
                )
                for a, x in enumerate(x_positions)
            )
        )
        boxes = VGroup(
            *(
                Rectangle(width=3.15, height=2.7)
                .move_to(RIGHT * x + DOWN * 0.3)
                .set_stroke(BLUE_C, width=1.5)
                for x in x_positions
            )
        )
        self.at("sort")
        self.show(labels, boxes, run_time=0.7)
        self.play(
            LaggedStart(
                *(
                    item.animate.move_to(targets[a, b])
                    for a, column in enumerate(columns)
                    for item, b in sorted(
                        zip(
                            column,
                            [pair[1] for pair in order if pair[0] == a],
                            strict=True,
                        ),
                        key=lambda pair: pair[1],
                    )
                ),
                lag_ratio=0.08,
            ),
            run_time=3,
        )

        self.wait_until_narration(self.cues["define"])
        self.play(FadeOut(boxes), FadeOut(caption), run_time=0.5)
        self.body.remove(boxes, caption)
        targets_h = [
            formula(rf"H_{a}(P)", size=39, color=BLUE_C).move_to(
                RIGHT * x_positions[a] + DOWN * 0.25
            )
            for a in range(4)
        ]
        self.at("name_H")
        self.play(
            *(
                Transform(column, target)
                for column, target in zip(columns, targets_h, strict=True)
            ),
            run_time=1.5,
        )
        definition = formula(r"H_a(P)=\sum_{b=0}^{u^2-1}h_{a,b}P^b", size=44)
        definition.move_to(UP * 1.9)
        self.play(
            *(
                label.animate.move_to(RIGHT * x + UP * 0.65)
                for label, x in zip(labels, x_positions, strict=True)
            ),
            run_time=0.7,
        )
        self.show(definition)
        self.at("decomposition")
        decomposition = formula(
            r"h(Z,P)=H_0(P)+ZH_1(P)+Z^2H_2(P)+Z^3H_3(P)",
            size=40,
            color=YELLOW,
            width=14,
        ).move_to(DOWN * 2.1)
        self.body.add(decomposition)
        self.play(TransformFromCopy(columns, decomposition), run_time=1.7)
        self.show(
            words("The common Z powers stay outside each H.", size=26).move_to(
                DOWN * 3.2
            )
        )

        self.section("unique", "The basis positions and their signs are unchanged")
        self.show(
            formula(r"\{Z^aP^b:0\le a<4,\ 0\le b<u^2\}", size=45, color=BLUE_C).move_to(
                UP * 1.8
            ),
            words("An integer basis · one coefficient per position", size=27).move_to(
                UP * 0.75
            ),
        )
        expansion = formula(r"H_2(P)", size=58, color=BLUE_C).move_to(DOWN * 0.5)
        self.at("reexpand")
        self.show(expansion)
        self.play(
            Transform(
                expansion,
                formula(
                    r"H_2(P)=\sum_{b=0}^{u^2-1}h_{2,b}P^b",
                    size=44,
                    width=13,
                ).move_to(expansion),
            ),
            run_time=1.5,
        )
        self.at("same_signs")
        self.show(
            formula(
                r"h_{2,b}\in\{-1,1\}\quad\text{for every }b", size=43, color=YELLOW
            ).move_to(DOWN * 1.85),
            words("Regrouping uses no norm calculation.", size=27).move_to(DOWN * 3.0),
        )

        self.section("column", "Order 36 · four rows of nine symbolic coefficients")
        self.show(formula(r"u=3,\qquad u^2=9", size=41).move_to(LEFT * 4.3 + UP * 2.0))
        grid = (
            VGroup(
                *(
                    VGroup(
                        *(
                            formula(rf"h_{{{a},{b}}}", size=28, color=BLUE_C)
                            for b in range(9)
                        )
                    ).arrange(RIGHT, buff=0.5)
                    for a in range(4)
                )
            )
            .arrange(DOWN, buff=0.5)
            .move_to(DOWN * 0.2)
        )
        row_labels = VGroup(
            *(
                formula(rf"H_{a}(P)", size=29).next_to(row, LEFT, buff=0.5)
                for a, row in enumerate(grid)
            )
        )
        self.show(grid, row_labels)
        self.at("symbolic")
        self.show(
            words("Symbolic positions · no order-36 row constructed", size=25).move_to(
                DOWN * 2.8
            )
        )
        self.at("choose_column")
        selected = VGroup(*(row[4] for row in grid))
        highlight = SurroundingRectangle(selected, buff=0.16).set_color(YELLOW)
        self.show(
            highlight,
            formula(r"P^4", size=36, color=YELLOW).next_to(highlight, UP, buff=0.25),
        )
        self.play(selected.animate.set_color(YELLOW), run_time=0.8)
        self.at("combine")
        self.show(
            words("A fixed P power picks one sign from each H.", size=27).move_to(
                DOWN * 3.55
            )
        )

        self.section("handoff", "Two independent checks before normalization")
        expression = formula(
            r"h(Z,P)=H_0(P)+ZH_1(P)+Z^2H_2(P)+Z^3H_3(P)",
            size=40,
            color=BLUE_C,
            width=14,
        ).move_to(UP * 1.55)
        self.show(expression)
        self.at("evaluate_next")
        self.show(
            Arrow(LEFT * 2 + UP * 0.85, LEFT * 3.8 + DOWN * 0.15, buff=0.1),
            words("Evaluate Z", size=32, color=YELLOW).move_to(LEFT * 4 + DOWN * 0.7),
            words("Preserve the norm", size=25).move_to(LEFT * 4 + DOWN * 1.55),
        )
        self.at("parity_next")
        self.show(
            Arrow(RIGHT * 2 + UP * 0.85, RIGHT * 3.8 + DOWN * 0.15, buff=0.1),
            words("Check parity", size=32, color=YELLOW).move_to(
                RIGHT * 4 + DOWN * 0.7
            ),
            words("Halves remain integral", size=25).move_to(RIGHT * 4 + DOWN * 1.55),
        )
        self.at("normalization")
        self.show(
            words("Then combine both checks in normalization", size=29).move_to(
                DOWN * 3.0
            )
        )
