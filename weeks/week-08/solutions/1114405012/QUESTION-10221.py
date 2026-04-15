"""UVA 10221 - Satellites

正式版：統一角度為度數後取較小中心角，再計算弧長與弦長。
"""

from __future__ import annotations

import math
import sys

EARTH_RADIUS = 6440.0


def calc_arc_and_chord(s: int, a: int, unit: str) -> tuple[float, float]:
    """回傳弧長與弦長（公里）。"""
    radius = EARTH_RADIUS + float(s)

    angle_deg = float(a)
    if unit == "min":
        angle_deg /= 60.0

    # 兩點間路徑取較短弧，所以中心角限制在 [0, 180]。
    if angle_deg > 180.0:
        angle_deg = 360.0 - angle_deg

    angle_rad = math.radians(angle_deg)
    arc = radius * angle_rad
    chord = 2.0 * radius * math.sin(angle_rad / 2.0)
    return arc, chord


def solve(raw_input: str) -> str:
    lines = [line.strip() for line in raw_input.splitlines() if line.strip()]
    outputs = []

    for line in lines:
        s_str, a_str, unit = line.split()
        arc, chord = calc_arc_and_chord(int(s_str), int(a_str), unit)
        outputs.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(outputs)


def main() -> None:
    data = sys.stdin.read()
    if not data.strip():
        return
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()
