export const PHASES = ["c", "d", "g"];
export const POINTS = [...PHASES, "E"];
export const CIRCLE_RADIUS = 80;

export function phaseScene(turn = 1, normalized = false) {
  if (!Number.isInteger(turn) || turn < 0 || turn > 2) {
    throw new RangeError("turn must be an integer from 0 to 2");
  }

  const angle = 2 * Math.PI * turn / 3;
  const cosine = Math.cos(angle);
  const sine = Math.sin(angle);
  const left = {
    c: { re: 3, im: 0 },
    d: { re: -3, im: 0 },
    g: { re: 0, im: 3 },
  };
  const right = Object.fromEntries(PHASES.map((name) => {
    const { re, im } = left[name];
    return [name, { re: re * cosine - im * sine, im: re * sine + im * cosine }];
  }));

  for (const points of [left, right]) {
    const difference = {
      re: points.g.re - points.c.re,
      im: points.g.im - points.c.im,
    };
    points.E = {
      re: (points.d.re - points.c.re) / 2 + (difference.re + difference.im) / 2,
      im: (points.d.im - points.c.im) / 2 + (difference.im - difference.re) / 2,
    };
  }

  if (normalized) {
    for (const points of [left, right]) {
      const reference = points.c;
      const norm = reference.re ** 2 + reference.im ** 2;
      for (const name of POINTS) {
        const { re, im } = points[name];
        points[name] = {
          re: (re * reference.re + im * reference.im) / norm,
          im: (im * reference.re - re * reference.im) / norm,
        };
      }
    }
  }

  return { left, right, radius: normalized ? 1 : 3 };
}

export function phasePoint({ re, im }, radius) {
  return { x: 160 + CIRCLE_RADIUS * re / radius, y: 150 - CIRCLE_RADIUS * im / radius };
}

export function phaseLabelBox({ x, y }) {
  const horizontal = Math.abs(x - 160) < 8 ? 0 : Math.sign(x - 160);
  const vertical = Math.abs(y - 150) < 8 ? 0 : Math.sign(y - 150);
  return {
    x: horizontal < 0 ? x - 71 : horizontal > 0 ? x + 7 : x - 32,
    y: vertical < 0 ? y - 47 : vertical > 0 ? y + 7 : y - 20,
    align: horizontal < 0 ? "end" : horizontal > 0 ? "start" : "center",
  };
}
