# UVA 10908 — Largest Square
# 這個程式解決了在字元網格中，對於給定的中心點，找出所有字元相同最大正方形的邊長。

import sys  # 匯入 sys 模組，用於讀取標準輸入

def check_square(grid, r, c, k):  # 定義函數檢查以 (r, c) 為中心，邊長 k 的正方形是否所有字元相同
    half = (k - 1) // 2  # 計算半徑
    char = grid[r][c]  # 中心字元
    for i in range(r - half, r + half + 1):  # 檢查行範圍
        for j in range(c - half, c + half + 1):  # 檢查列範圍
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or grid[i][j] != char:  # 如果超出邊界或字元不同
                return False  # 返回 False
    return True  # 所有字元相同，返回 True

T = int(input())  # 讀取測試資料組數 T
for _ in range(T):  # 對於每一組測試資料
    M, N, Q = map(int, input().split())  # 讀取 M, N, Q
    grid = []  # 初始化網格列表
    for _ in range(M):  # 讀取 M 行網格
        grid.append(list(input().strip()))  # 將每行轉為字元列表
    print(M, N, Q)  # 輸出 M N Q
    for _ in range(Q):  # 對於每個查詢
        r, c = map(int, input().split())  # 讀取中心點 r, c
        max_side = 1  # 初始化最大邊長為 1
        k = 1  # 從邊長 1 開始檢查
        while True:  # 無限迴圈，直到找不到更大的
            if check_square(grid, r, c, k):  # 如果邊長 k 的正方形有效
                max_side = k  # 更新最大邊長
                k += 2  # 增加到下一個奇數邊長
            else:  # 如果無效
                break  # 停止
        print(max_side)  # 輸出最大邊長