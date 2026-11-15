import { describe, expect, test } from "bun:test";
import { CIRCLE_RADIUS, PHASES, POINTS, phasePoint, phaseScene } from "./phase-model.js";

function expectPoint(actual, expected) {
  expect(actual.re).toBeCloseTo(expected.re, 12);
  expect(actual.im).toBeCloseTo(expected.im, 12);
}

function quotient(value, reference) {
  const norm = reference.re ** 2 + reference.im ** 2;
  return {
    re: (value.re * reference.re + value.im * reference.im) / norm,
    im: (value.im * reference.re - value.re * reference.im) / norm,
  };
}

describe("common rotation phase model", () => {
  const rotations = [
    { re: 1, im: 0 },
    { re: -0.5, im: Math.sqrt(3) / 2 },
    { re: -0.5, im: -Math.sqrt(3) / 2 },
  ];

  for (const [turn, rotation] of rotations.entries()) {
    test(`turn ${turn} preserves radius three and rotates every point together`, () => {
      const { left, right, radius } = phaseScene(turn);
      expect(radius).toBe(3);
      expect(left).toEqual({
        c: { re: 3, im: 0 },
        d: { re: -3, im: 0 },
        g: { re: 0, im: 3 },
        E: { re: -3, im: 3 },
      });
      for (const name of PHASES) {
        expect(Math.hypot(left[name].re, left[name].im)).toBeCloseTo(3, 12);
        expect(Math.hypot(right[name].re, right[name].im)).toBeCloseTo(3, 12);
        expectPoint(quotient(right[name], left[name]), rotation);
      }
      for (const points of [left, right]) {
        expectPoint(quotient(points.d, points.c), { re: -1, im: 0 });
        expectPoint(quotient(points.g, points.c), { re: 0, im: 1 });
      }
    });

    test(`turn ${turn} carries the derived E point through the same rotation`, () => {
      const { left, right } = phaseScene(turn);
      for (const points of [left, right]) {
        const difference = {
          re: points.g.re - points.c.re,
          im: points.g.im - points.c.im,
        };
        const gaussianTerm = quotient(difference, { re: 1, im: 1 });
        expectPoint(points.E, {
          re: (points.d.re - points.c.re) / 2 + gaussianTerm.re,
          im: (points.d.im - points.c.im) / 2 + gaussianTerm.im,
        });
        expect(Math.hypot(points.E.re, points.E.im)).toBeCloseTo(3 * Math.sqrt(2), 12);
      }
      expectPoint(left.E, { re: -3, im: 3 });
      expectPoint(quotient(right.E, left.E), rotation);
    });

    test(`turn ${turn} disappears when each plane is divided by its own c`, () => {
      const { left, right, radius } = phaseScene(turn, true);
      const raw = phaseScene(turn);
      expect(radius).toBe(1);
      const expected = {
        c: { re: 1, im: 0 },
        d: { re: -1, im: 0 },
        g: { re: 0, im: 1 },
      };
      for (const name of PHASES) {
        expectPoint(left[name], expected[name]);
        expectPoint(right[name], expected[name]);
        expect(Math.hypot(right[name].re, right[name].im)).toBeCloseTo(1, 12);
      }
      expectPoint(left.E, quotient(raw.left.E, raw.left.c));
      expectPoint(right.E, quotient(raw.right.E, raw.right.c));
      expectPoint(left.E, { re: -1, im: 1 });
      expectPoint(right.E, left.E);
      expect(Math.hypot(right.E.re, right.E.im)).toBeCloseTo(Math.sqrt(2), 12);
    });
  }

  test("defaults to the 120-degree schematic", () => {
    expect(PHASES).toEqual(["c", "d", "g"]);
    expect(POINTS).toEqual(["c", "d", "g", "E"]);
    expect(phaseScene()).toEqual(phaseScene(1));
  });

  test("rejects values outside the three discrete turns", () => {
    for (const turn of [-1, 3, 0.5, NaN, Infinity, -Infinity, "1", null]) {
      expect(() => phaseScene(turn)).toThrow(RangeError);
    }
  });
});

describe("phase diagram coordinates", () => {
  test("maps complex directions to SVG coordinates with upward positive imaginary values", () => {
    expect(CIRCLE_RADIUS).toBe(80);
    expect(phasePoint({ re: 0, im: 0 }, 3)).toEqual({ x: 160, y: 150 });
    for (const radius of [1, 3]) {
      expect(phasePoint({ re: radius, im: 0 }, radius)).toEqual({ x: 240, y: 150 });
      expect(phasePoint({ re: -radius, im: 0 }, radius)).toEqual({ x: 80, y: 150 });
      expect(phasePoint({ re: 0, im: radius }, radius)).toEqual({ x: 160, y: 70 });
      expect(phasePoint({ re: 0, im: -radius }, radius)).toEqual({ x: 160, y: 230 });
    }
    expect(phasePoint({ re: 1.5, im: -1.5 }, 3)).toEqual({ x: 200, y: 190 });
  });

  test("all plotted points fit every scene", () => {
    for (const turn of [0, 1, 2]) {
      for (const normalized of [false, true]) {
        const { left, right, radius } = phaseScene(turn, normalized);
        for (const points of [left, right]) {
          for (const name of POINTS) {
            const { x, y } = phasePoint(points[name], radius);
            expect(x).toBeGreaterThan(0);
            expect(x).toBeLessThan(320);
            expect(y).toBeGreaterThan(0);
            expect(y).toBeLessThan(300);
          }
        }
      }
    }
  });
});
