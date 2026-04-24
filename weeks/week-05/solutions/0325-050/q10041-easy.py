# 檔名: q10041-easy.py
# 這是 UVA 10041 (Vito's Family) 的簡易好記版 (Easy Version)

import sys

# 1. 一次讀取所有輸入，並直接全部轉換為整數陣列
data = [int(x) for x in sys.stdin.read().split()]

if data:
    test_cases = data[0]
    idx = 1
    
    for _ in range(test_cases):
        r = data[idx]  # 親戚的數量
        idx += 1
        
        relatives = data[idx : idx + r]  # 抓出這 r 個親戚的門牌號碼
        idx += r
        
        # 2. 排序並找出中位數 (數量為偶數時，取 r // 2 左邊那個剛好符合最佳解)
        relatives.sort()
        median = relatives[r // 2]
        
        # 3. 計算所有親戚家到中位數的絕對距離總和
        total_distance = 0
        for x in relatives:
            total_distance += abs(x - median)
            
        print(total_distance)