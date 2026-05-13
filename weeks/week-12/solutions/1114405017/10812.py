# UVA 10812 — Beat the Spread!
# 這個程式解決了超級盃賭局的問題：給定兩隊分數的和 S 與差 D，找出兩隊的分數。

import sys  # 匯入 sys 模組，用於讀取標準輸入

# 讀取測試資料組數 n
n = int(input())  # 從標準輸入讀取第一行，轉換為整數

# 對於每一組測試資料
for _ in range(n):  # 迴圈執行 n 次
    # 讀取和 S 與差 D
    S, D = map(int, input().split())  # 從標準輸入讀取一行，分割為兩個整數
    
    # 計算較高分和較低分
    # 較高分 = (S + D) / 2
    # 較低分 = (S - D) / 2
    high = (S + D) // 2  # 使用整數除法計算較高分
    low = (S - D) // 2   # 使用整數除法計算較低分
    
    # 檢查條件：S + D 必須為偶數，且兩分數必須為非負整數
    if (S + D) % 2 != 0 or (S - D) % 2 != 0 or high < 0 or low < 0:
        # 如果不符合條件，輸出 impossible
        print("impossible")
    else:
        # 如果有解，輸出較大的分數在前，較小的在後
        print(high, low)