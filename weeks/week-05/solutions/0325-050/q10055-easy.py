# 檔名: q10055-easy.py
# 這是 UVA 10055 (單調函數增減性) 的簡易好記版 (Easy Version)

import sys

# 1. 一次把所有輸入讀進來，全部轉換成整數陣列
data = [int(x) for x in sys.stdin.read().split()]

if data:
    N = data[0]
    Q = data[1]
    
    # 2. 建立一個長度為 N+1 的陣列，0 代表增函數，1 代表減函數
    arr = [0] * (N + 1)
    
    idx = 2
    for _ in range(Q):
        v = data[idx]
        
        if v == 1:
            # 操作 1：反轉 f_i 的狀態。利用 1 - arr[i] 讓 0 變 1、1 變 0
            i = data[idx + 1]
            arr[i] = 1 - arr[i]
            idx += 2
            
        elif v == 2:
            # 操作 2：查詢區間 [L, R] 
            L = data[idx + 1]
            R = data[idx + 2]
            
            # 3. 暴力切片大絕招：直接把 L 到 R 的數字加總，取 2 的餘數就是答案！
            print(sum(arr[L : R + 1]) % 2)
            idx += 3