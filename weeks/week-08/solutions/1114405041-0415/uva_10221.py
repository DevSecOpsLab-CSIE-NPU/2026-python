from __future__ import annotations

import math
import sys


EARTH_RADIUS = 6440


def solve(data: str) -> str:
    outputs: list[str] = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        s_text, a_text, unit = line.split()
        radius = EARTH_RADIUS + int(s_text)
        angle = float(a_text)

        if unit == "min":
            angle /= 60

        if angle > 180:
            angle = 360 - angle

        theta = math.radians(angle)
        arc = radius * theta
        chord = 2 * radius * math.sin(theta / 2)
        outputs.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
