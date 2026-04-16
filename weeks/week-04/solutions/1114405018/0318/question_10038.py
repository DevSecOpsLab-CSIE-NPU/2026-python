"""UVA 10038 - Jolly Jumpers

逐行讀入：
- 每行第一個數字為 n
- 後面接 n 個整數
判斷是否為 Jolly jumper。
"""

from __future__ import annotations

import sys


def is_jolly(seq: list[int]) -> bool:
    n = len(seq)
    if n <= 1:
        return True

    diffs = set()
    for i in range(1, n):
        d = abs(seq[i] - seq[i - 1])
        if d < 1 or d >= n:
            return False
        diffs.add(d)

    return len(diffs) == n - 1


def solve(data: str) -> str:
    out = []

    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        nums = list(map(int, line.split()))
        n = nums[0]
        seq = nums[1 : 1 + n]

        out.append("Jolly" if is_jolly(seq) else "Not jolly")

    return "\n".join(out)


def main() -> None:
    result = solve(sys.stdin.read())
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
