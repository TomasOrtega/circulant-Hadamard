import { writeFileSync } from "node:fs";
import { renderMarkdown } from "../../../markdown.js";

const styles = new Set();
const blue = "#0086bd";
const labels = [];
const label = (x, y, width, height, source, size = 21, color = "#222") => {
  const result = renderMarkdown(source, "Node 7 storyboard");
  styles.add(result.css);
  labels.push(`<foreignObject x="${x}" y="${y}" width="${width}" height="${height}" aria-hidden="true"><div xmlns="http://www.w3.org/1999/xhtml" class="label" style="font-size:${size}px;color:${color}">${result.html}</div></foreignObject>`);
};
const shapes = [];
const point = ([cx, cy], [re, im], scale) => [cx + scale * re, cy - scale * im];
const line = (from, to, className, marker = "") => {
  shapes.push(`<line x1="${from[0].toFixed(2)}" y1="${from[1].toFixed(2)}" x2="${to[0].toFixed(2)}" y2="${to[1].toFixed(2)}" class="${className}"${marker ? ` marker-end="url(#${marker})"` : ""}/>`);
};
const dot = (at, name, color = "#777", radius = 4) => {
  shapes.push(`<circle data-point="${name}" cx="${at[0].toFixed(2)}" cy="${at[1].toFixed(2)}" r="${radius}" fill="${color}"/>`);
};
const plane = (center, scale, radius) => {
  line([center[0] - 165, center[1]], [center[0] + 165, center[1]], "axis");
  line([center[0], center[1] - 165], [center[0], center[1] + 165], "axis");
  shapes.push(`<circle cx="${center[0]}" cy="${center[1]}" r="${scale * radius}" class="circle"/>`);
};
const rotate = ([re, im]) => [-re / 2 - im * Math.sqrt(3) / 2, re * Math.sqrt(3) / 2 - im / 2];
const first = [245, 370];
const second = [725, 350];
const third = [1195, 380];
const initial = [[3, 0], [-3, 0], [0, 3]];
const eInitial = [-3, 3];
for (const [index, center] of [first, second].entries()) {
  plane(center, 35, 3);
  const transform = index ? rotate : (z) => z;
  initial.forEach((z, j) => {
    const p = point(center, transform(z), 35);
    line(center, p, "guide");
    dot(p, `${["c", "d", "g"][j]}-${index}`);
  });
  const halfway = point(center, transform([-3, 0]), 35);
  const end = point(center, transform(eInitial), 35);
  line(center, halfway, "component", "component-arrow");
  line(halfway, end, "component", "component-arrow");
  line(center, end, "result", "result-arrow");
  dot(end, `E-${index}`, blue, 5);
}
plane(third, 100, 1);
const normalized = point(third, [-1, 1], 100);
line(third, point(third, [1, 0], 100), "guide");
dot(point(third, [1, 0], 100), "normalized-c");
line(third, normalized, "coincident");
line(third, normalized, "result", "result-arrow");
dot(normalized, "normalized-E", blue, 5);

label(90, 150, 310, 55, String.raw`$P=1$`, 25);
label(570, 150, 310, 55, String.raw`$P=\omega,\quad\lambda=\omega$`, 25);
label(1040, 150, 310, 55, String.raw`$\text{Divide each value by }c$`, 22);
label(350, 345, 95, 50, String.raw`$c(1)$`, 20);
label(42, 353, 90, 48, String.raw`$d(1)$`, 20);
label(203, 213, 92, 45, String.raw`$g(1)$`, 20);
label(45, 217, 140, 48, String.raw`$E(1)$`, 22, blue);
label(164, 376, 60, 44, String.raw`$-3$`, 19);
label(90, 291, 48, 44, String.raw`$3i$`, 19);
label(610, 208, 130, 46, String.raw`$c(\omega)$`, 20);
label(783, 425, 130, 46, String.raw`$d(\omega)$`, 20);
label(495, 384, 135, 46, String.raw`$g(\omega)$`, 20);
label(636, 495, 130, 48, String.raw`$E(\omega)$`, 22, blue);
label(1267, 389, 90, 48, String.raw`$1$`, 20);
label(1028, 219, 150, 50, String.raw`$-1+i$`, 22, blue);
label(1042, 502, 305, 48, String.raw`$\left|c/c\right|=1$`, 20);
label(40, 556, 410, 55, String.raw`$E(1)=-3+3i$`, 24, blue);
label(42, 620, 406, 50, String.raw`$\dfrac{d(1)-c(1)}2=-3$`, 21);
label(42, 677, 406, 55, String.raw`$\dfrac{g(1)-c(1)}{1+i}=3i$`, 21);
label(515, 556, 420, 55, String.raw`$E(\omega)=\omega E(1)$`, 24, blue);
label(510, 620, 430, 50, String.raw`$\arg\lambda=120^\circ$`, 22);
label(510, 680, 430, 48, String.raw`$|E(1)|=|E(\omega)|=3\sqrt2$`, 21);
label(995, 556, 400, 62, String.raw`$\dfrac{E(1)}{c(1)}=\dfrac{E(\omega)}{c(\omega)}=-1+i$`, 21, blue);
label(995, 641, 400, 65, String.raw`$\dfrac{E(1)}{c(1)}-\dfrac{E(\omega)}{c(\omega)}=0$`, 22);

const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="850" viewBox="0 0 1440 850" role="img" aria-labelledby="title description">
<title id="title">One common rotation gives one vanishing difference</title>
<desc id="description">Three panels illustrate evaluated complex vectors. First, c equals three, d equals minus three and g equals three i. The scaled differences are minus three and three i, with sum E equal to minus three plus three i, outside the circle of radius three. Second, multiplication by omega rotates every vector, including E, counterclockwise by 120 degrees. Third, dividing each configuration by its own c value brings both normalized E arrows to minus one plus i. Their exact difference is zero. These schematic values are not an order-36 Hadamard construction and do not assert the all-ones coefficient congruence.</desc>
<defs>
<marker id="result-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="${blue}"/></marker>
<marker id="component-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#444"/></marker>
</defs>
<style>
${[...styles].join("\n")}
text{font-family:Arial,Helvetica,sans-serif;fill:#222}
.heading{font-size:28px;font-weight:600}
.step{font-size:25px;font-weight:600}
.note{font-size:19px;fill:#555}
.axis{stroke:#ccc;stroke-width:1.2}
.circle{fill:none;stroke:#aaa;stroke-width:1.5}
.guide{stroke:#b5b5b5;stroke-width:1.5}
.component{stroke:#444;stroke-width:2}
.result{stroke:${blue};stroke-width:3}
.coincident{stroke:#b9dbea;stroke-width:10}
.label{height:100%;display:flex;align-items:center;justify-content:center;text-align:center;font-family:Arial,Helvetica,sans-serif}
.label p{margin:0;line-height:1.2}
</style>
<rect width="1440" height="850" fill="#f4f9fc"/>
<text x="720" y="42" text-anchor="middle" class="heading">Node 7 · One rotation, one vanishing sum</text>
<text x="720" y="76" text-anchor="middle" class="note">Construct the vector, rotate it with the triple, then cancel the rotation by dividing.</text>
<rect x="16" y="105" width="454" height="675" rx="16" fill="white" stroke="#b9dbea" stroke-width="1.5"/>
<rect x="490" y="105" width="460" height="675" rx="16" fill="white" stroke="#b9dbea" stroke-width="1.5"/>
<rect x="970" y="105" width="454" height="675" rx="16" fill="white" stroke="#b9dbea" stroke-width="1.5"/>
<text x="245" y="140" text-anchor="middle" class="step">1. Construct the sum</text>
<text x="725" y="140" text-anchor="middle" class="step">2. Rotate everything</text>
<text x="1195" y="140" text-anchor="middle" class="step">3. Normalize and cancel</text>
${shapes.join("\n")}
${labels.join("\n")}
<text x="245" y="759" text-anchor="middle" class="note">Add the scaled arrows head-to-tail.</text>
<text x="725" y="759" text-anchor="middle" class="note">The sum is outside the radius-three circle.</text>
<text x="1195" y="759" text-anchor="middle" class="note">Both normalized arrows coincide.</text>
<text x="720" y="823" text-anchor="middle" class="note">Schematic continuation of Node 6, not an order-36 Hadamard construction.</text>
</svg>
`;

writeFileSync(new URL("rotation-cancellation.svg", import.meta.url), svg);
