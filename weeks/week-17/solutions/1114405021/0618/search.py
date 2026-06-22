def linear_search(data: list, target) -> int:
    """從左到右逐一比對目標，返回找到的索引；找不到回 -1"""
    for i, val in enumerate(data):
        if val == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """
    二分搜尋。

    前提：data 已經升冪排序。
    如果傳入未排序的 data，行為定義為回傳 -1（不嘗試排序）。
    返回值：找到的索引，找不到回 -1。
    """
    # 檢查是否已排序（簡易實現：與排序後版本比較）
    sorted_data = sorted(data)
    if data != sorted_data:
        return -1

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


def set_search(data: list, target) -> bool:
    """用 set / hash 檢查目標是否存在，返回 True / False"""
    data_set = set()
    for item in data:
        data_set.add(item)
    return target in data_set
