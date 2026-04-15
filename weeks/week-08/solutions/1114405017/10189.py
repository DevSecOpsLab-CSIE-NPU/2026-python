import sys

def solve():
    # 使用 sys.stdin.read().split() 快速讀取所有輸入並依空格/換行切分
    input_data = sys.stdin.read().split()
    idx = 0
    field_count = 1 # 用來追蹤當前是第幾組測試資料
    
    while idx < len(input_data):
        # 讀取行數 n 與列數 m
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2
        
        # 題目規定：當 n=0, m=0 時結束程式
        if n == 0 and m == 0:
            break
        
        # 讀取地圖資料，將每一行轉為 list 方便後續存取
        grid = []
        for i in range(n):
            grid.append(list(input_data[idx]))
            idx += 1
            
        # 格式控制：除了第一組資料外，每組資料輸出前都要先換一行
        if field_count > 1:
            print()
            
        print(f"Field #{field_count}:")
        
        # 開始遍歷網格中的每一個格子 (r: row, c: col)
        for r in range(n):
            row_result = "" # 用來儲存這一行計算後的結果
            for c in range(m):
                # 如果當前位置是地雷，直接保留 '*'
                if grid[r][c] == '*':
                    row_result += '*'
                else:
                    # 如果是空白格 '.'，則開始掃描周圍 8 個方位
                    mine_count = 0
                    # dr, dc 代表列與行的位移 (Delta Row, Delta Col)
                    # 範圍從 -1 到 1，涵蓋上、下、左、右及四個斜對角
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            # 跳過偏移量皆為 0 的情況（即自己本身）
                            if dr == 0 and dc == 0:
                                continue
                            
                            nr, nc = r + dr, c + dc # 計算鄰居格子的座標
                            
                            # 邊界檢查：確保鄰居座標沒有超出地圖範圍
                            if 0 <= nr < n and 0 <= nc < m:
                                # 如果鄰居是地雷，計數加 1
                                if grid[nr][nc] == '*':
                                    mine_count += 1
                    
                    # 將計算出的地雷總數轉為字串並加入行結果中
                    row_result += str(mine_count)
            
            # 輸出一整行計算完成的結果
            print(row_result)
            
        # 組號遞增
        field_count += 1

if __name__ == "__main__":
    solve()