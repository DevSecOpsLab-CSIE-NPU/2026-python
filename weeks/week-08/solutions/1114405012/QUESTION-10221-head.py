"""UVA 10221 - Satellites（手打版）

手打流程：
1. 先算衛星軌道半徑 r = 6440 + s。
2. 若單位是 min，角度先除以 60 轉成 degree。
3. 角度若超過 180，改成 360-a（走短弧）。
4. 弧長 = r * 弧度；弦長 = 2*r*sin(弧度/2)。
"""

from __future__ import annotations

import math
import sys

EARTH_R = 6440.0


def one_case(s: int, a: int, unit: str) -> tuple[float, float]:
    """計算單筆弧長與弦長。"""
    r = EARTH_R + float(s)

    deg = float(a)
    if unit == "min":
        deg /= 60.0

    if deg > 180.0:
        deg = 360.0 - deg

    rad = math.radians(deg)
    arc = r * rad
    chord = 2.0 * r * math.sin(rad / 2.0)
    return arc, chord


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    ans: list[str] = []

    for line in lines:
        s_str, a_str, unit = line.split()
        arc, chord = one_case(int(s_str), int(a_str), unit)
        ans.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(ans)


def main() -> None:
    raw = sys.stdin.read()
    if not raw.strip():
        return
    sys.stdout.write(solve(raw))


if __name__ == "__main__":
    main()
