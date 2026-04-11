"""
UVA 299 - Train Swapping (ZeroJudge e561)

解法：
  - 最少相鄰交換次數 = 陣列的「逆序數（inversion count）」
  - 逆序數：所有 i < j 且 arr[i] > arr[j] 的 (i,j) 對數量
  - L ≤ 50，O(n²) 雙層迴圈直接計算即可
"""

import sys

data = sys.stdin.read().split('\n')
idx = 0

N = int(data[idx].strip())
idx += 1

for _ in range(N):
    L = int(data[idx].strip())
    idx += 1

    if L == 0:
        print("Optimal train swapping takes 0 swaps.")
        continue

    arr = list(map(int, data[idx].strip().split()))
    idx += 1

    swaps = 0
    for i in range(L):
        for j in range(i + 1, L):
            if arr[i] > arr[j]:
                swaps += 1

    print(f"Optimal train swapping takes {swaps} swaps.")