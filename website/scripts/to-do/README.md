# Website media to-do

All current node overviews have accepted videos and production scripts. Keep
their completed sources in `overview.md` and `node1/`–`node8/`; the outstanding
work below concerns previews cut from a parent's overview.

For a future node without an accepted script/video pair, keep its unfinished
script or task in `<node-id>.md` here and leave its `video` unset. When both are
ready, save the completed source in its numbered folder, record the production,
attach the video, and remove the to-do entry.

## Parent previews

Review each parent's coverage before choosing a preview. Measure a suitable
passage, or prepare and record introductory coverage when none exists. Add
the real `segment` and its thumbnail before removing a row. Each child's full
video, script, and written explanation already exist.

| Parent node | Child node | Existing child script |
| --- | --- | --- |
| `restriction-on-the-order` | `order-is-square` | [2.1](../node2/order-is-square.md) |
| `restriction-on-the-order` | `order-is-even` | [2.2](../node2/order-is-even.md) |
| `restriction-on-the-order` | `power-of-two-cycle` | [2.3](../node2/power-of-two-cycle.md) |
| `restriction-on-the-order` | `cyclotomic-divisibility` | [2.4](../node2/cyclotomic-divisibility.md) |
| `restriction-on-the-order` | `fold-and-divide` | [2.5](../node2/fold-and-divide.md) |
| `restriction-on-the-order` | `odd-squares-mod-eight` | [2.6](../node2/odd-squares-mod-eight.md) |
| `delta-theorem` | `local-character-comparison` | [4.3](../node4/local-character-comparison.md) |
| `products-to-sums` | `split-exact-products` | [7.1](../node7/split-exact-products.md) |
| `products-to-sums` | `expand-integral-products` | [7.2](../node7/expand-integral-products.md) |
| `products-to-sums` | `cancel-before-reduction` | [7.3](../node7/cancel-before-reduction.md) |

The Delta and Products to Sums overviews have limited coverage. Their four
previews need suitable parent coverage rather than invented cut bounds. The
Order overview explains the square and parity steps but accepts oddness;
review its recording before planning the remaining previews.

`make -C website check` verifies that this table matches all unavailable parent
previews and that each node has an accepted video/script pair or its own to-do.
