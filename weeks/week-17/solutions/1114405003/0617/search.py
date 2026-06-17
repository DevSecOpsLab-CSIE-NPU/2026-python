"""0617 任務二 — linear_search / binary_search

規格:
  1. linear_search: 逐一比對,回傳第一個 index,找不到回 -1
  2. binary_search: 前提 data 已排序,回傳第一個 index 或 -1
  3. 兩者不可修改傳入的 data
  4. binary_search 收到未排序 data 時照常搜尋,結果不保證(docstring 說明)
"""


def linear_search(data: list, target) -> int:
    """逐一比對,回傳 target 第一次出現的 index,找不到回 -1"""
    for i, item in enumerate(data):
        if item == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """二分搜尋,前提 data 已排序,回傳 target 第一次出現的 index 或 -1

    注意:若 data 未排序,結果不保證正確。
    """
    low, high = 0, len(data) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            result = mid
            high = mid - 1
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result
