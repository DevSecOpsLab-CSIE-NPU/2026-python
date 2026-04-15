"""UVA 10193 - easy 版本（含中文註解）。"""

import math
import sys


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    t = int(lines[0])
    out = []
    idx = 1

    for case_no in range(1, t + 1):
        a_bin = lines[idx]
        b_bin = lines[idx + 1]
        idx += 2

        a = int(a_bin, 2)
        b = int(b_bin, 2)

        if math.gcd(a, b) > 1:
            out.append(f"Pair #{case_no}: All you need is love!")
        else:
            out.append(f"Pair #{case_no}: Love is not all you need!")

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
