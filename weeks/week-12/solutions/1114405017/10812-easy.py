# UVA 10812 — Beat the Spread! (簡單版本)
# 這個版本使用 sys.stdin.read() 一次性讀取所有輸入，更簡單且容易記憶。

import sys  # 匯入 sys 模組，用於讀取標準輸入

# 一次性讀取所有輸入資料，並分割成列表
data = sys.stdin.read().split()  # 讀取所有輸入，分割為字串列表

# 第一個數字是測試資料組數 n
n = int(data[0])  # 轉換為整數

# 從索引 1 開始處理每組資料
index = 1  # 索引從 1 開始，因為 data[0] 是 n
for _ in range(n):  # 迴圈 n 次
    # 讀取 S 和 D
    S = int(data[index])      # 和
    D = int(data[index + 1])  # 差
    index += 2  # 索引增加 2，準備下一組
    
    # 計算兩隊分數
    a = (S + D) // 2  # 較高分
    b = (S - D) // 2  # 較低分
    
    # 檢查條件：分數非負且 S+D 為偶數
    if a >= 0 and b >= 0 and (S + D) % 2 == 0:
        print(a, b)  # 輸出分數
    else:
        print("impossible")  # 輸出 impossible