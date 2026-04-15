"""
UVA 10221 - Satellites
AI 教學簡單版本（含中文註解）
"""

import math
import sys


def solve(data: str) -> str:
    out = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        s_str, a_str, unit = line.split()
        s = float(s_str)
        a = float(a_str)

        # unit = min 代表角分，要先轉成度
        if unit == "min":
            a = a / 60.0

        # 題目要取較短弧，中心角大於 180 時改成 360-a
        if a > 180.0:
            a = 360.0 - a

        r = 6440.0 + s
        rad = math.radians(a)

        arc = r * rad
        chord = 2.0 * r * math.sin(rad / 2.0)

        out.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(out)


def main() -> None:
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
