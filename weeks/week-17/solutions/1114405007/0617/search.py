def linear_search(data: list, target) -> int:
    """從左到右逐一比對，回傳第一個匹配的 index，找不到回 -1。"""
    for i, value in enumerate(data):
        if value == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """在已排序（升序）的 data 中二分搜尋 target。

    前提：data 必須是升序排列。
          傳入未排序的資料會產生未定義行為，回傳值可能不正確。
    回傳：第一個匹配的 index，找不到回 -1。
    """
    left, right = 0, len(data) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            result = mid
            right = mid - 1
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
