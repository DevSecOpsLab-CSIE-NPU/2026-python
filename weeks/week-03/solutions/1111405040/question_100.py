"""
UVA 100 - 3n + 1 問題。

對每組輸入 i, j：
1. 輸出時保留原本的 i, j 順序。
2. 計算區間 [min(i, j), max(i, j)] 的最大 cycle length。
"""

from __future__ import annotations

import sys


def collatz_cycle_length(n: int, cache: dict[int, int]) -> int:
    """
    使用記憶化快取計算 n 的 cycle length。

    cycle length 會同時計入起始值 n 與結尾的 1。
    """
    original = n
    path: list[int] = []

    while n not in cache:
        path.append(n)
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2

    length = cache[n]
    for value in reversed(path):
        length += 1
        cache[value] = length

    return cache[original]


def max_cycle_length(i: int, j: int, cache: dict[int, int]) -> int:
    """回傳區間 [min(i, j), max(i, j)] 內的最大 cycle length。"""
    left = min(i, j)
    right = max(i, j)

    best = 0
    for value in range(left, right + 1):
        best = max(best, collatz_cycle_length(value, cache))
    return best


def solve(text: str) -> str:
    """處理輸入文字中的所有測資。"""
    cache: dict[int, int] = {1: 1}
    outputs: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        i, j = map(int, line.split())
        outputs.append(f"{i} {j} {max_cycle_length(i, j, cache)}")

    return "\n".join(outputs)


def main() -> None:
    """主程式進入點。"""
    data = sys.stdin.read()
    result = solve(data)
    if result:
        sys.stdout.write(result + "\n")


if __name__ == "__main__":
    main()
