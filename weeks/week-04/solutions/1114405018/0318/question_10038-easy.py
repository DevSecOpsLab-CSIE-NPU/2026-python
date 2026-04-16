"""UVA 10038 - Jolly Jumpers（easy 版）

題目重點：
1. 每行輸入一個序列：第一個數字是長度 n，後面接 n 個整數。
2. 若相鄰數字差值的絕對值，剛好涵蓋 1 到 n-1（各一次）→ Jolly。
3. 否則輸出 Not jolly。

這個 easy 版本的核心想法：
- 直接把所有相鄰差值絕對值放進集合 diffs。
- 再和標準答案集合 {1,2,...,n-1} 比較是否完全相同。
"""

import sys

# 逐行讀取測資（直到 EOF）
for line in sys.stdin:
    # 移除前後空白與換行
    line = line.strip()

    # 空行略過
    if not line:
        continue

    # 解析整行數字
    # arr[0] 是 n，arr[1:] 是實際序列
    arr = list(map(int, line.split()))
    n = arr[0]
    nums = arr[1:]

    # n=0 或 n=1 時，沒有相鄰差值要檢查，視為 Jolly
    if n <= 1:
        print("Jolly")
        continue

    # 計算所有相鄰元素差值絕對值
    # 例：nums = [1, 4, 2, 3] -> diffs = {3,2,1}
    diffs = {abs(nums[i] - nums[i - 1]) for i in range(1, n)}

    # 標準應有差值集合為 {1, 2, ..., n-1}
    # 完全一致才是 Jolly
    print("Jolly" if diffs == set(range(1, n)) else "Not jolly")
