"""UVA 10038 Jolly Jumpers 解答。"""

from __future__ import annotations

import sys


def is_jolly(seq: list[int]) -> bool:
    """檢查序列是否為 Jolly Jumper。"""
    n = len(seq)
    if n <= 1:
        return True

    diffs = set()
    for i in range(1, n):
        diffs.add(abs(seq[i] - seq[i - 1]))

    return diffs == set(range(1, n))


def solve(data: str) -> str:
    """
    每行一組測資：n + n 個整數。
    若序列是 jolly jumper 輸出 `Jolly`，否則輸出 `Not jolly`。
    """
    outputs: list[str] = []

    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        nums = list(map(int, line.split()))
        n = nums[0]
        seq = nums[1 : 1 + n]

        outputs.append("Jolly" if is_jolly(seq) else "Not jolly")

    if not outputs:
        return ""

    return "\n".join(outputs) + "\n"


def main() -> None:
    """標準輸入輸出入口。"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
