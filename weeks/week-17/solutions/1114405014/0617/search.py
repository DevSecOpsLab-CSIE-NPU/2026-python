"""0617 任務二 — 搜尋函式實作

本檔提供兩個搜尋函式:

1. linear_search(data, target)
   - 使用線性搜尋
   - 從左到右逐一比對
   - 找到回傳 index
   - 找不到回傳 -1
   - 不修改傳入的 data

2. binary_search(data, target)
   - 使用二分搜尋
   - 前提: data 必須已經由小到大排序
   - 找到回傳 index
   - 找不到回傳 -1
   - 不修改傳入的 data

binary_search 對未排序資料的定義:
   - 本函式「不主動檢查」data 是否已排序。
   - 如果傳入未排序資料，結果不保證正確。
   - 這樣做是為了保留 binary search 的 O(log n) 搜尋特性。
"""


def linear_search(data: list, target) -> int:
    """使用線性搜尋尋找 target。

    Args:
        data: 要搜尋的 list。
        target: 要尋找的目標值。

    Returns:
        int: 找到時回傳第一個符合目標的 index，找不到回傳 -1。
    """
    for index, value in enumerate(data):
        if value == target:
            return index

    return -1


def binary_search(data: list, target) -> int:
    """使用二分搜尋尋找 target。

    前提:
        data 必須已經由小到大排序。

    未排序資料行為:
        本函式不主動檢查 data 是否排序。
        若傳入未排序 data，搜尋結果不保證正確。

    Args:
        data: 已排序的 list。
        target: 要尋找的目標值。

    Returns:
        int: 找到時回傳 target 的 index，找不到回傳 -1。
    """
    left = 0
    right = len(data) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_value = data[middle]

        if middle_value == target:
            return middle

        if middle_value < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1