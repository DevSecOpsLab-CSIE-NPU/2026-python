"""UVA 100 - The 3n + 1 problem

題意：
- 每行輸入一組 i, j。
- 輸出 i j max_cycle_length，其中 max_cycle_length 是區間 [min(i, j), max(i, j)]
  內所有數的最大 cycle length。

此版本特色：
- 使用記憶化（memoization）加速重複子問題。
- 保留原始輸入順序輸出（即使 i > j）。
"""

from __future__ import annotations

import sys


# memo[n] = n 的 cycle length，先放 base case
memo: dict[int, int] = {1: 1}


def cycle_length(n: int) -> int:
    """計算單一 n 的 cycle length（含起點 n 與終點 1）。"""
    if n in memo:
        return memo[n]

    path: list[int] = []
    current = n

    # 先一路推進直到遇到已知值，避免遞迴深度問題
    while current not in memo:
        path.append(current)
        if current % 2 == 1:
            current = 3 * current + 1
        else:
            current //= 2

    # current 已在 memo 裡，從已知長度倒推回 path
    length = memo[current]
    for value in reversed(path):
        length += 1
        memo[value] = length

    return memo[n]


def max_cycle_in_range(i: int, j: int) -> int:
    """回傳區間 [min(i, j), max(i, j)] 的最大 cycle length。"""
    lo, hi = (i, j) if i <= j else (j, i)
    best = 0
    for n in range(lo, hi + 1):
        c = cycle_length(n)
        if c > best:
            best = c
    return best


def solve(data: str) -> str:
    """處理多行輸入並回傳對應輸出字串。"""
    out_lines: list[str] = []

    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        i_str, j_str = line.split()
        i, j = int(i_str), int(j_str)

        best = max_cycle_in_range(i, j)
        out_lines.append(f"{i} {j} {best}")

    return "\n".join(out_lines)


def main() -> None:
    """程式進入點：讀 stdin，寫 stdout。"""
    data = sys.stdin.read()
    result = solve(data)
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
