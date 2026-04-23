# 檔名: q10038-easy.py
# 這是 UVA 10038 (Jolly Jumpers) 的簡易好記版 (Easy Version)

import sys

for line in sys.stdin:
    # 1. 讀取並將整行轉成整數陣列
    parts = [int(x) for x in line.split()]
    if not parts:
        continue
        
    n = parts[0]       # 第一個數字是長度 n
    seq = parts[1:]    # 後面的才是真正的數列
    
    diffs = []
    # 2. 用最基礎的 for 迴圈計算相鄰的絕對差值，收集到陣列中
    for i in range(n - 1):
        diffs.append(abs(seq[i] - seq[i+1]))
        
    # 3. 將差值陣列由小到大排序
    diffs.sort()
    
    # 4. 判斷排序後的差值是不是剛好等於 [1, 2, ..., n-1]
    # list(range(1, n)) 會自動產生一個 1 到 n-1 的標準陣列，直接用 == 比較即可！
    if diffs == list(range(1, n)):
        print("Jolly")
    else:
        print("Not jolly")