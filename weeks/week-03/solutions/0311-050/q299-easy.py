# 檔名: q299-easy.py
# 這是 UVA 299 的簡易好記版 (Easy Version)

import sys

# 1. 一次把所有輸入讀進來，用空白/換行切成一個一個的純字串列表
data = sys.stdin.read().split()

if data:
    test_cases = int(data[0])
    idx = 1  # 建立一個指標，用來記錄我們目前讀到哪裡了
    
    for _ in range(test_cases):
        L = int(data[idx])  # 這台火車有幾節車廂
        idx += 1
        
        # 2. 利用 Python 切片技巧，一口氣把這 L 節車廂的數字抓出來轉成 int
        arr = [int(x) for x in data[idx : idx + L]]
        idx += L
        
        swaps = 0
        # 3. 最基礎、最暴力的氣泡排序法 (Bubble Sort)
        # 外層控制要跑幾回合，內層負責相鄰交換。
        for i in range(L):
            for j in range(L - 1):  # 簡化版：每次都固定從頭檢查相鄰兩個
                # 如果前面的數字比後面的數字大，就把它們交換位置
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swaps += 1  # 記錄交換了一次
                    
        # 4. 印出結果
        print(f"Optimal train swapping takes {swaps} swaps.")