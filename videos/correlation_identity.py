from manimlib import (
    BLUE_B,
    BLUE_C,
    BLUE_E,
    DOWN,
    UP,
    YELLOW,
    FlashAround,
    Matrix,
    TransformFromCopy,
    VGroup,
    color_gradient,
)

from videos.node_scene import NodeScene, formula, words


class CorrelationIdentity(NodeScene):
    node_id = "correlation-identity"
    title = "1.4 · A product records every dot product"

    def present(self):
        self.section("expand", "Multiply h by its cyclic reversal")
        self.show(
            self.stack(
                formula(
                    r"h=\sum_jh_jX^j,\qquad h^*=\sum_kh_kX^{-k}", size=48, color=BLUE_C
                ),
                formula(r"hh^*=\sum_{j,k}h_jh_kX^{j-k}", size=57, color=YELLOW),
                words("All exponents are read modulo n.", size=29),
            )
        )

        self.section("grid", "n = 4 illustration · collect equal exponents")
        grid = (
            Matrix(
                [[rf"h_{j}h_{k}X^{(j - k) % 4}" for k in range(4)] for j in range(4)],
                h_buff=1.8,
                v_buff=0.7,
            )
            .set_width(10)
            .move_to(DOWN * 0.3)
        )
        palette = color_gradient([BLUE_E, BLUE_B], 4)
        for index, entry in enumerate(grid.get_entries()):
            j, k = divmod(index, 4)
            entry.set_color(palette[(j - k) % 4])
        self.show(grid)
        chosen = VGroup(
            *(
                grid.get_entries()[4 * j + k]
                for j in range(4)
                for k in range(4)
                if (j - k) % 4 == 1
            )
        )
        self.play(chosen.animate.set_color(YELLOW), run_time=0.8)
        self.play(FlashAround(chosen, color=YELLOW), run_time=0.8)
        condition = formula(r"j-k\equiv1\pmod4", size=37, color=YELLOW)
        condition.move_to(DOWN * 2.5)
        self.show(condition)
        self.wait_until_narration(self.cues["grid"] + 10)
        self.remove(condition)
        collected = formula(
            r"[X](hh^*)=h_0h_3+h_1h_0+h_2h_1+h_3h_2",
            size=35,
            color=YELLOW,
        ).move_to(DOWN * 2.5)
        self.body.add(collected)
        self.play(TransformFromCopy(chosen, collected), run_time=1.8)

        self.section("coefficient", "Fix one exponent a")
        self.show(
            self.stack(
                formula(
                    r"j-k\equiv a\pmod n\quad\Longleftrightarrow"
                    r"\quad k\equiv j-a\pmod n",
                    size=44,
                ),
                formula(
                    r"[X^a](hh^*)=\sum_{j=0}^{n-1}h_jh_{j-a}", size=58, color=YELLOW
                ),
                words("Coefficient in the representative of degree below n.", size=26),
            )
        )

        self.section("dot", "The shifted row supplies the second factor")
        self.show(
            self.stack(
                formula(r"\text{original row:}\quad(h_j)_{j=0}^{n-1}", color=BLUE_C),
                formula(r"\text{a-step right shift:}\quad(h_{j-a})_{j=0}^{n-1}"),
                formula(
                    r"\langle\mathrm{row}_0,\mathrm{row}_a\rangle"
                    r"=\sum_jh_jh_{j-a}=[X^a](hh^*)",
                    size=46,
                    color=YELLOW,
                ),
            )
        )

        self.section("example", "Four correlations of the original sign row")
        rows = [r"(-1,1,1,1)", r"(1,-1,1,1)", r"(1,1,-1,1)", r"(1,1,1,-1)"]
        equations = (
            VGroup(
                *(
                    formula(
                        rf"a={a}:\quad(-1,1,1,1)\cdot"
                        + row
                        + "="
                        + str(4 if a == 0 else 0),
                        size=37,
                        color=BLUE_C if a == 0 else "#FFFFFF",
                    )
                    for a, row in enumerate(rows)
                )
            )
            .arrange(DOWN, buff=0.45)
            .move_to(UP * 0.2)
        )
        for equation in equations:
            self.show(equation)
        self.show(
            formula(r"hh^*=4+0X+0X^2+0X^3=4", size=44, color=YELLOW).move_to(DOWN * 2.3)
        )

        self.section("general", "The cyclic correlation identity")
        self.show(
            self.stack(
                formula(
                    r"hh^*=\sum_{a=0}^{n-1}\left(\sum_{j=0}^{n-1}h_jh_{j-a}\right)X^a",
                    size=59,
                    color=YELLOW,
                ),
                words(
                    "Valid for arbitrary integer coefficients.", size=31, color=BLUE_C
                ),
                formula(
                    r"h_j=\pm1\quad\Longrightarrow\quad[X^0](hh^*)=\sum_jh_j^2=n",
                    size=43,
                ),
                words("Next: the Hadamard dictionary.", size=29),
            )
        )
