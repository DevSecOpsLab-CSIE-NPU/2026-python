import sys

# 讀取測試資料組數
t = int(sys.stdin.readline())

for _ in range(t):

    # 讀取車廂數量
    n = int(sys.stdin.readline())

    # 讀取每節車廂的編號
    arr = list(map(int, sys.stdin.readline().split()))

    # 記錄交換次數
    swaps = 0

    # 使用最簡單的氣泡排序
    # 每次遇到前一個比後一個大就交換
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    # 輸出需要交換的次數
    print("Optimal train swapping takes", swaps, "swaps.")