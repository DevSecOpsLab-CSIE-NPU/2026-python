from __future__ import annotations

import math
import sys


EARTH_RADIUS = 6440


def solve(data: str) -> str:
    """
    簡單版做法：
    1. 先算衛星到地心的半徑 r = 6440 + s。
    2. 如果角度是分(min)，先除以 60 變成度。
    3. 因為圓周上有兩段弧，我們只取比較短的那一段，所以角度大於 180 時改成 360-a。
    4. 弧長 = r × θ，弦長 = 2r × sin(θ/2)。
    """
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
        arc_length = radius * theta
        chord_length = 2 * radius * math.sin(theta / 2)
        outputs.append(f"{arc_length:.6f} {chord_length:.6f}")

    return "\n".join(outputs)


def main() -> None:
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()
