import { renderMarkdown } from "./markdown.js";
import { CIRCLE_RADIUS, POINTS, phaseLabelBox, phasePoint, phaseScene } from "./phase-model.js";

const controls = "min-h-12 cursor-pointer rounded-md border border-theme/30 bg-white px-3 py-2 font-sans text-base has-[:checked]:bg-theme/15 has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-theme";

function MathText({ children, className = "", inline = false }) {
  const Tag = inline ? "span" : "div";
  const html = renderMarkdown(children).html;
  return <Tag className={`min-w-0 overflow-x-auto ${className}`}
    dangerouslySetInnerHTML={{ __html: inline ? html.replace(/^<p>([\s\S]*)<\/p>$/, "$1") : html }} />;
}

function PhaseCircle({ id, side, values }) {
  const input = side === "left" ? "1" : "ω";
  const texInput = side === "left" ? "1" : String.raw`\omega`;
  return (
    <figure className="min-w-0 rounded-md bg-white p-3">
      <MathText className="text-center">{`$P=${side === "left" ? "1" : "\\omega"}$`}</MathText>
      <svg viewBox="0 0 320 300" role="img" aria-labelledby={`${id}-${side}-title ${id}-${side}-desc`}
        data-phase-plane={side} className="mx-auto block w-full max-w-90 text-theme">
        <title id={`${id}-${side}-title`}>{`Values at P = ${input}`}</title>
        <desc id={`${id}-${side}-desc`} data-phase-description>
          {`The values c(${input}), d(${input}), and g(${input}) lie on a circle of radius three. The triangular E(${input}) marker lies outside it. All four values rotate by 120 degrees from left to right.`}
        </desc>
        <path d="M20 150H300M160 15V285" fill="none" stroke="currentColor" opacity="0.2" />
        <circle cx="160" cy="150" r={CIRCLE_RADIUS} fill="none" stroke="currentColor" opacity="0.45" />
        <text x="294" y="168" className="fill-dark-gray font-sans text-xs">Re</text>
        <text x="168" y="25" className="fill-dark-gray font-sans text-xs">Im</text>
        {POINTS.map(name => {
          const point = phasePoint(values[name], 3);
          const label = phaseLabelBox(point);
          return <g key={name} data-phase-value={name}>
            <line x1="160" y1="150" x2={point.x} y2={point.y} stroke="currentColor"
              opacity={name === "E" ? "0.9" : "0.55"} strokeWidth={name === "E" ? "2" : "1"} data-phase-ray />
            <g transform={`translate(${point.x} ${point.y})`} data-phase-marker>
              {name === "c" ? <circle r="6" fill="currentColor" />
                : name === "d" ? <path d="M0 -7L7 0L0 7L-7 0Z" className="fill-black" />
                : name === "E" ? <path d="M0 -8L7 6L-7 6Z" fill="white" stroke="currentColor" strokeWidth="2" />
                : <rect x="-5.5" y="-5.5" width="11" height="11" fill="white" stroke="currentColor" strokeWidth="2" />}
            </g>
            <foreignObject x={label.x} y={label.y} width="64" height="40" data-phase-label-box>
              <div xmlns="http://www.w3.org/1999/xhtml" data-phase-label-align
                className={`flex size-full items-center text-sm text-black ${label.align === "end" ? "justify-end" : label.align === "start" ? "justify-start" : "justify-center"}`}>
                <span data-phase-label="raw"><MathText inline>{`$${name}(${texInput})$`}</MathText></span>
                <span data-phase-label="normalized" hidden><MathText inline>{`$\\frac{${name}(${texInput})}{c(${texInput})}$`}</MathText></span>
              </div>
            </foreignObject>
          </g>;
        })}
      </svg>
      <figcaption className="text-center font-sans text-sm text-dark-gray" data-phase-caption>
        {side === "left" ? "Reference values · circle radius 3" : "All four values rotated · circle radius 3"}
      </figcaption>
    </figure>
  );
}

export function PhaseExplorer({ id, stage = "rotation", nextHref }) {
  const showNormalization = stage === "normalization";
  const scene = phaseScene();
  return (
    <div data-phase-explorer data-phase-stage={stage} className="flex min-w-0 flex-col gap-6 rounded-md border border-theme/40 bg-theme/5 p-6 max-md:p-4"
      role="group" aria-labelledby={`${id}-title`}>
      <h3 id={`${id}-title`} className="font-sans text-2xl">
        {showNormalization ? "Cancel the common rotation" : "Explore the common rotation"}
      </h3>
      <MathText>{showNormalization
        ? String.raw`Divide by $c(1)$ on the left and $c(\omega)$ on the right. The two normalized evaluations of $E(P)$ then line up.`
        : String.raw`For $u=3$, compare the fixed inputs $P=1$ and $P=\omega$. Choose a common rotation $\lambda$ and watch all four evaluations turn together. The triangular markers are the values of $E(P)$.`}</MathText>
      <fieldset disabled data-phase-controls className="flex min-w-0 flex-col gap-4 font-sans">
        <legend className="mb-3 text-base">Rotation from the left circle to the right</legend>
        <div className="flex flex-wrap gap-3">
          {["1", String.raw`\omega`, String.raw`\omega^2`].map((lambda, turn) =>
            <label key={turn} className={`${controls} inline-flex items-center gap-2`}>
              <input type="radio" name={`${id}-rotation`} value={turn} defaultChecked={turn === 1} data-phase-turn
                className="size-4 accent-theme" />
              <span>{turn * 120}°</span>
              <MathText inline>{`$\\lambda=${lambda}$`}</MathText>
            </label>)}
        </div>
        {showNormalization && <label className={`${controls} flex w-fit items-center gap-3`}>
          <input type="checkbox" data-phase-normalize className="size-5 accent-theme"
            aria-label="Divide by c(1) on the left and c(omega) on the right" />
          <MathText inline>{String.raw`Divide by $c(1)$ and $c(\omega)$`}</MathText>
        </label>}
      </fieldset>
      <noscript>The circles show a 120° common rotation. Enable JavaScript to use the controls.</noscript>
      <div className="grid min-w-0 grid-cols-2 gap-4 max-md:grid-cols-1">
        <PhaseCircle id={id} side="left" values={scene.left} />
        <PhaseCircle id={id} side="right" values={scene.right} />
      </div>
      <p data-phase-status role="status" aria-live="polite" aria-atomic="true" className="font-sans text-base">
        All four evaluations turn by 120°. Their relative angles stay fixed.
      </p>
      {!showNormalization && <>
        <MathText>{String.raw`The polynomial $E(P)$ is built from $c(P),d(P),g(P)$ by`}</MathText>
        <MathText className="max-md:text-sm">{String.raw`$$
E(P)=\frac{d(P)-c(P)}2+\frac{g(P)-c(P)}{1+i}.
$$`}</MathText>
        <MathText>{String.raw`Here $E(1)=-3+3i$. Its value rotates by the same angle as the values of $c(P),d(P),g(P)$, although it need not lie on their circle. The forward multiplier is $\lambda$; the reverse rotation is $\Delta(c)=\lambda^{-1}$.`}</MathText>
      </>}
      <p className="font-sans text-sm text-dark-gray">
        This is an illustration: no circulant Hadamard matrix of order 36 exists.
      </p>
      {!showNormalization && <details className="rounded-md border border-theme/30 bg-white p-4">
        <summary className="min-h-12 cursor-pointer font-sans text-lg">The conflict suggested by the picture</summary>
        <div className="mt-4 flex min-w-0 flex-col gap-5">
          <MathText>{String.raw`Node 5 gives $E(1)\equiv1\pmod{1+i}$. At $P=\omega$, the all-ones terms cancel, so the same coefficient condition requires $E(\omega)\equiv0\pmod{1+i}$.`}</MathText>
          <div className="grid min-w-0 grid-cols-2 gap-4 max-md:grid-cols-1">
            <MathText className="rounded-md bg-theme/5 p-3 text-center">{String.raw`**Required at $P=1$:** a nonzero residue.`}</MathText>
            <MathText className="rounded-md bg-theme/5 p-3 text-center">{String.raw`**Required at $P=\omega$:** zero residue.`}</MathText>
          </div>
          <MathText>{String.raw`But $E(1)$ and $E(\omega)$ must share an invertible rotation multiplier. It remains invertible modulo $1+i$, so it cannot carry a nonzero residue to zero. The angle changes; the conflict is between the common rotation and these two arithmetic requirements.`}</MathText>
          <p>Node 7 uses the equality proved above to compare the two residues and finish the nine-position example.</p>
          {nextHref && <a href={nextHref} className="self-start font-sans">Continue to Node 7 →</a>}
          <p className="font-sans text-sm text-dark-gray">
            These are requirements of the Hadamard construction, not residues computed from the schematic points above.
            Changing an angle alone does not make a residue become zero.
          </p>
        </div>
      </details>}
    </div>
  );
}
