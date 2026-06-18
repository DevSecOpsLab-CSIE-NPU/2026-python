"""search.py — 線性搜尋與二分搜尋

兩個函式都不修改傳入的 data。

binary_search 對未排序 data 的行為
────────────────────────────────
binary_search 的正確性依賴「data 已升序排序」這個前提。
若傳入未排序的 data，函式**不會拋出例外**，而是照樣執行二分邏輯。
這代表：
  - 如果 target 剛好在二分路徑上，可能回傳一個看似正確的 index；
  - 如果 target 不在二分路徑上，則回傳 -1（即使 target 實際上存在於 data 中）。
呼叫者有責任傳入已排序的資料；本函式不做排序前置檢查（避免額外 O(n) 開銷）。
"""

from __future__ import annotations


def linear_search(data: list, target) -> int:
    """逐一比對 data，回傳第一個等於 target 的 index；找不到回傳 -1。

    時間複雜度：O(n)
    空間複雜度：O(1)
    不修改傳入的 data。
    """
    for i, item in enumerate(data):
        if item == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """在**已升序排序**的 data 中用二分法找 target，回傳 index；找不到回傳 -1。

    時間複雜度：O(log n)
    空間複雜度：O(1)
    不修改傳入的 data。

    未排序行為：見模組 docstring。
    """
    lo, hi = 0, len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
