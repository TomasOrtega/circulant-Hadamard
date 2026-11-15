from manimlib import (
    BLUE_C,
    DOWN,
    LEFT,
    PI,
    RIGHT,
    UP,
    YELLOW,
    Circle,
    Transform,
    VGroup,
)

from videos.node_scene import NodeScene, formula, words


class StarOperation(NodeScene):
    node_id = "star-operation"
    title = "1.3 · The star operation"

    def present(self):
        self.section("definition", "Read cyclic positions in the opposite direction")
        self.show(
            self.stack(
                formula(r"h(X)=\sum_{j=0}^{n-1}h_jX^j", color=BLUE_C),
                formula(
                    r"h^*(X)=\sum_{j=0}^{n-1}h_jX^{-j}=h(X^{-1})", size=49, color=YELLOW
                ),
                formula(r"X^{-1}=X^{n-1}", size=45),
            )
        )

        self.section("generic", "Fix position zero; reverse the others")
        center = LEFT * 3 + DOWN * 0.25
        circle = Circle(radius=1.4).set_color(BLUE_C).move_to(center)
        positions = [center + direction * 1.85 for direction in [UP, RIGHT, DOWN, LEFT]]
        coefficients = VGroup(
            *(
                formula(value, color=BLUE_C).move_to(position)
                for value, position in zip(["a", "b", "c", "d"], positions, strict=True)
            )
        )
        self.show(circle, coefficients)
        self.show(
            formula(r"(a,b,c,d)\longmapsto(a,d,c,b)", size=32, width=6).move_to(
                RIGHT * 2.7
            ),
            words("a stays at the marked start", size=23, width=6).move_to(
                RIGHT * 2.7 + DOWN
            ),
        )
        self.play(
            Transform(
                coefficients[1],
                coefficients[1].copy().move_to(positions[3]),
                path_arc=PI / 2,
            ),
            Transform(
                coefficients[3],
                coefficients[3].copy().move_to(positions[1]),
                path_arc=PI / 2,
            ),
            run_time=2,
        )

        self.section("example", "The fixed sign row happens to be symmetric")
        self.show(
            self.stack(
                formula(r"h=-1+X+X^2+X^3", color=BLUE_C),
                formula(r"h^*=-1+X^{-1}+X^{-2}+X^{-3}", size=44),
                formula(r"=-1+X^3+X^2+X=h", size=44, color=YELLOW),
                words("This example has h* = h; the general row need not.", size=25),
            )
        )

        self.section("well_defined", "The defining relation survives reversal")
        self.show(
            self.stack(
                formula(r"X^n=1", color=BLUE_C, size=64),
                formula(r"\Longrightarrow", size=52),
                formula(r"(X^{-1})^n=(X^n)^{-1}=1", color=YELLOW, size=55),
                words("Replacing X by X⁻¹ respects the quotient.", size=28),
            )
        )

        self.section("involution", "Two reversals return every coefficient")
        entries = VGroup(*(formula(v, color=BLUE_C) for v in ["a", "b", "c", "d"]))
        entries.arrange(RIGHT, buff=1).move_to(UP * 1.3)
        self.show(entries)
        positions = [obj.get_center().copy() for obj in entries]
        for targets in [(3, 1), (1, 3)]:
            self.play(
                Transform(
                    entries[1],
                    entries[1].copy().move_to(positions[targets[0]]),
                    path_arc=PI / 2,
                ),
                Transform(
                    entries[3],
                    entries[3].copy().move_to(positions[targets[1]]),
                    path_arc=PI / 2,
                ),
                run_time=1.3,
            )
        self.show(
            formula(r"(h^*)^*=h", size=65, color=YELLOW).move_to(DOWN * 0.3),
            formula(r"(fg)^*=f^*g^*", size=52).move_to(DOWN * 1.8),
        )

        self.section("purpose", "Reversal turns a product into correlations")
        self.show(
            self.stack(
                words(
                    "Reverse positions. Keep the coefficients.", size=31, color=BLUE_C
                ),
                formula(r"h^*(X)=h(X^{-1})", size=60, color=YELLOW),
                formula(
                    r"(h_0,h_1,\ldots,h_{n-1})\mapsto(h_0,h_{n-1},\ldots,h_1)", size=40
                ),
                words("Next: the coefficients of hh* are dot products.", size=28),
            )
        )
