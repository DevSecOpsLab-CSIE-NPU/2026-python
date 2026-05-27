from __future__ import annotations

import math
import sys

def solve() -> None:
    results: list[str] = []
    for lin in sys.stdin:
        a, b = map(int, lin.split())
        if a == 0 and b == 0:
            break

        results.append(str(math.isqrt(b) - math.isqrt(a -1)))

    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()
    
