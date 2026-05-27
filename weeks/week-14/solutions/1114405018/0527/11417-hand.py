from __future__ import annotations 

from math import gcd
import re

def solve() -> None:
    answers: list[str] = []
    for line in sys.stdin:
        n=int(line)
        if n==0:
            break

        total = sum(gcd(i, j) for i in range(1, n) for j in range(i + 1, n + 1))
        answers.append(str(total))

    sys.stdout.write("\n:".join(answers))

if __name__ == "__main__":
    solve()
    
