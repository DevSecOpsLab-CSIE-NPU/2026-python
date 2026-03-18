"""QUESTION-10038 easy 版。

判斷 Jolly Jumper 的方法很好記：
1. 長度是 n，就應該剛好出現差值 1 到 n-1。
2. 逐一計算相鄰兩數的絕對差。
3. 若差值超出範圍，或某個差值重複出現，就直接判定失敗。

這版不用集合做最終比對，而是用布林陣列逐格標記，
很適合考場手打。
"""

from __future__ import annotations

import sys


def check_jolly(sequence: list[int]) -> bool:
    n = len(sequence)
    if n <= 1:
        return True

    seen = [False] * n

    for index in range(1, n):
        diff = abs(sequence[index] - sequence[index - 1])

        if diff < 1 or diff >= n:
            return False
        if seen[diff]:
            return False

        seen[diff] = True

    for diff in range(1, n):
        if not seen[diff]:
            return False

    return True


def solve(text: str) -> str:
    answers = []

    for line in text.splitlines():
        if not line.strip():
            continue

        data = list(map(int, line.split()))
        n = data[0]
        sequence = data[1 : 1 + n]

        if check_jolly(sequence):
            answers.append("Jolly")
        else:
            answers.append("Not jolly")

    return "\n".join(answers)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
