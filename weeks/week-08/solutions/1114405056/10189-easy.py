# 踩地雷：讀入地圖，計算每格周圍有幾顆地雷

case = 0  # 第幾個測試案例

while True:
    line = input().split()
    n, m = int(line[0]), int(line[1])

    # 輸入 0 0 代表結束
    if n == 0 and m == 0:
        break

    # 讀入地圖，每列是一個字串
    grid = []
    for _ in range(n):
        grid.append(input())

    case += 1

    # 測試案例之間要空一行
    if case > 1:
        print()

    print(f"Field #{case}:")

    # 遍歷每一格
    for i in range(n):
        row = ""
        for j in range(m):
            if grid[i][j] == '*':
                # 本格是地雷，直接輸出 *
                row += '*'
            else:
                # 計算周圍 8 個方向有幾顆地雷
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue  # 跳過自己
                        ni, nj = i + di, j + dj
                        # 確認鄰格在範圍內且是地雷
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '*':
                            count += 1
                row += str(count)
        print(row)
