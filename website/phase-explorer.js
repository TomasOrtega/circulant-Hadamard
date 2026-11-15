import { POINTS, phaseLabelBox, phasePoint, phaseScene } from "./phase-model.js";

export function initPhaseExplorer(root) {
  const update = () => {
    const turn = Number(root.querySelector("[data-phase-turn]:checked").value);
    const normalized = root.querySelector("[data-phase-normalize]")?.checked ?? false;
    const scene = phaseScene(turn, normalized);
    for (const side of ["left", "right"]) {
      const plane = root.querySelector(`[data-phase-plane="${side}"]`);
      const input = side === "left" ? "1" : "ω";
      for (const name of POINTS) {
        const point = phasePoint(scene[side][name], scene.radius);
        const group = plane.querySelector(`[data-phase-value="${name}"]`);
        const ray = group.querySelector("[data-phase-ray]");
        ray.setAttribute("x2", point.x);
        ray.setAttribute("y2", point.y);
        group.querySelector("[data-phase-marker]").setAttribute("transform", `translate(${point.x} ${point.y})`);
        const label = phaseLabelBox(point);
        const box = group.querySelector("[data-phase-label-box]");
        box.setAttribute("x", label.x);
        box.setAttribute("y", label.y);
        const alignment = box.querySelector("[data-phase-label-align]");
        for (const align of ["start", "center", "end"])
          alignment.classList.toggle(`justify-${align}`, label.align === align);
        box.querySelector('[data-phase-label="raw"]').hidden = normalized;
        box.querySelector('[data-phase-label="normalized"]').hidden = !normalized;
      }
      plane.querySelector("[data-phase-description]").textContent = normalized
        ? `After division by c(${input}), the normalized values at ${input} agree with those in the other picture. E(${input})/c(${input}) is minus 1 plus i, outside the unit circle.`
        : `The values c(${input}), d(${input}), and g(${input}) lie on a circle of radius three. The triangular E(${input}) marker lies outside it. All four evaluations rotate by ${turn * 120} degrees from left to right.`;
      plane.parentElement.querySelector("[data-phase-caption]").textContent = normalized
        ? `After division by c(${input}) · circle radius 1`
        : `${side === "left" ? "Reference values" : "All four values rotated"} · circle radius 3`;
    }
    root.querySelector("[data-phase-status]").textContent = normalized
      ? `The ${turn * 120}° rotation cancels. The corresponding points now line up.`
      : `All four evaluations turn by ${turn * 120}°. Their relative angles stay fixed.`;
  };
  root.addEventListener("change", update);
  update();
  root.querySelector("[data-phase-controls]").disabled = false;
}

if (typeof document !== "undefined") {
  for (const root of document.querySelectorAll("[data-phase-explorer]"))
    initPhaseExplorer(root);
}
