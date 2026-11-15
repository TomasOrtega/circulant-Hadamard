import { writeFileSync } from "node:fs";
import { renderMarkdown } from "../../../markdown.js";

const styles = new Set();
const blue = "#0086bd";
const labels = [];
const label = (x, y, width, height, source, size = 21, color = "#222") => {
  const result = renderMarkdown(source, "Node 6 storyboard");
  styles.add(result.css);
  labels.push(`<foreignObject x="${x}" y="${y}" width="${width}" height="${height}" aria-hidden="true"><div xmlns="http://www.w3.org/1999/xhtml" class="label" style="font-size:${size}px;color:${color}">${result.html}</div></foreignObject>`);
};
const point = (cx, cy, degrees, radius = 145) => {
  const angle = degrees * Math.PI / 180;
  return [cx + radius * Math.cos(angle), cy - radius * Math.sin(angle)];
};
const left = [290, 340];
const right = [910, 340];
const directions = [0, 180, 90];
const shapes = [];
for (const [index, center] of [left, right].entries()) {
  const [cx, cy] = center;
  shapes.push(`<line x1="${cx - 175}" y1="${cy}" x2="${cx + 175}" y2="${cy}" class="axis"/>
<line x1="${cx}" y1="${cy - 175}" x2="${cx}" y2="${cy + 175}" class="axis"/>
<circle cx="${cx}" cy="${cy}" r="145" class="circle"/>`);
  directions.forEach((angle, j) => {
    const [x, y] = point(cx, cy, angle + index * 120);
    shapes.push(`<line x1="${cx}" y1="${cy}" x2="${x.toFixed(2)}" y2="${y.toFixed(2)}" class="ray"/>
<circle data-point="${["c", "d", "g"][j]}-${index}" cx="${x.toFixed(2)}" cy="${y.toFixed(2)}" r="6" fill="${blue}"/>`);
  });
}

label(185, 110, 210, 48, String.raw`$P=1$`, 24);
label(805, 110, 210, 48, String.raw`$P=\omega$`, 24);
label(410, 293, 145, 48, String.raw`$c(1)=3$`, 20, blue);
label(4, 337, 150, 48, String.raw`$d(1)=-3$`, 20, blue);
label(198, 150, 184, 44, String.raw`$g(1)=3i$`, 20, blue);
label(748, 166, 180, 50, String.raw`$c(\omega)=3\omega$`, 20, blue);
label(973, 469, 210, 50, String.raw`$d(\omega)=-3\omega$`, 20, blue);
label(658, 420, 190, 50, String.raw`$g(\omega)=3i\omega$`, 20, blue);
label(240, 510, 100, 42, String.raw`$|z|=3$`, 19);
label(860, 510, 100, 42, String.raw`$|z|=3$`, 19);
label(498, 237, 204, 52, String.raw`$\lambda=\omega$`, 24, blue);
label(492, 287, 216, 44, String.raw`$+120^\circ$`, 21, blue);
label(490, 397, 220, 58, String.raw`$R=W=1$`, 25);
label(180, 581, 840, 68, String.raw`$\bigl(c(\omega),d(\omega),g(\omega)\bigr)=\lambda\bigl(c(1),d(1),g(1)\bigr)$`, 24);
label(400, 654, 400, 45, String.raw`$\Delta(c)=\lambda^{-1}=\omega^2$`, 20);

const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="790" viewBox="0 0 1200 790" role="img" aria-labelledby="title description">
<title id="title">Odd-order rigidity gives one common rotation</title>
<desc id="description">Two circles of radius three show a schematic triple of polynomial values. At P equals one the points are c equals three, d equals minus three, and g equals three i. At P equals omega every point has been multiplied by omega, a counterclockwise rotation of 120 degrees. Their relative positions remain unchanged, while R and W equal one. These illustrative values do not constitute a Hadamard construction.</desc>
<defs><marker id="rotation-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="${blue}"/></marker></defs>
<style>
${[...styles].join("\n")}
text{font-family:Arial,Helvetica,sans-serif;fill:#222}
.heading{font-size:28px;font-weight:600}
.note{font-size:18px;fill:#555}
.axis{stroke:#bbb;stroke-width:1.3}
.circle{fill:none;stroke:#999;stroke-width:1.7}
.ray{stroke:${blue};stroke-width:1.8}
.label{height:100%;display:flex;align-items:center;justify-content:center;text-align:center;font-family:Arial,Helvetica,sans-serif}
.label p{margin:0;line-height:1.2}
</style>
<rect width="1200" height="790" fill="#f4f9fc"/>
<rect x="15" y="92" width="1170" height="654" rx="16" fill="white" stroke="#b9dbea" stroke-width="1.5"/>
<text x="600" y="42" text-anchor="middle" class="heading">Node 6 · One common rotation</text>
<text x="600" y="73" text-anchor="middle" class="note">The same angle carries each point from the left circle to the right circle.</text>
${shapes.join("\n")}
<path d="M 500 340 L 700 340" fill="none" stroke="${blue}" stroke-width="3" marker-end="url(#rotation-arrow)"/>
<text x="600" y="376" text-anchor="middle" class="note">counterclockwise</text>
${labels.join("\n")}
<text x="600" y="725" text-anchor="middle" class="note">The three points stay separate; their relative positions are preserved.</text>
<text x="600" y="776" text-anchor="middle" class="note">Schematic illustration of the conclusion, not an order-36 Hadamard construction.</text>
</svg>
`;

writeFileSync(new URL("common-rotation.svg", import.meta.url), svg);
