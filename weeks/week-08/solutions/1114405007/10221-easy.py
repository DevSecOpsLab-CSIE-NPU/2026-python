"""UVA 10221 - easy 版本（含中文註解）。"""

import math
import sys

EARTH_RADIUS = 6440.0


def solve(data: str) -> str:
    out = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        s_str, a_str, unit = line.split()
        s = float(s_str)
        angle = float(a_str)

        if unit == "min":
            angle /= 60.0

        # 只需要較短的那段圓弧，所以角度大於 180 要轉成 360-angle
        if angle > 180.0:
            angle = 360.0 - angle

        r = EARTH_RADIUS + s
        rad = math.radians(angle)

        arc = r * rad
        chord = 2.0 * r * math.sin(rad / 2.0)
        out.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
