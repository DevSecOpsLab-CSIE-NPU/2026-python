"""
UVA 10093 - 炮兵部隊部署最大化（簡易版本）

問題：N×M 網格，部署炮兵，攻擊範圍上下左右各 2 格。
目標：最多能部署多少支炮兵？

思路：
回溯法：逐個位置嘗試放置或不放置炮兵。
檢查每個位置是否與已放置的炮兵衝突。
"""

from __future__ import annotations

from typing import List


def solve(n: int, m: int, grid: List[str]) -> int:
    """求最多炮兵數。"""
    max_count = [0]

    def can_place(r: int, c: int, placed: List[tuple]) -> bool:
        """檢查 (r, c) 是否能放置。"""
        if grid[r][c] == "H":
            return False
        for pr, pc in placed:
            if abs(pr - r) <= 2 and abs(pc - c) <= 2 and (pr != r or pc != c):
                return False
        return True

    def backtrack(row: int, col: int, placed: List[tuple]) -> None:
        """回溯掃描每個位置。"""
        # 掃描完成
        if row >= n:
            max_count[0] = max(max_count[0], len(placed))
            return

        # 計算下一個位置
        next_row = row
        next_col = col + 1
        if next_col >= m:
            next_row += 1
            next_col = 0

        # 不放置
        backtrack(next_row, next_col, placed)

        # 嘗試放置
        if can_place(row, col, placed):
            backtrack(next_row, next_col, placed + [(row, col)])

    backtrack(0, 0, [])
    return max_count[0]


def main() -> None:
    """讀入並輸出結果。"""
    import sys

    lines = sys.stdin.read().strip().split("\n")
    n, m = map(int, lines[0].split())
    grid = [lines[i + 1] for i in range(n)]
    print(solve(n, m, grid))


if __name__ == "__main__":
    main()
