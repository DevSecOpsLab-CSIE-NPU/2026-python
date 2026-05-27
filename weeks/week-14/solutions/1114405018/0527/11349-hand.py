from __future__ import annotatinons

import re
import sys

def solve() -> None:

    date = list(map(int, re.findall(r"-?\d+", sys.stdin.read())))
    if not date:
        return
    
    t = date[0]
    idx = 1
    answers: list[str] = []

    for case_no in range(1, t + 1):
        n = date[idx]
        idx += 1

        ok = True
        matrix: list[list[int]] = []
        for _ in range(n):
            row = date[idx:idx + n]
            idx += n
            matrix.append(row)
            if any(value < 0 for value in row):
                ok = False

        for i in range(n):
            for j in range(n):
                if matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                    ok = False

        answers.append(f"Test #{case_no}: {'Symmetric.' if ok else 'Non-symmetric.'}")

    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    solve()