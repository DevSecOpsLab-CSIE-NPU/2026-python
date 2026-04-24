# -*- coding: utf-8 -*-
import sys

def solve(n, m, grid):
    """
    計算地雷區中每個空格周圍的地雷數量。
    :param n: 網格列數 (高度)
    :param m: 網格行數 (寬度)
    :param grid: 包含字串的串列，代表原始網格
    :return: 包含字串的串列，代表計算完成的網格
    """
    result = []
    for i in range(n):
        row = ""
        for j in range(m):
            if grid[i][j] == '*':
                row += '*'
            else:
                count = 0
                # 檢查周圍 8 個方向 (含斜角)
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        # 確保不會越界，且該位置是地雷
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '*':
                            count += 1
                row += str(count)
        result.append(row)
    return result

if __name__ == '__main__':
    field_num = 1
    
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        
        n, m = map(int, parts)
        if n == 0 and m == 0:
            break
            
        grid = [sys.stdin.readline().strip() for _ in range(n)]
        solved_grid = solve(n, m, grid)
        
        if field_num > 1:
            print() # 每組測試資料之間要輸出一個空行
            
        print(f"Field #{field_num}:")
        print('\n'.join(solved_grid))
        field_num += 1