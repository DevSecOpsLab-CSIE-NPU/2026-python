# 簡單版 Minesweeper 程式
# 使用繁體中文註解說明

import sys

def main():
    # 初始化場地編號
    field_num = 1
    # 讀取所有輸入行
    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line:
            continue
        # 讀取行數和列數
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        # 讀取網格
        grid = []
        for _ in range(n):
            row = list(lines[i].strip())
            grid.append(row)
            i += 1
        
        # 處理網格，為每個空白格子計算周圍地雷數量
        result = []
        for x in range(n):  # 遍歷每一行
            new_row = []
            for y in range(m):  # 遍歷每一列
                if grid[x][y] == '*':
                    # 如果是地雷，保持不變
                    new_row.append('*')
                else:
                    # 計算周圍8個方向的地雷數量
                    count = 0
                    # 檢查所有相鄰位置
                    for dx in [-1, 0, 1]:  # 行偏移
                        for dy in [-1, 0, 1]:  # 列偏移
                            if dx == 0 and dy == 0:
                                continue  # 跳過自己
                            nx, ny = x + dx, y + dy
                            # 檢查是否在網格內且是地雷
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '*':
                                count += 1
                    new_row.append(str(count))
            result.append(''.join(new_row))
        
        # 輸出結果
        print(f"Field #{field_num}:")
        for row in result:
            print(row)
        print()  # 空行分隔
        field_num += 1

if __name__ == "__main__":
    main()