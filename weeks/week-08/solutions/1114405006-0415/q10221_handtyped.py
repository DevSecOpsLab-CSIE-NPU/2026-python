"""
UVA 10221 - Satellites
手打版本
"""

import math
import sys


def run(text: str) -> str:
    ans = []

    for row in text.splitlines():
        row = row.strip()
        if row == "":
            continue

        s_raw, a_raw, unit = row.split()
        s = float(s_raw)
        a = float(a_raw)

        if unit == "min":
            a = a / 60.0

        if a > 180.0:
            a = 360.0 - a

        r = 6440.0 + s
        rad = math.radians(a)

        arc = r * rad
        chord = 2.0 * r * math.sin(rad / 2.0)

        ans.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(ans)


def main() -> None:
    text = sys.stdin.read()
    print(run(text))


if __name__ == "__main__":
    main()
