from __future__ import annotations

import sys


# 快取已計算過的 cycle length，避免重複計算。
memo: dict[int, int] = {1: 1}


def cycle_length(n: int) -> int:
    """回傳 n 的 Collatz cycle length（長度包含起點與終點 1）。"""
    # 記住原始 n，最後要回傳它的長度。
    original = n
    # path 用來暫存「尚未在 memo 出現」的路徑節點。
    path = []

    # 一路推進到遇到已知長度的節點為止。
    while n not in memo:
        path.append(n)
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2

    # 從已知節點反推回 path，逐一回填快取。
    length = memo[n]
    for value in reversed(path):
        length += 1
        memo[value] = length

    return memo[original]


def max_cycle_length(i: int, j: int) -> int:
    """計算區間 [min(i, j), max(i, j)] 的最大 cycle length。"""
    # 題目允許 i > j，因此先正規化區間。
    start, end = (i, j) if i <= j else (j, i)
    best = 0

    for value in range(start, end + 1):
        current = cycle_length(value)
        if current > best:
            best = current

    return best


def solve(data: str) -> str:
    """將多行輸入轉成對應輸出，每行格式為：i j max_cycle。"""
    lines = []

    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        i_str, j_str = line.split()
        i, j = int(i_str), int(j_str)
        # 輸出時保留原始輸入順序的 i 與 j。
        lines.append(f"{i} {j} {max_cycle_length(i, j)}")

    return "\n".join(lines)


def main() -> None:
    """標準輸入/輸出進入點，符合 UVA 線上判題格式。"""
    data = sys.stdin.read()
    if not data:
        return

    result = solve(data)
    if result:
        sys.stdout.write(result + "\n")


if __name__ == "__main__":
    main()
