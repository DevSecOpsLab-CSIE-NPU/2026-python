"""
資料清理程式 — AI 簡易版（D2-easy）

功能：
    讀取多組整數數列，每組依序進行：
      1. 去除重複（保留第一次出現的順序）
      2. 只保留能被 2 整除的數
      3. 由小到大排序
    若無符合數字則輸出 NONE。

時間複雜度：O(N log N)
    - 去重：O(N)   （dict 插入與查詢平均 O(1)）
    - 篩選：O(N)
    - 排序：O(K log K)，K 為篩選後的數量，最差 K = N

空間複雜度：O(N)
    - 存放唯一值的 dict 與排序串列
"""

import sys


def main():
    """讀取 stdin，逐組處理並輸出結果。"""
    data = sys.stdin.read().strip().splitlines()
    i = 0
    while i < len(data):
        line = data[i].strip()
        if not line:
            i += 1
            continue

        n = int(line)
        if n == 0:
            break

        i += 1
        # 讀取該組所有整數
        nums = list(map(int, data[i].split()))
        i += 1

        # 1. 去除重複（dict.fromkeys 保留插入順序）
        unique = list(dict.fromkeys(nums))

        # 2. 篩選能被 2 整除的數
        evens = [x for x in unique if x % 2 == 0]

        # 3. 排序
        evens.sort()

        # 輸出
        if not evens:
            print("NONE")
        else:
            print(" ".join(map(str, evens)))


if __name__ == "__main__":
    main()
