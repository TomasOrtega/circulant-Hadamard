import { writeFileSync } from "node:fs";
import { renderMarkdown } from "../../../markdown.js";

const styles = new Set();
const blue = "#0086bd";
const labels = [];
const shapes = [];
const label = (x, y, width, height, source, size = 22, color = "#222") => {
  const result = renderMarkdown(source, "Node 8 storyboard");
  styles.add(result.css);
  labels.push(`<foreignObject x="${x}" y="${y}" width="${width}" height="${height}" aria-hidden="true"><div xmlns="http://www.w3.org/1999/xhtml" class="label" style="font-size:${size}px;color:${color}">${result.html}</div></foreignObject>`);
};
const arrow = (from, to, className = "vector") => {
  shapes.push(`<line x1="${from[0].toFixed(2)}" y1="${from[1].toFixed(2)}" x2="${to[0].toFixed(2)}" y2="${to[1].toFixed(2)}" class="${className}" marker-end="url(#arrow)"/>`);
};
const roots = [0, 1, 2].map(k => [Math.cos(2 * Math.PI * k / 3), Math.sin(2 * Math.PI * k / 3)]);
shapes.push('<circle cx="245" cy="300" r="75" class="circle"/>');
for (const [re, im] of roots) arrow([245, 300], [245 + 75 * re, 300 - 75 * im]);
for (const x of [83, 220, 357]) {
  const points = [[x, 455], [x + 52, 455], [x + 26, 455 - 26 * Math.sqrt(3)]];
  points.forEach((point, index) => arrow(point, points[(index + 1) % 3]));
}
for (let j = 0; j < 9; j++) {
  const x = 523 + 43 * j;
  arrow([x, 270], [x + 29, 270]);
  label(x - 2, 286, 34, 42, "$1$", 22);
  label(x - 2, 431, 34, 45, "$1$", 24, j === 8 ? blue : "#222");
}
for (let j = 0; j < 4; j++) {
  const x = 515 + j * 86;
  shapes.push(`<rect x="${x}" y="420" width="79" height="64" rx="10" fill="none" stroke="#aaa" stroke-width="1.5"/>`);
  label(x - 1, 490, 81, 46, String.raw`$1+1\equiv0$`, 15);
}
shapes.push('<circle cx="881" cy="453" r="29" fill="#e7f4fa" stroke="#0086bd" stroke-width="2"/>');
label(45, 160, 400, 50, String.raw`$P=\omega$`, 26);
label(310, 277, 50, 45, "$1$", 23);
label(166, 199, 55, 45, String.raw`$\omega$`, 23);
label(158, 351, 65, 45, String.raw`$\omega^2$`, 23);
label(40, 540, 410, 62, String.raw`$J(\omega)=3(1+\omega+\omega^2)$`, 21);
label(45, 615, 400, 60, String.raw`$J(\omega)=0$`, 29, blue);
label(520, 160, 400, 50, "$P=1$", 26);
label(520, 339, 400, 55, String.raw`$J(1)=9$`, 24);
label(520, 553, 400, 55, String.raw`$2=(1+i)(1-i)$`, 23);
label(520, 615, 400, 60, String.raw`$9\equiv1\pmod{1+i}$`, 26, blue);
label(995, 175, 400, 55, String.raw`$c(1)^2=9,\quad c(1)=\pm3$`, 22);
label(990, 260, 410, 70, String.raw`$\dfrac{9}{c(1)}=\pm3\equiv1$`, 25, blue);
label(992, 368, 405, 60, String.raw`$\text{Node 7: }\mathcal S\equiv0$`, 25);
label(992, 458, 405, 60, String.raw`$\text{Node 8: }\mathcal S\equiv1$`, 25, blue);
label(992, 555, 405, 75, String.raw`$0\ne1$`, 39, blue);
label(990, 650, 410, 55, String.raw`$n\in\{1,4\}$`, 28);
label(520, 383, 400, 44, String.raw`Now reduce modulo $1+i$:`, 18, "#555");
label(110, 793, 1220, 45, String.raw`The same alternating sum cannot be both zero and one modulo $1+i$.`, 18, "#555");

const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="850" viewBox="0 0 1440 850" role="img" aria-labelledby="title description">
<title id="title">Why an odd number of ones finishes the proof</title>
<desc id="description">The first panel shows the three cube roots as unit arrows, and nine terms forming three closed equilateral triangles; their complex sum is exactly zero. The second panel first adds nine parallel arrows to nine, then separately pairs nine symbols one in the reduction ring: four pairs have residue zero and one remains. The third panel accounts for c at one being plus or minus three, so nine divided by c has residue one. This conflicts with the zero residue of the same sum from Node 7. Zero and one are distinct in the nonzero reduction ring. The theorem leaves only orders one and four.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="${blue}"/></marker></defs>
<style>
${[...styles].join("\n")}
text{font-family:Arial,Helvetica,sans-serif;fill:#222}
.heading{font-size:28px;font-weight:600}
.step{font-size:25px;font-weight:600}
.note{font-size:18px;fill:#555}
.vector{stroke:${blue};stroke-width:2}
.circle{fill:none;stroke:#aaa;stroke-width:1.4}
.label{height:100%;display:flex;align-items:center;justify-content:center;text-align:center;font-family:Arial,Helvetica,sans-serif}
.label p{margin:0;line-height:1.2}
</style>
<rect width="1440" height="850" fill="#f4f9fc"/>
<text x="720" y="42" text-anchor="middle" class="heading">Node 8 · An odd number of ones</text>
<text x="720" y="76" text-anchor="middle" class="note">Evaluate exactly, reduce algebraically, and compare the two residues.</text>
<rect x="16" y="105" width="454" height="675" rx="16" fill="white" stroke="#b9dbea" stroke-width="1.5"/>
<rect x="490" y="105" width="460" height="675" rx="16" fill="white" stroke="#b9dbea" stroke-width="1.5"/>
<rect x="970" y="105" width="454" height="675" rx="16" fill="white" stroke="#b9dbea" stroke-width="1.5"/>
<text x="245" y="140" text-anchor="middle" class="step">1. Root terms cancel</text>
<text x="720" y="140" text-anchor="middle" class="step">2. One remains</text>
<text x="1195" y="140" text-anchor="middle" class="step">3. The residues conflict</text>
${shapes.join("\n")}
${labels.join("\n")}
<text x="245" y="750" text-anchor="middle" class="note">Exact cancellation in the complex plane.</text>
<text x="720" y="750" text-anchor="middle" class="note">Four pairs vanish in characteristic two.</text>
<text x="1195" y="750" text-anchor="middle" class="note">The reduction ring is nonzero.</text>
</svg>
`;
writeFileSync(new URL("odd-ones.svg", import.meta.url), svg);
