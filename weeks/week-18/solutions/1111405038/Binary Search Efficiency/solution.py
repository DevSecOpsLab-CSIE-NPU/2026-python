"""
解題檔：二分搜尋效能（Binary Search Efficiency）- 第四題

提供線性搜尋與二分搜尋的實作，並統計比較次數。
"""


def linear_search(arr, target):
    """線性搜尋：回傳 (found, idx, cmp)"""
    cmp = 0
    for idx, value in enumerate(arr):
        cmp += 1
        if value == target:
            return True, idx, cmp
    return False, -1, cmp


def binary_search(arr, target):
    """二分搜尋：回傳 (found, idx, cmp)"""
    left = 0
    right = len(arr) - 1
    cmp = 0

    while left <= right:
        mid = (left + right) // 2
        cmp += 1

        if arr[mid] == target:
            return True, mid, cmp
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False, -1, cmp


if __name__ == "__main__":
    pass
