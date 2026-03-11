"""
UVA 299 — 火車車廂交換（Train Swapping）
AI 教學版本：附繁體中文註解
"""

# 讀取測資數量
n = int(input())

for _ in range(n):
    # 讀取火車長度
    l = int(input())
    # 讀取車廂排列
    arr = list(map(int, input().split()))

    swaps = 0
    # Bubble Sort：外層迴圈控制輪數
    for i in range(l):
        # 內層迴圈比較相鄰元素
        for j in range(l - 1 - i):
            # 若前面比後面大（逆序），交換並計數
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    # 輸出結果
    print(f"Optimal train swapping takes {swaps} swaps.")
