"""Task 2: Student Ranking

輸入 n 與 k，接著讀入 n 筆學生資料：name score age。
排序規則：score 降冪、age 升冪、name 升冪。
輸出前 k 名。
"""

from __future__ import annotations

import sys


def main() -> None:
    tokens = sys.stdin.read().split()
    if len(tokens) < 2:
        return

    n = int(tokens[0])
    k = int(tokens[1])

    students = []
    idx = 2
    for _ in range(n):
        if idx + 2 >= len(tokens):
            break
        name = tokens[idx]
        score = int(tokens[idx + 1])
        age = int(tokens[idx + 2])
        students.append((name, score, age))
        idx += 3

    students.sort(key=lambda s: (-s[1], s[2], s[0]))

    lines = [f"{name} {score} {age}" for name, score, age in students[:k]]
    if lines:
        print("\n".join(lines))


if __name__ == "__main__":
    main()
