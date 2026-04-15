"""UVA 10193 - 手打版本。"""

import math
import sys


def solve(data: str) -> str:
    rows = [line.strip() for line in data.splitlines() if line.strip()]
    total = int(rows[0])
    pos = 1
    ans = []

    for i in range(1, total + 1):
        x = int(rows[pos], 2)
        y = int(rows[pos + 1], 2)
        pos += 2

        if math.gcd(x, y) > 1:
            ans.append(f"Pair #{i}: All you need is love!")
        else:
            ans.append(f"Pair #{i}: Love is not all you need!")

    return "\n".join(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
