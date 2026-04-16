"""UVA 299 - Train Swapping (easy 版)

題目重點：
1. 每筆測資給一列火車車廂順序。
2. 你只能做「相鄰兩車廂交換」。
3. 要求最少交換幾次才能排成遞增順序。

核心觀念：
- 相鄰交換最少次數 = 逆序對（inversion）數量。
- 逆序對定義：存在索引 i < j，但 cars[i] > cars[j]。
- 每消除一個逆序對，至少需要一次相鄰交換。
"""

# 第一行：測資筆數
n = int(input())

# 逐筆處理每組測資
for _ in range(n):
    # 每組第一行：車廂數量（L）
    length = int(input())

    # 每組第二行：車廂排列
    # 若 L=0，則 cars 直接設為空列表
    cars = list(map(int, input().split())) if length > 0 else []

    # 計算逆序對數量（也就是最少交換次數）
    swaps = 0

    # 雙層迴圈檢查所有 i < j 的配對
    for i in range(len(cars)):
        for j in range(i + 1, len(cars)):
            # 若前面車廂編號比後面大，代表這是一個逆序對
            if cars[i] > cars[j]:
                swaps += 1

    # 輸出需完全符合題目指定格式
    print(f"Optimal train swapping takes {swaps} swaps.")
