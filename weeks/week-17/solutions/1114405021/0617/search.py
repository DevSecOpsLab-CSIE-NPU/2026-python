def linear_search(data: list, target) -> int:
    """逐一比對 data 中的每個元素。

    回傳第一個等於 target 的 index，找不到回傳 -1。
    """
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """二元搜尋，前提 data 已由小到大排序。

    若 data 未排序，回傳值無定義（可能找不到或找到錯誤 index）。
    回傳 target 的 index，找不到回傳 -1。
    """
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
