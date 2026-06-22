"""
資料清理 (Data Cleaning) — A01 詳細註解版

功能：
    讀取多組整數數列，每組依序進行：
      1. 去除重複（保留第一次出現的順序）
      2. 只保留能被 D=2 整除的數（偶數）
      3. 由小到大排序
    若無符合數字則輸出 NONE。
    當 n=0 時結束程式。

時間複雜度：O(N log N)
    - 去重：O(N)
    - 篩選：O(N)
    - 排序：O(K log K)，K 為篩選後數量，最差 K=N
空間複雜度：O(N)
"""

import sys

D = 2  # 整除參數（學號末碼 8 → 8 % 4 + 2 = 2）


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

        # 讀取該組整數
        i += 1
        nums = list(map(int, data[i].split()))
        i += 1

        # 步驟 ①：去除重複（dict 保留插入順序）
        unique = list(dict.fromkeys(nums))

        # 步驟 ②：只保留能被 D 整除的數
        filtered = [x for x in unique if x % D == 0]

        # 步驟 ③：由小到大排序
        filtered.sort()

        # 輸出
        if not filtered:
            print("NONE")
        else:
            print(" ".join(map(str, filtered)))


if __name__ == "__main__":
    main()
