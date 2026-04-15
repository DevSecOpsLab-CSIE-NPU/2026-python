"""
UVA 10221 - Satellites
簡單版（CPE 現場可手打）
"""

import math


def solve() -> None:
    import sys

    out = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        s_str, a_str, unit = line.split()
        s = float(s_str)
        a = float(a_str)

        # min 代表角分，先轉成角度
        if unit == "min":
            a = a / 60.0

        # 要取較短路徑的中心角，所以超過 180 度就轉成 360-a
        if a > 180.0:
            a = 360.0 - a

        r = 6440.0 + s
        rad = math.radians(a)

        # 弧長與弦長公式
        arc = r * rad
        chord = 2.0 * r * math.sin(rad / 2.0)

        out.append(f"{arc:.6f} {chord:.6f}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
