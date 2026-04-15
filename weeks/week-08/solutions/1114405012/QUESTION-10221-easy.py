"""UVA 10221 - Satellites（easy 版）

步驟：
1. 半徑 r = 6440 + s
2. 把角度轉成 degree（若是 min 就除 60）
3. 角度若大於 180，改成 360-angle（取短弧）
4. 轉弧度後算弧長與弦長
"""

from __future__ import annotations

import math
import sys

BASE_R = 6440.0


def solve(raw_input: str) -> str:
    lines = [ln.strip() for ln in raw_input.splitlines() if ln.strip()]
    ans = []

    for ln in lines:
        s_str, a_str, unit = ln.split()
        s = int(s_str)
        a = int(a_str)

        r = BASE_R + s

        deg = float(a)
        if unit == "min":
            deg /= 60.0

        if deg > 180.0:
            deg = 360.0 - deg

        rad = math.radians(deg)
        arc = r * rad
        chord = 2.0 * r * math.sin(rad / 2.0)

        ans.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(ans)


def main() -> None:
    data = sys.stdin.read()
    if not data.strip():
        return
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()
