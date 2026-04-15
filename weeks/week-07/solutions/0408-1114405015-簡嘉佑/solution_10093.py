"""
UVA 10093 - 炮兵部隊部署最大化

題目描述：
在 N×M 網格上部署炮兵，避免互相攻擊。
攻擊範圍：上下各 2 格、左右各 2 格。
最多能部署多少支炮兵？

解法：
使用回溯法（backtracking）逐個位置嘗試放置或不放置炮兵。
檢查每個位置是否與已放置的炮兵衝突。
"""

from __future__ import annotations

from typing import List


def solve_artillery(n: int, m: int, grid: List[str]) -> int:
    """
    計算最多能部署的炮兵數。
    
    參數：
        n: 行數
        m: 列數
        grid: 地圖，grid[i][j] = 'P' (平原) 或 'H' (山地)
    
    回傳：最多炮兵數
    """
    max_count = [0]

    def can_place(r: int, c: int, placed: List[tuple]) -> bool:
        """檢查 (r, c) 是否能放置炮兵。"""
        if grid[r][c] == "H":
            return False
        for pr, pc in placed:
            # 距離在 1 到 2 之間時不能共存
            if abs(pr - r) <= 2 and abs(pc - c) <= 2 and (pr != r or pc != c):
                return False
        return True

    def backtrack(row: int, col: int, placed: List[tuple]) -> None:
        """按行按列掃描，嘗試每個位置放或不放。"""
        # 掃描完成（已處理完所有位置）
        if row >= n:
            max_count[0] = max(max_count[0], len(placed))
            return

        # 計算下一個位置
        next_row = row
        next_col = col + 1
        if next_col >= m:
            next_row += 1
            next_col = 0

        # 在當前位置不放置
        backtrack(next_row, next_col, placed)

        # 在當前位置放置（如果可以）
        if can_place(row, col, placed):
            backtrack(next_row, next_col, placed + [(row, col)])

    backtrack(0, 0, [])
    return max_count[0]


def main() -> None:
    """主程式：讀入輸入並輸出結果。"""
    import sys

    lines = sys.stdin.read().strip().split("\n")
    n, m = map(int, lines[0].split())
    grid = [lines[i + 1] for i in range(n)]

    result = solve_artillery(n, m, grid)
    sys.stdout.write(str(result))


if __name__ == "__main__":
    main()
