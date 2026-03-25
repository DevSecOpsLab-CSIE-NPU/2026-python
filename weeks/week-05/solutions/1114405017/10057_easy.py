import sys

# 將所有輸入一次讀進來，變成一個大清單
data = sys.stdin.read().split()
i = 0

while i < len(data):
    n = int(data[i])
    i += 1
    # 讀取接下來的 n 個數字並排序
    nums = sorted(map(int, data[i : i + n]))
    i += n
    
    # 取得中位數區間的左端點與右端點
    m1 = nums[(n - 1) // 2]
    m2 = nums[n // 2]
    
    # 計算在 nums 中落在 [m1, m2] 範圍內的個數
    # (簡單好記的寫法：直接遍歷算個數)
    count = sum(1 for x in nums if m1 <= x <= m2)
    
    # 計算 A 的可能種類：右端點 - 左端點 + 1
    ans = m2 - m1 + 1
    
    print(f"{m1} {count} {ans}")