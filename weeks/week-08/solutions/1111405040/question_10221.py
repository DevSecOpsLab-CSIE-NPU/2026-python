"""
UVA 10221: Satellites
"""

from __future__ import annotations

import math
import sys


EARTH_RADIUS = 6440.0


def normalize_angle_degrees(angle: float, unit: str) -> float:
    """將角度轉成度，並取較短的圓心角。"""
    if unit == "min":
        angle /= 60.0

    angle %= 360.0
    if angle > 180.0:
        angle = 360.0 - angle

    return angle


def satellite_distances(height: float, angle: float, unit: str) -> tuple[float, float]:
    """計算弧長與弦長。"""
    radius = EARTH_RADIUS + height
    degrees = normalize_angle_degrees(angle, unit)
    radians = math.radians(degrees)

    arc = radius * radians
    chord = 2.0 * radius * math.sin(radians / 2.0)
    return arc, chord


def solve(text: str) -> str:
    """逐行處理衛星距離資料。"""
    outputs: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        height_text, angle_text, unit = line.split()
        arc, chord = satellite_distances(float(height_text), float(angle_text), unit)
        outputs.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
