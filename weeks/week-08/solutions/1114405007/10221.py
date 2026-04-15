"""UVA 10221 - 手打版本。"""

import math
import sys


def solve(data: str) -> str:
    answers = []

    for raw in data.splitlines():
        raw = raw.strip()
        if not raw:
            continue

        s_str, a_str, unit = raw.split()
        s = float(s_str)
        a = float(a_str)

        if unit == "min":
            a /= 60.0

        if a > 180.0:
            a = 360.0 - a

        radius = 6440.0 + s
        theta = math.radians(a)

        arc_len = radius * theta
        chord_len = 2.0 * radius * math.sin(theta / 2.0)

        answers.append(f"{arc_len:.6f} {chord_len:.6f}")

    return "\n".join(answers)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
