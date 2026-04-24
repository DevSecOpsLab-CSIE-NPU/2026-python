# 檔名: q10057-easy.py
# 這是 UVA 10057 (A mid-summer night's dream) 的簡易好記版 (Easy Version)

import sys

# 1. 萬用讀取法：把所有輸入切成一維整數陣列
data = [int(x) for x in sys.stdin.read().split()]

idx = 0
while idx < len(data):
    n = data[idx]
    idx += 1
    
    arr = data[idx : idx + n]  # 抓出這組測資的 n 個數字
    idx += n
    
    # 2. 找中位數的黃金法則：先排序！
    arr.sort()
    
    # 3. 統一奇偶數的寫法 (免寫 if-else)
    mid1 = arr[(n - 1) // 2]  # 左中位數 (奇數時為正中間)
    mid2 = arr[n // 2]        # 右中位數 (奇數時也為正中間)
    
    # 答案 2：輸入中有多少個數字落在 [mid1, mid2] 這個最佳解區間內
    count = 0
    for x in arr:
        if mid1 <= x <= mid2:
            count += 1
            
    # 印出結果： 最小的A、陣列中符合條件的個數、可能值的總數
    print(f"{mid1} {count} {mid2 - mid1 + 1}")