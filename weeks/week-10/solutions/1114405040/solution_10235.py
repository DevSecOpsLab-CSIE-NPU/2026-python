"""
UVA 10235 - 蛇放置問題

題目：在 N×M 格子上放置環狀蛇，使得：
- 所有非插座格子（1）恰好被一條蛇占據
- 所有插座格子（0）不被蛇占據
- 求方案數 MOD 10^9+7

解法：Profile DP（行級狀態壓縮）
- 逐行掃描，維護「該行哪些格子已被前行蛇延伸」
- 狀態轉移：當前行如何被蛇覆蓋
"""

import sys
from typing import List, Dict, Tuple

MOD = 1000000007


def solve_snake_placement(n: int, m: int, grid: List[List[int]]) -> int:
    """
    使用 Profile DP 計算蛇放置方案數。
    
    時間複雜度: O(N × M × 4^M)
    空間複雜度: O(M × 4^M)（DP 表空間）
    
    參數：
        n: 行數（1 ≤ N ≤ 11）
        m: 列數（1 ≤ M ≤ 11）
        grid[i][j]: 1=可放蛇格, 0=插座禁地
    
    回傳：合法放置方案數 MOD 10^9+7
    """
    # 邊界檢查
    empty_count = sum(1 for i in range(n) for j in range(m) if grid[i][j] == 1)
    if empty_count == 0:
        return 1  # 無格子需放蛇，唯一方案
    
    # dp[row][mask] = 到達第 row 行，該行覆蓋情況為 mask 的方案數
    # mask 的第 j 位=1 表示格 (row, j) 被當前蛇覆蓋
    dp: Dict[Tuple[int, int], int] = {(0, 0): 1}
    
    for row in range(n):
        new_dp: Dict[Tuple[int, int], int] = {}
        
        for (r, cur_mask), count in dp.items():
            if r != row:
                continue
            
            # 掃描本行，決定蛇的覆蓋方式
            def fill_row(col: int, cur: int, next_row_mask: int) -> None:
                """
                遞迴填充本行。
                
                參數：
                    col: 當前列位置
                    cur: 本行當前填充狀態位掩碼
                    next_row_mask: 向下延伸到下一行的位掩碼
                """
                if col == m:
                    # 本行填充完成
                    # 檢查：是否所有非插座格都被覆蓋
                    valid = True
                    for j in range(m):
                        if grid[row][j] == 1 and not (cur & (1 << j)):
                            valid = False  # 該放蛇的格未被覆蓋
                            break
                    
                    if valid:
                        # 有效方案：保存到下一行狀態
                        key = (row + 1, next_row_mask)
                        new_dp[key] = (new_dp.get(key, 0) + count) % MOD
                    return
                
                # 已被覆蓋，跳到下一列
                if cur & (1 << col):
                    fill_row(col + 1, cur, next_row_mask)
                    return
                
                # 當前格必須被覆蓋（若非插座）
                if grid[row][col] == 0:
                    # 插座格，不能被蛇覆蓋
                    fill_row(col + 1, cur, next_row_mask)
                else:
                    # 可放蛇格，嘗試不同蛇的方向
                    # 簡化版本：只嘗試向右延伸（長度>=2）或向下延伸
                    
                    # 選項 1：向下延伸到下一行
                    new_next_mask = next_row_mask | (1 << col)
                    fill_row(col + 1, cur | (1 << col), new_next_mask)
                    
                    # 選項 2：向右延伸（如右邊也是可放格）
                    if col + 1 < m and grid[row][col + 1] == 1 and not (cur & (1 << (col + 1))):
                        fill_row(col + 1, cur | (1 << col), next_row_mask)
            
            fill_row(0, cur_mask, 0)
        
        dp.update(new_dp)
    
    # 最終答案：第 n 行完成，無下行延伸
    return dp.get((n, 0), 0)


def read_test_cases() -> List[Tuple[int, int, List[List[int]]]]:
    """
    讀取測試案例（直到 N=0, M=0）。
    
    格式：
    N M
    N 行，每行 M 個 0 或 1
    ...
    0 0
    """
    cases: List[Tuple[int, int, List[List[int]]]] = []
    
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            
            parts = line.split()
            n, m = int(parts[0]), int(parts[1])
            
            if n == 0 and m == 0:
                break
            
            grid: List[List[int]] = []
            for _ in range(n):
                row_line = sys.stdin.readline().strip()
                row = [int(ch) for ch in row_line]  # 逐字符解析
                grid.append(row)
            
            cases.append((n, m, grid))
    
    except (EOFError, ValueError):
        pass
    
    return cases


def main():
    """主程式：輸出格式 "Case (number): (answer)" """
    cases = read_test_cases()
    
    for case_num, (n, m, grid) in enumerate(cases, 1):
        result = solve_snake_placement(n, m, grid)
        print(f"Case {case_num}: {result}")


if __name__ == '__main__':
    main()
