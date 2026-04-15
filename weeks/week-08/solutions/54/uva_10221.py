import math
import sys


EARTH_RADIUS = 6440.0


def normalize_degrees(angle: float, unit: str) -> float:
    if unit == "min":
        angle /= 60.0
    if angle > 180.0:
        angle = 360.0 - angle
    return angle


def distances(s: float, a: float, unit: str) -> tuple[float, float]:
    r = EARTH_RADIUS + s
    deg = normalize_degrees(a, unit)
    rad = math.radians(deg)
    arc = r * rad
    chord = 2.0 * r * math.sin(rad / 2.0)
    return arc, chord


def solve(data: str) -> str:
    out: list[str] = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        s, a, unit = line.split()
        arc, chord = distances(float(s), float(a), unit)
        out.append(f"{arc:.6f} {chord:.6f}")
    return "\n".join(out)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
