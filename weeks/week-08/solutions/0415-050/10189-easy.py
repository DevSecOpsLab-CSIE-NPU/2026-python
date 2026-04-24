# -*- coding: utf-8 -*-
# 這是 UVA 10189 (Minesweeper) 的簡易好記版 (Easy Version)
import sys

def solve(n, m, grid):
    """
    簡易好記秘訣：【加一圈外框 (Padding)】
    在地圖外圍加一圈 '.'，這樣在算周圍 8 格時就不會越界 (IndexError)，
    可以把煩人的邊界判斷 if 條件全部刪掉！
    """
    # 1. 幫地圖加上下左右的 '.' 外框
    padded_grid = ['.' * (m + 2)]
    for row in grid:
        padded_grid.append('.' + row + '.')
    padded_grid.append('.' * (m + 2))
    
    result = []
    # 2. 原始座標 (0,0) 因為加了外框，會平移變成從 (1,1) 開始
    for i in range(1, n + 1):
        row_result = ""
        for j in range(1, m + 1):
            if padded_grid[i][j] == '*':
                row_result += '*'
            else:
                count = 0
                # 3. 直接暴力雙迴圈掃描 9 宮格！
                # (因為自己這格一定是 '.'，所以就算掃到自己也不會多算地雷)
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if padded_grid[i+dx][j+dy] == '*':
                            count += 1
                row_result += str(count)
        result.append(row_result)
    return result

if __name__ == '__main__':
    # 萬用讀取法：把所有輸入切成一維陣列，不用再煩惱換行跟空白
    data = sys.stdin.read().split()
    idx = 0; field_num = 1
    
    while idx < len(data):
        n, m = int(data[idx]), int(data[idx+1])
        idx += 2
        if n == 0 and m == 0: break
        grid = data[idx : idx+n]; idx += n
        if field_num > 1: print() # 測資之間空一行
        print(f"Field #{field_num}:\n" + '\n'.join(solve(n, m, grid)))
        field_num += 1